# The Definitive Catholic Theology Quiz — v4.0

**[▶️ Take the Quiz](https://jcalepos146.github.io/Definitive-Catholic-Theology-Quiz/)**

A comprehensive theological assessment tool that maps your beliefs across 88 schools of Catholic thought, Protestant traditions, and Eastern Orthodoxy — rendered in a CRT phosphor-green dark mode with copper-engraving-style SVG portraits for every school.

![Header](header.png)

## What's New in v4.0

### Visual Overhaul: CRT Phosphor Dark Mode
The quiz is built around a CRT terminal aesthetic — phosphor green (`#39FF14`) on pure black, with scanline overlays, edge vignetting, subtle flicker animation, and monospace UI accents (`Share Tech Mono`). All 88 schools have unique SVG engraving-style portraits that render in the theme's green and glow with a pulsing phosphor halo on the results screen.

### Question Consolidation (134 → 119 questions)
Fifteen questions were merged or cut to eliminate redundancy while preserving theological depth:
- **10 merges**: TLM + Francis restrictions, Church-State + confessional state, immigration policy + hierarchy stance, moral systems + manualist value, Protestant ecumenism + Lutheran reunion, fewness of saved + Extra Ecclesiam, justification nature + sanctification growth, predestination decrees + infra/supra, prayer importance + highest form, Marian apparitions + devotional forms
- **5 cuts**: Redemptorist, Salesian, Vincentian, Servite, and Mercedarian individual spirituality questions (the general "which order resonates?" question and the 5 most theologically distinct orders remain)

### New Eucharistic Presence Question
A dedicated question on articulating the Real Presence with five options: Thomist Transubstantiation (per modum substantiae), Scotist formal-metaphysical, Eastern Mystery (beyond philosophical categories), Suárez/Bellarmine Second Scholasticism (non-corporeal sacramental mode), and Spiritual-Real Presence (Radbertus tradition, veiled objective reality received by faith).

### Category Reassignment
22 questions were moved to their proper theological categories. The "Contemporary Debates" catch-all shrank from 42 to 35 questions, while Metaphysics (now 7), Moral (now 6), and Christology (now 9) gained substance. Every question in the array is sorted contiguously by category.

### Axis Scoring Fix
The old axis formula divided raw scores by total questions × multiplier, locking every axis into a narrow 43–57% band even at maximum extremes. The new system:
- **Tracks actual axis exposure**: Only questions you answered that carry each axis count toward the denominator
- **Applies tanh curve** (`Math.tanh(normalized * 2.2)`): Compresses the mushy middle and stretches toward the fringes — 50% lean → 86%, full extreme → 94%
- **Revived PIETY axis**: Was completely dead (0 questions); now fed by 13 questions on prayer, contemplation, mysticism, confession, Marian devotion, and monastic life
- **All axes boosted**: 2–5 additional question-weights added across GRACE, PAPAL, LIT, RIGOR, ESCH, SCRIPT, JUST

### Hybrid Normalized School Scoring
Raw percentage alone let 2-question niche schools dominate. The new formula blends:
- **70% raw alignment** (points / max possible)
- **20% confidence** (exponential decay penalizing low question counts)
- **10% coverage** (bonus for schools tested across many questions)

"Standard Catholic" is excluded from rankings (shown as a baseline alignment percentage) since it appears on 150+ options and everyone scores high. Schools with fewer than 3 matching questions appear in a separate "Possible Affinities" section.

### 103 Theologian Figures in Saint Views (was 73)
30 new figures added to the "Saints & Theologians Who Held These Views" panels, bringing total saint cards to 1,089 across all 119 questions. Notable additions:
- **Bossuet** (10 questions) — Gallican liberties, papal authority, Scripture/Tradition, Church-State, Protestant controversies
- **Patristic Fathers**: St. Maximus the Confessor, St. John Damascene, St. Irenaeus of Lyon, St. Anselm of Canterbury
- **Thomist commentators**: Cajetan, John of St. Thomas (Poinsot)
- **Mystics**: Meister Eckhart, St. Catherine of Siena, St. Peter Damian, Prosper Guéranger, Dom Columba Marmion
- **Dominicans**: Yves Congar, Marie-Dominique Chenu, Francisco de Vitoria, Bartolomé de Las Casas
- **Modern voices**: Romano Guardini, Edith Stein, Adrienne von Speyr, Teilhard de Chardin, Vladimir Solovyov, Antonio Rosmini
- **Ecumenical/humanist**: Erasmus of Rotterdam, Nicholas of Cusa, Marsilio Ficino
- **Jansenist principals**: Cornelius Jansen, Antoine Arnauld
- **Spiritual writers**: St. Francis de Sales, Charles Journet

### 88 SVG Engraving Portraits
Every school result displays a unique copper-engraving-style line-art portrait of its representative figure: Dominican tonsures, Franciscan habits, Byzantine mitres, Carmelite wimples, cardinal robes, Victorian suits, pince-nez glasses, and everything in between. Portraits use CSS `var(--verd)` for strokes, automatically matching the CRT theme. Includes a glow-pulse animation and blur-to-sharp reveal on results.

### AI Removed, Copy-Prompt Retained
The built-in AI panel (Gemini, local LLM) has been removed entirely. A floating clipboard button (📋) copies a pre-built prompt — containing the current question, all options, and instructions to explain each theologically — for pasting into ChatGPT, Gemini, Claude, or [Magisterium.com](https://www.magisterium.com/).

## Overview

The quiz presents 119 questions across 10 theological categories, scoring responses against 88 distinct schools, traditions, and spiritualities. Each answer assigns positive or negative points to relevant schools. Final scores are hybrid-normalized (alignment × confidence × coverage) and ranked. Eight theological axes provide a spectrum profile.

## Features

- **CRT Dark Mode**: Phosphor green on black with scanlines, vignette, flicker, and glow effects
- **88 SVG Portraits**: Unique copper-engraving line-art for every school result
- **Adaptive Quiz Length**: 25, 50, 75, or all 119 questions
- **10 Theological Categories**: Scripture, Metaphysics, Christology, Grace, Sacraments, Ecclesiology, Moral, Orders, Political, Contemporary
- **Hybrid Normalized Scoring**: Confidence-weighted percentages prevent niche-school noise
- **8 Theological Axes**: Tanh-curved spectrums with proper per-axis normalization
- **1,089 Saint/Theologian Cards**: 103 unique figures mapped across all questions
- **"I Don't Know" Button**: Value-neutral option on every question
- **Copy Prompt**: One-click clipboard copy for external AI assistance
- **Heterodoxy Warnings**: Flags for condemned, schismatic, irregular, or non-Catholic results
- **Category Navigation**: Tab bar with per-category progress; click to jump between sections
- **Mobile Responsive**: Full functionality on phones and tablets
- **Single-File Architecture**: No dependencies, no build step, no server required

## Files

- `index.html` — The complete quiz application (standalone HTML, ~690KB)
- `header.png` — CRT-style header image with religious order heraldry
- `README.md` — This documentation

## Categories & Question Distribution

| Category | Questions | Range |
|----------|-----------|-------|
| Scripture & Hermeneutics | 4 | Q0–Q3 |
| Metaphysics & Philosophy | 7 | Q4–Q10 |
| Christology & Soteriology | 9 | Q11–Q19 |
| Grace & Predestination | 15 | Q20–Q34 |
| Sacramental Theology | 11 | Q35–Q45 |
| Ecclesiology & Authority | 15 | Q46–Q60 |
| Moral Theology | 6 | Q61–Q66 |
| Religious Orders & Spirituality | 7 | Q67–Q73 |
| Political & Social | 10 | Q74–Q83 |
| Contemporary Debates | 35 | Q84–Q118 |
| **Total** | **119** | |

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
| DOM | Dominican | St. Dominic de Guzmán |
| JES | Jesuit | St. Ignatius of Loyola |
| CARM | Carmelite | St. Teresa of Ávila |
| BENED | Benedictine | St. Benedict of Nursia |
| FRAN | Franciscan (order) | St. Francis of Assisi |
| OPUS | Opus Dei | St. Josemaría Escrivá |
| ORAT | Oratorian | St. Philip Neri |
| CHART | Carthusian | St. Romuald |
| OSA | Augustinian (Order) | St. Monica |
| OCSO | Cistercian/Trappist | St. Bernard of Clairvaux |
| CSSR | Redemptorist | St. Alphonsus Liguori |
| SDB | Salesian | St. John Bosco |
| CM | Vincentian/Lazarist | St. Vincent de Paul |
| CP | Passionist | St. Paul of the Cross |
| OSM | Servite | The Seven Holy Founders |
| OPRAEM | Norbertine | St. Norbert of Xanten |
| MERC | Mercedarian | St. Peter Nolasco |

### Ecclesiology & Authority
| Code | School | Key Figure |
|------|--------|------------|
| ULTRA | Ultramontane | Joseph de Maistre |
| PAPMOD | Moderate Papalist | St. John Henry Newman |
| PAPMIN | Papal Minimalist | Johann Adam Möhler |
| GALL | Gallican/Conciliarist 📜 | Jacques-Bénigne Bossuet |
| EASTECC | Eastern Catholic | Metropolitan Andrey Sheptytsky |
| SYNOD | Synodalist | Cardinal Walter Kasper |
| ORDINAR | Ordinariate | Msgr. Jeffrey Steenson |
| EASTLIT | Eastern Liturgical | Alexander Schmemann |

### Moral Theology
| Code | School | Key Figure |
|------|--------|------------|
| THOMMOR | Thomist Natural Law | St. Thomas Aquinas |
| MANUAL | Manualist | Henry Davis, S.J. |
| VIRTUE | Virtue Ethics | Alasdair MacIntyre |
| PERSMOR | Personalist Moral | St. John Paul II |
| NEOSCH | Neo-Scholastic Rigorist | Cardinal Alfredo Ottaviani |
| CASUIST | Casuist | Bartolomé de Medina, O.P. |
| TUTIOR | Tutiorist | Giovanni Patuzzi, O.P. |

### Political & Social Teaching
| Code | School | Key Figure |
|------|--------|------------|
| INTEG | Integralist | Pope St. Pius X |
| INTEGHARD | Hard Integralist | Archbishop Marcel Lefebvre |
| INTEGSOFT | Soft Integralist | Thomas Pink |
| LIBCATH | Liberal Catholic ⚡ | John Courtney Murray, S.J. |
| DISTRIBUT | Distributist | G.K. Chesterton |
| CORPCATH | Corporatist Catholic | Heinrich Pesch, S.J. |
| SOCDEM | Catholic Social Democrat | Jacques Maritain |
| LIBERTAR | Catholic Libertarian | Michael Novak |
| TRADNAT | Traditionalist Nationalist | Juan Donoso Cortés |
| CATHUNIV | Catholic Universalist | Pope Francis |
| WORKERCATH | Worker-Catholic | Dorothy Day |
| AGRAR | Catholic Agrarian | Hilaire Belloc |

### Liturgical & Contemporary
| Code | School | Key Figure |
|------|--------|------------|
| TRAD | Traditionalist | Dietrich von Hildebrand |
| ROTR | Reform of the Reform | Pope Benedict XVI |
| PROG | Progressive | Karl Rahner, S.J. |
| RESS | Ressourcement | Henri de Lubac, S.J. |
| STD | Standard Catholic | St. John Henry Newman |
| SSPX | SSPX-leaning ⚠️ | Archbishop Marcel Lefebvre |
| SEDE | Sedevacantist ⛔ | Bp. Guérard des Lauriers |
| ORTHOPH | Orthophile | Sergei Bulgakov |
| ANTIMOD | Anti-Modernist | Pope St. Pius X |
| DEVPROG | Developmental Progressive | St. John Henry Newman |
| COMMUN | Communio School | Joseph Ratzinger |
| RADORTH | Radical Orthodoxy | John Milbank |
| TRADUM | Traditionis Custodes Compliant | Pope Francis |

### Non-Catholic Traditions
| Code | School | Key Figure |
|------|--------|------------|
| REFORM | Reformed ✝️ | John Calvin |
| LUTHERAN | Lutheran ✝️ | Martin Luther |
| METHOD | Anglican-Methodist ✝️ | John Wesley |
| EORTHO | Eastern Orthodox ☦️ | St. Photios the Great |
| COPTIC | Oriental Orthodox ☦️ | St. Cyril of Alexandria |

## Theological Axes (8)

Each axis uses per-question normalization with a `tanh(x × 2.2)` curve, ensuring decisive answer patterns produce visible movement toward the fringes.

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

## Scoring System

Each answer assigns positive or negative points to relevant schools:

```json
{
    "text": "How should the Real Presence of Christ in the Eucharist be articulated?",
    "options": [
        ["Thomist Transubstantiation: The substance of bread/wine is wholly converted...", {"THOM": 4, "TRIDSAC": 4, "DOM": 2, "NEOSCH": 2}],
        ["Scotist Real Presence: True conversion via formal distinctions...", {"SCOT": 4, "FRAN": 3}],
        ["Eastern Mystery: A true change, but the mechanism is divine mystery...", {"EASTSAC": 4, "PALAM": 3, "EASTECC": 3}],
        ["Suárez/Bellarmine: Truly present but not as a quantitative body...", {"JES": 3, "MOL": 2, "STD": 2}],
        ["Spiritual-Real Presence: Hidden, veiled reality received by faith...", {"TRAD": 2, "TRIDSAC": 2, "BENED": 2}]
    ],
    "axis_weights": {"LIT": 2}
}
```

Final scores use hybrid normalization:

```
score = (raw_pct × 0.7) + (confidence × 0.2) + (coverage × 0.1)
```

Where `confidence = 1 - e^(-questionCount / 8)` and `coverage = min(1, questionCount / 10)`.

## Theologian Figures in Saint Views (103)

The "Saints & Theologians Who Held These Views" panel on each question draws from 103 unique figures spanning 17 centuries. Key additions in v4:

| Figure | Era | Appears On |
|--------|-----|-----------|
| Jacques-Bénigne Bossuet | 1627–1704 | 10 questions (Gallicanism, papacy, Scripture, politics) |
| Cajetan (Tommaso de Vio) | 1469–1534 | 4 questions (Real Presence, papacy, virtue ethics) |
| Yves Congar, O.P. | 1904–1995 | 5 questions (ecclesiology, Vatican II, ecumenism) |
| St. Maximus the Confessor | c. 580–662 | 4 questions (dyothelitism, Chalcedon, theosis) |
| St. John Damascene | c. 675–749 | 3 questions (icons, Eucharist, apophatic theology) |
| St. Irenaeus of Lyon | c. 130–202 | 3 questions (recapitulation, tradition, original sin) |
| St. Anselm of Canterbury | 1033–1109 | 3 questions (satisfaction, faith/reason) |
| St. Catherine of Siena | 1347–1380 | 4 questions (papal resistance, women, contemplation) |
| Meister Eckhart, O.P. | c. 1260–1328 | 3 questions (mysticism, theosis, contemplation) |
| Marsilio Ficino | 1433–1499 | 3 questions (Neoplatonism, participatory being) |
| Francisco de Vitoria, O.P. | c. 1483–1546 | 3 questions (natural law, property, immigration) |
| Bartolomé de Las Casas, O.P. | 1484–1566 | 3 questions (human rights, justice, moral norms) |
| St. Teresa Benedicta (Edith Stein) | 1891–1942 | 4 questions (personalism, Judaism, Carmel, women) |
| Pierre Teilhard de Chardin, S.J. | 1881–1955 | 3 questions (cosmic Christology, theosis, culture) |

## Heterodoxy Legend

| Symbol | Level | Meaning |
|--------|-------|---------|
| ⛔ | Schismatic | Outside communion with the Catholic Church |
| ⚠️ | Condemned / Irregular | Formally condemned or canonically irregular |
| ⚡ | Caution | Requires qualification or magisterial tension |
| 📜 | Historically Superseded | Implicitly rejected by later magisterial definitions |
| ✝️ | Non-Catholic | Protestant tradition |
| ☦️ | Non-Catholic | Orthodox tradition (not in full communion) |

## Header Image

The CRT-style header image (`header.png`) displays religious order heraldry and coat of arms in phosphor green on black with pixel-grid texture. To set it, place the image file in the repository root and it will load automatically. If the image is unavailable, the title renders as glowing text with no visual break.

## Usage

Open `index.html` in any modern web browser. No server, build step, or internet connection required.

For AI-assisted question explanation, click the 📋 button to copy a pre-built prompt, then paste it into your preferred AI tool.

## Version History

| Version | Questions | Schools | Key Changes |
|---------|-----------|---------|-------------|
| v1.0 | 154 | 105 | Original release |
| v3.0 | 134 | 85 | School consolidation, heterodoxy warnings, AI panel |
| v4.0 | 119 | 88 | CRT dark mode, 88 SVG portraits, axis fix, hybrid scoring, 103 theologian figures, category reassignment |

## License

This project is provided for educational purposes. Theological content draws from public domain Church documents, academic sources, and traditional teaching.

## Acknowledgments

Church Fathers and Doctors, magisterial documents (Trent, Vatican I & II, papal encyclicals), the academic theologians cited throughout the quiz, and the Catholic intellectual tradition.

---

*"In necessariis unitas, in dubiis libertas, in omnibus caritas."*
— Often attributed to St. Augustine
