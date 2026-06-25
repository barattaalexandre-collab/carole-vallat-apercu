from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

from PIL import Image, ImageOps
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

ROOT = Path.cwd()
ZIP_PATH = ROOT / "carole-vallat-assets.zip"
EXTRACT_DIR = ROOT / "_audit_assets"
TEMP_DIR = ROOT / "_audit_tmp"
OUTPUT_DIR = ROOT / "audit-artifact"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
GROUP_NAMES = {"references", "apercu-captures", "photos-carole"}


def reset_dirs() -> None:
    shutil.rmtree(EXTRACT_DIR, ignore_errors=True)
    shutil.rmtree(TEMP_DIR, ignore_errors=True)
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    EXTRACT_DIR.mkdir(parents=True)
    TEMP_DIR.mkdir(parents=True)
    OUTPUT_DIR.mkdir(parents=True)


def extract_assets() -> list[Path]:
    if not ZIP_PATH.exists():
        raise FileNotFoundError(f"Missing {ZIP_PATH}")
    with zipfile.ZipFile(ZIP_PATH) as archive:
        archive.extractall(EXTRACT_DIR)
    files = sorted(
        path
        for path in EXTRACT_DIR.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )
    if not files:
        raise RuntimeError("No images found in the asset archive")
    return files


def relative_name(path: Path) -> str:
    return path.relative_to(EXTRACT_DIR).as_posix()


def group_for(path: Path) -> str:
    for part in path.relative_to(EXTRACT_DIR).parts:
        if part in GROUP_NAMES:
            return part
    return "other"


def open_rgb(path: Path) -> Image.Image:
    image = ImageOps.exif_transpose(Image.open(path))
    if image.mode in ("RGBA", "LA"):
        background = Image.new("RGB", image.size, "white")
        background.paste(image, mask=image.getchannel("A"))
        image.close()
        return background
    return image.convert("RGB")


def make_temp_jpeg(image: Image.Image, name: str, max_width: int, max_height: int) -> Path:
    copy = image.copy()
    copy.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
    destination = TEMP_DIR / f"{name}.jpg"
    copy.save(destination, "JPEG", quality=88, optimize=True, progressive=True)
    copy.close()
    return destination


def draw_background(pdf: canvas.Canvas, width: float, height: float) -> None:
    pdf.setFillColorRGB(0.945, 0.935, 0.91)
    pdf.rect(0, 0, width, height, stroke=0, fill=1)


def draw_header(pdf: canvas.Canvas, title: str, width: float, height: float, dark: bool = False) -> float:
    bar_height = 44
    if dark:
        pdf.setFillColorRGB(0.09, 0.08, 0.07)
        text_color = (1, 1, 1)
    else:
        pdf.setFillColorRGB(0.98, 0.975, 0.96)
        text_color = (0.13, 0.11, 0.09)
    pdf.rect(0, height - bar_height, width, bar_height, stroke=0, fill=1)
    pdf.setFillColorRGB(*text_color)
    pdf.setFont("Helvetica-Bold", 13)
    display = title if len(title) <= 132 else title[:129] + "..."
    pdf.drawString(18, height - 28, display)
    return bar_height


def draw_image_fit(
    pdf: canvas.Canvas,
    image_path: Path,
    x: float,
    y: float,
    box_width: float,
    box_height: float,
) -> None:
    with Image.open(image_path) as image:
        image_width, image_height = image.size
    scale = min(box_width / image_width, box_height / image_height)
    width = image_width * scale
    height = image_height * scale
    pdf.drawImage(
        ImageReader(str(image_path)),
        x + (box_width - width) / 2,
        y + (box_height - height) / 2,
        width=width,
        height=height,
        preserveAspectRatio=True,
        mask="auto",
    )


def write_manifest(files: list[Path]) -> None:
    lines: list[str] = []
    for group in ("apercu-captures", "references", "photos-carole", "other"):
        items = [path for path in files if group_for(path) == group]
        if not items:
            continue
        lines.append(f"[{group}] ({len(items)})")
        for path in items:
            with Image.open(path) as image:
                lines.append(
                    f"{relative_name(path)}\t{image.width}x{image.height}\t{path.stat().st_size} bytes"
                )
        lines.append("")
    (OUTPUT_DIR / "00-manifest.txt").write_text("\n".join(lines), encoding="utf-8")


def build_overview(files: list[Path]) -> None:
    destination = OUTPUT_DIR / "01-all-assets-overview.pdf"
    pdf = canvas.Canvas(str(destination), pagesize=(1200, 900), pageCompression=1)
    ordered: list[Path] = []
    for group in ("apercu-captures", "references", "photos-carole", "other"):
        ordered.extend(path for path in files if group_for(path) == group)

    cells = ((20, 450, 570, 390), (610, 450, 570, 390), (20, 30, 570, 390), (610, 30, 570, 390))
    for offset in range(0, len(ordered), 4):
        pdf.setPageSize((1200, 900))
        draw_background(pdf, 1200, 900)
        pdf.setFillColorRGB(0.11, 0.095, 0.08)
        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(22, 867, f"Carole Vallat — visual inventory — page {offset // 4 + 1}")
        for local_index, (path, cell) in enumerate(zip(ordered[offset : offset + 4], cells)):
            x, y, width, height = cell
            pdf.setFillColorRGB(1, 1, 1)
            pdf.roundRect(x, y, width, height, 8, stroke=0, fill=1)
            pdf.setFillColorRGB(0.13, 0.11, 0.09)
            pdf.setFont("Helvetica-Bold", 10)
            pdf.drawString(x + 12, y + height - 21, relative_name(path)[:88])
            image = open_rgb(path)
            temporary = make_temp_jpeg(image, f"overview-{offset + local_index:04d}", 1150, 720)
            image.close()
            draw_image_fit(pdf, temporary, x + 12, y + 10, width - 24, height - 43)
        pdf.showPage()
    pdf.save()


def build_single_page_pdf(paths: list[Path], filename: str) -> None:
    destination = OUTPUT_DIR / filename
    pdf = canvas.Canvas(str(destination), pageCompression=1)
    for index, path in enumerate(paths):
        image = open_rgb(path)
        portrait = image.height > image.width * 1.2
        page_width, page_height = ((760, 1180) if portrait else (1200, 900))
        pdf.setPageSize((page_width, page_height))
        draw_background(pdf, page_width, page_height)
        header = draw_header(pdf, relative_name(path), page_width, page_height)
        temporary = make_temp_jpeg(image, f"single-{filename}-{index:04d}", 2400, 3000)
        image.close()
        draw_image_fit(pdf, temporary, 18, 18, page_width - 36, page_height - header - 30)
        pdf.showPage()
    pdf.save()


def build_preview_detail(paths: list[Path]) -> None:
    destination = OUTPUT_DIR / "02-current-previews-detail.pdf"
    pdf = canvas.Canvas(str(destination), pageCompression=1)
    temp_counter = 0
    for path in paths:
        image = open_rgb(path)
        portrait = image.height > image.width * 1.2
        page_width, page_height = ((760, 1180) if portrait else (1200, 900))
        pdf.setPageSize((page_width, page_height))
        draw_background(pdf, page_width, page_height)
        header = draw_header(pdf, relative_name(path), page_width, page_height)
        temporary = make_temp_jpeg(image, f"preview-full-{temp_counter:04d}", 2400, 3200)
        temp_counter += 1
        draw_image_fit(pdf, temporary, 18, 18, page_width - 36, page_height - header - 30)
        pdf.showPage()

        if image.height > image.width * 1.3:
            chunk_height = int(image.width * (2.08 if image.width < 700 else 0.68))
            chunk_height = max(500, min(chunk_height, image.height))
            overlap = int(chunk_height * 0.06)
            step = max(1, chunk_height - overlap)
            starts = list(range(0, max(1, image.height - chunk_height + 1), step))
            final_start = max(0, image.height - chunk_height)
            if not starts or starts[-1] != final_start:
                starts.append(final_start)
            for slice_index, top in enumerate(starts, start=1):
                crop = image.crop((0, top, image.width, min(image.height, top + chunk_height)))
                slice_width, slice_height = ((760, 1180) if image.width < 700 else (1200, 900))
                pdf.setPageSize((slice_width, slice_height))
                draw_background(pdf, slice_width, slice_height)
                header = draw_header(
                    pdf,
                    f"{relative_name(path)} — slice {slice_index}/{len(starts)}",
                    slice_width,
                    slice_height,
                    dark=True,
                )
                temporary = make_temp_jpeg(crop, f"preview-slice-{temp_counter:04d}", 2600, 2600)
                temp_counter += 1
                crop.close()
                draw_image_fit(pdf, temporary, 12, 12, slice_width - 24, slice_height - header - 22)
                pdf.showPage()
        image.close()
    pdf.save()


def main() -> None:
    reset_dirs()
    files = extract_assets()
    write_manifest(files)
    build_overview(files)
    previews = [path for path in files if group_for(path) == "apercu-captures"]
    references = [path for path in files if group_for(path) == "references"]
    photos = [path for path in files if group_for(path) == "photos-carole"]
    build_preview_detail(previews)
    build_single_page_pdf(references, "03-reference-library.pdf")
    build_single_page_pdf(photos, "04-carole-photos.pdf")
    print(
        f"Rendered {len(files)} images: {len(previews)} previews, "
        f"{len(references)} references, {len(photos)} Carole photos"
    )


if __name__ == "__main__":
    main()
