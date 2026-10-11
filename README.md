# The Definitive Catholic Theology Quiz — v12

**[▶️ Take the Quiz](https://jcalepos146.github.io/Definitive-Catholic-Theology-Quiz/)**

A Catholic theological assessment that compares your answers with historical theological schools and plots a separate 12-axis doctrine profile. Every result is now represented by a real historical figure with a portrait.

- **105 active questions** in plain, university-level language
- **103 detailed results** and **9 Catholic families**, each with its own representative figure and portrait
- **12 doctrine axes**, scored independently of school matching
- Four quiz depths: Essential (30), Standard (60), Advanced (75), Complete (105)

## Files

| File | Purpose |
|---|---|
| `index.html` | The quiz. Open it in any modern browser; no build step or server needed. |
| `portraits.js` | All 104 portraits (embedded JPEGs) and their image credits. Keep it next to `index.html`. Without it the quiz still works and shows the older drawn portraits. |
| `GOURGEOUS LOGO.png` | Header logo, loaded by `index.html` from the same folder. |
| `PORTRAIT_CREDITS.md` | Author, licence and source for every portrait. |
| `CHANGELOG_v9.md` … `CHANGELOG_v12.md` | Release notes. |
| `tools/portrait_fetcher.html` | Maintenance tool: finds freely licensed portraits on Wikimedia Commons and saves them as `CODE.jpg` plus `credits.json`. |
| `legacy/catholic_quiz_legacy_134q.html` | An early 134-question HTML build, kept for reference. It was previously misnamed `catholic_quiz_IMPROVED.py`; it is not Python and is not maintained. |
| `LICENSE` | MIT licence for the code. Portraits keep their own licences (see below). |

## Quiz depths

| Mode | Questions | Purpose |
|---|---:|---|
| Essential | 30 | Broad orientation; still anchors all 12 doctrine axes |
| Standard | 60 | Recommended; major schools plus a stable axis profile |
| Advanced | 75 | Finer distinctions and broader evidence |
| Complete | 105 | Every active question |

Shorter modes are not purely random: one direct anchor question for every doctrine axis is guaranteed before the remaining slots are spread across categories.

## Question bank

140 source entries, 35 retired, **105 active**. Retired entries stay in the file so old challenge links and saved progress keep working.

| # | Category | Active Questions |
|---|---|---:|
| 1 | Scripture & Hermeneutics | 7 |
| 2 | Metaphysics & Philosophy | 5 |
| 3 | Christology & Soteriology | 6 |
| 4 | Grace & Predestination | 11 |
| 5 | Sacramental Theology | 13 |
| 6 | Ecclesiology & Authority | 14 |
| 7 | Moral Theology | 7 |
| 8 | Religious Orders & Spirituality | 5 |
| 9 | Political & Social | 8 |
| 10 | Contemporary Debates | 29 |
| | **Total** | **105** |

## The 12 doctrine axes

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

Each axis uses hand-selected direct questions with explicit per-option coordinates from −1 to +1, normalized linearly. Axes do not use category weights or school scores, so a school match can legitimately differ from an axis position.

## Scoring

**School matching:** `school points × category weight × question reliability × conviction`

- Core dogmatic questions weigh modestly more; preference, spirituality and current-affairs questions weigh less.
- Conviction: Tentative 0.80×, Considered 1.00×, Strong 1.20×.
- A detailed school needs at least 4 evidence-bearing questions to enter the primary ranking. Families aggregate related schools, so a one-question micro-school cannot become the headline.

**Answer de-priming:** answers show propositions, not identity labels such as “Thomist” or “Traditionalist.” Scoring associations stay internal; representative theologians appear in the learning panels.

## Results screen

- Headline Catholic family with its representative figure's portrait, name, dates and image credit
- Closest detailed school with its figure
- Catholic families, 12 doctrine axes, and detailed rankings with small portraits beside each school
- Detailed analysis: ecclesial analogues, approach map, categories, answer review, school comparison, reading list, timeline, neighbour map
- Portrait credits for every image shown
- Portrait-format share card (1080×1350) with the headline figure

## Catholic families

| Family | Representative figure |
|---|---|
| Thomist–Dominican | St. Thomas Aquinas |
| Augustinian | St. Augustine of Hippo |
| Franciscan–Scotist | Bl. John Duns Scotus |
| Jesuit–Molinist | Luis de Molina, S.J. |
| Patristic–Ressourcement | Henri de Lubac, S.J. |
| Eastern Catholic | Met. Andrey Sheptytsky |
| Tridentine–Neo-Scholastic | Pope St. Pius V |
| Communio–Personalist | Joseph Ratzinger |
| Conciliar–Pastoral Renewal | Pope St. John XXIII |

## Detailed results and representative figures (103)

Every result has a distinct figure.

### Grace & predestination

| Code | Result | Representative figure | Era |
|---|---|---|---|
| `AUG` | Augustinian | St. Augustine of Hippo | 354–430 |
| `AUGP` | Strict Augustinian | St. Prosper of Aquitaine | c. 390–455 |
| `NEOAUG` | Neo-Augustinian (ressourcement) | Romano Guardini | 1885–1968 |
| `JANS` | Jansenist | Cornelius Jansen | 1585–1638 |
| `THOM` | Thomist (mainstream) | St. Thomas Aquinas | 1225–1274 |
| `THOMP` | Strict Thomist | Réginald Garrigou-Lagrange, O.P. | 1877–1964 |
| `BANEZ` | Bañezian | Domingo Báñez, O.P. | 1528–1604 |
| `MOL` | Molinist | Luis de Molina, S.J. | 1535–1600 |
| `CONG` | Congruist | St. Robert Bellarmine, S.J. | 1542–1621 |
| `SCOT` | Scotist | Bl. John Duns Scotus | c. 1266–1308 |
| `FRANC` | Franciscan (Bonaventure) | St. Bonaventure | 1221–1274 |
| `SUPRA` | Supralapsarian | Gottschalk of Orbais | c. 808–867 |
| `INFRA` | Infralapsarian | Francisco Suárez, S.J. | 1548–1617 |

### Orders

| Code | Result | Representative figure | Era |
|---|---|---|---|
| `DOM` | Dominican | St. Dominic | 1170–1221 |
| `JES` | Jesuit | St. Ignatius of Loyola | 1491–1556 |
| `CARM` | Carmelite | St. Teresa of Ávila | 1515–1582 |
| `BENED` | Benedictine | St. Benedict of Nursia | c. 480–547 |
| `OPUS` | Opus Dei | St. Josemaría Escrivá | 1902–1975 |
| `FRAN` | Franciscan (order) | St. Francis of Assisi | 1181–1226 |
| `ORAT` | Oratorian | St. Philip Neri | 1515–1595 |
| `CHART` | Carthusian | St. Bruno of Cologne | c. 1030–1101 |
| `OSA` | Augustinian (Order) | St. Thomas of Villanova | 1488–1555 |
| `OCSO` | Cistercian/Trappist | St. Bernard of Clairvaux | 1090–1153 |
| `CSSR` | Redemptorist | St. Alphonsus Liguori | 1696–1787 |
| `SDB` | Salesian | St. John Bosco | 1815–1888 |
| `CM` | Vincentian/Lazarist | St. Vincent de Paul | 1581–1660 |
| `CP` | Passionist | St. Paul of the Cross | 1694–1775 |
| `OSM` | Servite | St. Philip Benizi | 1233–1285 |
| `OPRAEM` | Norbertine/Premonstratensian | St. Norbert of Xanten | c. 1080–1134 |
| `MERC` | Mercedarian | St. Peter Nolasco | c. 1189–1256 |

### Metaphysics

| Code | Result | Representative figure | Era |
|---|---|---|---|
| `NEOPLAT` | Neo-Platonist | Pseudo-Dionysius the Areopagite | late 5th–early 6th c. |
| `THOMMETA` | Thomist (Realist) | Étienne Gilson | 1884–1978 |
| `SCOTMETA` | Scotist (univocity) | Gerard Manley Hopkins, S.J. | 1844–1889 |
| `VOLUNT` | Voluntarist | Gabriel Biel | c. 1420–1495 |
| `INTELL` | Intellectualist | Pierre Rousselot, S.J. | 1878–1915 |
| `PALAM` | Palamite | St. Gregory Palamas | 1296–1359 |
| `NOMINAL` | Nominalist | William of Ockham | c. 1287–1347 |

### Christology

| Code | Result | Representative figure | Era |
|---|---|---|---|
| `RESSCH` | Ressourcement Christology | Hans Urs von Balthasar | 1905–1988 |
| `CHALMAX` | Chalcedonian Maximalist | St. Maximus the Confessor | c. 580–662 |
| `KENOT` | Kenoticism-sympathetic | Sergei Bulgakov | 1871–1944 |

### Sacraments

| Code | Result | Representative figure | Era |
|---|---|---|---|
| `TRIDSAC` | Tridentine Sacramentalism | Pope St. Pius V | 1504–1572 |
| `THOMSAC` | Thomist Sacramentology | Thomas Cajetan, O.P. | 1469–1534 |
| `EASTSAC` | Eastern Sacramental | St. John Chrysostom | c. 349–407 |
| `TRANSIG` | Transignification-open | Edward Schillebeeckx, O.P. | 1914–2009 |
| `EUCHMYST` | Eucharistic Mysticism | St. Peter Julian Eymard | 1811–1868 |
| `AUGSAC` | Augustinian Sacramental | Hugh of St. Victor | c. 1096–1141 |
| `SACMIN` | Sacramental Minimalist | Huldrych Zwingli | 1484–1531 |

### Ecclesiology

| Code | Result | Representative figure | Era |
|---|---|---|---|
| `ULTRA` | Ultramontane | Joseph de Maistre | 1753–1821 |
| `PAPMOD` | Moderate Papalist | Pope St. Paul VI | 1897–1978 |
| `PAPMIN` | Papal Minimalist | Bp. Josef Fessler | 1813–1872 |
| `GALL` | Gallican | Jacques-Bénigne Bossuet | 1627–1704 |
| `CONCIL` | Conciliarist | Jean Gerson | 1363–1429 |
| `EASTECC` | Eastern Catholic | Met. Andrey Sheptytsky | 1865–1944 |
| `SYNOD` | Synodalist | Cardinal Walter Kasper | b. 1933 |
| `SEDE` | Sedevacantist | Fr. Joaquín Sáenz y Arriaga, S.J. | 1899–1976 |
| `SEDEPRIV` | Sedeprivationist | Bp. M.-L. Guérard des Lauriers, O.P. | 1898–1988 |
| `ORDINAR` | Ordinariate | Msgr. Jeffrey N. Steenson | b. 1952 |

### Moral

| Code | Result | Representative figure | Era |
|---|---|---|---|
| `THOMMOR` | Thomist Natural Law | Francisco de Vitoria, O.P. | c. 1483–1546 |
| `MANUAL` | Manualist | Jean-Pierre Gury, S.J. | 1801–1866 |
| `VIRTUE` | Virtue Ethics | Alasdair MacIntyre | 1929–2025 |
| `PERSMOR` | Personalist Moral | Pope St. John Paul II | 1920–2005 |
| `NEOSCH` | Neo-Scholastic Rigorist | Cardinal Alfredo Ottaviani | 1890–1979 |
| `CASUIST` | Casuist | Martín de Azpilcueta | 1491–1586 |
| `PROBABIL` | Probabilist | Bartolomé de Medina, O.P. | 1527–1580 |
| `TUTIOR` | Tutiorist | Daniele Concina, O.P. | 1687–1756 |
| `PROPORT` | Proportionalist | Richard A. McCormick, S.J. | 1922–2000 |
| `AUGMORAL` | Augustinian Moral | Blaise Pascal | 1623–1662 |

### Political

| Code | Result | Representative figure | Era |
|---|---|---|---|
| `INTEG` | Integralist | Bl. Pope Pius IX | 1792–1878 |
| `INTEGHARD` | Hard Integralist | Pope Boniface VIII | c. 1230–1303 |
| `INTEGSOFT` | Soft Integralist | Pope Leo XIII | 1810–1903 |
| `LIBCATH` | Liberal Catholic | John Courtney Murray, S.J. | 1904–1967 |
| `DISTRIBUT` | Distributist | G. K. Chesterton | 1874–1936 |
| `CORPCATH` | Corporatist Catholic | Heinrich Pesch, S.J. | 1854–1926 |
| `SOCDEM` | Catholic Social Democrat | Jacques Maritain | 1882–1973 |
| `LIBERTAR` | Catholic Libertarian | Michael Novak | 1933–2017 |
| `TRADNAT` | Traditionalist Nationalist | Juan Donoso Cortés | 1809–1853 |
| `CATHUNIV` | Catholic Universalist | Pope Francis | 1936–2025 |
| `WORKERCATH` | Worker-Catholic | Servant of God Dorothy Day | 1897–1980 |
| `AGRAR` | Catholic Agrarian | Hilaire Belloc | 1870–1953 |

### Liturgical / identity

| Code | Result | Representative figure | Era |
|---|---|---|---|
| `TRAD` | Traditionalist | Dietrich von Hildebrand | 1889–1977 |
| `ROTR` | Reform of the Reform | Cardinal Robert Sarah | b. 1945 |
| `PROG` | Progressive | Karl Rahner, S.J. | 1904–1984 |
| `RESS` | Ressourcement | Henri de Lubac, S.J. | 1896–1991 |
| `STD` | Standard Catholic | Ven. Fulton J. Sheen | 1895–1979 |
| `SSPX` | SSPX-leaning | Abp. Marcel Lefebvre | 1905–1991 |
| `EASTLIT` | Eastern Liturgical | Alexander Schmemann | 1921–1983 |
| `ORTHOPH` | Orthophile | Vladimir Solovyov | 1853–1900 |
| `ANTIMOD` | Anti-Modernist | Pope St. Pius X | 1835–1914 |
| `DEVPROG` | Developmental Progressive | St. John Henry Newman | 1801–1890 |
| `COMMUN` | Communio School | Joseph Ratzinger | 1927–2022 |
| `RADORTH` | Radical Orthodoxy | John Milbank | b. 1952 |
| `TRADUM` | Traditionis Custodes Compliant | Dom Gérard Calvet, O.S.B. | 1927–2008 |
| `ECUM` | Ecumenical Convergence | Yves Congar, O.P. | 1904–1995 |

### Separated brethren

| Code | Result | Representative figure | Era |
|---|---|---|---|
| `REFORM` | Reformed | John Calvin | 1509–1564 |
| `LUTHERAN` | Lutheran | Martin Luther | 1483–1546 |
| `METHOD` | Methodist | John Wesley | 1703–1791 |
| `ANGLICAN` | Anglican | Thomas Cranmer | 1489–1556 |
| `ANGLOCATH` | Anglo-Catholic | Edward Bouverie Pusey | 1800–1882 |
| `OLDCATH` | Old Catholic (Union of Utrecht type) | Ignaz von Döllinger | 1799–1890 |
| `EORTHO` | Eastern Orthodox | St. Photios the Great | c. 810–893 |
| `OORTHO` | Oriental Orthodox | St. Severus of Antioch | c. 465–538 |
| `COPTIC` | Coptic Orthodox | St. Cyril of Alexandria | c. 376–444 |
| `BAIUS` | Baianist / Baian Augustinian | Michael Baius | 1513–1589 |

## Heterodoxy legend

| Symbol | Level | Meaning |
|---|---|---|
| ⛔ | Schismatic | Outside communion with the Catholic Church |
| ⚠️ | Condemned / Irregular | Formally condemned or canonically irregular |
| ⚡ | Caution | Requires qualification or magisterial tension |
| 📜 | Historically Superseded | Implicitly rejected by later definitions |
| ✝️ | Non-Catholic | Protestant tradition |
| ☦️ | Non-Catholic | Orthodox tradition |

## Version history

| Version | Questions | Results | Key additions |
|---|---|---|---|
| v1.0 | 154 | 105 | Original release |
| v3.0 | 134 | 85 | School consolidation, heterodoxy warnings |
| v4.0 | 119 | 88 | CRT dark mode, SVG portraits, axis fix |
| v5.0 | 119 | 88 | Share card, result tabs, save/resume, comparison, challenge, timeline, neighbour map |
| v9 | 130 | 103 | Content rationalization, 18 new questions, anti-priming answer display |
| v10 | 130 | 103 | Modern scholastic UI, 12 doctrine axes, scoring overhaul |
| v11 | 105 | 103 | One distinct figure per result, plain-language rewrite, 25 questions retired, 21 scoring fixes |
| v12 | 105 | 103 | Real portraits for every result, family and share card; portrait credits |

## Usage

Open `index.html` in any modern browser, with `portraits.js` in the same folder. Works offline except for web fonts.

## Licence

Code: MIT (see `LICENSE`). Portraits are from Wikimedia Commons or were supplied by the site owner; each keeps its own licence, listed in `PORTRAIT_CREDITS.md`. Images under CC BY or CC BY-SA must keep their attribution.

---

*"In necessariis unitas, in dubiis libertas, in omnibus caritas."*
