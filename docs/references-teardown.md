# Recherche A — Teardown des références studios (mouvement / wellness)
### Pour la refonte Carole Vallat · build = thème blocs WordPress rapide, SEO/GEO fort, warm editorial premium, Fraunces+Inter, palette terre/terracotta

> Déstructuration en profondeur des références d'Alex + 5 ajouts mondiaux. Conclusion : aucun site copiable en bloc ; le move gagnant = blend JOIA (région) + Pvolve/The Class (voix) + Forma/Forme (DA).

## ⚠️ Note de méthode & fiabilité
L'environnement a **bloqué la quasi-totalité des fetchs live**. Seul **JOIA** a été lu en première main. Le reste est reconstruit (audits design publics, portfolios d'agences, case studies, listings apps, docs).
- Positionnement, ton, IA, plateforme booking → **bonne confiance** (corroboré).
- **Hex exacts, polices, headers tech → INFÉRÉS** (le markdown strippe CSS/`<head>`). Aucune couleur ci-dessous = token vérifié.
- Avant de figer les design tokens : repasser chaque URL en navigateur + DevTools/Wappalyzer + `curl -I`.

**Corrections honnêtes :**
- **Forme Studio** : `formestudio.com`/`forme.life` = aucun studio premium identifiable. Vrai = `forme.fitness` (**Webflow** confirmé via staging `forme-655173.webflow.io`). La marque luxe du cluster = **Forma Pilates** (`formapilates.co`).
- **Melo Studio** (`melo.studio`) : **PAS un studio de pilates** — portfolio du photographe parisien Yoann « Melo » Guerini. Réf direction photo uniquement.
- **Embody Movement (UK)** : introuvable → analysé `embodymovementpilates.com` (US).
- **The Class** : `theclass.com` (≠ `taryntoomey.com`, bio legacy).

---

## PARTIE 1 — Teardowns

### 1. Alo Yoga — aloyoga.com — **6,5/10**
Athleisure-lifestyle aspirationnel, magazine-led, calme, un peu distant. Quasi-monochrome (noir/blanc/oat), **un seul grotesque** uppercase espacé, **pas de serif**, photo lifestyle haut budget. Home : promo → hero carrousel image+CTA → tuiles → lookbook → produits → UGC « Alo in The Wild » → footer. Stack **Shopify Plus** (+ headless React/Next probable). **Note F sur cache headers.** SEO copy produit mince.
- **STEAL :** discipline « 1 image + 1 ligne + 1 CTA » par bande ; mega-menu sticky aéré ; bande UGC/preuve sociale.
- **NE PAS :** palette froide ; sans-serif unique ; copy mince ; JS lourd.

### 2. Forme — forme.fitness (+ réf Forma Pilates) — **8,5/10**
Reformer boutique, communauté/transformation, chaleureux premium-local. Neutres chauds (cream/sand/taupe/argile + accent muté) — **très proche de la cible**. Page « What is Reformer Pilates? » = bonne hygiène locale. Booking **Mariana Tek** probable. Stack **Webflow** (confirmé staging).
- **STEAL :** (1) palette neutre chaude + photo communauté réelle ; (2) **pattern page « Qu'est-ce que [modalité] ? »** → dupliquer pour réflexologie & **ménopause** (GEO/SEO + réassurance) ; (3) « Réserver » persistant + page booking dédiée qui passe la main au moteur.
- **NE PAS :** Webflow (≠ stack), feel template, booking app-first.

### 3. Sky Ting — skyting.com — **5/10**
Yoga NYC communautaire, playful, downtown-cool, mascottes par lieu. Maximaliste rétro-70s (corail/bleu ciel/jaune, color-blocking + illustration). On-demand « SKY TING TV ». Stack **Shopify probable**.
- **STEAL :** voix + motif graphique signature ownable ; IA Schedule/On-Demand/About/Shop ; photo réelle + couche graphique chaude.
- **NE PAS :** palette criarde ; OTT vidéo ; Shopify colonne vertébrale.

### 4. The Class by Taryn Toomey — theclass.com — **6,5/10**
Méthode somatique premium, émotionnel/viscéral/quasi-spirituel, founder-led. Sobre moody (charcoal/bone/skin mutés), **serif éditorial haute-contraste**, DA **vidéo-first** cinématique. Abonnement vidéo $40/mo + in-studio **Mindbody**. Écosystème multi-domaines.
- **STEAL :** (1) **page « Méthode »** qui nomme/explique l'approche signature (Pilates+yoga+réflexo+ménopause = méthode cohérente « incarnée ») ; (2) **copy sensorielle tutoiement** (« relâcher », « ce que ton corps retient ») ; (3) DA cinématique retenue (court clip > graphique chargé).
- **NE PAS :** app-first/gated/OTT (tue SEO/GEO) ; multi-domaines ; hero vidéo lourd (→ poster + clip optionnel).

### 5. Heartcore — weareheartcore.com (London) — **8,5/10**
Marque bien-être premium « Positive Movement », communauté « Heartcore Warriors ». Clair naturel (cream/sage/neutres chauds). Hero vidéo. **Stack WordPress (haute conf. indirecte)** : agence **Wholegrain Digital** (WP-only, low-carbon, créateurs du Website Carbon Calculator), hébergé **Kinsta**. **403 aux bots** (mauvais GEO).
- **STEAL :** (1) **une idée de marque qui possède tout** (« Positive Movement » + communauté nommée) ; (2) **discipline WordPress low-carbon / budget page-weight** = preuve que premium + WP rapide coexistent (stack cible) ; (3) motion/vidéo de la **vraie praticienne**.
- **NE PAS :** hero vidéo lourd en solo ; plateforme membership custom ; **le 403 anti-bots**.

### 6. Melo Studio — melo.studio — **3/10** ⚠️ MISMATCH
Portfolio photographe (Yoann Guerini), pas un studio. Galerie image-first, zéro conversion/SEO. **Réf mood photo seulement** (hiérarchie image-first, corps-en-mouvement, retenue confiante).

### 7. Embody Movement Pilates — embodymovementpilates.com (US) — **6/10**
Studio local chaleureux, « 30+ ans », petits groupes (max 4), crédibilité-led. Template small-studio, **vraie force = SEO local** (pages par service/intention/lieu). Stack **WordPress probable**.
- **STEAL :** (1) **sprawl SEO local** (page par service+lieu : « Pilates débutant Le Landeron », « réflexologie plantaire », « accompagnement ménopause Neuchâtel ») ; (2) page **histoire fondatrice** (parfait « incarné »/tutoiement) ; (3) page **« 101 / débuter »** (search informationnel).
- **NE PAS :** visuel template daté ; booking téléphone.

### 8. Pvolve — pvolve.com — **7/10**
Mouvement fonctionnel science-led pour femmes, **toutes étapes de vie**, Clinical Advisory Board, série « Phase & Function » calée sur le cycle, longévité. **Meilleure réf de positionnement pour le track ménopause.** Rebrand 2024 « Natural Connection » : 3 neutres earthy + 2 accents, **script manuscrit en titres** + logo uppercase, photo nature. Home commerce-first + **quiz 2 min « find your bundle »**. **Shopify** + SPA streaming.
- **STEAL :** (1) **positionnement étapes-de-vie/cycle/ménopause** crédible-chaleureux ; (2) **recette « script en titres + uppercase structuré + palette earthy »** = valide Fraunces+Inter+terracotta ; (3) **mini-quiz d'orientation** « Par où commencer ? » (route + capte lead, faisable WP léger).
- **NE PAS :** Shopify + SPA streaming + DTC équipement/abonnement.

### 9. Forma Pilates — formapilates.co — **5/10** (DA 9/10, tech 1/10)
**L'exclusivité comme marque** — studio sur référence, cult/célébrités, mystère. **Bruns chauds + accents noirs**, textiles doux vs miroirs durs, bois clair, pierre. Web minimaliste neutre chaud haut-contraste, négatif généreux, photo éditoriale moody. **Visuellement la plus proche de la cible terracotta/argile.** **SEO volontairement mince.**
- **STEAL :** (1) **retenue radicale + négatif + photo-as-hero** (palette brun-argile/noir) ; (2) **framing rareté/intimité = premium, pas « petit »** (petits groupes = feature, honnête pour Carole) ; (3) entrée « Explorer » calme curatée.
- **NE PAS :** stack streaming custom ; opacité gated ; **SEO mince** (elle doit être trouvée) ; abonnement.

### 10. JOIA Studio — joia-studio.com — **9,5/10** ✅ RÉFÉRENCE #1 (confirmée first-hand)
Reformer boutique **Neuchâtel, Lausanne, Berne** — **canton et langue de Carole**. FR-first, premium-chaleureux, designé par Yolanda Gálvez (NE). **Booking sur bSport** (plateforme FR/EU). Ton : *« Find JOIA in the simple moments of life »*, *« precision, authenticity, human connection »* — registre incarné exact. Neutre minimal chaud (sand/cream + 1 accent), display+sans, photo lifestyle lumière chaude. Home : nav (3 lieux + Classes + Book) → hero 1 phrase → philosophie → 3 studios → classes → produits → promo app → email → footer « Designed by YG ». **bSport confirmé** (`backoffice.bsport.io`). Stack **WordPress probable + Shopify-shop probable** (hybride). **SEO fort** : titres géo-riches humains, **page indexée par lieu**, FR + `/en/`.
- **STEAL :** (1) **pages landing indexées par lieu/service, titres géo-riches** (« Pilates à Le Landeron », « Réflexologie Neuchâtel », « Ménopause Suisse romande ») ; (2) **bSport** comme couche booking (prouvé région/langue) ; (3) **hero éditorial 1 phrase + image**.
- **NE PAS :** app native + machinerie multi-lieux (échelle qu'elle n'a pas).

### 11. Bodyism — bodyism.com — **7,5/10** (architecture hybride)
Wellness premium global, aspirationnel doux (« Rethink health & wellbeing », mantra italique « be kind to yourself »). Near-monochrome + terres via photo. **Stack WordPress confirmé** (`/wp-content/uploads/`) **+ Shopify** (`shop.bodyism.com`). **Le template d'architecture le plus utile si commerce.**
- **STEAL :** (1) **split WordPress (vitrine rapide) + Shopify (sous-domaine)** ; (2) **bande mantra italique** (1 ligne « incarnée ») ; (3) **strip stats-confiance** (« ASCA agréée », « X ans »).
- **NE PAS :** positionnement corporate ; suppléments ; chrome noir froid.

### 12. Frame — moveyourframe.com — **6/10** (foil « trop fort »)
« Fun fitness for every body », loud/playful/inclusif. Extrême bold-editorial (contre-exemple). **Stack WordPress confirmé + Mariana Tek** (booking) + Fisikal.
- **STEAL :** (1) **pattern WP + booking externe** mature (pour elle : bSport/SimplyBook) ; (2) voix inclusive plain-spoken tutoiement (volume baissé) ; (3) **timetable en page indexée**.
- **NE PAS :** color-blocking criard ; gym haute énergie ; complexité app/on-demand.

---

## PARTIE 2 — Synthèse : patterns « premium movement studio 2026 »

| # | Pattern | Présent chez | Fit Carole | Survit au WP rapide ? |
|---|---------|--------------|-----------|----------------------|
| 1 | **Hero éditorial : 1 phrase + 1 image + 1 CTA** | JOIA, Alo, Bodyism, The Class, Forma | ✅ cœur de cible | ✅ |
| 2 | **Page « Méthode / Qu'est-ce que [modalité] »** | The Class, Forme, Embody, Heartcore | ✅✅ or pour réflexo + **ménopause** | ✅ |
| 3 | **Une idée de marque qui possède tout** + communauté nommée | Heartcore, Sky Ting | ✅ trouver son équivalent | ✅ |
| 4 | **Booking externe spécialisé embarqué** | JOIA (bSport), Frame (Mariana Tek) | ✅✅ bSport ou SimplyBook | ✅ |
| 5 | **Hybride WP-vitrine + Shopify-shop** (sous-domaine) | Bodyism, JOIA probable | ⚠️ si cartes cadeaux/produits | ✅ |
| 6 | **Pages landing géo-indexées par lieu/service** | JOIA, Embody | ✅✅ **move ROI #1** | ✅ |
| 7 | **Palette neutre chaude earthy + accent terracotta/argile** | Forma, Pvolve, Forme, JOIA, Heartcore | ✅✅ cible exacte | ✅ |
| 8 | **Serif expressif en titres + sans propre en corps** | The Class, Pvolve, Forma | ✅✅ = Fraunces + Inter | ✅ |
| 9 | **Photo réelle, corps-en-mouvement, lumière naturelle, négatif** | Forma, JOIA, Pvolve | ✅✅ incarné | ✅ |
| 10 | **Quiz « Par où commencer ? »** | Pvolve | ✅ route + lead | ✅ léger |

**À REJETER :** hero vidéo lourd ; app-first/OTT/streaming gated ; headless React/multi-domaines ; monochrome froid ; maximalisme saturé / color-blocking gym ; SEO mince / 403 anti-bots.

**Verdict — blend à 3 sources :**
1. **JOIA** (Suisse romande, 9,5/10) → architecture, **bSport**, **SEO géo-indexé**, hero 1 phrase. Référence #1.
2. **Pvolve + The Class** → voix (ménopause/étapes-de-vie crédible-chaleureux ; page « Méthode » ; copy sensorielle) + recette Fraunces+Inter+earthy.
3. **Forma + Forme** → direction artistique (retenue, négatif, brun-argile/terracotta, photo réelle) + page éducative « Qu'est-ce que… ».
Plus **Bodyism** (split WP+Shopify si commerce) et **Heartcore** (preuve premium = WP rapide low-carbon, stack cible).

**Limites :** hex/polices/headers non vérifiés (fetchs bloqués) sauf JOIA. Confirmer en DevTools avant de figer les tokens.
