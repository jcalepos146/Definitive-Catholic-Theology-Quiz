# The Definitive Catholic Theology Quiz — v10 Modern Scholastic UI

**[▶️ Take the Quiz](https://jcalepos146.github.io/Definitive-Catholic-Theology-Quiz/)**

A comprehensive Catholic theological assessment that compares a user's propositions with historical theological schools while separately plotting a 12-axis doctrine profile. The web build contains **130 active questions**, de-primed answer choices, representative theologians, evidence-aware school matching, and four quiz depths.

`index.html` is the canonical build. `catholic_quiz_IMPROVED.py` is retained as a legacy desktop/prototype file and does not contain the full v10 presentation layer.

---

## v10: Modern Scholastic UI + Scoring Overhaul

### New interface

The default interface has been rebuilt around a 12Axes-style information hierarchy rather than the old CRT dashboard:

- **Landing → depth selection → quiz → profile → detailed exploration**
- Warm academic “library” palette with burgundy accents
- The question itself dominates the quiz screen; category strips and numbered question grids are hidden from the ordinary interface
- School names remain hidden from answer choices
- Representative theologians and sources live in expandable learning panels
- Results are a scrolling profile: headline match, **12 doctrine axes**, Catholic families, then optional detailed analysis
- Share image redesigned as a portrait-format theological profile card
- The old DOS boot code remains in the file only as a dormant legacy feature; it is disabled by default

### Quiz depths

| Mode | Questions | Purpose |
|---|---:|---|
| Essential | 30 | Broad orientation while still anchoring all 12 doctrine axes |
| Standard | 60 | Recommended; major schools plus a stable axis profile |
| Advanced | 90 | Finer distinctions and broader evidence |
| Complete | 130 | Every active question |

Shorter modes are **not purely random**. One direct anchor question for every doctrine axis is guaranteed before the remaining slots are distributed across categories.

### Weighting overhaul

School matching and axis placement now use separate logic.

**School matching** uses:

`school points × category weight × question reliability × conviction`

Core dogmatic questions receive modestly greater weight; preferences, spirituality/lifestyle questions, and current-prudential applications receive less. This prevents questions such as favorite pope, devotional style, or current-policy judgments from moving a school result as much as grace, justification, ecclesiology, sacramental causality, or metaphysics.

Conviction is deliberately constrained:

- **Tentative:** 0.80×
- **Considered:** 1.00×
- **Strong conviction:** 1.20×

This replaces the old 0.55–1.45 range, which allowed intensity to overpower content.

**Doctrine axes** do not use category weights or school scores. Each axis has a hand-selected set of direct questions and explicit per-option coordinates from -1 to +1. Direct questions carry the most weight. Axis position is normalized linearly, without the old tanh curve.

## The 12 Doctrine Axes

| Axis | Left endpoint | Right endpoint |
|---|---|---|
| Grace & Freedom | **Synergism** | **Monergism** |
| Providence & Efficacy | **Molinism** | **Physical Premotion** |
| Metaphysics of Being | **Univocity of Being** | **Analogy of Being** |
| Primacy of Faculty | **Voluntarism** | **Intellectualism** |
| Motive of the Incarnation | **Fall-Contingent Incarnation** | **Absolute Primacy of Christ** |
| Justification | **Forensic Justification** | **Transformative Justification** |
| Sacramental Ontology | **Memorialism** | **Sacramental Realism** |
| Ecclesial Polity | **Conciliarism** | **Ultramontanism** |
| Biblical Hermeneutic | **Historical-Critical** | **Patristic-Figural** |
| Liturgical Hermeneutic | **Liturgical Reformism** | **Liturgical Traditionalism** |
| Moral Systems | **Probabilism** | **Tutiorism** |
| Eschatological Hope | **Universalist Hope** | **Restrictivism** |

The endpoint names are intentionally theological terms rather than vague cultural labels such as “liberal/conservative” or “traditional/progressive.” A user's school match can therefore disagree with one of their axis positions without creating a scoring contradiction: the school result compares a historical pattern, while the axis reports the proposition-level answers directly.

## Answer De-Priming

Answer text displays the proposition rather than an identity cue such as “Thomist,” “Molinist,” “Traditionalist,” or “Progressive.” The scoring association stays internal. Personal names may remain when they are materially part of the theological distinction, and representative theologians can be shown in the expandable learning panel.

## Question Bank

The v9 rationalization remains in place: 140 source entries, 10 retired duplicates/identity-priming prompts, and **130 active questions**.

| # | Category | Active Questions |
|---|---|---:|
| 1 | Scripture & Hermeneutics | 7 |
| 2 | Metaphysics & Philosophy | 6 |
| 3 | Christology & Soteriology | 9 |
| 4 | Grace & Predestination | 17 |
| 5 | Sacramental Theology | 16 |
| 6 | Ecclesiology & Authority | 17 |
| 7 | Moral Theology | 7 |
| 8 | Religious Orders & Spirituality | 7 |
| 9 | Political & Social | 10 |
| 10 | Contemporary Debates | 34 |
| | **Total** | **130** |

## Major Features

- 130 active questions with 30/60/90/130-question modes
- 12 proposition-level doctrine axes
- Evidence-adjusted Catholic family and detailed-school matching
- De-primed answer choices
- Representative theologians / witnesses and sources
- “I don't know / no settled position” response
- Optional conviction weighting
- Formation and Examination modes
- Category breakdown, answer review, school comparison, reading list, historical timeline, and theological-neighbor map
- Save/resume via localStorage
- Challenge-a-friend links
- Portrait-format share card
- Responsive mobile layout
- Standalone `index.html`; no build step required

---

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
