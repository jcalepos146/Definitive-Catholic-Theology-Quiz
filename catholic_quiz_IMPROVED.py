#!/usr/bin/env python3
"""
Build script for the Enhanced Catholic Theology Quiz
Generates index.html with:
- Paginated categories (max 10 pages per quiz length)
- Question citations
- AI helper integration
"""

import json
import re

# =============================================
# CATEGORY DEFINITIONS
# =============================================

CATEGORIES = [
    {
        "id": "scripture",
        "name": "Scripture & Hermeneutics",
        "shortName": "Scripture",
        "icon": "📖",
        "questionIndices": list(range(0, 3))  # Will be filled dynamically
    },
    {
        "id": "grace",
        "name": "Grace & Predestination", 
        "shortName": "Grace",
        "icon": "✨",
        "questionIndices": list(range(3, 17))
    },
    {
        "id": "metaphysics",
        "name": "Metaphysics & Philosophy",
        "shortName": "Metaphysics",
        "icon": "🔮",
        "questionIndices": list(range(17, 26))
    },
    {
        "id": "orders",
        "name": "Religious Orders & Spirituality",
        "shortName": "Orders",
        "icon": "🕯️",
        "questionIndices": list(range(26, 46))
    },
    {
        "id": "sacraments",
        "name": "Sacramental Theology",
        "shortName": "Sacraments",
        "icon": "🍷",
        "questionIndices": list(range(46, 56))
    },
    {
        "id": "ecclesiology",
        "name": "Ecclesiology & Authority",
        "shortName": "Ecclesiology",
        "icon": "⛪",
        "questionIndices": list(range(56, 72))
    },
    {
        "id": "moral",
        "name": "Moral Theology",
        "shortName": "Moral",
        "icon": "⚖️",
        "questionIndices": list(range(72, 85))
    },
    {
        "id": "political",
        "name": "Political & Social Teaching",
        "shortName": "Political",
        "icon": "🏛️",
        "questionIndices": list(range(85, 100))
    },
    {
        "id": "christology",
        "name": "Christology & Soteriology",
        "shortName": "Christology",
        "icon": "✝️",
        "questionIndices": list(range(100, 112))
    },
    {
        "id": "contemporary",
        "name": "Contemporary Debates",
        "shortName": "Contemporary",
        "icon": "📰",
        "questionIndices": list(range(112, 132))  # Now includes new questions 127-131
    }
]

# =============================================
# CITATIONS DATABASE - keyed by question index
# =============================================

CITATIONS = {
    0: [
        {"title": "Dei Verbum", "author": "Second Vatican Council", "year": 1965, "note": "Constitution on Divine Revelation"},
        {"title": "Summa Theologiae I-II, q. 106-108", "author": "St. Thomas Aquinas"},
        {"title": "Scripture in the Tradition", "author": "Yves Congar, O.P.", "year": 1964}
    ],
    1: [
        {"title": "Medieval Exegesis (4 vols)", "author": "Henri de Lubac", "year": 1959},
        {"title": "Divino Afflante Spiritu", "author": "Pope Pius XII", "year": 1943},
        {"title": "Interpretation of the Bible in the Church", "author": "Pontifical Biblical Commission", "year": 1993}
    ],
    2: [
        {"title": "The Senses of Scripture", "author": "Raymond Brown", "year": 1955},
        {"title": "Providentissimus Deus", "author": "Pope Leo XIII", "year": 1893}
    ],
    3: [
        {"title": "Concordia liberi arbitrii", "author": "Luis de Molina, S.J.", "year": 1588},
        {"title": "Commentary on ST I", "author": "Domingo Báñez, O.P.", "year": 1584},
        {"title": "De gratia et libero arbitrio", "author": "St. Augustine", "year": 426},
        {"title": "Grace and Freedom", "author": "Bernard Lonergan, S.J.", "year": 1971}
    ],
    4: [
        {"title": "Summa Theologiae I, q. 23", "author": "St. Thomas Aquinas", "note": "On Predestination"},
        {"title": "De praedestinatione sanctorum", "author": "St. Augustine", "year": 429},
        {"title": "Ordinatio I, d. 41", "author": "Bl. John Duns Scotus"}
    ],
    5: [
        {"title": "Surnaturel", "author": "Henri de Lubac", "year": 1946},
        {"title": "The Mystery of the Supernatural", "author": "Henri de Lubac", "year": 1967},
        {"title": "Humani Generis", "author": "Pope Pius XII", "year": 1950}
    ],
    6: [
        {"title": "Council of Trent, Session VI", "year": 1547, "note": "Decree on Justification"},
        {"title": "De perseverantiae dono", "author": "St. Augustine", "year": 429}
    ],
    7: [
        {"title": "Concordia", "author": "Luis de Molina, S.J.", "year": 1588},
        {"title": "Summa Theologiae I, q. 14, a. 13", "author": "St. Thomas Aquinas"}
    ],
    8: [
        {"title": "De auxiliis divinae gratiae", "author": "Congregation de Auxiliis", "year": 1607},
        {"title": "Grace, Predestination and Freewill", "author": "Reginald Garrigou-Lagrange, O.P.", "year": 1936}
    ],
    9: [
        {"title": "Summa Theologiae I-II, q. 109-114", "author": "St. Thomas Aquinas"},
        {"title": "The Theology of Grace", "author": "Joseph Pohle", "year": 1911}
    ],
    10: [
        {"title": "Augustinus", "author": "Cornelius Jansen", "year": 1640},
        {"title": "Cum occasione", "author": "Pope Innocent X", "year": 1653}
    ],
    # Metaphysics
    17: [
        {"title": "Summa Theologiae I, q. 19", "author": "St. Thomas Aquinas", "note": "On the Will of God"},
        {"title": "Ordinatio I, d. 8", "author": "Bl. John Duns Scotus"},
        {"title": "Quodlibetal Questions", "author": "William of Ockham"}
    ],
    18: [
        {"title": "Natural Law and Natural Rights", "author": "John Finnis", "year": 1980},
        {"title": "The Sources of Christian Ethics", "author": "Servais Pinckaers, O.P.", "year": 1985},
        {"title": "Veritatis Splendor", "author": "Pope John Paul II", "year": 1993}
    ],
    19: [
        {"title": "De ente et essentia", "author": "St. Thomas Aquinas"},
        {"title": "Ordinatio II, d. 3", "author": "Bl. John Duns Scotus"},
        {"title": "Metalogicon", "author": "John of Salisbury", "year": 1159}
    ],
    20: [
        {"title": "The Analogy of Being", "author": "Erich Przywara", "year": 1932},
        {"title": "Ordinatio I, d. 3 & d. 8", "author": "Bl. John Duns Scotus"}
    ],
    # Religious Orders
    26: [
        {"title": "Rule of St. Benedict", "author": "St. Benedict of Nursia", "year": 530},
        {"title": "Spiritual Exercises", "author": "St. Ignatius of Loyola", "year": 1548},
        {"title": "Interior Castle", "author": "St. Teresa of Ávila", "year": 1577}
    ],
    27: [
        {"title": "Summa de vita spirituali", "author": "St. Thomas Aquinas"},
        {"title": "Ascent of Mount Carmel", "author": "St. John of the Cross", "year": 1585}
    ],
    # Sacraments
    46: [
        {"title": "Council of Trent, Session XIII", "year": 1551, "note": "Decree on the Eucharist"},
        {"title": "Mysterium Fidei", "author": "Pope Paul VI", "year": 1965},
        {"title": "Summa Theologiae III, q. 75-77", "author": "St. Thomas Aquinas"}
    ],
    47: [
        {"title": "Mediator Dei", "author": "Pope Pius XII", "year": 1947},
        {"title": "The Spirit of the Liturgy", "author": "Joseph Ratzinger", "year": 2000},
        {"title": "Sacrosanctum Concilium", "year": 1963}
    ],
    48: [
        {"title": "Summa Theologiae III, q. 62", "author": "St. Thomas Aquinas"},
        {"title": "In IV Sent., d. 1", "author": "Bl. John Duns Scotus"}
    ],
    # Ecclesiology
    56: [
        {"title": "Pastor Aeternus", "year": 1870, "note": "Vatican I on Papal Primacy"},
        {"title": "Lumen Gentium", "year": 1964, "note": "Chapter III on Hierarchy"},
        {"title": "The Limits of the Papacy", "author": "Patrick Granfield", "year": 1987}
    ],
    57: [
        {"title": "Pastor Aeternus, Chapter 4", "year": 1870},
        {"title": "Infallibility", "author": "Peter Chirico", "year": 1977}
    ],
    # Moral
    72: [
        {"title": "Veritatis Splendor", "author": "Pope John Paul II", "year": 1993},
        {"title": "The Acting Person", "author": "Karol Wojtyła", "year": 1969}
    ],
    73: [
        {"title": "Theologia Moralis", "author": "St. Alphonsus Liguori", "year": 1748},
        {"title": "Provinciales", "author": "Blaise Pascal", "year": 1656}
    ],
    # Political
    85: [
        {"title": "Dignitatis Humanae", "year": 1965},
        {"title": "Quas Primas", "author": "Pope Pius XI", "year": 1925}
    ],
    86: [
        {"title": "Rerum Novarum", "author": "Pope Leo XIII", "year": 1891},
        {"title": "Quadragesimo Anno", "author": "Pope Pius XI", "year": 1931},
        {"title": "What's Wrong with the World", "author": "G.K. Chesterton", "year": 1910}
    ],
    # Christology
    100: [
        {"title": "Council of Chalcedon", "year": 451},
        {"title": "Summa Theologiae III, q. 1-26", "author": "St. Thomas Aquinas"},
        {"title": "Cur Deus Homo", "author": "St. Anselm", "year": 1098}
    ],
    # Contemporary
    112: [
        {"title": "Sacrosanctum Concilium", "year": 1963},
        {"title": "Traditionis Custodes", "author": "Pope Francis", "year": 2021}
    ],
    113: [
        {"title": "Amoris Laetitia", "author": "Pope Francis", "year": 2016},
        {"title": "Familiaris Consortio", "author": "Pope John Paul II", "year": 1981}
    ],
    114: [
        {"title": "Nostra Aetate", "year": 1965},
        {"title": "Dominus Iesus", "author": "CDF", "year": 2000}
    ]
}

# Default citation for questions without specific ones
DEFAULT_CITATIONS = [
    {"title": "Catechism of the Catholic Church", "year": 1992},
    {"title": "Denzinger-Hünermann", "note": "Enchiridion Symbolorum"},
    {"title": "New Catholic Encyclopedia", "year": 2003}
]

# Citations for the 5 NEW questions (127-131, which become indices after adding)
CITATIONS[127] = [
    {"title": "De gratia et praedestinatione", "author": "Garrigou-Lagrange, O.P."},
    {"title": "Summa Theologiae Suppl., q. 72", "author": "St. Thomas Aquinas", "note": "On the number of the elect"},
    {"title": "City of God XXI", "author": "St. Augustine"},
    {"title": "Dare We Hope That All Men Be Saved?", "author": "Hans Urs von Balthasar", "year": 1988}
]
CITATIONS[128] = [
    {"title": "Quanto conficiamur moerore", "author": "Pope Pius IX", "year": 1863},
    {"title": "Lumen Gentium §14-16", "note": "Vatican II on Church membership"},
    {"title": "Letter to Fr. Leonard Feeney", "author": "Holy Office", "year": 1949},
    {"title": "The One Mediator, The Saints, and Mary", "note": "Lutheran-Catholic Dialogue", "year": 1992}
]
CITATIONS[129] = [
    {"title": "Pastor Aeternus", "note": "Vatican I", "year": 1870},
    {"title": "Haec Sancta", "note": "Council of Constance", "year": 1415},
    {"title": "An Essay on the Development of Christian Doctrine", "author": "John Henry Newman", "year": 1845},
    {"title": "The Limits of the Papacy", "author": "Patrick Granfield", "year": 1987}
]
CITATIONS[130] = [
    {"title": "Summa Theologiae I, q. 1", "author": "St. Thomas Aquinas", "note": "On sacred doctrine as science"},
    {"title": "De Trinitate", "author": "St. Augustine"},
    {"title": "The Mystical Theology of the Eastern Church", "author": "Vladimir Lossky", "year": 1944},
    {"title": "Ordinatio Prol.", "author": "Bl. John Duns Scotus"}
]
CITATIONS[131] = [
    {"title": "Orientalium Ecclesiarum", "note": "Vatican II", "year": 1964},
    {"title": "Ut Unum Sint", "author": "Pope John Paul II", "year": 1995},
    {"title": "For the Life of the World", "author": "Alexander Schmemann", "year": 1963},
    {"title": "The Byzantine Liturgy", "author": "Hans-Joachim Schulz", "year": 1986}
]

def get_citations_for_question(index):
    """Get citations for a question, with fallback to defaults"""
    return CITATIONS.get(index, DEFAULT_CITATIONS)

def generate_html():
    """Generate the complete enhanced quiz HTML"""
    
    # Read the original file to extract data (use 132-question version if available)
    import os
    source_file = '/home/claude/quiz/original_132.html' if os.path.exists('/home/claude/quiz/original_132.html') else '/home/claude/quiz/original.html'
    with open(source_file, 'r', encoding='utf-8') as f:
        original = f.read()
    print(f"Using source: {source_file}")
    
    # Extract the QUESTIONS array from original
    questions_match = re.search(r'const QUESTIONS = \[(.*?)\];', original, re.DOTALL)
    schools_match = re.search(r'const SCHOOLS = \[(.*?)\];', original, re.DOTALL)
    school_desc_match = re.search(r'const SCHOOL_DESC = \{(.*?)\};', original, re.DOTALL)
    patron_match = re.search(r'const PATRON_SAINTS = \{(.*?)\};', original, re.DOTALL)
    
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Definitive Catholic Theology Quiz</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Crimson+Pro:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold: #c9a227;
            --gold-light: #e8d48a;
            --crimson: #8b1538;
            --crimson-dark: #5c0d25;
            --ivory: #f5f2eb;
            --parchment: #ede4d3;
            --ink: #1a1a1a;
            --ink-light: #3d3d3d;
            --shadow: rgba(0,0,0,0.15);
            --blue: #2a5298;
            --blue-light: #4a7bc8;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Crimson Pro', Georgia, serif;
            background: linear-gradient(145deg, var(--ivory) 0%, var(--parchment) 100%);
            min-height: 100vh;
            color: var(--ink);
            line-height: 1.6;
        }
        
        /* Main Layout */
        .main-container { display: flex; min-height: 100vh; }
        .quiz-panel {
            flex: 1;
            max-width: 900px;
            padding: 2rem;
            margin: 0 auto;
            transition: max-width 0.3s ease;
        }
        .quiz-panel.with-ai { max-width: 650px; margin-right: 420px; }
        
        /* AI Helper Panel */
        .ai-panel {
            width: 400px;
            background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
            border-left: 3px solid var(--gold);
            display: none;
            flex-direction: column;
            position: fixed;
            right: 0;
            top: 0;
            height: 100vh;
            z-index: 1000;
            box-shadow: -5px 0 25px rgba(0,0,0,0.3);
        }
        .ai-panel.open { display: flex; }
        .ai-header {
            padding: 1.25rem;
            background: linear-gradient(135deg, var(--crimson-dark), #1a1a2e);
            border-bottom: 1px solid var(--gold);
            position: relative;
        }
        .ai-header h3 {
            font-family: 'Cinzel', serif;
            color: var(--gold-light);
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .ai-close {
            position: absolute;
            right: 1rem;
            top: 50%;
            transform: translateY(-50%);
            background: transparent;
            border: 1px solid var(--gold-light);
            color: var(--gold-light);
            width: 28px;
            height: 28px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.2s;
        }
        .ai-close:hover { background: var(--gold); color: var(--ink); }
        .ai-messages {
            flex: 1;
            overflow-y: auto;
            padding: 1rem;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        .ai-message {
            padding: 1rem;
            border-radius: 12px;
            font-size: 0.95rem;
            line-height: 1.6;
            animation: fadeIn 0.3s ease;
        }
        .ai-message.user {
            background: rgba(201, 162, 39, 0.15);
            border: 1px solid var(--gold);
            color: var(--gold-light);
            margin-left: 1rem;
        }
        .ai-message.assistant {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.1);
            color: #e8e8e8;
            margin-right: 1rem;
        }
        .ai-message.system {
            background: rgba(139, 21, 56, 0.2);
            border: 1px solid var(--crimson);
            color: #f0d0d8;
            font-style: italic;
            text-align: center;
            font-size: 0.9rem;
        }
        .ai-input-area {
            padding: 1rem;
            border-top: 1px solid rgba(255,255,255,0.1);
            background: rgba(0,0,0,0.2);
        }
        .ai-input-wrapper { display: flex; gap: 0.5rem; }
        .ai-input {
            flex: 1;
            padding: 0.75rem 1rem;
            border: 1px solid var(--gold);
            border-radius: 8px;
            background: rgba(255,255,255,0.05);
            color: #fff;
            font-family: inherit;
            font-size: 0.95rem;
            resize: none;
        }
        .ai-input:focus {
            outline: none;
            border-color: var(--gold-light);
            background: rgba(255,255,255,0.1);
        }
        .ai-input::placeholder { color: rgba(255,255,255,0.4); }
        .ai-send {
            padding: 0.75rem 1.25rem;
            background: linear-gradient(135deg, var(--gold), var(--gold-light));
            border: none;
            border-radius: 8px;
            color: var(--ink);
            font-family: 'Cinzel', serif;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }
        .ai-send:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(201, 162, 39, 0.4); }
        .ai-send:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
        .ai-typing {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 1rem;
            color: rgba(255,255,255,0.6);
            font-style: italic;
        }
        .ai-typing .dots span {
            display: inline-block;
            width: 6px;
            height: 6px;
            background: var(--gold);
            border-radius: 50%;
            animation: bounce 1.4s ease-in-out infinite;
            margin: 0 2px;
        }
        .ai-typing .dots span:nth-child(2) { animation-delay: 0.2s; }
        .ai-typing .dots span:nth-child(3) { animation-delay: 0.4s; }
        @keyframes bounce {
            0%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-8px); }
        }
        
        /* AI Toggle Button */
        .ai-toggle {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--blue), var(--blue-light));
            border: 2px solid var(--gold);
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(42, 82, 152, 0.4);
            transition: all 0.3s ease;
            z-index: 999;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .ai-toggle:hover { transform: scale(1.1); box-shadow: 0 6px 25px rgba(42, 82, 152, 0.6); }
        .ai-toggle.hidden { display: none; }
        
        /* Header */
        header { text-align: center; padding: 2.5rem 1rem; border-bottom: 1px solid var(--gold-light); margin-bottom: 1.5rem; }
        header h1 { font-family: 'Cinzel', serif; font-size: 2.2rem; font-weight: 600; color: var(--crimson); letter-spacing: 0.05em; margin-bottom: 0.5rem; }
        header .subtitle { font-size: 1.05rem; color: var(--ink-light); font-style: italic; }
        .cross-divider { display: flex; align-items: center; justify-content: center; margin: 1.25rem 0; color: var(--gold); }
        .cross-divider::before, .cross-divider::after { content: ''; flex: 1; height: 1px; background: linear-gradient(90deg, transparent, var(--gold-light), transparent); max-width: 150px; }
        .cross-divider span { padding: 0 1rem; font-size: 1.5rem; }
        
        /* Start Screen */
        .start-screen { text-align: center; padding: 2rem; }
        .start-screen h2 { font-family: 'Cinzel', serif; font-size: 1.6rem; color: var(--crimson); margin-bottom: 1.25rem; }
        .start-screen p { font-size: 1.05rem; color: var(--ink-light); margin-bottom: 1rem; max-width: 600px; margin-left: auto; margin-right: auto; }
        .stats { display: flex; justify-content: center; gap: 2rem; margin: 1.5rem 0; flex-wrap: wrap; }
        .stat { text-align: center; }
        .stat-value { font-family: 'Cinzel', serif; font-size: 2.2rem; color: var(--gold); font-weight: 700; }
        .stat-label { font-size: 0.85rem; color: var(--ink-light); text-transform: uppercase; letter-spacing: 0.1em; }
        
        /* Quiz Length Selector */
        .quiz-length-section { margin: 1.5rem 0; padding: 1.25rem; background: white; border-radius: 12px; box-shadow: 0 2px 10px var(--shadow); border: 1px solid var(--gold-light); }
        .quiz-length-section h3 { font-family: 'Cinzel', serif; font-size: 1.1rem; color: var(--crimson); margin-bottom: 1rem; }
        .length-options { display: flex; justify-content: center; gap: 0.6rem; flex-wrap: wrap; }
        .length-option { cursor: pointer; }
        .length-option input { display: none; }
        .length-card { display: flex; flex-direction: column; align-items: center; padding: 0.85rem 1rem; border: 2px solid var(--gold-light); border-radius: 8px; transition: all 0.2s ease; min-width: 70px; }
        .length-card:hover { border-color: var(--gold); transform: translateY(-2px); }
        .length-option input:checked + .length-card { border-color: var(--crimson); background: linear-gradient(135deg, rgba(139, 21, 56, 0.08), rgba(201, 162, 39, 0.08)); box-shadow: 0 2px 8px rgba(139, 21, 56, 0.2); }
        .length-number { font-family: 'Cinzel', serif; font-size: 1.3rem; font-weight: 600; color: var(--crimson); }
        .length-label { font-size: 0.8rem; color: var(--ink-light); text-align: center; }
        .length-label small { color: var(--gold); }
        .length-note { font-size: 0.85rem; color: var(--ink-light); font-style: italic; margin-top: 1rem; margin-bottom: 0; }
        
        .start-btn { font-family: 'Cinzel', serif; font-size: 1.1rem; padding: 0.9rem 2.5rem; background: linear-gradient(135deg, var(--crimson), var(--crimson-dark)); color: white; border: none; border-radius: 8px; cursor: pointer; transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 1rem; }
        .start-btn:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(139, 21, 56, 0.4); }
        
        /* Category Navigation */
        .category-nav {
            display: flex;
            gap: 0.4rem;
            flex-wrap: wrap;
            justify-content: center;
            margin-bottom: 1.5rem;
            padding: 1rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px var(--shadow);
            border: 1px solid var(--gold-light);
        }
        .cat-btn {
            font-family: 'Cinzel', serif;
            font-size: 0.7rem;
            padding: 0.4rem 0.7rem;
            background: transparent;
            border: 1px solid var(--gold-light);
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
            color: var(--ink-light);
            position: relative;
            text-align: center;
        }
        .cat-btn:hover { border-color: var(--gold); color: var(--ink); }
        .cat-btn.active { background: var(--crimson); border-color: var(--crimson); color: white; }
        .cat-btn.completed::after {
            content: '✓';
            position: absolute;
            top: -5px;
            right: -5px;
            background: var(--gold);
            color: var(--ink);
            width: 14px;
            height: 14px;
            border-radius: 50%;
            font-size: 0.55rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .cat-progress { font-size: 0.6rem; opacity: 0.8; display: block; margin-top: 2px; }
        .cat-icon { font-size: 1rem; display: block; margin-bottom: 2px; }
        
        /* Progress */
        .progress-section { background: white; border-radius: 8px; padding: 1.25rem; margin-bottom: 1.5rem; box-shadow: 0 2px 10px var(--shadow); border: 1px solid var(--gold-light); }
        .progress-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem; }
        .progress-text { font-family: 'Cinzel', serif; font-size: 0.95rem; color: var(--crimson); }
        .progress-count { font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; color: var(--ink-light); }
        .progress-bar { height: 8px; background: var(--parchment); border-radius: 4px; overflow: hidden; }
        .progress-fill { height: 100%; background: linear-gradient(90deg, var(--crimson), var(--gold)); border-radius: 4px; transition: width 0.4s ease; }
        
        /* Question Card */
        .question-card { background: white; border-radius: 12px; padding: 1.75rem; margin-bottom: 1.5rem; box-shadow: 0 4px 20px var(--shadow); border: 1px solid var(--gold-light); position: relative; animation: fadeIn 0.4s ease; }
        .question-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, var(--crimson), var(--gold), var(--crimson)); border-radius: 12px 12px 0 0; }
        .question-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem; }
        .question-number { font-family: 'Cinzel', serif; font-size: 0.8rem; color: var(--gold); letter-spacing: 0.1em; text-transform: uppercase; }
        .question-category-tag {
            font-size: 0.65rem;
            padding: 0.2rem 0.5rem;
            background: linear-gradient(135deg, rgba(139, 21, 56, 0.1), rgba(201, 162, 39, 0.1));
            border: 1px solid var(--gold-light);
            border-radius: 12px;
            color: var(--crimson);
            font-family: 'Cinzel', serif;
        }
        .question-text { font-size: 1.2rem; font-weight: 500; color: var(--ink); margin-bottom: 1.25rem; line-height: 1.5; }
        
        /* Options */
        .options { display: flex; flex-direction: column; gap: 0.65rem; }
        .option { display: flex; align-items: flex-start; padding: 0.9rem 1.1rem; background: var(--ivory); border: 2px solid transparent; border-radius: 8px; cursor: pointer; transition: all 0.25s ease; }
        .option:hover { background: var(--parchment); border-color: var(--gold-light); transform: translateX(4px); }
        .option.selected { background: linear-gradient(135deg, rgba(139, 21, 56, 0.08), rgba(201, 162, 39, 0.08)); border-color: var(--gold); box-shadow: 0 2px 8px rgba(201, 162, 39, 0.2); }
        .option input { display: none; }
        .option-radio { width: 20px; height: 20px; min-width: 20px; border: 2px solid var(--ink-light); border-radius: 50%; margin-right: 0.9rem; margin-top: 2px; display: flex; align-items: center; justify-content: center; transition: all 0.25s ease; }
        .option.selected .option-radio { border-color: var(--crimson); background: var(--crimson); }
        .option.selected .option-radio::after { content: ''; width: 7px; height: 7px; background: white; border-radius: 50%; }
        .option-text { font-size: 1rem; line-height: 1.5; color: var(--ink); }
        
        /* Citation */
        .citation-section { margin-top: 1.5rem; padding-top: 1rem; border-top: 1px dashed var(--gold-light); }
        .citation-toggle {
            font-family: 'Cinzel', serif;
            font-size: 0.8rem;
            color: var(--blue);
            background: transparent;
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 0;
            transition: color 0.2s;
        }
        .citation-toggle:hover { color: var(--blue-light); }
        .citation-toggle .arrow { transition: transform 0.2s; }
        .citation-toggle.open .arrow { transform: rotate(90deg); }
        .citation-content {
            display: none;
            margin-top: 0.75rem;
            padding: 1rem;
            background: rgba(42, 82, 152, 0.05);
            border-radius: 8px;
            border-left: 3px solid var(--blue);
        }
        .citation-content.open { display: block; animation: fadeIn 0.3s ease; }
        .citation-content h4 { font-family: 'Cinzel', serif; font-size: 0.85rem; color: var(--blue); margin-bottom: 0.75rem; }
        .citation-content ul { list-style: none; padding: 0; }
        .citation-content li { font-size: 0.85rem; color: var(--ink-light); margin-bottom: 0.5rem; padding-left: 1.5rem; position: relative; }
        .citation-content li::before { content: '📖'; position: absolute; left: 0; font-size: 0.75rem; }
        .citation-content a { color: var(--blue); text-decoration: none; }
        .citation-content a:hover { text-decoration: underline; }
        .ai-explain-btn {
            margin-top: 0.75rem;
            font-family: 'Cinzel', serif;
            font-size: 0.75rem;
            padding: 0.45rem 0.9rem;
            background: linear-gradient(135deg, var(--blue), var(--blue-light));
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
        }
        .ai-explain-btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(42, 82, 152, 0.3); }
        
        /* Navigation */
        .navigation { display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap; }
        .nav-btn { font-family: 'Cinzel', serif; font-size: 0.95rem; padding: 0.7rem 1.75rem; border: 2px solid var(--crimson); border-radius: 6px; cursor: pointer; transition: all 0.25s ease; text-transform: uppercase; letter-spacing: 0.05em; }
        .nav-btn.primary { background: var(--crimson); color: white; }
        .nav-btn.primary:hover { background: var(--crimson-dark); transform: translateY(-2px); box-shadow: 0 4px 12px rgba(139, 21, 56, 0.3); }
        .nav-btn.secondary { background: transparent; color: var(--crimson); }
        .nav-btn.secondary:hover { background: var(--crimson); color: white; }
        .nav-btn:disabled { opacity: 0.4; cursor: not-allowed; transform: none !important; }
        
        /* Question Nav Dots */
        .question-nav { display: flex; flex-wrap: wrap; gap: 0.4rem; justify-content: center; margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid var(--gold-light); }
        .q-dot { width: 28px; height: 28px; border-radius: 50%; border: 2px solid var(--gold-light); background: white; font-family: 'JetBrains Mono', monospace; font-size: 0.6rem; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.2s ease; color: var(--ink-light); }
        .q-dot:hover { border-color: var(--gold); transform: scale(1.1); }
        .q-dot.answered { background: var(--gold); border-color: var(--gold); color: white; }
        .q-dot.current { border-color: var(--crimson); box-shadow: 0 0 0 3px rgba(139, 21, 56, 0.2); }
        
        /* Results */
        .results-screen { display: none; }
        .results-header { text-align: center; margin-bottom: 1.5rem; }
        .results-header h2 { font-family: 'Cinzel', serif; font-size: 1.8rem; color: var(--crimson); margin-bottom: 0.5rem; }
        
        .top-match { background: linear-gradient(135deg, var(--crimson), var(--crimson-dark)); color: white; border-radius: 12px; padding: 2rem; margin-bottom: 1.5rem; text-align: center; position: relative; overflow: hidden; }
        .top-match::before { content: '✝'; position: absolute; top: -20px; right: -20px; font-size: 120px; opacity: 0.1; color: var(--gold); }
        .top-match-label { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.15em; opacity: 0.8; margin-bottom: 0.5rem; }
        .top-match-name { font-family: 'Cinzel', serif; font-size: 1.8rem; font-weight: 600; margin-bottom: 0.5rem; color: var(--gold-light); }
        .top-match-score { font-family: 'JetBrains Mono', monospace; font-size: 0.95rem; opacity: 0.9; margin-bottom: 1.25rem; }
        .top-match-summary { font-size: 1.05rem; line-height: 1.6; font-style: italic; max-width: 550px; margin: 0 auto 1.25rem; }
        .top-match-affirmations { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.4rem; }
        .affirmation-tag { background: rgba(255,255,255,0.15); padding: 0.35rem 0.7rem; border-radius: 20px; font-size: 0.8rem; }
        
        .patron-section { text-align: center; padding: 1.25rem; background: rgba(255,255,255,0.1); border-radius: 8px; margin-top: 1.25rem; }
        .patron-label { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.8; margin-bottom: 0.4rem; }
        .patron-name { font-family: 'Cinzel', serif; font-size: 1.1rem; }
        .patron-era { font-style: italic; opacity: 0.8; font-size: 0.9rem; }
        
        /* Tabs */
        .tabs { display: flex; gap: 0.4rem; margin-bottom: 1.25rem; justify-content: center; flex-wrap: wrap; }
        .tab-btn { font-family: 'Cinzel', serif; font-size: 0.85rem; padding: 0.55rem 1.25rem; background: transparent; border: 2px solid var(--gold-light); border-radius: 6px; cursor: pointer; transition: all 0.2s ease; color: var(--ink); }
        .tab-btn:hover { border-color: var(--gold); }
        .tab-btn.active { background: var(--crimson); border-color: var(--crimson); color: white; }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        
        /* Rankings */
        .rankings-card, .axes-card { background: white; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; box-shadow: 0 4px 20px var(--shadow); border: 1px solid var(--gold-light); }
        .rankings-card h3, .axes-card h3 { font-family: 'Cinzel', serif; font-size: 1.2rem; color: var(--crimson); margin-bottom: 1.25rem; text-align: center; }
        .rankings-table { width: 100%; border-collapse: collapse; }
        .rankings-table th { font-family: 'Cinzel', serif; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--ink-light); padding: 0.65rem; text-align: left; border-bottom: 2px solid var(--gold-light); }
        .rankings-table td { padding: 0.65rem; border-bottom: 1px solid var(--parchment); }
        .rankings-table tr:hover { background: var(--ivory); }
        .rank-num { font-family: 'Cinzel', serif; font-weight: 600; color: var(--gold); width: 50px; }
        .rank-num.top-3 { color: var(--crimson); }
        .school-name { font-weight: 500; }
        .score-bar-container { width: 100%; max-width: 180px; }
        .score-bar { height: 8px; background: var(--parchment); border-radius: 4px; overflow: hidden; }
        .score-bar-fill { height: 100%; background: linear-gradient(90deg, var(--crimson), var(--gold)); border-radius: 4px; }
        .score-value { font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: var(--ink-light); margin-top: 2px; }
        
        /* Axes */
        .axis-row { margin-bottom: 1.25rem; }
        .axis-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem; }
        .axis-name { font-weight: 500; color: var(--ink); font-size: 0.95rem; }
        .axis-score { font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: var(--ink-light); }
        .axis-bar { position: relative; height: 22px; background: var(--parchment); border-radius: 11px; overflow: hidden; }
        .axis-labels { position: absolute; top: 0; left: 0; right: 0; bottom: 0; display: flex; justify-content: space-between; align-items: center; padding: 0 0.65rem; font-size: 0.65rem; color: var(--ink-light); z-index: 1; }
        .axis-marker { position: absolute; top: 2px; bottom: 2px; width: 18px; background: var(--crimson); border-radius: 9px; transition: left 0.5s ease; box-shadow: 0 2px 6px rgba(139, 21, 56, 0.4); }
        
        .retake-section { text-align: center; margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid var(--gold-light); }
        .hidden { display: none !important; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        
        @media (max-width: 900px) {
            .ai-panel { width: 100%; height: 55vh; top: auto; bottom: 0; border-left: none; border-top: 3px solid var(--gold); }
            .quiz-panel.with-ai { max-width: 100%; margin-right: 0; padding-bottom: 57vh; }
        }
        
        @media (max-width: 600px) {
            .quiz-panel { padding: 1rem; }
            header h1 { font-size: 1.5rem; }
            .question-text { font-size: 1.05rem; }
            .option { padding: 0.75rem 0.9rem; }
            .nav-btn { padding: 0.55rem 1.25rem; font-size: 0.85rem; }
            .q-dot { width: 24px; height: 24px; font-size: 0.55rem; }
            .top-match-name { font-size: 1.4rem; }
            .stat-value { font-size: 1.8rem; }
            .length-options { gap: 0.4rem; }
            .length-card { padding: 0.65rem 0.85rem; min-width: 55px; }
            .length-number { font-size: 1.1rem; }
            .length-label { font-size: 0.7rem; }
            .cat-btn { font-size: 0.6rem; padding: 0.35rem 0.5rem; }
            .ai-toggle { width: 50px; height: 50px; font-size: 1.2rem; bottom: 1rem; right: 1rem; }
        }
    </style>
</head>
<body>
    <div class="main-container">
        <div class="quiz-panel" id="quiz-panel">
            <header>
                <h1>Catholic Theology Schools Quiz</h1>
                <p class="subtitle">Discover your theological affinities across 98 schools of thought</p>
                <div class="cross-divider"><span>✝</span></div>
            </header>

            <div id="start-screen" class="start-screen">
                <h2>Find Your Theological Home</h2>
                <p>This comprehensive quiz explores your positions on grace, predestination, ecclesiology, moral theology, liturgy, and more.</p>
                <div class="stats">
                    <div class="stat"><div class="stat-value">132</div><div class="stat-label">Questions</div></div>
                    <div class="stat"><div class="stat-value">98</div><div class="stat-label">Schools</div></div>
                    <div class="stat"><div class="stat-value">8</div><div class="stat-label">Axes</div></div>
                </div>
                
                <div class="quiz-length-section">
                    <h3>Choose Quiz Length</h3>
                    <div class="length-options">
                        <label class="length-option" onclick="setQuizLength(22)">
                            <input type="radio" name="length" value="22">
                            <div class="length-card">
                                <span class="length-number">22</span>
                                <span class="length-label">Quick<br><small>~6 min</small></span>
                            </div>
                        </label>
                        <label class="length-option" onclick="setQuizLength(44)">
                            <input type="radio" name="length" value="44">
                            <div class="length-card">
                                <span class="length-number">44</span>
                                <span class="length-label">Short<br><small>~12 min</small></span>
                            </div>
                        </label>
                        <label class="length-option" onclick="setQuizLength(66)">
                            <input type="radio" name="length" value="66">
                            <div class="length-card">
                                <span class="length-number">66</span>
                                <span class="length-label">Medium<br><small>~18 min</small></span>
                            </div>
                        </label>
                        <label class="length-option" onclick="setQuizLength(88)">
                            <input type="radio" name="length" value="88">
                            <div class="length-card">
                                <span class="length-number">88</span>
                                <span class="length-label">Long<br><small>~24 min</small></span>
                            </div>
                        </label>
                        <label class="length-option" onclick="setQuizLength(110)">
                            <input type="radio" name="length" value="110">
                            <div class="length-card">
                                <span class="length-number">110</span>
                                <span class="length-label">Extended<br><small>~30 min</small></span>
                            </div>
                        </label>
                        <label class="length-option" onclick="setQuizLength(132)">
                            <input type="radio" name="length" value="132" checked>
                            <div class="length-card">
                                <span class="length-number">132</span>
                                <span class="length-label">Complete<br><small>~36 min</small></span>
                            </div>
                        </label>
                    </div>
                    <p class="length-note">Questions are organized into 10 theological categories. Each quiz length is evenly divisible (intervals of 22).</p>
                </div>
                
                <button class="start-btn" onclick="startQuiz()">Begin the Quiz</button>
            </div>

            <div id="quiz-screen" class="hidden">
                <div class="category-nav" id="category-nav"></div>
                
                <div class="progress-section">
                    <div class="progress-header">
                        <span class="progress-text" id="progress-text">Question 1 of 132</span>
                        <span class="progress-count" id="answered-count">Answered: 0 / 132</span>
                    </div>
                    <div class="progress-bar"><div class="progress-fill" id="progress-fill" style="width: 0%"></div></div>
                </div>
                
                <div class="question-card">
                    <div class="question-header">
                        <span class="question-number" id="question-number">Question I</span>
                        <span class="question-category-tag" id="question-category-tag">Grace & Predestination</span>
                    </div>
                    <p class="question-text" id="question-text"></p>
                    <div class="options" id="options"></div>
                    
                    <div class="citation-section" id="citation-section">
                        <button class="citation-toggle" id="citation-toggle" onclick="toggleCitation()">
                            <span class="arrow">▶</span> Further Reading & Sources
                        </button>
                        <div class="citation-content" id="citation-content">
                            <h4>Recommended Sources</h4>
                            <ul id="citation-list"></ul>
                            <button class="ai-explain-btn" onclick="askAIToExplain()">
                                🤖 Ask AI to Explain This
                            </button>
                        </div>
                    </div>
                </div>
                
                <div class="navigation">
                    <button class="nav-btn secondary" id="prev-btn" onclick="prevQuestion()" disabled>← Previous</button>
                    <button class="nav-btn primary" id="next-btn" onclick="nextQuestion()">Next →</button>
                    <button class="nav-btn primary hidden" id="results-btn" onclick="showResults()">See Results</button>
                </div>
                
                <div class="question-nav" id="question-nav"></div>
            </div>

            <div id="results-screen" class="results-screen">
                <div class="results-header">
                    <h2>Your Theological Profile</h2>
                    <div class="cross-divider"><span>✝</span></div>
                </div>
                
                <div class="top-match" id="top-match"></div>
                
                <div class="tabs">
                    <button class="tab-btn active" onclick="showTab('rankings')">All Rankings</button>
                    <button class="tab-btn" onclick="showTab('axes')">Theological Axes</button>
                </div>
                
                <div id="rankings-tab" class="tab-content active">
                    <div class="rankings-card">
                        <h3>Top 20 Schools</h3>
                        <table class="rankings-table">
                            <thead><tr><th>Rank</th><th>School</th><th>Score</th></tr></thead>
                            <tbody id="rankings-body"></tbody>
                        </table>
                    </div>
                </div>
                
                <div id="axes-tab" class="tab-content">
                    <div class="axes-card">
                        <h3>Your Position on Key Spectrums</h3>
                        <div id="axes-content"></div>
                    </div>
                </div>
                
                <div class="retake-section">
                    <button class="nav-btn secondary" onclick="retakeQuiz()">Take Quiz Again</button>
                </div>
            </div>
        </div>
        
        <!-- AI Helper Panel -->
        <div class="ai-panel" id="ai-panel">
            <div class="ai-header">
                <h3>🤖 Theological Guide</h3>
                <button class="ai-close" onclick="closeAI()">×</button>
            </div>
            <div class="ai-messages" id="ai-messages">
                <div class="ai-message system">
                    Welcome! I can help explain theological concepts, clarify scholastic terminology, or discuss the nuances of different Catholic schools of thought. Ask me anything about the questions you encounter.
                </div>
            </div>
            <div class="ai-input-area">
                <div class="ai-input-wrapper">
                    <textarea class="ai-input" id="ai-input" placeholder="Ask about this question or any theological concept..." rows="2" onkeydown="handleAIKeydown(event)"></textarea>
                    <button class="ai-send" id="ai-send" onclick="sendAIMessage()">Send</button>
                </div>
            </div>
        </div>
    </div>
    
    <button class="ai-toggle" id="ai-toggle" onclick="toggleAI()" title="Open AI Theological Guide">
        🤖
    </button>

    <script>
'''

    # Add the data from original file
    html += f'''
// Schools from original quiz
const SCHOOLS = [{schools_match.group(1) if schools_match else ''}];

const SCHOOL_NAME = Object.fromEntries(SCHOOLS);

const SCHOOL_DESC = {{{school_desc_match.group(1) if school_desc_match else ''}}};

const PATRON_SAINTS = {{{patron_match.group(1) if patron_match else ''}}};

const AXES = [
    ["GRACE", "Grace Theology"],
    ["PAPAL", "Papal Authority"],
    ["LIT", "Liturgical Traditionalism"],
    ["RIGOR", "Moral Rigorism"],
    ["PIETY", "Personal Piety"],
    ["SCRIPT", "Scripture Authority & Hermeneutics"],
    ["JUST", "Justification & Union"],
    ["ESCH", "Eschatology & Final Judgment"]
];

const AXIS_ENDPOINTS = {{"GRACE": ["Synergistic", "Monergistic"], "PAPAL": ["Conciliar/Local", "Ultramontane"], "LIT": ["Reformist", "Traditional"], "RIGOR": ["Pastoral/Lenient", "Rigorist"], "PIETY": ["Lower Intensity", "High Contemplative"], "SCRIPT": ["Magisterium-first", "Scripture-first"], "JUST": ["Forensic emphasis", "Participatory/union"], "ESCH": ["This-world focus", "Judgment & beatific end"]}};

const AXIS_MULTIPLIER = {{"GRACE": 3, "PAPAL": 3, "LIT": 3, "RIGOR": 3, "PIETY": 3, "SCRIPT": 4, "JUST": 4, "ESCH": 4}};

// Questions from original quiz
const QUESTIONS = [{questions_match.group(1) if questions_match else ''}];

// Category definitions
const CATEGORIES = [
    {{ id: "scripture", name: "Scripture & Hermeneutics", shortName: "Scripture", icon: "📖", questions: [0, 1, 2] }},
    {{ id: "grace", name: "Grace & Predestination", shortName: "Grace", icon: "✨", questions: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] }},
    {{ id: "metaphysics", name: "Metaphysics & Philosophy", shortName: "Metaphysics", icon: "🔮", questions: [17, 18, 19, 20, 21, 22, 23, 24, 25] }},
    {{ id: "orders", name: "Religious Orders", shortName: "Orders", icon: "🕯️", questions: [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45] }},
    {{ id: "sacraments", name: "Sacramental Theology", shortName: "Sacraments", icon: "🍷", questions: [46, 47, 48, 49, 50, 51, 52, 53, 54, 55] }},
    {{ id: "ecclesiology", name: "Ecclesiology & Authority", shortName: "Ecclesiology", icon: "⛪", questions: [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71] }},
    {{ id: "moral", name: "Moral Theology", shortName: "Moral", icon: "⚖️", questions: [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84] }},
    {{ id: "political", name: "Political & Social", shortName: "Political", icon: "🏛️", questions: [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99] }},
    {{ id: "christology", name: "Christology & Soteriology", shortName: "Christology", icon: "✝️", questions: [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111] }},
    {{ id: "contemporary", name: "Contemporary Debates", shortName: "Contemporary", icon: "📰", questions: [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131] }}
];
'''

    # Add the citations database
    citations_js = json.dumps(CITATIONS, indent=2)
    default_citations_js = json.dumps(DEFAULT_CITATIONS, indent=2)
    
    html += f'''
// Citations database
const CITATIONS = {citations_js};

const DEFAULT_CITATIONS = {default_citations_js};

function getCitationsForQuestion(index) {{
    return CITATIONS[index] || DEFAULT_CITATIONS;
}}
'''

    # Add the main JavaScript logic
    html += '''
// =============================================
// QUIZ STATE
// =============================================

let currentQuestion = 0;
let answers = [];
let scores = {};
let axisScores = {};
let selectedQuestions = [];
let quizLength = 132;
let currentCategoryIndex = 0;
let categoryQuestions = {}; // Maps category id to selected question indices
let aiMessages = [];

// =============================================
// QUIZ LENGTH AND SELECTION
// =============================================

function setQuizLength(length) {
    quizLength = length;
    document.querySelectorAll('.length-option input').forEach(input => {
        const card = input.nextElementSibling;
        if (parseInt(input.value) === length) {
            input.checked = true;
            card.style.borderColor = 'var(--crimson)';
            card.style.background = 'linear-gradient(135deg, rgba(139, 21, 56, 0.08), rgba(201, 162, 39, 0.08))';
        } else {
            input.checked = false;
            card.style.borderColor = 'var(--gold-light)';
            card.style.background = 'transparent';
        }
    });
}

function selectQuestionsForQuiz(count) {
    // Distribute questions proportionally across categories
    const totalQuestions = QUESTIONS.length;
    categoryQuestions = {};
    
    CATEGORIES.forEach(cat => {
        const catTotal = cat.questions.length;
        const proportion = catTotal / totalQuestions;
        let numToSelect = Math.max(1, Math.round(count * proportion));
        
        // Don't select more than available
        numToSelect = Math.min(numToSelect, catTotal);
        
        // Shuffle and select
        const shuffled = [...cat.questions].sort(() => Math.random() - 0.5);
        categoryQuestions[cat.id] = shuffled.slice(0, numToSelect).sort((a, b) => a - b);
    });
    
    // Flatten to get all selected questions in order
    const allSelected = [];
    CATEGORIES.forEach(cat => {
        allSelected.push(...categoryQuestions[cat.id]);
    });
    
    return allSelected;
}

// =============================================
// INITIALIZATION
// =============================================

function initScores() {
    scores = {};
    SCHOOLS.forEach(([code]) => scores[code] = 0);
    axisScores = {};
    AXES.forEach(([code]) => axisScores[code] = 0);
}

function startQuiz() {
    document.getElementById('start-screen').classList.add('hidden');
    document.getElementById('quiz-screen').classList.remove('hidden');
    initScores();
    selectedQuestions = selectQuestionsForQuiz(quizLength);
    answers = new Array(selectedQuestions.length).fill(null);
    currentQuestion = 0;
    currentCategoryIndex = 0;
    buildCategoryNav();
    buildQuestionNav();
    renderQuestion();
}

// =============================================
// CATEGORY NAVIGATION
// =============================================

function buildCategoryNav() {
    const nav = document.getElementById('category-nav');
    nav.innerHTML = '';
    
    CATEGORIES.forEach((cat, idx) => {
        const catQs = categoryQuestions[cat.id] || [];
        if (catQs.length === 0) return;
        
        const btn = document.createElement('button');
        btn.className = 'cat-btn' + (idx === 0 ? ' active' : '');
        btn.onclick = () => jumpToCategory(idx);
        btn.innerHTML = `
            <span class="cat-icon">${cat.icon}</span>
            ${cat.shortName}
            <span class="cat-progress">0/${catQs.length}</span>
        `;
        btn.dataset.catIdx = idx;
        nav.appendChild(btn);
    });
}

function updateCategoryNav() {
    const buttons = document.querySelectorAll('.cat-btn');
    buttons.forEach(btn => {
        const idx = parseInt(btn.dataset.catIdx);
        const cat = CATEGORIES[idx];
        const catQs = categoryQuestions[cat.id] || [];
        
        // Count answered in this category
        let answered = 0;
        catQs.forEach(qIdx => {
            const selIdx = selectedQuestions.indexOf(qIdx);
            if (selIdx !== -1 && answers[selIdx] !== null) answered++;
        });
        
        // Update progress
        const progressSpan = btn.querySelector('.cat-progress');
        if (progressSpan) progressSpan.textContent = `${answered}/${catQs.length}`;
        
        // Mark as completed
        btn.classList.toggle('completed', answered === catQs.length && catQs.length > 0);
        
        // Mark current category
        const currentQIdx = selectedQuestions[currentQuestion];
        const isCurrentCat = catQs.includes(currentQIdx);
        btn.classList.toggle('active', isCurrentCat);
    });
}

function jumpToCategory(catIdx) {
    const cat = CATEGORIES[catIdx];
    const catQs = categoryQuestions[cat.id] || [];
    if (catQs.length === 0) return;
    
    // Find first question of this category in selected questions
    const firstQIdx = catQs[0];
    const selIdx = selectedQuestions.indexOf(firstQIdx);
    if (selIdx !== -1) {
        currentQuestion = selIdx;
        renderQuestion();
        window.scrollTo(0, 0);
    }
}

function getCategoryForQuestion(qIdx) {
    for (const cat of CATEGORIES) {
        if (cat.questions.includes(qIdx)) return cat;
    }
    return CATEGORIES[0];
}

// =============================================
// QUESTION NAVIGATION
// =============================================

function buildQuestionNav() {
    const nav = document.getElementById('question-nav');
    nav.innerHTML = '';
    for (let i = 0; i < selectedQuestions.length; i++) {
        const dot = document.createElement('div');
        dot.className = 'q-dot';
        dot.textContent = i + 1;
        dot.onclick = () => jumpToQuestion(i);
        nav.appendChild(dot);
    }
    updateQuestionNav();
}

function updateQuestionNav() {
    const dots = document.querySelectorAll('.q-dot');
    dots.forEach((dot, i) => {
        dot.classList.remove('answered', 'current');
        if (answers[i] !== null) dot.classList.add('answered');
        if (i === currentQuestion) dot.classList.add('current');
    });
    updateCategoryNav();
}

// =============================================
// QUESTION RENDERING
// =============================================

function renderQuestion() {
    const qIndex = selectedQuestions[currentQuestion];
    const q = QUESTIONS[qIndex];
    const cat = getCategoryForQuestion(qIndex);
    
    // Update progress
    document.getElementById('progress-text').textContent = `Question ${currentQuestion + 1} of ${selectedQuestions.length}`;
    const answeredCount = answers.filter(a => a !== null).length;
    document.getElementById('answered-count').textContent = `Answered: ${answeredCount} / ${selectedQuestions.length}`;
    document.getElementById('progress-fill').style.width = `${(answeredCount / selectedQuestions.length) * 100}%`;
    
    // Roman numerals
    const romanNumerals = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII','XXIII','XXIV','XXV','XXVI','XXVII','XXVIII','XXIX','XXX','XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL','XLI','XLII','XLIII','XLIV','XLV','XLVI','XLVII','XLVIII','XLIX','L','LI','LII','LIII','LIV','LV','LVI','LVII','LVIII','LIX','LX','LXI','LXII','LXIII','LXIV','LXV','LXVI','LXVII','LXVIII','LXIX','LXX','LXXI','LXXII','LXXIII','LXXIV','LXXV','LXXVI','LXXVII','LXXVIII','LXXIX','LXXX','LXXXI','LXXXII','LXXXIII','LXXXIV','LXXXV','LXXXVI','LXXXVII','LXXXVIII','LXXXIX','XC','XCI','XCII','XCIII','XCIV','XCV','XCVI','XCVII','XCVIII','XCIX','C','CI','CII','CIII','CIV','CV','CVI','CVII','CVIII','CIX','CX','CXI','CXII','CXIII','CXIV','CXV','CXVI','CXVII','CXVIII','CXIX','CXX','CXXI','CXXII','CXXIII','CXXIV','CXXV','CXXVI','CXXVII'];
    
    document.getElementById('question-number').textContent = `Question ${romanNumerals[currentQuestion] || currentQuestion + 1}`;
    document.getElementById('question-category-tag').textContent = `${cat.icon} ${cat.shortName}`;
    document.getElementById('question-text').textContent = q.text;
    
    // Options
    const optionsDiv = document.getElementById('options');
    optionsDiv.innerHTML = '';
    q.options.forEach((opt, i) => {
        const option = document.createElement('label');
        option.className = 'option' + (answers[currentQuestion] === i ? ' selected' : '');
        option.innerHTML = `<input type="radio" name="answer" value="${i}"><div class="option-radio"></div><span class="option-text">${opt[0]}</span>`;
        option.onclick = () => selectOption(i);
        optionsDiv.appendChild(option);
    });
    
    // Citations
    renderCitations(qIndex);
    
    // Navigation buttons
    document.getElementById('prev-btn').disabled = currentQuestion === 0;
    const nextBtn = document.getElementById('next-btn');
    const resultsBtn = document.getElementById('results-btn');
    if (currentQuestion === selectedQuestions.length - 1) {
        nextBtn.classList.add('hidden');
        resultsBtn.classList.remove('hidden');
    } else {
        nextBtn.classList.remove('hidden');
        resultsBtn.classList.add('hidden');
    }
    
    updateQuestionNav();
    
    // Close citation panel on new question
    document.getElementById('citation-toggle').classList.remove('open');
    document.getElementById('citation-content').classList.remove('open');
}

function renderCitations(qIndex) {
    const citations = getCitationsForQuestion(qIndex);
    const list = document.getElementById('citation-list');
    list.innerHTML = '';
    
    citations.forEach(cite => {
        const li = document.createElement('li');
        let text = `<strong>${cite.title}</strong>`;
        if (cite.author) text += ` — ${cite.author}`;
        if (cite.year) text += ` (${cite.year})`;
        if (cite.note) text += `<br><em style="font-size: 0.8rem; opacity: 0.8;">${cite.note}</em>`;
        li.innerHTML = text;
        list.appendChild(li);
    });
}

function toggleCitation() {
    const toggle = document.getElementById('citation-toggle');
    const content = document.getElementById('citation-content');
    toggle.classList.toggle('open');
    content.classList.toggle('open');
}

// =============================================
// ANSWER SELECTION
// =============================================

function selectOption(index) {
    answers[currentQuestion] = index;
    document.querySelectorAll('.option').forEach((opt, i) => opt.classList.toggle('selected', i === index));
    updateQuestionNav();
    const answeredCount = answers.filter(a => a !== null).length;
    document.getElementById('answered-count').textContent = `Answered: ${answeredCount} / ${selectedQuestions.length}`;
    document.getElementById('progress-fill').style.width = `${(answeredCount / selectedQuestions.length) * 100}%`;
}

function nextQuestion() {
    if (answers[currentQuestion] === null) {
        alert('Please select an answer.');
        return;
    }
    if (currentQuestion < selectedQuestions.length - 1) {
        currentQuestion++;
        renderQuestion();
        window.scrollTo(0, 0);
    }
}

function prevQuestion() {
    if (currentQuestion > 0) {
        currentQuestion--;
        renderQuestion();
        window.scrollTo(0, 0);
    }
}

function jumpToQuestion(index) {
    currentQuestion = index;
    renderQuestion();
    window.scrollTo(0, 0);
}

// =============================================
// SCORING AND RESULTS
// =============================================

function calculateScores() {
    initScores();
    answers.forEach((ans, i) => {
        if (ans === null) return;
        const qIndex = selectedQuestions[i];
        const q = QUESTIONS[qIndex];
        const weights = q.options[ans][1];
        Object.entries(weights).forEach(([code, w]) => {
            if (scores.hasOwnProperty(code)) scores[code] += w;
        });
        Object.entries(q.axis_weights || {}).forEach(([ax, w]) => {
            if (axisScores.hasOwnProperty(ax)) axisScores[ax] += w;
        });
    });
}

function showResults() {
    const answeredCount = answers.filter(a => a !== null).length;
    if (answeredCount < selectedQuestions.length / 2) {
        if (!confirm(`You've only answered ${answeredCount} of ${selectedQuestions.length} questions. Show results anyway?`)) return;
    }
    calculateScores();
    document.getElementById('quiz-screen').classList.add('hidden');
    document.getElementById('results-screen').style.display = 'block';
    renderTopMatch();
    renderRankings();
    renderAxes();
    window.scrollTo(0, 0);
}

function renderTopMatch() {
    const ranked = Object.entries(scores).sort((a, b) => b[1] - a[1]);
    const [topCode, topScore] = ranked[0];
    const name = SCHOOL_NAME[topCode] || topCode;
    const desc = SCHOOL_DESC[topCode] || {};
    const patron = PATRON_SAINTS[topCode];
    
    let patronHTML = '';
    if (patron && patron.primary) {
        patronHTML = `<div class="patron-section"><div class="patron-label">Patron Figure</div><div class="patron-name">${patron.primary[0]}</div><div class="patron-era">${patron.primary[1]}</div></div>`;
    }
    
    const affirmationsHTML = (desc.affirmations || []).map(a => `<span class="affirmation-tag">${a}</span>`).join('');
    
    document.getElementById('top-match').innerHTML = `
        <div class="top-match-label">Your Top Match</div>
        <div class="top-match-name">${name}</div>
        <div class="top-match-score">Score: ${topScore} points</div>
        <div class="top-match-summary">${desc.summary || ''}</div>
        <div class="top-match-affirmations">${affirmationsHTML}</div>
        ${patronHTML}
    `;
}

function renderRankings() {
    const ranked = Object.entries(scores).sort((a, b) => b[1] - a[1]);
    const maxScore = ranked[0][1] || 1;
    const tbody = document.getElementById('rankings-body');
    tbody.innerHTML = '';
    ranked.slice(0, 20).forEach(([code, score], i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td class="rank-num ${i < 3 ? 'top-3' : ''}">${i + 1}</td>
            <td class="school-name">${SCHOOL_NAME[code] || code}</td>
            <td class="score-bar-container">
                <div class="score-bar"><div class="score-bar-fill" style="width: ${(score / maxScore) * 100}%"></div></div>
                <div class="score-value">${score} pts</div>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

function renderAxes() {
    const container = document.getElementById('axes-content');
    container.innerHTML = '';
    AXES.forEach(([code, name]) => {
        const score = axisScores[code] || 0;
        const mult = AXIS_MULTIPLIER[code] || 3;
        const [lo, hi] = AXIS_ENDPOINTS[code] || ['Low', 'High'];
        const normalized = Math.max(0, Math.min(100, 50 + score * mult));
        const row = document.createElement('div');
        row.className = 'axis-row';
        row.innerHTML = `
            <div class="axis-header">
                <span class="axis-name">${name}</span>
                <span class="axis-score">(${score >= 0 ? '+' : ''}${score})</span>
            </div>
            <div class="axis-bar">
                <div class="axis-labels"><span>${lo}</span><span>${hi}</span></div>
                <div class="axis-marker" style="left: calc(${normalized}% - 9px)"></div>
            </div>
        `;
        container.appendChild(row);
    });
}

function showTab(tabName) {
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    event.target.classList.add('active');
    document.getElementById(tabName + '-tab').classList.add('active');
}

function retakeQuiz() {
    document.getElementById('results-screen').style.display = 'none';
    document.getElementById('start-screen').classList.remove('hidden');
    window.scrollTo(0, 0);
}

// =============================================
// AI HELPER FUNCTIONS
// =============================================

function toggleAI() {
    const panel = document.getElementById('ai-panel');
    const quizPanel = document.getElementById('quiz-panel');
    const toggle = document.getElementById('ai-toggle');
    
    panel.classList.toggle('open');
    quizPanel.classList.toggle('with-ai');
    toggle.classList.toggle('hidden', panel.classList.contains('open'));
}

function closeAI() {
    const panel = document.getElementById('ai-panel');
    const quizPanel = document.getElementById('quiz-panel');
    const toggle = document.getElementById('ai-toggle');
    
    panel.classList.remove('open');
    quizPanel.classList.remove('with-ai');
    toggle.classList.remove('hidden');
}

function handleAIKeydown(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendAIMessage();
    }
}

function askAIToExplain() {
    const qIndex = selectedQuestions[currentQuestion];
    const q = QUESTIONS[qIndex];
    const cat = getCategoryForQuestion(qIndex);
    
    // Open AI panel if not open
    const panel = document.getElementById('ai-panel');
    if (!panel.classList.contains('open')) {
        toggleAI();
    }
    
    // Send automatic explanation request
    const message = `Please explain this question in simpler terms: "${q.text}" 

This question is about ${cat.name}. Help me understand the theological concepts and what each option means.`;
    
    document.getElementById('ai-input').value = message;
    sendAIMessage();
}

async function sendAIMessage() {
    const input = document.getElementById('ai-input');
    const message = input.value.trim();
    if (!message) return;
    
    const sendBtn = document.getElementById('ai-send');
    sendBtn.disabled = true;
    input.value = '';
    
    // Add user message
    addAIMessage(message, 'user');
    
    // Show typing indicator
    const messagesDiv = document.getElementById('ai-messages');
    const typingDiv = document.createElement('div');
    typingDiv.className = 'ai-typing';
    typingDiv.innerHTML = 'Thinking<div class="dots"><span></span><span></span><span></span></div>';
    messagesDiv.appendChild(typingDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
    
    // Get current question context
    const qIndex = selectedQuestions[currentQuestion];
    const q = QUESTIONS[qIndex];
    const cat = getCategoryForQuestion(qIndex);
    
    const systemPrompt = `You are a Catholic theological guide helping someone understand complex theological concepts while taking a quiz about Catholic schools of thought. 

Current question being asked in the quiz:
"${q.text}"

Category: ${cat.name}

Options:
${q.options.map((opt, i) => `${i + 1}. ${opt[0]}`).join('\\n')}

Be helpful, educational, and explain theological concepts in accessible language. If asked to explain the question, break down the theological terms and what each option represents. Do NOT tell the user which answer to pick - help them understand the concepts so they can decide for themselves based on their own beliefs.

Keep responses concise (2-3 paragraphs max) but informative.`;

    try {
        const response = await fetch('https://api.anthropic.com/v1/messages', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                model: 'claude-sonnet-4-20250514',
                max_tokens: 1000,
                system: systemPrompt,
                messages: [
                    ...aiMessages.map(m => ({ role: m.role, content: m.content })),
                    { role: 'user', content: message }
                ]
            })
        });
        
        const data = await response.json();
        typingDiv.remove();
        
        if (data.content && data.content[0]) {
            const aiResponse = data.content[0].text;
            addAIMessage(aiResponse, 'assistant');
            aiMessages.push({ role: 'user', content: message });
            aiMessages.push({ role: 'assistant', content: aiResponse });
            
            // Keep conversation history manageable
            if (aiMessages.length > 10) {
                aiMessages = aiMessages.slice(-10);
            }
        } else {
            addAIMessage('I apologize, but I encountered an issue. Please try again.', 'assistant');
        }
    } catch (error) {
        typingDiv.remove();
        addAIMessage('Unable to connect to the AI service. This feature requires an API connection. You can still use the citations and your own research to understand the questions.', 'system');
    }
    
    sendBtn.disabled = false;
}

function addAIMessage(content, role) {
    const messagesDiv = document.getElementById('ai-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `ai-message ${role}`;
    messageDiv.textContent = content;
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// =============================================
// INITIALIZATION
// =============================================

document.addEventListener('DOMContentLoaded', () => {
    initScores();
    setQuizLength(132);
});
    </script>
</body>
</html>
'''
    
    return html

if __name__ == '__main__':
    html_content = generate_html()
    with open('/home/claude/quiz/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Generated index.html successfully!")
    print(f"File size: {len(html_content)} characters")
