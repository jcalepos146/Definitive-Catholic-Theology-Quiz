"""
Catholic Theology Schools Quiz - Full Multiple Choice Edition
Features:
- ALL questions are multiple choice with distinct theological options
- Topics: grace, predestination, voluntarism, intellectualism, nominalism, 
  religious orders, infra/supralapsarianism, eucharistic views, economics, 
  workers' rights, nationalism, integralism, temporal authority, liturgy, etc.
- 72 schools with detailed descriptions
- Axes scoring with visualization
- "Show me why" explainability panel

Build to .exe (Windows):
  pip install pyinstaller matplotlib
  pyinstaller --onefile --windowed catholic_quiz_mc.py
"""

import json
import math
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# ----------------------------
# 1) Schools
# ----------------------------
SCHOOLS = [
    # Grace / Predestination
    ("AUG", "Augustinian"),
    ("AUGP", "Strict Augustinian"),
    ("NEOAUG", "Neo-Augustinian (ressourcement)"),
    ("SEMIAUG", "Soft Augustinian"),
    ("JANS", "Jansenist"),
    ("THOM", "Thomist (mainstream)"),
    ("THOMP", "Strict Thomist"),
    ("BANEZ", "Bañezian"),
    ("MOL", "Molinist"),
    ("CONG", "Congruist"),
    ("SCOT", "Scotist"),
    ("FRANC", "Franciscan (Bonaventure)"),
    ("INFRA", "Infralapsarian"),
    ("SUPRA", "Supralapsarian"),

    # Orders
    ("DOM", "Dominican"),
    ("JES", "Jesuit"),
    ("CARM", "Carmelite"),
    ("BENED", "Benedictine"),
    ("OPUS", "Opus Dei"),
    ("FRAN", "Franciscan (order)"),
    ("ORAT", "Oratorian"),
    ("CHART", "Carthusian"),
    ("OSA", "Augustinian (Order)"),
    ("OCSO", "Cistercian/Trappist"),
    ("CSSR", "Redemptorist"),
    ("SDB", "Salesian"),
    ("CM", "Vincentian/Lazarist"),
    ("CP", "Passionist"),
    ("OSM", "Servite"),
    ("OPRAEM", "Norbertine/Premonstratensian"),
    ("MERC", "Mercedarian"),
    ("CSC", "Holy Cross"),
    ("OSBCAM", "Camaldolese"),


    # Metaphysics
    ("NEOPLAT", "Neo-Platonist"),
    ("THOMMETA", "Thomist Realism"),
    ("SCOTMETA", "Scotist (univocity)"),
    ("NOMIN", "Nominalist-leaning"),
    ("VOLUNT", "Voluntarist"),
    ("INTELL", "Intellectualist"),
    ("PALAM", "Palamite"),

    # Christology
    ("RESSCH", "Ressourcement Christology"),
    ("CHALMAX", "Chalcedonian Maximalist"),
    ("KENOT", "Kenoticism-sympathetic"),

    # Sacraments / Eucharist
    ("TRIDSAC", "Tridentine Sacramentalism"),
    ("THOMSAC", "Thomist Sacramentology"),
    ("AUGSAC", "Augustinian Sacramentology"),
    ("MINSAC", "Minimalist Sacramental"),
    ("EASTSAC", "Eastern Sacramental"),
    ("TRANSUB", "Strict Transubstantiation"),
    ("TRANSIG", "Transignification-open"),
    ("EUCHMYST", "Eucharistic Mysticism"),

    # Ecclesiology
    ("ULTRA", "Ultramontane"),
    ("PAPMOD", "Moderate Papalist"),
    ("PAPMIN", "Papal Minimalist"),
    ("GALL", "Gallican"),
    ("CONCIL", "Conciliarist"),
    ("EASTECC", "Eastern Catholic"),
    ("SYNOD", "Synodalist"),

    # Moral theology
    ("THOMMOR", "Thomist Natural Law"),
    ("MANUAL", "Manualist"),
    ("VIRTUE", "Virtue Ethics"),
    ("AUGMOR", "Augustinian Moral"),
    ("PERSMOR", "Personalist Moral"),
    ("PROP", "Proportionalist"),
    ("NEOSCH", "Neo-Scholastic Rigorist"),
    ("CASUIST", "Casuist"),
    ("PROBAB", "Probabilist"),
    ("TUTIOR", "Tutiorist"),

    # Political / Social
    ("INTEG", "Integralist"),
    ("INTEGHARD", "Hard Integralist"),
    ("INTEGSOFT", "Soft Integralist"),
    ("LIBCATH", "Liberal Catholic"),
    ("DISTRIBUT", "Distributist"),
    ("CORPCATH", "Corporatist Catholic"),
    ("SOCDEM", "Catholic Social Democrat"),
    ("LIBERTAR", "Catholic Libertarian"),
    ("TRADNAT", "Traditionalist Nationalist"),
    ("CATHUNIV", "Catholic Universalist"),
    ("WORKERCATH", "Worker-Catholic"),
    ("AGRAR", "Catholic Agrarian"),

    # Liturgical / Cultural
    ("TRAD", "Traditionalist"),
    ("ROTR", "Reform of the Reform"),
    ("PROG", "Progressive"),
    ("RESS", "Ressourcement"),
    ("STD", "Standard Catholic"),

    # Extreme positions
    ("SSPX", "SSPX-leaning"),
    ("SEDE", "Sedevacantist"),
    ("SEDEPRIV", "Sedeprivationist"),

    # New Schools - Ecumenical & Liturgical
    ("ORDINAR", "Ordinariate"),
    ("EASTLIT", "Eastern Liturgical"),
    ("ORTHOPH", "Orthophile"),
    ("LUTHCAT", "Lutheran-Catholic Convergence"),
    ("ECUMON", "Ecumenical Monergist"),
    
    # New Schools - Theological Movements
    ("ANTIMOD", "Anti-Modernist"),
    ("DEVPROG", "Developmental Progressive"),
    ("COMMUN", "Communio School"),
    ("RADORTH", "Radical Orthodoxy"),
    ("TRADUM", "Traditionis Custodes Compliant"),
]

SCHOOL_CODES = [c for c, _ in SCHOOLS]
SCHOOL_NAME = {c: n for c, n in SCHOOLS}

# ----------------------------
# 1b) School Descriptions
# ----------------------------
SCHOOL_DESC = {
    "AUG": {
        "summary": "Emphasizes the depth of human fallenness and the absolute necessity of divine grace for any salvific good.",
        "affirmations": ["Grace precedes all merit", "Original sin profoundly wounds nature", "God's will grounds predestination"]
    },
    "AUGP": {
        "summary": "Stricter Augustine: irresistible grace, massa damnata, double predestination in softer form.",
        "affirmations": ["Efficacious grace infallibly achieves its effect", "The reprobate are justly passed over"]
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
    "SCOT": {
        "summary": "Franciscan school of Duns Scotus: primacy of will, univocity of being, absolute primacy of Christ.",
        "affirmations": ["Being is univocal", "Will is primary faculty", "Incarnation independent of Fall"]
    },
    "VOLUNT": {
        "summary": "Divine will is the ultimate ground of morality and truth; God's commands make things good.",
        "affirmations": ["God's will is the source of moral obligation", "Natural law depends on divine command"]
    },
    "INTELL": {
        "summary": "Divine intellect is primary; God wills things because they are good, not vice versa.",
        "affirmations": ["Goodness is prior to divine willing", "Natural law reflects eternal reason"]
    },
    "NOMIN": {
        "summary": "Universals are names/concepts only; reality consists of particulars. Associated with Ockham.",
        "affirmations": ["Universals don't exist in re", "Parsimony in metaphysical commitments"]
    },
    "TRANSUB": {
        "summary": "Strict Tridentine transubstantiation: substance of bread/wine entirely converted to Body/Blood.",
        "affirmations": ["Whole substance changes", "Accidents remain without subject", "Real, true, substantial presence"]
    },
    "TRANSIG": {
        "summary": "Open to transignification/transfinalisation language as complementary to transubstantiation.",
        "affirmations": ["Meaning and purpose truly change", "Phenomenological categories can illuminate"]
    },
    "INFRA": {
        "summary": "God's decree of predestination logically follows his decree to permit the Fall.",
        "affirmations": ["Election from the fallen mass", "More 'merciful' framing"]
    },
    "SUPRA": {
        "summary": "God's decree of predestination logically precedes his decree to permit the Fall.",
        "affirmations": ["Election logically prior to Fall", "Stronger sovereignty emphasis"]
    },
    "INTEG": {
        "summary": "The state should acknowledge and support the true religion; no strict separation of church and state.",
        "affirmations": ["Christ's kingship extends to political order", "Religious neutrality is impossible"]
    },
    "INTEGHARD": {
        "summary": "Robust integralism: confessional state, suppression of public heresy, bishops direct temporal rulers.",
        "affirmations": ["Temporal power subordinate to spiritual", "Error has no rights publicly"]
    },
    "INTEGSOFT": {
        "summary": "Moderate integralism: state should favor true religion but with prudential tolerance.",
        "affirmations": ["Prudential tolerance in pluralist contexts", "Gradual cultural transformation"]
    },
    "DISTRIBUT": {
        "summary": "Wide distribution of productive property; neither capitalism nor socialism; subsidiarity central.",
        "affirmations": ["Property ownership should be widespread", "Against concentrated economic power"]
    },
    "CORPCATH": {
        "summary": "Corporatist/solidarist model: organized vocational groups mediate between state and individual.",
        "affirmations": ["Guilds/corporations structure economy", "Class cooperation over conflict"]
    },
    "WORKERCATH": {
        "summary": "Strong emphasis on workers' rights, unions, just wages, and dignity of labor.",
        "affirmations": ["Living wage is moral requirement", "Unions are natural right"]
    },
    "TRADNAT": {
        "summary": "Synthesis of Catholic tradition with national/ethnic identity; skeptical of globalism.",
        "affirmations": ["Nations are natural communities", "Borders and culture worth preserving"]
    },
    "CATHUNIV": {
        "summary": "Emphasis on Church's universal mission transcending national boundaries.",
        "affirmations": ["Gospel transcends ethnicity", "International solidarity"]
    },
    "DOM": {
        "summary": "Dominican spirituality: contemplata aliis tradere; truth, preaching, intellectual apostolate.",
        "affirmations": ["Contemplation ordered to preaching", "Truth is primary", "Thomism as framework"]
    },
    "JES": {
        "summary": "Jesuit spirituality: finding God in all things; discernment, adaptability, active apostolate.",
        "affirmations": ["Ad maiorem Dei gloriam", "Discernment of spirits central"]
    },
    "CARM": {
        "summary": "Carmelite spirituality: contemplative prayer, mystical theology, interior castle.",
        "affirmations": ["Prayer is essential", "Mystical union possible for all"]
    },
    "BENED": {
        "summary": "Benedictine spirituality: ora et labora, stability, liturgy of the hours.",
        "affirmations": ["Liturgy is source and summit", "Stability and community"]
    },
    "SSPX": {
        "summary": "Traditionalist resistance to post-conciliar changes while typically maintaining papal legitimacy.",
        "affirmations": ["Vatican II contains errors/ambiguities", "Traditional Mass normative"]
    },
    "SEDE": {
        "summary": "Sedevacantist: the See is vacant; post-1958 claimants are not true popes.",
        "affirmations": ["No valid pope since Pius XII", "Vatican II invalid"]
    },
    "SEDEPRIV": {
        "summary": "Material-formal distinction: current claimants are materially but not formally pope.",
        "affirmations": ["Material succession exists", "Formal authority lacking"]
    },
    "STD": {
        "summary": "Mainstream Catholic without strong identification with any particular school.",
        "affirmations": ["Loyalty to Magisterium", "Balance of traditions"]
    },
    "PROBAB": {
        "summary": "In doubtful moral cases, one may follow a solidly probable opinion favoring liberty.",
        "affirmations": ["Probable opinions can be followed", "Liberty in doubt"]
    },
    "TUTIOR": {
        "summary": "In doubtful cases, one must follow the safer (tutior) opinion favoring the law.",
        "affirmations": ["Safer opinion must be followed", "Strictness in doubt"]
    },
}

# Extended descriptions for all schools
EXTENDED_DESC = {
    "NEOAUG": {
        "summary": "Ressourcement retrieval of Augustine: participatory ontology, Christocentric grace, liturgical renewal.",
        "affirmations": ["Christ is the concrete universal", "Grace as participation in divine life"]
    },
    "SEMIAUG": {
        "summary": "Moderate Augustinianism: depth of Fall and priority of grace with room for human cooperation.",
        "affirmations": ["Grace is necessary but human response matters", "Balance of sovereignty and agency"]
    },
    "JANS": {
        "summary": "Rigorous Augustinianism: irresistible grace, strict moral demands, rare worthy communion.",
        "affirmations": ["Grace is irresistible when given", "Many called, few chosen"]
    },
    "THOMP": {
        "summary": "Strict Thomism: rigorous adherence to Thomas and traditional commentators.",
        "affirmations": ["24 Thomistic Theses are normative", "Real distinction of essence and existence"]
    },
    "CONG": {
        "summary": "Congruism: efficacious grace suited to circumstances God foresees.",
        "affirmations": ["Grace efficacy depends on divine wisdom", "Middle knowledge grounds providence"]
    },
    "FRANC": {
        "summary": "Franciscan theology of Bonaventure: exemplarism, Christ as center, affective-mystical approach.",
        "affirmations": ["Christ is medium of all knowledge", "Love leads to wisdom"]
    },
    "OPUS": {
        "summary": "Opus Dei: sanctification of ordinary work, universal call to holiness.",
        "affirmations": ["Work is path to holiness", "Lay faithful called to sanctity"]
    },
    "FRAN": {
        "summary": "Franciscan spirituality: poverty, simplicity, love of creation, service to poor.",
        "affirmations": ["Lady Poverty embraced", "Creation reveals Creator"]
    },
    "ORAT": {
        "summary": "Oratorian spirituality: pastoral gentleness, intellectual culture, liturgical beauty.",
        "affirmations": ["Gentleness in pastoral care", "Liturgy as school of holiness"]
    },
    "CHART": {
        "summary": "Carthusian spirituality: eremitical solitude, perpetual silence, contemplative focus.",
        "affirmations": ["Solitude is path to God", "Stat crux dum volvitur orbis"]
    },
    "OSA": {
        "summary": "Augustinian Order: interiority, community life, intellectual apostolate, Augustinian tradition.",
        "affirmations": ["Restless hearts find rest in God", "Truth dwelling within", "Common life and fraternity"]
    },
    "OCSO": {
        "summary": "Cistercian/Trappist: strict Benedictine observance, silence, manual labor, contemplative depth.",
        "affirmations": ["Silence speaks to God", "Labor is prayer", "Simplicity leads to God"]
    },
    "CSSR": {
        "summary": "Redemptorist: abundant redemption, popular missions, Alphonsian moral theology.",
        "affirmations": ["Copiosa apud eum redemptio", "Preach to most abandoned", "Equiprobabilism"]
    },
    "SDB": {
        "summary": "Salesian: Don Bosco's preventive system, joy, youth education, Mary Help of Christians.",
        "affirmations": ["Education is matter of heart", "Reason, religion, loving-kindness"]
    },
    "CM": {
        "summary": "Vincentian: service to poor, clergy formation, simplicity, humility, practical charity.",
        "affirmations": ["Poor are our masters", "Simplicity, humility, charity", "Love in action"]
    },
    "CP": {
        "summary": "Passionist: memoria passionis, contemplation of Christ's suffering, preaching missions.",
        "affirmations": ["Keep memory of Passion alive", "Suffering united to Christ redeems"]
    },
    "OSM": {
        "summary": "Servite: servants of Mary, compassion at Cross, Marian devotion, Seven Holy Founders.",
        "affirmations": ["Stand with Mary at Cross", "Compassion as way of life"]
    },
    "OPRAEM": {
        "summary": "Norbertine: canons regular, liturgical solemnity, communal life, active-contemplative balance.",
        "affirmations": ["Contemplata aliis tradere", "Solemn liturgy sanctifies"]
    },
    "MERC": {
        "summary": "Mercedarian: ransom of captives, fourth vow to give life for captives, Marian devotion.",
        "affirmations": ["Free captive at any cost", "Mary of Mercy liberates"]
    },
    "CSC": {
        "summary": "Holy Cross: education as apostolate, hope in Cross, zeal for souls.",
        "affirmations": ["Cross is our only hope", "Education of mind and heart"]
    },
    "OSBCAM": {
        "summary": "Camaldolese: eremitical Benedictine reform, threefold good, flexibility.",
        "affirmations": ["Solitude deepens communion", "Hermitage and cenobium united"]
    },
    "NEOPLAT": {
        "summary": "Christian Neo-Platonism: participatory metaphysics, divine ideas, ascent of soul.",
        "affirmations": ["Reality participates in divine forms", "Beauty leads to Beautiful itself"]
    },
    "THOMMETA": {
        "summary": "Thomistic realism: act-potency, matter-form, being as analogical.",
        "affirmations": ["Being is analogical", "Aristotelian categories serve theology"]
    },
    "SCOTMETA": {
        "summary": "Scotist metaphysics: univocity of being, formal distinction, haecceity.",
        "affirmations": ["Being is univocal", "Individuation by haecceity"]
    },
    "PALAM": {
        "summary": "Palamite theology: essence-energies distinction, theosis through uncreated energies.",
        "affirmations": ["God's energies are participated", "Theosis is real deification"]
    },
    "RESSCH": {
        "summary": "Ressourcement Christology: Christ's concrete humanity, patristic retrieval.",
        "affirmations": ["Christ's humanity is central", "Chalcedon read through Cyril"]
    },
    "CHALMAX": {
        "summary": "Chalcedonian Maximalist: strict two natures, two wills, two operations.",
        "affirmations": ["Two natures without confusion", "Dyothelitism essential"]
    },
    "KENOT": {
        "summary": "Kenotic Christology: Philippians 2 self-emptying, Christ genuinely limited.",
        "affirmations": ["Christ truly emptied himself", "Solidarity with human weakness"]
    },
    "TRIDSAC": {
        "summary": "Tridentine sacramentology: ex opere operato, proper matter and form.",
        "affirmations": ["Sacraments confer grace ex opere operato", "Trent irreformable"]
    },
    "THOMSAC": {
        "summary": "Thomistic sacramentology: sacraments as instrumental causes.",
        "affirmations": ["Sacraments are instrumental causes", "Character configures to Christ"]
    },
    "AUGSAC": {
        "summary": "Augustinian sacramentology: faith and interiority, visible words.",
        "affirmations": ["Word joined to element makes sacrament"]
    },
    "MINSAC": {
        "summary": "Minimalist sacramental: focus on essentials for validity.",
        "affirmations": ["Essential form and matter suffice"]
    },
    "EASTSAC": {
        "summary": "Eastern sacramental: mystery emphasis, epiclesis, theosis orientation.",
        "affirmations": ["Sacraments are holy mysteries", "Liturgy is heaven on earth"]
    },
    "EUCHMYST": {
        "summary": "Eucharistic mysticism: personal encounter with Christ, adoration.",
        "affirmations": ["Eucharist is heart of Christian life", "Adoration deepens communion"]
    },
    "ULTRA": {
        "summary": "Ultramontanism: strong papal authority, infallibility maximally interpreted.",
        "affirmations": ["Pope has supreme jurisdiction everywhere"]
    },
    "PAPMOD": {
        "summary": "Moderate papalism: primacy and infallibility with episcopal collegiality.",
        "affirmations": ["Pope has primacy, bishops are true pastors"]
    },
    "PAPMIN": {
        "summary": "Papal minimalism: infallibility strictly and rarely applied.",
        "affirmations": ["Infallibility rare and narrow"]
    },
    "GALL": {
        "summary": "Gallicanism: national church autonomy, conciliar limits on pope.",
        "affirmations": ["National churches have autonomy"]
    },
    "CONCIL": {
        "summary": "Conciliarism: councils supreme, can limit pope in emergencies.",
        "affirmations": ["Council can depose erring pope"]
    },
    "EASTECC": {
        "summary": "Eastern Catholic ecclesiology: communion of churches, patriarchal structures.",
        "affirmations": ["Church is communion of churches"]
    },
    "SYNOD": {
        "summary": "Synodalist: synodal processes, listening, pilgrim people.",
        "affirmations": ["Synodality constitutive of Church"]
    },
    "THOMMOR": {
        "summary": "Thomistic natural law: acts ordered to end, virtue perfects nature.",
        "affirmations": ["Natural law participates in eternal law"]
    },
    "MANUAL": {
        "summary": "Manualist moral theology: systematic treatment, confession-focused.",
        "affirmations": ["Clear categories aid confessors"]
    },
    "VIRTUE": {
        "summary": "Virtue ethics: character, habituation, practical wisdom.",
        "affirmations": ["Character over isolated acts"]
    },
    "AUGMOR": {
        "summary": "Augustinian moral: rightly ordered love, grace for virtue.",
        "affirmations": ["Love is form of virtues"]
    },
    "PERSMOR": {
        "summary": "Personalist moral: dignity of person, conscience emphasized.",
        "affirmations": ["Person never merely a means"]
    },
    "PROP": {
        "summary": "Proportionalism: weighing proportionate reasons in moral evaluation.",
        "affirmations": ["Proportionate reason can justify"]
    },
    "NEOSCH": {
        "summary": "Neo-scholastic rigorism: strict manual tradition, moral absolutes.",
        "affirmations": ["Moral absolutes admit no exceptions"]
    },
    "CASUIST": {
        "summary": "Casuistry: case-based moral reasoning, practical wisdom.",
        "affirmations": ["Cases illuminate principles"]
    },
    "LIBCATH": {
        "summary": "Liberal Catholicism: dialogue with modernity, religious freedom.",
        "affirmations": ["Dignitatis Humanae is development"]
    },
    "SOCDEM": {
        "summary": "Catholic social democracy: welfare state, workers protections.",
        "affirmations": ["State has role in justice"]
    },
    "LIBERTAR": {
        "summary": "Catholic libertarianism: free markets, minimal state.",
        "affirmations": ["Economic freedom is right"]
    },
    "AGRAR": {
        "summary": "Catholic agrarianism: rural life ideal, distributed land.",
        "affirmations": ["Land is proper basis of economy"]
    },
    "TRAD": {
        "summary": "Traditionalist: traditional liturgy, doctrine, discipline.",
        "affirmations": ["Traditional Latin Mass normative"]
    },
    "ROTR": {
        "summary": "Reform of the Reform: improve Novus Ordo with traditional elements.",
        "affirmations": ["Novus Ordo can be reverent"]
    },
    "PROG": {
        "summary": "Progressive Catholic: ongoing reform, pastoral accompaniment.",
        "affirmations": ["Church must continually reform"]
    },
    "RESS": {
        "summary": "Ressourcement: return to patristic and biblical sources.",
        "affirmations": ["Fathers are primary sources"]
    },
    "ORDINAR": {
        "summary": "Anglican patrimony within Catholicism; Divine Worship liturgy, English choral tradition, married priesthood exception.",
        "affirmations": ["Anglican patrimony enriches Catholicism", "Divine Worship is legitimate liturgical expression", "Vernacular solemnity is possible"]
    },
    "EASTLIT": {
        "summary": "Strong preference for Byzantine/Eastern liturgical forms; may attend Eastern Catholic parishes.",
        "affirmations": ["Eastern liturgies preserved ancient forms", "The West has much to learn from the East", "Liturgical diversity is treasure"]
    },
    "ORTHOPH": {
        "summary": "Strong Eastern Orthodox sympathies; values Orthodox liturgy, theology, and spirituality while remaining Catholic.",
        "affirmations": ["Orthodoxy preserved much the West lost", "Palamite theology is valuable", "Filioque is negotiable"]
    },
    "LUTHCAT": {
        "summary": "Affirms Lutheran-Catholic convergence on justification; JDDJ as genuine ecumenical achievement.",
        "affirmations": ["JDDJ represents real progress", "Faith alone rightly understood is Catholic", "Ecumenical progress is real"]
    },
    "ECUMON": {
        "summary": "Catholics open to dialogue on Protestant soteriology; sees possible convergence on grace.",
        "affirmations": ["Augustinian heritage is shared", "Sola fide can be understood orthodoxly", "Dialogue advances truth"]
    },
    "ANTIMOD": {
        "summary": "Emphasis on Pascendi, Lamentabili, anti-Modernist oath; suspicious of post-conciliar updating.",
        "affirmations": ["Modernism is synthesis of all heresies", "Anti-Modernist oath should be restored", "Aggiornamento was disaster"]
    },
    "DEVPROG": {
        "summary": "Newman-style development of doctrine; organic growth from seminal principles; neither rigid nor rupturist.",
        "affirmations": ["Doctrine develops organically", "Later definitions make explicit what was implicit", "Development is not corruption"]
    },
    "COMMUN": {
        "summary": "Communio school: Balthasar, Ratzinger, de Lubac; ecclesiology of communion, Christocentric focus.",
        "affirmations": ["Church is communion of persons", "Christocentrism integrates all theology", "Ressourcement and aggiornamento balance"]
    },
    "RADORTH": {
        "summary": "Radical Orthodoxy (Milbank, Pickstock); critique of secular modernity, participatory ontology.",
        "affirmations": ["Secular reason is heretical", "All truth participates in divine truth", "Modernity must be narrated theologically"]
    },
    "TRADUM": {
        "summary": "Traditional preferences within Traditionis Custodes restrictions; obedient but grieving; hopes for restoration.",
        "affirmations": ["Obedience to Pope even when painful", "TLM will eventually be freed", "Work within system for reform"]
    },

}

for code, desc in EXTENDED_DESC.items():
    if code not in SCHOOL_DESC:
        SCHOOL_DESC[code] = desc
    elif SCHOOL_DESC[code].get("summary", "").startswith("The "):
        SCHOOL_DESC[code] = desc

for code in SCHOOL_CODES:
    if code not in SCHOOL_DESC:
        SCHOOL_DESC[code] = {
            "summary": f"The {SCHOOL_NAME[code]} position.",
            "affirmations": ["See detailed theological literature"]
        }

# ----------------------------
# 2) ALL MULTIPLE CHOICE QUESTIONS
# ----------------------------
QUESTIONS = [
    # ==================== SCRIPTURE, TRADITION & HERMENEUTICS ====================
    {
        "text": "How would you rank the normative authority of Scripture, Tradition, and the Magisterium?",
        "options": [
            (
                "Scripture has the highest dignity and is the supreme norm, but only as read within apostolic Tradition and the Church's infallible teaching.",
                {"NEOAUG": 4, "RESS": 3, "AUG": 2, "BENED": 1, "ORAT": 1, "STD": 1},
            ),
            (
                "Scripture and Tradition are co-equal fonts of revelation, while the Magisterium is their authoritative interpreter and guardian.",
                {"THOM": 3, "THOMMETA": 2, "TRIDSAC": 1, "PAPMOD": 2, "STD": 2, "DOM": 1},
            ),
            (
                "In practice, the Magisterium is the proximate rule of faith; Scripture and Tradition are received through that living authority.",
                {"ULTRA": 4, "PAPMOD": 2, "INTEG": 2, "NEOSCH": 1},
            ),
            (
                "The hierarchy can err widely in non-definitive matters; Scripture and the Fathers supply the main corrective.",
                {"SSPX": 3, "TRAD": 2, "ROTR": 1, "NEOAUG": 1, "PAPMIN": 1},
            ),
        ],
        "axis_weights": {"SCRIPT": 4},
    },
    {
        "text": "Which approach best describes how Scripture should normally be interpreted in theology and preaching?",
        "options": [
            (
                "Patristic exegesis (literal + spiritual senses) should normally govern; historical criticism is secondary and constrained.",
                {"RESS": 3, "NEOAUG": 2, "AUG": 2, "BENED": 2, "TRAD": 2, "NEOPLAT": 1},
            ),
            (
                "Historical-grammatical meaning is primary; spiritual senses are real but must be controlled by the literal sense.",
                {"THOM": 3, "DOM": 2, "THOMMETA": 1, "STD": 2},
            ),
            (
                "Historical-critical methods are useful and often necessary, but must be disciplined by dogma and the Church's rule of faith.",
                {"PAPMOD": 2, "RESS": 2, "STD": 2, "JES": 2, "NEOAUG": 1},
            ),
            (
                "The text's meaning is best read through contemporary experience and community reception.",
                {"PROG": 3, "PERSMOR": 2, "LIBCATH": 1},
            ),
        ],
        "axis_weights": {"SCRIPT": 3},
    },
    {
        "text": "In theological disputes, which is the normal direction of reasoning?",
        "options": [
            (
                "Scripture (as received in the Church) judges theology; systems must be revised to fit Scripture's full witness.",
                {"NEOAUG": 3, "RESS": 2, "AUG": 2, "BENED": 1},
            ),
            (
                "Dogma and metaphysics provide the framework that stabilizes interpretation; Scripture is read within that settled grammar.",
                {"THOM": 3, "THOMMETA": 2, "NEOSCH": 2, "DOM": 1},
            ),
            (
                "The living Magisterium provides the proximate norm; speculative resolution is less important than obedience.",
                {"ULTRA": 3, "PAPMOD": 2, "STD": 1},
            ),
            (
                "Multiple theologies can legitimately coexist; Scripture underdetermines systematic disputes.",
                {"STD": 2, "PAPMOD": 1, "RESS": 1, "PROG": 1},
            ),
        ],
        "axis_weights": {"SCRIPT": 3},
    },
    {
        "text": "Which Bible translation posture best serves the Church?",
        "options": [
            (
                "Liturgical stability and doctrinal continuity: a formal, traditional Catholic translation style.",
                {"BENED": 3, "TRAD": 2, "TRIDSAC": 2, "NEOSCH": 1, "ROTR": 1},
            ),
            (
                "Critical-text precision: modern scholarly editions are valuable so long as doctrine governs interpretation.",
                {"DOM": 2, "THOM": 2, "JES": 2, "PAPMOD": 1, "STD": 2},
            ),
            (
                "Pastoral accessibility: clarity for modern readers is the priority.",
                {"PROG": 2, "PERSMOR": 2, "LIBCATH": 1, "STD": 1},
            ),
            (
                "Different translations for different uses (liturgy vs study vs devotion).",
                {"STD": 3, "RESS": 1, "PAPMOD": 1},
            ),
        ],
        "axis_weights": {"SCRIPT": 2, "LIT": 1},
    },

    # ==================== JUSTIFICATION, UNION & INCREASE OF GRACE ====================
    {
        "text": "Justification consists primarily in…",
        "options": [
            (
                "A real interior renewal by infused grace: God makes the soul righteous (not merely declared so).",
                {"THOM": 3, "THOMSAC": 1, "TRIDSAC": 2, "THOMMOR": 1, "DOM": 1, "STD": 1},
            ),
            (
                "A real participation in Christ Himself: union with Christ is the core, with forensic language secondary.",
                {"NEOAUG": 4, "RESS": 2, "AUG": 2, "EUCHMYST": 1, "BENED": 1, "PALAM": 1},
            ),
            (
                "Primarily a forensic declaration (acquittal) with sanctification following as a distinct work.",
                {"JANS": 3, "AUGP": 2, "NEOSCH": 1, "MANUAL": 1},
            ),
            (
                "A covenantal status within the people of God; categories of 'infused habit' are less central.",
                {"PROG": 2, "PERSMOR": 1, "TRANSIG": 1, "STD": 1},
            ),
        ],
        "axis_weights": {"JUST": 4, "GRACE": 1},
    },
    {
        "text": "After baptism, can justification increase?",
        "options": [
            (
                "Yes: one can truly grow in grace and righteousness (while remaining entirely dependent on grace).",
                {"THOM": 3, "AUG": 2, "TRIDSAC": 2, "STD": 1},
            ),
            (
                "Yes, best described as deeper participation/union with Christ rather than as a 'quantity' of righteousness.",
                {"NEOAUG": 3, "RESS": 2, "AUG": 1, "PALAM": 1},
            ),
            (
                "No: justification is complete as a verdict; only sanctification increases.",
                {"JANS": 2, "AUGP": 1, "MANUAL": 1},
            ),
            (
                "The question is misleading; use primarily relational language.",
                {"PROG": 2, "PERSMOR": 1},
            ),
        ],
        "axis_weights": {"JUST": 3},
    },
    {
        "text": "How are justification and sanctification related?",
        "options": [
            (
                "Distinct but inseparable graces: God both forgives and makes holy; separating them distorts the Gospel.",
                {"THOM": 2, "NEOAUG": 2, "RESS": 1, "AUG": 2, "STD": 2},
            ),
            (
                "Justification is logically prior; sanctification follows as fruit, and confusing them risks works-righteousness.",
                {"MANUAL": 2, "NEOSCH": 1, "AUGP": 1, "JANS": 1},
            ),
            (
                "Union with Christ is prior: both justification and sanctification flow from participation in Christ.",
                {"NEOAUG": 3, "RESS": 2, "PALAM": 2, "EUCHMYST": 1},
            ),
            (
                "Pastoral framing matters more than precise distinctions; emphasize accompaniment and growth.",
                {"PERSMOR": 2, "PROG": 2, "LIBCATH": 1},
            ),
        ],
        "axis_weights": {"JUST": 3},
    },

    # ==================== SIN, CONCUPISCENCE & MORAL PSYCHOLOGY ====================
    {
        "text": "Post-baptismal concupiscence is best described as…",
        "options": [
            (
                "A disordered inclination that remains as a wound and penalty, but is not sin unless consented to.",
                {"THOM": 3, "THOMMOR": 2, "TRIDSAC": 1, "STD": 2},
            ),
            (
                "Not formally sin, but it can carry derivative moral responsibility insofar as it flows from prior voluntary vice and culpable negligence.",
                {"AUG": 3, "NEOAUG": 2, "AUGMOR": 2, "VIRTUE": 1, "NEOPLAT": 1},
            ),
            (
                "In itself it is truly sin in the regenerate (even without consent), though not always imputable in the same way.",
                {"JANS": 4, "AUGP": 2, "TUTIOR": 1},
            ),
            (
                "Primarily a psychological phenomenon; 'sin' language should be reserved for conscious harmful choices.",
                {"PROG": 3, "PERSMOR": 2},
            ),
        ],
        "axis_weights": {"RIGOR": 2, "GRACE": 1},
    },
    {
        "text": "Habitual vice formed by prior voluntary sin…",
        "options": [
            (
                "Can incur guilt through culpable omission: failure to pursue virtue and remedies becomes morally weighty.",
                {"AUG": 2, "AUGMOR": 2, "VIRTUE": 2, "NEOSCH": 1},
            ),
            (
                "Is a dangerous disposition, but guilt attaches only to present voluntary acts and consent.",
                {"THOM": 2, "THOMMOR": 2, "STD": 1},
            ),
            (
                "Shows that the will is deeply bound; strict ascetic discipline and frequent confession are the safest path.",
                {"TRAD": 2, "MANUAL": 2, "NEOSCH": 2, "TUTIOR": 1},
            ),
            (
                "The Church should avoid scrupulosity: focus on healing and gradual growth.",
                {"PERSMOR": 2, "PROG": 2},
            ),
        ],
        "axis_weights": {"RIGOR": 2},
    },

    # ==================== ASSURANCE, PERSEVERANCE & FINAL SALVATION ====================
    {
        "text": "Can a Christian know they are presently in the state of grace?",
        "options": [
            (
                "Not with absolute certainty, but one can have moral confidence through signs, humility, and the sacraments.",
                {"THOM": 3, "STD": 2, "PAPMOD": 1},
            ),
            (
                "One should maintain hopeful trust without seeking assurance; fear and humility protect against presumption.",
                {"AUG": 2, "AUGP": 1, "TRAD": 1, "NEOSCH": 1},
            ),
            (
                "Strong assurance is spiritually dangerous and usually presumption; emphasize penitence.",
                {"JANS": 3, "TUTIOR": 2, "MANUAL": 1},
            ),
            (
                "Interior peace is a sufficient indicator; anxiety about grace is unhealthy.",
                {"PROG": 2, "PERSMOR": 2},
            ),
        ],
        "axis_weights": {"JUST": 2, "ESCH": 2},
    },
    {
        "text": "Final perseverance is best described as…",
        "options": [
            (
                "A special grace to be humbly prayed for; not guaranteed, but God is faithful.",
                {"THOM": 3, "AUG": 2, "STD": 2, "DOM": 1},
            ),
            (
                "Infallibly granted to those truly predestined; the elect cannot finally fall away.",
                {"AUGP": 2, "JANS": 3, "SUPRA": 1},
            ),
            (
                "A mystery better handled pastorally than speculatively; emphasize fidelity in the present.",
                {"PAPMOD": 2, "STD": 2, "RESS": 1},
            ),
            (
                "Assurance of salvation is central to the Gospel's comfort; excessive emphasis on uncertainty is harmful.",
                {"PROG": 2, "LIBCATH": 1, "PERSMOR": 1},
            ),
        ],
        "axis_weights": {"GRACE": 2, "ESCH": 2},
    },

    # ==================== ESCHATOLOGY & FINAL JUDGMENT ====================
    {
        "text": "The Christian life is primarily oriented toward…",
        "options": [
            (
                "The Beatific Vision: loving contemplation of God as final end.",
                {"THOM": 3, "BENED": 2, "DOM": 1, "STD": 1},
            ),
            (
                "Final judgment and salvation from damnation: vigilance, penitence, and fear of the Lord.",
                {"JANS": 3, "TRAD": 2, "NEOSCH": 2, "MANUAL": 1, "TUTIOR": 1},
            ),
            (
                "Theosis/deification: participation in divine life as transformative communion.",
                {"PALAM": 4, "EASTSAC": 2, "EUCHMYST": 2, "NEOPLAT": 1, "RESS": 1},
            ),
            (
                "Renewal of the world and social holiness: the Church's mission in history.",
                {"PROG": 3, "SOCDEM": 1, "WORKERCATH": 1, "PERSMOR": 1},
            ),
        ],
        "axis_weights": {"ESCH": 4},
    },
    {
        "text": "Purgatory is best understood primarily as…",
        "options": [
            (
                "Satisfaction and purification from temporal punishment due to sin.",
                {"MANUAL": 2, "NEOSCH": 2, "TRAD": 1, "STD": 1},
            ),
            (
                "Final purification of love: removal of attachments so the soul can see God.",
                {"THOM": 2, "BENED": 2, "RESS": 1, "NEOAUG": 1, "STD": 2},
            ),
            (
                "An encounter with divine fire that heals and illumines (Eastern-leaning emphasis).",
                {"PALAM": 3, "EASTSAC": 2, "EUCHMYST": 1, "NEOPLAT": 1},
            ),
            (
                "A symbol pointing to God's mercy; details shouldn't be systematized.",
                {"PROG": 2, "PERSMOR": 1},
            ),
        ],
        "axis_weights": {"ESCH": 3, "RIGOR": 1},
    },

    # ==================== CONSCIENCE, ASSENT & ECCLESIAL BELONGING ====================
    {
        "text": "If a non-definitive magisterial teaching seems doubtful or imprudent, what is the Catholic posture?",
        "options": [
            (
                "Interior assent is normally required; public disagreement risks scandal and disobedience.",
                {"ULTRA": 3, "PAPMOD": 1, "INTEG": 1},
            ),
            (
                "Religious submission is owed, but one may withhold interior assent cautiously while seeking clarification and remaining obedient.",
                {"PAPMOD": 3, "STD": 3, "THOM": 1},
            ),
            (
                "Respectful, reasoned critique is sometimes necessary; the Fathers and Tradition can correct modern confusions.",
                {"RESS": 2, "NEOAUG": 2, "TRAD": 2, "SSPX": 2, "PAPMIN": 1},
            ),
            (
                "If it conflicts with Tradition, public resistance is justified.",
                {"SSPX": 3, "TRAD": 2, "SEDEPRIV": 1, "SEDE": 1},
            ),
            (
                "Conscience is supreme; dissent can be fully legitimate.",
                {"PROG": 3, "LIBCATH": 2, "PERSMOR": 1},
            ),
        ],
        "axis_weights": {"PAPAL": 2, "SCRIPT": 1},
    },
    {
        "text": "Theologians primarily serve the Church by…",
        "options": [
            (
                "Clarifying and defending settled doctrine with precision (often scholastic).",
                {"DOM": 2, "THOM": 2, "NEOSCH": 2, "MANUAL": 1},
            ),
            (
                "Retrieving the Fathers and liturgical tradition to renew theology (ressourcement).",
                {"RESS": 3, "NEOAUG": 2, "BENED": 1, "NEOPLAT": 1},
            ),
            (
                "Mediating doctrine pastorally for modern contexts while preserving essentials.",
                {"PAPMOD": 2, "STD": 2, "JES": 2, "PERSMOR": 1},
            ),
            (
                "Testing boundaries and developing new paradigms to meet contemporary needs.",
                {"PROG": 3, "LIBCATH": 1},
            ),
        ],
        "axis_weights": {"SCRIPT": 1},
    },

    # ==================== GRACE & PREDESTINATION ====================
    {
        "text": "What is the relationship between fallen human nature and the ability to do good?",
        "options": [
            ("Fallen humans can do natural goods but absolutely cannot move toward salvation without prevenient grace",
             {"AUG": 3, "AUGP": 3, "THOM": 2, "BANEZ": 2, "JANS": 2}),
            ("Fallen humans retain significant natural capacity; grace assists but doesn't wholly initiate",
             {"SEMIAUG": 3, "MOL": 2, "PROG": 1}),
            ("Human nature is so corrupted that even natural goods are tainted without grace",
             {"JANS": 3, "AUGP": 2}),
            ("Grace and nature cooperate from the start; the distinction is somewhat artificial",
             {"NEOAUG": 2, "RESS": 2}),
        ],
        "axis_weights": {"GRACE": 1}
    },
    {
        "text": "How does God's grace relate to human freedom in salvation?",
        "options": [
            ("Grace is intrinsically efficacious—it infallibly moves the will while preserving freedom (Bañezian)",
             {"BANEZ": 3, "THOMP": 2, "DOM": 2, "AUGP": 2}),
            ("Grace is extrinsically efficacious through God's middle knowledge of free response (Molinist)",
             {"MOL": 3, "JES": 2, "CONG": 1}),
            ("Grace is congruous—fitted to circumstances so it will be freely accepted (Congruist)",
             {"CONG": 3, "JES": 1, "MOL": 1}),
            ("Grace heals and elevates nature, enabling but not determining free response (Thomist)",
             {"THOM": 3, "DOM": 1}),
            ("Grace is offered universally; efficacy depends wholly on human cooperation",
             {"SEMIAUG": 2, "PROG": 1}),
        ],
        "axis_weights": {"GRACE": 2}
    },
    {
        "text": "How should we understand predestination?",
        "options": [
            ("Primarily as God's merciful choice to save some from the massa damnata",
             {"AUG": 3, "THOM": 2, "INFRA": 2}),
            ("As a symmetrical doctrine: God actively predestines some to glory, others to reprobation",
             {"AUGP": 2, "JANS": 2, "SUPRA": 1}),
            ("Post praevisa merita: God predestines based on foreseen merits and faith",
             {"MOL": 3, "JES": 2, "SEMIAUG": 2}),
            ("The question is mysterious and best left to divine wisdom without systematic resolution",
             {"STD": 2, "RESS": 1}),
        ],
        "axis_weights": {"GRACE": 1}
    },
    {
        "text": "Regarding the logical order of God's decrees about predestination and the Fall:",
        "options": [
            ("Supralapsarian: Election/reprobation logically precedes the decree to permit the Fall",
             {"SUPRA": 3, "AUGP": 2, "JANS": 2}),
            ("Infralapsarian: Election logically follows the decree to permit the Fall",
             {"INFRA": 3, "AUG": 2, "THOM": 2}),
            ("Post praevisa merita: Election follows foreseen merits/faith",
             {"MOL": 3, "JES": 2, "SEMIAUG": 1}),
            ("The question is speculative and best left undetermined",
             {"STD": 2, "THOM": 1}),
        ],
        "axis_weights": {"GRACE": 2}
    },
    {
        "text": "Would the Incarnation have occurred if Adam had never sinned?",
        "options": [
            ("Yes—Christ is the absolute primacy of creation, independent of sin (Scotist)",
             {"SCOT": 3, "FRANC": 3, "SUPRA": 2, "CARM": 1}),
            ("No—the Incarnation was ordered primarily to redemption from sin (Thomist)",
             {"THOM": 3, "AUG": 2, "DOM": 1, "INFRA": 1}),
            ("Probably not, but the question is speculative",
             {"STD": 2}),
            ("Yes, but the mode would have been different (glorious rather than suffering)",
             {"NEOAUG": 2, "RESS": 1}),
        ],
        "axis_weights": {"GRACE": -1}
    },
    {
        "text": "What is the nature of sufficient grace?",
        "options": [
            ("Sufficient grace gives real power to act but becomes efficacious only with God's further motion",
             {"BANEZ": 3, "THOMP": 2, "DOM": 2}),
            ("Sufficient grace becomes efficacious through human free cooperation foreseen by middle knowledge",
             {"MOL": 3, "JES": 2, "CONG": 2}),
            ("The distinction between sufficient and efficacious grace is largely verbal",
             {"JANS": 2, "AUGP": 1}),
            ("Sufficient grace truly enables, and its becoming efficacious involves genuine synergy",
             {"SEMIAUG": 2, "THOM": 1}),
        ],
        "axis_weights": {"GRACE": 2}
    },

    # ==================== METAPHYSICS ====================
    {
        "text": "What is the relationship between God's will and God's intellect?",
        "options": [
            ("Intellectualist: God wills things because they are good; goodness is prior to willing",
             {"INTELL": 3, "THOM": 3, "DOM": 2, "THOMMETA": 2}),
            ("Voluntarist: Things are good because God wills them; divine will is the source of moral order",
             {"VOLUNT": 3, "SCOT": 2, "NOMIN": 2}),
            ("Modified voluntarism: God's will is primary but always acts according to wisdom",
             {"SCOT": 2, "VOLUNT": 1, "FRANC": 1}),
            ("The distinction is artificial; will and intellect are identical in God",
             {"PALAM": 2, "NEOPLAT": 1}),
        ],
        "axis_weights": {}
    },
    {
        "text": "What is the source of moral obligations?",
        "options": [
            ("Divine commands—things are good/evil because God wills them so",
             {"VOLUNT": 3, "SCOT": 2, "NOMIN": 2}),
            ("The nature of things known by reason—God wills them because they are good",
             {"THOM": 3, "INTELL": 3, "THOMMOR": 2, "DOM": 1}),
            ("Participation in eternal law, which is both rational and willed",
             {"AUG": 2, "NEOPLAT": 2, "THOM": 1}),
            ("A combination: God's will establishes positive law, but natural law reflects reason",
             {"STD": 2, "THOM": 1}),
        ],
        "axis_weights": {"RIGOR": 1}
    },
    {
        "text": "Regarding universals (like 'humanity' or 'justice'):",
        "options": [
            ("Moderate realism: Universals exist in things as real natures",
             {"THOMMETA": 3, "THOM": 2, "DOM": 1, "INTELL": 1}),
            ("Nominalism: Universals are only names/mental concepts; only particulars exist",
             {"NOMIN": 3, "VOLUNT": 1}),
            ("Platonic/Participatory: Universals exist primarily in the divine mind; things participate",
             {"NEOPLAT": 3, "AUG": 2, "FRANC": 1}),
            ("Scotist: Universals have a 'formal distinction'—less than real but more than nominal",
             {"SCOTMETA": 3, "SCOT": 2}),
        ],
        "axis_weights": {}
    },
    {
        "text": "What is the best framework for understanding being?",
        "options": [
            ("Analogy of being: Being is predicated analogically between God and creatures (Thomist)",
             {"THOMMETA": 3, "THOM": 3, "DOM": 2}),
            ("Univocity of being: Being is predicated in the same sense of God and creatures (Scotist)",
             {"SCOTMETA": 3, "SCOT": 3}),
            ("Participatory: Creatures participate in divine being without univocity or mere analogy",
             {"NEOPLAT": 3, "PALAM": 2}),
            ("The question is too abstract; focus on God's revealed names instead",
             {"NOMIN": 2, "VOLUNT": 1}),
        ],
        "axis_weights": {}
    },

    # ==================== RELIGIOUS ORDERS ====================
    {
        "text": "Which religious order's spirituality most resonates with you?",
        "options": [
            ("Dominican: Contemplation for preaching; truth and intellectual apostolate",
             {"DOM": 3, "THOM": 2, "INTELL": 1}),
            ("Jesuit: Finding God in all things; discernment, adaptability, active mission",
             {"JES": 3, "MOL": 1, "CONG": 1}),
            ("Franciscan: Poverty, simplicity, creation spirituality, affective devotion",
             {"FRAN": 3, "FRANC": 2, "SCOT": 1}),
            ("Carmelite: Contemplative prayer, mystical ascent, interior transformation",
             {"CARM": 3, "NEOPLAT": 1, "PALAM": 1}),
            ("Benedictine: Liturgy, stability, ora et labora, monastic rhythm",
             {"BENED": 3, "TRAD": 1, "TRIDSAC": 1}),
            ("Opus Dei: Sanctification of ordinary work, lay spirituality",
             {"OPUS": 3, "INTEG": 1, "NEOSCH": 1}),
            ("Oratorian: Community of secular priests, intellectual and pastoral",
             {"ORAT": 3, "STD": 1}),
            ("No particular preference / diocesan spirituality",
             {"STD": 2}),
        ],
        "axis_weights": {"PIETY": 1}
    },
    {
        "text": "What is the highest form of the religious life?",
        "options": [
            ("Contemplative life ordered to preaching and teaching (Dominican ideal)",
             {"DOM": 3, "THOM": 2}),
            ("Pure contemplation in solitude (Carthusian/Carmelite ideal)",
             {"CARM": 3, "CHART": 3, "BENED": 1}),
            ("Active apostolate for the greater glory of God (Jesuit ideal)",
             {"JES": 3, "OPUS": 1}),
            ("Liturgical prayer as the Church's public worship (Benedictine ideal)",
             {"BENED": 3, "TRAD": 1}),
            ("Evangelical poverty and simplicity among the people (Franciscan ideal)",
             {"FRAN": 3, "FRANC": 2}),
            ("Sanctification in ordinary secular life (Opus Dei ideal)",
             {"OPUS": 3}),
        ],
        "axis_weights": {"PIETY": 2}
    },

    # ==================== EUCHARISTIC THEOLOGY ====================
    {
        "text": "Which best expresses Christ's presence in the Eucharist?",
        "options": [
            ("Strict transubstantiation: Whole substance of bread/wine converts; only accidents remain",
             {"TRANSUB": 3, "TRIDSAC": 3, "THOMSAC": 2, "TRAD": 1}),
            ("Thomistic transubstantiation with precise metaphysical categories",
             {"THOMSAC": 3, "THOM": 2, "TRANSUB": 2}),
            ("Real presence affirmed, but transignification language can complement traditional terms",
             {"TRANSIG": 3, "RESS": 2, "PROG": 1}),
            ("Eastern approach: True change occurs but Latin metaphysics not binding",
             {"EASTSAC": 3, "EUCHMYST": 2, "PALAM": 1}),
            ("Mystery best approached contemplatively rather than philosophically defined",
             {"EUCHMYST": 3, "CARM": 1, "NEOPLAT": 1}),
        ],
        "axis_weights": {"LIT": 2}
    },
    {
        "text": "What is the primary way to understand the Eucharist?",
        "options": [
            ("Real, substantial presence of Christ's Body and Blood under sacramental species",
             {"TRANSUB": 3, "TRIDSAC": 3, "THOMSAC": 2, "TRAD": 2}),
            ("The sacrifice of Calvary made present—emphasis on propitiation",
             {"TRIDSAC": 3, "TRAD": 2, "MANUAL": 1}),
            ("Communion/meal: The gathered community encounters the Risen Lord",
             {"PROG": 2, "RESS": 1, "TRANSIG": 1}),
            ("Mystical participation in heavenly liturgy",
             {"EASTSAC": 3, "EUCHMYST": 2, "PALAM": 1}),
            ("All of the above in balance",
             {"STD": 2, "THOM": 1}),
        ],
        "axis_weights": {"LIT": 2}
    },
    {
        "text": "How do the sacraments cause grace?",
        "options": [
            ("Instrumental efficient causality—sacraments are true instruments that cause grace",
             {"THOMSAC": 3, "THOM": 3, "TRIDSAC": 2}),
            ("Moral causality—sacraments move God to give grace, not physical instruments",
             {"MINSAC": 2, "SCOT": 1}),
            ("Occasional causality—God gives grace on the occasion of sacramental rites",
             {"NOMIN": 2, "MINSAC": 1}),
            ("Mystical/symbolic causality—sacraments participate in and manifest grace",
             {"EASTSAC": 3, "NEOPLAT": 2, "AUGSAC": 1}),
        ],
        "axis_weights": {}
    },
    {
        "text": "Regarding ex opere operato (sacraments work by the rite performed):",
        "options": [
            ("Strongly affirm: Grace is given by valid administration regardless of minister's holiness",
             {"TRIDSAC": 3, "THOMSAC": 3, "THOM": 2, "STD": 2}),
            ("Affirm, but recipient's disposition significantly affects fruitfulness",
             {"THOM": 2, "AUGSAC": 2, "STD": 2}),
            ("The emphasis can obscure the importance of faith and community",
             {"PROG": 2, "TRANSIG": 1}),
            ("Valid but the Eastern tradition emphasizes epiclesis and mystery over mechanism",
             {"EASTSAC": 3, "PALAM": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== ECCLESIOLOGY ====================
    {
        "text": "What is the extent of papal authority?",
        "options": [
            ("Full, immediate, and ordinary jurisdiction over the entire Church (Ultramontane)",
             {"ULTRA": 3, "INTEG": 2}),
            ("Real primacy with ordinary jurisdiction, but exercised with restraint (Moderate)",
             {"PAPMOD": 3, "STD": 2}),
            ("Primacy of honor and final appeal, but not ordinary jurisdiction over all (Minimalist)",
             {"PAPMIN": 3, "GALL": 2, "EASTECC": 2}),
            ("Conciliar authority is superior to papal in certain circumstances",
             {"CONCIL": 3, "GALL": 2}),
        ],
        "axis_weights": {"PAPAL": 3}
    },
    {
        "text": "How should papal infallibility be understood?",
        "options": [
            ("Broadly: The ordinary magisterium shares in a kind of practical infallibility",
             {"ULTRA": 2, "INTEG": 1}),
            ("Narrowly: Only ex cathedra definitions on faith/morals are strictly infallible",
             {"PAPMIN": 3, "GALL": 2, "CONCIL": 2, "EASTECC": 2}),
            ("Moderately: Infallibility is rare but the ordinary magisterium binds seriously",
             {"PAPMOD": 3, "STD": 2, "THOM": 1}),
            ("The concept itself is problematic or needs significant qualification",
             {"PROG": 2, "CONCIL": 1}),
        ],
        "axis_weights": {"PAPAL": 1}
    },
    {
        "text": "Where does episcopal authority come from?",
        "options": [
            ("Directly from the Pope; bishops are essentially papal delegates",
             {"ULTRA": 3}),
            ("From Christ through episcopal consecration, but exercised in communion with Rome",
             {"PAPMIN": 2, "EASTECC": 3, "SYNOD": 2, "THOM": 1}),
            ("From Christ through consecration; Rome has primacy but not source of jurisdiction",
             {"GALL": 2, "CONCIL": 2, "PAPMIN": 2}),
            ("Bishops are true ordinaries with proper authority; papal primacy is real but limited",
             {"PAPMOD": 3, "STD": 2}),
        ],
        "axis_weights": {"PAPAL": 2}
    },
    {
        "text": "How did the early Church function?",
        "options": [
            ("Essentially as today—with Roman primacy and centralized authority",
             {"ULTRA": 3, "INTEG": 1}),
            ("More synodally and collegially, with Roman primacy developing over time",
             {"SYNOD": 3, "CONCIL": 3, "EASTECC": 2, "GALL": 2}),
            ("With real Roman primacy but more subsidiarity than later periods",
             {"PAPMOD": 2, "STD": 2}),
            ("As a communion of local churches with Rome as first among equals",
             {"EASTECC": 3, "SYNOD": 2, "PAPMIN": 2}),
        ],
        "axis_weights": {"PAPAL": 1}
    },
    {
        "text": "What is the proper model of Church unity?",
        "options": [
            ("Juridical unity under papal authority with doctrinal uniformity",
             {"ULTRA": 3, "INTEG": 2, "NEOSCH": 1}),
            ("Communion of churches united in faith, sacraments, and fellowship with Rome",
             {"EASTECC": 3, "SYNOD": 2, "PAPMOD": 2}),
            ("Unity in essentials, liberty in doubtful matters, charity in all",
             {"STD": 3, "PAPMOD": 2, "RESS": 1}),
            ("Conciliar unity: The college of bishops with the Pope as head",
             {"CONCIL": 2, "SYNOD": 2, "PAPMOD": 1}),
        ],
        "axis_weights": {"PAPAL": 1}
    },

    # ==================== TEMPORAL AUTHORITY & INTEGRALISM ====================
    {
        "text": "What is the proper relationship between Church and State?",
        "options": [
            ("Hard integralism: State must formally recognize Church and suppress public heresy",
             {"INTEGHARD": 3, "INTEG": 2, "TRAD": 1}),
            ("Soft integralism: State should favor true religion with prudential tolerance",
             {"INTEGSOFT": 3, "INTEG": 1, "STD": 1}),
            ("Separation with cooperation: Distinct spheres cooperating for human flourishing",
             {"PAPMOD": 2, "STD": 2, "RESS": 1}),
            ("Liberal Catholic: Religious liberty is a genuine right; separation protects both",
             {"LIBCATH": 3, "PROG": 2}),
            ("Depends entirely on circumstances; no model universally normative",
             {"STD": 2}),
        ],
        "axis_weights": {"PAPAL": 1, "RIGOR": 1}
    },
    {
        "text": "Should Catholic rulers defer to bishops on faith and morals?",
        "options": [
            ("Yes, always—temporal authority is subordinate to spiritual in these matters",
             {"INTEGHARD": 3, "INTEG": 2, "ULTRA": 2}),
            ("Generally yes, but rulers have their own prudential competence",
             {"INTEGSOFT": 2, "PAPMOD": 2, "STD": 1}),
            ("Only when the teaching is clear and definitive",
             {"GALL": 2, "PAPMIN": 1}),
            ("No—temporal and spiritual authority should be strictly separate",
             {"LIBCATH": 3, "PROG": 2}),
        ],
        "axis_weights": {"PAPAL": 2}
    },
    {
        "text": "Is a confessional Catholic state still the ideal?",
        "options": [
            ("Yes, absolutely—this is the perennial teaching of the Church",
             {"INTEGHARD": 3, "INTEG": 3, "TRAD": 2, "SSPX": 2}),
            ("In principle yes, but rarely prudent in modern pluralist societies",
             {"INTEGSOFT": 3, "STD": 1}),
            ("No—Dignitatis Humanae represents genuine doctrinal development",
             {"LIBCATH": 3, "PROG": 2, "RESS": 1}),
            ("The question is more complex than a simple yes/no",
             {"STD": 2, "PAPMOD": 1}),
        ],
        "axis_weights": {"PAPAL": 2, "LIT": 1}
    },
    {
        "text": "What is the relationship between Christ's kingship and political order?",
        "options": [
            ("Christ is King of nations; states should formally acknowledge this",
             {"INTEG": 3, "INTEGHARD": 3, "TRAD": 2}),
            ("Christ's kingship is primarily spiritual; political acknowledgment is optional",
             {"LIBCATH": 2, "PROG": 2}),
            ("Social kingship is real but expressed through culture more than law",
             {"INTEGSOFT": 3, "RESS": 1}),
            ("Christ's kingdom is not of this world in a political sense",
             {"PROG": 2, "LIBCATH": 1}),
        ],
        "axis_weights": {"PAPAL": 1}
    },

    # ==================== ECONOMICS ====================
    {
        "text": "Which economic vision best reflects Catholic social teaching?",
        "options": [
            ("Distributism: Wide property distribution; neither capitalism nor socialism",
             {"DISTRIBUT": 3, "INTEG": 1, "TRAD": 1}),
            ("Corporatism/Solidarism: Vocational groups mediate between individual and state",
             {"CORPCATH": 3, "INTEG": 1}),
            ("Social market economy: Free markets with strong social safety net",
             {"SOCDEM": 3, "LIBCATH": 1, "STD": 1}),
            ("Free market with minimal state, relying on private charity",
             {"LIBERTAR": 3}),
            ("Worker cooperatives and strong unions as primary vehicles for justice",
             {"WORKERCATH": 3, "SOCDEM": 1}),
            ("Catholic agrarianism: Return to the land and local economies",
             {"AGRAR": 3, "DISTRIBUT": 2, "TRAD": 1}),
        ],
        "axis_weights": {}
    },
    {
        "text": "Is a living wage a strict moral obligation?",
        "options": [
            ("Yes—employers must pay wages sufficient for dignified family support",
             {"WORKERCATH": 3, "DISTRIBUT": 2, "SOCDEM": 2, "CORPCATH": 2}),
            ("It's a strong moral ideal but circumstances may prevent it",
             {"STD": 2, "INTEG": 1}),
            ("Market wages are just if freely agreed; charity handles insufficiency",
             {"LIBERTAR": 3}),
            ("Yes, and the state should enforce it when employers fail",
             {"SOCDEM": 2, "WORKERCATH": 2}),
        ],
        "axis_weights": {"RIGOR": 1}
    },
    {
        "text": "What is the role of unions in Catholic social teaching?",
        "options": [
            ("Essential: Workers have a natural right to organize that must be respected",
             {"WORKERCATH": 3, "DISTRIBUT": 2, "SOCDEM": 2, "CORPCATH": 2}),
            ("Generally positive but can become corrupt or politically captured",
             {"STD": 2, "INTEG": 1}),
            ("Unnecessary in a truly free market; often harmful",
             {"LIBERTAR": 3}),
            ("Useful within a corporatist structure that includes all vocational groups",
             {"CORPCATH": 3}),
        ],
        "axis_weights": {}
    },
    {
        "text": "What is the proper scope of private property?",
        "options": [
            ("Wide distribution is essential; concentrated ownership is problematic",
             {"DISTRIBUT": 3, "WORKERCATH": 2, "AGRAR": 2}),
            ("Private property is a natural right with minimal restrictions",
             {"LIBERTAR": 3}),
            ("Property has a social mortgage; regulation for common good is justified",
             {"SOCDEM": 3, "WORKERCATH": 2}),
            ("Property should be organized through vocational/corporate bodies",
             {"CORPCATH": 3}),
        ],
        "axis_weights": {}
    },

    # ==================== NATIONALISM ====================
    {
        "text": "How should Catholics view national identity?",
        "options": [
            ("Nations are natural communities; Catholicism should be inculturated nationally",
             {"TRADNAT": 3, "INTEG": 1, "TRAD": 1}),
            ("The Church transcends nations; nationalism easily becomes idolatrous",
             {"CATHUNIV": 3, "PROG": 1, "JES": 1}),
            ("Moderate patriotism is healthy but subordinate to Catholic identity",
             {"STD": 2, "PAPMOD": 1}),
            ("National sovereignty defends against globalist ideologies hostile to faith",
             {"TRADNAT": 2, "INTEG": 2, "SSPX": 1}),
        ],
        "axis_weights": {"LIT": 1}
    },
    {
        "text": "How should Catholic nations approach immigration?",
        "options": [
            ("Prioritize cultural and religious compatibility over economic factors",
             {"TRADNAT": 3, "INTEG": 2, "INTEGHARD": 2}),
            ("Welcome the stranger as a Gospel imperative; borders are secondary",
             {"CATHUNIV": 3, "PROG": 2, "LIBCATH": 2}),
            ("Balance hospitality with legitimate concerns for common good",
             {"STD": 3, "PAPMOD": 2}),
            ("Local communities should decide without centralized immigration policy",
             {"DISTRIBUT": 2, "LIBERTAR": 1}),
        ],
        "axis_weights": {}
    },
    {
        "text": "Should the Church resist international institutions promoting secular values?",
        "options": [
            ("Yes, strongly—these institutions are hostile to natural law and faith",
             {"INTEG": 3, "TRADNAT": 3, "TRAD": 2, "SSPX": 2}),
            ("Engage critically but don't refuse all cooperation",
             {"STD": 2, "PAPMOD": 2}),
            ("Support international cooperation for peace and human rights",
             {"PROG": 2, "LIBCATH": 2, "CATHUNIV": 2}),
            ("Focus on local and national levels; international institutions are secondary",
             {"DISTRIBUT": 2, "TRADNAT": 1}),
        ],
        "axis_weights": {"RIGOR": 1}
    },

    # ==================== MORAL THEOLOGY ====================
    {
        "text": "What is the best approach to moral theology?",
        "options": [
            ("Virtue ethics: Focus on character formation and the virtues",
             {"VIRTUE": 3, "THOMMOR": 2, "RESS": 1}),
            ("Natural law: Universal norms knowable by reason, applied through casuistry",
             {"THOMMOR": 3, "MANUAL": 2, "NEOSCH": 1}),
            ("Personalist: Emphasis on human dignity and concrete situations",
             {"PERSMOR": 3, "PROG": 1}),
            ("Manualist: Clear rules and cases for confessional practice",
             {"MANUAL": 3, "NEOSCH": 2, "CASUIST": 2}),
        ],
        "axis_weights": {"RIGOR": -1}
    },
    {
        "text": "Do universal moral norms admit exceptions in concrete circumstances?",
        "options": [
            ("Never for intrinsically evil acts; prudence applies norms, doesn't create exceptions",
             {"THOMMOR": 3, "MANUAL": 3, "NEOSCH": 3}),
            ("Proportionate reason can justify apparent exceptions (Proportionalism)",
             {"PROP": 3, "PROG": 2}),
            ("Pastoral discernment may find that a norm doesn't apply in a particular case",
             {"PERSMOR": 2, "PROG": 2}),
            ("Epikeia allows departure from law's letter to fulfill its spirit",
             {"THOM": 2, "VIRTUE": 1}),
        ],
        "axis_weights": {"RIGOR": -2}
    },
    {
        "text": "How should a confessor handle doubtful cases?",
        "options": [
            ("Tutiorism: Always follow the safer opinion favoring the law",
             {"TUTIOR": 3, "JANS": 2, "NEOSCH": 2}),
            ("Probabilism: A solidly probable opinion favoring liberty may be followed",
             {"PROBAB": 3, "JES": 2, "MOL": 1}),
            ("Equiprobabilism: Follow liberty only if equally or more probable than law",
             {"THOMMOR": 2, "STD": 2}),
            ("Laxism: Any probable opinion may be followed (condemned but historically relevant)",
             {"PROP": 1}),
        ],
        "axis_weights": {"RIGOR": 2}
    },
    {
        "text": "What is the value of the manualist tradition in moral theology?",
        "options": [
            ("Essential: Provides clarity, precision, and practical guidance for confessors",
             {"MANUAL": 3, "NEOSCH": 2, "TRAD": 2, "CASUIST": 2}),
            ("Useful but needs integration with virtue ethics and Scripture",
             {"THOMMOR": 2, "STD": 2}),
            ("Problematic: Legalistic, minimalistic, and detached from spiritual growth",
             {"VIRTUE": 2, "PERSMOR": 2, "RESS": 2, "PROG": 1}),
            ("Outdated and should be largely set aside",
             {"PROP": 2, "PROG": 2}),
        ],
        "axis_weights": {"RIGOR": 2}
    },

    # ==================== LITURGY ====================
    {
        "text": "Which direction should the priest face during the Eucharistic Prayer?",
        "options": [
            ("Ad orientem (same direction as people): Expresses common worship toward God",
             {"TRAD": 3, "TRIDSAC": 3, "ROTR": 2, "SSPX": 3, "BENED": 2}),
            ("Versus populum (facing people): Emphasizes community and participation",
             {"PROG": 3}),
            ("Either is legitimate depending on circumstances",
             {"STD": 2, "ROTR": 1}),
            ("The question is secondary to interior participation",
             {"RESS": 1, "CARM": 1}),
        ],
        "axis_weights": {"LIT": 3}
    },
    {
        "text": "How should Holy Communion be received?",
        "options": [
            ("On the tongue while kneeling: Traditional and most reverent",
             {"TRAD": 3, "TRIDSAC": 3, "SSPX": 3, "ROTR": 1}),
            ("On the tongue standing: Traditional but adapted",
             {"ROTR": 2, "STD": 1}),
            ("In the hand is legitimate and can express lay dignity",
             {"PROG": 2}),
            ("Either way with proper reverence; interior disposition matters most",
             {"STD": 2}),
        ],
        "axis_weights": {"LIT": 2}
    },
    {
        "text": "How should we evaluate the post-Vatican II liturgical reforms?",
        "options": [
            ("Largely mistaken: The Novus Ordo represents a break with tradition",
             {"SSPX": 3, "SEDE": 3, "TRAD": 2}),
            ("Good intentions but badly implemented; reform of the reform needed",
             {"ROTR": 3, "BENED": 2}),
            ("Generally positive: Made liturgy more accessible and participatory",
             {"PROG": 3, "STD": 1}),
            ("Legitimate development guided by the Council Fathers",
             {"STD": 2, "RESS": 1}),
        ],
        "axis_weights": {"LIT": 2}
    },
    {
        "text": "What is the proper place of the Traditional Latin Mass today?",
        "options": [
            ("Should be the normative form or at least freely available everywhere",
             {"TRAD": 3, "SSPX": 3, "SEDE": 3, "ROTR": 2}),
            ("A legitimate option that enriches the Church's liturgical life",
             {"ROTR": 2, "STD": 2, "BENED": 1}),
            ("Of historical interest but the reformed liturgy is the Church's lex orandi",
             {"PROG": 2}),
            ("Should be restricted to prevent division",
             {"PROG": 1}),
        ],
        "axis_weights": {"LIT": 3}
    },
    {
        "text": "What is the role of silence in the liturgy?",
        "options": [
            ("Essential: Sacred silence enables contemplation and encounter with mystery",
             {"TRAD": 3, "CARM": 2, "BENED": 2, "TRIDSAC": 2}),
            ("Important but balanced with congregational participation",
             {"STD": 2, "ROTR": 2}),
            ("Often excessive in pre-conciliar liturgy; active participation is key",
             {"PROG": 2}),
            ("Deeply valued in Eastern liturgy as part of the mystery",
             {"EASTSAC": 2, "PALAM": 1}),
        ],
        "axis_weights": {"LIT": 2, "PIETY": 1}
    },
    {
        "text": "How important is rubrical exactness in liturgy?",
        "options": [
            ("Very important: Rubrics protect the sacred and express theology",
             {"TRAD": 3, "TRIDSAC": 3, "MANUAL": 2, "NEOSCH": 2}),
            ("Important but not at the expense of pastoral adaptation",
             {"STD": 2, "ROTR": 1}),
            ("Secondary: The spirit of the liturgy matters more than exact rubrics",
             {"PROG": 2, "RESS": 1}),
            ("Rubrics serve the mystery and should be followed with understanding",
             {"BENED": 2, "THOM": 1}),
        ],
        "axis_weights": {"LIT": 2, "RIGOR": 1}
    },

    # ==================== VATICAN II & ECCLESIAL CRISIS ====================
    {
        "text": "How should we understand Vatican II's doctrinal status?",
        "options": [
            ("Fully authoritative ecumenical council binding on all Catholics",
             {"STD": 3, "PAPMOD": 2, "PROG": 2, "RESS": 2}),
            ("Authoritative but pastoral council that didn't define new dogma",
             {"ROTR": 2, "TRAD": 1}),
            ("Contains ambiguities/errors that need correction in light of tradition",
             {"SSPX": 3, "TRAD": 2}),
            ("A robber council or non-authoritative assembly",
             {"SEDE": 3, "SEDEPRIV": 2}),
        ],
        "axis_weights": {"LIT": 2, "PAPAL": -1}
    },
    {
        "text": "Regarding the post-1958 popes:",
        "options": [
            ("Fully legitimate popes with ordinary magisterial authority",
             {"STD": 3, "PAPMOD": 3, "PROG": 2, "RESS": 2}),
            ("Legitimate but their prudential decisions can be resisted when conflicting with Tradition",
             {"SSPX": 3, "TRAD": 2}),
            ("Material but not formal popes (Sedeprivationist thesis)",
             {"SEDEPRIV": 3}),
            ("Not true popes at all; the See has been vacant",
             {"SEDE": 3}),
        ],
        "axis_weights": {"PAPAL": -2, "LIT": 2}
    },
    {
        "text": "Can a Catholic resist or disobey Roman directives?",
        "options": [
            ("Never: Submission to Rome is essential to Catholic identity",
             {"ULTRA": 3, "PAPMOD": 1}),
            ("Only in extreme cases where directives clearly contradict defined doctrine",
             {"SSPX": 3, "TRAD": 2}),
            ("Yes, when they conflict with Sacred Tradition and the sensus fidelium",
             {"SSPX": 2, "SEDE": 2, "SEDEPRIV": 2}),
            ("Prudent disagreement is possible but public resistance is rarely justified",
             {"STD": 2, "PAPMOD": 2}),
        ],
        "axis_weights": {"PAPAL": -3}
    },

    # ==================== SPIRITUALITY & PRAYER ====================
    {
        "text": "What is the highest form of prayer?",
        "options": [
            ("Contemplative prayer: Simple loving gaze upon God",
             {"CARM": 3, "NEOPLAT": 2, "PALAM": 2}),
            ("The Holy Sacrifice of the Mass",
             {"BENED": 3, "TRIDSAC": 2, "TRAD": 2}),
            ("Liturgy of the Hours as the Church's official prayer",
             {"BENED": 3, "DOM": 1}),
            ("Lectio Divina: Prayerful reading of Scripture",
             {"BENED": 2, "RESS": 2}),
            ("Ignatian meditation with imagination and application of senses",
             {"JES": 3}),
            ("All are valid paths suited to different vocations",
             {"STD": 2}),
        ],
        "axis_weights": {"PIETY": 2}
    },
    {
        "text": "How important is mental prayer in the Christian life?",
        "options": [
            ("Essential: Daily mental prayer is morally necessary for serious Christians",
             {"CARM": 3, "JES": 2, "DOM": 2, "OPUS": 2}),
            ("Very important but vocal prayer and sacraments can suffice for some",
             {"STD": 2, "BENED": 1}),
            ("Helpful but not essential; the liturgy is sufficient",
             {"BENED": 2}),
            ("Overemphasized in some traditions; action and service matter more",
             {"PROG": 1}),
        ],
        "axis_weights": {"PIETY": 3}
    },
    {
        "text": "How should we understand mystical experiences?",
        "options": [
            ("Extraordinary graces given to some; not to be sought but accepted",
             {"CARM": 3, "DOM": 2, "THOM": 2}),
            ("The normal flowering of the life of grace available to all who persevere",
             {"CARM": 2, "NEOPLAT": 2}),
            ("Suspect: Focus on ordinary virtue and sacraments instead",
             {"MANUAL": 2, "NEOSCH": 1}),
            ("Central to Eastern spirituality: Theosis/deification is the goal",
             {"PALAM": 3, "EASTSAC": 2}),
        ],
        "axis_weights": {"PIETY": 2}
    },
    {
        "text": "How often should a devout Catholic go to confession?",
        "options": [
            ("Weekly or at least fortnightly, even without mortal sin",
             {"TRAD": 3, "CARM": 2, "OPUS": 3, "MANUAL": 2}),
            ("Monthly for devotional confession; more often if in mortal sin",
             {"STD": 2, "JES": 1}),
            ("Whenever conscious of serious sin; otherwise a few times a year",
             {"PROG": 2}),
            ("The Eastern tradition emphasizes spiritual direction over frequent confession",
             {"EASTSAC": 2, "PALAM": 1}),
        ],
        "axis_weights": {"PIETY": 2, "RIGOR": 1}
    },

    # ==================== CHRISTOLOGY ====================
    {
        "text": "How should we understand Christ's human knowledge during His earthly life?",
        "options": [
            ("Christ possessed the beatific vision from conception, giving comprehensive knowledge.",
             {"THOM": 3, "THOMP": 2, "CHALMAX": 3, "TRIDSAC": 1, "NEOSCH": 2}),
            ("Christ's human knowledge was genuinely limited; He learned and grew authentically.",
             {"KENOT": 4, "RESSCH": 2, "PROG": 2, "PERSMOR": 1}),
            ("Christ had infused knowledge sufficient for His mission, without unlimited knowledge.",
             {"SCOT": 2, "FRANC": 2, "SCOTMETA": 1, "STD": 2}),
            ("The mystery exceeds our categories; emphasize soteriological sufficiency.",
             {"RESS": 2, "NEOAUG": 2, "RESSCH": 2, "BENED": 1}),
        ],
        "axis_weights": {"JUST": 2}
    },
    {
        "text": "The relationship between Christ's divine and human wills:",
        "options": [
            ("Two distinct wills in perfect harmony; human will freely conforms to divine.",
             {"CHALMAX": 4, "THOM": 3, "THOMP": 2, "DOM": 1}),
            ("Divine will primary, human will its instrument; unity with dyothelitism.",
             {"RESSCH": 3, "NEOAUG": 2, "RESS": 2, "PALAM": 1}),
            ("Christ's human will genuinely struggled before conforming; soteriologically important.",
             {"KENOT": 4, "RESSCH": 2, "FRANC": 2, "PERSMOR": 1}),
            ("Maximus's synthesis: natural human will always good; gnomic willing absent.",
             {"PALAM": 3, "EASTECC": 2, "CHALMAX": 2, "EASTSAC": 1}),
        ],
        "axis_weights": {}
    },
    {
        "text": "The 'communication of idioms' (communicatio idiomatum) means:",
        "options": [
            ("Predicates of either nature attributed to the Person, carefully avoiding mixing natures.",
             {"CHALMAX": 4, "THOM": 2, "THOMP": 2, "NEOSCH": 1}),
            ("Profound exchange: 'God suffered,' 'this man is omnipotent' — Incarnation in speech.",
             {"RESSCH": 3, "NEOAUG": 2, "RESS": 2, "NEOPLAT": 1}),
            ("Shows divine condescension: God truly entered human weakness and suffering.",
             {"KENOT": 4, "FRANC": 2, "CARM": 1, "PERSMOR": 1}),
            ("Liturgically: 'O admirabile commercium' — God becomes man that man might become God.",
             {"BENED": 3, "EASTSAC": 2, "EUCHMYST": 2, "TRAD": 1}),
        ],
        "axis_weights": {"LIT": 1}
    },
    {
        "text": "Why did the Son of God become incarnate?",
        "options": [
            ("Primarily to redeem from sin; without Fall, no Incarnation.",
             {"THOM": 3, "AUG": 2, "AUGP": 1, "INFRA": 2, "THOMP": 1}),
            ("Christ would have come even without sin; Incarnation is creation's crown.",
             {"SCOT": 4, "FRANC": 3, "SCOTMETA": 2, "SUPRA": 2}),
            ("Both redemption and divinization: save from sin AND unite to God in theosis.",
             {"PALAM": 3, "EASTECC": 2, "RESSCH": 2, "NEOAUG": 2}),
            ("The question is speculative; focus on actual economy revealed.",
             {"STD": 2, "PAPMOD": 1, "RESS": 1, "BENED": 1}),
        ],
        "axis_weights": {"GRACE": 2, "JUST": 1}
    },
    {
        "text": "Christ's descent into hell (Sheol/Hades):",
        "options": [
            ("Triumphant proclamation and liberation of righteous — Harrowing of Hell.",
             {"TRAD": 3, "EASTSAC": 3, "BENED": 2, "CHALMAX": 1}),
            ("Christ truly experienced full human death, including darkness, before rising.",
             {"KENOT": 4, "RESSCH": 2, "NEOAUG": 1, "FRANC": 1}),
            ("Soteriological completion: saving work extends to those who died before.",
             {"THOM": 2, "STD": 2, "PAPMOD": 1, "INFRA": 1}),
            ("Primarily creedal affirmation; avoid excessive speculation.",
             {"STD": 2, "NEOSCH": 1, "MANUAL": 1}),
        ],
        "axis_weights": {"ESCH": 3}
    },

    # ==================== RELIGIOUS ORDERS ====================
    {
        "text": "Which approach to religious life most appeals to you?",
        "options": [
            ("Strict silence, manual labor, deep contemplation removed from world.",
             {"OCSO": 4, "CHART": 3, "OSBCAM": 2, "BENED": 1}),
            ("Active apostolate with community prayer; preaching, teaching, serving poor.",
             {"DOM": 2, "JES": 2, "CM": 2, "SDB": 2, "FRAN": 1}),
            ("Intellectual life and study as path to God, with pastoral work.",
             {"DOM": 3, "OSA": 3, "JES": 2, "OPRAEM": 1, "CSC": 2}),
            ("Contemplative prayer and mysticism, available for spiritual direction.",
             {"CARM": 4, "ORAT": 2, "CHART": 1}),
        ],
        "axis_weights": {"PIETY": 3}
    },
    {
        "text": "St. Augustine's spirituality emphasizes:",
        "options": [
            ("Interior journey: 'Return to yourself; truth dwells in the inner man.'",
             {"OSA": 4, "AUG": 3, "NEOAUG": 2, "CARM": 1}),
            ("Ordered love (ordo amoris): rightly ordering desires toward God.",
             {"AUG": 3, "AUGMOR": 3, "OSA": 2, "VIRTUE": 1}),
            ("Grace and predestination: absolute priority of God's initiative.",
             {"AUG": 3, "AUGP": 3, "BANEZ": 2, "JANS": 1}),
            ("Community life: 'One mind and one heart intent upon God.'",
             {"OSA": 4, "BENED": 2, "OPRAEM": 1}),
        ],
        "axis_weights": {"GRACE": 2, "PIETY": 2}
    },
    {
        "text": "The Cistercian/Trappist reform emphasizes:",
        "options": [
            ("Strict silence and solitude as essential for encountering God.",
             {"OCSO": 4, "CHART": 3, "OSBCAM": 2}),
            ("Manual labor as prayer: working with hands sanctifies.",
             {"OCSO": 4, "BENED": 2, "AGRAR": 1}),
            ("Simplicity and austerity: stripping away to find essential.",
             {"OCSO": 3, "CHART": 2, "FRAN": 2, "TRAD": 1}),
            ("Liturgical beauty in pure, unadorned Benedictine form.",
             {"OCSO": 3, "BENED": 3, "OPRAEM": 2, "TRAD": 1}),
        ],
        "axis_weights": {"PIETY": 4, "LIT": 1}
    },
    {
        "text": "St. Alphonsus Liguori and Redemptorists are known for:",
        "options": [
            ("Moral theology: equiprobabilism between rigorism and laxism.",
             {"CSSR": 4, "PROBAB": 2, "STD": 2, "CASUIST": 1}),
            ("Popular missions preaching 'abundant redemption' to abandoned.",
             {"CSSR": 4, "CM": 2, "CP": 1, "FRAN": 1}),
            ("Marian devotion: 'Glories of Mary' and confidence in intercession.",
             {"CSSR": 3, "OSM": 2, "MERC": 1, "TRAD": 1}),
            ("Practical pastoral approach: meeting people where they are.",
             {"CSSR": 3, "CM": 2, "SDB": 2, "PERSMOR": 1}),
        ],
        "axis_weights": {"RIGOR": -2}
    },
    {
        "text": "Don Bosco's Salesian spirituality centers on:",
        "options": [
            ("Preventive system: reason, religion, loving-kindness in education.",
             {"SDB": 4, "JES": 1, "PERSMOR": 1}),
            ("Joy and cheerfulness as essential witness, especially to youth.",
             {"SDB": 4, "FRAN": 2, "ORAT": 1}),
            ("Practical holiness in everyday life, accessible to all.",
             {"SDB": 3, "OPUS": 2, "STD": 2}),
            ("Devotion to Mary Help of Christians and the Eucharist.",
             {"SDB": 3, "TRAD": 1, "EUCHMYST": 1}),
        ],
        "axis_weights": {"PIETY": 2}
    },
    {
        "text": "St. Vincent de Paul and Vincentian spirituality emphasizes:",
        "options": [
            ("'The poor are our lords and masters' — radical service to marginalized.",
             {"CM": 4, "FRAN": 2, "WORKERCATH": 2, "SOCDEM": 1}),
            ("Formation of clergy: holy priests transform the Church.",
             {"CM": 3, "ORAT": 2, "OPRAEM": 1, "DOM": 1}),
            ("Simplicity, humility, meekness as core virtues.",
             {"CM": 4, "FRAN": 2, "SDB": 1}),
            ("Practical charity: 'Love is inventive to infinity.'",
             {"CM": 4, "PERSMOR": 1, "VIRTUE": 1}),
        ],
        "axis_weights": {}
    },
    {
        "text": "Passionist spirituality is characterized by:",
        "options": [
            ("Keeping alive 'memoria passionis' — memory of Christ's suffering.",
             {"CP": 4, "CARM": 1, "TRAD": 1}),
            ("Preaching missions focused on Cross and conversion.",
             {"CP": 4, "CSSR": 2, "DOM": 1}),
            ("Reparation for sin through contemplation of Passion.",
             {"CP": 3, "TRAD": 2, "EUCHMYST": 1}),
            ("Solidarity with suffering: finding Christ in those who suffer.",
             {"CP": 3, "CM": 2, "KENOT": 2, "WORKERCATH": 1}),
        ],
        "axis_weights": {"PIETY": 3}
    },
    {
        "text": "The Norbertines (Premonstratensians) combine:",
        "options": [
            ("Solemn liturgical life with active pastoral ministry.",
             {"OPRAEM": 4, "BENED": 2, "DOM": 1}),
            ("Canons regular: common life serving parishes and communities.",
             {"OPRAEM": 4, "OSA": 2, "ORAT": 1}),
            ("Marian devotion central to community identity.",
             {"OPRAEM": 3, "OSM": 2, "CSSR": 1}),
            ("Ancient liturgical traditions preserved with care.",
             {"OPRAEM": 3, "BENED": 3, "TRAD": 2, "ROTR": 1}),
        ],
        "axis_weights": {"LIT": 3}
    },
    {
        "text": "Which founder's charism most resonates with you?",
        "options": [
            ("St. Benedict: stability, prayer-work balance, liturgical life.",
             {"BENED": 4, "OCSO": 2, "OPRAEM": 1, "OSBCAM": 1}),
            ("St. Dominic: truth, preaching, study with contemplation.",
             {"DOM": 4, "THOM": 2, "OSA": 1}),
            ("St. Ignatius: discernment, flexibility, God in all things.",
             {"JES": 4, "MOL": 1, "ORAT": 1}),
            ("St. Francis: poverty, simplicity, joy, creation.",
             {"FRAN": 4, "FRANC": 2, "SDB": 1}),
            ("St. Vincent de Paul: practical charity, serving poor, forming priests.",
             {"CM": 4, "WORKERCATH": 1, "SOCDEM": 1}),
            ("Bl. Basil Moreau: education, hope in Cross, zeal for souls.",
             {"CSC": 4, "SDB": 1, "JES": 1}),
        ],
        "axis_weights": {"PIETY": 2}
    },
    {
        "text": "Servite devotion to Our Lady of Sorrows teaches:",
        "options": [
            ("Standing with Mary at Cross transforms suffering into redemption.",
             {"OSM": 4, "CP": 2, "CARM": 1}),
            ("Compassion (suffering-with) is central to Christian life.",
             {"OSM": 4, "CM": 2, "KENOT": 1, "PERSMOR": 1}),
            ("Marian devotion leads to deeper union with Christ.",
             {"OSM": 3, "CSSR": 2, "MERC": 2, "TRAD": 1}),
            ("Seven Sorrows are a school of discipleship.",
             {"OSM": 4, "CP": 2, "TRAD": 1}),
        ],
        "axis_weights": {"PIETY": 2}
    },

    # ==================== BALANCE QUESTIONS ====================
    {
        "text": "In moral theology, when facing a doubtful law:",
        "options": [
            ("Follow solidly probable opinion favoring liberty (Probabilism).",
             {"PROBAB": 4, "JES": 2, "MOL": 1, "CASUIST": 2}),
            ("Always follow safer opinion favoring law (Tutiorism).",
             {"TUTIOR": 4, "JANS": 2, "NEOSCH": 2, "AUGP": 1}),
            ("Follow more probable opinion after discernment (Probabiliorism).",
             {"THOM": 2, "DOM": 2, "THOMMOR": 2, "STD": 1}),
            ("Equiprobabilism: liberty only when opinions roughly equal.",
             {"STD": 3, "PAPMOD": 1, "MANUAL": 1}),
        ],
        "axis_weights": {"RIGOR": 4}
    },
    {
        "text": "The Carthusian vocation represents:",
        "options": [
            ("Highest Christian life: pure contemplation, hidden intercession.",
             {"CHART": 4, "CARM": 2, "BENED": 1, "TRAD": 1}),
            ("Valid but exceptional; active apostolate normative for most.",
             {"DOM": 2, "JES": 2, "STD": 2, "FRAN": 1}),
            ("Important witness, but Church needs engaged presence.",
             {"PROG": 2, "LIBCATH": 1, "SOCDEM": 1}),
            ("Desert tradition: 'flee, be silent, pray' as perennial wisdom.",
             {"CHART": 3, "EASTECC": 2, "PALAM": 1, "ORAT": 1}),
        ],
        "axis_weights": {"PIETY": 4}
    },
    {
        "text": "Catholic rural/agrarian life should be valued as:",
        "options": [
            ("Land-based life forms virtue uniquely; prefer smallholdings.",
             {"AGRAR": 4, "DISTRIBUT": 3, "TRADNAT": 2, "CHART": 1}),
            ("Has value but industrialization not inherently evil.",
             {"STD": 2, "SOCDEM": 2, "PAPMOD": 1}),
            ("Romantic nostalgia; address actual worker conditions.",
             {"WORKERCATH": 2, "PROG": 2, "LIBCATH": 1}),
            ("Rural parishes preserve faith; special concern for farmers.",
             {"TRAD": 2, "AGRAR": 2, "BENED": 2, "CORPCATH": 1}),
        ],
        "axis_weights": {}
    },
    {
        "text": "Scripture's literal and spiritual senses:",
        "options": [
            ("Literal foundational; spiritual senses controlled by it.",
             {"THOM": 3, "DOM": 2, "THOMMETA": 1, "STD": 1}),
            ("Spiritual senses reveal deepest meaning; Fathers normative.",
             {"RESS": 3, "NEOAUG": 3, "NEOPLAT": 2, "BENED": 2, "ORAT": 1}),
            ("Historical-critical establishes literal; spiritual is devotional.",
             {"PROG": 2, "LIBCATH": 2, "JES": 1}),
            ("All four senses work together; Scripture inexhaustibly rich.",
             {"BENED": 2, "STD": 2, "PAPMOD": 1, "EASTECC": 1}),
        ],
        "axis_weights": {"SCRIPT": 3}
    },
    {
        "text": "Catholic approaches to nationalism:",
        "options": [
            ("Nations are natural communities; faith should inform identity.",
             {"TRADNAT": 4, "INTEG": 2, "INTEGHARD": 1, "CORPCATH": 1}),
            ("Church transcends nations; nationalism contradicts universality.",
             {"CATHUNIV": 4, "LIBCATH": 2, "PROG": 1, "SOCDEM": 1}),
            ("Legitimate patriotism distinct from nationalism.",
             {"STD": 3, "PAPMOD": 2, "THOMMOR": 1}),
            ("Subsidiarity supports sovereignty; nations serve persons.",
             {"DISTRIBUT": 2, "INTEGSOFT": 2, "LIBERTAR": 1, "TRADNAT": 1}),
        ],
        "axis_weights": {}
    },


    # ==================== GALLICANISM & CHURCH-STATE ====================
    {
        "text": "What is your position on Gallican liberties and national church autonomy?",
        "options": [
            ("Nations may legitimately negotiate appointment rights and synodal authority with Rome, provided they don't strongarm the Holy See.",
             {"PAPMOD": 4, "STD": 3, "INTEGSOFT": 3, "GALL": 2, "DEVPROG": 2}),
            ("Would make sense with stable Catholic monarchies, but impractical in modern liberal democracies.",
             {"TRADNAT": 4, "INTEG": 3, "TRAD": 3, "GALL": 2, "CORPCATH": 2}),
            ("A dangerous affront to papal authority. The Pope's universal jurisdiction must not be compromised.",
             {"ULTRA": 6, "INTEG": 3, "PAPMOD": -2, "GALL": -5, "CONCIL": -4}),
            ("Risks enabling nationalists to co-opt the Church and undermine her transnational mission.",
             {"CATHUNIV": 5, "LIBCATH": 4, "PROG": 3, "SOCDEM": 2, "TRADNAT": -4}),
        ],
        "axis_weights": {"PAPAL": 3}
    },

    # ==================== IMMIGRATION ====================
    {
        "text": "What is your view of the Church hierarchy's approach to immigration?",
        "options": [
            ("A generational matter. Once older bishops retire, I'm optimistic about better balance.",
             {"PROG": 3, "STD": 2, "SYNOD": 3, "DEVPROG": 2}),
            ("Some nationalist governments have acted excessively, but prudential judgment on borders isn't sinful. National consciousness is legitimate.",
             {"TRADNAT": 5, "INTEGSOFT": 4, "DISTRIBUT": 3, "STD": 2, "CATHUNIV": -3}),
            ("A welcome prophetic stance against the pagan idols of nationalism and kinism.",
             {"CATHUNIV": 6, "LIBCATH": 5, "PROG": 4, "SOCDEM": 3, "TRADNAT": -5}),
            ("Balanced - the clergy can be naive about practical realities, but their intentions are good.",
             {"STD": 4, "PAPMOD": 3, "ROTR": 2, "TRADUM": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== LITURGICAL REFORM ====================
    {
        "text": "What are your thoughts on reforming the Novus Ordo toward a vernacular TLM (like the Orthodox Divine Liturgy of St. Gregory)?",
        "options": [
            ("A worthy compromise honoring tradition without the abuses of the current Pauline Mass.",
             {"ROTR": 5, "TRAD": 3, "EASTECC": 3, "BENED": 3, "ORDINAR": 4, "EASTLIT": 3}),
            ("Good idea if executed carefully. Sacrosanctum Concilium never intended liturgical chaos.",
             {"ROTR": 4, "STD": 3, "PAPMOD": 2, "COMMUN": 2, "TRADUM": 3}),
            ("The Mass must be in Latin. Vatican II's liturgical reforms must be entirely undone.",
             {"SSPX": 6, "SEDE": 5, "TRAD": 4, "ANTIMOD": 4, "PROG": -5, "LIBCATH": -4}),
            ("The Ordinariate's Divine Worship liturgy is an excellent model of vernacular solemnity.",
             {"ORDINAR": 6, "EASTECC": 3, "ROTR": 4, "BENED": 3, "EASTLIT": 3}),
            ("Reform of the Reform: end abuses, restore sacred music, ad orientem, keep NO structure.",
             {"ROTR": 6, "STD": 3, "PAPMOD": 3, "TRADUM": 3, "COMMUN": 2}),
            ("No - the old liturgy was an ossified relic. The reform liberated us.",
             {"PROG": 6, "LIBCATH": 5, "TRAD": -5, "ROTR": -3, "SSPX": -6}),
        ],
        "axis_weights": {"LIT": 5}
    },

    # ==================== ORTHODOX REUNION ====================
    {
        "text": "How should the Catholic Church approach reunion with the Eastern Orthodox?",
        "options": [
            ("Return to Rome under papal authority as Vatican I defined. No compromises on primacy.",
             {"ULTRA": 5, "INTEG": 3, "NEOSCH": 3, "ANTIMOD": 2, "ORTHOPH": -4}),
            ("A 'Sister Churches' model with restored communion but preserved Eastern autonomy.",
             {"EASTECC": 5, "EASTSAC": 4, "PALAM": 3, "SYNOD": 3, "ORTHOPH": 5, "EASTLIT": 3, "ULTRA": -3}),
            ("Focus on resolving theological issues (Filioque, essence-energies) before structural questions.",
             {"THOM": 3, "RESS": 3, "PALAM": 3, "DOM": 2, "COMMUN": 2, "ORTHOPH": 2}),
            ("Ecumenism has gone too far. Maintain clear boundaries until they accept all Catholic dogma.",
             {"TRAD": 4, "SSPX": 4, "NEOSCH": 3, "ANTIMOD": 3, "PROG": -3}),
            ("Practical cooperation first; doctrinal unity will follow organically.",
             {"PROG": 4, "LIBCATH": 3, "CM": 2, "SYNOD": 2, "TRAD": -2}),
        ],
        "axis_weights": {"PAPAL": 2}
    },

    # ==================== DIGNITATIS HUMANAE ====================
    {
        "text": "How do you understand Vatican II's teaching on religious liberty (Dignitatis Humanae)?",
        "options": [
            ("Legitimate development - the state shouldn't coerce conscience, though truth remains objective.",
             {"PAPMOD": 4, "STD": 4, "RESS": 3, "DEVPROG": 4, "COMMUN": 3}),
            ("A prudential adaptation for pluralist societies, not reversal of prior teaching.",
             {"INTEGSOFT": 5, "ROTR": 3, "STD": 3, "TRADUM": 3}),
            ("A rupture with Tradition. Quanta Cura condemned exactly what DH teaches.",
             {"SSPX": 6, "TRAD": 5, "INTEGHARD": 5, "SEDE": 4, "ANTIMOD": 5, "LIBCATH": -6}),
            ("The Church finally embraced freedom of conscience as foundational to human dignity.",
             {"LIBCATH": 6, "PROG": 5, "PERSMOR": 4, "SYNOD": 2, "INTEG": -5}),
            ("Ambiguously worded; needs authoritative clarification to reconcile with prior magisterium.",
             {"TRAD": 4, "ROTR": 3, "PAPMIN": 3, "TRADUM": 3, "ANTIMOD": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== CELIBACY ====================
    {
        "text": "What is your view on mandatory clerical celibacy in the Latin Rite?",
        "options": [
            ("Precious discipline that should never be relaxed. Frees priests for total dedication.",
             {"TRAD": 4, "OPUS": 4, "INTEG": 3, "NEOSCH": 3, "CARM": 2, "CHART": 2}),
            ("Valuable but could permit married priests in mission territories, as Eastern Catholics do.",
             {"EASTECC": 4, "PAPMOD": 3, "STD": 3, "SYNOD": 3, "ORDINAR": 3, "ORTHOPH": 2}),
            ("Should be entirely optional. Many good men are lost; the Apostles were married.",
             {"PROG": 5, "LIBCATH": 5, "SYNOD": 3, "TRAD": -4, "OPUS": -3}),
            ("Essential for eschatological witness. It images heavenly life.",
             {"CARM": 4, "CHART": 4, "BENED": 3, "OCSO": 4, "TRAD": 3, "CP": 2}),
            ("The Ordinariate exception shows flexibility is possible. Expand it carefully.",
             {"ORDINAR": 5, "PAPMOD": 3, "DEVPROG": 2, "STD": 2}),
        ],
        "axis_weights": {"RIGOR": 2, "PIETY": 1}
    },

    # ==================== TRADITIONIS CUSTODES ====================
    {
        "text": "How do you view Pope Francis's restrictions on the Traditional Latin Mass?",
        "options": [
            ("Necessary to prevent the TLM from becoming a flag for rejecting Vatican II.",
             {"PROG": 4, "LIBCATH": 3, "SYNOD": 2, "ULTRA": 2, "TRAD": -5, "SSPX": -5}),
            ("Pastorally devastating. Summorum Pontificum was working. Benedict XVI was right.",
             {"ROTR": 5, "TRAD": 5, "BENED": 3, "TRADUM": 4, "COMMUN": 2, "PROG": -3}),
            ("An unjust suppression. I attend TLM regardless of canonical regularity.",
             {"SSPX": 6, "TRAD": 5, "SEDE": 3, "ANTIMOD": 3, "ULTRA": -4, "PAPMOD": -3}),
            ("The Pope has authority to regulate liturgy. I obey even if I preferred the old policy.",
             {"ULTRA": 4, "STD": 4, "PAPMOD": 4, "TRADUM": 5, "SSPX": -4}),
            ("Understandable concern but heavy-handed. Dialogue would have been better.",
             {"STD": 3, "ROTR": 3, "PAPMOD": 2, "ORAT": 2, "TRADUM": 3, "DEVPROG": 2}),
        ],
        "axis_weights": {"LIT": 4, "PAPAL": 2}
    },

    # ==================== NON-CATHOLIC SOTERIOLOGY ====================
    {
        "text": "Which non-Catholic view of soteriology do you find most compatible with Catholic faith?",
        "options": [
            ("Lutheran - if 'faith alone' is properly understood and sacramental realism affirmed, we're close.",
             {"LUTHCAT": 6, "ECUMON": 5, "AUG": 3, "NEOAUG": 2, "DEVPROG": 2, "TRAD": -3}),
            ("Eastern Orthodox - patristic synthesis preserved. Theosis, synergy, mystery are deeply Catholic.",
             {"ORTHOPH": 6, "PALAM": 5, "EASTECC": 4, "EASTSAC": 3, "RESS": 2, "NEOAUG": 2}),
            ("None. Extra Ecclesiam nulla salus. Protestant communities lack valid sacraments.",
             {"TRAD": 5, "SSPX": 5, "NEOSCH": 4, "ANTIMOD": 3, "ECUMON": -5, "LUTHCAT": -5}),
            ("Reformed/Calvinist - they take grace seriously. Augustinian roots are shared.",
             {"AUGP": 4, "JANS": 3, "BANEZ": 2, "ECUMON": 2, "MOL": -3}),
            ("Anglican - via media, sacramental emphasis, liturgical beauty. The Ordinariate shows convergence.",
             {"ORDINAR": 6, "ROTR": 2, "BENED": 2, "DEVPROG": 2}),
        ],
        "axis_weights": {"GRACE": 2, "JUST": 2}
    },

    # ==================== LUTHERAN CONVERGENCE ====================
    {
        "text": "If Lutheran 'Sacramental Union' recognized ontological change, and 'faith alone' was understood as Benedict XVI saw it, would these impede reunion?",
        "options": [
            ("No - properly understood, these need not be impediments. JDDJ showed real convergence.",
             {"LUTHCAT": 6, "ECUMON": 5, "DEVPROG": 4, "COMMUN": 3, "PAPMOD": 2, "TRAD": -4}),
            ("Possibly not, but we'd still need agreement on papacy, Marian dogmas, purgatory.",
             {"PAPMOD": 4, "STD": 4, "THOM": 3, "ECUMON": 2, "DEVPROG": 2}),
            ("Yes - Lutheran theology is fundamentally incompatible. Trent's condemnations stand.",
             {"TRAD": 5, "NEOSCH": 5, "ANTIMOD": 4, "SSPX": 4, "LUTHCAT": -6, "ECUMON": -5}),
            ("This hypothetical concedes too much. Lutheranism doesn't actually affirm these things.",
             {"THOM": 3, "DOM": 2, "STD": 2, "NEOSCH": 2}),
        ],
        "axis_weights": {"JUST": 3}
    },

    # ==================== HERMENEUTIC OF CONTINUITY ====================
    {
        "text": "What is your opinion on the 'hermeneutic of continuity' proposed by Benedict XVI?",
        "options": [
            ("Essential and correct. Vatican II must be read in continuity with all prior councils.",
             {"COMMUN": 5, "ROTR": 5, "DEVPROG": 4, "TRADUM": 4, "STD": 3, "BENED": 3}),
            ("Noble attempt, but the texts themselves contain ambiguities enabling rupturist readings.",
             {"TRAD": 4, "ROTR": 3, "ANTIMOD": 3, "TRADUM": 3, "PAPMIN": 2}),
            ("Continuity is a fiction. Vatican II was a new beginning, and that's good.",
             {"PROG": 5, "LIBCATH": 5, "SYNOD": 2, "COMMUN": -3, "TRAD": -5}),
            ("Partially valid but insufficient. Some texts genuinely conflict with prior magisterium.",
             {"SSPX": 5, "SEDE": 4, "TRAD": 4, "ANTIMOD": 4, "COMMUN": -2}),
            ("A pastoral strategy more than theological argument. Useful for maintaining unity.",
             {"PAPMOD": 3, "STD": 3, "JES": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== DIGITAL EVANGELIZATION ====================
    {
        "text": "How should Catholics approach lay apostolates and evangelization in the digital space?",
        "options": [
            ("Embrace fully. Social media is the new Areopagus. Memes and podcasts reach millions.",
             {"SDB": 4, "JES": 3, "PROG": 3, "OPUS": 3, "STD": 2, "CHART": -2}),
            ("Cautiously useful, but nothing replaces parish life and sacramental encounter.",
             {"STD": 4, "BENED": 3, "PAPMOD": 2, "ORAT": 3, "CM": 2}),
            ("Dangerous - breeds pride and controversy-seeking. Focus on real community.",
             {"CHART": 4, "OCSO": 3, "BENED": 2, "CARM": 2, "TRAD": 2}),
            ("Essential for reaching the young, but must be done with theological competence.",
             {"DOM": 4, "JES": 3, "COMMUN": 2, "ORAT": 2, "SDB": 3}),
            ("Lay apostolates online have revived tradition more than the hierarchy. Keep going.",
             {"TRAD": 4, "ROTR": 3, "TRADUM": 3, "ANTIMOD": 2, "SYNOD": -2}),
        ],
        "axis_weights": {}
    },

    # ==================== PROTESTANT JUSTIFICATION ====================
    {
        "text": "'Reformed and Lutheran views of justification, despite differences, are mostly compatible with some Catholic schools.' Your response:",
        "options": [
            ("Agree - Augustinian and Bañezian positions share significant common ground. JDDJ was right.",
             {"LUTHCAT": 6, "ECUMON": 5, "AUG": 3, "BANEZ": 2, "AUGP": 2, "NEOSCH": -4}),
            ("Partially - overlap on grace's priority exists, but merit and sacraments differ substantially.",
             {"THOM": 3, "STD": 3, "PAPMOD": 3, "DEVPROG": 2, "AUG": 2}),
            ("Disagree - Protestant soteriology is forensic and extrinsic. Catholic justification is real transformation.",
             {"THOM": 4, "TRIDSAC": 4, "NEOSCH": 4, "DOM": 3, "LUTHCAT": -4}),
            ("Strongly disagree - Trent definitively condemned sola fide as Protestants teach it.",
             {"TRAD": 5, "SSPX": 5, "NEOSCH": 5, "ANTIMOD": 4, "LUTHCAT": -6, "ECUMON": -5}),
        ],
        "axis_weights": {"JUST": 4, "GRACE": 3}
    },

    # ==================== HISTORICAL MONERGISM ====================
    {
        "text": "'Historical Catholic soteriology (Augustine, Prosper, Isidore, Council of Orange) was essentially monergistic.' Your assessment:",
        "options": [
            ("Correct. The Fathers and Orange taught even the beginning of faith is God's gift.",
             {"AUG": 5, "AUGP": 5, "NEOAUG": 4, "BANEZ": 4, "ECUMON": 3, "JANS": 3, "MOL": -4}),
            ("Partially true, but 'monergism' is anachronistic. Fathers affirmed grace's priority AND cooperation.",
             {"THOM": 4, "STD": 3, "RESS": 3, "DEVPROG": 3, "NEOAUG": 2}),
            ("Overstated. Orange affirmed free will's role. Catholic teaching has always been synergistic.",
             {"MOL": 5, "JES": 3, "CONG": 3, "SCOT": 2, "AUGP": -4, "BANEZ": -3}),
            ("Augustinian tradition was later balanced by Aquinas and Jesuits. Don't overcorrect.",
             {"THOM": 4, "MOL": 3, "JES": 2, "DOM": 2, "STD": 2}),
        ],
        "axis_weights": {"GRACE": 5}
    },

    # ==================== FILIOQUE ====================
    {
        "text": "'We can omit the Filioque from the Creed for reunion with the Orthodox.' Your view:",
        "options": [
            ("Yes - it was a Western addition. The original Creed didn't have it. Remove it.",
             {"ORTHOPH": 6, "EASTECC": 5, "EASTSAC": 4, "PALAM": 4, "SYNOD": 2, "ULTRA": -4}),
            ("Possibly in Eastern liturgies, but the theology is true. A pastoral accommodation.",
             {"PAPMOD": 4, "EASTECC": 4, "STD": 3, "DEVPROG": 3, "COMMUN": 2, "ORTHOPH": 2}),
            ("No - Filioque is dogmatically defined and expresses important Trinitarian truth.",
             {"THOM": 4, "TRAD": 4, "NEOSCH": 4, "ULTRA": 3, "ANTIMOD": 3, "ORTHOPH": -4}),
            ("Florence's 'through the Son' shows reconciliation is possible without abandoning Western theology.",
             {"THOM": 3, "PAPMOD": 3, "RESS": 3, "DEVPROG": 3, "COMMUN": 3, "ORTHOPH": 2}),
            ("The controversy shows Orthodox are schismatics rejecting legitimate development.",
             {"ULTRA": 5, "ANTIMOD": 3, "NEOSCH": 3, "TRAD": 3, "ORTHOPH": -6}),
        ],
        "axis_weights": {"PAPAL": 2}
    },

    # ==================== WOMEN'S ROLES ====================
    {
        "text": "What expanded roles, if any, should women have in the Church?",
        "options": [
            ("Female deacons should be restored; women should lead wherever ordination isn't required.",
             {"PROG": 5, "SYNOD": 4, "LIBCATH": 5, "TRAD": -5, "INTEG": -4}),
            ("Women already have vital roles. Recognize existing contributions, don't invent offices.",
             {"STD": 4, "PAPMOD": 3, "OPUS": 3, "TRAD": 2}),
            ("The push reflects secular feminism infiltrating the Church. Resist it.",
             {"TRAD": 5, "INTEG": 5, "SSPX": 4, "ANTIMOD": 4, "PROG": -5}),
            ("Study historical evidence for deaconesses carefully; proceed with tradition.",
             {"RESS": 3, "EASTECC": 3, "PAPMOD": 3, "DEVPROG": 2, "COMMUN": 2}),
            ("Religious sisters already exercise profound spiritual authority. This is the feminine genius.",
             {"CARM": 4, "BENED": 3, "CM": 2, "FRAN": 2, "OSM": 2, "OPUS": 2}),
        ],
        "axis_weights": {"RIGOR": 2}
    },

    # ==================== ECONOMICS ====================
    {
        "text": "Which economic arrangement best reflects Catholic Social Teaching?",
        "options": [
            ("Distributism - widespread ownership, guilds, cooperatives. Chesterton and Belloc were right.",
             {"DISTRIBUT": 6, "AGRAR": 4, "CORPCATH": 3, "TRADNAT": 2, "LIBERTAR": -3}),
            ("Regulated markets with welfare state and worker protections. European social model.",
             {"SOCDEM": 5, "WORKERCATH": 4, "CM": 2, "LIBCATH": 2, "LIBERTAR": -4}),
            ("Free markets with private charity. Government creates dependency.",
             {"LIBERTAR": 6, "OPUS": 2, "SOCDEM": -5, "WORKERCATH": -3}),
            ("Corporatism - organized vocational groups. Quadragesimo Anno's vision.",
             {"CORPCATH": 6, "INTEG": 3, "DISTRIBUT": 3, "TRADNAT": 2}),
            ("CST provides principles, not a system. Context determines application.",
             {"STD": 4, "PAPMOD": 3, "JES": 2, "DEVPROG": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== JEWISH RELATIONS ====================
    {
        "text": "How should the Church understand her relationship with Judaism after Nostra Aetate?",
        "options": [
            ("The Old Covenant remains valid. Jews have a unique path not requiring explicit Christian faith.",
             {"PROG": 4, "LIBCATH": 4, "RESS": 2, "TRAD": -5, "NEOSCH": -4}),
            ("Nostra Aetate condemned antisemitism but didn't change the necessity of Christ for salvation.",
             {"STD": 4, "PAPMOD": 4, "THOM": 3, "DEVPROG": 2, "TRAD": 2}),
            ("The Church has overcorrected. Supersessionism is traditional and shouldn't be abandoned.",
             {"TRAD": 5, "SSPX": 4, "NEOSCH": 4, "ANTIMOD": 3, "PROG": -4}),
            ("Complex - honor Jewish roots, condemn antisemitism, maintain missionary mandate to all.",
             {"RESS": 4, "NEOAUG": 3, "BENED": 3, "COMMUN": 3, "STD": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== MARIAN APPARITIONS ====================
    {
        "text": "What is your view on Marian apparitions (Fatima, Lourdes, etc.)?",
        "options": [
            ("Essential to Catholic piety. The Fatima consecration should be taken seriously.",
             {"TRAD": 4, "CSSR": 3, "OSM": 3, "MERC": 2, "ANTIMOD": 2}),
            ("Approved apparitions are credible but private revelation is never obligatory.",
             {"STD": 4, "PAPMOD": 3, "THOM": 2, "DEVPROG": 2}),
            ("Often verge on superstition. Focus on Scripture and Sacraments.",
             {"PROG": 3, "LIBCATH": 3, "DOM": 2, "TRAD": -2, "CSSR": -2}),
            ("Some are solid (Fatima, Lourdes) but others (Medjugorje) are likely fraudulent.",
             {"TRAD": 3, "STD": 3, "ROTR": 2, "PAPMOD": 2}),
        ],
        "axis_weights": {"PIETY": 2}
    },

    # ==================== EMPTY HELL ====================
    {
        "text": "What is your view on the possibility of an 'empty hell' (Balthasar's hope)?",
        "options": [
            ("Permissible - we may dare to hope all are saved. God's mercy is infinite.",
             {"COMMUN": 5, "PROG": 4, "LIBCATH": 4, "TRAD": -4, "AUGP": -4, "JANS": -4}),
            ("Heretical or temerarious. Scripture and Tradition attest many are damned.",
             {"AUGP": 5, "JANS": 4, "TRAD": 4, "NEOSCH": 3, "ANTIMOD": 3, "COMMUN": -4}),
            ("We can hope for individuals but the Church teaches hell is populated.",
             {"STD": 4, "THOM": 3, "PAPMOD": 2, "AUG": 2}),
            ("Speculative. Focus on your own salvation, not universal questions.",
             {"CARM": 3, "CHART": 3, "STD": 2, "BENED": 2}),
        ],
        "axis_weights": {"ESCH": 4, "RIGOR": 3}
    },

    # ==================== AMORIS LAETITIA ====================
    {
        "text": "What is your view on Amoris Laetitia and communion for the divorced and remarried?",
        "options": [
            ("A development allowing pastoral discernment in complex situations.",
             {"PROG": 5, "SYNOD": 4, "PERSMOR": 3, "LIBCATH": 3, "TRAD": -5, "NEOSCH": -4}),
            ("Ambiguous document misused by progressives. The dubia remain unanswered.",
             {"TRAD": 5, "ROTR": 3, "TRADUM": 3, "NEOSCH": 3, "ANTIMOD": 2}),
            ("Heretical. Contradicts Familiaris Consortio and perennial teaching.",
             {"SSPX": 5, "SEDE": 4, "TRAD": 4, "ANTIMOD": 4, "PROG": -5}),
            ("Pastoral accompaniment is good but doesn't change the discipline.",
             {"STD": 4, "PAPMOD": 3, "MANUAL": 2, "THOMMOR": 2}),
        ],
        "axis_weights": {"RIGOR": 4}
    },

    # ==================== VATICAN II ASSESSMENT ====================
    {
        "text": "How do you assess the Second Vatican Council overall?",
        "options": [
            ("The greatest council - opened the Church to the modern world.",
             {"PROG": 6, "LIBCATH": 5, "SYNOD": 3, "TRAD": -5, "SSPX": -6, "ANTIMOD": -5}),
            ("Legitimate council often misinterpreted. Hermeneutic of continuity needed.",
             {"COMMUN": 5, "ROTR": 5, "TRADUM": 4, "DEVPROG": 4, "STD": 3}),
            ("Pastoral, not dogmatic. Prudential judgments can be questioned.",
             {"TRAD": 4, "ROTR": 3, "PAPMIN": 3, "TRADUM": 3}),
            ("A catastrophe. The texts contain errors or dangerous ambiguities.",
             {"SSPX": 6, "ANTIMOD": 5, "SEDE": 4, "TRAD": 4, "COMMUN": -3, "PROG": -5}),
            ("Invalid or doubtfully valid. The Church has been in eclipse since.",
             {"SEDE": 6, "SEDEPRIV": 5, "SSPX": 3, "STD": -5, "PAPMOD": -5}),
        ],
        "axis_weights": {"LIT": 2}
    },

    # ==================== HUMANAE VITAE ====================
    {
        "text": "What is your position on Humanae Vitae's teaching on contraception?",
        "options": [
            ("Prophetic and absolutely binding. NFP is the only moral option.",
             {"TRAD": 5, "NEOSCH": 5, "OPUS": 4, "THOMMOR": 4, "INTEG": 3}),
            ("True but pastoral sensitivity needed. Distinguish grave matter from mortal sin.",
             {"STD": 4, "PAPMOD": 3, "PERSMOR": 2}),
            ("The principle is right but application involves prudential judgment.",
             {"PERSMOR": 4, "CASUIST": 3, "PROG": 2, "NEOSCH": -3}),
            ("Should be reconsidered. Sensus fidelium has rejected it.",
             {"PROG": 4, "LIBCATH": 5, "SYNOD": 2, "TRAD": -6, "NEOSCH": -5}),
        ],
        "axis_weights": {"RIGOR": 5}
    },

    # ==================== CHURCH & DEMOCRACY ====================
    {
        "text": "How should the Church relate to secular liberal democracy?",
        "options": [
            ("Reject it - Christendom should be restored. Christ must reign socially.",
             {"INTEGHARD": 6, "INTEG": 5, "TRADNAT": 4, "TRAD": 3, "LIBCATH": -5}),
            ("Accept pragmatically but work for culture's conversion over time.",
             {"INTEGSOFT": 5, "ROTR": 3, "STD": 3, "DEVPROG": 2}),
            ("Liberal democracy, rightly understood, is compatible with Catholicism.",
             {"LIBCATH": 5, "PAPMOD": 3, "STD": 3, "DEVPROG": 3, "INTEG": -4}),
            ("Fine but must be limited by natural law and subsidiarity.",
             {"DISTRIBUT": 4, "STD": 3, "THOMMOR": 3, "INTEGSOFT": 2}),
            ("Church should focus on souls, not political arrangements.",
             {"CARM": 3, "CHART": 3, "STD": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== SIGNATURE: FUNDAMENTAL ORIENTATION ====================
    {
        "text": "Which statement best captures your fundamental theological orientation?",
        "options": [
            ("'Grace does not destroy nature but perfects it.' The Thomistic synthesis is perennially valid.",
             {"THOM": 6, "DOM": 4, "THOMMETA": 4, "THOMMOR": 3}),
            ("'Our hearts are restless until they rest in Thee.' Augustine's interiority and grace theology are primary.",
             {"AUG": 6, "OSA": 4, "NEOAUG": 4, "AUGMOR": 3}),
            ("'Finding God in all things.' Ignatian discernment and active engagement with the world.",
             {"JES": 6, "MOL": 3, "CONG": 2}),
            ("'Pray and work.' The Benedictine balance of liturgy, labor, and stability.",
             {"BENED": 6, "OCSO": 4, "OPRAEM": 3, "CHART": 2}),
            ("'Lady Poverty.' Franciscan simplicity, creation spirituality, and joyful service.",
             {"FRAN": 6, "FRANC": 4, "SDB": 2}),
            ("Ressourcement - return to Fathers and Scripture to renew the Church.",
             {"RESS": 6, "NEOAUG": 4, "COMMUN": 4, "BENED": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== SIGNATURE: LITURGY ====================
    {
        "text": "On liturgical matters, you identify most closely with:",
        "options": [
            ("The Traditional Latin Mass is the Mass of the Ages. The Novus Ordo is at best a compromise.",
             {"TRAD": 6, "SSPX": 4, "ROTR": 2, "ANTIMOD": 3}),
            ("Novus Ordo celebrated reverently, ad orientem, with chant. Reform of the Reform.",
             {"ROTR": 6, "TRADUM": 4, "STD": 2, "COMMUN": 2}),
            ("Eastern Divine Liturgy - Byzantine, Maronite, or other Eastern Catholic traditions.",
             {"EASTLIT": 6, "EASTECC": 5, "EASTSAC": 4, "ORTHOPH": 3}),
            ("The Ordinariate's Divine Worship - Anglican patrimony in full communion.",
             {"ORDINAR": 6, "ROTR": 2, "BENED": 2}),
            ("The reformed liturgy as commonly celebrated. The Mass is the Mass.",
             {"STD": 5, "PROG": 3, "LIBCATH": 2, "TRAD": -3}),
            ("Liturgy should be creative, inculturated, and community-centered.",
             {"PROG": 6, "LIBCATH": 4, "TRAD": -5, "ROTR": -4}),
        ],
        "axis_weights": {"LIT": 6}
    },

    # ==================== SIGNATURE: PAPAL AUTHORITY ====================
    {
        "text": "Your view of papal authority is closest to:",
        "options": [
            ("Maximal - supreme, immediate, ordinary jurisdiction everywhere. Roma locuta.",
             {"ULTRA": 6, "INTEG": 3, "PAPMOD": -2, "GALL": -5, "CONCIL": -5}),
            ("Vatican I is true but narrowly applied. Collegiality balances primacy.",
             {"PAPMOD": 6, "STD": 3, "COMMUN": 2, "DEVPROG": 2}),
            ("Papal minimalism - infallibility is real but rare. Most teaching is reformable.",
             {"PAPMIN": 6, "GALL": 3, "CONCIL": 2, "ULTRA": -4}),
            ("The current occupant may not be a true pope. Discernment is required.",
             {"SEDE": 6, "SEDEPRIV": 5, "SSPX": 3, "ULTRA": -6, "PAPMOD": -5}),
            ("Synodality should be strengthened. Pope is first among equals.",
             {"SYNOD": 5, "EASTECC": 4, "CONCIL": 3, "PROG": 2, "ULTRA": -5}),
        ],
        "axis_weights": {"PAPAL": 6}
    },

    # ==================== SIGNATURE: GRACE (BANEZ vs MOLINA) ====================
    {
        "text": "In the De Auxiliis controversy between Bañezians and Molinists, you side with:",
        "options": [
            ("Bañez - physical premotion, intrinsically efficacious grace, predestination ante praevisa merita.",
             {"BANEZ": 6, "AUGP": 4, "DOM": 3, "AUG": 3, "THOMP": 3, "MOL": -5, "JES": -3}),
            ("Molina - middle knowledge, extrinsically efficacious grace, libertarian freedom preserved.",
             {"MOL": 6, "JES": 4, "CONG": 3, "SCOT": 2, "BANEZ": -5, "AUGP": -3}),
            ("Congruism - a mediating position. Grace is suited to circumstances God foresees.",
             {"CONG": 6, "MOL": 3, "JES": 2, "STD": 2}),
            ("The Church left it open. Both are permissible opinions within Catholic bounds.",
             {"STD": 4, "PAPMOD": 3, "THOM": 2, "DEVPROG": 2}),
            ("I lean Augustinian/Bañezian but wouldn't call Molinism heresy.",
             {"AUG": 4, "BANEZ": 3, "THOM": 3, "DOM": 2, "STD": 2}),
        ],
        "axis_weights": {"GRACE": 6}
    },

    # ==================== SIGNATURE: JANSENISM ====================
    {
        "text": "How do you assess the Jansenist movement?",
        "options": [
            ("Authentic Augustinianism unjustly condemned due to Jesuit political maneuvering.",
             {"JANS": 6, "AUGP": 4, "TRAD": 2, "JES": -5, "MOL": -4}),
            ("Contained genuine insights about grace but went too far into rigorism and near-Calvinism.",
             {"AUG": 3, "AUGP": 2, "THOM": 3, "STD": 2}),
            ("Rightly condemned. Its rigorism harmed souls and its ecclesiology was schismatic.",
             {"JES": 4, "MOL": 3, "STD": 3, "PAPMOD": 2, "JANS": -5}),
            ("A complex phenomenon. Some Jansenists were holy; the label was applied too broadly.",
             {"RESS": 3, "DEVPROG": 2, "STD": 2, "NEOAUG": 2}),
        ],
        "axis_weights": {"GRACE": 4, "RIGOR": 3}
    },

    # ==================== SIGNATURE: INFRA/SUPRALAPSARIANISM ====================
    {
        "text": "On the order of divine decrees (predestination), you hold:",
        "options": [
            ("Infralapsarianism - God's decree of election logically follows the decree to permit the Fall.",
             {"INFRA": 6, "THOM": 3, "AUG": 2, "STD": 2}),
            ("Supralapsarianism - God's decree of election logically precedes the Fall. Stronger sovereignty.",
             {"SUPRA": 6, "AUGP": 3, "BANEZ": 2, "SCOT": 2}),
            ("These distinctions are overly speculative. Focus on pastoral realities.",
             {"STD": 3, "PERSMOR": 2, "PROG": 2}),
            ("I affirm predestination but don't commit to the order of decrees.",
             {"AUG": 3, "THOM": 3, "STD": 3, "BANEZ": 2}),
        ],
        "axis_weights": {"GRACE": 4}
    },

    # ==================== SIGNATURE: VOLUNTARISM ====================
    {
        "text": "On divine voluntarism vs intellectualism:",
        "options": [
            ("Voluntarism - God's will is the ultimate ground of morality. Divine command makes things good.",
             {"VOLUNT": 6, "SCOT": 4, "NOMIN": 3, "THOM": -4, "INTELL": -5}),
            ("Intellectualism - God wills things because they are good. Natural law reflects eternal reason.",
             {"INTELL": 6, "THOM": 4, "THOMMETA": 3, "DOM": 2, "VOLUNT": -5}),
            ("A false dichotomy. In God, will and intellect are one. Both capture partial truths.",
             {"THOM": 3, "STD": 3, "DEVPROG": 2, "RESS": 2}),
            ("I lean Scotist/voluntarist but affirm natural law is knowable by reason.",
             {"SCOT": 4, "VOLUNT": 3, "FRANC": 2, "SCOTMETA": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== SIGNATURE: SACRAMENTAL THEOLOGY ====================
    {
        "text": "Which sacramental theology resonates most with you?",
        "options": [
            ("Strict Tridentine - ex opere operato, transubstantiation precisely defined, seven sacraments.",
             {"TRIDSAC": 6, "TRANSUB": 5, "NEOSCH": 3, "TRAD": 3}),
            ("Thomistic - sacraments as instrumental efficient causes, Christ the principal cause.",
             {"THOMSAC": 6, "THOM": 4, "DOM": 3, "TRIDSAC": 2}),
            ("Augustinian - emphasis on faith, interiority, sacraments as 'visible words.'",
             {"AUGSAC": 6, "AUG": 4, "OSA": 3, "NEOAUG": 2}),
            ("Eastern - holy mysteries, epiclesis centrality, theosis orientation.",
             {"EASTSAC": 6, "EASTLIT": 4, "EASTECC": 4, "PALAM": 3, "ORTHOPH": 3}),
            ("Open to transignification language as complementary to transubstantiation.",
             {"TRANSIG": 5, "PROG": 3, "RESS": 2, "TRANSUB": -3, "TRAD": -3}),
            ("Eucharistic mysticism - personal encounter, adoration, transformative union.",
             {"EUCHMYST": 6, "CARM": 3, "BENED": 2, "CP": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== SIGNATURE: MORAL SYSTEMS ====================
    {
        "text": "In moral theology, which system do you favor?",
        "options": [
            ("Probabilism - in doubt, a solidly probable opinion favoring liberty may be followed.",
             {"PROBAB": 6, "JES": 3, "CSSR": 3, "CASUIST": 3, "TUTIOR": -5}),
            ("Tutiorism - always follow the safer opinion favoring law. Strictness protects souls.",
             {"TUTIOR": 6, "JANS": 4, "NEOSCH": 3, "AUGP": 2, "PROBAB": -5}),
            ("Equiprobabilism - St. Alphonsus's balanced middle way between rigorism and laxism.",
             {"CSSR": 5, "STD": 3, "MANUAL": 2, "CASUIST": 2}),
            ("Virtue ethics over casuistry. Character formation matters more than case analysis.",
             {"VIRTUE": 6, "THOMMOR": 3, "AUGMOR": 3, "MANUAL": -3}),
            ("Proportionalism - weigh proportionate reasons; traditional 'intrinsic evil' needs nuance.",
             {"PROP": 6, "PERSMOR": 3, "PROG": 2, "NEOSCH": -5, "TRAD": -4}),
        ],
        "axis_weights": {"RIGOR": 5}
    },


    # ==================== SIGNATURE: RADICAL ORTHODOXY ====================
    {
        "text": "The Radical Orthodoxy movement (Milbank, Pickstock) argues that:",
        "options": [
            ("Secular reason is 'heresy' - modernity's autonomy from theology must be rejected root and branch.",
             {"RADORTH": 6, "INTEG": 3, "NEOPLAT": 3, "COMMUN": 2, "LIBCATH": -4}),
            ("Interesting critique of secularism but sometimes overstates the case against modernity.",
             {"COMMUN": 3, "RESS": 3, "DEVPROG": 2, "STD": 2}),
            ("Too academic and obscure. Practical pastoral concerns matter more than philosophical critique.",
             {"STD": 3, "CM": 2, "SDB": 2, "PROG": 2}),
            ("Essentially correct - all truth participates in divine truth. There is no 'neutral' reason.",
             {"RADORTH": 5, "NEOPLAT": 4, "INTEG": 3, "THOMMETA": 2}),
            ("Dangerous flirtation with fideism. Reason has its own integrity under grace.",
             {"THOM": 3, "DOM": 2, "JES": 2, "RADORTH": -3}),
        ],
        "axis_weights": {}
    },

    # ==================== METAPHYSICS: ANALOGY VS UNIVOCITY ====================
    {
        "text": "On the question of being - analogy (Aquinas) or univocity (Scotus)?",
        "options": [
            ("Analogy - being is said in many ways. God and creatures share being analogically, not identically.",
             {"THOM": 5, "THOMMETA": 5, "DOM": 3, "INTELL": 2, "SCOTMETA": -4}),
            ("Univocity - being must be predicated univocally or we can't speak of God at all.",
             {"SCOTMETA": 6, "SCOT": 5, "FRANC": 3, "VOLUNT": 2, "THOMMETA": -4}),
            ("Both capture important insights. The debate is often overblown.",
             {"STD": 3, "DEVPROG": 2, "RESS": 2}),
            ("Univocity opened the door to modern errors. Analogia entis is non-negotiable.",
             {"RADORTH": 4, "THOMMETA": 4, "THOM": 3, "NEOPLAT": 2, "SCOTMETA": -3}),
        ],
        "axis_weights": {}
    },

    # ==================== NOMINALISM ====================
    {
        "text": "How do you assess the nominalist tradition (Ockham, etc.)?",
        "options": [
            ("A disaster that led to voluntarism, fideism, and ultimately secularism.",
             {"THOM": 4, "THOMMETA": 4, "RADORTH": 3, "INTELL": 3, "NOMIN": -5}),
            ("Contains genuine insights about parsimony and the limits of metaphysical speculation.",
             {"NOMIN": 5, "SCOT": 2, "VOLUNT": 2, "THOM": -2}),
            ("An interesting historical episode with little relevance to contemporary theology.",
             {"STD": 3, "PROG": 2, "DEVPROG": 2}),
            ("Ockham was a faithful Catholic; his positions are defensible within tradition.",
             {"NOMIN": 4, "VOLUNT": 3, "SCOTMETA": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== PALAMISM ====================
    {
        "text": "What is your view of Palamite theology (essence-energies distinction)?",
        "options": [
            ("True - distinguishes God's unknowable essence from His participated energies. Essential for theosis.",
             {"PALAM": 6, "ORTHOPH": 5, "EASTECC": 4, "EASTSAC": 3, "THOM": -2}),
            ("Possibly compatible with Thomism if properly understood. Worth ecumenical dialogue.",
             {"PAPMOD": 3, "DEVPROG": 3, "COMMUN": 3, "ORTHOPH": 2, "RESS": 2}),
            ("Incompatible with divine simplicity. The West rightly rejected it.",
             {"THOM": 4, "THOMMETA": 4, "NEOSCH": 3, "PALAM": -5, "ORTHOPH": -3}),
            ("A distinctly Eastern approach that enriches Catholic theology without replacing Thomism.",
             {"EASTECC": 4, "PALAM": 3, "RESS": 3, "EASTLIT": 2}),
        ],
        "axis_weights": {}
    },

    # ==================== THEOSIS ====================
    {
        "text": "How central is theosis (divinization) to your understanding of salvation?",
        "options": [
            ("Central - 'God became man that man might become God.' This is the heart of soteriology.",
             {"PALAM": 5, "ORTHOPH": 5, "EASTECC": 4, "NEOAUG": 4, "RESS": 3}),
            ("Important but must be balanced with juridical/forensic categories. Both-and, not either-or.",
             {"THOM": 3, "STD": 3, "DEVPROG": 2, "AUG": 2}),
            ("Western theology rightly emphasizes justification. Theosis language risks pantheism.",
             {"NEOSCH": 3, "TRIDSAC": 3, "MANUAL": 2, "PALAM": -3}),
            ("A beautiful Eastern emphasis the West should recover through ressourcement.",
             {"RESS": 5, "NEOAUG": 4, "COMMUN": 3, "PALAM": 3, "BENED": 2}),
        ],
        "axis_weights": {"JUST": 4}
    },

    # ==================== CARMELITE SPIRITUALITY ====================
    {
        "text": "Carmelite spirituality (Teresa of Ávila, John of the Cross) emphasizes:",
        "options": [
            ("Interior prayer and mystical union - the soul's journey through mansions to divine marriage.",
             {"CARM": 6, "EUCHMYST": 3, "CHART": 2, "PIETY": 3}),
            ("Valuable for contemplatives but most Catholics need active, engaged spirituality.",
             {"JES": 3, "DOM": 2, "SDB": 2, "OPUS": 2}),
            ("The 'dark night' teaches detachment from consolations - demanding but transformative.",
             {"CARM": 5, "OCSO": 3, "CHART": 3, "CP": 2}),
            ("Mysticism is dangerous without strong doctrinal grounding and ecclesial oversight.",
             {"NEOSCH": 3, "TRAD": 2, "DOM": 2, "CARM": -2}),
        ],
        "axis_weights": {"PIETY": 5}
    },

    # ==================== PASSIONIST SPIRITUALITY ====================
    {
        "text": "The Passionist emphasis on 'memoria passionis' (memory of Christ's suffering) is:",
        "options": [
            ("Central to Christian life. Meditating on the Passion transforms the soul.",
             {"CP": 6, "CARM": 3, "TRAD": 2, "OSM": 2}),
            ("Important but should be balanced with Resurrection joy and hope.",
             {"STD": 3, "BENED": 2, "SDB": 2, "FRAN": 2}),
            ("Can become morbid. Focus on Christ's victory, not His suffering.",
             {"PROG": 2, "LIBCATH": 2, "CP": -2}),
            ("Connects us to those who suffer today - solidarity with the crucified peoples.",
             {"CP": 4, "CM": 3, "WORKERCATH": 3, "KENOT": 2}),
        ],
        "axis_weights": {"PIETY": 3}
    },

    # ==================== MERCEDARIAN CHARISM ====================
    {
        "text": "The Mercedarian fourth vow - to give one's life for captives if necessary - represents:",
        "options": [
            ("Heroic charity. The willingness to die for another's freedom is profoundly Christlike.",
             {"MERC": 6, "CM": 3, "FRAN": 2, "CP": 2}),
            ("A noble historical charism that should be adapted for modern forms of captivity (trafficking, addiction).",
             {"MERC": 4, "CM": 3, "WORKERCATH": 2, "PROG": 2}),
            ("Inspiring but exceptional. Most are not called to such radical sacrifice.",
             {"STD": 3, "PAPMOD": 2}),
            ("All religious should have this spirit of total self-gift, even if not vowed.",
             {"CHART": 3, "OCSO": 2, "CARM": 2, "MERC": 2}),
        ],
        "axis_weights": {"PIETY": 2}
    },

    # ==================== CULTURE & MODERNITY ====================
    {
        "text": "How should the Church relate to modern culture?",
        "options": [
            ("Resist: Modern culture is largely hostile to faith and natural law",
             {"TRAD": 3, "INTEG": 3, "SSPX": 3, "NEOSCH": 2}),
            ("Engage critically: Affirm what is good, reject what contradicts faith",
             {"STD": 2, "ROTR": 2, "PAPMOD": 2}),
            ("Adapt: The Church must speak modern language to be heard",
             {"PROG": 3, "LIBCATH": 2}),
            ("Ressourcement: Return to sources to address modern questions freshly",
             {"RESS": 3, "NEOAUG": 2}),
        ],
        "axis_weights": {"LIT": 2}
    },
    {
        "text": "What is the value of Scholasticism today?",
        "options": [
            ("Perennially valid: Thomistic philosophy and theology remain normative",
             {"THOMMETA": 3, "THOM": 3, "DOM": 2, "NEOSCH": 3}),
            ("Valuable but not exclusively: Other traditions have insights",
             {"STD": 2, "RESS": 2}),
            ("Historically important but modern thought has surpassed it",
             {"PROG": 2, "LIBCATH": 1}),
            ("One approach among many; Scotist, Augustinian alternatives are equally valid",
             {"SCOT": 2, "FRANC": 2, "AUG": 1}),
        ],
        "axis_weights": {}
    },
    {
        "text": "Did ressourcement theology recover authentic insights?",
        "options": [
            ("Yes: Patristic retrieval corrected neo-scholastic narrowness",
             {"RESS": 3, "NEOAUG": 2, "NEOPLAT": 2}),
            ("Partially: Some good insights but also problematic tendencies",
             {"STD": 2, "THOM": 1}),
            ("No: It undermined sound theology and paved way for modernism",
             {"NEOSCH": 2, "TRAD": 2, "SSPX": 1}),
            ("It's complicated: Need to distinguish various authors and claims",
             {"PAPMOD": 2}),
        ],
        "axis_weights": {}
    },
]

NUM_QUESTIONS = len(QUESTIONS)

# ----------------------------
# 4) Axes definitions
# ----------------------------
AXES = [
    ('GRACE', 'Grace Theology'),
    ('PAPAL', 'Papal Authority'),
    ('LIT', 'Liturgical Traditionalism'),
    ('RIGOR', 'Moral Rigorism'),
    ('PIETY', 'Personal Piety'),
    ('SCRIPT', 'Scripture Authority & Hermeneutics'),
    ('JUST', 'Justification & Union'),
    ('ESCH', 'Eschatology & Final Judgment'),
]

AXIS_CODES = [c for c, _ in AXES]
AXIS_NAME = {c: n for c, n in AXES}
AXIS_ENDPOINTS = {
    "GRACE": ("Synergistic", "Monergistic"),
    "PAPAL": ("Conciliar/Local", "Ultramontane"),
    "LIT": ("Reformist", "Traditional"),
    "RIGOR": ("Pastoral/Lenient", "Rigorist"),
    "PIETY": ("Lower Intensity", "High Contemplative"),
    "SCRIPT": ("Magisterium-first", "Scripture-first (within Tradition)"),
    "JUST": ("Forensic emphasis", "Participatory / union emphasis"),
    "ESCH": ("This-world / pastoral", "Judgment & beatific end"),
}

# Per-axis display scaling. Higher multipliers give axes with fewer questions a fuller spread.
AXIS_MULTIPLIER = {
    "GRACE": 3,
    "PAPAL": 3,
    "LIT": 3,
    "RIGOR": 3,
    "PIETY": 3,
    "SCRIPT": 4,
    "JUST": 4,
    "ESCH": 4,
}

# ----------------------------
# 5) Patron Saints
# ----------------------------
PATRON_SAINTS = {
    "AUG": {"primary": ("St. Augustine of Hippo", "Late Antique"), "why": "Doctor of Grace."},
    "THOM": {"primary": ("St. Thomas Aquinas", "Medieval"), "why": "The Angelic Doctor."},
    "SCOT": {"primary": ("Bl. John Duns Scotus", "Medieval"), "why": "The Subtle Doctor."},
    "DOM": {"primary": ("St. Dominic", "Medieval"), "why": "Founder of the Order of Preachers."},
    "JES": {"primary": ("St. Ignatius of Loyola", "Early Modern"), "why": "Founder of the Society of Jesus."},
    "CARM": {"primary": ("St. Teresa of Ávila", "Early Modern"), "why": "Doctor of Prayer."},
    "BENED": {"primary": ("St. Benedict of Nursia", "Late Antique"), "why": "Father of Western Monasticism."},
    "INTEG": {"primary": ("Pope St. Pius X", "Modern"), "why": "Defender against Modernism."},
    "DISTRIBUT": {"primary": ("G.K. Chesterton", "Modern"), "why": "Champion of Distributism."},
    "STD": {"primary": ("St. John Henry Newman", "Modern"), "why": "Model of balanced Catholic thought."},
    "BANEZ": {"primary": ("Domingo Báñez, O.P.", "Early Modern"), "why": "Architect of physical premotion."},
    "MOL": {"primary": ("Luis de Molina, S.J.", "Early Modern"), "why": "Architect of middle knowledge."},
}

for code in SCHOOL_CODES:
    if code not in PATRON_SAINTS:
        PATRON_SAINTS[code] = {"primary": ("Various Saints", ""), "why": "See theological literature."}


# ============================================================
# GUI Application
# ============================================================

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Catholic Theology Schools Quiz - Full Multiple Choice")
        self.geometry("1000x750")
        self.resizable(True, True)

        self.q_index = 0
        self.answers = [None] * NUM_QUESTIONS
        self.scores = {code: 0 for code in SCHOOL_CODES}
        self.axis_scores = {ax: 0 for ax in AXIS_CODES}

        self._build_ui()
        self._render_question()

    def _build_ui(self):
        main = ttk.Frame(self, padding=10)
        main.pack(fill="both", expand=True)

        # Left: question list
        left = ttk.Frame(main, width=220)
        left.pack(side="left", fill="y", padx=(0, 10))

        ttk.Label(left, text="Questions", font=("Arial", 11, "bold")).pack(anchor="w")

        list_frame = ttk.Frame(left)
        list_frame.pack(fill="both", expand=True)

        self.q_list = tk.Listbox(list_frame, width=30, height=35, font=("Arial", 9))
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.q_list.yview)
        self.q_list.configure(yscrollcommand=scrollbar.set)

        self.q_list.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for i, q in enumerate(QUESTIONS):
            prefix = q["text"][:30] + "..." if len(q["text"]) > 30 else q["text"]
            self.q_list.insert("end", f"{i+1}. {prefix}")

        self.q_list.bind("<<ListboxSelect>>", self._jump_to_question)

        # Right: question + answers
        right = ttk.Frame(main)
        right.pack(side="right", fill="both", expand=True)

        # Progress
        top_bar = ttk.Frame(right)
        top_bar.pack(fill="x", pady=(0, 10))

        self.progress_var = tk.StringVar(value=f"Question 1 of {NUM_QUESTIONS}")
        ttk.Label(top_bar, textvariable=self.progress_var, font=("Arial", 10, "bold")).pack(side="left")

        self.answered_var = tk.StringVar(value=f"Answered: 0 / {NUM_QUESTIONS}")
        ttk.Label(top_bar, textvariable=self.answered_var).pack(side="right")

        self.pb = ttk.Progressbar(right, maximum=NUM_QUESTIONS, length=500)
        self.pb.pack(fill="x", pady=(0, 10))

        # Question
        q_frame = ttk.LabelFrame(right, text="Question", padding=10)
        q_frame.pack(fill="x", pady=(0, 10))

        self.question_box = tk.Text(q_frame, wrap="word", height=3, font=("Arial", 11), state="disabled", bg="#f9f9f9")
        self.question_box.pack(fill="x")

        # Answers
        ans_container = ttk.LabelFrame(right, text="Select Your Answer", padding=10)
        ans_container.pack(fill="both", expand=True, pady=(0, 10))

        # Scrollable frame for answers
        canvas = tk.Canvas(ans_container, highlightthickness=0)
        scrollbar2 = ttk.Scrollbar(ans_container, orient="vertical", command=canvas.yview)
        self.answer_frame = ttk.Frame(canvas)

        self.answer_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.answer_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar2.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar2.pack(side="right", fill="y")

        self.choice_var = tk.IntVar(value=-1)

        # Navigation
        nav = ttk.Frame(right)
        nav.pack(fill="x")

        self.back_btn = ttk.Button(nav, text="← Back", command=self._go_back)
        self.back_btn.pack(side="left")

        self.next_btn = ttk.Button(nav, text="Next →", command=self._go_next)
        self.next_btn.pack(side="left", padx=10)

        self.results_btn = ttk.Button(nav, text="See Results", command=self._show_results)
        self.results_btn.pack(side="right")

    def _render_question(self):
        i = self.q_index
        q = QUESTIONS[i]

        self.progress_var.set(f"Question {i+1} of {NUM_QUESTIONS}")
        self.pb["value"] = i

        answered = sum(1 for a in self.answers if a is not None)
        self.answered_var.set(f"Answered: {answered} / {NUM_QUESTIONS}")

        self.back_btn["state"] = "normal" if i > 0 else "disabled"

        self.question_box.configure(state="normal")
        self.question_box.delete("1.0", "end")
        self.question_box.insert("end", q["text"])
        self.question_box.configure(state="disabled")

        # Clear answers
        for widget in self.answer_frame.winfo_children():
            widget.destroy()

        self.choice_var.set(-1)

        for j, (label, weights) in enumerate(q["options"]):
            rb = tk.Radiobutton(self.answer_frame, text=label, variable=self.choice_var, value=j, 
                               wraplength=550, justify="left", anchor="w", padx=10, pady=3,
                               font=("Arial", 10), bg="#f5f5f5", activebackground="#e0e0e0",
                               selectcolor="#d0d0d0")
            rb.pack(anchor="w", pady=4, padx=5, fill="x")

        if self.answers[i] is not None:
            self.choice_var.set(self.answers[i])

        self.q_list.selection_clear(0, "end")
        self.q_list.selection_set(i)
        self.q_list.see(i)

    def _jump_to_question(self, event=None):
        sel = self.q_list.curselection()
        if sel:
            self.q_index = sel[0]
            self._render_question()

    def _go_back(self):
        if self.q_index > 0:
            self.q_index -= 1
            self._render_question()

    def _go_next(self):
        i = self.q_index
        val = self.choice_var.get()

        if val == -1:
            messagebox.showwarning("Answer Required", "Please select an answer before continuing.")
            return

        self.answers[i] = val

        if i < NUM_QUESTIONS - 1:
            self.q_index += 1
            self._render_question()
        else:
            self._show_results()

    def _compute_scores(self):
        self.scores = {code: 0 for code in SCHOOL_CODES}
        self.axis_scores = {ax: 0 for ax in AXIS_CODES}

        for i, ans in enumerate(self.answers):
            if ans is None:
                continue
            q = QUESTIONS[i]

            if 0 <= ans < len(q["options"]):
                _, weights = q["options"][ans]
                for code, w in weights.items():
                    if code in self.scores:
                        self.scores[code] += w

                axis_w = q.get("axis_weights", {})
                for ax, w in axis_w.items():
                    if ax in self.axis_scores:
                        self.axis_scores[ax] += w

    def _show_results(self):
        answered = sum(1 for a in self.answers if a is not None)
        if answered < NUM_QUESTIONS // 2:
            if not messagebox.askyesno("Incomplete", f"You've answered {answered}/{NUM_QUESTIONS}. Show results anyway?"):
                return

        self._compute_scores()

        results = tk.Toplevel(self)
        results.title("Quiz Results")
        results.geometry("950x700")

        notebook = ttk.Notebook(results)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Tab 1: Rankings
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="School Rankings")

        ttk.Label(tab1, text="Your Top Theological Schools", font=("Arial", 14, "bold")).pack(pady=10)

        ranked = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)

        tree = ttk.Treeview(tab1, columns=("rank", "school", "score"), show="headings", height=20)
        tree.heading("rank", text="Rank")
        tree.heading("school", text="School")
        tree.heading("score", text="Score")
        tree.column("rank", width=60, anchor="center")
        tree.column("school", width=400)
        tree.column("score", width=80, anchor="center")

        for j, (code, score) in enumerate(ranked[:30]):
            tree.insert("", "end", values=(j+1, SCHOOL_NAME.get(code, code), score))

        tree.pack(fill="both", expand=True, padx=10)

        # Tab 2: Axes
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Axes Profile")

        ttk.Label(tab2, text="Your Theological Axes", font=("Arial", 14, "bold")).pack(pady=10)

        for ax in AXIS_CODES:
            frame = ttk.Frame(tab2)
            frame.pack(fill="x", padx=20, pady=8)

            lo, hi = AXIS_ENDPOINTS.get(ax, ("Low", "High"))
            score = self.axis_scores.get(ax, 0)
            mult = AXIS_MULTIPLIER.get(ax, 3)
            norm = max(0, min(100, 50 + score * mult))

            ttk.Label(frame, text=f"{AXIS_NAME[ax]}:", width=22, anchor="e").pack(side="left")
            ttk.Label(frame, text=lo, width=18).pack(side="left")

            pb = ttk.Progressbar(frame, length=300, value=norm, maximum=100)
            pb.pack(side="left", padx=5)

            ttk.Label(frame, text=hi, width=18).pack(side="left")
            ttk.Label(frame, text=f"({score:+d})", width=8).pack(side="left")

        # Tab 3: Top match
        tab3 = ttk.Frame(notebook)
        notebook.add(tab3, text="Your Top Match")

        if ranked:
            top_code, top_score = ranked[0]
            desc = SCHOOL_DESC.get(top_code, {})
            patron = PATRON_SAINTS.get(top_code, {})

            ttk.Label(tab3, text=f"Your Top Match: {SCHOOL_NAME.get(top_code, top_code)}",
                     font=("Arial", 16, "bold")).pack(pady=15)

            ttk.Label(tab3, text=f"Score: {top_score}", font=("Arial", 12)).pack()

            ttk.Label(tab3, text=desc.get("summary", ""), wraplength=700,
                     font=("Arial", 11)).pack(pady=15, padx=20)

            ttk.Label(tab3, text="Typical Affirmations:", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
            for aff in desc.get("affirmations", []):
                ttk.Label(tab3, text=f"  • {aff}", wraplength=650).pack(anchor="w", padx=30)

            if patron:
                primary = patron.get("primary", ("", ""))
                ttk.Label(tab3, text=f"\nPatron Figure: {primary[0]} ({primary[1]})",
                         font=("Arial", 11, "italic")).pack(pady=15)


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
