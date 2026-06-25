# Carole Vallat — Wireframes basse fidélité

> Document de travail. Structure visuelle des 6 pages, bloc par bloc. Les textes renvoient au document `carolevallat_textes_v1.md`. Le style visuel est défini dans `carolevallat_direction_artistique.md`. Ces wireframes servent à valider la structure AVANT le design haute fidélité.

---

## 🧭 Header global (toutes pages)

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  CAROLE VALLAT    Mouvement  Réflexologie  Ménopause  À propos  │
│                                                      [Réserver] │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

- **Hauteur** : 80px desktop, 64px mobile
- **Logo / nom** : à gauche, en Fraunces 500 20px, couleur Encre terre
- **Nav centrale** : 4 liens principaux, Inter 500 15px
- **CTA "Réserver"** : bouton Terracotta à droite
- **Sticky** : oui, avec backdrop-blur subtil au scroll
- **Mobile** : hamburger à droite, logo centré

---

## 🦶 Footer global (toutes pages)

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  CAROLE VALLAT            NAVIGATION           CONTACT          │
│  Enseignante, coach       Accueil              Studio Soham     │
│  & réflexologue           Mouvement            [Adresse]        │
│  au Landeron              Réflexologie         +41 78 924 24 82 │
│                           Ménopause            info@carole…     │
│  [Instagram] [Facebook]   À propos                              │
│                           Réserver             NEWSLETTER       │
│                                                 [Email input]   │
│                                                 [S'inscrire]    │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  © 2026 Carole Vallat     Mentions légales   Confidentialité   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

- **4 colonnes** desktop, empilées en mobile
- **Fond** : Sable clair `#EFE7D8`
- **Padding** : 96px vertical desktop, 64px mobile
- **Séparateur bas** : filet Lin `#E5DCC9`

---

## 🏠 1. Page d'accueil — `/`

### Structure en 9 sections

```
┌─────────────────────────────────────────────────────────────────┐
│ [HEADER GLOBAL]                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION 1 — HERO                              min-height: 92vh │
│                                                                 │
│  ┌───────────────────────┐  ┌─────────────────────────────┐    │
│  │                       │  │                             │    │
│  │  H1 Retrouve un       │  │                             │    │
│  │  corps plus fort,     │  │    [PHOTO CAROLE           │    │
│  │  plus mobile et       │  │     plan moyen,             │    │
│  │  plus serein.         │  │     regard caméra,          │    │
│  │                       │  │     portrait 3:4]           │    │
│  │  Sous-titre 1-2 lignes│  │                             │    │
│  │                       │  │                             │    │
│  │  [CTA primaire] ↓     │  │                             │    │
│  │  [CTA secondaire]     │  │                             │    │
│  │                       │  │                             │    │
│  └───────────────────────┘  └─────────────────────────────┘    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION 2 — RECONNAISSANCE                         fond Sable  │
│                                                                 │
│           "Peut-être que tu te reconnais ici…"                  │
│                                                                 │
│       Texte centré, max-width 680px, Fraunces 500 28px          │
│       Tu as l'impression que ton corps n'est plus...            │
│       [4-5 phrases d'accroche]                                  │
│                                                                 │
│                Tu n'es pas seule.                               │
│               Et tu n'as pas à subir.                           │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION 3 — TROIS PORTES D'ENTRÉE                  fond Ivoire │
│                                                                 │
│           Trois manières de revenir à toi                       │
│                                                                 │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐       │
│  │               │  │               │  │               │       │
│  │ [Photo 1:1]   │  │ [Photo 1:1]   │  │ [Photo 1:1]   │       │
│  │               │  │               │  │               │       │
│  │ Le mouvement  │  │ Réflexologie  │  │ Ménopause     │       │
│  │               │  │               │  │               │       │
│  │ Yoga, Pilates,│  │ Un soin pour  │  │ À partir de   │       │
│  │ Yin et aérien │  │ ralentir...   │  │ 40 ans...     │       │
│  │               │  │               │  │               │       │
│  │ Découvrir →   │  │ Découvrir →   │  │ Découvrir →   │       │
│  │               │  │               │  │               │       │
│  └───────────────┘  └───────────────┘  └───────────────┘       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION 4 — MON APPROCHE                           fond Sable  │
│                                                                 │
│  ┌─────────────────────────┐  ┌──────────────────────────┐     │
│  │                         │  │                          │     │
│  │ H2 Une approche qui     │  │  [Photo détail           │     │
│  │ relie tout ce qui te    │  │   mains/geste/matière]   │     │
│  │ compose                 │  │                          │     │
│  │                         │  │                          │     │
│  │ Texte (3 paragraphes)   │  │                          │     │
│  │ Depuis plus de dix ans… │  │                          │     │
│  │                         │  │                          │     │
│  │ Citation mise en avant  │  │                          │     │
│  │ "Le but n'est pas de    │  │                          │     │
│  │ faire plus. C'est de    │  │                          │     │
│  │ faire plus juste."      │  │                          │     │
│  │                         │  │                          │     │
│  └─────────────────────────┘  └──────────────────────────┘     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION 5 — LES 5 PILIERS                          fond Ivoire │
│                                                                 │
│           H2 Les 5 piliers que je travaille avec toi            │
│                                                                 │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                  │
│  │ 01   │ │ 02   │ │ 03   │ │ 04   │ │ 05   │                  │
│  │      │ │      │ │      │ │      │ │      │                  │
│  │Muscl.│ │Cardio│ │Mental│ │Fascia│ │Nourr.│                  │
│  │& os  │ │      │ │      │ │      │ │      │                  │
│  │      │ │      │ │      │ │      │ │      │                  │
│  │Texte │ │Texte │ │Texte │ │Texte │ │Texte │                  │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘                  │
│                                                                 │
│  → Mobile: scroll horizontal snap ou empilement vertical        │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION 6 — TÉMOIGNAGES                            fond Sable  │
│                                                                 │
│         Ce que vivent les femmes que j'accompagne               │
│                                                                 │
│  ┌─────────────────────────────────────────────────────┐       │
│  │  "Studio Soham est pour moi un lieu exceptionnel    │       │
│  │  que je fréquente depuis 5 ans. Carole est une      │       │
│  │  professeure incroyable..."                         │       │
│  │                                                     │       │
│  │  [Photo ronde]  — Prénom, Le Landeron               │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                 │
│         ● ○ ○    (indicateurs de slider/carousel)               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION 7 — LOCALISATION                           fond Ivoire │
│                                                                 │
│  ┌──────────────────────────┐  ┌────────────────────────┐      │
│  │                          │  │                        │      │
│  │ H2 Au Studio Soham,      │  │  [Photo studio vide    │      │
│  │ au Landeron              │  │   lumière naturelle]   │      │
│  │                          │  │                        │      │
│  │ Texte + infos pratiques  │  │                        │      │
│  │ 📍 [Adresse]             │  │                        │      │
│  │ 📞 +41 78 924 24 82      │  │                        │      │
│  │ ✉️  info@carolevallat.ch  │  │                        │      │
│  │                          │  │                        │      │
│  │ → Voir le plan           │  │                        │      │
│  │                          │  │                        │      │
│  └──────────────────────────┘  └────────────────────────┘      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION 8 — CTA FINAL                         fond Terracotta  │
│                                                                 │
│             H2 Un premier pas, à ton rythme.                    │
│             (couleur Ivoire sur fond Terracotta)                │
│                                                                 │
│              Texte court en 2 lignes                            │
│                                                                 │
│   [Réserver cours]  [Réflexologie]  [Appel ménopause]           │
│     (ghost Ivoire)  (ghost Ivoire)  (ghost Ivoire)              │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ [FOOTER GLOBAL]                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Notes desktop** : hero asymétrique (texte 55% / photo 45%). Cards portes d'entrée en grille 3 colonnes. Section approche inversée (image à droite).

**Notes mobile** : tout empilé, hero photo au-dessus ou en background atténué, cards portes d'entrée empilées.

---

## 🧘 2. Page Mouvement — `/mouvement/`

```
┌─────────────────────────────────────────────────────────────────┐
│ [HEADER GLOBAL]                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  HERO                                           min-height: 80vh│
│                                                                 │
│  ┌─────────────────────────┐  ┌────────────────────────┐       │
│  │                         │  │                        │       │
│  │ H1 Le mouvement pour    │  │                        │       │
│  │ une vie qui te          │  │ [Photo Carole en       │       │
│  │ ressemble.              │  │  mouvement, dynamique, │       │
│  │                         │  │  lumière studio]       │       │
│  │ Sous-titre              │  │                        │       │
│  │                         │  │                        │       │
│  │ [Réserver cours d'essai]│  │                        │       │
│  │                         │  │                        │       │
│  └─────────────────────────┘  └────────────────────────┘       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION POUR QUI                                   fond Sable  │
│                                                                 │
│    H2 Tu veux retrouver un corps capable dans ta vraie vie      │
│                                                                 │
│    Texte avec "Tu veux…" en liste mise en avant                 │
│    (max-width 680px, centré)                                    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION DISCIPLINES                                fond Ivoire │
│                                                                 │
│                       H2 Mes cours                              │
│                                                                 │
│  Alternance texte/image inversée par bloc :                     │
│                                                                 │
│  ┌─────────────────┐  ┌──────────────────────┐                 │
│  │                 │  │ 01 — Pilates         │                 │
│  │ [Photo Pilates] │  │                      │                 │
│  │                 │  │ Une approche fluide  │                 │
│  │                 │  │ et fonctionnelle...  │                 │
│  │                 │  │                      │                 │
│  │                 │  │ Pour qui : ...       │                 │
│  └─────────────────┘  └──────────────────────┘                 │
│                                                                 │
│  ┌──────────────────────┐  ┌─────────────────┐                 │
│  │ 02 — Pilates Reformer│  │ [Photo Reformer]│                 │
│  │                      │  │                 │                 │
│  │ Texte...             │  │                 │                 │
│  │                      │  │                 │                 │
│  └──────────────────────┘  └─────────────────┘                 │
│                                                                 │
│  [Même pattern pour Yin, Yoga Fascias, Inside Flow,             │
│   Yoga Nidra, Yoga aérien]                                      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION APPROCHE                                   fond Sable  │
│                                                                 │
│          H2 Une approche qui te respecte                        │
│                                                                 │
│       Texte centré max-width 680px, 2 paragraphes               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION STUDIO SOHAM                          fond Ivoire      │
│                                                                 │
│  [Grille 3 photos du studio en format varié]                    │
│                                                                 │
│  ┌──────────┐ ┌──────┐                                          │
│  │          │ │      │                                          │
│  │          │ │      │                                          │
│  │  Grande  │ ├──────┤   H2 Le Studio Soham, au Landeron        │
│  │          │ │      │                                          │
│  │          │ │ Petite                                          │
│  └──────────┘ └──────┘   Texte (4-5 lignes)                     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION HORAIRES & TARIFS                          fond Sable  │
│                                                                 │
│           H2 Horaires & tarifs                                  │
│                                                                 │
│         Texte court explicatif                                  │
│                                                                 │
│  [Voir horaires] [Voir tarifs] [Réserver cours d'essai]         │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CTA FINAL                                     fond Terracotta  │
│                                                                 │
│           H2 Et si tu venais essayer ?                          │
│           Texte 2 lignes                                        │
│           [Réserver mon cours d'essai]                          │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ [FOOTER GLOBAL]                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🦶 3. Page Réflexologie — `/reflexologie-plantaire/`

```
┌─────────────────────────────────────────────────────────────────┐
│ [HEADER GLOBAL]                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  HERO                                           min-height: 80vh│
│                                                                 │
│  Layout centré (différent des autres pages pour créer calme)    │
│                                                                 │
│                [Photo détail mains/pieds]                       │
│                    (format paysage)                             │
│                                                                 │
│        H1 Un soin pour ralentir, relâcher, rééquilibrer.        │
│                                                                 │
│                    Sous-titre 2 lignes                          │
│                                                                 │
│                  [Prendre rendez-vous]                          │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION POUR QUI                                   fond Sable  │
│                                                                 │
│             H2 Ce soin est pour toi si…                         │
│                                                                 │
│    • Tu te sens stressée, tendue ou en surcharge.               │
│    • Tu dors moins bien ou tu récupères difficilement.          │
│    • Tu traverses une période de transition hormonale...        │
│    • Tu veux un moment de soin qui fasse du bien...             │
│    • Tu cherches une vraie pause, pas seulement un massage.     │
│                                                                 │
│    (liste alignée à gauche, max-width 680px, centré)            │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION COMMENT ÇA MARCHE                          fond Ivoire │
│                                                                 │
│  ┌────────────────────────┐  ┌────────────────────────┐         │
│  │                        │  │                        │         │
│  │  [Photo détail         │  │ H2 Ce que la           │         │
│  │   séance, setup        │  │ réflexologie peut      │         │
│  │   apaisant]            │  │ t'apporter             │         │
│  │                        │  │                        │         │
│  │                        │  │ Texte 2 paragraphes    │         │
│  │                        │  │                        │         │
│  └────────────────────────┘  └────────────────────────┘         │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION UNE SÉANCE                                 fond Sable  │
│                                                                 │
│             H2 Comment se déroule une séance                    │
│                                                                 │
│          Texte déroulé en 3-4 phrases                           │
│                                                                 │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐                │
│  │  Durée     │  │   Tarif    │  │    Lieu    │                │
│  │   1h       │  │   [CHF]    │  │Studio Soham│                │
│  └────────────┘  └────────────┘  └────────────┘                │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION FAQ                                        fond Ivoire │
│                                                                 │
│          H2 Les questions qu'on me pose souvent                 │
│                                                                 │
│  ▸ Est-ce que c'est douloureux ?                                │
│  ▸ Combien de séances faut-il ?                                 │
│  ▸ Est-ce remboursé par les assurances ?                        │
│  ▸ Est-ce compatible avec un suivi médical ?                    │
│                                                                 │
│  (Accordéons natifs <details> HTML, max-width 720px)            │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CTA FINAL                                     fond Terracotta  │
│                                                                 │
│               H2 Réserver ton soin                              │
│               Texte 2 lignes                                    │
│               [Prendre rendez-vous]                             │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ [FOOTER GLOBAL]                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🌿 4. Page Ménopause — `/menopause/`

```
┌─────────────────────────────────────────────────────────────────┐
│ [HEADER GLOBAL]                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  HERO                                           min-height: 92vh│
│                                                                 │
│  ┌────────────────────────┐  ┌─────────────────────────┐       │
│  │                        │  │                         │       │
│  │ H1 Tu n'as pas à       │  │                         │       │
│  │ subir. Il existe des   │  │  [Photo Carole          │       │
│  │ solutions.             │  │   regard direct,        │       │
│  │                        │  │   posture incarnée,     │       │
│  │ Sous-titre             │  │   portrait 3:4]         │       │
│  │                        │  │                         │       │
│  │ [Découvrir programme]  │  │                         │       │
│  │ [Appel découverte]     │  │                         │       │
│  │                        │  │                         │       │
│  └────────────────────────┘  └─────────────────────────┘       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION LE PROBLÈME                                fond Sable  │
│                                                                 │
│           H2 Tu te reconnais peut-être ici…                     │
│                                                                 │
│          Texte en phrases courtes, centré, espacé               │
│                                                                 │
│              Tu ne reconnais plus ton corps.                    │
│           Ce qui marchait avant ne marche plus pareil.          │
│            Tu manques d'énergie, de tonus, de clarté.           │
│                      [etc.]                                     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION MESSAGE CLÉ                        fond Terracotta     │
│                                                                 │
│    Bloc pleine largeur, texte Ivoire grand, centré              │
│                                                                 │
│                Ton corps n'est pas cassé.                       │
│             Il a changé de physiologie.                         │
│     Le but n'est pas de faire plus. C'est de faire plus juste.  │
│                                                                 │
│    (Fraunces 300, 40-48px, line-height 1.3, max-width 900px)    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION MÉTHODE — 5 PILIERS                        fond Ivoire │
│                                                                 │
│    H2 Ma méthode : les 5 piliers de la femme à partir de 40 ans │
│                                                                 │
│              Intro courte (2-3 lignes)                          │
│                                                                 │
│  ┌─────────────────────────────────────────────────────┐       │
│  │ 01  Muscles & os                                    │       │
│  │     À partir de 40 ans, tu perds en masse...        │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                 │
│  ┌─────────────────────────────────────────────────────┐       │
│  │ 02  Cardio                                          │       │
│  │     Le système cardio-vasculaire change...          │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                 │
│  [3 autres blocs empilés verticalement]                         │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION DEUX CHEMINS                               fond Sable  │
│                                                                 │
│            H2 Deux manières d'être accompagnée                  │
│                                                                 │
│  ┌────────────────────────┐  ┌────────────────────────┐         │
│  │                        │  │                        │         │
│  │  [Icône ou visuel]     │  │  [Icône ou visuel]     │         │
│  │                        │  │                        │         │
│  │  Programme en ligne    │  │  Coaching privé        │         │
│  │                        │  │                        │         │
│  │  Texte description     │  │  Texte description     │         │
│  │                        │  │                        │         │
│  │  BADGE: En préparation │  │                        │         │
│  │                        │  │                        │         │
│  │  [Liste d'attente]     │  │  [Appel découverte]    │         │
│  │                        │  │                        │         │
│  └────────────────────────┘  └────────────────────────┘         │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION POURQUOI MOI                               fond Ivoire │
│                                                                 │
│  ┌────────────────────────┐  ┌────────────────────────┐         │
│  │                        │  │                        │         │
│  │  [Photo Carole         │  │  H2 Pourquoi me        │         │
│  │   portrait contempla-  │  │  faire confiance       │         │
│  │   tif]                 │  │                        │         │
│  │                        │  │  Texte bio 2 paragraphes│        │
│  │                        │  │                        │         │
│  │                        │  │  → Mon parcours        │         │
│  └────────────────────────┘  └────────────────────────┘         │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION FAQ                                        fond Sable  │
│                                                                 │
│           H2 Questions fréquentes                               │
│                                                                 │
│  ▸ À partir de quel âge ce programme me concerne ?              │
│  ▸ Est-ce que je dois déjà être sportive ?                      │
│  ▸ Combien de temps dure le programme ?                         │
│  ▸ Est-ce que tu remplaces un suivi médical ?                   │
│  ▸ Et si je veux juste un avis avant de m'engager ?             │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CTA FINAL                                     fond Terracotta  │
│                                                                 │
│   H2 Le moment de reprendre la main, c'est maintenant.          │
│                                                                 │
│   [Liste d'attente programme]  [Appel découverte]               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ [FOOTER GLOBAL]                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 👋 5. Page À propos — `/a-propos/`

```
┌─────────────────────────────────────────────────────────────────┐
│ [HEADER GLOBAL]                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  HERO                                           min-height: 85vh│
│                                                                 │
│  Layout : grande photo portrait 60% + texte 40%                 │
│                                                                 │
│  ┌──────────────────────────────┐  ┌──────────────────┐        │
│  │                              │  │                  │        │
│  │                              │  │ H1 Bonjour,      │        │
│  │                              │  │ je suis Carole.  │        │
│  │   [GRANDE PHOTO              │  │                  │        │
│  │    PORTRAIT CAROLE           │  │ Sous-titre       │        │
│  │    expression calme          │  │ 2 lignes         │        │
│  │    lumière douce]            │  │                  │        │
│  │                              │  │                  │        │
│  │                              │  │                  │        │
│  └──────────────────────────────┘  └──────────────────┘        │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION MON HISTOIRE                               fond Sable  │
│                                                                 │
│                 H2 Mon parcours                                 │
│                                                                 │
│  Texte long, max-width 680px, centré                            │
│  Fraunces 400 20px pour les intertitres, Inter 18px corps       │
│                                                                 │
│  J'ai commencé la gymnastique à cinq ans. Très vite...          │
│                                                                 │
│  Je me suis ensuite formée au Pilates, au yoga...               │
│                                                                 │
│  Aujourd'hui, je tisse tout ça ensemble...                      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION PHILOSOPHIE                                fond Ivoire │
│                                                                 │
│  ┌──────────────────────┐  ┌───────────────────────────┐       │
│  │                      │  │                           │       │
│  │                      │  │ H2 Ce que je crois        │       │
│  │  [Photo détail       │  │                           │       │
│  │   main, geste,       │  │ 3 paragraphes             │       │
│  │   matière]           │  │                           │       │
│  │                      │  │                           │       │
│  └──────────────────────┘  └───────────────────────────┘       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION FORMATIONS                                 fond Sable  │
│                                                                 │
│           H2 Mes formations & certifications                    │
│                                                                 │
│  Layout en 2 colonnes, liste propre                             │
│                                                                 │
│  • Pilates Mat & Reformer    • Yoga Nidra                       │
│  • Inside Flow Yoga          • Yoga aérien                      │
│  • BiointegrityYoga          • Réflexologie plantaire           │
│  • Yin Yoga                  • Formation ménopause              │
│                                                                 │
│  (Chaque ligne : titre + école + année en Taupe plus petit)     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION PLUS PERSONNEL                             fond Ivoire │
│                                                                 │
│           H2 Ce que je préfère, en dehors du studio             │
│                                                                 │
│     Texte personnel de Carole, max-width 680px                  │
│                                                                 │
│     Photos en mosaïque plus lifestyle (3-4 images)              │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CTA FINAL                                     fond Terracotta  │
│                                                                 │
│    Texte "Si ce que tu as lu ici te parle..."                   │
│                                                                 │
│   [Découvrir cours]  [Réflexologie]  [Appel découverte]         │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ [FOOTER GLOBAL]                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📅 6. Page Réserver — `/reserver/`

```
┌─────────────────────────────────────────────────────────────────┐
│ [HEADER GLOBAL]                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  HERO COMPACT                                   min-height: 50vh│
│                                                                 │
│                 H1 Réserver ta séance                           │
│                                                                 │
│           Sous-titre court, 2 lignes, centré                    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION 3 CARDS DE RÉSERVATION                     fond Sable  │
│                                                                 │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐       │
│  │               │  │               │  │               │       │
│  │ [Icône cours] │  │ [Icône soin]  │  │ [Icône ménop] │       │
│  │               │  │               │  │               │       │
│  │ Un cours      │  │ Un soin de    │  │ Un appel      │       │
│  │ collectif     │  │ réflexologie  │  │ découverte    │       │
│  │               │  │               │  │               │       │
│  │ Yoga, Pilates,│  │ Une heure pour│  │ 30 minutes    │       │
│  │ Yin, Inside   │  │ ralentir...   │  │ gratuit       │       │
│  │ Flow, aérien  │  │               │  │               │       │
│  │               │  │               │  │               │       │
│  │ [Réserver →]  │  │ [Réserver →]  │  │ [Réserver →]  │       │
│  │               │  │               │  │               │       │
│  └───────────────┘  └───────────────┘  └───────────────┘       │
│                                                                 │
│  → Chaque bouton ouvre le widget Calendly correspondant         │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION CONTACT DIRECT                             fond Ivoire │
│                                                                 │
│  ┌──────────────────────┐  ┌──────────────────────────┐        │
│  │                      │  │                          │        │
│  │ H2 Tu préfères       │  │  Formulaire              │        │
│  │ m'écrire             │  │                          │        │
│  │ directement ?        │  │  Prénom                  │        │
│  │                      │  │  [___________________]   │        │
│  │                      │  │                          │        │
│  │ 📞 +41 78 924 24 82  │  │  Email                   │        │
│  │ ✉️  info@carole…      │  │  [___________________]   │        │
│  │                      │  │                          │        │
│  │                      │  │  Téléphone (optionnel)   │        │
│  │                      │  │  [___________________]   │        │
│  │                      │  │                          │        │
│  │                      │  │  Ton message             │        │
│  │                      │  │  [___________________]   │        │
│  │                      │  │  [___________________]   │        │
│  │                      │  │                          │        │
│  │                      │  │  [Envoyer]               │        │
│  │                      │  │                          │        │
│  └──────────────────────┘  └──────────────────────────┘        │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SECTION LOCALISATION                               fond Sable  │
│                                                                 │
│        H2 Studio Soham — Le Landeron                            │
│                                                                 │
│  ┌───────────────────────────────────────────────────┐         │
│  │                                                   │         │
│  │                                                   │         │
│  │           [Carte statique avec pin]               │         │
│  │                                                   │         │
│  │                                                   │         │
│  └───────────────────────────────────────────────────┘         │
│                                                                 │
│              [Adresse exacte]                                   │
│              2525 Le Landeron, canton de Neuchâtel              │
│              À 15 min de Neuchâtel, 25 min de Bienne            │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ [FOOTER GLOBAL]                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📱 Notes responsive globales

### Breakpoints clés

```
Mobile   (< 640px)  : tout empilé, 1 colonne, padding réduit
Tablet   (640-1024) : 2 colonnes pour les grids, hero réorganisé
Desktop  (> 1024)   : layouts 2-3-4 colonnes selon les sections
```

### Règles mobile spécifiques

1. **Hero** : photo passe au-dessus du texte (ou en background atténué)
2. **Cards en grille** → empilement vertical avec espacement
3. **Sections "image + texte"** → image avant texte dans l'ordre DOM
4. **Nav** → hamburger avec overlay plein écran
5. **Boutons CTA** → pleine largeur ou centrés, padding généreux pour le tactile (min 48px)
6. **Typographie** → H1 64px → 42px, H2 48px → 32px, corps 18px → 17px
7. **Marges verticales** → 128px → 80px

### Règles d'accessibilité

- Tous les CTA ont un `aria-label` clair
- Tous les formulaires ont des `<label>` associés
- Les images décoratives ont `alt=""`, les images informatives ont un alt descriptif
- Ordre de tabulation logique (DOM suit l'ordre visuel)
- Contrastes vérifiés (voir direction artistique)

---

## ✅ À valider avec Carole

- [ ] Structure générale des 6 pages
- [ ] Position du bouton "Réserver" dans le header (ok en top-right ?)
- [ ] Nombre de sections par page (trop / pas assez ?)
- [ ] Choix du layout "hero asymétrique" vs "hero centré" selon les pages
- [ ] Présence ou non de la section "Les 5 piliers" sur la home (redondant avec menopause ?)
- [ ] Décision finale : témoignages en carousel ou grille statique ?
- [ ] Formulaire contact : champ téléphone obligatoire ou optionnel ?

---

## Prochaines étapes après validation

1. **Design haute fidélité** dans Lovable ou Figma : 1-2 variantes pour l'accueil d'abord
2. **Validation visuelle** avec Carole sur la page d'accueil
3. **Déclinaison** du design sur les 5 autres pages
4. **Setup Astro** + structure de composants
5. **Build page par page** avec preview sur `dev.carolevallat.ch`
