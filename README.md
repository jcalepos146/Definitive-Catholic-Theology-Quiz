# Definitive Catholic Theology Quiz — v3.0

**[▶️ Take the Quiz](https://jcalepos146.github.io/Definitive-Catholic-Theology-Quiz/)**

A comprehensive theological assessment tool that maps your beliefs across 85 schools of Catholic thought, Protestant traditions, and Eastern Orthodoxy.

## What's New in v3.0

**School Consolidation (105 → 85 schools).** Twenty redundant or near-dead schools were merged into their parent traditions. Schools like Congruist (always a subset of Molinist), Strict Thomist (indistinguishable from Thomist in scoring), and Sedeprivationist (too thin to ever surface) were folded in. All scoring weights were recalculated — merged points add to the parent, so no information is lost, just noise removed.

**Question Set Refined (154 → 134 questions).** Redundant and low-discrimination questions were cut. The remaining 134 cover the same 10 categories with better signal-to-noise.

**Heterodoxy Warnings.** Results now flag schools that carry magisterial concerns: condemned positions (Jansenism), schismatic positions (Sedevacantism), canonically irregular groups (SSPX), historically superseded views (Gallicanism, Conciliarism), and non-Catholic traditions (Reformed, Lutheran, Anglican, Eastern Orthodox). Each warning includes the relevant documents and pastoral guidance.

**Magisterium AI Panel.** A floating button on each question opens a modal that loads the Magisterium AI assistant in an iframe, pre-loaded with a prompt about the current question's theological topic. If the iframe is blocked, it falls back to copying the prompt to clipboard and opening Magisterium in a new tab.

**Patron Saints & Figures.** Every school now has an associated historical figure with biographical information — from St. Augustine (Augustinian) to Dorothy Day (Worker-Catholic) to John Calvin (Reformed). These appear in the results alongside your top matches.

**8 Theological Axes.** Results include spectrum positions across eight dimensions, giving you a profile beyond just school rankings:
  - Grace Theology (Synergistic ↔ Monergistic)
  - Papal Authority (Conciliar/Local ↔ Ultramontane)
  - Liturgical Traditionalism (Reformist ↔ Traditional)
  - Moral Rigorism (Pastoral/Lenient ↔ Rigorist)
  - Personal Piety (Lower Intensity ↔ High Contemplative)
  - Scripture & Hermeneutics (Magisterium-first ↔ Scripture-first)
  - Justification (Forensic emphasis ↔ Participatory/union)
  - Eschatology (This-world focus ↔ Judgment & beatific end)

**Local AI Helper.** An optional side panel connects to a local LLM (Ollama, LM Studio, or any OpenAI-compatible endpoint) to explain theological concepts while you take the quiz. Includes provider auto-detection, model selection, and CORS troubleshooting instructions.

**Expanded Question Topics.** Each question now has a topic entry with a description and a suggested prompt for deeper study via Gemini or another AI, covering all 134 questions across the full theological range.

## Overview

The quiz presents 134 questions across 10 theological categories, scoring responses against 85 distinct schools, traditions, and spiritualities. Each answer assigns positive or negative points to relevant schools. Final scores are normalized against each school's maximum possible score and ranked.

## Features

- **Adaptive Quiz Length**: 25, 50, 75, 100, or all 134 questions
- **10 Theological Categories**: Scripture & Hermeneutics, Metaphysics & Philosophy, Christology & Soteriology, Grace & Predestination, Sacramental Theology, Ecclesiology & Authority, Moral Theology, Religious Orders & Spirituality, Political & Social Teaching, Contemporary Debates
- **Detailed Results**: Top theological alignments with descriptions, affirmations, and match percentages
- **Patron Saints**: Each school has an associated historical figure with era and key works
- **Heterodoxy Alerts**: Warnings for condemned, schismatic, irregular, or non-Catholic results
- **8 Theological Axes**: Spectrum positions showing where you fall on key theological dimensions
- **Magisterium AI Integration**: One-click access to AI-assisted theological explanation per question
- **Local AI Helper**: Side panel connecting to Ollama/LM Studio for real-time concept explanation
- **Question Topics & Prompts**: Study guide with AI-ready prompts for every question
- **Category-Aware Selection**: Shorter quiz lengths sample proportionally from all 10 categories
- **Mobile Responsive**: Full functionality on phones and tablets
- **Single-File Architecture**: No dependencies, no build step, no server required

## Files

- `index.html` — The complete quiz application (standalone HTML, ~350KB)
- `README.md` — This documentation

## Theological Schools (85)

### Grace & Predestination
| Code | School | Key Figure |
|------|--------|------------|
| AUG | Augustinian | St. Augustine of Hippo |
| AUGP | Strict Augustinian | Prosper of Aquitaine |
| NEOAUG | Neo-Augustinian (ressourcement) | Henri de Lubac, S.J. |
| JANS | Jansenist ⚠️ | Blaise Pascal |
| THOM | Thomist (mainstream) | St. Thomas Aquinas |
| BANEZ | Bañezian | Domingo Báñez, O.P. |
| MOL | Molinist | Luis de Molina, S.J. |
| SCOT | Scotist | Bl. John Duns Scotus |
| INFRA | Infralapsarian | Francisco Suárez, S.J. |
| SUPRA | Supralapsarian ⚡ | Gottschalk of Orbais |

### Metaphysics & Philosophy
| Code | School | Key Figure |
|------|--------|------------|
| THOMMETA | Thomist Realist | Étienne Gilson |
| NEOPLAT | Neo-Platonist | Pseudo-Dionysius |
| NOMIN | Nominalist-leaning ⚡ | William of Ockham |
| INTELL | Intellectualist | St. Thomas Aquinas |
| FRANC | Franciscan (Bonaventure) | St. Bonaventure |

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
| CHART | Carthusian | St. Bruno of Cologne |
| OCSO | Cistercian/Trappist | St. Bernard of Clairvaux |
| CSSR | Redemptorist | St. Alphonsus Liguori |
| SDB | Salesian | St. John Bosco |
| CM | Vincentian/Lazarist | St. Vincent de Paul |
| CP | Passionist | St. Paul of the Cross |
| OSM | Servite | The Seven Holy Founders |
| OPRAEM | Norbertine | St. Norbert of Xanten |
| MERC | Mercedarian | St. Peter Nolasco |

### Christology
| Code | School | Key Figure |
|------|--------|------------|
| RESSCH | Ressourcement Christology | Hans Urs von Balthasar |
| CHALMAX | Chalcedonian Maximalist | St. Cyril of Alexandria |
| KENOT | Kenoticism-sympathetic ⚡ | Sergei Bulgakov |
| PALAM | Palamite | St. Gregory Palamas |

### Sacramental Theology
| Code | School | Key Figure |
|------|--------|------------|
| TRIDSAC | Tridentine Sacramentalism | St. Charles Borromeo |
| EASTSAC | Eastern Sacramental | Nicholas Cabasilas |
| TRANSIG | Transignification-open ⚡ | Edward Schillebeeckx |
| EUCHMYST | Eucharistic Mysticism | St. Peter Julian Eymard |

### Ecclesiology & Authority
| Code | School | Key Figure |
|------|--------|------------|
| ULTRA | Ultramontane | Joseph de Maistre |
| PAPMOD | Moderate Papalist | St. Robert Bellarmine |
| PAPMIN | Papal Minimalist | Lord Acton |
| GALL | Gallican 📜 | Jacques-Bénigne Bossuet |
| CONCIL | Conciliarist 📜 | Jean Gerson |
| EASTECC | Eastern Catholic | Patriarch Maximos IV |
| SYNOD | Synodalist | Pope Francis |

### Moral Theology
| Code | School | Key Figure |
|------|--------|------------|
| THOMMOR | Thomist Natural Law | St. Thomas Aquinas |
| MANUAL | Manualist | Thomas Slater, S.J. |
| VIRTUE | Virtue Ethics | Alasdair MacIntyre |
| PERSMOR | Personalist Moral | Karol Wojtyła |
| PROP | Proportionalist ⚠️ | Richard McCormick, S.J. |
| NEOSCH | Neo-Scholastic Rigorist | Various manualists |
| CASUIST | Casuist | Various confessors |
| PROBAB | Probabilist | Bartolomé de Medina |
| TUTIOR | Tutiorist | Various rigorists |

### Political & Social Teaching
| Code | School | Key Figure |
|------|--------|------------|
| INTEG | Integralist | Card. Alfredo Ottaviani |
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
| SSPX | SSPX-leaning ⚠️ | Abp. Marcel Lefebvre |
| SEDE | Sedevacantist ⛔ | Various authors |
| ORDINAR | Ordinariate | Msgr. Jeffrey Steenson |
| ORTHOPH | Orthophile | Sergei Bulgakov |
| ECUMON | Ecumenical Monergist | Louis Bouyer |
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
| ANGLICAN | Anglican ✝️ | Thomas Cranmer |
| EORTHO | Eastern Orthodox ☦️ | St. Photios the Great |

## Schools Merged in v3.0

The following 20 schools were absorbed into parent traditions due to scoring redundancy:

| Removed | Merged Into | Reason |
|---------|-------------|--------|
| Congruist (CONG) | Molinist | 100% scoring overlap |
| Augustinian Moral (AUGMOR) | Augustinian | 100% scoring overlap |
| Thomist Sacramentology (THOMSAC) | Thomist | 100% scoring overlap |
| Strict Thomist (THOMP) | Thomist | Scoring subset, max 19 |
| Methodist (METHOD) | Anglican | 100% scoring overlap |
| Coptic Orthodox (COPTIC) | Eastern Orthodox | 2 options, placeholder |
| Oriental Orthodox (ORIENTAL) | Eastern Orthodox | 2 options, placeholder |
| Scotist univocity (SCOTMETA) | Scotist | 75% subset, max 19 |
| Eastern Liturgical (EASTLIT) | Eastern Catholic | 83% subset, max 27 |
| Lutheran-Catholic (LUTHCAT) | Ecumenical Monergist | 89% overlap |
| Hard Integralist (INTEGHARD) | Integralist | 67% subset |
| Strict Transubstantiation (TRANSUB) | Tridentine Sacramentalism | 60% subset |
| Voluntarist (VOLUNT) | Nominalist-leaning | 78% overlap |
| Sedeprivationist (SEDEPRIV) | Sedevacantist | 75% subset |
| Soft Augustinian (SEMIAUG) | Augustinian | Near-dead, max 12 |
| Augustinian Sacramentology (AUGSAC) | Augustinian | Near-dead, max 9 |
| Augustinian Order (OSA) | Augustinian | Near-dead, max 15 |
| Minimalist Sacramental (MINSAC) | Tridentine Sacramentalism | 1 option, max 2 |
| Holy Cross (CSC) | Benedictine | 2 options, max 6 |
| Camaldolese (OSBCAM) | Benedictine | 3 options, max 5 |

## Scoring System

Each answer assigns positive or negative points to relevant schools. Example:

```json
{
    "text": "Which approach best describes how Scripture should normally be interpreted?",
    "options": [
        ["Patristic exegesis (literal + spiritual senses)...", {"RESS": 3, "NEOAUG": 2, "AUG": 2, "BENED": 2}],
        ["Historical-grammatical meaning is primary...", {"THOM": 3, "DOM": 2, "STD": 2}],
        ["Historical-critical methods are useful...", {"PAPMOD": 2, "RESS": 2, "JES": 2}],
        ["The text is best read through contemporary experience...", {"PROG": 3, "PERSMOR": 2}]
    ],
    "axis_weights": {"SCRIPT": 3}
}
```

Final scores are normalized against each school's maximum possible score (the sum of the best option for that school across all questions) and ranked as percentages. The 8 theological axes are scored separately and displayed as spectrum positions.

## Heterodoxy Legend

Results may carry these warnings:

| Symbol | Level | Meaning |
|--------|-------|---------|
| ⛔ | Schismatic | Outside communion with the Catholic Church |
| ⚠️ | Condemned / Irregular | Formally condemned or canonically irregular |
| ⚡ | Caution | Requires qualification or magisterial tension |
| 📜 | Historically Superseded | Implicitly rejected by later magisterial definitions |
| ✝️ | Non-Catholic | Protestant tradition |
| ☦️ | Non-Catholic | Orthodox tradition (not in full communion) |

## Usage

Open `index.html` in any modern web browser. No server, build step, or internet connection required (except for optional AI features).

For the local AI helper, you'll need a running LLM server (Ollama, LM Studio, etc.). Click the ⚙ icon in the AI panel to configure the endpoint.

## License

This project is provided for educational purposes. Theological content draws from public domain Church documents, academic sources, and traditional teaching.

## Acknowledgments

Church Fathers and Doctors, magisterial documents (Trent, Vatican I & II, papal encyclicals), the academic theologians cited throughout the quiz, and the Catholic intellectual tradition.

---

*"In necessariis unitas, in dubiis libertas, in omnibus caritas."*
— Often attributed to St. Augustine
