#!/usr/bin/env python3
"""
Catholic Theology Quiz - Build Script (Enhanced)

This script can:
1. Extract question/school data from existing HTML
2. Modify questions, schools, or options
3. Regenerate the HTML file
4. Includes all enhanced data: figures, heterodoxy warnings, question topics

Usage:
    python3 catholic_quiz_build.py [--extract | --build | --add-question | --annotate]
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
# SCHOOL FIGURES (Public representatives)
# =============================================

SCHOOL_FIGURES = {
    "AUG": {"figure": "St. Augustine of Hippo", "era": "354–430", "bio": "Bishop of Hippo and Doctor of Grace whose writings on original sin, predestination, and divine grace shaped Western theology.", "works": "Confessions, City of God, On Grace and Free Will"},
    "AUGP": {"figure": "Prosper of Aquitaine", "era": "c. 390–455", "bio": "Lay theologian and defender of Augustine's strict predestinarian views against Semi-Pelagians.", "works": "The Call of All Nations, Grace and Free Will"},
    "NEOAUG": {"figure": "Henri de Lubac, S.J.", "era": "1896–1991", "bio": "French Jesuit whose ressourcement theology recovered patristic and Augustinian themes.", "works": "Surnaturel, Catholicism, The Mystery of the Supernatural"},
    "SEMIAUG": {"figure": "St. Francis de Sales", "era": "1567–1622", "bio": "Doctor of the Church known for gentle synthesis of Augustinian grace theology with pastoral accessibility.", "works": "Introduction to the Devout Life, Treatise on the Love of God"},
    "JANS": {"figure": "Blaise Pascal", "era": "1623–1662", "bio": "French mathematician and philosopher associated with Port-Royal who defended Jansenist theology.", "works": "Pensées, Provincial Letters"},
    "THOM": {"figure": "St. Thomas Aquinas", "era": "1225–1274", "bio": "The Angelic Doctor whose synthesis of Aristotelian philosophy and Christian theology became the Church's preferred framework.", "works": "Summa Theologiae, Summa Contra Gentiles"},
    "THOMP": {"figure": "Reginald Garrigou-Lagrange, O.P.", "era": "1877–1964", "bio": "Dominican theologian and strict Thomist who defended classical metaphysics.", "works": "The Three Ages of the Interior Life, Reality: A Synthesis of Thomistic Thought"},
    "BANEZ": {"figure": "Domingo Báñez, O.P.", "era": "1528–1604", "bio": "Spanish Dominican who developed the theory of physical premotion.", "works": "Scholastic Commentaries on the Summa"},
    "MOL": {"figure": "Luis de Molina, S.J.", "era": "1535–1600", "bio": "Spanish Jesuit who developed middle knowledge (scientia media) to reconcile divine sovereignty with human freedom.", "works": "Concordia"},
    "CONG": {"figure": "St. Robert Bellarmine, S.J.", "era": "1542–1621", "bio": "Jesuit Cardinal and Doctor who defended a modified Molinist position (Congruism).", "works": "De Controversiis"},
    "SCOT": {"figure": "Bl. John Duns Scotus", "era": "c. 1266–1308", "bio": "The Subtle Doctor who championed univocity of being, primacy of will, and absolute primacy of Christ.", "works": "Ordinatio, Quodlibetal Questions"},
    "FRANC": {"figure": "St. Bonaventure", "era": "1221–1274", "bio": "Seraphic Doctor whose mystical-affective theology emphasized Christ as the center of all knowledge.", "works": "The Soul's Journey into God, Breviloquium"},
    "DOM": {"figure": "St. Dominic de Guzmán", "era": "1170–1221", "bio": "Founder of the Order of Preachers dedicated to contemplation, study, and preaching.", "works": "Dominican Constitutions"},
    "JES": {"figure": "St. Ignatius of Loyola", "era": "1491–1556", "bio": "Founder of the Society of Jesus emphasizing discernment and finding God in all things.", "works": "Spiritual Exercises, Autobiography"},
    "CARM": {"figure": "St. Teresa of Ávila", "era": "1515–1582", "bio": "Doctor of the Church and Carmelite reformer whose writings on contemplative prayer remain unsurpassed.", "works": "Interior Castle, The Way of Perfection"},
    "BENED": {"figure": "St. Benedict of Nursia", "era": "c. 480–547", "bio": "Father of Western Monasticism whose Rule established ora et labora.", "works": "Rule of St. Benedict"},
    "TRAD": {"figure": "Dietrich von Hildebrand", "era": "1889–1977", "bio": "Philosopher who defended traditional Catholic teaching against liturgical reform.", "works": "Trojan Horse in the City of God"},
    "PROG": {"figure": "Karl Rahner, S.J.", "era": "1904–1984", "bio": "German Jesuit whose transcendental Thomism shaped progressive Catholic theology.", "works": "Foundations of Christian Faith"},
    "STD": {"figure": "St. John Henry Newman", "era": "1801–1890", "bio": "Cardinal whose thought exemplifies balanced, mainstream Catholic theology.", "works": "Grammar of Assent, Parochial Sermons"},
    "SSPX": {"figure": "Archbishop Marcel Lefebvre", "era": "1905–1991", "bio": "Founder of the Society of St. Pius X who rejected aspects of Vatican II.", "works": "I Accuse the Council"},
    "SEDE": {"figure": "Various Authors", "era": "20th–21st c.", "bio": "Sedevacantists hold the See of Peter has been vacant since Vatican II.", "works": "Various sedevacantist publications"},
    "INTEG": {"figure": "Pope St. Pius X", "era": "1835–1914", "bio": "Pope who condemned Modernism and promoted integral Catholicism.", "works": "Pascendi Dominici Gregis"},
    "DISTRIBUT": {"figure": "G.K. Chesterton", "era": "1874–1936", "bio": "English writer who championed Distributism as a third way.", "works": "What's Wrong with the World"},
    "REFORM": {"figure": "John Calvin", "era": "1509–1564", "bio": "French Reformer whose Institutes systematized Reformed theology.", "works": "Institutes of the Christian Religion"},
    "LUTHERAN": {"figure": "Martin Luther", "era": "1483–1546", "bio": "German Reformer whose theology emphasized justification by faith alone.", "works": "Small Catechism, Bondage of the Will"},
    "EORTHO": {"figure": "St. Photios the Great", "era": "c. 810–893", "bio": "Patriarch of Constantinople and defender of Eastern Orthodoxy.", "works": "Mystagogy of the Holy Spirit"},
    # Add more as needed...
}

# =============================================
# HETERODOXY WARNINGS
# =============================================

HETERODOXY_STATUS = {
    "JANS": {
        "level": "condemned",
        "title": "⚠️ Condemned Position",
        "warning": "Jansenism was formally condemned by multiple popes (Cum Occasione, 1653; Unigenitus, 1713).",
        "documents": "Cum Occasione (1653), Unigenitus (1713)",
        "guidance": "While figures like Pascal offer genuine spiritual insight, the core Jansenist theological system is incompatible with Catholic orthodoxy."
    },
    "SEDE": {
        "level": "schismatic",
        "title": "⛔ Schismatic Position",
        "warning": "Sedevacantism rejects the legitimacy of post-Vatican II popes, placing adherents outside communion with the Catholic Church.",
        "documents": "Canon Law on Schism, Ecclesia Dei (1988)",
        "guidance": "This position is incompatible with Catholic faith."
    },
    "SEDEPRIV": {
        "level": "schismatic",
        "title": "⛔ Schismatic Position",
        "warning": "Sedeprivationism holds that post-conciliar popes are 'material' but not 'formal' popes.",
        "documents": "Canon Law on Schism",
        "guidance": "This position lacks any precedent in Catholic theology."
    },
    "PROP": {
        "level": "problematic",
        "title": "⚠️ Magisterially Critiqued",
        "warning": "Proportionalism was critiqued by St. John Paul II in Veritatis Splendor (1993).",
        "documents": "Veritatis Splendor (1993), §§75-83",
        "guidance": "Pure proportionalism undermines absolute moral norms."
    },
    "SSPX": {
        "level": "irregular",
        "title": "⚠️ Canonically Irregular",
        "warning": "The SSPX's episcopal consecrations without papal mandate (1988) incurred excommunication (later lifted). The Society remains canonically irregular.",
        "documents": "Ecclesia Dei (1988), 2009 Decree",
        "guidance": "Their canonical situation is irregular and sacraments involve complications."
    },
    "GALL": {
        "level": "historical",
        "title": "📜 Historically Superseded",
        "warning": "Gallicanism's claims about limits on papal authority were implicitly rejected by Vatican I (1870).",
        "documents": "Pastor Aeternus (Vatican I, 1870)",
        "guidance": "Historical Gallicanism is superseded by Vatican I."
    },
    "CONCIL": {
        "level": "historical",
        "title": "📜 Historically Superseded",
        "warning": "Strict conciliarism was condemned at the Fifth Lateran Council and contradicted by Vatican I.",
        "documents": "Pastor Aeternus (Vatican I, 1870)",
        "guidance": "The pope is not subject to conciliar judgment."
    },
    "REFORM": {
        "level": "non-catholic",
        "title": "✝️ Non-Catholic Tradition",
        "warning": "Reformed/Calvinist theology represents a Protestant tradition with substantial disagreements with Catholic teaching.",
        "documents": "Council of Trent, Joint Declaration (1999)",
        "guidance": "Study for ecumenical understanding, but recognize incompatibility with Catholic doctrine."
    },
    "LUTHERAN": {
        "level": "non-catholic",
        "title": "✝️ Non-Catholic Tradition",
        "warning": "Lutheran theology differs from Catholic teaching on justification, the Mass, and papal authority.",
        "documents": "Council of Trent, Joint Declaration (1999)",
        "guidance": "The Joint Declaration represents convergence, but real differences remain."
    },
    "EORTHO": {
        "level": "non-catholic",
        "title": "☦️ Orthodox (Not in Full Communion)",
        "warning": "Eastern Orthodoxy shares apostolic succession but is not in full communion with Rome.",
        "documents": "Unitatis Redintegratio",
        "guidance": "Orthodox theology is a treasure for Catholics. The differences are real but the traditions are close."
    },
}

# =============================================
# QUESTION TOPICS
# =============================================

QUESTION_TOPICS = {
    0: {
        "topic": "The Rule of Faith: Scripture, Tradition, and Magisterium",
        "description": "This question addresses the relationship between the three sources of Catholic authority.",
        "reading": "Dei Verbum (Vatican II), Catechism §§74-100, Congar's 'Tradition and Traditions'",
        "geminiPrompt": "Explain the Catholic understanding of the relationship between Scripture, Tradition, and the Magisterium. What are the main theological schools of thought? Present Ressourcement, Thomist, Ultramontane, and Traditionalist perspectives fairly."
    },
    1: {
        "topic": "Biblical Hermeneutics",
        "description": "The proper method of interpreting Scripture: patristic exegesis, scholastic priority, historical-critical, or reader-response.",
        "reading": "Dei Verbum §§11-13, de Lubac's 'Medieval Exegesis'",
        "geminiPrompt": "What are the main approaches to biblical interpretation in Catholic theology? Explain patristic exegesis, Thomistic interpretation, historical-critical method, and contemporary approaches fairly."
    },
    2: {
        "topic": "Theological Method",
        "description": "Whether Scripture, metaphysics, or Magisterium should be primary in resolving disputes.",
        "reading": "Fides et Ratio, Aeterni Patris",
        "geminiPrompt": "In Catholic theology, what should be the primary norm for resolving theological disputes? Explain views prioritizing Scripture, metaphysical frameworks, or magisterial teaching."
    },
    3: {
        "topic": "Bible Translation Philosophy",
        "description": "Formal equivalence, dynamic equivalence, liturgical considerations, and pastoral accessibility.",
        "reading": "Liturgiam Authenticam, Comme le Prévoit",
        "geminiPrompt": "What are the main philosophies of Bible translation in Catholic context? Explain formal equivalence, dynamic equivalence, and liturgical translation principles."
    },
    4: {
        "topic": "The Doctrine of Justification",
        "description": "How sinners are reconciled to God. Catholic teaching affirms real interior transformation.",
        "reading": "Council of Trent Session 6, Joint Declaration on Justification (1999), Catechism §§1987-2029",
        "geminiPrompt": "Explain the Catholic doctrine of justification. How does it differ from Protestant views? What are the emphases within Catholic theology?"
    },
    5: {
        "topic": "Growth in Justification",
        "description": "Whether and how justification can increase after baptism through cooperation with grace.",
        "reading": "Council of Trent Session 6, Chapter 10",
        "geminiPrompt": "Can justification increase after baptism according to Catholic teaching? Explain the Tridentine doctrine and various interpretations."
    },
    6: {
        "topic": "Justification and Sanctification",
        "description": "The relationship between being declared righteous and being made holy.",
        "reading": "Trent Session 6, Joint Declaration on Justification",
        "geminiPrompt": "How are justification and sanctification related in Catholic theology? Compare Catholic and Protestant understandings."
    },
    7: {
        "topic": "Concupiscence After Baptism",
        "description": "The nature and moral status of disordered desires remaining after baptismal regeneration.",
        "reading": "Trent Session 5, Catechism §§1264, 2515",
        "geminiPrompt": "What is concupiscence and how does Catholic theology understand its status after baptism?"
    },
    8: {
        "topic": "Habitual Vice and Culpability",
        "description": "How prior sinful choices affect moral responsibility for present actions.",
        "reading": "Aquinas ST I-II q.78, Catechism §§1865-1866",
        "geminiPrompt": "How does habitual vice formed by prior voluntary sin affect moral culpability according to Catholic moral theology?"
    },
    9: {
        "topic": "Assurance of Salvation",
        "description": "Whether Christians can know they are presently in the state of grace.",
        "reading": "Trent Session 6, Chapter 9; Catechism §2005",
        "geminiPrompt": "Can a Christian know with certainty they are in the state of grace? Explain the Catholic position versus Protestant views on assurance."
    },
    10: {
        "topic": "Final Perseverance",
        "description": "The gift of persisting in grace until death.",
        "reading": "Trent Session 6, Chapter 13; Augustine's De Dono Perseverantiae",
        "geminiPrompt": "What is final perseverance in Catholic theology? Explain the various views on whether it is a special gift or assured for the elect."
    },
    11: {
        "topic": "The Goal of the Christian Life",
        "description": "What the Christian life is primarily oriented toward.",
        "reading": "Catechism §§1-3, 1024; Aquinas ST I-II q.3",
        "geminiPrompt": "What is the ultimate goal of the Christian life according to Catholic teaching? Explain beatific vision, theosis, and other frameworks."
    },
    12: {
        "topic": "Purgatory",
        "description": "The nature and purpose of purgatorial purification after death.",
        "reading": "Catechism §§1030-1032, Council of Florence, Trent Session 25",
        "geminiPrompt": "Explain the Catholic doctrine of purgatory. What are the various theological models for understanding purification after death?"
    },
    13: {
        "topic": "Dissent from Non-Definitive Teaching",
        "description": "The proper Catholic response to ordinary magisterial teaching that seems doubtful.",
        "reading": "Donum Veritatis (CDF 1990), Catechism §892",
        "geminiPrompt": "What is the proper Catholic posture toward non-definitive magisterial teaching that seems doubtful? Explain religious submission and legitimate dissent."
    },
    14: {
        "topic": "The Role of Theologians",
        "description": "How theologians serve the Church in relation to the Magisterium.",
        "reading": "Donum Veritatis, Veritatis Gaudium",
        "geminiPrompt": "How do theologians serve the Church according to Catholic teaching? What is their relationship to the Magisterium?"
    },
    15: {
        "topic": "Fallen Nature and the Good",
        "description": "The relationship between fallen human nature and the ability to do good.",
        "reading": "Trent Session 6, Catechism §§405-406, 1949",
        "geminiPrompt": "What is the relationship between fallen human nature and the ability to do good in Catholic theology? Explain various positions from Semi-Pelagian to strict Augustinian."
    },
    16: {
        "topic": "Grace and Freedom",
        "description": "How God's grace relates to human freedom in salvation.",
        "reading": "Trent Session 6, Catechism §§1993-2000",
        "geminiPrompt": "How does God's grace relate to human freedom in salvation? Explain Thomist, Molinist, and Augustinian perspectives."
    },
    17: {
        "topic": "Predestination",
        "description": "How to understand God's eternal decree regarding salvation.",
        "reading": "Romans 8-9, Aquinas ST I q.23, Catechism §600",
        "geminiPrompt": "How should Catholics understand predestination? Explain the spectrum from double predestination to conditional election."
    },
    18: {
        "topic": "Infralapsarianism vs Supralapsarianism",
        "description": "The logical order of God's decrees about predestination and the Fall.",
        "reading": "Aquinas ST I q.23, Garrigou-Lagrange's Predestination",
        "geminiPrompt": "What is the difference between infralapsarianism and supralapsarianism? How do Catholic theologians approach this question?"
    },
    19: {
        "topic": "The Absolute Primacy of Christ",
        "description": "Whether the Incarnation would have occurred if Adam had never sinned.",
        "reading": "Scotus' Ordinatio, Aquinas ST III q.1 a.3",
        "geminiPrompt": "Would the Incarnation have occurred if Adam had never sinned? Explain the Scotist and Thomist positions on Christ's primacy."
    },
    20: {
        "topic": "Sufficient Grace",
        "description": "The nature of grace that enables but does not determine salvation.",
        "reading": "De Auxiliis controversy documents, Garrigou-Lagrange",
        "geminiPrompt": "What is sufficient grace in Catholic theology? Explain how Thomists, Molinists, and Augustinians understand its relationship to efficacious grace."
    },
    21: {
        "topic": "Divine Will and Intellect",
        "description": "The relationship between God's will and God's intellect.",
        "reading": "Aquinas ST I q.19, Scotus' Ordinatio",
        "geminiPrompt": "What is the relationship between God's will and intellect? Explain intellectualist and voluntarist positions in Catholic theology."
    },
    22: {
        "topic": "The Source of Moral Obligations",
        "description": "What grounds moral obligations - divine command, natural law, or something else.",
        "reading": "Aquinas ST I-II q.90-94",
        "geminiPrompt": "What is the source of moral obligations according to Catholic theology? Explain natural law, divine command, and virtue-based approaches."
    },
    23: {
        "topic": "The Problem of Universals",
        "description": "The metaphysical status of universals like 'humanity' or 'justice'.",
        "reading": "Aquinas' De Ente et Essentia, various medieval commentaries",
        "geminiPrompt": "What is the problem of universals and how do Catholic philosophers approach it? Explain realism, nominalism, and moderate realism."
    },
    24: {
        "topic": "The Analogy of Being",
        "description": "How we can speak meaningfully about God using created concepts.",
        "reading": "Aquinas ST I q.13, Fourth Lateran Council",
        "geminiPrompt": "What is the analogy of being (analogia entis)? Explain how Thomists and Scotists differ on how we can speak about God."
    },
    146: {
        "topic": "Papal Response to Heterodox Bishops' Conferences",
        "description": "How the Pope should respond to regional episcopal conferences that deviate from orthodox teaching.",
        "reading": "Pastor Aeternus, Apostolos Suos (1998), CDF documents on the Synodal Path",
        "geminiPrompt": "How should the Pope respond to bishops' conferences that deviate from orthodox teaching? Explain different ecclesiological approaches."
    },
    147: {
        "topic": "Benedict XVI's 'Smaller, Purer Church'",
        "description": "Whether a smaller, more orthodox Church would be preferable to a larger but less fervent one.",
        "reading": "Ratzinger's 'Faith and the Future' (1969)",
        "geminiPrompt": "What did Benedict XVI mean by a 'smaller, purer Church'? Explain various perspectives on numerical decline and spiritual renewal."
    },
    148: {
        "topic": "Evaluating Post-Conciliar Popes",
        "description": "Which post-Vatican II pope best served the Church.",
        "reading": "Biographies and encyclicals of post-conciliar popes",
        "geminiPrompt": "Compare the post-conciliar popes. What were their main contributions and how do different Catholic groups evaluate them?"
    },
    149: {
        "topic": "The Future of the Catholic Church",
        "description": "Personal outlook on where the Church is headed.",
        "reading": "Various contemporary Catholic commentary",
        "geminiPrompt": "What are the different Catholic perspectives on the future of the Church? Explain optimistic, cautious, traditionalist, and progressive views."
    },
    # Default fallback
    "default": {
        "topic": "Catholic Theological Question",
        "description": "This question explores an area of Catholic theological discussion where different schools offer varying perspectives.",
        "reading": "Catechism of the Catholic Church, relevant theological manuals",
        "geminiPrompt": "Explain the various Catholic theological perspectives on this topic, presenting each school of thought fairly."
    }
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
    
    match = re.search(r'const QUESTIONS = (\[[\s\S]*?\]);[\s\n]*(?:const|//)', content)
    if match:
        return match.group(1)
    return None

def extract_schools_from_html(html_path):
    """Extract SCHOOLS array from existing HTML file."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'const SCHOOLS = (\[[\s\S]*?\]);', content)
    if match:
        return match.group(1)
    return None

def generate_js_school_figures():
    """Generate JavaScript object for SCHOOL_FIGURES."""
    lines = ["const SCHOOL_FIGURES = {"]
    for code, data in SCHOOL_FIGURES.items():
        lines.append(f'    "{code}": {{ figure: "{data["figure"]}", era: "{data["era"]}", bio: "{data["bio"]}", works: "{data["works"]}" }},')
    lines.append("};")
    return "\n".join(lines)

def generate_js_heterodoxy():
    """Generate JavaScript object for HETERODOXY_STATUS."""
    lines = ["const HETERODOXY_STATUS = {"]
    for code, data in HETERODOXY_STATUS.items():
        lines.append(f'    "{code}": {{')
        lines.append(f'        level: "{data["level"]}",')
        lines.append(f'        title: "{data["title"]}",')
        lines.append(f'        warning: "{data["warning"]}",')
        lines.append(f'        documents: "{data["documents"]}",')
        lines.append(f'        guidance: "{data["guidance"]}"')
        lines.append('    },')
    lines.append("};")
    return "\n".join(lines)

def generate_js_question_topics():
    """Generate JavaScript object for QUESTION_TOPICS."""
    lines = ["const QUESTION_TOPICS = {"]
    for key, data in QUESTION_TOPICS.items():
        if key == "default":
            lines.append(f'    default: {{')
        else:
            lines.append(f'    {key}: {{')
        lines.append(f'        topic: "{data["topic"]}",')
        lines.append(f'        description: "{data["description"]}",')
        lines.append(f'        reading: "{data["reading"]}",')
        lines.append(f'        geminiPrompt: "{data["geminiPrompt"]}"')
        lines.append('    },')
    lines.append("};")
    return "\n".join(lines)

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

# =============================================
# MAIN
# =============================================

def main():
    parser = argparse.ArgumentParser(description='Catholic Theology Quiz Build Tool')
    parser.add_argument('--extract', action='store_true', help='Extract data from existing HTML')
    parser.add_argument('--build', action='store_true', help='Build new HTML from Python data')
    parser.add_argument('--annotate', action='store_true', help='Add theological indicators to options')
    parser.add_argument('--generate-js', action='store_true', help='Generate JS data structures')
    parser.add_argument('--input', type=str, default='index.html', help='Input HTML file')
    parser.add_argument('--output', type=str, default='index.html', help='Output HTML file')
    
    args = parser.parse_args()
    
    if args.extract:
        print(f"Extracting from {args.input}...")
        questions = extract_questions_from_html(args.input)
        schools = extract_schools_from_html(args.input)
        print(f"Found {len(SCHOOLS)} schools defined")
        
    elif args.annotate:
        print(f"Adding theological indicators to {args.input}...")
        with open(args.input, 'r', encoding='utf-8') as f:
            content = f.read()
        content = add_theological_indicators(content)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Saved to {args.output}")
        
    elif args.generate_js:
        print("Generating JavaScript data structures...")
        print("\n" + "="*60)
        print("SCHOOL_FIGURES:")
        print("="*60)
        print(generate_js_school_figures())
        print("\n" + "="*60)
        print("HETERODOXY_STATUS:")
        print("="*60)
        print(generate_js_heterodoxy())
        print("\n" + "="*60)
        print("QUESTION_TOPICS:")
        print("="*60)
        print(generate_js_question_topics())
        
    else:
        print("Catholic Theology Quiz Build Tool (Enhanced)")
        print("Usage:")
        print("  --extract     : Extract data from existing HTML")
        print("  --annotate    : Add theological position indicators")
        print("  --generate-js : Generate JS data structures for copy/paste")
        print("  --build       : Build HTML from Python data (not yet implemented)")

if __name__ == "__main__":
    main()
