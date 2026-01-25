#!/usr/bin/env python3
"""
Catholic Theology Quiz - Build Script

This script can:
1. Extract question/school data from existing HTML
2. Modify questions, schools, or options
3. Regenerate the HTML file

Usage:
    python3 catholic_quiz_build.py [--extract | --build | --add-question]
"""

import json
import re
import argparse
from pathlib import Path

# =============================================
# SCHOOLS DEFINITION
# =============================================

SCHOOLS = [
    # Grace & Predestination
    ["AUG", "Augustinian"],
    ["AUGP", "Strict Augustinian"],
    ["NEOAUG", "Neo-Augustinian (ressourcement)"],
    ["SEMIAUG", "Soft Augustinian"],
    ["JANS", "Jansenist"],
    ["THOM", "Thomist (mainstream)"],
    ["THOMP", "Strict Thomist"],
    ["BANEZ", "Bañezian"],
    ["MOL", "Molinist"],
    ["CONG", "Congruist"],
    ["SCOT", "Scotist"],
    ["FRANC", "Franciscan (Bonaventure)"],
    ["INFRA", "Infralapsarian"],
    ["SUPRA", "Supralapsarian"],
    
    # Religious Orders
    ["DOM", "Dominican"],
    ["JES", "Jesuit"],
    ["CARM", "Carmelite"],
    ["BENED", "Benedictine"],
    ["OPUS", "Opus Dei"],
    ["FRAN", "Franciscan (order)"],
    ["ORAT", "Oratorian"],
    ["CHART", "Carthusian"],
    ["OSA", "Augustinian (Order)"],
    ["OCSO", "Cistercian/Trappist"],
    ["CSSR", "Redemptorist"],
    ["SDB", "Salesian"],
    ["CM", "Vincentian/Lazarist"],
    ["CP", "Passionist"],
    ["OSM", "Servite"],
    ["OPRAEM", "Norbertine/Premonstratensian"],
    ["MERC", "Mercedarian"],
    ["CSC", "Holy Cross"],
    ["OSBCAM", "Camaldolese"],
    
    # Metaphysics
    ["NEOPLAT", "Neo-Platonist"],
    ["THOMMETA", "Thomist Realism"],
    ["SCOTMETA", "Scotist (univocity)"],
    ["NOMIN", "Nominalist-leaning"],
    ["VOLUNT", "Voluntarist"],
    ["INTELL", "Intellectualist"],
    ["PALAM", "Palamite"],
    
    # Christology
    ["RESSCH", "Ressourcement Christology"],
    ["CHALMAX", "Chalcedonian Maximalist"],
    ["KENOT", "Kenoticism-sympathetic"],
    
    # Sacraments
    ["TRIDSAC", "Tridentine Sacramentalism"],
    ["THOMSAC", "Thomist Sacramentology"],
    ["AUGSAC", "Augustinian Sacramentology"],
    ["MINSAC", "Minimalist Sacramental"],
    ["EASTSAC", "Eastern Sacramental"],
    ["TRANSUB", "Strict Transubstantiation"],
    ["TRANSIG", "Transignification-open"],
    ["EUCHMYST", "Eucharistic Mysticism"],
    
    # Ecclesiology
    ["ULTRA", "Ultramontane"],
    ["PAPMOD", "Moderate Papalist"],
    ["PAPMIN", "Papal Minimalist"],
    ["GALL", "Gallican"],
    ["CONCIL", "Conciliarist"],
    ["EASTECC", "Eastern Catholic"],
    ["SYNOD", "Synodalist"],
    
    # Moral Theology
    ["THOMMOR", "Thomist Natural Law"],
    ["MANUAL", "Manualist"],
    ["VIRTUE", "Virtue Ethics"],
    ["AUGMOR", "Augustinian Moral"],
    ["PERSMOR", "Personalist Moral"],
    ["PROP", "Proportionalist"],
    ["NEOSCH", "Neo-Scholastic Rigorist"],
    ["CASUIST", "Casuist"],
    ["PROBAB", "Probabilist"],
    ["TUTIOR", "Tutiorist"],
    
    # Political/Social
    ["INTEG", "Integralist"],
    ["INTEGHARD", "Hard Integralist"],
    ["INTEGSOFT", "Soft Integralist"],
    ["LIBCATH", "Liberal Catholic"],
    ["DISTRIBUT", "Distributist"],
    ["CORPCATH", "Corporatist Catholic"],
    ["SOCDEM", "Catholic Social Democrat"],
    ["LIBERTAR", "Catholic Libertarian"],
    ["TRADNAT", "Traditionalist Nationalist"],
    ["CATHUNIV", "Catholic Universalist"],
    ["WORKERCATH", "Worker-Catholic"],
    ["AGRAR", "Catholic Agrarian"],
    
    # Liturgical/Contemporary
    ["TRAD", "Traditionalist"],
    ["ROTR", "Reform of the Reform"],
    ["PROG", "Progressive"],
    ["RESS", "Ressourcement"],
    ["STD", "Standard Catholic"],
    ["SSPX", "SSPX-leaning"],
    ["SEDE", "Sedevacantist"],
    ["SEDEPRIV", "Sedeprivationist"],
    ["ORDINAR", "Ordinariate"],
    ["EASTLIT", "Eastern Liturgical"],
    ["ORTHOPH", "Orthophile"],
    ["LUTHCAT", "Lutheran-Catholic Convergence"],
    ["ECUMON", "Ecumenical Monergist"],
    ["ANTIMOD", "Anti-Modernist"],
    ["DEVPROG", "Developmental Progressive"],
    ["COMMUN", "Communio School"],
    ["RADORTH", "Radical Orthodoxy"],
    ["TRADUM", "Traditionis Custodes Compliant"],
    
    # Protestant
    ["REFORM", "Reformed/Calvinist"],
    ["LUTHERAN", "Lutheran"],
    ["ANGLICAN", "Anglican"],
    ["METHOD", "Methodist"],
    
    # Eastern Orthodox
    ["EORTHO", "Eastern Orthodox"],
    ["COPTIC", "Coptic Orthodox"],
    ["ORIENTAL", "Oriental Orthodox"],
]

# =============================================
# SCHOOL DESCRIPTIONS
# =============================================

SCHOOL_DESC = {
    "AUG": {
        "summary": "Emphasizes the depth of human fallenness and the absolute necessity of divine grace for any salvific good.",
        "affirmations": ["Grace precedes all merit", "Original sin profoundly wounds nature", "God's will grounds predestination"]
    },
    "JANS": {
        "summary": "Jansenist (Pascal, Arnauld): strict Augustinian within Trent; efficacious grace, moral rigorism, infrequent communion, anti-Molinist.",
        "affirmations": ["Efficacious grace alone saves", "Infused righteousness (per Trent)", "Few are saved", "Worthy communion is rare"]
    },
    "THOM": {
        "summary": "Mainstream Thomism balancing Aristotelian metaphysics with Augustinian grace theology.",
        "affirmations": ["Being is analogical", "Grace perfects nature", "Will follows intellect's presentation of good"]
    },
    "BANEZ": {
        "summary": "Dominican school emphasizing physical premotion and intrinsically efficacious grace.",
        "affirmations": ["God physically premoves the will", "Predestination ante praevisa merita"]
    },
    "MOL": {
        "summary": "Jesuit school emphasizing middle knowledge and libertarian freedom.",
        "affirmations": ["God knows counterfactuals of freedom", "Grace extrinsically efficacious", "Human freedom is libertarian"]
    },
    "REFORM": {
        "summary": "Reformed/Calvinist: TULIP soteriology, covenant theology, sola fide/sola scriptura, Westminster standards.",
        "affirmations": ["Total depravity", "Unconditional election", "Limited atonement", "Irresistible grace", "Perseverance of saints"]
    },
    "LUTHERAN": {
        "summary": "Lutheran: Law-Gospel distinction, forensic justification, sacramental realism, two kingdoms, Book of Concord.",
        "affirmations": ["Justification by faith alone", "Simul iustus et peccator", "Real presence (sacramental union)"]
    },
    "EORTHO": {
        "summary": "Eastern Orthodox: Seven Ecumenical Councils, essence-energies distinction, theosis, rejection of papal supremacy and filioque.",
        "affirmations": ["Nicene Creed without filioque", "Essence-energies distinction", "Theosis as salvation", "Conciliar authority over papal"]
    },
    "COPTIC": {
        "summary": "Coptic Orthodox: Miaphysite Christology (one united nature), Alexandrian tradition, St. Cyril's theology.",
        "affirmations": ["One united nature of Christ (miaphysitism)", "Cyril of Alexandria normative", "Three Ecumenical Councils"]
    },
    # ... Additional descriptions would be extracted from the HTML
}

# =============================================
# CATEGORIES
# =============================================

CATEGORIES = [
    {"id": "scripture", "name": "Scripture & Hermeneutics", "shortName": "Scripture", "icon": "📖"},
    {"id": "grace", "name": "Grace & Predestination", "shortName": "Grace", "icon": "✨"},
    {"id": "metaphysics", "name": "Metaphysics & Philosophy", "shortName": "Metaphysics", "icon": "🔮"},
    {"id": "orders", "name": "Religious Orders", "shortName": "Orders", "icon": "🕯️"},
    {"id": "sacraments", "name": "Sacramental Theology", "shortName": "Sacraments", "icon": "🍷"},
    {"id": "ecclesiology", "name": "Ecclesiology & Authority", "shortName": "Ecclesiology", "icon": "⛪"},
    {"id": "moral", "name": "Moral Theology", "shortName": "Moral", "icon": "⚖️"},
    {"id": "political", "name": "Political & Social", "shortName": "Political", "icon": "🏛️"},
    {"id": "christology", "name": "Christology & Soteriology", "shortName": "Christology", "icon": "✝️"},
    {"id": "contemporary", "name": "Contemporary Debates", "shortName": "Contemporary", "icon": "📰"},
]

# =============================================
# UTILITY FUNCTIONS
# =============================================

def extract_questions_from_html(html_path):
    """Extract QUESTIONS array from existing HTML file."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find QUESTIONS array
    match = re.search(r'const QUESTIONS = (\[[\s\S]*?\]);[\s\n]*(?:const|//)', content)
    if match:
        questions_str = match.group(1)
        # This would need proper JS parsing, simplified here
        return questions_str
    return None

def extract_schools_from_html(html_path):
    """Extract SCHOOLS array from existing HTML file."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'const SCHOOLS = (\[[\s\S]*?\]);', content)
    if match:
        return match.group(1)
    return None

def add_school(code, name, summary, affirmations, patron=None):
    """Add a new school to the quiz."""
    SCHOOLS.append([code, name])
    SCHOOL_DESC[code] = {
        "summary": summary,
        "affirmations": affirmations
    }
    if patron:
        # Would add to PATRON_SAINTS
        pass

def add_question(text, options, category, axis_weights):
    """
    Add a new question.
    
    Args:
        text: Question text
        options: List of [answer_text, {school_code: points}]
        category: Category ID (e.g., "grace", "ecclesiology")
        axis_weights: Dict of axis weights (e.g., {"JUST": 3, "GRACE": 2})
    """
    question = {
        "text": text,
        "options": options,
        "axis_weights": axis_weights
    }
    return question

def add_theological_indicators(content):
    """Add parenthetical theological position indicators to answer options."""
    
    INDICATORS = {
        "AUG": "Augustinian", "AUGP": "Strict Augustinian", "JANS": "Jansenist",
        "THOM": "Thomist", "BANEZ": "Bañezian", "MOL": "Molinist",
        "REFORM": "Reformed/Calvinist", "LUTHERAN": "Lutheran", 
        "ANGLICAN": "Anglican", "METHOD": "Methodist",
        "EORTHO": "Eastern Orthodox", "COPTIC": "Coptic Orthodox",
        "ORIENTAL": "Oriental Orthodox", "PALAM": "Palamite/Eastern",
        "ULTRA": "Ultramontane", "TRAD": "Traditionalist", "PROG": "Progressive",
        "RESS": "Ressourcement", "STD": "Mainstream",
        # ... etc
    }
    
    def get_top_schools(scores_str):
        pairs = re.findall(r'"(\w+)":\s*(-?\d+)', scores_str)
        scores = {k: int(v) for k, v in pairs if int(v) > 0}
        if not scores:
            return []
        sorted_schools = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_score = sorted_schools[0][1]
        return [code for code, score in sorted_schools[:2] if score >= top_score - 1 and score >= 2]
    
    def add_indicator(match):
        text = match.group(1)
        scores = match.group(2)
        
        # Skip if already has indicator
        if re.search(r'\([A-Z][a-z]+', text):
            return match.group(0)
        
        top = get_top_schools(scores)
        if not top:
            return match.group(0)
        
        labels = [INDICATORS.get(code, code) for code in top]
        indicator = " (" + ", ".join(labels) + ")"
        return f'["{text.rstrip()}{indicator}", {{{scores}}}]'
    
    pattern = r'\["([^"]+)",\s*\{([^}]+)\}\]'
    return re.sub(pattern, add_indicator, content)

def update_quiz_lengths(content, total_questions):
    """Update quiz length intervals to be equidistant."""
    interval = total_questions // 6
    lengths = [interval * i for i in range(1, 7)]
    lengths[-1] = total_questions  # Ensure last one is exact total
    
    # Would update the HTML length options
    return content, lengths

# =============================================
# MAIN
# =============================================

def main():
    parser = argparse.ArgumentParser(description='Catholic Theology Quiz Build Tool')
    parser.add_argument('--extract', action='store_true', help='Extract data from existing HTML')
    parser.add_argument('--build', action='store_true', help='Build new HTML from Python data')
    parser.add_argument('--annotate', action='store_true', help='Add theological indicators to options')
    parser.add_argument('--input', type=str, default='index.html', help='Input HTML file')
    parser.add_argument('--output', type=str, default='index.html', help='Output HTML file')
    
    args = parser.parse_args()
    
    if args.extract:
        print(f"Extracting from {args.input}...")
        questions = extract_questions_from_html(args.input)
        schools = extract_schools_from_html(args.input)
        print(f"Found {len(SCHOOLS)} schools")
        
    elif args.annotate:
        print(f"Adding theological indicators to {args.input}...")
        with open(args.input, 'r', encoding='utf-8') as f:
            content = f.read()
        content = add_theological_indicators(content)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Saved to {args.output}")
        
    else:
        print("Catholic Theology Quiz Build Tool")
        print("Usage:")
        print("  --extract  : Extract data from existing HTML")
        print("  --annotate : Add theological position indicators")
        print("  --build    : Build HTML from Python data (not yet implemented)")

if __name__ == "__main__":
    main()
