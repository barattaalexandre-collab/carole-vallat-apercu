# HANDOFF — Refonte site Carole Vallat
> Document de reprise complet. À lire en entier avant de continuer (autre chat / autre session). Date : 24/06/2026.
> Dossier maître : `~/Downloads/Refonte Site Carole Vallat/`. Mémoire persistante : `project_carole_vallat_site.md`.

---

## 0. TL;DR — où on en est
- **Tout l'amont est fait** : stratégie, benchmark, direction artistique, architecture, **textes finaux**, offres, tarifs, freebie.
- **Le build a démarré** : thème WordPress blocs sur-mesure scaffoldé, **l'accueil tourne en local et est on-brand** (testé sur WordPress Playground).
- **Reste** : décliner les autres pages dans le thème, récupérer photos + vrais témoignages, déployer sur Infomaniak.

---

## 1. Le projet
- **Cliente :** Carole Vallat — **Studio Soham**, Le Landeron (canton Neuchâtel, Suisse romande).
- **Pour :** Alexandre Baratta (studio **LPL / Les Précurseurs Lab**). **C'est le site vitrine de référence d'Alexandre** → doit être exceptionnel (génère ses futures opportunités).
- **Domaine :** `carolevallat.ch` (actuellement sous **Showit**, à quitter). `carolevalla.ch` n'existe pas.
- **Cible :** femmes 40+, péri/ménopause, Entre-deux-Lacs (Le Landeron, La Neuveville, Cressier, Neuchâtel, Bienne).

## 2. Positionnement (VALIDÉ par Carole)
**Mouvement-first**, 3 niveaux : **(1) Le mouvement** (principal) → **(2) L'accompagnement ménopause** → **(3) La réflexologie**.
- **Accueil = 2 univers** : « Le studio » (mouvement) + « L'accompagnement » (ménopause). **La réflexologie n'est PAS sur l'accueil** (page à part).
- **Ton :** incarné, **tutoiement**, simple, langage du corps & du ressenti. Pas de minceur culpabilisant, pas de jargon, pas de copier-coller des templates Menopulse.
- **Signature :** « Passe de spectatrice à actrice de ta ménopause. »
- **CTA principal :** « Je réserve mon appel offert » + « M'écrire sur WhatsApp ».

## 3. Stack technique (VERROUILLÉE)
- **WordPress — thème blocs (FSE) SUR-MESURE** (Claude code & modifie ; Carole édite le contenu visuellement).
- **Hébergement : Infomaniak** (Genève, données suisses), WordPress managé.
- **Réservation : SimplyBook.me** embarqué (cours + appel découverte + réflexo) → remplace MomoYoga.
- **Paiement : Stripe → TWINT.**
- **Rejetés (ne pas y revenir) :** Framer (GUI non pilotable par Claude), Astro (perd l'édition autonome), Lovable/SPA (SEO pourri).
- **Newsletter/freebie :** Brevo ou MailerLite (double opt-in nLPD).
- **SEO :** RankMath. **GEO/SEO via HTML rendu serveur** = avantage WordPress.

## 4. Faits & données CONFIRMÉS (tous validés)
**Offres ménopause (officiel, `05/Offres-Menopause_OFFICIEL.md`) :**
- **Programme en ligne — 200 CHF** (vidéos + cohorte 2 sem + 5 visios, **8 semaines**, visio)
- **Accompagnement 1:1 — 650 CHF** (bilan 90 min + 4×45 min, sur-mesure, **5 mois**, au studio + visio)
- **Coaching Premium — 800 CHF** (les deux combinés)
- Piliers : nutrition, compléments, stress, sommeil, mouvement, renforcement, cardio, mobilité, plancher pelvien.

**Cours (studio) + tarifs (MomoYoga) :**
- Cours : **Pilates** (groupe), **Yin Yoga**, **Pilates sur appareils** (reformer, Cadillac, Wunda Chair, Spine Corrector) en **privé/duo/trio**, **Yoga aérien**. + **Menovibe** = nouveau cours collectif rentrée (Pilates+cardio doux+renforcement, péri/ménopause, 8 max). *(dates à venir)*
- Tarifs carnets (CHF) : groupe 10×=**300** · privé/SOLO 10×=**1050** · DUO=**580** · TRIO=**450** · abos 40/12mois=1000, 20/20sem=500, 20/6mois=550, 10/10sem=275.
- Planning type : Lun 8h45/10h/12h30/17h/18h · Mar 9h/10h15/17h45 · Mer 8h20/10h35 · Jeu 17h45/19h · Ven 9h/10h.

**Réflexologie :** **1 heure · 120 CHF** · protocole chinois · **Agréée ASCA → remboursable par les complémentaires** (ASCA = OUI, à afficher).

**Bio/parcours :** ex-**designer horlogère de luxe** (15+ ans) → diplôme **Pilates Montréal 2010** → **studio fondé 2017** au Landeron (⚠️ PAS 2010) → accompagnement depuis 2015. A vécu elle-même la ménopause.

**Formations (pour À propos) :** Pilates Ann Mac Millan (2010), Personal Training (2011), Mentorat Fascia (2016) · Yin & Médecine chinoise (2016-18), BioIntegrityYoga (2021-22), Inside Flow (2023), Yoga Nidra (2023), Yoga Balle (2023), Yoga Aérien Fly Yoga (2024) · Coach Ménopause (2025), L'Ère du Souffle (2025) · Réflexologie Plantaire Chinoise (2018), Adaptive Bodywork (2019), Heart and Bones (2021) · **Agréée ASCA**.

**NAP :** Studio Soham — Carole Vallat · Ville 1, 2525 Le Landeron · +41 78 924 24 82 · info@carolevallat.ch · Instagram + Facebook.

**Freebie :** « **Ménopause Glow** » (PDF 11 p. existant, `05/Freebie_Menopause-Glow.pdf`) = lead magnet, à utiliser tel quel (palette jaune Canva à harmoniser plus tard).

## 5. Direction artistique (tokens — dans le theme.json)
- **Palette :** Ivoire `#F7F2EA` (fond) · Encre terre `#2B211A` (texte) · Terracotta `#9C5A3C` (accent/CTA) · Argile `#D4A78A` · Sauge `#5E6B4D` · Sable `#EFE7D8` · Lin `#E5DCC9` · Taupe `#7A6B5D`.
- **Typo :** **Fraunces** (titres, serif) + **Inter** (corps) — **self-hostées** (woff2 dans `assets/fonts/`, RGPD/nLPD, PAS Google CDN).
- **Style :** premium éditorial chaud, sobriété, grandes photos réelles, négatif généreux, une idée par écran, bouton radius 2px, easing `cubic-bezier(0.16,1,0.3,1)`.
- **À FUIR :** WebGL lourd, Lenis smooth-scroll, curseur custom, React/SPA, palette froide/magenta/jaune criard.
- **Réfs (vérifiées) :** The Class, Forma Pilates, JOIA (Neuchâtel), Heartcore (= WP rapide), Pvolve (positionnement). **Modèle de complétude de Carole = menostudio.fr** (coach Ménopulse, « elle veut ça + le studio en plus »). **Réf de ton = healthyrootswithlaurene.com.**

## 6. Structure des dossiers (tout est rangé ici)
```
Refonte Site Carole Vallat/
├── _HANDOFF.md  ← CE FICHIER · _LISEZ-MOI.md
├── 00 - Brief & Directives/        brief_refonte_v2.pdf
├── 01 - Strategie & Positionnement/ Carole-Vallat-Dossier-Strategique.(html|pdf)
├── 02 - Direction artistique & Contenu/
│     ├── carolevallat_direction_artistique_v2.md   (DA technique — tokens)
│     ├── Carole-Vallat_Direction-Artistique_Presentation.(html|pdf)  (DA cliente, 19 p.)
│     ├── Architecture-v2_validee-Carole.md
│     ├── Trames-de-redaction_pages.md   (structure + SEO par page)
│     ├── Textes-finaux_pages_v1.md   ← *** LES TEXTES FINAUX DES 8 PAGES ***
│     ├── carolevallat_wireframes.md
│     └── presentation-assets/  (images de la DA cliente)
├── 03 - Recherche & Benchmark/   Recherche-A/B/C (studios, tier mondial+techno, message)
├── 04 - Inspiration & Moodboard/  moodboards + Captures/ + References Alexandre/ + References-Carole_*.md
├── 05 - Contenu source Carole/
│     ├── Carole_PageAccueil_texte-COMPLET.md  (son texte d'accueil)
│     ├── Offres-Menopause_OFFICIEL.md  (200/650/800)
│     ├── Freebie_Menopause-Glow.pdf
│     ├── Comparatif-Offres-Menopause.pdf + .pages
│     └── Formation Menopulse (Drive Carole)/  (templates génériques — NE PAS copier ; légal = France inutilisable)
├── 06 - Build WordPress/
│     ├── README_build.md   ← *** SETUP COMPLET DU BUILD ***
│     ├── blueprint.json    (Playground : active le thème)
│     └── carole-vallat-theme/  ← LE THÈME
│           ├── theme.json (design system), style.css, functions.php
│           ├── templates/ (front-page.html = ACCUEIL, index.html, page.html)
│           ├── parts/ (header.html, footer.html)
│           ├── patterns/  (vide — à remplir)
│           └── assets/ (fonts/*.woff2 ✓, js/motion.js, css/editor.css)
└── 07 - Prospection & Comms/
```
**⚠️ Distinct :** le SaaS « MenoCoach / app ménopause » (`~/Downloads/meno/`, `HANDOFF-menopause-design.md`) = AUTRE projet, ne pas mélanger.

## 7. État du build
- **Thème scaffoldé et FONCTIONNEL** : `theme.json` (palette+typo+espacement), `front-page.html` (accueil complet avec les vrais textes), header/footer, motion.js.
- **Testé en local sur WordPress Playground** → accueil rend correctement, on-brand (ivoire, Fraunces, terracotta, sable, double CTA). 0 erreur PHP.
- **Polices self-hostées OK** (Fraunces + Inter dans assets/fonts/).

**Relancer le WP local (PHP-wasm, ni Docker ni PHP requis, juste Node) :**
```bash
cd "$HOME/Downloads/Refonte Site Carole Vallat/06 - Build WordPress"
npx --yes @wp-playground/cli@latest server --port=9400 \
  --mount=./carole-vallat-theme:/wordpress/wp-content/themes/carole-vallat-theme \
  --blueprint=./blueprint.json
# → http://127.0.0.1:9400  (auto-login admin ; warnings EBADF php-wasm = non bloquants)
```

## 8. CE QUI RESTE À FAIRE (ordonné)
1. **Décliner les autres pages** dans le thème (templates + patterns), à partir de `02/Textes-finaux_pages_v1.md` : Le studio · L'accompagnement (tableau 200/650/800) · Réflexologie · Ma méthode · À propos (formations) · Réserver · FAQ · Journal.
2. **Photos** : les récupérer depuis carolevallat.ch (Showit charge en CSS/JS → besoin d'inspection réseau navigateur, ou Carole fournit les fichiers). Crédit photo : « Caroline Raemi ».
3. **Polish accueil** : titre du site → « Carole Vallat » ; affiner la taille du H1 hero ; intégrer la photo hero.
4. **Plugins** : RankMath (SEO/schema), Performance Lab Image Placeholders (+AVIF, confirmer Imagick Infomaniak), Brevo/MailerLite (freebie).
5. **Intégrations** : SimplyBook (réservation), Stripe/TWINT, formulaire freebie → envoi « Ménopause Glow ».
6. **SEO** : schema LocalBusiness/Service/Person, **pages géo** (Le Landeron, La Neuveville, Cressier, Neuchâtel, Bienne), **nettoyer NAP** (domaine mort `sohombilatesyoga.com`/ville « Cornaux » → 301), optimiser GBP.
7. **Déploiement Infomaniak** + perf (cibles : Lighthouse mobile ≥95, LCP<2,5s, INP<200ms, CLS<0,1, accueil<1Mo).

## 9. En attente de Carole (mini-liste)
1. **Photos** (séance pro / de son site) · 2. **Vrais témoignages** + accord (Videoask — actuellement `[FICTIF]` dans les textes) · 3. **« Plus personnel »** de la page À propos · 4. **Dates Menovibe**.

## 10. Gotchas / corrections à NE PAS oublier
- **Studio fondé 2017** (pas 2010).
- **Prix ménopause = 200/650/800** (PAS 390/650/990 que j'avais supposés au début).
- **Menovibe** (singulier) = nom validé du cours rentrée.
- **ASCA = OUI** → afficher « remboursable ».
- **Réflexo = 1h / 120 CHF.**
- **Témoignages actuels = FICTIFS** (marqués `[FICTIF]`), à remplacer.
- Le kit « Formation Menopulse » du Drive = **templates génériques à NE PAS copier** (Google déclasse) ; ses docs **légaux = France, inutilisables** (faire du **suisse/nLPD**).
- Freebie « Ménopause Glow » = palette jaune Canva ≠ terracotta du site (harmoniser plus tard).

## 11. Comment reprendre dans le nouveau chat
1. Lire ce `_HANDOFF.md` + la mémoire `project_carole_vallat_site.md` (chargée auto).
2. Fichiers prioritaires : `02/Textes-finaux_pages_v1.md` (contenu), `06/README_build.md` (build), `06/carole-vallat-theme/` (le code).
3. Relancer le WP local (§7) pour voir l'état.
4. Continuer par : **décliner les autres pages** (§8.1).
