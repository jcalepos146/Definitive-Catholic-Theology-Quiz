# The Definitive Catholic Theology Quiz — v5.0

**[▶️ Take the Quiz](https://jcalepos146.github.io/Definitive-Catholic-Theology-Quiz/)**

A comprehensive theological assessment tool that maps your beliefs across 88 schools of Catholic thought, Protestant traditions, and Eastern Orthodoxy. CRT phosphor-green dark mode. 88 SVG engraving-style portraits. Shareable results cards. Save/resume. Challenge-a-friend mode.

---

## What's New in v5.0

### Shareable Results Card
A "Download PNG" and "Copy to Clipboard" button generates an 800×500 CRT-styled image of your results — top 5 schools with bar charts, all 8 axis spectrum positions with markers, scanline texture, and the quiz URL. Designed for posting to Twitter, Discord, Reddit, or sending to your theology group.

### Results Breakdown by Category
New "By Category" tab shows your top school *per theological category* as a grid of 10 cards. Captures the composite nature of real theological identity: "Augustinian in Grace, Gallican in Ecclesiology, Distributist in Politics, Reform of the Reform in Liturgy."

### Save & Resume
Answers auto-save to localStorage on every selection. Return to the page and a banner offers to resume where you left off. Saved data expires after 7 days. Progress clears when you view results.

### Question Review Mode
New "Review" tab shows every question with your answer highlighted and the exact school-score codes it triggered (`THOM:+4 DOM:+2 NEOSCH:+2`). Organized by category. Full scoring transparency — no black boxes.

### "Why This Score?" Drill-Down
Click any school in the Rankings tab to expand a breakdown of every question that contributed points, sorted by impact. Positive contributions in green, negative in red. Trace exactly *why* you scored 78% Thomist.

### School Comparison Mode
New "Compare" tab. Select any two schools from your top 15 and see: overall agreement percentage, and a row-by-row breakdown of which option each school prefers on every relevant question. Agreements in green, divergences in red.

### Personalized Reading List
New "Reading" tab generates a curated list based on your top 3 schools: the key figure's primary works, biographical context, and specific further-reading sources from questions where you scored points for that school.

### Challenge a Friend
Click "Challenge a Friend" to generate a URL encoding your exact question selection and answers. Send the link — they take the same questions, then see a side-by-side comparison showing agreement percentage across all shared questions.

### Historical Timeline
New "Timeline" tab renders an SVG timeline of your top 7 schools' key figures, plotted chronologically with pulsing markers. See whether your theology is rooted in the patristic, medieval, Counter-Reformation, or modern era at a glance.

### Theological Neighbors Map
New "Map" tab renders a force-directed SVG graph of your top 12 schools positioned by cosine similarity of their scoring vectors. Similar schools cluster together; dissimilar ones repel. Links drawn between schools with >30% similarity. Your #1 result is highlighted with a glowing node.

### Most Decisive Questions
Below your top match, the 5 questions with the biggest impact on your #1 school are listed with point values.

### CRT Flicker Removed
The periodic screen-flicker animation from v4 has been removed. The CRT aesthetic (scanlines, vignette, phosphor glow) remains.

---

## Carried Forward from v4.0

- **CRT Phosphor Dark Mode**: `#39FF14` electric green on pure black with scanline overlays, edge vignette, and glow effects
- **88 SVG Engraving Portraits**: Unique copper-engraving line-art for every school result, rendering in theme green via `var(--verd)`
- **119 Questions across 10 Categories**: Consolidated from 154 (v1) → 134 (v3) → 119 (v4)
- **Hybrid Normalized Scoring**: 70% raw alignment + 20% confidence (exponential decay) + 10% coverage
- **Tanh-Curved Axis Spectrums**: Per-axis normalization with `tanh(x × 2.2)` ensuring decisive patterns reach the fringes
- **1,089 Saint/Theologian Cards**: 103 unique figures across all questions, including Bossuet (10q), Congar (5q), Maximus the Confessor (4q), Catherine of Siena (4q), Edith Stein (4q)
- **"I Don't Know" Button**: Value-neutral option on every question
- **Copy Prompt (📋)**: Clipboard-ready prompt for external AI (ChatGPT, Claude, Magisterium.com)
- **Heterodoxy Warnings**: Flags for condemned, schismatic, irregular, or non-Catholic results
- **Category Navigation**: Scrollable tab bar with per-category progress counters

---

## Overview

The quiz presents 119 questions across 10 theological categories, scoring responses against 88 distinct schools, traditions, and spiritualities. Each answer assigns positive or negative points to relevant schools. Final scores are hybrid-normalized and ranked. Eight theological axes provide a spectrum profile. Results include 8 analysis tabs, shareable image export, and challenge-a-friend mode.

## Features at a Glance

| Feature | Description |
|---------|-------------|
| 🖥️ CRT Dark Mode | Phosphor green on black, scanlines, vignette, glow |
| 🎨 88 SVG Portraits | Unique engraving-style art per school |
| 📊 8 Results Tabs | Rankings, Spectrums, By Category, Review, Compare, Reading, Timeline, Map |
| 🖼️ Share Card | Download/clipboard PNG of your results |
| 💾 Save & Resume | Auto-saves progress via localStorage |
| 🔍 Score Drill-Down | Click any school to see exactly which questions contributed |
| ⚔️ School Comparison | Side-by-side comparison of any two schools |
| 📚 Reading List | Personalized book recommendations from your top 3 |
| 🤝 Challenge Mode | Send a friend the same questions, compare answers |
| 📅 Timeline | Your key figures plotted across 17 centuries |
| 🗺️ Neighbors Map | Force-directed graph of school similarities |
| ✝️ 1,089 Saint Cards | 103 theologians mapped across all questions |
| 📈 Hybrid Scoring | Confidence-weighted normalization |
| 📐 Tanh Axis Curves | Decisive patterns reach the fringes |
| 🤷 IDK Button | Value-neutral "I Don't Know" on every question |
| 📋 Copy Prompt | One-click AI help via external tools |
| ⚠️ Heterodoxy Flags | Warnings on condemned/irregular/non-Catholic results |
| 📱 Mobile Responsive | Full functionality on phones and tablets |
| 📦 Single File | No dependencies, no build step, no server |

## Files

| File | Description | Size |
|------|-------------|------|
| `index.html` | Complete quiz application (standalone) | ~730 KB |
| `header.png` | CRT-style header image with religious order heraldry | — |
| `README.md` | This documentation | — |

### Header Image Setup

The quiz includes a header image slot that displays above the title. Place `header.png` in the repository root and it loads automatically. If the image is unavailable, the title renders as glowing text with no visual break.

To use a custom URL, find this line in `index.html`:

```html
<img id="header-img" src="" alt="The Definitive Catholic Theology Quiz"
```

Replace `src=""` with your image URL:

```html
<img id="header-img" src="https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/header.png"
```

The image has a gradient fade at the bottom that bleeds into the dark background, a green border glow, and a brightness filter. If loading fails, the `onerror` handler hides it gracefully.

## Categories & Questions

| # | Category | Questions | Range |
|---|----------|-----------|-------|
| 1 | Scripture & Hermeneutics | 4 | Q0–Q3 |
| 2 | Metaphysics & Philosophy | 7 | Q4–Q10 |
| 3 | Christology & Soteriology | 9 | Q11–Q19 |
| 4 | Grace & Predestination | 15 | Q20–Q34 |
| 5 | Sacramental Theology | 11 | Q35–Q45 |
| 6 | Ecclesiology & Authority | 15 | Q46–Q60 |
| 7 | Moral Theology | 6 | Q61–Q66 |
| 8 | Religious Orders & Spirituality | 7 | Q67–Q73 |
| 9 | Political & Social | 10 | Q74–Q83 |
| 10 | Contemporary Debates | 35 | Q84–Q118 |
| | **Total** | **119** | |

## Theological Schools (88)

### Grace & Predestination
| Code | School | Key Figure |
|------|--------|------------|
| AUG | Augustinian | St. Augustine of Hippo |
| AUGP | Strict Augustinian | Prosper of Aquitaine |
| NEOAUG | Neo-Augustinian (ressourcement) | Henri de Lubac, S.J. |
| JANS | Jansenist ⚠️ | Blaise Pascal |
| THOM | Thomist (mainstream) | St. Thomas Aquinas |
| THOMP | Strict Thomist | Réginald Garrigou-Lagrange, O.P. |
| BANEZ | Bañezian | Domingo Báñez, O.P. |
| MOL | Molinist | Luis de Molina, S.J. |
| CONG | Congruist | St. Robert Bellarmine, S.J. |
| SCOT | Scotist | Bl. John Duns Scotus |
| FRANC | Franciscan (Bonaventure) | St. Bonaventure |
| SUPRA | Supralapsarian ⚡ | Gottschalk of Orbais |

### Metaphysics & Philosophy
| Code | School | Key Figure |
|------|--------|------------|
| THOMMETA | Thomist Realist | Étienne Gilson |
| SCOTMETA | Scotist (univocity) | Charles Sanders Peirce |
| NEOPLAT | Neo-Platonist | Pseudo-Dionysius |
| VOLUNT | Nominalist-Voluntarist ⚡ | William of Ockham |
| INTELL | Intellectualist | St. Thomas Aquinas |
| PALAM | Palamite | St. Gregory Palamas |

### Christology & Soteriology
| Code | School | Key Figure |
|------|--------|------------|
| RESSCH | Ressourcement Christology | Hans Urs von Balthasar |
| CHALMAX | Chalcedonian Maximalist | St. Cyril of Alexandria |
| KENOT | Kenoticism-sympathetic ⚡ | Sergei Bulgakov |

### Sacramental Theology
| Code | School | Key Figure |
|------|--------|------------|
| TRIDSAC | Tridentine Sacramentalism | St. Thomas Aquinas |
| THOMSAC | Thomist Sacramentology | St. Thomas Aquinas |
| EASTSAC | Eastern Sacramental | St. John Chrysostom |
| TRANSIG | Transignification-open ⚡ | Edward Schillebeeckx, O.P. |
| EUCHMYST | Eucharistic Mysticism | St. John of the Cross |

### Religious Orders & Spiritualities
| Code | School | Key Figure |
|------|--------|------------|
| DOM | Dominican | JES | Jesuit | CARM | Carmelite | BENED | Benedictine | FRAN | Franciscan (order) | OPUS | Opus Dei | ORAT | Oratorian | CHART | Carthusian | OSA | Augustinian (Order) | OCSO | Cistercian/Trappist | CSSR | Redemptorist | SDB | Salesian | CM | Vincentian/Lazarist | CP | Passionist | OSM | Servite | OPRAEM | Norbertine | MERC | Mercedarian |

*(17 schools — see v4 README for full table with figures)*

### Ecclesiology, Moral, Political, Liturgical, Non-Catholic

*(53 schools — see full school table in v4 README or browse the quiz results)*

## Theological Axes (8)

| Axis | Left Endpoint | Right Endpoint | Questions |
|------|--------------|----------------|-----------|
| Grace | Synergistic | Monergistic | 18 |
| Papal Authority | Conciliar/Local | Ultramontane | 23 |
| Liturgical | Reformist | Traditional | 21 |
| Moral Rigorism | Pastoral/Lenient | Rigorist | 22 |
| Personal Piety | Lower Intensity | High Contemplative | 13 |
| Scripture | Magisterium-first | Scripture-first | 13 |
| Justification | Forensic emphasis | Participatory/union | 9 |
| Eschatology | This-world focus | Judgment & beatific end | 9 |

Each axis uses per-question normalization with `tanh(x × 2.2)` amplification. Half-leaning → 86%. Full extreme → 94%.

## Scoring

**School scoring** — hybrid normalization:
```
score = (raw_pct × 0.7) + (confidence × 0.2) + (coverage × 0.1)
where confidence = 1 - e^(-questionCount / 8), coverage = min(1, questionCount / 10)
```

**Axis scoring** — per-axis normalization against actual max, then tanh curve.

## Results Tabs

| Tab | Content |
|-----|---------|
| **Rankings** | School rankings with click-to-drill-down |
| **Spectrums** | 8 tanh-curved axis positions |
| **By Category** | Top school per category, 10-card grid |
| **Review** | All answers with scoring codes |
| **Compare** | Two-school side-by-side comparison |
| **Reading** | Personalized book/source recommendations |
| **Timeline** | SVG chronological plot of key figures |
| **Map** | Force-directed school similarity graph |

## Heterodoxy Legend

| Symbol | Level | Meaning |
|--------|-------|---------|
| ⛔ | Schismatic | Outside communion with the Catholic Church |
| ⚠️ | Condemned / Irregular | Formally condemned or canonically irregular |
| ⚡ | Caution | Requires qualification or magisterial tension |
| 📜 | Historically Superseded | Implicitly rejected by later definitions |
| ✝️ | Non-Catholic | Protestant tradition |
| ☦️ | Non-Catholic | Orthodox tradition |

## Version History

| Version | Questions | Schools | Key Additions |
|---------|-----------|---------|---------------|
| v1.0 | 154 | 105 | Original release |
| v3.0 | 134 | 85 | School consolidation, heterodoxy warnings |
| v4.0 | 119 | 88 | CRT dark mode, 88 SVGs, axis fix, 103 figures |
| v5.0 | 119 | 88 | Share card, 8 tabs, save/resume, comparison, challenge, timeline, neighbors map |

## Usage

Open `index.html` in any modern web browser. No server or internet connection required.

## License

Educational purposes. Theological content from public domain Church documents and academic sources.

---

*"In necessariis unitas, in dubiis libertas, in omnibus caritas."*
