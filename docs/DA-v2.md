# Carole Vallat — Direction artistique V2
### Build-ready · supersède la v1 · intègre la revue critique (recherches A+B, stack WordPress)

> **Objectif :** un site **incarné, féminin, premium, éditorial**. Zéro template wellness générique, zéro effet « généré par IA ». Étoiles polaires (vérifiées) : **The Class** + **Forma Pilates** (serif + neutres chauds + photo de mouvement réelle + négatif), **JOIA** (architecture suisse), **The Gentlewoman / Cereal** (éditorial). Identité propre à Carole : terre, argile, terracotta, intériorité, Suisse romande.
>
> **Stack cible :** thème blocs **WordPress** (FSE) · hébergement **Infomaniak (CH)** · réservation **SimplyBook.me** embarquée · **Stripe→TWINT**. *(La v1 supposait Astro/Calendly — corrigé partout.)*

---

## 1. Principes directeurs

1. **L'espace avant la décoration** — marges généreuses, sections jamais surchargées, une idée par écran.
2. **Le mot avant l'image** — le copywriting pilote, l'image illustre. Jamais d'image « pour remplir ».
3. **Le vrai avant le joli** — uniquement des photos de Carole, dans son vrai studio. Aucune stock, aucun visuel générique.
4. **Le silence avant l'effet — mais UN moment signature autorisé.** Animations discrètes par défaut ; **un seul** moment mémorable (titre hero) toléré. Pas de parallax excessif, pas de reveal tape-à-l'œil partout.
5. **La lisibilité avant le style** — contraste suffisant, taille de texte confortable, hiérarchie claire.
6. **La vitesse fait partie du premium** — chaque effet se justifie contre le budget performance (§12). Un site lent n'est jamais premium.

---

## 2. Palette de couleurs

Terre cuite, sable suisse, argile, lin écru. Chaude, apaisante, féminine sans cliché. *(Confirmée par les captures réelles : Forma = bois/crème, The Class = taupe/sable.)*

### Principales
| Rôle | Nom | Hex | Usage |
|---|---|---|---|
| Fond principal | Ivoire chaud | `#F7F2EA` | Fond de toutes les pages (≠ blanc pur) |
| Texte principal | Encre terre | `#2B211A` | Corps, titres (≠ noir pur) |
| Accent primaire | Terracotta profond | `#9C5A3C` | CTA principaux, liens, accents H1 |
| Accent secondaire | Argile rose | `#D4A78A` | Hover, séparateurs, détails |
| Vert végétal | Sauge profonde | `#5E6B4D` | Touches nature, pilier nature, badges |

### Support
| Rôle | Nom | Hex |
|---|---|---|
| Fond alternatif | Sable clair | `#EFE7D8` |
| Bordures douces | Lin | `#E5DCC9` |
| Texte secondaire | Taupe | `#7A6B5D` |
| Succès / info | Olive douce | `#8B9065` |

**On évite :** noir pur `#000` · blanc pur `#FFF` · gradients violet/bleu (tech IA) · rose poudré générique (wellness cliché) · or/cuivre métallisé (influenceuse Instagram).

**Contrastes vérifiés (WCAG AA) :** Encre/Ivoire = 12,8:1 ✅ · Terracotta/Ivoire = 5,2:1 ✅.

---

## 3. Typographie

Combo serif éditorial expressif + sans contemporain. **Validé par les meilleurs du monde** (The Class, Pvolve, Forma = serif titres + sans corps).

- **Titres — Fraunces** (variable). H1, H2, sections, hero. Poids 300/500/700. `"opsz" 144` sur les très gros titres.
- **Corps — Inter** (variable). Paragraphes, nav, boutons, formulaires. Poids 400/500/600.
- *Alternatives premium si besoin : Editorial New / Söhne (payantes) ; Cormorant Garamond (gratuite, + classique).*

### 🔧 Règle technique critique — self-host, PAS le CDN Google Fonts
Le jugement de Munich (2022) : charger Google Fonts depuis le CDN de Google = **violation RGPD** (fuite l'IP visiteur) ; nLPD suisse alignée. Pour une praticienne **ménopause suisse** = risque légal + confiance. Donc :
- **Self-host les woff2** sur Infomaniak (même Fraunces/Inter, juste hébergées chez nous).
- **Variable fonts** (un fichier, tous poids) + **subset latin-français** (`é è ê à â ç î ô û œ ` + ponctuation) → −50 à −80 % de poids.
- **`preload`** la/les 1-2 polices du LCP uniquement.
- **`font-display: optional`** + fallback `size-adjust`/`ascent-override` pour **zéro shift** (CLS).

### Hiérarchie
```
H1 (Hero)    → Fraunces 300, 64-88px, lh 1.05, ls -0.02em
H2 (Section) → Fraunces 400, 40-56px, lh 1.15, ls -0.01em
H3 (Sub)     → Fraunces 500, 28-32px, lh 1.2
H4           → Inter 600, 20px, lh 1.3, uppercase, ls 0.08em
Corps        → Inter 400, 17-18px, lh 1.65
Petit        → Inter 400, 14px, lh 1.5
Meta/label   → Inter 500, 13px, uppercase, ls 0.1em
```
**Règles :** ligne max 65 caractères (corps) · marges verticales 96-128px desktop / 64-80px mobile · alignement à gauche uniquement · italiques pour citations/mises en valeur subtiles, pas pour décorer.

---

## 4. Direction photo *(le point le plus critique — 80 % de l'impression)*

⚠️ **Dépendance n°1 du projet :** tout repose sur de vraies photos de Carole. **À verrouiller avec elle en priorité** (sans shooting pro, le niveau visé est inatteignable).

**Ambiance :** lumière naturelle uniquement · heure dorée · tons chauds (terre/sable/lin) · grain doux léger · profondeur de champ marquée.

**Photos nécessaires :**
| # | Type | Usage | Qté |
|---|---|---|---|
| 1 | Portrait Carole, plan moyen, regard caméra, calme incarné | Hero accueil, à propos | 2-3 |
| 2 | Portrait Carole, regard ailleurs, contemplation | Hero ménopause / à propos alt | 2 |
| 3 | Carole en mouvement (yoga, pilates, pas figé) | Page mouvement, témoignages | 5-6 |
| 4 | Détails : mains, pieds, hamac, reformer, matériel | Interstitiels d'ambiance | 6-8 |
| 5 | Studio Soham vide, lumière naturelle | Localisation, page mouvement | 3-4 |
| 6 | Réflexologie (pieds, mains, setup) | Page réflexologie | 3-4 |
| 7 | Nature / campagne neuchâteloise | Transitions, page ménopause | 3-4 |

**Cadrage :** formats variés (1:1, 3:4, 16:9, 21:9) · compositions asymétriques · gestes naturels (respirer, pas poser) · espace négatif généreux.

**On évite :** stock (même belles) · poses figées catalogue · filtres Instagram saturés · fond blanc studio · mains-qui-tiennent-un-thé · pieds-dans-l'herbe-vus-d'en-haut · cœurs/mandalas/namaste.

---

## 5. Références (mood board mis à jour)

**Studios — cible chaude premium :**
1. **The Class** · theclass.com — étoile polaire : serif éditorial + mouvement réel + page « Méthode ».
2. **Forma Pilates** · formapilates.co — la palette earthy (bois/crème/terracotta) + retenue + négatif.
3. **JOIA** · joia-studio.com — réf n°1, même canton : géo-SEO + booking bSport + hero une-phrase.
4. **Heartcore** · weareheartcore.com — preuve que premium = WordPress rapide (Kinsta low-carbon).
5. **Pvolve** · pvolve.com — positionnement ménopause/étapes-de-vie + quiz. *(visuel sombre/promo : NE PAS copier.)*
6. **Forme** · forme.fitness — géo en H1 + page « Qu'est-ce que… ».

**Éditorial / typo :** The Gentlewoman, Cereal, Kinfolk, Sunday Forever.
**Photo (mood seulement) :** Yoann « Melo » Guerini *(photographe, PAS un studio)*, Sarah Moon, Dirk Braeckman, Vilhelm Hammershøi.
**Matières :** céramiques suisses (argile/grès/raku), lin froissé, coton bio.

---

## 6. Composants UI

**Boutons**
- *Primaire :* fond Terracotta `#9C5A3C`, texte Ivoire, Inter 500 16px ls 0.02em, padding `18px 32px`, radius `2px`, hover −8 % + shift −1px, transition 300ms `var(--ease-out-expo)`.
- *Secondaire :* lien souligné, underline 1px offset 4px, hover underline Terracotta.
- *Tertiaire (ghost) :* bordure 1px Encre, fond transparent, hover fond Sable.

**Cards :** fond Sable `#EFE7D8`, radius `4px`, padding `40px`, shadow nulle (ou `0 1px 2px rgba(43,33,26,.04)`), hover shift −2px + bordure Terracotta 1px optionnelle.

**Séparateurs :** filet 1px Lin · ou `*`/`•` centré · ou simplement l'espace + changement de fond.

**Formulaires :** input fond Ivoire, bordure basse 1px Taupe, label Inter 500 13px uppercase au-dessus (fixe, pas flottant) ; focus bordure basse Terracotta 2px ; erreur rouge brique `#A04545`.

**Navigation :** desktop = logo gauche, liens centre, CTA « Réserver » (primaire) droite ; sticky fond Ivoire translucide + backdrop-blur 8px ; active = underline fin ; mobile = hamburger, ouverture en fade.

---

## 7. Layout & grille

- **12 colonnes** desktop, gutter `24px` · container max `1280px` · marges latérales `32px` desktop / `20px` mobile.
- **Texte long** contraint à max-width `680px`.
- **Breakpoints :** Mobile 0-639 · Tablet 640-1023 · Desktop 1024-1439 · Large 1440+.
- **Rythme vertical :** hero `min-height: 92vh` · sections 128px desktop / 80px mobile · entre éléments 48/32px · entre paragraphes 24px.

---

## 8. Animations & micro-interactions *(upgradé)*

**Règle d'or :** si une animation n'apporte pas clarté ou émotion juste, on l'enlève. Construire d'abord le chemin **reduced-motion**, superposer le motion en enhancement.

### Easing (token unique)
`--ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1)` — réutilisé partout, ~400-700ms. **Plus grand levier de qualité perçue, coût nul.**

### Adopté (quasi gratuit, SEO-safe)
- **Fade-in + translate-up** (opacité 0→1, +16px) à l'apparition.
- **Reveals CSS scroll-driven** (`animation-timeline: view()`) — hors main thread, **sans JS**, derrière `@supports`, fallback statique. *(Préféré à Motion One pour les reveals.)*
- **View Transitions cross-document** (`@view-transition { navigation: auto }` + `view-transition-name` sur hero/logo) — **effet SPA sur WordPress PHP**, ≤300ms, dégrade proprement.
- **Hover bouton** (couleur 300ms) · **hover image** (zoom 1.02x en 800ms) · **nav sticky** en fade.
- **1 CTA magnétique** sur le bouton de conversion principal (~30 lignes vanilla JS, off tactile + reduced-motion).

### Le moment signature (UN seul)
**Titre hero homepage en GSAP SplitText** (révélation ligne/mot), `defer`, homepage uniquement, reduced-motion gated, ~50 Ko sur 1 page. GSAP est **gratuit depuis avril 2025**. *Un moment, pas dix.*

### Refusé (la v1 avait raison — confirmé par la recherche)
❌ WebGL / Three.js / R3F / Spline ❌ Lenis / smooth-scroll global *(menace l'INP + hostile vestibulaire = mauvais pour audience ménopause)* ❌ curseur custom ❌ scroll-snap / scroll-jacking ❌ vidéo background lourde en hero ❌ front React / Framer Motion.

---

## 9. Accessibilité *(renforcé)*

- **Contraste AA** sur tout texte (4.5:1) — vérifié §2.
- **Taille corps min 16px.**
- **`prefers-reduced-motion`** = interrupteur maître autour de **chaque** animation. **Doublement critique** : audience ménopause/plus âgée = sensibilité vestibulaire fréquente. Ici, l'a11y EST une part du premium (et l'EAA EU 2025 augmente l'exposition légale).
- **`:focus-visible`** ring Terracotta 2px offset · navigation clavier complète · skip-link · ne pas laisser le JS avaler ancres/tab.
- **Alt text** utile sur toute image informative, `alt=""` sur décoratif · un seul H1/page · pas de niveaux sautés.

---

## 10. Système d'icônes

**Lucide** (1.5px stroke, fin, gratuit, open source) en SVG inline. Taille défaut 20px, couleur héritée. Pour social, flèches, check, téléphone, email, localisation. Pas d'emoji, pas de bitmap.

---

## 11. 🆕 Pipeline image *(absent de la v1)*

- **AVIF/WebP** — WP core 6.5+ génère l'AVIF nativement *si Imagick/GD le supporte* (→ **1 email à Infomaniak pour confirmer**). Sinon WebP.
- **`srcset`/`sizes` responsive** — WP core automatique, ne pas réinventer.
- **Placeholder couleur dominante** — plugin **Performance Lab « Image Placeholders »** → tue le flash blanc, **prévient le CLS**, coût client ~0.
- **Hero : `fetchpriority="high"` et PAS lazy** *(erreur WordPress classique qui détruit le LCP)*. Tout le reste : `loading="lazy"`.
- `width`/`height` (ou `aspect-ratio`) sur **tout** média → zéro CLS.

---

## 12. 🆕 Budget performance *(absent de la v1 — c'est l'argument de vente)*

Cibles défendables (75e percentile, mobile) :
| Métrique | Cible |
|---|---|
| Lighthouse Performance (mobile) | **≥ 95** · A11y/SEO/Best-practices **100** |
| LCP (chargement) | **≤ 2,5 s** |
| INP (réactivité) | **≤ 200 ms** |
| CLS (stabilité) | **< 0,1** |
| Poids page d'accueil | **< 1 Mo** |

Leviers WP : CSS critique inline · GSAP/JS `defer` seulement où utilisé · cache page Infomaniak · mesurer en RUM (`web-vitals`/CrUX), pas que Lighthouse.

---

## 13. Favicon & meta-images *(corrigé : WordPress, pas Astro)*

- **Favicon :** monogramme « CV » en Fraunces, Terracotta sur Ivoire. SVG + PNG 32, 180 (apple-touch), 512.
- **Open Graph :** 1 image OG/page (1200×630), titre Fraunces sur fond photo + logo discret. Génération via **plugin SEO WordPress (RankMath)** ou images statiques par page. *(Plus de `@vercel/og` — on n'est pas sur Astro.)*

---

## 14. 🆕 Templates de page ROI *(venus de la recherche)*

À intégrer aux wireframes :
- **Template « Méthode / Qu'est-ce que… »** — pattern The Class/Forme/Heartcore (« Our Method »). Forte valeur GEO/SEO + réassurance. Décliner pour **réflexologie** ET **ménopause**.
- **Template « page locale géo-indexée »** — move ROI n°1 (JOIA, Embody) : 1 page par service+localité, titres géo-riches humains (« Pilates à Le Landeron », « Réflexologie Neuchâtel », « Ménopause Suisse romande »).
- **Barre de confiance** — version solo de la barre presse (Forma) : « Agréée ASCA · remboursable », avis Google, « depuis 2010 / 15+ ans ».
- **Mini-quiz d'orientation** (Pvolve) — « Par où commencer ? » route vers la bonne porte + capte un lead. WP léger, sans SPA.

---

## 15. Ce que ça donne, in fine

Provoquer chez la visiteuse, dans les 5 premières secondes :
1. **« C'est beau. »** — qualité photo, vide, typographie.
2. **« C'est pour moi. »** — le copywriting qui la reconnaît.
3. **« Cette personne est sérieuse. »** — cohérence, sobriété, clarté, vitesse.

Pas de wow-effect tape-à-l'œil. Une tenue, une écriture, une respiration — et un seul moment de grâce.

---

## ✅ À valider avec Carole
- [ ] Palette (présenter 2-3 mockups avant de figer)
- [ ] Polices (lui montrer des exemples)
- [ ] **Matériel photo §4 — le bloquant n°1** (peut-elle fournir / faut-il un shooting ?)
- [ ] Références §5 qui lui parlent le plus
- [ ] Ton des animations (calme, un seul moment)
- [ ] Confirmer Imagick AVIF chez Infomaniak (email)
- [ ] Liste exacte formations/certifications + agrément ASCA (E-E-A-T)

---
*v2 — supersède `carolevallat_direction_artistique.md` (v1). Voir `Revue-Critique_Direction-Artistique.md` pour le détail des changements.*
