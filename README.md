# Definitive Catholic Theology Quiz

A comprehensive theological assessment tool that helps users discover their alignment with various schools of Catholic thought, as well as Protestant and Eastern Orthodox traditions.

## Overview

This quiz presents 146 questions across 10 theological categories, scoring responses against 117+ distinct theological schools, traditions, and spiritualities. It includes:

- **Catholic Schools**: Thomism, Augustinianism, Molinism, Bañezianism, Scotism, and more
- **Religious Orders**: Dominican, Jesuit, Franciscan, Carmelite, Benedictine spiritualities
- **Protestant Traditions**: Reformed/Calvinist, Lutheran, Anglican, Methodist
- **Eastern Churches**: Eastern Orthodox, Coptic Orthodox, Oriental Orthodox
- **Contemporary Movements**: Ressourcement, Traditionalist, Progressive, Integralist

## Features

- **Adaptive Quiz Length**: Choose from 24, 49, 73, 97, 122, or 146 questions
- **10 Theological Categories**:
  - Scripture & Hermeneutics
  - Grace & Predestination
  - Metaphysics & Philosophy
  - Religious Orders & Spirituality
  - Sacramental Theology
  - Ecclesiology & Authority
  - Moral Theology
  - Political & Social Teaching
  - Christology & Soteriology
  - Contemporary Debates
- **Detailed Results**: Shows top theological alignments with explanations
- **Patron Saints**: Each school has associated saints/figures
- **AI Helper**: Optional integration for explaining theological concepts
- **Citations**: Academic references for further study

## Files

- `index.html` - The complete quiz application (standalone, no dependencies)
- `catholic_quiz_build.py` - Python build script for generating/modifying the quiz
- `README.md` - This documentation file

## Theological Schools Included

### Grace & Predestination
| Code | School | Key Figures |
|------|--------|-------------|
| AUG | Augustinian | St. Augustine |
| AUGP | Strict Augustinian | - |
| JANS | Jansenist | Pascal, Arnauld |
| THOM | Thomist | St. Thomas Aquinas |
| BANEZ | Bañezian | Domingo Báñez, O.P. |
| MOL | Molinist | Luis de Molina, S.J. |
| CONG | Congruist | Suárez |

### Protestant Traditions
| Code | School | Key Figures |
|------|--------|-------------|
| REFORM | Reformed/Calvinist | John Calvin |
| LUTHERAN | Lutheran | Martin Luther |
| ANGLICAN | Anglican | Thomas Cranmer |
| METHOD | Methodist | John Wesley |

### Eastern Churches
| Code | School | Key Figures |
|------|--------|-------------|
| EORTHO | Eastern Orthodox | St. Gregory Palamas |
| COPTIC | Coptic Orthodox | St. Athanasius |
| ORIENTAL | Oriental Orthodox | St. Cyril of Alexandria |
| PALAM | Palamite | St. Gregory Palamas |

### Ecclesiology
| Code | School | Description |
|------|--------|-------------|
| ULTRA | Ultramontane | Strong papal authority |
| PAPMOD | Moderate Papalist | Balanced primacy/collegiality |
| PAPMIN | Papal Minimalist | Narrow infallibility |
| GALL | Gallican | National church autonomy |
| CONCIL | Conciliarist | Councils supreme |

### Moral Theology
| Code | School | Approach |
|------|--------|----------|
| THOMMOR | Thomist Natural Law | Acts ordered to ends |
| PROBAB | Probabilist | Liberty in doubt |
| TUTIOR | Tutiorist | Safer opinion |
| PERSMOR | Personalist | Dignity-centered |

### Liturgical/Contemporary
| Code | School | Orientation |
|------|--------|-------------|
| TRAD | Traditionalist | Traditional Latin Mass |
| ROTR | Reform of Reform | Improve Novus Ordo |
| PROG | Progressive | Ongoing reform |
| RESS | Ressourcement | Return to sources |

## Usage

### Running the Quiz
Simply open `index.html` in any modern web browser. No server or installation required.

### Building/Modifying
```bash
python3 catholic_quiz_build.py
```

This generates a new `index.html` with any modifications made to the Python source.

## Question Structure

Each question has:
- **Text**: The question prompt
- **Options**: 2-8 answer choices, each with school scoring
- **Axis Weights**: Which theological axes the question measures

Example:
```python
{
    "text": "Justification consists primarily in…",
    "options": [
        ["A real interior renewal by infused grace...", {"THOM": 3, "JANS": 3, "TRIDSAC": 2}],
        ["Primarily a forensic declaration...", {"REFORM": 4, "LUTHERAN": 4}],
        # ...
    ],
    "axis_weights": {"JUST": 4, "GRACE": 1}
}
```

## Scoring System

- Each answer assigns positive or negative points to relevant schools
- Final scores are normalized and ranked
- Top 5 schools are displayed with descriptions
- Theological axes show spectrum positions (e.g., Augustinian ↔ Molinist)

## Key Theological Distinctions

### On Justification
- **Catholic (Trent)**: Infused righteousness, real interior renewal
- **Protestant**: Forensic declaration, imputed righteousness
- **Jansenist**: Follows Trent but with strict Augustinian emphasis on efficacious grace

### On the Eucharist
- **Transubstantiation**: Whole substance changes (Catholic)
- **Sacramental Union**: "In, with, under" (Lutheran)
- **Spiritual Presence**: Present to faith (Reformed)
- **Eastern**: True change, metaphysics not binding

### On Papal Authority
- **Ultramontane**: Supreme universal jurisdiction
- **Eastern Orthodox**: Primacy of honor, not jurisdiction
- **Conciliarist**: Councils can limit papal authority

### On Christology
- **Chalcedonian**: Two natures, without confusion
- **Miaphysite**: One united nature (Oriental Orthodox)

## Contributing

To add questions or schools:
1. Edit `catholic_quiz_build.py`
2. Add school to `SCHOOLS` array
3. Add description to `SCHOOL_DESC`
4. Add patron to `PATRON_SAINTS`
5. Create questions with appropriate scoring
6. Run build script

## License

This project is provided for educational purposes. Theological content draws from public domain Church documents, academic sources, and traditional teaching.

## Acknowledgments

- Church Fathers and Doctors
- Magisterial documents (Trent, Vatican I & II, Papal encyclicals)
- Academic theologians cited in the quiz
- The Catholic intellectual tradition

---

*"In essentials, unity; in doubtful matters, liberty; in all things, charity."*
— Often attributed to St. Augustine
