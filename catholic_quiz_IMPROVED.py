<!DOCTYPE html>
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
        
        /* Topic Section */
        .topic-section { margin-bottom: 1.25rem; padding-bottom: 1rem; border-bottom: 1px dashed var(--gold-light); }
        .topic-header { font-family: 'Cinzel', serif; font-size: 1rem; color: var(--crimson); margin-bottom: 0.5rem; font-weight: 600; }
        .topic-description { font-size: 0.9rem; color: var(--ink); line-height: 1.5; margin-bottom: 0.75rem; }
        .topic-reading { font-size: 0.85rem; color: var(--ink-light); margin-bottom: 0.75rem; }
        
        
        .citation-header { font-size: 0.9rem; color: var(--blue); margin: 0.75rem 0 0.5rem 0; }

        /* Defer / Skip Buttons */

        /* Defer Modal/Panel */

        .saint-name {
            font-family: 'Cinzel', serif;
            font-size: 0.85rem;
            color: var(--crimson);
            font-weight: 600;
        }
        .saint-era {
            font-size: 0.75rem;
            color: var(--ink-light);
            font-style: italic;
        }
        .saint-position {
            font-size: 0.85rem;
            color: var(--ink);
            margin-top: 0.25rem;
            line-height: 1.4;
        }
        .saint-option-label {
            font-size: 0.7rem;
            color: var(--gold);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 0.2rem;
        }
        .defer-note {
            font-size: 0.75rem;
            color: var(--ink-light);
            margin-top: 0.5rem;
            font-style: italic;
        }

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
        
        /* Enhanced Figure Section */
        .figure-section { text-align: left; padding: 1.25rem; background: rgba(255,255,255,0.1); border-radius: 8px; margin-top: 1.25rem; border: 1px solid rgba(201, 162, 39, 0.3); }
        .figure-label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.7; margin-bottom: 0.4rem; }
        .figure-name { font-family: 'Cinzel', serif; font-size: 1.2rem; color: var(--gold-light); margin-bottom: 0.2rem; }
        .figure-era { font-style: italic; opacity: 0.8; font-size: 0.85rem; margin-bottom: 0.75rem; color: var(--gold-light); }
        .figure-bio { font-size: 0.95rem; line-height: 1.5; margin-bottom: 0.75rem; }
        .figure-works { font-size: 0.85rem; opacity: 0.9; line-height: 1.4; }
        
        /* Heterodoxy Warnings */
        .heterodoxy-warning { padding: 1rem 1.25rem; border-radius: 8px; margin: 1rem 0; text-align: left; }
        .heterodoxy-warning.severe { background: rgba(220, 53, 69, 0.2); border: 2px solid #dc3545; }
        .heterodoxy-warning.moderate { background: rgba(255, 193, 7, 0.2); border: 2px solid #ffc107; }
        .heterodoxy-warning.caution { background: rgba(255, 193, 7, 0.15); border: 1px solid #ffc107; }
        .heterodoxy-warning.non-catholic { background: rgba(108, 117, 125, 0.2); border: 1px solid #6c757d; }
        .heterodoxy-title { font-family: 'Cinzel', serif; font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem; }
        .heterodoxy-warning.severe .heterodoxy-title { color: #ff6b6b; }
        .heterodoxy-warning.moderate .heterodoxy-title { color: #ffd43b; }
        .heterodoxy-warning.caution .heterodoxy-title { color: #ffe066; }
        .heterodoxy-warning.non-catholic .heterodoxy-title { color: #adb5bd; }
        .heterodoxy-text { font-size: 0.9rem; line-height: 1.5; margin-bottom: 0.75rem; }
        .heterodoxy-docs { font-size: 0.8rem; opacity: 0.9; margin-bottom: 0.5rem; }
        .heterodoxy-guidance { font-size: 0.85rem; font-style: italic; opacity: 0.9; }
        
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
        .school-name .question-count { font-weight: 400; font-size: 0.75rem; color: var(--ink-light); margin-left: 0.5rem; }
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
            
        }
    
        /* Screen Reader Only - Accessibility */
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border-width: 0;
        }

        /* Category Page Navigation */
        .category-page { display: none; }
        .category-page.active { display: block; animation: fadeIn 0.4s ease; }
        
        .page-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.25rem;
            background: white;
            border-radius: 12px;
            box-shadow: 0 2px 10px var(--shadow);
            border: 1px solid var(--gold-light);
            margin-bottom: 1.5rem;
        }
        .page-nav-title {
            font-family: 'Cinzel', serif;
            font-size: 1.1rem;
            color: var(--crimson);
        }
        .page-nav-subtitle {
            font-size: 0.85rem;
            color: var(--ink-light);
        }
        
        /* Magisterium Button */
        .magisterium-btn {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            padding: 0.75rem 1.25rem;
            background: linear-gradient(135deg, #1a3a5c, #2a5298);
            border: 2px solid var(--gold);
            color: var(--gold-light);
            font-family: 'Cinzel', serif;
            font-size: 0.8rem;
            border-radius: 10px;
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(26, 58, 92, 0.4);
            transition: all 0.3s ease;
            z-index: 999;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .magisterium-btn:hover { transform: translateY(-3px); box-shadow: 0 6px 25px rgba(26, 58, 92, 0.6); }
        /* Magisterium Panel */
.mag-panel {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.55);
  z-index: 1200;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}

.mag-panel.hidden { display: none !important; }

.mag-panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  border-bottom: 1px solid var(--gold-light);
  background: white;
  border-radius: 12px 12px 0 0;
}

.mag-panel-title {
  font-family: 'Cinzel', serif;
  color: var(--crimson);
  font-size: 0.95rem;
}

.mag-panel-actions { display: flex; gap: 0.5rem; flex-wrap: wrap; }

.mag-panel-btn {
  font-family: 'Cinzel', serif;
  font-size: 0.75rem;
  padding: 0.45rem 0.7rem;
  border-radius: 8px;
  border: 1px solid var(--gold-light);
  background: var(--ivory);
  cursor: pointer;
}

.mag-panel-btn:hover { border-color: var(--gold); background: var(--parchment); }

.mag-panel-body {
  width: min(1100px, 96vw);
  height: min(720px, 86vh);
  background: white;
  border-radius: 0 0 12px 12px;
  box-shadow: 0 10px 35px rgba(0,0,0,0.35);
  overflow: hidden;
  border: 1px solid var(--gold-light);
}

.mag-panel-status {
  padding: 0.6rem 0.9rem;
  font-size: 0.85rem;
  color: var(--ink-light);
  border-bottom: 1px dashed var(--gold-light);
  background: rgba(42, 82, 152, 0.05);
}

.mag-iframe {
  width: 100%;
  height: calc(100% - 44px);
  border: 0;
}
        /* I Don't Know Button */
        .idk-btn {
            display: block;
            width: 100%;
            margin-top: 0.75rem;
            padding: 0.7rem 1rem;
            background: var(--ivory);
            border: 2px dashed var(--gold-light);
            border-radius: 8px;
            font-family: 'Crimson Pro', serif;
            font-size: 0.95rem;
            color: var(--ink-light);
            cursor: pointer;
            transition: all 0.25s ease;
            text-align: center;
        }
        .idk-btn:hover { background: var(--parchment); border-color: var(--gold); color: var(--ink); }
        .idk-btn.selected { background: rgba(201, 162, 39, 0.1); border-color: var(--gold); border-style: solid; color: var(--gold); }
        
        /* Saints Panel */
        .saints-toggle {
            font-family: 'Cinzel', serif;
            font-size: 0.8rem;
            color: var(--crimson);
            background: transparent;
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 0;
            margin-top: 0.75rem;
            transition: color 0.2s;
        }
        .saints-toggle:hover { color: var(--crimson-dark); }
        .saints-toggle .arrow { transition: transform 0.2s; display: inline-block; }
        .saints-toggle.open .arrow { transform: rotate(90deg); }
        .saints-content {
            display: none;
            margin-top: 0.5rem;
            padding: 1rem;
            background: linear-gradient(135deg, rgba(139, 21, 56, 0.04), rgba(201, 162, 39, 0.04));
            border-radius: 8px;
            border-left: 3px solid var(--crimson);
        }
        .saints-content.open { display: block; animation: fadeIn 0.3s ease; }
        .saint-card {
            padding: 0.6rem 0.8rem;
            margin-bottom: 0.4rem;
            background: white;
            border: 1px solid var(--gold-light);
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .saint-card:hover { border-color: var(--gold); transform: translateX(3px); }
        .saint-card.active { border-color: var(--crimson); background: rgba(139, 21, 56, 0.04); }
        .saint-card-name { font-family: 'Cinzel', serif; font-size: 0.8rem; color: var(--crimson); font-weight: 600; }
        .saint-card-era { font-size: 0.7rem; color: var(--ink-light); font-style: italic; }
        .saint-card-pos { font-size: 0.8rem; color: var(--ink); margin-top: 0.15rem; line-height: 1.4; }
        .saint-card-opt { font-size: 0.65rem; color: var(--gold); text-transform: uppercase; letter-spacing: 0.05em; }
        .no-saints { font-size: 0.85rem; color: var(--ink-light); font-style: italic; padding: 0.5rem 0; }
        
        /* Sources Panel */
        .sources-toggle {
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
        .sources-toggle:hover { color: var(--blue-light); }
        .sources-toggle .arrow { transition: transform 0.2s; display: inline-block; }
        .sources-toggle.open .arrow { transform: rotate(90deg); }
        .sources-content {
            display: none;
            margin-top: 0.5rem;
            padding: 1rem;
            background: rgba(42, 82, 152, 0.04);
            border-radius: 8px;
            border-left: 3px solid var(--blue);
        }
        .sources-content.open { display: block; animation: fadeIn 0.3s ease; }
        .source-topic { font-family: 'Cinzel', serif; font-size: 0.9rem; color: var(--blue); margin-bottom: 0.4rem; }
        .source-desc { font-size: 0.85rem; color: var(--ink); margin-bottom: 0.5rem; line-height: 1.5; }
        .source-reading { font-size: 0.85rem; color: var(--ink-light); line-height: 1.5; }
        .source-reading strong { color: var(--ink); }

    </style>
</head>
<body>
    <div class="main-container">
        <div class="quiz-panel" id="quiz-panel">
            <header>
                <h1>Definitive Catholic Theology Quiz</h1>
                <p class="subtitle">134 Questions · 85 Schools of Thought · Hybrid Scoring</p>
                <div class="cross-divider"><span>✝</span></div>
            </header>
            
            <!-- Start Screen -->
            <div id="start-screen">
                <div class="start-screen">
                    <h2>Discover Your Theological Position</h2>
                    <p>This comprehensive quiz maps your theological convictions across the full spectrum of Catholic schools of thought, religious orders, and related traditions.</p>
                    <div class="stats">
                        <div class="stat"><span class="stat-value">134</span><span class="stat-label">Questions</span></div>
                        <div class="stat"><span class="stat-value">10</span><span class="stat-label">Categories</span></div>
                        <div class="stat"><span class="stat-value">85</span><span class="stat-label">Schools</span></div>
                    </div>
                    
                    <div class="quiz-length-section">
                        <h3>Choose Quiz Length</h3>
                        <div class="length-options">
                            <label class="length-option" onclick="setQuizLength(25)">
                                <input type="radio" name="quiz-length" value="25">
                                <div class="length-card">
                                    <span class="length-number">25</span>
                                    <span class="length-label">Quick</span>
                                </div>
                            </label>
                            <label class="length-option" onclick="setQuizLength(50)">
                                <input type="radio" name="quiz-length" value="50">
                                <div class="length-card">
                                    <span class="length-number">50</span>
                                    <span class="length-label">Medium</span>
                                </div>
                            </label>
                            <label class="length-option" onclick="setQuizLength(75)">
                                <input type="radio" name="quiz-length" value="75">
                                <div class="length-card">
                                    <span class="length-number">75</span>
                                    <span class="length-label">Extended</span>
                                </div>
                            </label>
                            <label class="length-option" onclick="setQuizLength(100)">
                                <input type="radio" name="quiz-length" value="100">
                                <div class="length-card">
                                    <span class="length-number">100</span>
                                    <span class="length-label">Thorough</span>
                                </div>
                            </label>
                            <label class="length-option" onclick="setQuizLength(134)">
                                <input type="radio" name="quiz-length" value="134" checked>
                                <div class="length-card">
                                    <span class="length-number">134</span>
                                    <span class="length-label">All <small>(Recommended)</small></span>
                                </div>
                            </label>
                        </div>
                        <p class="length-note">Shorter quizzes sample proportionally from each category.</p>
                    </div>
                    
                    <button class="start-btn" onclick="startQuiz()">Begin Quiz</button>
                </div>
            </div>
            
            <!-- Quiz Screen -->
            <div id="quiz-screen" class="hidden">
                <!-- Category Tab Navigation -->
                <div class="category-nav" id="category-nav"></div>
                
                <!-- Progress -->
                <div class="progress-section">
                    <div class="progress-header">
                        <span class="progress-text" id="progress-text">Question 1 of 134</span>
                        <span class="progress-count" id="answered-count">Answered: 0 / 134</span>
                    </div>
                    <div class="progress-bar"><div class="progress-fill" id="progress-fill"></div></div>
                </div>
                
                <!-- Question Card -->
                <div class="question-card">
                    <div class="question-header">
                        <span class="question-number" id="question-number">Question I</span>
                        <span class="question-category-tag" id="question-category-tag"></span>
                    </div>
                    <div class="question-text" id="question-text"></div>
                    
                    <!-- Options -->
                    <div class="options" id="options"></div>
                    
                    <!-- I Don't Know -->
                    <button class="idk-btn" id="idk-btn" onclick="selectIDK()">🤷 I Don't Know / No Strong Opinion</button>
                    
                    <!-- Saints & Theologians -->
                    <button class="saints-toggle" id="saints-toggle" onclick="toggleSaints()">
                        <span class="arrow">▶</span> ✝️ Saints &amp; Theologians Who Held These Views
                    </button>
                    <div class="saints-content" id="saints-content">
                        <div id="saints-list"></div>
                    </div>
                    
                    <!-- Further Reading -->
                    <button class="sources-toggle" id="sources-toggle" onclick="toggleSources()">
                        <span class="arrow">▶</span> 📖 Further Reading &amp; Sources
                    </button>
                    <div class="sources-content" id="sources-content">
                        <div id="sources-list"></div>
                    </div>
                </div>
                
                <!-- Navigation -->
                <div class="navigation">
                    <button class="nav-btn secondary" id="prev-btn" onclick="prevQuestion()">← Previous</button>
                    <button class="nav-btn primary" id="next-btn" onclick="nextQuestion()">Next →</button>
                    <button class="nav-btn primary hidden" id="results-btn" onclick="showResults()">View Results</button>
                </div>
                
                <!-- Question Nav Dots -->
                <div class="question-nav" id="question-nav"></div>
            </div>
            
            <!-- Results Screen -->
            <div id="results-screen" class="results-screen">
                <div class="results-header">
                    <h2>Your Theological Profile</h2>
                    <div class="cross-divider"><span>✝</span></div>
                </div>
                <div id="top-match-container"></div>
                
                <div class="tabs">
                    <button class="tab-btn active" onclick="switchTab('rankings')">Rankings</button>
                    <button class="tab-btn" onclick="switchTab('axes')">Spectrums</button>
                </div>
                
                <div id="rankings-tab" class="tab-content active">
                    <div class="rankings-card">
                        <h3>School Rankings</h3>
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
    </div>
    
    <!-- Magisterium Button -->
    <button class="magisterium-btn" id="magisterium-btn" style="display:none;" onclick="openMagisteriumPanel()" title="Get help from Magisterium AI">
        📖 Ask Magisterium AI
    </button>

    <script>
// =============================================
// DATA
// =============================================

const SCHOOLS = [
    ["AUG", "Augustinian"],
    ["AUGP", "Strict Augustinian"],
    ["NEOAUG", "Neo-Augustinian (ressourcement)"],
    ["JANS", "Jansenist"],
    ["THOM", "Thomist (mainstream)"],
    ["BANEZ", "Bañezian"],
    ["MOL", "Molinist"],
    ["SCOT", "Scotist"],
    ["FRANC", "Franciscan (Bonaventure)"],
    ["INFRA", "Infralapsarian"],
    ["SUPRA", "Supralapsarian"],
    ["DOM", "Dominican"],
    ["JES", "Jesuit"],
    ["CARM", "Carmelite"],
    ["BENED", "Benedictine"],
    ["OPUS", "Opus Dei"],
    ["FRAN", "Franciscan (order)"],
    ["ORAT", "Oratorian"],
    ["CHART", "Carthusian"],
    ["OCSO", "Cistercian/Trappist"],
    ["CSSR", "Redemptorist"],
    ["SDB", "Salesian"],
    ["CM", "Vincentian/Lazarist"],
    ["CP", "Passionist"],
    ["OSM", "Servite"],
    ["OPRAEM", "Norbertine/Premonstratensian"],
    ["MERC", "Mercedarian"],
    ["NEOPLAT", "Neo-Platonist"],
    ["THOMMETA", "Thomist (Realist)"],
    ["NOMIN", "Nominalist-leaning"],
    ["INTELL", "Intellectualist"],
    ["PALAM", "Palamite"],
    ["RESSCH", "Ressourcement Christology"],
    ["CHALMAX", "Chalcedonian Maximalist"],
    ["KENOT", "Kenoticism-sympathetic"],
    ["TRIDSAC", "Tridentine Sacramentalism"],
    ["EASTSAC", "Eastern Sacramental"],
    ["TRANSIG", "Transignification-open"],
    ["EUCHMYST", "Eucharistic Mysticism"],
    ["ULTRA", "Ultramontane"],
    ["PAPMOD", "Moderate Papalist"],
    ["PAPMIN", "Papal Minimalist"],
    ["GALL", "Gallican"],
    ["CONCIL", "Conciliarist"],
    ["EASTECC", "Eastern Catholic"],
    ["SYNOD", "Synodalist"],
    ["THOMMOR", "Thomist Natural Law"],
    ["MANUAL", "Manualist"],
    ["VIRTUE", "Virtue Ethics"],
    ["PERSMOR", "Personalist Moral"],
    ["PROP", "Proportionalist"],
    ["NEOSCH", "Neo-Scholastic Rigorist"],
    ["CASUIST", "Casuist"],
    ["PROBAB", "Probabilist"],
    ["TUTIOR", "Tutiorist"],
    ["INTEG", "Integralist"],
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
    ["TRAD", "Traditionalist"],
    ["ROTR", "Reform of the Reform"],
    ["PROG", "Progressive"],
    ["RESS", "Ressourcement"],
    ["STD", "Standard Catholic"],
    ["SSPX", "SSPX-leaning"],
    ["SEDE", "Sedevacantist"],
    ["ORDINAR", "Ordinariate"],
    ["ORTHOPH", "Orthophile"],
    ["ECUMON", "Ecumenical Monergist"],
    ["ANTIMOD", "Anti-Modernist"],
    ["DEVPROG", "Developmental Progressive"],
    ["COMMUN", "Communio School"],
    ["RADORTH", "Radical Orthodoxy"],
    ["TRADUM", "Traditionis Custodes Compliant"],
    ["REFORM", "Reformed"],
    ["LUTHERAN", "Lutheran"],
    ["ANGLICAN", "Anglican"],
    ["EORTHO", "Eastern Orthodox"]
];

const SCHOOL_NAME = Object.fromEntries(SCHOOLS);

const MAX_POSSIBLE_SCORES = {
  "STD": 288, "THOM": 244, "PROG": 239, "TRAD": 214, "PAPMOD": 160, "LIBCATH": 154,
  "RESS": 147, "AUG": 142, "EASTECC": 139, "BENED": 123, "INTEG": 115, "SSPX": 113,
  "NEOSCH": 112, "DOM": 100, "DEVPROG": 93, "COMMUN": 90, "TRIDSAC": 89, "PALAM": 87,
  "NEOAUG": 85, "SCOT": 80, "JES": 79, "ROTR": 74, "ANTIMOD": 74, "CARM": 74,
  "ORTHOPH": 72, "PERSMOR": 70, "SYNOD": 66, "ULTRA": 65, "EORTHO": 60, "MOL": 59,
  "JANS": 59, "REFORM": 59, "ECUMON": 56, "SEDE": 54, "EASTSAC": 54, "AUGP": 53,
  "NEOPLAT": 47, "FRANC": 45, "THOMMETA": 43, "LUTHERAN": 42, "NOMIN": 40, "BANEZ": 40,
  "CHART": 39, "ANGLICAN": 38, "OPUS": 35, "MANUAL": 33, "FRAN": 33, "WORKERCATH": 30,
  "THOMMOR": 30, "CATHUNIV": 29, "CM": 28, "INTEGSOFT": 28, "DISTRIBUT": 28, "PAPMIN": 27,
  "EUCHMYST": 26, "CSSR": 26, "TRADUM": 25, "TRADNAT": 25, "SDB": 24, "SOCDEM": 24,
  "OCSO": 24, "OSM": 23, "KENOT": 22, "CP": 21, "GALL": 21, "CONCIL": 21,
  "ORAT": 20, "INTELL": 20, "SUPRA": 20, "RADORTH": 16, "CHALMAX": 16, "RESSCH": 15,
  "ORDINAR": 14, "CORPCATH": 14, "MERC": 14, "LIBERTAR": 13, "INFRA": 11, "TRANSIG": 10,
  "TUTIOR": 10, "OPRAEM": 10, "VIRTUE": 10, "CASUIST": 10, "AGRAR": 10, "PROBAB": 6,
  "PROP": 5
};

const SCHOOL_QUESTION_COUNTS = {
  "STD": 107, "PROG": 86, "TRAD": 76, "THOM": 74, "PAPMOD": 64, "RESS": 61,
  "LIBCATH": 56, "BENED": 54, "NEOSCH": 45, "DOM": 44, "AUG": 42, "PERSMOR": 37,
  "DEVPROG": 37, "NEOAUG": 34, "INTEG": 34, "EASTECC": 33, "JES": 32, "TRIDSAC": 30,
  "COMMUN": 30, "SSPX": 30, "PALAM": 30, "CARM": 29, "ROTR": 25, "SYNOD": 25,
  "ANTIMOD": 24, "JANS": 20, "NEOPLAT": 19, "ORTHOPH": 19, "ULTRA": 18, "FRANC": 18,
  "EASTSAC": 18, "SCOT": 17, "AUGP": 17, "SEDE": 16, "MANUAL": 16, "REFORM": 16,
  "THOMMETA": 14, "FRAN": 14, "PAPMIN": 13, "EORTHO": 13, "OPUS": 13, "BANEZ": 13,
  "LUTHERAN": 13, "CHART": 13, "MOL": 12, "EUCHMYST": 12, "SOCDEM": 12, "WORKERCATH": 12,
  "THOMMOR": 12, "CM": 11, "ANGLICAN": 11, "ORAT": 10, "SDB": 10, "DISTRIBUT": 10,
  "OSM": 9, "ECUMON": 9, "TRADUM": 8, "INTELL": 8, "CP": 8, "CSSR": 8,
  "GALL": 8, "INTEGSOFT": 8, "CATHUNIV": 8, "NOMIN": 7, "SUPRA": 7, "KENOT": 7,
  "OCSO": 7, "CONCIL": 7, "TRADNAT": 7, "RESSCH": 6, "CORPCATH": 6, "VIRTUE": 6,
  "TUTIOR": 5, "CHALMAX": 5, "OPRAEM": 5, "CASUIST": 5, "MERC": 5, "LIBERTAR": 5,
  "TRANSIG": 4, "RADORTH": 4, "INFRA": 4, "AGRAR": 4, "ORDINAR": 3, "PROP": 2,
  "PROBAB": 2
};

const SCHOOL_DESC = {
    "AUG": {"summary": "Emphasizes the depth of human fallenness and the absolute necessity of divine grace for any salvific good.", "affirmations": ["Grace precedes merit", "Nature profoundly wounded", "Will grounds predestination"]},
    "AUGP": {"summary": "Stricter Augustine: irresistible grace, massa damnata, double predestination in softer form.", "affirmations": ["Grace infallibly efficacious", "Reprobate justly passed over"]},
    "NEOAUG": {"summary": "Ressourcement retrieval of Augustine: participatory ontology, Christocentric grace, liturgical renewal.", "affirmations": ["Christ is the concrete universal", "Grace as participation in divine life"]},
    "THOM": {"summary": "Mainstream Thomism balancing Aristotelian metaphysics with Augustinian grace theology.", "affirmations": ["Being is analogical", "Grace perfects nature", "Will follows intellect's presentation of good"]},
    "MOL": {"summary": "Jesuit school emphasizing middle knowledge and libertarian freedom.", "affirmations": ["God knows counterfactuals of freedom", "Grace extrinsically efficacious", "Human freedom is libertarian"]},
    "FRANC": {"summary": "Franciscan theology of Bonaventure: exemplarism, Christ as center, affective-mystical approach.", "affirmations": ["Christ is medium of all knowledge", "Love leads to wisdom"]},
    "INFRA": {"summary": "God's decree of predestination logically follows his decree to permit the Fall.", "affirmations": ["Election from the fallen mass", "More 'merciful' framing"]},
    "SUPRA": {"summary": "God's decree of predestination logically precedes his decree to permit the Fall.", "affirmations": ["Election logically prior to Fall", "Stronger sovereignty emphasis"]},
    "DOM": {"summary": "Dominican spirituality: contemplata aliis tradere; truth, preaching, intellectual apostolate.", "affirmations": ["Contemplation ordered to preaching", "Truth is primary", "Thomism as framework"]},
    "JES": {"summary": "Jesuit spirituality: finding God in all things; discernment, adaptability, active apostolate.", "affirmations": ["Ad maiorem Dei gloriam", "Discernment of spirits central"]},
    "CARM": {"summary": "Carmelite spirituality: contemplative prayer, mystical theology, interior castle.", "affirmations": ["Prayer is essential", "Mystical union possible for all"]},
    "BENED": {"summary": "Benedictine spirituality: ora et labora, stability, liturgy of the hours.", "affirmations": ["Liturgy is source and summit", "Stability and community"]},
    "OPUS": {"summary": "Opus Dei: sanctification of ordinary work, universal call to holiness.", "affirmations": ["Work is path to holiness", "Lay faithful called to sanctity"]},
    "FRAN": {"summary": "Franciscan spirituality: poverty, simplicity, love of creation, service to poor.", "affirmations": ["Lady Poverty embraced", "Creation reveals Creator"]},
    "ORAT": {"summary": "Oratorian spirituality: pastoral gentleness, intellectual culture, liturgical beauty.", "affirmations": ["Gentleness in pastoral care", "Liturgy as school of holiness"]},
    "CHART": {"summary": "Carthusian spirituality: eremitical solitude, perpetual silence, contemplative focus.", "affirmations": ["Solitude is path to God", "Stat crux dum volvitur orbis"]},
    "CSSR": {"summary": "Redemptorist: abundant redemption, popular missions, Alphonsian moral theology.", "affirmations": ["Copiosa apud eum redemptio", "Preach to most abandoned", "Equiprobabilism"]},
    "SDB": {"summary": "Salesian: Don Bosco's preventive system, joy, youth education, Mary Help of Christians.", "affirmations": ["Education is matter of heart", "Reason, religion, loving-kindness"]},
    "CM": {"summary": "Vincentian: service to poor, clergy formation, simplicity, humility, practical charity.", "affirmations": ["Poor are our masters", "Simplicity, humility, charity", "Love in action"]},
    "CP": {"summary": "Passionist: memoria passionis, contemplation of Christ's suffering, preaching missions.", "affirmations": ["Keep memory of Passion alive", "Suffering united to Christ redeems"]},
    "OSM": {"summary": "Servite: servants of Mary, compassion at Cross, Marian devotion, Seven Holy Founders.", "affirmations": ["Stand with Mary at Cross", "Compassion as way of life"]},
    "OPRAEM": {"summary": "Norbertine: canons regular, liturgical solemnity, communal life, active-contemplative balance.", "affirmations": ["Contemplata aliis tradere", "Solemn liturgy sanctifies"]},
    "MERC": {"summary": "Mercedarian: ransom of captives, fourth vow to give life for captives, Marian devotion.", "affirmations": ["Free captive at any cost", "Mary of Mercy liberates"]},
    "PALAM": {"summary": "Palamite theology: essence-energies distinction, theosis through uncreated energies.", "affirmations": ["God's energies are participated", "Theosis is real deification"]},
    "RESSCH": {"summary": "Ressourcement Christology: Christ's concrete humanity, patristic retrieval.", "affirmations": ["Christ's humanity is central", "Chalcedon read through Cyril"]},
    "CHALMAX": {"summary": "Chalcedonian Maximalist: strict two natures, two wills, two operations.", "affirmations": ["Two natures without confusion", "Dyothelitism essential"]},
    "KENOT": {"summary": "Kenotic Christology: Philippians 2 self-emptying, Christ genuinely limited.", "affirmations": ["Christ truly emptied himself", "Solidarity with human weakness"]},
    "TRIDSAC": {"summary": "Tridentine sacramentology: ex opere operato, proper matter and form.", "affirmations": ["Sacraments confer grace ex opere operato", "Trent irreformable"]},
    "EUCHMYST": {"summary": "Eucharistic mysticism: personal encounter with Christ, adoration.", "affirmations": ["Eucharist is heart of Christian life", "Adoration deepens communion"]},
    "ULTRA": {"summary": "Ultramontanism: strong papal authority, infallibility maximally interpreted.", "affirmations": ["Pope has supreme jurisdiction everywhere"]},
    "PAPMOD": {"summary": "Moderate papalism: primacy and infallibility with episcopal collegiality.", "affirmations": ["Pope has primacy, bishops are true pastors"]},
    "PAPMIN": {"summary": "Papal minimalism: infallibility strictly and rarely applied.", "affirmations": ["Infallibility rare and narrow"]},
    "GALL": {"summary": "Gallicanism: national church autonomy, conciliar limits on pope.", "affirmations": ["National churches have autonomy"]},
    "CONCIL": {"summary": "Conciliarism: councils supreme, can limit pope in emergencies.", "affirmations": ["Council can depose erring pope"]},
    "EASTECC": {"summary": "Eastern Catholic ecclesiology: communion of churches, patriarchal structures.", "affirmations": ["Church is communion of churches"]},
    "SYNOD": {"summary": "Synodalist: synodal processes, listening, pilgrim people.", "affirmations": ["Synodality constitutive of Church"]},
    "THOMMOR": {"summary": "Thomistic natural law: acts ordered to end, virtue perfects nature.", "affirmations": ["Natural law participates in eternal law"]},
    "MANUAL": {"summary": "Manualist moral theology: systematic treatment, confession-focused.", "affirmations": ["Clear categories aid confessors"]},
    "VIRTUE": {"summary": "Virtue ethics: character, habituation, practical wisdom.", "affirmations": ["Character over isolated acts"]},
    "PROP": {"summary": "Proportionalism: weighing proportionate reasons in moral evaluation.", "affirmations": ["Proportionate reason can justify"]},
    "NEOSCH": {"summary": "Neo-scholastic rigorism: strict manual tradition, moral absolutes.", "affirmations": ["Moral absolutes admit no exceptions"]},
    "CASUIST": {"summary": "Casuistry: case-based moral reasoning, practical wisdom.", "affirmations": ["Cases illuminate principles"]},
    "PROBAB": {"summary": "In doubtful moral cases, one may follow a solidly probable opinion favoring liberty.", "affirmations": ["Probable opinions can be followed", "Liberty in doubt"]},
    "TUTIOR": {"summary": "In doubtful cases, one must follow the safer (tutior) opinion favoring the law.", "affirmations": ["Safer opinion must be followed", "Strictness in doubt"]},
    "INTEG": {"summary": "The state should acknowledge and support the true religion; no strict separation of church and state.", "affirmations": ["Christ's kingship extends to political order", "Religious neutrality is impossible"]},
    "LIBCATH": {"summary": "Liberal Catholicism: dialogue with modernity, religious freedom.", "affirmations": ["Dignitatis Humanae is development"]},
    "DISTRIBUT": {"summary": "Wide distribution of productive property; neither capitalism nor socialism; subsidiarity central.", "affirmations": ["Property ownership should be widespread", "Against concentrated economic power"]},
    "CORPCATH": {"summary": "Corporatist/solidarist model: organized vocational groups mediate between state and individual.", "affirmations": ["Guilds/corporations structure economy", "Class cooperation over conflict"]},
    "SOCDEM": {"summary": "Catholic social democracy: welfare state, workers protections.", "affirmations": ["State has role in justice"]},
    "LIBERTAR": {"summary": "Catholic libertarianism: free markets, minimal state.", "affirmations": ["Economic freedom is right"]},
    "TRADNAT": {"summary": "Synthesis of Catholic tradition with national/ethnic identity; skeptical of globalism.", "affirmations": ["Nations are natural communities", "Borders and culture worth preserving"]},
    "CATHUNIV": {"summary": "Emphasis on Church's universal mission transcending national boundaries.", "affirmations": ["Gospel transcends ethnicity", "International solidarity"]},
    "WORKERCATH": {"summary": "Strong emphasis on workers' rights, unions, just wages, and dignity of labor.", "affirmations": ["Living wage is moral requirement", "Unions are natural right"]},
    "AGRAR": {"summary": "Catholic agrarianism: rural life ideal, distributed land.", "affirmations": ["Land is proper basis of economy"]},
    "TRAD": {"summary": "Traditionalist: traditional liturgy, doctrine, discipline.", "affirmations": ["Traditional Latin Mass normative"]},
    "ROTR": {"summary": "Reform of the Reform: improve Novus Ordo with traditional elements.", "affirmations": ["Novus Ordo can be reverent"]},
    "PROG": {"summary": "Progressive Catholic: ongoing reform, pastoral accompaniment.", "affirmations": ["Church must continually reform"]},
    "RESS": {"summary": "Ressourcement: return to patristic and biblical sources.", "affirmations": ["Fathers are primary sources"]},
    "STD": {"summary": "Mainstream Catholic without strong identification with any particular school.", "affirmations": ["Loyalty to Magisterium", "Balance of traditions"]},
    "SSPX": {"summary": "Traditionalist resistance to post-conciliar changes while typically maintaining papal legitimacy.", "affirmations": ["Vatican II contains errors/ambiguities", "Traditional Mass normative"]},
    "SEDE": {"summary": "Sedevacantist: the See is vacant; post-1958 claimants are not true popes.", "affirmations": ["No valid pope since Pius XII", "Vatican II invalid"]},
    "ANTIMOD": {"summary": "Emphasis on Pascendi, Lamentabili, anti-Modernist oath; suspicious of post-conciliar updating.", "affirmations": ["Modernism is synthesis of all heresies", "Anti-Modernist oath should be restored", "Aggiornamento was disaster"]},
    "DEVPROG": {"summary": "Newman-style development of doctrine; organic growth from seminal principles; neither rigid nor rupturist.", "affirmations": ["Doctrine develops organically", "Later definitions make explicit what was implicit", "Development is not corruption"]},
    "COMMUN": {"summary": "Communio school: Balthasar, Ratzinger, de Lubac; ecclesiology of communion, Christocentric focus.", "affirmations": ["Church is communion of persons", "Christocentrism integrates all theology", "Ressourcement and aggiornamento balance"]},
    "RADORTH": {"summary": "Radical Orthodoxy (Milbank, Pickstock); critique of secular modernity, participatory ontology.", "affirmations": ["Secular reason is heretical", "All truth participates in divine truth", "Modernity must be narrated theologically"]},
    "TRADUM": {"summary": "Traditional preferences within Traditionis Custodes restrictions; obedient but grieving; hopes for restoration.", "affirmations": ["Obedience to Pope even when painful", "TLM will eventually be freed", "Work within system for reform"]},
    "REFORM": {"summary": "Reformed: TULIP soteriology, covenant theology, sola fide/sola scriptura, Westminster standards.", "affirmations": ["Total depravity", "Unconditional election", "Limited atonement", "Irresistible grace", "Perseverance of saints", "Forensic justification"]},
    "LUTHERAN": {"summary": "Lutheran: Law-Gospel distinction, forensic justification, sacramental realism, two kingdoms, Book of Concord.", "affirmations": ["Justification by faith alone", "Simul iustus et peccator", "Real presence (sacramental union)", "Law-Gospel hermeneutic"]},
    "ANGLICAN": {"summary": "Anglican: Via media, Prayer Book tradition, episcopal polity, Reformed Catholic synthesis, comprehensiveness.", "affirmations": ["Scripture, tradition, reason", "Episcopal apostolic succession", "Real presence (various views)", "Justification by faith (Article XI)"]},
    "NOMIN": {"summary": "Universals are names/concepts only; reality consists of particulars. Associated with Ockham.", "affirmations": ["Universals don't exist in re", "Parsimony in metaphysical commitments"]},
    "ORTHOPH": {"summary": "Strong Eastern Orthodox sympathies; values Orthodox liturgy, theology, and spirituality while remaining Catholic.", "affirmations": ["Orthodoxy preserved much the West lost", "Palamite theology is valuable", "Filioque is negotiable"]},
    "NEOPLAT": {"summary": "Christian Neo-Platonism: participatory metaphysics, divine ideas, ascent of soul.", "affirmations": ["Reality participates in divine forms", "Beauty leads to Beautiful itself"]},
    "TRANSIG": {"summary": "Open to transignification/transfinalisation language as complementary to transubstantiation.", "affirmations": ["Meaning and purpose truly change", "Phenomenological categories can illuminate"]},
    "BANEZ": {"summary": "Dominican school emphasizing physical premotion and intrinsically efficacious grace.", "affirmations": ["God physically premoves the will", "Predestination ante praevisa merita"]},
    "EASTSAC": {"summary": "Eastern sacramental: mystery emphasis, epiclesis, theosis orientation.", "affirmations": ["Sacraments are holy mysteries", "Liturgy is heaven on earth"]},
    "THOMMETA": {"summary": "Thomistic realism: act-potency, matter-form, being as analogical.", "affirmations": ["Being is analogical", "Aristotelian categories serve theology"]},
    "ORDINAR": {"summary": "Anglican patrimony within Catholicism; Divine Worship liturgy, English choral tradition, married priesthood exception.", "affirmations": ["Anglican patrimony enriches Catholicism", "Divine Worship is legitimate liturgical expression", "Vernacular solemnity is possible"]},
    "JANS": {"summary": "Jansenist (Pascal, Arnauld): strict Augustinian within Trent; efficacious grace, moral rigorism, infrequent communion, anti-Molinist.", "affirmations": ["Efficacious grace alone saves", "Infused righteousness (per Trent)", "Few are saved", "Worthy communion is rare", "Tutiorist moral approach"]},
    "PERSMOR": {"summary": "Personalist moral: dignity of person, conscience emphasized.", "affirmations": ["Person never merely a means"]},
    "ECUMON": {"summary": "Catholics open to dialogue on Protestant soteriology; sees possible convergence on grace.", "affirmations": ["Augustinian heritage is shared", "Sola fide can be understood orthodoxly", "Dialogue advances truth"]},
    "OCSO": {"summary": "Cistercian/Trappist: strict Benedictine observance, silence, manual labor, contemplative depth.", "affirmations": ["Silence speaks to God", "Labor is prayer", "Simplicity leads to God"]},
    "EORTHO": {"summary": "Eastern Orthodox: Seven Ecumenical Councils, essence-energies distinction, theosis, rejection of papal supremacy and filioque, Divine Liturgy.", "affirmations": ["Nicene Creed without filioque", "Essence-energies distinction", "Theosis as salvation", "Conciliar authority over papal", "Mystery over scholastic precision"]},
    "INTELL": {"summary": "Divine intellect is primary; God wills things because they are good, not vice versa.", "affirmations": ["Goodness is prior to divine willing", "Natural law reflects eternal reason"]},
    "SCOT": {"summary": "Franciscan school of Duns Scotus: primacy of will, univocity of being, absolute primacy of Christ.", "affirmations": ["Being is univocal", "Will is primary faculty", "Incarnation independent of Fall"]},
    "INTEGSOFT": {"summary": "Moderate integralism: state should favor true religion but with prudential tolerance.", "affirmations": ["Prudential tolerance in pluralist contexts", "Gradual cultural transformation"]},
};

const SCHOOL_FIGURES = {
    "AUG": { figure: "St. Augustine of Hippo", era: "354–430", bio: "Bishop, Doctor of Grace, and philosophical theologian. Born in North Africa to St. Monica, his dramatic conversion (Confessions VIII) from Manichaeism transformed Western Christianity. His anti-Pelagian works (De Gratia et Libero Arbitrio, De Praedestinatione Sanctorum) defined Catholic teaching on grace, original sin, and predestination. Influence spans Catholic, Orthodox, and Protestant traditions.", works: "Confessions, City of God, On Grace and Free Will" },
    "AUGP": { figure: "Prosper of Aquitaine", era: "c. 390–455", bio: "Lay theologian and defender of Augustine's strict predestinarian views against Semi-Pelagians.", works: "The Call of All Nations, Grace and Free Will" },
    "NEOAUG": { figure: "Henri de Lubac, S.J.", era: "1896–1991", bio: "French Jesuit whose ressourcement theology recovered patristic and Augustinian themes.", works: "Surnaturel, Catholicism, The Mystery of the Supernatural" },
    "JANS": { figure: "Blaise Pascal", era: "1623–1662", bio: "French mathematician and philosopher associated with Port-Royal who defended Jansenist theology.", works: "Pensées, Provincial Letters" },
    "THOM": { figure: "St. Thomas Aquinas", era: "1225–1274", bio: "The Angelic Doctor whose synthesis of Aristotelian philosophy and Christian theology became the Church's preferred framework.", works: "Summa Theologiae, Summa Contra Gentiles" },
    "BANEZ": { figure: "Domingo Báñez, O.P.", era: "1528–1604", bio: "Spanish Dominican who developed the theory of physical premotion.", works: "Scholastic Commentaries on the Summa" },
    "MOL": { figure: "Luis de Molina, S.J.", era: "1535–1600", bio: "Spanish Jesuit who developed middle knowledge (scientia media) to reconcile divine sovereignty with human freedom.", works: "Concordia" },
    "SCOT": { figure: "Bl. John Duns Scotus", era: "c. 1266–1308", bio: "The Subtle Doctor who championed univocity of being, primacy of will, and absolute primacy of Christ.", works: "Ordinatio, Quodlibetal Questions" },
    "FRANC": { figure: "St. Bonaventure", era: "1221–1274", bio: "Seraphic Doctor whose mystical-affective theology emphasized Christ as the center of all knowledge.", works: "The Soul's Journey into God, Breviloquium" },
    "INFRA": { figure: "Francisco Suárez, S.J.", era: "1548–1617", bio: "Spanish Jesuit whose infralapsarian scheme influenced Catholic and Reformed discussions.", works: "Disputationes Metaphysicae" },
    "SUPRA": { figure: "Gottschalk of Orbais", era: "c. 808–867", bio: "Medieval monk whose strict double predestination was condemned but influenced later debates.", works: "Confessio Prolixior (fragments)" },
    "DOM": { figure: "St. Dominic de Guzmán", era: "1170–1221", bio: "Founder of the Order of Preachers dedicated to contemplation, study, and preaching.", works: "Dominican Constitutions" },
    "JES": { figure: "St. Ignatius of Loyola", era: "1491–1556", bio: "Founder of the Society of Jesus emphasizing discernment and finding God in all things.", works: "Spiritual Exercises, Autobiography" },
    "CARM": { figure: "St. Teresa of Ávila", era: "1515–1582", bio: "Doctor of the Church and Carmelite reformer whose writings on contemplative prayer remain unsurpassed.", works: "Interior Castle, The Way of Perfection" },
    "BENED": { figure: "St. Benedict of Nursia", era: "c. 480–547", bio: "Father of Western Monasticism whose Rule established ora et labora.", works: "Rule of St. Benedict" },
    "OPUS": { figure: "St. Josemaría Escrivá", era: "1902–1975", bio: "Founder of Opus Dei emphasizing sanctification of ordinary work.", works: "The Way, Christ Is Passing By" },
    "FRAN": { figure: "St. Francis of Assisi", era: "1181–1226", bio: "Founder of the Franciscan Order whose radical poverty renewed the medieval Church.", works: "Canticle of the Sun, Testament" },
    "ORAT": { figure: "St. Philip Neri", era: "1515–1595", bio: "Apostle of Rome and founder of the Oratory known for joyful spirituality.", works: "Maxims and Sayings" },
    "CHART": { figure: "St. Bruno of Cologne", era: "c. 1030–1101", bio: "Founder of the Carthusian Order dedicated to eremitical contemplation.", works: "Letters" },
    "OCSO": { figure: "St. Bernard of Clairvaux", era: "1090–1153", bio: "Doctor of the Church and Cistercian abbot whose mystical writings shaped medieval spirituality.", works: "Sermons on Song of Songs, On Loving God" },
    "CSSR": { figure: "St. Alphonsus Liguori", era: "1696–1787", bio: "Founder of Redemptorists and Doctor of Moral Theology who developed equiprobabilism.", works: "Moral Theology, The Glories of Mary" },
    "SDB": { figure: "St. John Bosco", era: "1815–1888", bio: "Founder of the Salesians dedicated to youth education through the Preventive System.", works: "Memoirs of the Oratory" },
    "CM": { figure: "St. Vincent de Paul", era: "1581–1660", bio: "Founder of the Vincentians dedicated to serving the poor and forming clergy.", works: "Correspondence, Conferences" },
    "CP": { figure: "St. Paul of the Cross", era: "1694–1775", bio: "Founder of the Passionists dedicated to preaching the Passion of Christ.", works: "Letters, Spiritual Diary" },
    "OSM": { figure: "The Seven Holy Founders", era: "13th century", bio: "Seven Florentine merchants who founded the Servite Order devoted to Mary's sorrows.", works: "Servite Constitutions" },
    "OPRAEM": { figure: "St. Norbert of Xanten", era: "c. 1080–1134", bio: "Founder of the Premonstratensian Canons combining contemplative life with active ministry.", works: "Known through hagiography" },
    "MERC": { figure: "St. Peter Nolasco", era: "c. 1189–1256", bio: "Founder of the Mercedarians dedicated to ransoming Christian captives.", works: "Mercedarian Constitutions" },
    "NEOPLAT": { figure: "Pseudo-Dionysius", era: "c. 5th–6th century", bio: "Anonymous author whose mystical theology profoundly influenced Eastern and Western Christianity.", works: "Divine Names, Mystical Theology" },
    "THOMMETA": { figure: "Étienne Gilson", era: "1884–1978", bio: "French philosopher who championed Thomistic realism and the philosophy of being.", works: "The Spirit of Medieval Philosophy" },
    "NOMIN": { figure: "William of Ockham", era: "c. 1287–1347", bio: "Franciscan friar whose nominalism challenged realist metaphysics.", works: "Summa Logicae" },
    "INTELL": { figure: "St. Thomas Aquinas", era: "1225–1274", bio: "Defender of intellectualism: the will follows the intellect's presentation of the good.", works: "Summa Theologiae I-II" },
    "PALAM": { figure: "St. Gregory Palamas", era: "1296–1359", bio: "Byzantine theologian who defended the essence-energies distinction and theosis.", works: "The Triads" },
    "RESSCH": { figure: "Hans Urs von Balthasar", era: "1905–1988", bio: "Swiss theologian whose dramatic Christology emphasized Christ as the concrete universal.", works: "The Glory of the Lord, Theo-Drama" },
    "CHALMAX": { figure: "St. Cyril of Alexandria", era: "c. 376–444", bio: "Patriarch and Doctor whose Christology emphasized the unity of Christ's person.", works: "On the Unity of Christ" },
    "KENOT": { figure: "Sergei Bulgakov", era: "1871–1944", bio: "Russian Orthodox theologian whose kenotic Sophiology explored divine self-emptying.", works: "The Lamb of God" },
    "TRIDSAC": { figure: "St. Charles Borromeo", era: "1538–1584", bio: "Cardinal Archbishop who implemented Tridentine reforms with attention to sacramental discipline.", works: "Acts of the Church of Milan" },
    "EASTSAC": { figure: "St. John Chrysostom", era: "c. 349–407", bio: "Doctor whose liturgy and sacramental theology shaped Eastern practice.", works: "On the Priesthood, Divine Liturgy" },
    "TRANSIG": { figure: "Edward Schillebeeckx, O.P.", era: "1914–2009", bio: "Belgian Dominican who explored transignification as a complement to transubstantiation.", works: "The Eucharist" },
    "EUCHMYST": { figure: "St. John of the Cross", era: "1542–1591", bio: "Doctor of Mystical Theology who emphasized Eucharistic union with Christ.", works: "Ascent of Mount Carmel, Dark Night" },
    "ULTRA": { figure: "Joseph de Maistre", era: "1753–1821", bio: "Counter-revolutionary thinker who championed absolute papal authority.", works: "The Pope" },
    "PAPMOD": { figure: "St. John Henry Newman", era: "1801–1890", bio: "Cardinal whose balanced ecclesiology affirmed papal authority while respecting conscience.", works: "Essay on Development, Letter to Duke of Norfolk" },
    "PAPMIN": { figure: "Johann Adam Möhler", era: "1796–1838", bio: "German theologian who emphasized the organic nature of the Church.", works: "Unity in the Church, Symbolism" },
    "GALL": { figure: "Jacques-Bénigne Bossuet", era: "1627–1704", bio: "French bishop who defended Gallican liberties while remaining Catholic.", works: "Declaration of the Gallican Clergy" },
    "CONCIL": { figure: "Jean Gerson", era: "1363–1429", bio: "Chancellor of Paris who advocated conciliar authority during the Western Schism.", works: "On Ecclesiastical Power" },
    "EASTECC": { figure: "Metropolitan Andrey Sheptytsky", era: "1865–1944", bio: "Ukrainian Greek Catholic leader who preserved Eastern traditions within Catholic communion.", works: "Pastoral Letters" },
    "SYNOD": { figure: "Cardinal Walter Kasper", era: "1933–present", bio: "German Cardinal whose ecclesiology emphasizes synodality and local church.", works: "The Catholic Church" },
    "THOMMOR": { figure: "St. Thomas Aquinas", era: "1225–1274", bio: "Developed natural law ethics grounded in human nature's orientation toward the good.", works: "Summa Theologiae I-II, q. 90-108" },
    "MANUAL": { figure: "Henry Davis, S.J.", era: "1866–1952", bio: "Author of a widely-used moral theology manual in the manualist tradition.", works: "Moral and Pastoral Theology" },
    "VIRTUE": { figure: "Alasdair MacIntyre", era: "1929–present", bio: "Philosopher whose recovery of virtue ethics influenced Catholic moral theology.", works: "After Virtue" },
    "PERSMOR": { figure: "St. John Paul II", era: "1920–2005", bio: "Philosopher-pope whose personalist ethics grounded moral norms in human dignity.", works: "Love and Responsibility, Veritatis Splendor" },
    "PROP": { figure: "Richard McCormick, S.J.", era: "1922–2000", bio: "American moral theologian who developed proportionalist approaches.", works: "Notes on Moral Theology" },
    "NEOSCH": { figure: "Cardinal Alfredo Ottaviani", era: "1890–1979", bio: "Prefect of the Holy Office who defended neo-scholastic theology.", works: "Various curial documents" },
    "CASUIST": { figure: "St. Alphonsus Liguori", era: "1696–1787", bio: "Doctor of Moral Theology whose casuistry sought the mean between rigorism and laxism.", works: "Theologia Moralis" },
    "PROBAB": { figure: "Bartolomé de Medina, O.P.", era: "1527–1580", bio: "Dominican who first systematically defended probabilism.", works: "Commentary on Prima Secundae" },
    "TUTIOR": { figure: "Giovanni Patuzzi, O.P.", era: "1700–1769", bio: "Dominican defender of tutiorism against probabilist laxity.", works: "Ethica Christiana" },
    "INTEG": { figure: "Pope St. Pius X", era: "1835–1914", bio: "Pope who condemned Modernism and promoted integral Catholicism.", works: "Pascendi Dominici Gregis" },
    "INTEGSOFT": { figure: "Thomas Pink", era: "Contemporary", bio: "Philosopher who defends integralism while accepting Vatican II.", works: "Articles on religious liberty" },
    "LIBCATH": { figure: "John Courtney Murray, S.J.", era: "1904–1967", bio: "American Jesuit whose work on religious liberty influenced Dignitatis Humanae.", works: "We Hold These Truths" },
    "DISTRIBUT": { figure: "G.K. Chesterton", era: "1874–1936", bio: "English writer who championed Distributism as a third way.", works: "What's Wrong with the World" },
    "CORPCATH": { figure: "Heinrich Pesch, S.J.", era: "1854–1926", bio: "German Jesuit economist who developed Catholic corporatism.", works: "Lehrbuch der Nationalökonomie" },
    "SOCDEM": { figure: "Jacques Maritain", era: "1882–1973", bio: "French Thomist whose political philosophy supported Christian democracy.", works: "Integral Humanism, Man and the State" },
    "LIBERTAR": { figure: "Michael Novak", era: "1933–2017", bio: "American theologian who argued for compatibility between Catholicism and democratic capitalism.", works: "The Spirit of Democratic Capitalism" },
    "TRADNAT": { figure: "Juan Donoso Cortés", era: "1809–1853", bio: "Spanish Catholic political theorist who defended traditional order.", works: "Essay on Catholicism, Liberalism, and Socialism" },
    "CATHUNIV": { figure: "Pope Francis", era: "1936–present", bio: "Pope whose emphasis on mercy and global solidarity represents Catholic universalism.", works: "Evangelii Gaudium, Laudato Si'" },
    "WORKERCATH": { figure: "Dorothy Day", era: "1897–1980", bio: "Co-founder of the Catholic Worker Movement combining radical Catholicism with service to the poor.", works: "The Long Loneliness" },
    "AGRAR": { figure: "Hilaire Belloc", era: "1870–1953", bio: "Anglo-French writer who promoted agrarian distributism.", works: "The Servile State" },
    "TRAD": { figure: "Dietrich von Hildebrand", era: "1889–1977", bio: "Philosopher who defended traditional Catholic teaching against liturgical reform.", works: "Trojan Horse in the City of God" },
    "ROTR": { figure: "Pope Benedict XVI", era: "1927–2022", bio: "Pope whose 'reform of the reform' sought continuity while addressing abuses.", works: "The Spirit of the Liturgy" },
    "PROG": { figure: "Karl Rahner, S.J.", era: "1904–1984", bio: "German Jesuit whose transcendental Thomism shaped progressive Catholic theology.", works: "Foundations of Christian Faith" },
    "RESS": { figure: "Henri de Lubac, S.J.", era: "1896–1991", bio: "Leader of the ressourcement movement returning to patristic sources.", works: "Catholicism, The Splendor of the Church" },
    "STD": { figure: "St. John Henry Newman", era: "1801–1890", bio: "Cardinal whose thought exemplifies balanced, mainstream Catholic theology.", works: "Grammar of Assent, Parochial Sermons" },
    "SSPX": { figure: "Archbishop Marcel Lefebvre", era: "1905–1991", bio: "Founder of the Society of St. Pius X who rejected aspects of Vatican II.", works: "I Accuse the Council" },
    "SEDE": { figure: "Various Authors", era: "20th–21st c.", bio: "Sedevacantists hold the See of Peter has been vacant since Vatican II.", works: "Various sedevacantist publications" },
    "ORDINAR": { figure: "Msgr. Jeffrey Steenson", era: "1952–present", bio: "First Ordinary of the Personal Ordinariate for former Anglicans.", works: "Various addresses" },
    "ORTHOPH": { figure: "Sergei Bulgakov", era: "1871–1944", bio: "Russian Orthodox theologian whose Sophiology attracted Catholic interest.", works: "The Orthodox Church" },
    "ECUMON": { figure: "Louis Bouyer", era: "1913–2004", bio: "Lutheran convert who worked on liturgical renewal and ecumenism.", works: "The Spirit and Forms of Protestantism" },
    "ANTIMOD": { figure: "Pope St. Pius X", era: "1835–1914", bio: "Pope who issued Pascendi and the Oath Against Modernism.", works: "Pascendi Dominici Gregis" },
    "DEVPROG": { figure: "St. John Henry Newman", era: "1801–1890", bio: "His Essay on Development established criteria for distinguishing true from false development.", works: "Essay on Development of Christian Doctrine" },
    "COMMUN": { figure: "Joseph Ratzinger", era: "1927–2022", bio: "Co-founder of Communio journal advocating ressourcement over Rahnerian progressivism.", works: "Introduction to Christianity" },
    "RADORTH": { figure: "John Milbank", era: "1952–present", bio: "Anglican theologian whose Radical Orthodoxy retrieves patristic-medieval thought.", works: "Theology and Social Theory" },
    "TRADUM": { figure: "Pope Francis", era: "1936–present", bio: "Issued Traditionis Custodes restricting the 1962 Missal.", works: "Traditionis Custodes" },
    "REFORM": { figure: "John Calvin", era: "1509–1564", bio: "French Reformer whose Institutes systematized Reformed theology.", works: "Institutes of the Christian Religion" },
    "LUTHERAN": { figure: "Martin Luther", era: "1483–1546", bio: "German Reformer whose theology emphasized justification by faith alone.", works: "Small Catechism, Bondage of the Will" },
    "ANGLICAN": { figure: "Thomas Cranmer", era: "1489–1556", bio: "Archbishop of Canterbury who shaped Anglican liturgy and theology.", works: "Book of Common Prayer" },
    "EORTHO": { figure: "St. Photios the Great", era: "c. 810–893", bio: "Patriarch of Constantinople and defender of Eastern Orthodoxy.", works: "Mystagogy of the Holy Spirit" }
};

const PATRON_SAINTS = Object.fromEntries(
    Object.entries(SCHOOL_FIGURES).map(([code, data]) => [
        code, 
        { primary: [data.figure, data.era], why: data.bio }
    ])
);

const HETERODOXY_STATUS = {
    "JANS": {
        level: "condemned",
        title: "⚠️ Condemned Position",
        warning: "Jansenism was formally condemned by multiple popes (Cum Occasione, 1653; Unigenitus, 1713). Its strict predestinarianism and moral rigorism were judged contrary to Catholic teaching.",
        documents: "Cum Occasione (1653), Unigenitus (1713)",
        guidance: "While figures like Pascal offer genuine spiritual insight, the core Jansenist theological system is incompatible with Catholic orthodoxy. Read with discernment."
    },
    "SEDE": {
        level: "schismatic",
        title: "⛔ Schismatic Position",
        warning: "Sedevacantism rejects the legitimacy of post-Vatican II popes, placing adherents outside communion with the Catholic Church.",
        documents: "Canon Law on Schism, Ecclesia Dei (1988)",
        guidance: "This position is incompatible with Catholic faith. The Church cannot defect, and valid papal elections cannot be nullified by private judgment."
    },
    "PROP": {
        level: "problematic",
        title: "⚠️ Magisterially Critiqued",
        warning: "Proportionalism was critiqued by St. John Paul II in Veritatis Splendor (1993) as incompatible with the Catholic understanding of intrinsically evil acts.",
        documents: "Veritatis Splendor (1993), §§75-83",
        guidance: "While proportionate reasoning has a place in Catholic moral analysis, pure proportionalism undermines absolute moral norms."
    },
    "TRANSIG": {
        level: "caution",
        title: "⚡ Requires Clarification",
        warning: "Transignification, if proposed as a replacement for transubstantiation rather than a complement, was critiqued by Paul VI in Mysterium Fidei (1965).",
        documents: "Mysterium Fidei (1965)",
        guidance: "The Church affirms transubstantiation as the proper term. Transignification may illumine pastoral aspects but cannot replace the metaphysical reality."
    },
    "GALL": {
        level: "historical",
        title: "📜 Historically Superseded",
        warning: "Gallicanism's claims about limits on papal authority were implicitly rejected by Vatican I's definitions on papal primacy and infallibility (1870).",
        documents: "Pastor Aeternus (Vatican I, 1870)",
        guidance: "Historical Gallicanism is superseded by Vatican I. Some concerns about centralization find legitimate expression in subsidiarity."
    },
    "CONCIL": {
        level: "historical",
        title: "📜 Historically Superseded",
        warning: "Strict conciliarism—holding that councils are superior to popes—was condemned at the Fifth Lateran Council and contradicted by Vatican I.",
        documents: "Pastor Aeternus (Vatican I, 1870)",
        guidance: "While councils have great authority, the pope is not subject to conciliar judgment. Moderate views on conciliar-papal cooperation remain legitimate."
    },
    "KENOT": {
        level: "caution",
        title: "⚡ Requires Clarification",
        warning: "Extreme kenoticism can imply that Christ divested himself of divine attributes, which contradicts Chalcedonian Christology.",
        documents: "Council of Chalcedon (451)",
        guidance: "Moderate kenotic themes (Phil 2:5-11) are orthodox; extreme versions that compromise Christ's divinity are not."
    },
    "NOMIN": {
        level: "caution",
        title: "⚡ Philosophical Tension",
        warning: "Extreme nominalism undermines the analogical knowledge of God central to Catholic theology.",
        documents: "Various magisterial affirmations of analogical predication",
        guidance: "While some nominalist insights are valuable, pure nominalism is difficult to reconcile with Catholic metaphysics and sacramental realism."
    },
    "SUPRA": {
        level: "caution",
        title: "⚡ Requires Qualification",
        warning: "Strict supralapsarianism, especially in its double predestination form, approaches positions condemned in Jansenism.",
        documents: "Council of Orange (529), Council of Trent",
        guidance: "Catholic theology affirms predestination to glory but not predestination to damnation. Supralapsarian language requires careful qualification."
    },
    "SSPX": {
        level: "irregular",
        title: "⚠️ Canonically Irregular",
        warning: "The SSPX's episcopal consecrations without papal mandate (1988) incurred excommunication (later lifted). The Society remains canonically irregular.",
        documents: "Ecclesia Dei (1988), 2009 Decree",
        guidance: "While the SSPX preserves many traditional practices, their canonical situation is irregular and sacraments involve complications."
    },
    "LIBCATH": {
        level: "caution",
        title: "⚡ Wide Spectrum",
        warning: "Some forms of liberal Catholicism accommodate positions contrary to Church teaching. The label covers a wide spectrum from legitimate development to heterodoxy.",
        documents: "Various encyclicals on modernism",
        guidance: "Distinguish legitimate development from accommodation to secular ideology. Vatican II's Gaudium et Spes offers balanced engagement with modernity."
    },
    "REFORM": {
        level: "non-catholic",
        title: "✝️ Non-Catholic Tradition",
        warning: "Reformed theology represents a Protestant tradition with substantial disagreements with Catholic teaching on justification, sacraments, and ecclesiology.",
        documents: "Council of Trent, Joint Declaration (1999)",
        guidance: "Study Reformed thought for ecumenical understanding, but recognize its incompatibility with Catholic doctrine on key points."
    },
    "LUTHERAN": {
        level: "non-catholic",
        title: "✝️ Non-Catholic Tradition",
        warning: "Lutheran theology, while closer to Catholicism than other Protestant traditions, differs on justification, the Mass, and papal authority.",
        documents: "Council of Trent, Joint Declaration (1999)",
        guidance: "The Joint Declaration represents significant convergence, but real differences remain."
    },
    "ANGLICAN": {
        level: "non-catholic",
        title: "✝️ Non-Catholic Tradition",
        warning: "Anglicanism spans from Catholic-leaning Anglo-Catholicism to evangelical Protestantism. Apostolicae Curae (1896) declared Anglican orders invalid.",
        documents: "Apostolicae Curae (1896)",
        guidance: "Anglo-Catholic spirituality has much to offer, but Anglicanism is not in communion with Rome."
    },
    "EORTHO": {
        level: "non-catholic",
        title: "☦️ Orthodox (Not in Full Communion)",
        warning: "Eastern Orthodoxy shares apostolic succession and valid sacraments but is not in full communion with Rome due to the 1054 schism.",
        documents: "Unitatis Redintegratio",
        guidance: "Orthodox theology is a treasure for Catholics. The differences (papal primacy, filioque) are real but the traditions are close."
    }
};

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

const AXIS_ENDPOINTS = {"GRACE": ["Synergistic", "Monergistic"], "PAPAL": ["Conciliar/Local", "Ultramontane"], "LIT": ["Reformist", "Traditional"], "RIGOR": ["Pastoral/Lenient", "Rigorist"], "PIETY": ["Lower Intensity", "High Contemplative"], "SCRIPT": ["Magisterium-first", "Scripture-first"], "JUST": ["Forensic emphasis", "Participatory/union"], "ESCH": ["This-world focus", "Judgment & beatific end"]};

const AXIS_MULTIPLIER = {"GRACE": 3, "PAPAL": 3, "LIT": 3, "RIGOR": 3, "PIETY": 3, "SCRIPT": 4, "JUST": 4, "ESCH": 4};

const CATEGORIES = [
    { id: "scripture", name: "Scripture & Hermeneutics", shortName: "Scripture", icon: "📖", questions: [0, 1, 2, 3, 4] },
    { id: "metaphysics", name: "Metaphysics & Philosophy", shortName: "Metaphysics", icon: "🔮", questions: [5, 6, 7, 8, 9] },
    { id: "christology", name: "Christology & Soteriology", shortName: "Christology", icon: "✝️", questions: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19] },
    { id: "grace", name: "Grace & Predestination", shortName: "Grace", icon: "✨", questions: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36] },
    { id: "sacraments", name: "Sacramental Theology", shortName: "Sacraments", icon: "🍷", questions: [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48] },
    { id: "ecclesiology", name: "Ecclesiology & Authority", shortName: "Ecclesiology", icon: "⛪", questions: [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62] },
    { id: "moral", name: "Moral Theology", shortName: "Moral", icon: "⚖️", questions: [63, 64, 65, 66, 67] },
    { id: "orders", name: "Religious Orders & Spirituality", shortName: "Orders", icon: "🕯️", questions: [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80] },
    { id: "political", name: "Political & Social", shortName: "Political", icon: "🏛️", questions: [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91] },
    { id: "contemporary", name: "Contemporary Debates", shortName: "Contemporary", icon: "📰", questions: [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133] }
];

const QUESTIONS = [
    {
        "text": "Which approach best describes how Scripture should normally be interpreted in theology and preaching?",
        "options": [
            ["Patristic exegesis (literal + spiritual senses) should normally govern; historical criticism is secondary and constrained. (Ressourcement, Neo-Augustinian)", {"RESS": 3, "NEOAUG": 2, "AUG": 2, "BENED": 2, "TRAD": 2, "NEOPLAT": 1}],
            ["Historical-grammatical meaning is primary; spiritual senses are real but must be controlled by the literal sense. (Thomist, Dominican)", {"THOM": 3, "DOM": 2, "THOMMETA": 1, "STD": 2}],
            ["Historical-critical methods are useful and often necessary, but must be disciplined by dogma and the Church's rule of faith. (Moderate Papalist, Ressourcement)", {"PAPMOD": 2, "RESS": 2, "STD": 2, "JES": 2, "NEOAUG": 1}],
            ["The text's meaning is best read through contemporary experience and community reception. (Progressive, Personalist)", {"PROG": 3, "PERSMOR": 2, "LIBCATH": 1}]
        ],
        "axis_weights": {"SCRIPT": 3}
    },
    {
        "text": "Which Bible translation posture best serves the Church?",
        "options": [
            ["Liturgical stability and doctrinal continuity: a formal, traditional Catholic translation style. (Benedictine, Traditionalist)", {"BENED": 3, "TRAD": 2, "TRIDSAC": 2, "NEOSCH": 1, "ROTR": 1}],
            ["Critical-text precision: modern scholarly editions are valuable so long as doctrine governs interpretation. (Dominican, Thomist)", {"DOM": 2, "THOM": 2, "JES": 2, "PAPMOD": 1, "STD": 2}],
            ["Pastoral accessibility: clarity for modern readers is the priority. (Progressive, Personalist)", {"PROG": 2, "PERSMOR": 2, "LIBCATH": 1, "STD": 1}],
            ["Different translations for different uses (liturgy vs study vs devotion). (Mainstream)", {"STD": 3, "RESS": 1, "PAPMOD": 1}]
        ],
        "axis_weights": {"SCRIPT": 2, "LIT": 1}
    },
    {
        "text": "Scripture's literal and spiritual senses:",
        "options": [
            ["Literal foundational; spiritual senses controlled by it. (Thomist, Dominican)", {"THOM": 3, "DOM": 2, "THOMMETA": 1, "STD": 1}],
            ["Spiritual senses reveal deepest meaning; Fathers normative. (Ressourcement, Neo-Augustinian)", {"RESS": 3, "NEOAUG": 3, "NEOPLAT": 2, "BENED": 2, "ORAT": 1}],
            ["Historical-critical establishes literal; spiritual is devotional. (Progressive, Liberal Catholic)", {"PROG": 2, "LIBCATH": 2, "JES": 1}],
            ["All four senses work together; Scripture inexhaustibly rich. (Benedictine, Mainstream)", {"BENED": 2, "STD": 2, "PAPMOD": 1, "EASTECC": 1}]
        ],
        "axis_weights": {"SCRIPT": 3}
    },
    {
        "text": "What is your opinion on the 'hermeneutic of continuity' proposed by Benedict XVI?",
        "options": [
            ["Essential and correct. Vatican II must be read in continuity with all prior councils. (Communio School, Reform of Reform)", {"COMMUN": 5, "ROTR": 5, "DEVPROG": 4, "TRADUM": 4, "STD": 3, "BENED": 3}],
            ["Noble attempt, but the texts themselves contain ambiguities enabling rupturist readings. (Traditionalist, Reform of Reform)", {"TRAD": 4, "ROTR": 3, "ANTIMOD": 3, "TRADUM": 3, "PAPMIN": 2}],
            ["Continuity is a fiction. Vatican II was a new beginning, and that's good. (Progressive, Liberal Catholic)", {"PROG": 5, "LIBCATH": 5, "SYNOD": 2, "COMMUN": -3, "TRAD": -5}],
            ["Partially valid but insufficient. Some texts genuinely conflict with prior magisterium. (SSPX-leaning, Sedevacantist)", {"SSPX": 5, "SEDE": 4, "TRAD": 4, "ANTIMOD": 4, "COMMUN": -2}],
            ["A pastoral strategy more than theological argument. Useful for maintaining unity. (Moderate Papalist, Mainstream)", {"PAPMOD": 3, "STD": 3, "JES": 2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "How should Latin Catholics regard the Byzantine and Eastern liturgical traditions?",
        "options": [
            ["Eastern liturgies preserved ancient forms often lost in the West. Latin Catholics can learn much from their reverence, iconography, and theological depth. (Eastern Orthodox, Eastern Liturgical)", {"EORTHO": 4, "EASTECC": 9, "ORTHOPH": 4, "RESS": 3, "BENED": 2, "TRAD": 2}],
            ["The Roman Rite is the Church's preeminent liturgy; Eastern rites are legitimate but the Latin tradition is normative and superior in precision. (Ultramontane, Traditionalist)", {"ULTRA": 4, "TRAD": 3, "NEOSCH": 3, "INTEG": 2, "EASTECC": -3, "ORTHOPH": -2}],
            ["Both traditions are apostolic and complementary. The 'two lungs' imagery of John Paul II captures the Church's need for both. (Mainstream, Moderate Papalist)", {"STD": 4, "PAPMOD": 4, "COMMUN": 3, "EASTECC": 3, "DEVPROG": 2, "BENED": 2}],
            ["Eastern Catholics should be fully Eastern, not Latinized. The Melkite and Ukrainian traditions suffered from Roman centralization. (Eastern Catholic, Eastern Liturgical)", {"EASTECC": 9, "SYNOD": 3, "PAPMIN": 2, "ULTRA": -4, "INTEG": -3}],
            ["The liturgy is the liturgy. Excessive focus on rite distinctions distracts from the essential: valid Mass, real presence, sacrifice. (Mainstream, Opus Dei)", {"STD": 3, "OPUS": 2, "JES": 2, "PROG": 2, "EASTECC": -2, "TRAD": -2}]
        ],
        "axis_weights": {"LIT": 3, "PAPAL": 1}
    },
    {
        "text": "Regarding universals (like 'humanity' or 'justice'):",
        "options": [
            ["Moderate realism: Universals exist in things as real natures (Thomist (Realist), Thomist)", {"THOMMETA": 3, "THOM": 2, "DOM": 1, "INTELL": 1}],
            ["Nominalism: Universals are only names/mental concepts; only particulars exist", {"NOMIN": 4}],
            ["Platonic/Participatory: Universals exist primarily in the divine mind; things participate (Neo-Platonist, Augustinian)", {"NEOPLAT": 3, "AUG": 2, "FRANC": 1}],
            ["Scotist: Universals have a 'formal distinction'—less than real but more than nominal", {"SCOT": 5}]
        ],
        "axis_weights": {}
    },
    {
        "text": "What is the best framework for understanding being?",
        "options": [
            ["Analogy of being (Analogia Entis): Being is predicated analogically between God and creatures—neither univocally nor equivocally, but proportionally. (Thomist, Thomist (Realist))", {"THOMMETA": 5, "THOM": 4, "DOM": 2, "INTELL": 2}],
            ["Univocity of being: Being is predicated in the same fundamental sense of God and creatures, though infinitely different in mode and perfection. (Scotist)", {"SCOT": 9, "FRANC": 2}],
            ["Participatory/Emanation: Creatures participate in or emanate from divine being through a hierarchy of degrees; emphasis on return to the One. (Neo-Platonist)", {"NEOPLAT": 5, "AUG": 2, "PALAM": 2}],
            ["The question is too abstract and speculative; focus on God's revealed names and salvation history rather than metaphysical speculation. (Nominalist)", {"NOMIN": 4, "PROG": 1}]
        ],
        "axis_weights": {}
    },
    {
        "text": "In the De Auxiliis controversy between Bañezians and Molinists, you side with:",
        "options": [
            ["Bañez - physical premotion, intrinsically efficacious grace, predestination ante praevisa merita. (Bañezian)", {"BANEZ": 6, "AUGP": 4, "DOM": 3, "AUG": 3, "THOM": 3, "MOL": -5, "JES": -3}],
            ["Molina - middle knowledge, extrinsically efficacious grace, libertarian freedom preserved. (Molinist)", {"MOL": 9, "JES": 4, "SCOT": 2, "BANEZ": -5, "AUGP": -3}],
            ["Congruism - a mediating position. Grace is suited to circumstances God foresees. (Congruist)", {"MOL": 9, "JES": 2, "STD": 2}],
            ["The Church left it open. Both are permissible opinions within Catholic bounds. (Mainstream, Moderate Papalist)", {"STD": 4, "PAPMOD": 3, "THOM": 2, "DEVPROG": 2}],
            ["I lean Augustinian/Bañezian but wouldn't call Molinism heresy.", {"AUG": 4, "BANEZ": 3, "THOM": 3, "DOM": 2, "STD": 2}]
        ],
        "axis_weights": {"GRACE": 6}
    },
    {
        "text": "Which sacramental theology resonates most with you?",
        "options": [
            ["Strict Tridentine - ex opere operato, transubstantiation precisely defined, seven sacraments.", {"TRIDSAC": 11, "NEOSCH": 3, "TRAD": 3}],
            ["Thomistic - sacraments as instrumental efficient causes, Christ the principal cause.", {"THOM": 10, "DOM": 3, "TRIDSAC": 2}],
            ["Augustinian - emphasis on faith, interiority, sacraments as 'visible words.'", {"AUG": 13, "NEOAUG": 2}],
            ["Eastern - holy mysteries, epiclesis centrality, theosis orientation. (Eastern Sacramental)", {"EASTSAC": 6, "EASTECC": 8, "PALAM": 3, "ORTHOPH": 3}],
            ["Open to transignification language as complementary to transubstantiation.", {"TRANSIG": 5, "PROG": 3, "RESS": 2, "TRIDSAC": -3, "TRAD": -3}],
            ["Eucharistic mysticism - personal encounter, adoration, transformative union. (Eucharistic Mysticism)", {"EUCHMYST": 6, "CARM": 3, "BENED": 2, "CP": 2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "The Radical Orthodoxy movement (Milbank, Pickstock) argues that:",
        "options": [
            ["Secular reason is 'heresy' - modernity's autonomy from theology must be rejected root and branch. (Radical Orthodoxy)", {"RADORTH": 6, "INTEG": 3, "NEOPLAT": 3, "COMMUN": 2, "LIBCATH": -4}],
            ["Interesting critique of secularism but sometimes overstates the case against modernity. (Communio School, Ressourcement)", {"COMMUN": 3, "RESS": 3, "DEVPROG": 2, "STD": 2}],
            ["Too academic and obscure. Practical pastoral concerns matter more than philosophical critique. (Mainstream, Vincentian)", {"STD": 3, "CM": 2, "SDB": 2, "PROG": 2}],
            ["Essentially correct - all truth participates in divine truth. There is no 'neutral' reason. (Radical Orthodoxy, Neo-Platonist)", {"RADORTH": 5, "NEOPLAT": 4, "INTEG": 3, "THOMMETA": 2}],
            ["Dangerous flirtation with fideism. Reason has its own integrity under grace. (Thomist, Dominican)", {"THOM": 3, "DOM": 2, "JES": 2, "RADORTH": -3}]
        ],
        "axis_weights": {}
    },
    {
        "text": "The Christian life is primarily oriented toward which of the following?",
        "category": "Eschatology",
        "options": [
            ["The Beatific Vision: loving contemplation of God as final end. (Thomist, Benedictine)", {"THOM": 3, "BENED": 2, "DOM": 1, "STD": 2}],
            ["Final judgment and salvation from damnation: vigilance, penitence, and fear of the Lord. (Jansenist, Traditionalist)", {"JANS": 3, "TRAD": 2, "NEOSCH": 2, "MANUAL": 1, "TUTIOR": 1}],
            ["Theosis/deification: participation in divine life as transformative communion. (Palamite/Eastern)", {"PALAM": 4, "EASTSAC": 2, "EUCHMYST": 2, "NEOPLAT": 1, "RESS": 1}],
            ["Renewal of the world and social holiness: the Church's mission in history. (Progressive)", {"PROG": 3, "SOCDEM": 1, "WORKERCATH": 1, "PERSMOR": 1}]
        ],
        "axis_weights": {"ESCH": 4}
    },
    {
        "text": "Would the Incarnation have occurred if Adam had never sinned?",
        "options": [
            ["Yes—Christ is the absolute primacy of creation, independent of sin (Scotist)", {"SCOT": 3, "FRANC": 3, "SUPRA": 2, "CARM": 1}],
            ["No—the Incarnation was ordered primarily to redemption from sin (Thomist)", {"THOM": 3, "AUG": 2, "DOM": 1, "INFRA": 1}],
            ["Probably not, but the question is speculative (Mainstream)", {"STD": 2}],
            ["Yes, but the mode would have been different (glorious rather than suffering) (Neo-Augustinian)", {"NEOAUG": 2, "RESS": 1}]
        ],
        "axis_weights": {"GRACE": -1}
    },
    {
        "text": "How important is mental prayer in the Christian life?",
        "options": [
            ["Essential: Daily mental prayer is morally necessary for serious Christians (Carmelite, Jesuit)", {"CARM": 3, "JES": 2, "DOM": 2, "OPUS": 2}],
            ["Very important but vocal prayer and sacraments can suffice for some (Mainstream)", {"STD": 2, "BENED": 1}],
            ["Helpful but not essential; the liturgy is sufficient (Benedictine)", {"BENED": 2}],
            ["Overemphasized in some traditions; action and service matter more", {"PROG": 1}]
        ],
        "axis_weights": {"PIETY": 3}
    },
    {
        "text": "How should we understand Christ's human knowledge during His earthly life?",
        "options": [
            ["Christ possessed the beatific vision from conception, giving comprehensive knowledge. (Thomist, Chalcedonian Maximalist)", {"THOM": 5, "CHALMAX": 3, "TRIDSAC": 1, "NEOSCH": 2}],
            ["Christ's human knowledge was genuinely limited; He learned and grew authentically. (Kenotic)", {"KENOT": 4, "RESSCH": 2, "PROG": 2, "PERSMOR": 1}],
            ["Christ had infused knowledge sufficient for His mission, without unlimited knowledge. (Scotist, Franciscan School)", {"SCOT": 4, "FRANC": 2, "STD": 2}],
            ["The mystery exceeds our categories; emphasize soteriological sufficiency. (Ressourcement, Neo-Augustinian)", {"RESS": 2, "NEOAUG": 2, "RESSCH": 2, "BENED": 1}]
        ],
        "axis_weights": {"JUST": 2}
    },
    {
        "text": "The relationship between Christ's divine and human wills:",
        "options": [
            ["Two distinct wills in perfect harmony; human will freely conforms to divine. (Chalcedonian Maximalist, Thomist)", {"CHALMAX": 4, "THOM": 5, "DOM": 1}],
            ["Divine will primary, human will its instrument; unity with dyothelitism. (Ressourcement Christology, Neo-Augustinian)", {"RESSCH": 3, "NEOAUG": 2, "RESS": 2, "PALAM": 1}],
            ["Christ's human will genuinely struggled before conforming; soteriologically important. (Kenotic)", {"KENOT": 4, "RESSCH": 2, "FRANC": 2, "PERSMOR": 1}],
            ["Maximus's synthesis: natural human will always good; gnomic willing absent. (Palamite/Eastern, Eastern Catholic)", {"PALAM": 3, "EASTECC": 2, "CHALMAX": 2, "EASTSAC": 1}]
        ],
        "axis_weights": {}
    },
    {
        "text": "The 'communication of idioms' (communicatio idiomatum) means:",
        "options": [
            ["Predicates of either nature attributed to the Person, carefully avoiding mixing natures. (Chalcedonian Maximalist)", {"CHALMAX": 4, "THOM": 4, "NEOSCH": 1}],
            ["Profound exchange: 'God suffered,' 'this man is omnipotent' — Incarnation in speech. (Ressourcement Christology, Neo-Augustinian)", {"RESSCH": 3, "NEOAUG": 2, "RESS": 2, "NEOPLAT": 1}],
            ["Shows divine condescension: God truly entered human weakness and suffering. (Kenotic)", {"KENOT": 4, "FRANC": 2, "CARM": 1, "PERSMOR": 1}],
            ["Liturgically: 'O admirabile commercium' — God becomes man that man might become God. (Benedictine, Eastern Sacramental)", {"BENED": 3, "EASTSAC": 2, "EUCHMYST": 2, "TRAD": 1}]
        ],
        "axis_weights": {"LIT": 1}
    },
    {
        "text": "How did Christ's death on the Cross achieve our salvation?",
        "options": [
            ["Christ stood under the full weight of the Father's forensic wrath as one legally counted a sinner; God treated Him as if He had committed all our sins, pouring out punitive hatred upon Him in our place. (Radical Penal Substitution)", {"REFORM": 5, "LUTHERAN": 4, "SUPRA": 3, "ANGLICAN": 2}],
            ["Christ, as our innocent Surety and Guarantor, freely accepted a real abandonment by the Father—not as one hated, but as one bearing the just debt of our impieties. His sacrifice of infinite love satisfied divine justice while remaining an act of supreme charity. (Anselmian Satisfaction / Vicarious Satisfaction — Bossuet, Liguori)", {"AUG": 5, "CSSR": 5, "ORAT": 4, "THOM": 7, "BANEZ": 3, "TRIDSAC": 2, "STD": 2}],
            ["The Cross was primarily Christ's triumphant victory over the powers of sin, death, and the devil, liberating humanity from bondage and recapitulating Adam's fall through His obedience. (Christus Victor / Recapitulation)", {"RESS": 4, "PALAM": 5, "EASTECC": 4, "EORTHO": 4, "NEOAUG": 3, "BENED": 2}],
            ["The Cross is supremely the revelation of God's boundless love, designed to move our hearts to repentance and kindle a response of love in return; juridical categories are secondary or metaphorical. (Moral Influence / Exemplarist)", {"PROG": 4, "LIBCATH": 4, "PERSMOR": 3, "SDB": 2, "KENOT": 2}],
            ["The Cross is the 'Primordial Sacrament' where Christ enters into the depths of human suffering and God-forsakenness, sanctifying all human anguish and opening the path to mystical union through co-suffering. (Passionist / Mystical Solidarity)", {"CP": 5, "CARM": 4, "CM": 3, "KENOT": 3, "OSM": 2, "EUCHMYST": 2}]
        ],
        "axis_weights": {"JUST": 5, "GRACE": 3, "PIETY": 2}
    },
    {
        "text": "Which non-Catholic view of soteriology do you find most compatible with Catholic faith?",
        "options": [
            ["Lutheran - if 'faith alone' is properly understood and sacramental realism affirmed, we're close.", {"ECUMON": 11, "AUG": 3, "NEOAUG": 2, "DEVPROG": 2, "TRAD": -3}],
            ["Eastern Orthodox - patristic synthesis preserved. Theosis, synergy, mystery are deeply Catholic. (Orthophile, Palamite/Eastern)", {"ORTHOPH": 6, "PALAM": 5, "EASTECC": 4, "EASTSAC": 3, "RESS": 2, "NEOAUG": 2}],
            ["None. Extra Ecclesiam nulla salus. Protestant communities lack valid sacraments. (Traditionalist, SSPX-leaning)", {"TRAD": 5, "SSPX": 5, "NEOSCH": 4, "ANTIMOD": 3, "ECUMON": -10}],
            ["Reformed - they take grace seriously. Augustinian roots are shared.", {"AUGP": 4, "JANS": 3, "BANEZ": 2, "ECUMON": 2, "MOL": -3}],
            ["Anglican - via media, sacramental emphasis, liturgical beauty. The Ordinariate shows convergence.", {"ORDINAR": 6, "ROTR": 2, "BENED": 2, "DEVPROG": 2}]
        ],
        "axis_weights": {"GRACE": 2, "JUST": 2}
    },
    {
        "text": "'Historical Catholic soteriology (Augustine, Prosper, Isidore, Council of Orange) was essentially monergistic.' Your assessment:",
        "options": [
            ["Correct. The Fathers and Orange taught even the beginning of faith is God's gift. (Augustinian, Strict Augustinian)", {"AUG": 5, "AUGP": 3, "NEOAUG": 4, "BANEZ": 4, "ECUMON": 3, "JANS": 3, "MOL": -4}],
            ["Partially true, but 'monergism' is anachronistic. Fathers affirmed grace's priority AND cooperation. (Thomist, Mainstream)", {"THOM": 4, "STD": 3, "RESS": 3, "DEVPROG": 3, "NEOAUG": 2}],
            ["Overstated. Orange affirmed free will's role. Catholic teaching has always been synergistic. (Molinist)", {"MOL": 8, "JES": 3, "AUGP": -4, "BANEZ": -3}],
            ["Augustinian tradition was later balanced by Aquinas and Jesuits. Don't overcorrect.", {"THOM": 4, "MOL": 3, "JES": 2, "DOM": 2, "STD": 2}]
        ],
        "axis_weights": {"GRACE": 5}
    },
    {
        "text": "On the question of being - analogy (Aquinas) or univocity (Scotus)?",
        "options": [
            ["Analogy (Analogia Entis): Being is said in many ways. God and creatures share being analogically—neither identically nor equivocally, but proportionally. This preserves divine transcendence. (Thomist, Thomist (Realist))", {"THOM": 5, "THOMMETA": 6, "DOM": 3, "INTELL": 2, "SCOT": -4}],
            ["Univocity: Being must be predicated univocally for our language about God to be meaningful at all. Without a common concept, theology collapses into equivocation. (Scotist Metaphysics, Scotist)", {"SCOT": 11, "FRANC": 3, "THOMMETA": -4}],
            ["Participatory/Neoplatonic: Creatures participate in divine being through emanation and return; theological language is primarily symbolic, apophatic, and mystical rather than strictly analogical. (Neo-Platonist)", {"NEOPLAT": 5, "PALAM": 3, "AUG": 2}],
            ["Both capture important insights; the debate is often overblown by partisans. The Church has not definitively settled this metaphysical question. (Mainstream, Developmental)", {"STD": 3, "DEVPROG": 3, "RESS": 2}],
            ["Univocity opened the door to modern errors (nominalism, secularism); Analogia entis is non-negotiable for sound metaphysics and safeguarding divine transcendence. (Radical Orthodoxy, Thomist (Realist))", {"RADORTH": 5, "THOMMETA": 4, "THOM": 3, "SCOT": -3}]
        ],
        "axis_weights": {}
    },
    {
        "text": "Justification consists primarily in which of the following?",
        "category": "Grace & Justification",
        "options": [
            ["Real interior renewal through infused sanctifying grace: God makes the soul truly righteous, not merely declared so. (Thomist, Jansenist)", {"THOM": 4, "JANS": 3, "TRIDSAC": 2, "THOMMOR": 1, "DOM": 1, "STD": 2}],
            ["Real participation in Christ Himself: union with Christ is the core, with forensic language secondary. (Neo-Augustinian)", {"NEOAUG": 4, "RESS": 2, "AUG": 2, "EUCHMYST": 1, "BENED": 1, "PALAM": 1}],
            ["Primarily a forensic declaration (acquittal) with sanctification following as a distinct work. (Reformed, Lutheran)", {"REFORM": 4, "LUTHERAN": 4, "ANGLICAN": 2}],
            ["Covenantal status within the people of God; categories of 'infused habit' are less central. (Progressive)", {"PROG": 2, "PERSMOR": 1, "TRANSIG": 1, "STD": 1}]
        ],
        "axis_weights": {"JUST": 4, "GRACE": 1}
    },
    {
        "text": "After baptism, can justification increase?",
        "options": [
            ["Yes: one can truly grow in grace and righteousness (while remaining entirely dependent on grace). (Thomist, Augustinian)", {"THOM": 3, "AUG": 2, "JANS": 2, "TRIDSAC": 2, "STD": 1}],
            ["Yes, best described as deeper participation/union with Christ rather than as a 'quantity' of righteousness. (Neo-Augustinian, Ressourcement)", {"NEOAUG": 3, "RESS": 2, "AUG": 1, "PALAM": 1}],
            ["No: justification is complete as a verdict; only sanctification increases. (Reformed, Lutheran)", {"REFORM": 3, "LUTHERAN": 3, "ANGLICAN": 2}],
            ["The question is misleading; use primarily relational language. (Progressive)", {"PROG": 2, "PERSMOR": 1}]
        ],
        "axis_weights": {"JUST": 3}
    },
    {
        "text": "How are justification and sanctification related?",
        "options": [
            ["Distinct but inseparable graces: God both forgives and makes holy; separating them distorts the Gospel. (Thomist, Neo-Augustinian)", {"THOM": 2, "NEOAUG": 2, "RESS": 1, "AUG": 2, "STD": 2}],
            ["Justification is logically prior; sanctification follows as fruit, and confusing them risks works-righteousness. (Reformed, Lutheran)", {"REFORM": 3, "LUTHERAN": 3, "ANGLICAN": 4}],
            ["Union with Christ is prior: both justification and sanctification flow from participation in Christ. (Neo-Augustinian, Ressourcement)", {"NEOAUG": 3, "RESS": 2, "PALAM": 2, "EUCHMYST": 1}],
            ["Pastoral framing matters more than precise distinctions; emphasize accompaniment and growth. (Personalist, Progressive)", {"PERSMOR": 2, "PROG": 2, "LIBCATH": 1}]
        ],
        "axis_weights": {"JUST": 3}
    },
    {
        "text": "Post-baptismal concupiscence is best described as which of the following?",
        "options": [
            ["A disordered inclination that remains as a wound and penalty, but is not sin unless consented to. (Thomist, Thomist (Natural Law))", {"THOM": 3, "THOMMOR": 2, "TRIDSAC": 1, "STD": 2}],
            ["Not formally sinful (guilt/reatus removed in baptism), though materially sinful (disordered inclination). Remains \'for the contest\' (ad agonem); culpability attaches only to consent. (Augustinian, Tridentine)", {"AUG": 3, "JANS": 1, "NEOAUG": 2, "TRIDSAC": 2, "STD": 1}],
            ["In itself it is truly sin in the regenerate (even without consent), though not always imputable in the same way. (Reformed, Lutheran)", {"REFORM": 4, "LUTHERAN": 4}],
            ["Primarily a psychological phenomenon; 'sin' language should be reserved for conscious harmful choices. (Progressive, Personalist)", {"PROG": 3, "PERSMOR": 2}]
        ],
        "axis_weights": {"RIGOR": 2, "GRACE": 1}
    },
    {
        "text": "How much certainty can a Christian have about their salvation and present state of grace?",
        "options": [
            ["Not absolute certainty, but moral confidence through signs of grace, humility, and faithful sacramental life. (Thomist, Mainstream)", {"THOM": 3, "STD": 3, "PAPMOD": 1}],
            ["Hopeful trust without seeking firm assurance; fear and humility protect against presumption. (Augustinian, Traditionalist)", {"AUG": 3, "AUGP": 2, "TRAD": 1, "NEOSCH": 1}],
            ["Strong assurance is spiritually dangerous and usually presumption; emphasize penitence and the fewness of the saved. (Jansenist, Tutiorist)", {"JANS": 3, "TUTIOR": 2, "MANUAL": 1}],
            ["Interior peace from the Holy Spirit is a sufficient indicator; excessive anxiety about grace is spiritually unhealthy. (Progressive, Personalist)", {"PROG": 2, "PERSMOR": 2, "LIBCATH": 1}],
            ["The truly elect will certainly persevere; assurance is a gift of faith rooted in God's promises. (Reformed, Lutheran)", {"REFORM": 3, "LUTHERAN": 3, "ECUMON": 2}],
            ["Conditional assurance: We can know we are in grace now, but final perseverance remains uncertain and requires ongoing cooperation. (Molinist, Jesuit)", {"MOL": 3, "JES": 2, "STD": 2}]
        ],
        "axis_weights": {"JUST": 2, "ESCH": 2, "GRACE": 2}
    },
    {
        "text": "Final perseverance is best described as which of the following?",
        "options": [
            ["A special grace to be humbly prayed for; not guaranteed, but God is faithful. (Thomist, Augustinian)", {"THOM": 3, "AUG": 2, "STD": 2, "DOM": 1}],
            ["Infallibly granted to those truly predestined; the elect cannot finally fall away. (Reformed)", {"REFORM": 4, "AUGP": 2, "SUPRA": 1}],
            ["A mystery better handled pastorally than speculatively; emphasize fidelity in the present. (Moderate Papalist, Mainstream)", {"PAPMOD": 2, "STD": 2, "RESS": 1}],
            ["Assurance of salvation is central to the Gospel's comfort; excessive emphasis on uncertainty is harmful. (Progressive)", {"PROG": 2, "LIBCATH": 1, "PERSMOR": 1}]
        ],
        "axis_weights": {"GRACE": 2, "ESCH": 2}
    },
    {
        "text": "How does God's grace relate to human freedom in salvation?",
        "options": [
            ["Grace is intrinsically efficacious—it infallibly moves the will while preserving freedom (Bañezian)", {"BANEZ": 3, "THOM": 2, "DOM": 2, "AUGP": 2}],
            ["Grace is extrinsically efficacious through God's middle knowledge of free response (Molinist)", {"MOL": 4, "JES": 2}],
            ["Grace is congruous—fitted to circumstances so it will be freely accepted (Congruist)", {"MOL": 4, "JES": 1}],
            ["Grace heals and elevates nature, enabling but not determining free response (Thomist)", {"THOM": 3, "DOM": 1}],
            ["Grace is offered universally; efficacy depends wholly on human cooperation (Semi-Augustinian)", {"AUG": 2, "PROG": 1}]
        ],
        "axis_weights": {"GRACE": 2}
    },
    {
    "text": "How should we understand the decree of predestination and reprobation?",
    "options": [
        ["God actively elects some to glory and, with equal sovereignty and by a parallel act of will, positively decrees the damnation of the rest for His glory. (Symmetrical Double Predestination / Equal Ultimacy)", {"SUPRA": 5, "AUGP": 3}],
        ["God actively elects some to glory by an efficacious decree, but merely 'passes over' (preteritio) the rest, justly permitting them to fall into the end their sins deserve without a positive decree of reprobation. (Asymmetrical Double Predestination / Preterition)", {"REFORM": 4, "AUG": 4, "THOM": 2, "BANEZ": 5, "JANS": 3, "INFRA": 3}],
        ["We should only speak of God predestining the elect to salvation; the loss of the reprobate is entirely a mystery of human rejection and resistance to grace, not a divine decree. (Single Predestination)", {"LUTHERAN": 5, "ANGLICAN": 7, "STD": 3, "PROG": 2}],
        ["Predestination is grounded in God's infallible foreknowledge (scientia media) of how each person would freely cooperate with grace in any given circumstance. (Conditional / Molinist)", {"MOL": 8, "JES": 4, "AUG": 3, "STD": 1}]
    ],
    "axis_weights": {"GRACE": 5, "ESCH": 2}
},
    {
    "text": "Regarding the logical order of God's decrees about predestination and the Fall:",
    "options": [
        ["Supralapsarian: The decree of election logically precedes the decree to permit the Fall (Sovereignty emphasis).", {"SUPRA": 5, "REFORM": 3, "AUGP": 1}],
        ["Infralapsarian: The decree of election logically follows the decree to permit the Fall (Mercy emphasis).", {"INFRA": 5, "AUG": 3, "THOM": 3, "BANEZ": 4, "JANS": 2, "STD": 1}],
        ["The decree is based on God's 'Middle Knowledge' of how a person would freely respond in any given circumstance.", {"MOL": 8, "JES": 4}],
        ["These scholastic categories are overly speculative and may distort the simplicity of the Gospel.", {"STD": 3, "RESS": 2, "PROG": 2}]
    ],
    "axis_weights": {"GRACE": 3}
},
    {
        "text": "What is the nature of sufficient grace?",
        "options": [
            ["Sufficient grace gives real power to act but becomes efficacious only with God's further motion (Bañezian, Strict Thomist)", {"BANEZ": 3, "THOM": 2, "DOM": 2}],
            ["Sufficient grace becomes efficacious through human free cooperation foreseen by middle knowledge (Molinist, Jesuit)", {"MOL": 5, "JES": 2}],
            ["The distinction between sufficient and efficacious grace is largely verbal (Reformed, Lutheran)", {"REFORM": 2, "LUTHERAN": 2}],
            ["Sufficient grace truly enables, and its becoming efficacious involves genuine synergy (Semi-Augustinian)", {"AUG": 2, "THOM": 1}]
        ],
        "axis_weights": {"GRACE": 2}
    },
    {
        "text": "How do the sacraments cause grace?",
        "options": [
            ["Instrumental efficient causality—sacraments are true instruments that cause grace (Thomist Sacramental, Thomist)", {"THOM": 6, "TRIDSAC": 2}],
            ["Moral causality—sacraments move God to give grace, not physical instruments (Minimalist Sacramental)", {"TRIDSAC": 2, "SCOT": 1}],
            ["Occasional causality—God gives grace on the occasion of sacramental rites (Nominalist)", {"NOMIN": 2, "TRIDSAC": 1}],
            ["Mystical/symbolic causality—sacraments participate in and manifest grace (Eastern Sacramental, Neo-Platonist)", {"EASTSAC": 3, "NEOPLAT": 2, "AUG": 1}]
        ],
        "axis_weights": {}
    },
    {
        "text": "'Reformed and Lutheran views of justification, despite differences, are mostly compatible with some Catholic schools.' Your response:",
        "options": [
            ["Agree - Augustinian and Bañezian positions share significant common ground. JDDJ was right.", {"ECUMON": 11, "AUG": 3, "BANEZ": 1, "AUGP": 2, "NEOSCH": -4}],
            ["Partially - overlap on grace's priority exists, but merit and sacraments differ substantially. (Thomist, Mainstream)", {"THOM": 3, "STD": 3, "PAPMOD": 3, "DEVPROG": 2, "AUG": 2}],
            ["Disagree - Protestant soteriology is forensic and extrinsic. Catholic justification is real transformation. (Thomist, Tridentine)", {"THOM": 4, "TRIDSAC": 4, "NEOSCH": 4, "DOM": 3, "ECUMON": -4}],
            ["Strongly disagree - Trent definitively condemned sola fide as Protestants teach it. (Traditionalist, SSPX-leaning)", {"TRAD": 5, "SSPX": 5, "NEOSCH": 5, "ANTIMOD": 4, "ECUMON": -11}]
        ],
        "axis_weights": {"JUST": 4, "GRACE": 3}
    },
    {
        "text": "Which statement best captures your fundamental theological orientation?",
        "options": [
            ["'Grace does not destroy nature but perfects it.' The Thomistic synthesis is perennially valid.", {"THOM": 6, "DOM": 4, "THOMMETA": 4, "THOMMOR": 3}],
            ["'Our hearts are restless until they rest in Thee.' Augustine's interiority and grace theology are primary. (Augustinian)", {"AUG": 13, "NEOAUG": 4}],
            ["'Finding God in all things.' Ignatian discernment and active engagement with the world. (Jesuit)", {"JES": 6, "MOL": 5}],
            ["'Pray and work.' The Benedictine balance of liturgy, labor, and stability.", {"BENED": 6, "OCSO": 4, "OPRAEM": 3, "CHART": 2}],
            ["'Lady Poverty.' Franciscan simplicity, creation spirituality, and joyful service.", {"FRAN": 6, "FRANC": 4, "SDB": 2}],
            ["Ressourcement - return to Fathers and Scripture to renew the Church. (Ressourcement)", {"RESS": 6, "NEOAUG": 4, "COMMUN": 4, "BENED": 2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "How has papal authority developed historically, and is its current form legitimate?",
        "options": [
            ["Papal authority as exercised today is a late innovation. Haec Sancta (1415) and early conciliar practice show a more collegial original model. (Gallican, Conciliarist)", {"GALL": 5, "CONCIL": 5, "PAPMIN": 3, "PROG": 2, "ULTRA": -5, "INTEG": -4}],
            ["Newman's development of doctrine applies: the seed of papal authority was always present, growing organically to Vatican I's definition. (Developmental, Moderate Papalist)", {"DEVPROG": 5, "PAPMOD": 4, "STD": 3, "COMMUN": 3, "THOM": 2, "GALL": -3}],
            ["Papal primacy and jurisdiction were clearly exercised from the earliest centuries. Vatican I defined what was always believed and practiced. (Ultramontane, Integralist)", {"ULTRA": 5, "INTEG": 4, "NEOSCH": 3, "ANTIMOD": 2, "GALL": -4, "CONCIL": -4}],
            ["The charism is real but over-centralization is a legitimate concern. Subsidiarity should govern how papal authority is exercised in practice. (Papal Minimalist, Mainstream)", {"PAPMIN": 4, "PAPMOD": 3, "STD": 3, "SYNOD": 2, "EASTECC": 2, "ULTRA": -3}],
            ["Papal authority as currently practiced is a Western development the East never accepted. Its maximalist form is a major obstacle to reunion. (Eastern Catholic, Orthophile)", {"EASTECC": 4, "ORTHOPH": 4, "CONCIL": 3, "SYNOD": 3, "ULTRA": -4, "INTEG": -3}]
        ],
        "axis_weights": {"PAPAL": 5}
    },
    {
        "text": "Can a justified person lose salvation?",
        "options": [
            ["No: the truly elect will certainly persevere; apparent apostasy proves one was never truly saved. (Reformed)", {"REFORM": 4, "SUPRA": 2}],
            ["Yes: mortal sin destroys justifying grace, but it can be restored through penance. (Thomist, Tridentine)", {"THOM": 3, "TRIDSAC": 3, "JANS": 2, "AUG": 2, "STD": 3}],
            ["Possible but difficult: believers can fall from grace but God's preserving work is powerful. (Lutheran, Methodist)", {"LUTHERAN": 3, "ANGLICAN": 5}],
            ["The question framed wrongly: focus on God's faithfulness and our response in the present. (Progressive, Personalist)", {"PROG": 2, "PERSMOR": 2}]
        ],
        "axis_weights": {"GRACE": 3, "ESCH": 2}
    },
    {
        "text": "What role do the saints play in the Christian life?",
        "options": [
            ["Saints intercede for us; we may invoke their prayers and venerate relics and images. (Traditionalist, Tridentine)", {"TRAD": 3, "TRIDSAC": 3, "BENED": 2, "STD": 3}],
            ["Saints are examples of faith; invocation is unbiblical and borders on idolatry. (Reformed)", {"REFORM": 4, "LUTHERAN": 2}],
            ["Saints are honored as examples; limited invocation may be permissible. (Anglican, Lutheran)", {"ANGLICAN": 4, "LUTHERAN": 2}],
            ["The communion of saints includes mutual prayer; the details are mysterious. (Ressourcement, Neo-Augustinian)", {"RESS": 2, "NEOAUG": 2}]
        ],
        "axis_weights": {"PIETY": 2, "LIT": 1}
    },
    {
        "text": "How should we understand the Christological formula of Chalcedon ('two natures')?",
        "options": [
            ["Dogmatically binding: Christ has two complete natures, divine and human, without confusion or separation. (Thomist, Chalcedonian Maximalist)", {"THOM": 4, "CHALMAX": 4, "TRIDSAC": 3, "STD": 3}],
            ["Correct but the 'one nature' (miaphysite) formula of Cyril is also orthodox if properly understood. (Eastern Orthodox, Ressourcement)", {"EORTHO": 3, "RESS": 3, "RESSCH": 3, "ECUMON": 3}],
            ["Chalcedon betrayed Cyril: 'one incarnate nature of God the Word' is the authentic formula. (Coptic Orthodox, Oriental Orthodox)", {"EORTHO": 10}],
            ["The terminology matters less than confessing Christ as truly God and truly man. (Progressive, Ecumenical Monergist)", {"PROG": 3, "ECUMON": 2, "LIBCATH": 2}]
        ],
        "axis_weights": {"SCRIPT": 3}
    },
    {
        "text": "Which understanding of Christ's Eucharistic presence best reflects your view?",
        "options": [
            ["Aristotelian-Thomist Transubstantiation: The substance of bread and wine becomes Christ's Body and Blood; accidents remain. Christ is present per modum substantiae, not locally.", {"TRIDSAC": 8, "THOM": 6, "TRAD": 2, "DOM": 2}],
            ["Scotist Formal-Metaphysical Presence: Real conversion affirmed, but explained via formal distinctions and haecceity rather than strict Aristotelian substance-accident categories.", {"SCOT": 7, "FRANC": 3, "TRIDSAC": 3}],
            ["Non-Corporeal Substantial Presence: Christ is fully and truly present in substance, but not as a quantitative body in the mode of extension. Emphasizes sacramental mode of existence.", {"JES": 3, "MOL": 2, "THOM": 2, "TRIDSAC": 2, "STD": 2, "PAPMOD": 1}],
            ["Sign-Reality (Sacramentum–Res) Model: Distinguishes objective sacramental sign from spiritual union received fruitfully by faith. Augustinian sacramental theology.", {"AUG": 6, "NEOAUG": 2, "RESS": 2, "THOM": 1, "COMMUN": 2}],
            ["Veiled Objective Reality: Christ is truly present but hidden under sacramental appearances; faith pierces the veil. Patristic emphasis on mystery and invisibility.", {"TRAD": 2, "TRIDSAC": 2, "EUCHMYST": 3, "BENED": 2, "CARM": 1, "EASTSAC": 1}],
            ["Liturgical-Mystical Participation (Eastern): The Eucharist as transforming communion in the deified Christ. Less focus on metaphysical mechanism, more on participation in divine life.", {"EASTSAC": 4, "EUCHMYST": 3, "PALAM": 3, "EASTECC": 5, "EORTHO": 2}],
            ["Ratramnian Spiritual-Real Presence: Christ truly present but not in a crude bodily manner; emphasizes spiritual reality and ecclesial faith over physical identity.", {"RESS": 3, "PROG": 2, "TRANSIG": 3, "NEOAUG": 2, "LIBCATH": 1}]
        ],
        "axis_weights": {"LIT": 2}
    },
    {
        "text": "Regarding ex opere operato (sacraments work by the rite performed):",
        "options": [
            ["Strongly affirm: Grace is given by valid administration regardless of minister's holiness (Tridentine, Thomist Sacramental)", {"TRIDSAC": 3, "THOM": 5, "STD": 2}],
            ["Affirm, but recipient's disposition significantly affects fruitfulness (Thomist, Augustinian Sacramental)", {"THOM": 2, "AUG": 2, "STD": 2}],
            ["The emphasis can obscure the importance of faith and community (Progressive)", {"PROG": 2, "TRANSIG": 1}],
            ["Valid but the Eastern tradition emphasizes epiclesis and mystery over mechanism (Eastern Sacramental, Palamite/Eastern)", {"EASTSAC": 3, "PALAM": 2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "Which direction should the priest face during the Eucharistic Prayer?",
        "options": [
            ["Ad orientem (same direction as people): Expresses common worship toward God (Traditionalist, Tridentine)", {"TRAD": 3, "TRIDSAC": 3, "ROTR": 2, "SSPX": 3, "BENED": 2}],
            ["Versus populum (facing people): Emphasizes community and participation (Progressive)", {"PROG": 3}],
            ["Either is legitimate depending on circumstances (Mainstream)", {"STD": 2, "ROTR": 1}],
            ["The question is secondary to interior participation", {"RESS": 1, "CARM": 1}]
        ],
        "axis_weights": {"LIT": 3}
    },
    {
        "text": "How should Holy Communion be received?",
        "options": [
            ["On the tongue while kneeling: Traditional and most reverent (Traditionalist, Tridentine)", {"TRAD": 3, "TRIDSAC": 3, "SSPX": 3, "ROTR": 1}],
            ["On the tongue standing: Traditional but adapted (Reform of Reform)", {"ROTR": 2, "STD": 1}],
            ["In the hand is legitimate and can express lay dignity (Progressive)", {"PROG": 2}],
            ["Either way with proper reverence; interior disposition matters most (Mainstream)", {"STD": 2}]
        ],
        "axis_weights": {"LIT": 2}
    },
    {
        "text": "How should we evaluate the post-Vatican II liturgical reforms, and what direction should the liturgy take?",
        "options": [
            ["Largely mistaken: The Novus Ordo represents a break with tradition. The TLM should be normative again. (SSPX-leaning, Sedevacantist)", {"SSPX": 4, "SEDE": 3, "TRAD": 3}],
            ["Good intentions but badly implemented. A 'reform of the reform' is needed — reforming the Novus Ordo toward Sacrosanctum Concilium's actual vision, perhaps toward a reverent vernacular form inspired by the TLM and Eastern Divine Liturgy. (Reform of Reform)", {"ROTR": 5, "BENED": 3, "COMMUN": 2, "TRAD": 1}],
            ["Generally positive: The reforms made liturgy more accessible and participatory; further inculturation should continue. (Progressive)", {"PROG": 4, "LIBCATH": 2, "SYNOD": 1}],
            ["Both forms have value. The Ordinary and Extraordinary Forms should coexist peacefully as mutual enrichment. (Mainstream, Benedictine)", {"STD": 3, "BENED": 2, "PAPMOD": 2, "ROTR": 1}],
            ["The Eastern Catholic liturgies show what reverent vernacular worship looks like. The West should learn from them rather than fight over Latin vs. vernacular. (Eastern Catholic, Eastern Liturgical)", {"EASTECC": 6, "RESS": 2, "ORTHOPH": 2}]
        ],
        "axis_weights": {"LIT": 4}
    },
    {
        "text": "What is the proper place of the Traditional Latin Mass today?",
        "options": [
            ["Should be the normative form or at least freely available everywhere (Traditionalist, SSPX-leaning)", {"TRAD": 3, "SSPX": 3, "SEDE": 3, "ROTR": 2}],
            ["A legitimate option that enriches the Church's liturgical life (Reform of Reform, Mainstream)", {"ROTR": 2, "STD": 2, "BENED": 1}],
            ["Of historical interest but the reformed liturgy is the Church's lex orandi", {"PROG": 2}],
            ["Should be restricted to prevent division", {"PROG": 1}]
        ],
        "axis_weights": {"LIT": 3}
    },
    {
        "text": "What is the role of silence in the liturgy?",
        "options": [
            ["Essential: Sacred silence enables contemplation and encounter with mystery (Traditionalist, Carmelite)", {"TRAD": 3, "CARM": 2, "BENED": 2, "TRIDSAC": 2}],
            ["Important but balanced with congregational participation (Mainstream, Reform of Reform)", {"STD": 2, "ROTR": 2}],
            ["Often excessive in pre-conciliar liturgy; active participation is key (Progressive)", {"PROG": 2}],
            ["Deeply valued in Eastern liturgy as part of the mystery (Eastern Sacramental)", {"EASTSAC": 2, "PALAM": 1}]
        ],
        "axis_weights": {"LIT": 2, "PIETY": 1}
    },
    {
        "text": "How important is rubrical exactness in liturgy?",
        "options": [
            ["Very important: Rubrics protect the sacred and express theology (Traditionalist, Tridentine)", {"TRAD": 3, "TRIDSAC": 3, "MANUAL": 2, "NEOSCH": 2}],
            ["Important but not at the expense of pastoral adaptation (Mainstream)", {"STD": 2, "ROTR": 1}],
            ["Secondary: The spirit of the liturgy matters more than exact rubrics (Progressive)", {"PROG": 2, "RESS": 1}],
            ["Rubrics serve the mystery and should be followed with understanding (Benedictine)", {"BENED": 2, "THOM": 1}]
        ],
        "axis_weights": {"LIT": 2, "RIGOR": 1}
    },
    {
        "text": "How do you view Pope Francis's restrictions on the Traditional Latin Mass?",
        "options": [
            ["Necessary to prevent the TLM from becoming a flag for rejecting Vatican II. (Progressive, Liberal Catholic)", {"PROG": 4, "LIBCATH": 3, "SYNOD": 2, "ULTRA": 2, "TRAD": -5, "SSPX": -5}],
            ["Pastorally devastating. Summorum Pontificum was working. Benedict XVI was right. (Reform of Reform, Traditionalist)", {"ROTR": 5, "TRAD": 5, "BENED": 3, "TRADUM": 4, "COMMUN": 2, "PROG": -3}],
            ["An unjust suppression. I attend TLM regardless of canonical regularity. (SSPX-leaning, Traditionalist)", {"SSPX": 6, "TRAD": 5, "SEDE": 3, "ANTIMOD": 3, "ULTRA": -4, "PAPMOD": -3}],
            ["The Pope has authority to regulate liturgy. I obey even if I preferred the old policy. (TC Compliant, Ultramontane)", {"ULTRA": 4, "STD": 4, "PAPMOD": 4, "TRADUM": 5, "SSPX": -4}],
            ["Understandable concern but heavy-handed. Dialogue would have been better. (Mainstream, Reform of Reform)", {"STD": 3, "ROTR": 3, "PAPMOD": 2, "ORAT": 2, "TRADUM": 3, "DEVPROG": 2}]
        ],
        "axis_weights": {"LIT": 4, "PAPAL": 2}
    },
    {
        "text": "How does the dogma of the Immaculate Conception relate to the Augustinian doctrine of original sin and the 'massa damnata'?",
        "options": [
            ["The dogma magnificently vindicates Augustine: Mary's singular exemption proves how universal and inescapable original sin truly is—only an extraordinary divine intervention could preserve anyone from the massa damnata. (Strict Augustinian)", {"AUGP": 5, "AUG": 4, "JANS": 4, "BANEZ": 3, "TRAD": 3, "SCOT": -4, "FRANC": -4}],
            ["The Immaculate Conception represents a harmonious synthesis: Mary was preserved by grace applied in anticipation of Christ's merits, fully consistent with Augustinian hamartiology and Thomistic precision. (Thomist-Augustinian Synthesis)", {"THOM": 5, "AUG": 4, "DOM": 4, "TRIDSAC": 3, "NEOSCH": 3, "STD": 2}],
            ["Bl. Scotus rightly saw that God could, and therefore did, preserve Mary entirely from the stain of original sin from the first instant—a 'more perfect redemption' that requires softening Augustine's view of seminal transmission. (Scotist / Franciscan)", {"SCOT": 8, "FRANC": 5, "CARM": 3, "OSM": 2, "AUGP": -3, "JANS": -3}],
            ["The East honors Mary as the 'All-Holy' (Panagia) and 'Immaculate' without the Latin juridical framework of inherited guilt or 'original sin' in the Augustinian sense; both traditions affirm her supreme purity by different theological paths. (Eastern Catholic / Patristic)", {"EASTECC": 5, "PALAM": 4, "EASTSAC": 4, "ORTHOPH": 4, "EORTHO": 3, "RESS": 2, "NEOSCH": -2}],
            ["The dogma was a medieval development driven largely by popular piety and Franciscan advocacy, not strict theological necessity; Augustine's severe view of inherited guilt makes the formulation awkward and historically contingent. (Critical / Progressive)", {"PROG": 4, "LIBCATH": 4, "DEVPROG": 3, "RESS": 2, "TRAD": -4, "INTEG": -3}]
        ],
        "axis_weights": {"GRACE": 4, "PIETY": 3, "RIGOR": 2}
    },
    {
        "text": "How do you assess the Jansenist movement?",
        "options": [
            ["Authentic Augustinianism unjustly condemned due to Jesuit political maneuvering.", {"JANS": 6, "AUGP": 4, "TRAD": 2, "JES": -5, "MOL": -4}],
            ["Contained genuine insights about grace but went too far into rigorism and near-Calvinism. (Augustinian, Thomist)", {"AUG": 3, "AUGP": 2, "THOM": 3, "STD": 2}],
            ["Rightly condemned. Its rigorism harmed souls and its ecclesiology was schismatic. (Jesuit, Molinist)", {"JES": 4, "MOL": 3, "STD": 3, "PAPMOD": 2, "JANS": -5}],
            ["A complex phenomenon. Some Jansenists were holy; the label was applied too broadly.", {"RESS": 3, "DEVPROG": 2, "STD": 2, "NEOAUG": 2}]
        ],
        "axis_weights": {"GRACE": 4, "RIGOR": 3}
    },
    {
        "text": "What degree of certainty can theology achieve, and how does it relate to faith?",
        "options": [
            ["Theology is a true science with demonstrative certainty, proceeding from principles known by divine faith to conclusions known by theological reason. (Thomist, Dominican)", {"THOM": 5, "DOM": 4, "THOMMETA": 4, "NEOSCH": 3, "INTELL": 3, "NOMIN": -3}],
            ["Theology is wisdom more than science — sapiential knowledge rooted in contemplative union with God, not merely syllogistic demonstration. (Augustinian, Neo-Platonist)", {"AUG": 4, "NEOPLAT": 4, "CARM": 3, "BENED": 2, "NEOAUG": 2, "PALAM": 2}],
            ["Theological conclusions are probable opinions, not demonstrations. Only Scripture and defined dogma are certain; the rest is theological opinion. (Nominalist, Voluntarist)", {"NOMIN": 7, "SCOT": 2, "RESS": 2, "THOMMETA": -2}],
            ["Theology must be done in dialogue with contemporary philosophy and science; its 'certainties' are always culturally conditioned and revisable. (Progressive, Liberal Catholic)", {"PROG": 4, "LIBCATH": 3, "PERSMOR": 2, "RADORTH": -3, "NEOSCH": -3}],
            ["The Eastern tradition emphasizes apophatic theology — God is known through what He is not. Western 'certainty' can become rationalist presumption. (Palamite/Eastern, Eastern Orthodox)", {"PALAM": 5, "EORTHO": 4, "EASTECC": 4, "ORTHOPH": 3, "NEOPLAT": 2, "THOMMETA": -2}]
        ],
        "axis_weights": {"SCRIPT": 2}
    },
    {
        "text": "How would you rank the normative authority of Scripture, Tradition, and the Magisterium?",
        "category": "Scripture & Tradition",
        "options": [
            ["Scripture has the highest dignity and is the supreme norm, but only as read within apostolic Tradition and the Church's infallible teaching. (Neo-Augustinian, Ressourcement)", {"NEOAUG": 4, "RESS": 3, "AUG": 2, "BENED": 1, "ORAT": 1, "STD": 2}],
            ["Scripture and Tradition are co-equal fonts of revelation, while the Magisterium is their authoritative interpreter and guardian. (Thomist, Thomist (Realist))", {"THOM": 3, "THOMMETA": 2, "TRIDSAC": 1, "PAPMOD": 2, "STD": 2, "DOM": 1}],
            ["In practice, the Magisterium is the proximate rule of faith; Scripture and Tradition are received through that living authority. (Ultramontane)", {"ULTRA": 4, "PAPMOD": 2, "INTEG": 2, "NEOSCH": 1}],
            ["The hierarchy can err widely in non-definitive matters; Scripture and the Fathers supply the main corrective. (SSPX-leaning, Traditionalist)", {"SSPX": 3, "TRAD": 2, "ROTR": 1, "NEOAUG": 1, "PAPMIN": 1}]
        ],
        "axis_weights": {"SCRIPT": 4}
    },
    {
        "text": "What is the proper understanding of papal authority, primacy, and infallibility?",
        "options": [
            ["Full, immediate, ordinary jurisdiction over the entire Church; the ordinary magisterium shares in a broad practical infallibility. (Ultramontane, Integralist)", {"ULTRA": 4, "INTEG": 3, "NEOSCH": 2}],
            ["Real primacy with ordinary jurisdiction, exercised with restraint; infallibility is rare but the ordinary magisterium binds seriously. (Moderate Papalist, Mainstream)", {"PAPMOD": 4, "STD": 3, "DEVPROG": 2}],
            ["Primacy of honor with jurisdiction of final appeal; infallibility is strictly and rarely applied to ex cathedra definitions only. (Papal Minimalist)", {"PAPMIN": 4, "GALL": 2, "EASTECC": 2}],
            ["Conciliar authority is supreme in emergencies; the pope is bound by councils and tradition, not above them. (Conciliarist, Gallican)", {"CONCIL": 4, "GALL": 3, "PAPMIN": 2, "EORTHO": 2}],
            ["Communion ecclesiology: The pope is head of a communion of local churches, each with proper autonomy; patriarchal structures should be restored. (Eastern Catholic, Synodalist)", {"EASTECC": 4, "SYNOD": 3, "PAPMOD": 2, "ORTHOPH": 2}]
        ],
        "axis_weights": {"PAPAL": 5}
    },
    {
        "text": "Where does episcopal authority come from?",
        "options": [
            ["Directly from the Pope; bishops are essentially papal delegates (Ultramontane)", {"ULTRA": 3}],
            ["From Christ through episcopal consecration, but exercised in communion with Rome (Eastern Catholic, Papal Minimalist)", {"PAPMIN": 2, "EASTECC": 3, "SYNOD": 2, "THOM": 1}],
            ["From Christ through consecration; Rome has primacy but not source of jurisdiction (Gallican, Conciliarist)", {"GALL": 2, "CONCIL": 2, "PAPMIN": 2}],
            ["Bishops are true ordinaries with proper authority; papal primacy is real but limited (Moderate Papalist, Mainstream)", {"PAPMOD": 3, "STD": 2}]
        ],
        "axis_weights": {"PAPAL": 2}
    },
    {
        "text": "What is the proper model of Church unity, and how should it be maintained?",
        "options": [
            ["Juridical unity under papal authority with doctrinal uniformity enforced from Rome. Unity requires obedience. (Ultramontane, Integralist)", {"ULTRA": 3, "INTEG": 3, "NEOSCH": 2}],
            ["Communion of churches united in faith, sacraments, and fellowship with Rome, respecting legitimate diversity. (Eastern Catholic, Synodalist)", {"EASTECC": 4, "SYNOD": 3, "PAPMOD": 2}],
            ["Unity in essentials, liberty in doubtful matters, charity in all. The papacy preserves unity without crushing diversity. (Mainstream, Moderate Papalist)", {"STD": 3, "PAPMOD": 3, "COMMUN": 2, "DEVPROG": 1}],
            ["Through shared liturgical tradition, doctrinal fidelity, and resistance to modernist innovations that fracture the faith. (Traditionalist, SSPX-leaning)", {"TRAD": 3, "SSPX": 2, "ANTIMOD": 2, "TRIDSAC": 1}],
            ["Through ongoing synodal dialogue, inculturation, and the sensus fidei of the whole people of God. (Progressive, Synodalist)", {"PROG": 3, "SYNOD": 3, "LIBCATH": 2, "PERSMOR": 1}]
        ],
        "axis_weights": {"PAPAL": 2}
    },
    {
        "text": "Should Catholic rulers defer to bishops on faith and morals?",
        "options": [
            ["Yes, always—temporal authority is subordinate to spiritual in these matters (Hard Integralist, Integralist)", {"INTEG": 5, "ULTRA": 2}],
            ["Generally yes, but rulers have their own prudential competence (Soft Integralist, Moderate Papalist)", {"INTEGSOFT": 2, "PAPMOD": 2, "STD": 1}],
            ["Only when the teaching is clear and definitive (Gallican)", {"GALL": 2, "PAPMIN": 1}],
            ["No—temporal and spiritual authority should be strictly separate (Liberal Catholic, Progressive)", {"LIBCATH": 3, "PROG": 2}]
        ],
        "axis_weights": {"PAPAL": 2}
    },
    {
        "text": "How should we assess Vatican II — both its doctrinal authority and its pastoral-practical effects?",
        "options": [
            ["A fully authoritative ecumenical council whose teachings are binding; its pastoral fruits, while imperfect, represent genuine renewal. (Mainstream, Ressourcement)", {"STD": 3, "PAPMOD": 2, "PROG": 2, "RESS": 4, "DEVPROG": 2}],
            ["Authoritative but pastoral in character — it defined no new dogma. Its ambiguities have been exploited, requiring a hermeneutic of continuity. (Reform of Reform, Communio)", {"ROTR": 4, "COMMUN": 3, "TRAD": 1, "BENED": 2}],
            ["Contains serious ambiguities and ruptures with prior teaching (religious liberty, ecumenism, collegiality) that need formal correction. (SSPX-leaning, Traditionalist)", {"SSPX": 4, "TRAD": 3, "ANTIMOD": 3, "NEOSCH": 2, "SEDE": 1}],
            ["A robber council or invalid assembly that deviated from the Faith; its documents lack binding force. (Sedevacantist)", {"SEDE": 8, "SSPX": 1, "STD": -3, "PROG": -3}],
            ["The 'event' of Vatican II — its spirit of dialogue, openness, and reform — matters more than its letter. The Council opened windows the Church should keep open. (Progressive, Liberal Catholic)", {"PROG": 4, "LIBCATH": 3, "SYNOD": 2, "DEVPROG": 2, "TRAD": -2}]
        ],
        "axis_weights": {"LIT": 3, "PAPAL": 2}
    },
    {
        "text": "Regarding the post-1958 popes:",
        "options": [
            ["Fully legitimate popes with ordinary magisterial authority (Mainstream, Moderate Papalist)", {"STD": 3, "PAPMOD": 3, "PROG": 2, "RESS": 2}],
            ["Legitimate but their prudential decisions can be resisted when conflicting with Tradition (SSPX-leaning, Traditionalist)", {"SSPX": 3, "TRAD": 2}],
            ["Material but not formal popes (Sedeprivationist thesis)", {"SEDE": 3}],
            ["Not true popes at all; the See has been vacant (Sedevacantist)", {"SEDE": 3}]
        ],
        "axis_weights": {"PAPAL": -2, "LIT": 2}
    },
    {
        "text": "Can a Catholic resist or disobey Roman directives?",
        "options": [
            ["Never: Submission to Rome is essential to Catholic identity (Ultramontane)", {"ULTRA": 3, "PAPMOD": 1}],
            ["Only in extreme cases where directives clearly contradict defined doctrine (SSPX-leaning, Traditionalist)", {"SSPX": 3, "TRAD": 2}],
            ["Yes, when they conflict with Sacred Tradition and the sensus fidelium (SSPX-leaning, Sedevacantist)", {"SSPX": 2, "SEDE": 4}],
            ["Prudent disagreement is possible but public resistance is rarely justified (Mainstream, Moderate Papalist)", {"STD": 2, "PAPMOD": 2}]
        ],
        "axis_weights": {"PAPAL": -3}
    },
    {
        "text": "What is your position on Gallican liberties and national church autonomy?",
        "options": [
            ["Nations may legitimately negotiate appointment rights and synodal authority with Rome, provided they don't strongarm the Holy See. (Moderate Papalist, Mainstream)", {"PAPMOD": 4, "STD": 3, "INTEGSOFT": 3, "GALL": 2, "DEVPROG": 2}],
            ["Would make sense with stable Catholic monarchies, but impractical in modern liberal democracies. (Trad. Nationalist, Integralist)", {"TRADNAT": 4, "INTEG": 3, "TRAD": 3, "GALL": 2, "CORPCATH": 2}],
            ["A dangerous affront to papal authority. The Pope's universal jurisdiction must not be compromised. (Ultramontane)", {"ULTRA": 6, "INTEG": 3, "PAPMOD": -2, "GALL": -5, "CONCIL": -4}],
            ["Risks enabling nationalists to co-opt the Church and undermine her transnational mission. (Catholic Universalist, Liberal Catholic)", {"CATHUNIV": 5, "LIBCATH": 4, "PROG": 3, "SOCDEM": 2, "TRADNAT": -4}]
        ],
        "axis_weights": {"PAPAL": 3}
    },
    {
        "text": "How should the Church relate to secular liberal democracy?",
        "options": [
            ["Reject it - Christendom should be restored. Christ must reign socially. (Hard Integralist, Integralist)", {"INTEG": 11, "TRADNAT": 4, "TRAD": 3, "LIBCATH": -5}],
            ["Accept pragmatically but work for culture's conversion over time. (Soft Integralist)", {"INTEGSOFT": 5, "ROTR": 3, "STD": 3, "DEVPROG": 2}],
            ["Liberal democracy, rightly understood, is compatible with Catholicism. (Liberal Catholic)", {"LIBCATH": 5, "PAPMOD": 3, "STD": 3, "DEVPROG": 3, "INTEG": -4}],
            ["Fine but must be limited by natural law and subsidiarity. (Distributist, Mainstream)", {"DISTRIBUT": 4, "STD": 3, "THOMMOR": 3, "INTEGSOFT": 2}],
            ["Church should focus on souls, not political arrangements. (Carmelite, Carthusian)", {"CARM": 3, "CHART": 3, "STD": 2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "Did ressourcement theology recover authentic insights?",
        "options": [
            ["Yes: Patristic retrieval corrected neo-scholastic narrowness (Ressourcement, Neo-Augustinian)", {"RESS": 3, "NEOAUG": 2, "NEOPLAT": 2}],
            ["Partially: Some good insights but also problematic tendencies (Mainstream)", {"STD": 2, "THOM": 1}],
            ["No: It undermined sound theology and paved way for modernism (Neo-Scholastic, Traditionalist)", {"NEOSCH": 2, "TRAD": 2, "SSPX": 1}],
            ["It's complicated: Need to distinguish various authors and claims (Moderate Papalist)", {"PAPMOD": 2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "What is the proper form of church government?",
        "options": [
            ["Episcopal: bishops in apostolic succession are essential to the Church's structure. (Ultramontane, Moderate Papalist)", {"ULTRA": 3, "PAPMOD": 3, "ANGLICAN": 3, "EASTECC": 3, "STD": 2}],
            ["Presbyterian: governance by elders in graded courts (session, presbytery, synod, assembly). (Reformed)", {"REFORM": 4}],
            ["Congregational: each local congregation is autonomous under Christ.", {"REFORM": 2}],
            ["The Pope holds supreme jurisdiction; episcopal authority derives from him. (Ultramontane, Integralist)", {"ULTRA": 4, "INTEG": 3}],
            ["Synodal/collegial: bishops govern together; Rome has primacy of honor, not jurisdiction. (Eastern Orthodox, Synodalist)", {"EORTHO": 4, "SYNOD": 3, "EASTECC": 2, "GALL": 2, "CONCIL": 2}]
        ],
        "axis_weights": {"PAPAL": 2}
    },
    {
        "text": "How should we understand the filioque clause ('and the Son') in the Nicene Creed?",
        "options": [
            ["A legitimate and necessary doctrinal development clarifying Trinitarian relations. (Thomist, Tridentine)", {"THOM": 3, "TRIDSAC": 3, "ULTRA": 2, "STD": 2}],
            ["Theologically defensible but pastorally unwise to have added unilaterally; dialogue needed. (Ecumenical Monergist, Ressourcement)", {"ECUMON": 4, "RESS": 3, "COMMUN": 2, "PAPMOD": 2}],
            ["A Western addition that distorts Trinitarian theology; the Spirit proceeds from the Father alone. (Eastern Orthodox)", {"EORTHO": 5, "ORTHOPH": 4, "EASTECC": 2, "PALAM": 2}],
            ["The original Creed should be restored; Rome overstepped in adding to an ecumenical formula. (Conciliarist, Gallican)", {"CONCIL": 4, "GALL": 3, "PAPMIN": 2, "SYNOD": 2}]
        ],
        "axis_weights": {"PAPAL": 2, "SCRIPT": 2}
    },
    {
        "text": "What is the role of icons in Christian worship?",
        "options": [
            ["Icons are windows to heaven; veneration is essential to Orthodox piety and theology. (Eastern Orthodox, Eastern Liturgical)", {"EORTHO": 5, "EASTECC": 7, "ORTHOPH": 4}],
            ["Sacred images are legitimate aids to devotion, distinct from idolatry. (Tridentine, Traditionalist)", {"TRIDSAC": 4, "TRAD": 3, "STD": 3, "BENED": 2}],
            ["Images are acceptable but not essential; the Word preached is primary. (Reformed, Lutheran)", {"REFORM": 2, "LUTHERAN": 3, "ANGLICAN": 2}],
            ["Icons risk becoming idols; worship should focus on God alone. (Reformed)", {"REFORM": 4}]
        ],
        "axis_weights": {"LIT": 3, "PIETY": 2}
    },
    {
        "text": "If a non-definitive magisterial teaching seems doubtful or imprudent, what is the Catholic posture?",
        "options": [
            ["Interior assent is normally required; public disagreement risks scandal and disobedience. (Ultramontane)", {"ULTRA": 3, "PAPMOD": 1, "INTEG": 1}],
            ["Religious submission is owed, but one may withhold interior assent cautiously while seeking clarification and remaining obedient. (Moderate Papalist, Mainstream)", {"PAPMOD": 3, "STD": 3, "THOM": 1}],
            ["Respectful, reasoned critique is sometimes necessary; the Fathers and Tradition can correct modern confusions. (Ressourcement, Neo-Augustinian)", {"RESS": 2, "NEOAUG": 2, "TRAD": 2, "SSPX": 2, "PAPMIN": 1}],
            ["If it conflicts with Tradition, public resistance is justified. (SSPX-leaning, Traditionalist)", {"SSPX": 3, "TRAD": 2, "SEDE": 2}],
            ["Conscience is supreme; dissent can be fully legitimate. (Progressive, Liberal Catholic)", {"PROG": 3, "LIBCATH": 2, "PERSMOR": 1}]
        ],
        "axis_weights": {"PAPAL": 2, "SCRIPT": 1}
    },
    {
        "text": "What is the best approach to moral theology?",
        "options": [
            ["Virtue ethics: Focus on character formation and the virtues (Virtue Ethics, Thomist (Natural Law))", {"VIRTUE": 3, "THOMMOR": 2, "RESS": 1}],
            ["Natural law: Universal norms knowable by reason, applied through casuistry (Thomist (Natural Law), Manualist)", {"THOMMOR": 3, "MANUAL": 2, "NEOSCH": 1}],
            ["Personalist: Emphasis on human dignity and concrete situations", {"PERSMOR": 3, "PROG": 1}],
            ["Manualist: Clear rules and cases for confessional practice", {"MANUAL": 3, "NEOSCH": 2, "CASUIST": 2}]
        ],
        "axis_weights": {"RIGOR": -1}
    },
    {
        "text": "Do universal moral norms admit exceptions in concrete circumstances?",
        "options": [
            ["Never for intrinsically evil acts; prudence applies norms, doesn't create exceptions (Thomist (Natural Law), Manualist)", {"THOMMOR": 3, "MANUAL": 3, "NEOSCH": 3}],
            ["Proportionate reason can justify apparent exceptions (Proportionalism)", {"PROP": 3, "PROG": 2}],
            ["Pastoral discernment may find that a norm doesn't apply in a particular case (Personalist, Progressive)", {"PERSMOR": 2, "PROG": 2}],
            ["Epikeia allows departure from law's letter to fulfill its spirit (Thomist)", {"THOM": 2, "VIRTUE": 1}]
        ],
        "axis_weights": {"RIGOR": -2}
    },
    {
        "text": "In moral theology, how should doubtful cases and uncertain laws be handled?",
        "options": [
            ["Probabilism: A solidly probable opinion favoring liberty may be followed, even if the opinion for the law is more probable. (Probabilist, Redemptorist)", {"PROBAB": 4, "CSSR": 3, "JES": 2, "CASUIST": 2}],
            ["Equiprobabilism: One may follow the opinion favoring liberty only when it is equally or nearly as probable as the one favoring the law. (St. Alphonsus, Mainstream)", {"STD": 3, "CSSR": 2, "THOM": 2, "CASUIST": 1}],
            ["Tutiorism: One must always follow the safer opinion favoring the law. In doubt, the stricter path is morally required. (Tutiorist, Jansenist)", {"TUTIOR": 4, "JANS": 3, "NEOSCH": 2, "MANUAL": 2}],
            ["Prudential discernment case-by-case: The confessor uses practical wisdom and pastoral sensitivity, not rigid systems. (Personalist, Progressive)", {"PERSMOR": 3, "PROG": 2, "LIBCATH": 1}],
            ["The manualist tradition provides clear, time-tested categories that aid confessors and penitents alike. (Manualist, Neo-Scholastic)", {"MANUAL": 4, "NEOSCH": 3, "TRAD": 1}]
        ],
        "axis_weights": {"RIGOR": 3}
    },
    {
        "text": "What is the value of the manualist tradition in moral theology?",
        "options": [
            ["Essential: Provides clarity, precision, and practical guidance for confessors (Manualist, Neo-Scholastic)", {"MANUAL": 3, "NEOSCH": 2, "TRAD": 2, "CASUIST": 2}],
            ["Useful but needs integration with virtue ethics and Scripture (Thomist (Natural Law), Mainstream)", {"THOMMOR": 2, "STD": 2}],
            ["Problematic: Legalistic, minimalistic, and detached from spiritual growth", {"VIRTUE": 2, "PERSMOR": 2, "RESS": 2, "PROG": 1}],
            ["Outdated and should be largely set aside (Proportionalist, Progressive)", {"PROP": 2, "PROG": 2}]
        ],
        "axis_weights": {"RIGOR": 2}
    },
    {
        "text": "Which religious order's spirituality most resonates with you?",
        "options": [
            ["Dominican: Contemplation for preaching; truth and intellectual apostolate", {"DOM": 3, "THOM": 2, "INTELL": 1}],
            ["Jesuit: Finding God in all things; discernment, adaptability, active mission", {"JES": 3, "MOL": 2}],
            ["Franciscan: Poverty, simplicity, creation spirituality, affective devotion", {"FRAN": 3, "FRANC": 2, "SCOT": 1}],
            ["Carmelite: Contemplative prayer, mystical ascent, interior transformation", {"CARM": 3, "NEOPLAT": 1, "PALAM": 1}],
            ["Benedictine: Liturgy, stability, ora et labora, monastic rhythm", {"BENED": 3, "TRAD": 1, "TRIDSAC": 1}],
            ["Opus Dei: Sanctification of ordinary work, lay spirituality (Opus Dei)", {"OPUS": 3, "INTEG": 1, "NEOSCH": 1}],
            ["Oratorian: Community of secular priests, intellectual and pastoral (Oratorian)", {"ORAT": 3, "STD": 1}],
            ["No particular preference / diocesan spirituality (Mainstream)", {"STD": 2}]
        ],
        "axis_weights": {"PIETY": 1}
    },
    {
        "text": "What is the highest form of the religious life?",
        "options": [
            ["Contemplative life ordered to preaching and teaching (Dominican ideal)", {"DOM": 3, "THOM": 2}],
            ["Pure contemplation in solitude (Carthusian/Carmelite ideal)", {"CARM": 3, "CHART": 3, "BENED": 1}],
            ["Active apostolate for the greater glory of God (Jesuit ideal)", {"JES": 3, "OPUS": 1}],
            ["Liturgical prayer as the Church's public worship (Benedictine ideal)", {"BENED": 3, "TRAD": 1}],
            ["Evangelical poverty and simplicity among the people (Franciscan ideal)", {"FRAN": 3, "FRANC": 2}],
            ["Sanctification in ordinary secular life (Opus Dei ideal)", {"OPUS": 3}]
        ],
        "axis_weights": {"PIETY": 2}
    },
    {
        "text": "Christ's descent into hell (Sheol/Hades):",
        "options": [
            ["Triumphant proclamation and liberation of righteous — Harrowing of Hell. (Traditionalist, Eastern Sacramental)", {"TRAD": 3, "EASTSAC": 3, "BENED": 2, "CHALMAX": 1}],
            ["Christ truly experienced full human death, including darkness, before rising. (Kenotic)", {"KENOT": 4, "RESSCH": 2, "NEOAUG": 1, "FRANC": 1}],
            ["Soteriological completion: saving work extends to those who died before. (Thomist, Mainstream)", {"THOM": 2, "STD": 2, "PAPMOD": 1}],
            ["Primarily creedal affirmation; avoid excessive speculation. (Mainstream)", {"STD": 2, "NEOSCH": 1, "MANUAL": 1}]
        ],
        "axis_weights": {"ESCH": 3}
    },
    {
        "text": "St. Augustine's spirituality emphasizes:",
        "options": [
            ["Interior journey: 'Return to yourself; truth dwells in the inner man.' (Augustinian Order, Augustinian)", {"AUG": 7, "NEOAUG": 2, "CARM": 1}],
            ["Ordered love (ordo amoris): rightly ordering desires toward God. (Augustinian, Augustinian Moral)", {"AUG": 8, "VIRTUE": 1}],
            ["Grace and predestination: absolute priority of God's initiative. (Augustinian, Strict Augustinian)", {"AUG": 3, "AUGP": 3, "BANEZ": 2, "JANS": 1}],
            ["Community life: 'One mind and one heart intent upon God.' (Augustinian Order)", {"AUG": 4, "BENED": 2, "OPRAEM": 1}]
        ],
        "axis_weights": {"GRACE": 2, "PIETY": 2}
    },
    {
        "text": "St. Alphonsus Liguori and Redemptorists are known for:",
        "options": [
            ["Moral theology: equiprobabilism between rigorism and laxism.", {"CSSR": 4, "PROBAB": 2, "STD": 2, "CASUIST": 1}],
            ["Popular missions preaching 'abundant redemption' to abandoned. (Redemptorist)", {"CSSR": 4, "CM": 2, "CP": 1, "FRAN": 1}],
            ["Marian devotion: 'Glories of Mary' and confidence in intercession. (Redemptorist, Servite)", {"CSSR": 3, "OSM": 2, "MERC": 1, "TRAD": 1}],
            ["Practical pastoral approach: meeting people where they are. (Redemptorist, Vincentian)", {"CSSR": 3, "CM": 2, "SDB": 2, "PERSMOR": 1}]
        ],
        "axis_weights": {"RIGOR": -2}
    },
    {
        "text": "Don Bosco's Salesian spirituality centers on:",
        "options": [
            ["Preventive system: reason, religion, loving-kindness in education. (Salesian)", {"SDB": 4, "JES": 1, "PERSMOR": 1}],
            ["Joy and cheerfulness as essential witness, especially to youth. (Salesian)", {"SDB": 4, "FRAN": 2, "ORAT": 1}],
            ["Practical holiness in everyday life, accessible to all. (Salesian, Opus Dei)", {"SDB": 3, "OPUS": 2, "STD": 2}],
            ["Devotion to Mary Help of Christians and the Eucharist. (Salesian)", {"SDB": 3, "TRAD": 1, "EUCHMYST": 1}]
        ],
        "axis_weights": {"PIETY": 2}
    },
    {
        "text": "St. Vincent de Paul and Vincentian spirituality emphasizes:",
        "options": [
            ["'The poor are our lords and masters' — radical service to marginalized. (Vincentian)", {"CM": 4, "FRAN": 2, "WORKERCATH": 2, "SOCDEM": 1}],
            ["Formation of clergy: holy priests transform the Church. (Vincentian, Oratorian)", {"CM": 3, "ORAT": 2, "OPRAEM": 1, "DOM": 1}],
            ["Simplicity, humility, meekness as core virtues. (Vincentian)", {"CM": 4, "FRAN": 2, "SDB": 1}],
            ["Practical charity: 'Love is inventive to infinity.' (Vincentian)", {"CM": 4, "PERSMOR": 1, "VIRTUE": 1}]
        ],
        "axis_weights": {}
    },
    {
        "text": "How do you view Passionist spirituality and its emphasis on the 'memoria passionis' (memory of Christ's suffering)?",
        "options": [
            ["Central to Christian life: Meditating on the Passion transforms the soul and fuels preaching missions of conversion. (Passionist)", {"CP": 5, "CARM": 2, "TRAD": 2, "OSM": 1}],
            ["Important but must be balanced with Resurrection joy and hope — the Cross without Easter is incomplete. (Mainstream, Benedictine)", {"STD": 3, "BENED": 2, "SDB": 2, "FRAN": 2}],
            ["The memoria passionis connects us to the crucified peoples of today — solidarity with those who suffer now. (Passionist, Worker-Catholic)", {"CP": 4, "CM": 3, "WORKERCATH": 3, "KENOT": 2}],
            ["Reparation for sin through contemplation of the Passion is a powerful but demanding spiritual path. (Passionist, Traditionalist)", {"CP": 4, "TRAD": 2, "EUCHMYST": 2, "CSSR": 1}],
            ["Can become morbid or masochistic. Better to focus on Christ's victory and the joy of the Resurrection. (Progressive)", {"PROG": 3, "LIBCATH": 2, "CP": -2}]
        ],
        "axis_weights": {"PIETY": 4}
    },
    {
        "text": "Servite devotion to Our Lady of Sorrows teaches:",
        "options": [
            ["Standing with Mary at Cross transforms suffering into redemption. (Servite)", {"OSM": 4, "CP": 2, "CARM": 1}],
            ["Compassion (suffering-with) is central to Christian life. (Servite)", {"OSM": 4, "CM": 2, "KENOT": 1, "PERSMOR": 1}],
            ["Marian devotion leads to deeper union with Christ. (Servite, Redemptorist)", {"OSM": 3, "CSSR": 2, "MERC": 2, "TRAD": 1}],
            ["Seven Sorrows are a school of discipleship. (Servite)", {"OSM": 4, "CP": 2, "TRAD": 1}]
        ],
        "axis_weights": {"PIETY": 2}
    },
    {
        "text": "The Carthusian vocation represents:",
        "options": [
            ["Highest Christian life: pure contemplation, hidden intercession. (Carthusian)", {"CHART": 4, "CARM": 2, "BENED": 1, "TRAD": 1}],
            ["Valid but exceptional; active apostolate normative for most. (Dominican, Jesuit)", {"DOM": 2, "JES": 2, "STD": 2, "FRAN": 1}],
            ["Important witness, but Church needs engaged presence. (Progressive)", {"PROG": 2, "LIBCATH": 1, "SOCDEM": 1}],
            ["Desert tradition: 'flee, be silent, pray' as perennial wisdom. (Carthusian, Eastern Catholic)", {"CHART": 3, "EASTECC": 2, "PALAM": 1, "ORAT": 1}]
        ],
        "axis_weights": {"PIETY": 4}
    },
    {
        "text": "How do you assess the nominalist tradition (Ockham, etc.)?",
        "options": [
            ["A disaster that led to voluntarism, fideism, and ultimately secularism. (Thomist, Thomist (Realist))", {"THOM": 4, "THOMMETA": 4, "RADORTH": 3, "INTELL": 3, "NOMIN": -5}],
            ["Contains genuine insights about parsimony and the limits of metaphysical speculation. (Nominalist)", {"NOMIN": 7, "THOM": -2}],
            ["An interesting historical episode with little relevance to contemporary theology. (Mainstream, Progressive)", {"STD": 3, "PROG": 2, "DEVPROG": 2}],
            ["Ockham was a faithful Catholic; his positions are defensible within tradition. (Nominalist, Voluntarist)", {"NOMIN": 7, "SCOT": 2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "How should we understand the relationship between God's essence and energies, and is Palamite theology orthodox?",
        "options": [
            ["The essence-energies distinction is true and essential: God's unknowable essence is distinguished from His participated uncreated energies, making theosis possible. (Palamite, Orthophile)", {"PALAM": 6, "ORTHOPH": 5, "EASTECC": 4, "EASTSAC": 3}],
            ["Possibly compatible with Thomism if properly understood. Worth serious ecumenical dialogue. (Moderate, Communio)", {"PAPMOD": 3, "DEVPROG": 3, "COMMUN": 3, "ORTHOPH": 2, "RESS": 2}],
            ["Incompatible with divine simplicity as understood in Western theology. The West rightly rejected it. (Thomist, Neo-Scholastic)", {"THOM": 4, "THOMMETA": 4, "NEOSCH": 3, "PALAM": -5, "ORTHOPH": -3}],
            ["A distinctly Eastern approach that enriches Catholic theology without replacing the Thomist framework. Both lungs can breathe. (Eastern Catholic, Ressourcement)", {"EASTECC": 6, "PALAM": 3, "RESS": 3}],
            ["Scotist formal distinctions offer an orthodox Western interpretation: a real formal distinction in God between essence and operations, without Palamas's specific framework. (Scotist)", {"SCOT": 7, "FRANC": 2, "PALAM": 1, "DEVPROG": 1}]
        ],
        "axis_weights": {}
    },
    {
        "text": "How central is theosis (divinization) to your understanding of salvation?",
        "options": [
            ["Central - 'God became man that man might become God.' This is the heart of soteriology. (Palamite/Eastern, Orthophile)", {"PALAM": 5, "ORTHOPH": 5, "EASTECC": 4, "NEOAUG": 4, "RESS": 3}],
            ["Important but must be balanced with juridical/forensic categories. Both-and, not either-or. (Thomist, Mainstream)", {"THOM": 3, "STD": 3, "DEVPROG": 2, "AUG": 2}],
            ["Western theology rightly emphasizes justification. Theosis language risks pantheism. (Neo-Scholastic, Tridentine)", {"NEOSCH": 3, "TRIDSAC": 3, "MANUAL": 2, "PALAM": -3}],
            ["A beautiful Eastern emphasis the West should recover through ressourcement. (Ressourcement, Neo-Augustinian)", {"RESS": 5, "NEOAUG": 4, "COMMUN": 3, "PALAM": 3, "BENED": 2}]
        ],
        "axis_weights": {"JUST": 4}
    },
    {
        "text": "What is the proper relationship between Church and State?",
        "options": [
            ["Hard integralism: State must formally recognize Church and suppress public heresy", {"INTEG": 5, "TRAD": 1}],
            ["Soft integralism: State should favor true religion with prudential tolerance", {"INTEGSOFT": 3, "INTEG": 1, "STD": 1}],
            ["Separation with cooperation: Distinct spheres cooperating for human flourishing (Moderate Papalist, Mainstream)", {"PAPMOD": 2, "STD": 2, "RESS": 1}],
            ["Liberal Catholic: Religious liberty is a genuine right; separation protects both (Liberal Catholic, Progressive)", {"LIBCATH": 3, "PROG": 2}],
            ["Depends entirely on circumstances; no model universally normative (Mainstream)", {"STD": 2}]
        ],
        "axis_weights": {"PAPAL": 1, "RIGOR": 1}
    },
    {
        "text": "What is the relationship between Christ's kingship and political order?",
        "options": [
            ["Christ is King of nations; states should formally acknowledge this (Integralist, Hard Integralist)", {"INTEG": 6, "TRAD": 2}],
            ["Christ's kingship is primarily spiritual; political acknowledgment is optional (Liberal Catholic, Progressive)", {"LIBCATH": 2, "PROG": 2}],
            ["Social kingship is real but expressed through culture more than law (Soft Integralist)", {"INTEGSOFT": 3, "RESS": 1}],
            ["Christ's kingdom is not of this world in a political sense (Progressive)", {"PROG": 2, "LIBCATH": 1}]
        ],
        "axis_weights": {"PAPAL": 1}
    },
    {
        "text": "Which economic vision best reflects Catholic social teaching?",
        "options": [
            ["Distributism: Wide property distribution; neither capitalism nor socialism (Distributist, Agrarian)", {"DISTRIBUT": 3, "AGRAR": 2, "INTEG": 1, "TRAD": 1}],
            ["Corporatism/Solidarism: Vocational groups mediate between individual and state (Corporatist)", {"CORPCATH": 3, "INTEG": 1}],
            ["Social market economy: Free markets with strong social safety net and worker protections (Social Democrat)", {"SOCDEM": 3, "LIBCATH": 1, "STD": 1, "WORKERCATH": 1}],
            ["Free market without cronyism: Competitive markets with strong regulation against rent-seeking, monopoly, and corporate welfare, ensuring affordable housing and energy (Catholic Libertarian, Mainstream)", {"LIBERTAR": 3, "STD": 2, "DISTRIBUT": 1}],
            ["Worker cooperatives and strong unions as primary vehicles for economic justice (Worker-Catholic)", {"WORKERCATH": 3, "SOCDEM": 1, "CORPCATH": 1}],
            ["Catholic agrarianism: Return to the land and local economies (Agrarian, Distributist)", {"AGRAR": 3, "DISTRIBUT": 2, "TRAD": 1}]
        ],
        "axis_weights": {}
    },
    {
        "text": "Is a living wage a strict moral obligation?",
        "options": [
            ["Yes—employers must pay wages sufficient for dignified family support (Worker-Catholic, Distributist)", {"WORKERCATH": 3, "DISTRIBUT": 2, "SOCDEM": 2, "CORPCATH": 2}],
            ["It's a strong moral ideal but circumstances may prevent it (Mainstream)", {"STD": 2, "INTEG": 1}],
            ["Market wages are just if freely agreed; charity handles insufficiency (Libertarian)", {"LIBERTAR": 3}],
            ["Yes, and the state should enforce it when employers fail (Social Democrat, Worker-Catholic)", {"SOCDEM": 2, "WORKERCATH": 2}]
        ],
        "axis_weights": {"RIGOR": 1}
    },
    {
        "text": "What is the role of unions in Catholic social teaching?",
        "options": [
            ["Essential: Workers have a natural right to organize that must be respected (Worker-Catholic, Distributist)", {"WORKERCATH": 3, "DISTRIBUT": 2, "SOCDEM": 2, "CORPCATH": 2}],
            ["Generally positive but can become corrupt or politically captured (Mainstream)", {"STD": 2, "INTEG": 1}],
            ["Unnecessary in a truly free market; often harmful (Libertarian)", {"LIBERTAR": 3}],
            ["Useful within a corporatist structure that includes all vocational groups (Corporatist)", {"CORPCATH": 3}]
        ],
        "axis_weights": {}
    },
    {
        "text": "What is the proper scope of private property?",
        "options": [
            ["Wide distribution is essential; concentrated ownership is problematic (Distributist, Worker-Catholic)", {"DISTRIBUT": 3, "WORKERCATH": 2, "AGRAR": 2}],
            ["Private property is a natural right with minimal restrictions (Libertarian)", {"LIBERTAR": 3}],
            ["Property has a social mortgage; regulation for common good is justified (Social Democrat, Worker-Catholic)", {"SOCDEM": 3, "WORKERCATH": 2}],
            ["Property should be organized through vocational/corporate bodies (Corporatist)", {"CORPCATH": 3}]
        ],
        "axis_weights": {}
    },
    {
        "text": "How should Catholics understand nationalism, patriotism, and national identity?",
        "options": [
            ["Nations are natural communities willed by God; Catholicism should be inculturated nationally and borders defended. (Traditionalist Nationalist)", {"TRADNAT": 4, "INTEG": 2, "TRAD": 2}],
            ["The Church transcends nations; nationalism easily becomes idolatrous and must be subordinated to universal solidarity. (Catholic Universalist)", {"CATHUNIV": 4, "PROG": 2, "JES": 1, "LIBCATH": 1}],
            ["Moderate patriotism is healthy and natural, but always subordinate to Catholic identity and the common good. (Mainstream)", {"STD": 3, "PAPMOD": 2}],
            ["Catholic integralism properly channels national identity: the state serves Christ's kingship within its particular cultural context. (Integralist)", {"INTEG": 5, "TRADNAT": 2, "TRAD": 1}],
            ["National identity is a cultural gift but must be purified by the Gospel; solidarity with immigrants and refugees takes priority. (Progressive, Worker-Catholic)", {"PROG": 2, "WORKERCATH": 2, "CATHUNIV": 2, "SOCDEM": 1, "LIBCATH": 1}]
        ],
        "axis_weights": {}
    },
    {
        "text": "How should Catholic nations approach immigration?",
        "options": [
            ["Prioritize cultural and religious compatibility over economic factors (Trad. Nationalist, Integralist)", {"TRADNAT": 3, "INTEG": 4}],
            ["Welcome the stranger as a Gospel imperative; borders are secondary (Catholic Universalist, Progressive)", {"CATHUNIV": 3, "PROG": 2, "LIBCATH": 2}],
            ["Balance hospitality with legitimate concerns for common good (Mainstream, Moderate Papalist)", {"STD": 3, "PAPMOD": 2}],
            ["Local communities should decide without centralized immigration policy (Distributist)", {"DISTRIBUT": 2, "LIBERTAR": 1}]
        ],
        "axis_weights": {}
    },
    {
        "text": "Should the Church resist international institutions promoting secular values?",
        "options": [
            ["Yes, strongly—these institutions are hostile to natural law and faith (Integralist, Trad. Nationalist)", {"INTEG": 3, "TRADNAT": 3, "TRAD": 2, "SSPX": 2}],
            ["Engage critically but don't refuse all cooperation (Mainstream, Moderate Papalist)", {"STD": 2, "PAPMOD": 2}],
            ["Support international cooperation for peace and human rights (Progressive, Liberal Catholic)", {"PROG": 2, "LIBCATH": 2, "CATHUNIV": 2}],
            ["Focus on local and national levels; international institutions are secondary (Distributist)", {"DISTRIBUT": 2, "TRADNAT": 1}]
        ],
        "axis_weights": {"RIGOR": 1}
    },
    {
        "text": "What is your view of the Church hierarchy's approach to immigration?",
        "options": [
            ["A generational matter. Once older bishops retire, I'm optimistic about better balance. (Progressive, Synodalist)", {"PROG": 3, "STD": 2, "SYNOD": 3, "DEVPROG": 2}],
            ["Some nationalist governments have acted excessively, but prudential judgment on borders isn't sinful. National consciousness is legitimate. (Trad. Nationalist, Soft Integralist)", {"TRADNAT": 5, "INTEGSOFT": 4, "DISTRIBUT": 3, "STD": 2, "CATHUNIV": -3}],
            ["A welcome prophetic stance against the pagan idols of nationalism and kinism. (Catholic Universalist, Liberal Catholic)", {"CATHUNIV": 6, "LIBCATH": 5, "PROG": 4, "SOCDEM": 3, "TRADNAT": -5}],
            ["Balanced - the clergy can be naive about practical realities, but their intentions are good. (Mainstream, Moderate Papalist)", {"STD": 4, "PAPMOD": 3, "ROTR": 2, "TRADUM": 2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "What is your view on Amoris Laetitia and communion for the divorced and remarried?",
        "options": [
            ["A development allowing pastoral discernment in complex situations. (Progressive, Synodalist)", {"PROG": 5, "SYNOD": 4, "PERSMOR": 3, "LIBCATH": 3, "TRAD": -5, "NEOSCH": -4}],
            ["Ambiguous document misused by progressives. The dubia remain unanswered. (Traditionalist)", {"TRAD": 5, "ROTR": 3, "TRADUM": 3, "NEOSCH": 3, "ANTIMOD": 2}],
            ["Heretical. Contradicts Familiaris Consortio and perennial teaching. (SSPX-leaning, Sedevacantist)", {"SSPX": 5, "SEDE": 4, "TRAD": 4, "ANTIMOD": 4, "PROG": -5}],
            ["Pastoral accompaniment is good but doesn't change the discipline. (Mainstream, Moderate Papalist)", {"STD": 4, "PAPMOD": 3, "MANUAL": 2, "THOMMOR": 2}]
        ],
        "axis_weights": {"RIGOR": 4}
    },
    {
        "text": "In theological disputes, which is the normal direction of reasoning?",
        "options": [
            ["Scripture (as received in the Church) judges theology; systems must be revised to fit Scripture's full witness. (Neo-Augustinian, Ressourcement)", {"NEOAUG": 3, "RESS": 2, "AUG": 2, "BENED": 1}],
            ["Dogma and metaphysics provide the framework that stabilizes interpretation; Scripture is read within that settled grammar. (Thomist, Thomist (Realist))", {"THOM": 3, "THOMMETA": 2, "NEOSCH": 2, "DOM": 1}],
            ["The living Magisterium provides the proximate norm; speculative resolution is less important than obedience. (Ultramontane, Moderate Papalist)", {"ULTRA": 3, "PAPMOD": 2, "STD": 1}],
            ["Multiple theologies can legitimately coexist; Scripture underdetermines systematic disputes. (Mainstream)", {"STD": 2, "PAPMOD": 1, "RESS": 1, "PROG": 1}]
        ],
        "axis_weights": {"SCRIPT": 3}
    },
    {
        "text": "Habitual vice formed by prior voluntary sin…",
        "options": [
            ["Can incur guilt through culpable omission: failure to pursue virtue and remedies becomes morally weighty. (Augustinian, Augustinian Moral)", {"AUG": 4, "VIRTUE": 2, "NEOSCH": 1}],
            ["Is a dangerous disposition, but guilt attaches only to present voluntary acts and consent. (Thomist, Thomist (Natural Law))", {"THOM": 2, "THOMMOR": 2, "STD": 1}],
            ["Shows that the will is deeply bound; strict ascetic discipline and frequent confession are the safest path. (Traditionalist, Manualist)", {"TRAD": 2, "MANUAL": 2, "NEOSCH": 2, "TUTIOR": 1}],
            ["The Church should avoid scrupulosity: focus on healing and gradual growth. (Personalist, Progressive)", {"PERSMOR": 2, "PROG": 2}]
        ],
        "axis_weights": {"RIGOR": 2}
    },
    {
        "text": "Purgatory is best understood primarily as which of the following?",
        "category": "Eschatology",
        "options": [
            ["Satisfaction and purification from temporal punishment due to sin. (Manualist, Neo-Scholastic)", {"MANUAL": 2, "NEOSCH": 2, "TRAD": 1, "STD": 2}],
            ["Final purification of love: removal of attachments so the soul can see God. (Thomist, Benedictine)", {"THOM": 2, "BENED": 2, "RESS": 1, "NEOAUG": 1, "STD": 2}],
            ["An encounter with divine fire that heals and illumines (Eastern-leaning emphasis). (Palamite/Eastern, Eastern Sacramental)", {"PALAM": 3, "EASTSAC": 2, "EUCHMYST": 1, "NEOPLAT": 1}],
            ["A symbol pointing to God's mercy; details shouldn't be systematized. (Progressive)", {"PROG": 2, "PERSMOR": 1}]
        ],
        "axis_weights": {"ESCH": 3, "RIGOR": 1}
    },
    {
        "text": "Theologians primarily serve the Church by…",
        "options": [
            ["Clarifying and defending settled doctrine with precision (often scholastic). (Dominican, Thomist)", {"DOM": 2, "THOM": 2, "NEOSCH": 2, "MANUAL": 1}],
            ["Retrieving the Fathers and liturgical tradition to renew theology (ressourcement). (Ressourcement, Neo-Augustinian)", {"RESS": 3, "NEOAUG": 2, "BENED": 1, "NEOPLAT": 1}],
            ["Mediating doctrine pastorally for modern contexts while preserving essentials. (Moderate Papalist, Mainstream)", {"PAPMOD": 2, "STD": 2, "JES": 2, "PERSMOR": 1}],
            ["Testing boundaries and developing new paradigms to meet contemporary needs. (Progressive)", {"PROG": 3, "LIBCATH": 1}]
        ],
        "axis_weights": {"SCRIPT": 1}
    },
    {
        "text": "What is the relationship between fallen human nature and the ability to do good?",
        "options": [
            ["Fallen humans can do natural goods but absolutely cannot move toward salvation without prevenient grace (Augustinian, Strict Augustinian)", {"AUG": 3, "AUGP": 3, "THOM": 2, "BANEZ": 2, "JANS": 2}],
            ["Fallen humans retain significant natural capacity; grace assists but doesn't wholly initiate (Semi-Augustinian, Molinist)", {"AUG": 3, "MOL": 2, "PROG": 1}],
            ["Human nature is so corrupted that even natural goods are tainted without grace (Reformed, Lutheran)", {"REFORM": 4, "LUTHERAN": 3}],
            ["Grace and nature cooperate from the start; the distinction is somewhat artificial (Neo-Augustinian, Ressourcement)", {"NEOAUG": 2, "RESS": 2}]
        ],
        "axis_weights": {"GRACE": 1}
    },
    {
        "text": "What is the relationship between God's will and God's intellect?",
        "options": [
            ["Intellectualist: God wills things because they are good; goodness is prior to willing. The divine intellect apprehends the good, and the will necessarily follows. (Intellectualist, Thomist)", {"INTELL": 4, "THOM": 4, "DOM": 3, "THOMMETA": 2}],
            ["Radical Voluntarist: Things are good solely because God wills them; divine will alone is the arbitrary source of all moral order. (Nominalist)", {"NOMIN": 8}],
            ["Moderate Voluntarism: God's will is formally primary and free, but always acts according to wisdom and the divine nature—never arbitrarily. (Scotist)", {"SCOT": 6, "NOMIN": 2, "FRANC": 3}],
            ["The distinction is artificial; will and intellect are identical in God and mutually implicate each other in the divine simplicity. (Palamite/Eastern)", {"PALAM": 3, "NEOPLAT": 2, "EASTECC": 2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "What is the source of moral obligations?",
        "options": [
            ["Radical divine command—things are good/evil solely because God wills them so; there is no independent rational order prior to the divine decree. (Nominalist)", {"NOMIN": 8}],
            ["The nature of things known by reason—God wills them because they are good. Natural law is grounded in eternal reason, not arbitrary will. (Thomist, Intellectualist)", {"THOM": 4, "INTELL": 4, "THOMMOR": 3, "DOM": 2}],
            ["God's will freely establishes the moral order, but this will is always guided by wisdom and the divine nature, never arbitrary or irrational. (Scotist)", {"SCOT": 4, "NOMIN": 2, "FRANC": 3}],
            ["Participation in eternal law, which is both rational and willed—the law written on our hearts reflects both divine wisdom and divine decree. (Augustinian, Neo-Platonist)", {"AUG": 3, "NEOPLAT": 3, "THOM": 1}],
            ["A combination: God's will establishes positive/ceremonial law, but natural law reflects the rational order of creation. (Mainstream)", {"STD": 3, "THOM": 1, "PAPMOD": 1}]
        ],
        "axis_weights": {"RIGOR": 1}
    },
    {
        "text": "How did the early Church function?",
        "options": [
            ["Essentially as today—with Roman primacy and centralized authority (Ultramontane)", {"ULTRA": 3, "INTEG": 1}],
            ["More synodally and collegially, with Roman primacy developing over time (Synodalist, Conciliarist)", {"SYNOD": 3, "CONCIL": 3, "EASTECC": 2, "GALL": 2}],
            ["With real Roman primacy but more subsidiarity than later periods (Moderate Papalist, Mainstream)", {"PAPMOD": 2, "STD": 2}],
            ["As a communion of local churches with Rome as first among equals (Eastern Catholic, Synodalist)", {"EASTECC": 3, "SYNOD": 2, "PAPMIN": 2}]
        ],
        "axis_weights": {"PAPAL": 1}
    },
    {
        "text": "Is a confessional Catholic state still the ideal?",
        "options": [
            ["Yes, absolutely—this is the perennial teaching of the Church (Hard Integralist, Integralist)", {"INTEG": 6, "TRAD": 2, "SSPX": 2}],
            ["In principle yes, but rarely prudent in modern pluralist societies (Soft Integralist)", {"INTEGSOFT": 3, "STD": 1}],
            ["No—Dignitatis Humanae represents genuine doctrinal development (Liberal Catholic, Progressive)", {"LIBCATH": 3, "PROG": 2, "RESS": 1}],
            ["The question is more complex than a simple yes/no (Mainstream)", {"STD": 2, "PAPMOD": 1}]
        ],
        "axis_weights": {"PAPAL": 2, "LIT": 1}
    },
    {
        "text": "What is the highest form of prayer?",
        "options": [
            ["Contemplative prayer: Simple loving gaze upon God (Carmelite, Neo-Platonist)", {"CARM": 3, "NEOPLAT": 2, "PALAM": 2}],
            ["The Holy Sacrifice of the Mass (Benedictine, Tridentine)", {"BENED": 3, "TRIDSAC": 2, "TRAD": 2}],
            ["Liturgy of the Hours as the Church's official prayer (Benedictine)", {"BENED": 3, "DOM": 1}],
            ["Lectio Divina: Prayerful reading of Scripture (Benedictine, Ressourcement)", {"BENED": 2, "RESS": 2}],
            ["Ignatian meditation with imagination and application of senses (Jesuit)", {"JES": 3}],
            ["All are valid paths suited to different vocations (Mainstream)", {"STD": 2}]
        ],
        "axis_weights": {"PIETY": 2}
    },
    {
        "text": "How should we understand mystical experiences?",
        "options": [
            ["Extraordinary graces given to some; not to be sought but accepted (Carmelite, Dominican)", {"CARM": 3, "DOM": 2, "THOM": 2}],
            ["The normal flowering of the life of grace available to all who persevere (Carmelite, Neo-Platonist)", {"CARM": 2, "NEOPLAT": 2}],
            ["Suspect: Focus on ordinary virtue and sacraments instead (Manualist)", {"MANUAL": 2, "NEOSCH": 1}],
            ["Central to Eastern spirituality: Theosis/deification is the goal (Palamite/Eastern, Eastern Sacramental)", {"PALAM": 3, "EASTSAC": 2}]
        ],
        "axis_weights": {"PIETY": 2}
    },
    {
        "text": "How often should a devout Catholic go to confession?",
        "options": [
            ["Weekly or at least fortnightly, even without mortal sin (Traditionalist, Opus Dei)", {"TRAD": 3, "CARM": 2, "OPUS": 3, "MANUAL": 2}],
            ["Monthly for devotional confession; more often if in mortal sin (Mainstream)", {"STD": 2, "JES": 1}],
            ["Whenever conscious of serious sin; otherwise a few times a year (Progressive)", {"PROG": 2}],
            ["The Eastern tradition emphasizes spiritual direction over frequent confession (Eastern Sacramental)", {"EASTSAC": 2, "PALAM": 1}]
        ],
        "axis_weights": {"PIETY": 2, "RIGOR": 1}
    },
    {
        "text": "Why did the Son of God become incarnate?",
        "options": [
            ["Primarily to redeem from sin; without Fall, no Incarnation. (Thomist, Augustinian)", {"THOM": 4, "AUG": 2, "AUGP": 1, "INFRA": 2}],
            ["Christ would have come even without sin; Incarnation is creation's crown. (Scotist, Franciscan School)", {"SCOT": 6, "FRANC": 3, "SUPRA": 2}],
            ["Both redemption and divinization: save from sin AND unite to God in theosis. (Palamite/Eastern, Eastern Catholic)", {"PALAM": 3, "EASTECC": 2, "RESSCH": 2, "NEOAUG": 2}],
            ["The question is speculative; focus on actual economy revealed. (Mainstream)", {"STD": 2, "PAPMOD": 1, "RESS": 1, "BENED": 1}]
        ],
        "axis_weights": {"GRACE": 2, "JUST": 1}
    },
    {
        "text": "The Cistercian/Trappist reform emphasizes:",
        "options": [
            ["Strict silence and solitude as essential for encountering God. (Cistercian/Trappist, Carthusian)", {"OCSO": 4, "CHART": 3, "BENED": 2}],
            ["Manual labor as prayer: working with hands sanctifies. (Cistercian/Trappist)", {"OCSO": 4, "BENED": 2, "AGRAR": 1}],
            ["Simplicity and austerity: stripping away to find essential. (Cistercian/Trappist, Carthusian)", {"OCSO": 3, "CHART": 2, "FRAN": 2, "TRAD": 1}],
            ["Liturgical beauty in pure, unadorned Benedictine form.", {"OCSO": 3, "BENED": 3, "OPRAEM": 2, "TRAD": 1}]
        ],
        "axis_weights": {"PIETY": 4, "LIT": 1}
    },
    {
        "text": "Catholic rural/agrarian life should be valued as:",
        "options": [
            ["Land-based life forms virtue uniquely; prefer smallholdings. (Agrarian, Distributist)", {"AGRAR": 4, "DISTRIBUT": 3, "TRADNAT": 2, "CHART": 1}],
            ["Has value but industrialization not inherently evil. (Mainstream, Social Democrat)", {"STD": 2, "SOCDEM": 2, "PAPMOD": 1}],
            ["Romantic nostalgia; address actual worker conditions. (Worker-Catholic, Progressive)", {"WORKERCATH": 2, "PROG": 2, "LIBCATH": 1}],
            ["Rural parishes preserve faith; special concern for farmers. (Traditionalist, Agrarian)", {"TRAD": 2, "AGRAR": 2, "BENED": 2, "CORPCATH": 1}]
        ],
        "axis_weights": {}
    },
    {
        "text": "How should the Catholic Church approach reunion with the Eastern Orthodox?",
        "options": [
            ["Return to Rome under papal authority as Vatican I defined. No compromises on primacy. (Ultramontane)", {"ULTRA": 5, "INTEG": 3, "NEOSCH": 3, "ANTIMOD": 2, "ORTHOPH": -4}],
            ["A 'Sister Churches' model with restored communion but preserved Eastern autonomy. (Eastern Catholic, Orthophile)", {"EASTECC": 8, "EASTSAC": 4, "PALAM": 3, "SYNOD": 3, "ORTHOPH": 5, "ULTRA": -3}],
            ["Focus on resolving theological issues (Filioque, essence-energies) before structural questions. (Thomist, Ressourcement)", {"THOM": 3, "RESS": 3, "PALAM": 3, "DOM": 2, "COMMUN": 2, "ORTHOPH": 2}],
            ["Ecumenism has gone too far. Maintain clear boundaries until they accept all Catholic dogma. (Traditionalist, SSPX-leaning)", {"TRAD": 4, "SSPX": 4, "NEOSCH": 3, "ANTIMOD": 3, "PROG": -3}],
            ["Practical cooperation first; doctrinal unity will follow organically. (Progressive, Liberal Catholic)", {"PROG": 4, "LIBCATH": 3, "CM": 2, "SYNOD": 2, "TRAD": -2}]
        ],
        "axis_weights": {"PAPAL": 2}
    },
    {
        "text": "How do you understand Vatican II's teaching on religious liberty (Dignitatis Humanae)?",
        "options": [
            ["Legitimate development - the state shouldn't coerce conscience, though truth remains objective. (Moderate Papalist, Mainstream)", {"PAPMOD": 4, "STD": 4, "RESS": 3, "DEVPROG": 4, "COMMUN": 3}],
            ["A prudential adaptation for pluralist societies, not reversal of prior teaching. (Soft Integralist)", {"INTEGSOFT": 5, "ROTR": 3, "STD": 3, "TRADUM": 3}],
            ["A rupture with Tradition. Quanta Cura condemned exactly what DH teaches. (SSPX-leaning, Traditionalist)", {"SSPX": 6, "TRAD": 5, "INTEG": 5, "SEDE": 4, "ANTIMOD": 5, "LIBCATH": -6}],
            ["The Church finally embraced freedom of conscience as foundational to human dignity. (Liberal Catholic, Progressive)", {"LIBCATH": 6, "PROG": 5, "PERSMOR": 4, "SYNOD": 2, "INTEG": -5}],
            ["Ambiguously worded; needs authoritative clarification to reconcile with prior magisterium. (Traditionalist, Reform of Reform)", {"TRAD": 4, "ROTR": 3, "PAPMIN": 3, "TRADUM": 3, "ANTIMOD": 2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "What is your view on mandatory clerical celibacy in the Latin Rite?",
        "options": [
            ["Precious discipline that should never be relaxed. Frees priests for total dedication. (Traditionalist, Opus Dei)", {"TRAD": 4, "OPUS": 4, "INTEG": 3, "NEOSCH": 3, "CARM": 2, "CHART": 2}],
            ["Valuable but could permit married priests in mission territories, as Eastern Catholics do. (Eastern Catholic, Moderate Papalist)", {"EASTECC": 4, "PAPMOD": 3, "STD": 3, "SYNOD": 3, "ORDINAR": 3, "ORTHOPH": 2}],
            ["Should be entirely optional. Many good men are lost; the Apostles were married. (Progressive, Liberal Catholic)", {"PROG": 5, "LIBCATH": 5, "SYNOD": 3, "TRAD": -4, "OPUS": -3}],
            ["Essential for eschatological witness. It images heavenly life. (Carmelite, Carthusian)", {"CARM": 4, "CHART": 4, "BENED": 3, "OCSO": 4, "TRAD": 3, "CP": 2}],
            ["The Ordinariate exception shows flexibility is possible. Expand it carefully. (Ordinariate)", {"ORDINAR": 5, "PAPMOD": 3, "DEVPROG": 2, "STD": 2}]
        ],
        "axis_weights": {"RIGOR": 2, "PIETY": 1}
    },
    {
        "text": "If Lutheran 'Sacramental Union' recognized ontological change, and 'faith alone' was understood as Benedict XVI saw it, would these impede reunion?",
        "options": [
            ["No - properly understood, these need not be impediments. JDDJ showed real convergence. (Lutheran-Catholic, Ecumenical Monergist)", {"ECUMON": 11, "DEVPROG": 4, "COMMUN": 3, "PAPMOD": 2, "TRAD": -4}],
            ["Possibly not, but we'd still need agreement on papacy, Marian dogmas, purgatory. (Moderate Papalist, Mainstream)", {"PAPMOD": 4, "STD": 4, "THOM": 3, "ECUMON": 2, "DEVPROG": 2}],
            ["Yes - Lutheran theology is fundamentally incompatible. Trent's condemnations stand.", {"TRAD": 5, "NEOSCH": 5, "ANTIMOD": 4, "SSPX": 4, "ECUMON": -11}],
            ["This hypothetical concedes too much. Lutheranism doesn't actually affirm these things.", {"THOM": 3, "DOM": 2, "STD": 2, "NEOSCH": 2}]
        ],
        "axis_weights": {"JUST": 3}
    },
    {
        "text": "How should Catholics approach lay apostolates and evangelization in the digital space?",
        "options": [
            ["Embrace fully. Social media is the new Areopagus. Memes and podcasts reach millions. (Salesian, Jesuit)", {"SDB": 4, "JES": 3, "PROG": 3, "OPUS": 3, "STD": 2, "CHART": -2}],
            ["Cautiously useful, but nothing replaces parish life and sacramental encounter. (Mainstream, Benedictine)", {"STD": 4, "BENED": 3, "PAPMOD": 2, "ORAT": 3, "CM": 2}],
            ["Dangerous - breeds pride and controversy-seeking. Focus on real community. (Carthusian, Cistercian/Trappist)", {"CHART": 4, "OCSO": 3, "BENED": 2, "CARM": 2, "TRAD": 2}],
            ["Essential for reaching the young, but must be done with theological competence. (Dominican, Jesuit)", {"DOM": 4, "JES": 3, "COMMUN": 2, "ORAT": 2, "SDB": 3}],
            ["Lay apostolates online have revived tradition more than the hierarchy. Keep going. (Traditionalist, Reform of Reform)", {"TRAD": 4, "ROTR": 3, "TRADUM": 3, "ANTIMOD": 2, "SYNOD": -2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "What expanded roles, if any, should women have in the Church?",
        "options": [
            ["Female deacons should be restored; women should lead wherever ordination isn't required. (Progressive, Liberal Catholic)", {"PROG": 5, "SYNOD": 4, "LIBCATH": 5, "TRAD": -5, "INTEG": -4}],
            ["Women already have vital roles. Recognize existing contributions, don't invent offices. (Mainstream, Moderate Papalist)", {"STD": 4, "PAPMOD": 3, "OPUS": 3, "TRAD": 2}],
            ["The push reflects secular feminism infiltrating the Church. Resist it. (Traditionalist, Integralist)", {"TRAD": 5, "INTEG": 5, "SSPX": 4, "ANTIMOD": 4, "PROG": -5}],
            ["Study historical evidence for deaconesses carefully; proceed with tradition. (Ressourcement, Eastern Catholic)", {"RESS": 3, "EASTECC": 3, "PAPMOD": 3, "DEVPROG": 2, "COMMUN": 2}],
            ["Religious sisters already exercise profound spiritual authority. This is the feminine genius. (Carmelite, Benedictine)", {"CARM": 4, "BENED": 3, "CM": 2, "FRAN": 2, "OSM": 2, "OPUS": 2}]
        ],
        "axis_weights": {"RIGOR": 2}
    },
    {
        "text": "How should the Church understand her relationship with Judaism after Nostra Aetate?",
        "options": [
            ["The Old Covenant remains valid. Jews have a unique path not requiring explicit Christian faith. (Progressive, Liberal Catholic)", {"PROG": 4, "LIBCATH": 4, "RESS": 2, "TRAD": -5, "NEOSCH": -4}],
            ["Nostra Aetate condemned antisemitism but didn't change the necessity of Christ for salvation. (Mainstream, Moderate Papalist)", {"STD": 4, "PAPMOD": 4, "THOM": 3, "DEVPROG": 2, "TRAD": 2}],
            ["The Church has overcorrected. Supersessionism is traditional and shouldn't be abandoned. (Traditionalist, SSPX-leaning)", {"TRAD": 5, "SSPX": 4, "NEOSCH": 4, "ANTIMOD": 3, "PROG": -4}],
            ["Complex - honor Jewish roots, condemn antisemitism, maintain missionary mandate to all. (Ressourcement, Neo-Augustinian)", {"RESS": 4, "NEOAUG": 3, "BENED": 3, "COMMUN": 3, "STD": 2}]
        ],
        "axis_weights": {}
    },
    {
        "text": "What is your view on Marian apparitions (Fatima, Lourdes, etc.)?",
        "options": [
            ["Essential to Catholic piety. The Fatima consecration should be taken seriously. (Traditionalist, Redemptorist)", {"TRAD": 4, "CSSR": 3, "OSM": 3, "MERC": 2, "ANTIMOD": 2}],
            ["Approved apparitions are credible but private revelation is never obligatory. (Mainstream, Moderate Papalist)", {"STD": 4, "PAPMOD": 3, "THOM": 2, "DEVPROG": 2}],
            ["Often verge on superstition. Focus on Scripture and Sacraments. (Progressive, Liberal Catholic)", {"PROG": 3, "LIBCATH": 3, "DOM": 2, "TRAD": -2, "CSSR": -2}],
            ["Some are solid (Fatima, Lourdes) but others (Medjugorje) are likely fraudulent.", {"TRAD": 3, "STD": 3, "ROTR": 2, "PAPMOD": 2}]
        ],
        "axis_weights": {"PIETY": 2}
    },
    {
        "text": "What is the proper understanding of Mary's role as 'Mediatrix' and the proposed title 'Co-redemptrix'?",
        "options": [
            ["Mary truly cooperated in our redemption in a unique and subordinate manner; the titles 'Mediatrix of All Graces' and 'Co-redemptrix' should be solemnly defined to crown Catholic Mariology. (Marian Maximalist)", {"TRAD": 5, "CSSR": 4, "OSM": 4, "MERC": 3, "INTEG": 3, "MANUAL": 2, "PROG": -4, "ORTHOPH": -3}],
            ["These titles, while capable of orthodox interpretation, risk serious misunderstanding and ecumenical harm; the Church should refrain from dogmatic definition while permitting private devotion. (Moderate / Prudential)", {"STD": 4, "PAPMOD": 4, "COMMUN": 3, "DEVPROG": 3, "THOM": 2, "JES": 2}],
            ["Mary is best understood as the 'Archetype' or 'Type' of the Church—the first and most perfect disciple who models receptivity to grace. Maximalist titles obscure this ecclesiotypical emphasis recovered by ressourcement. (Ressourcement / Ecclesiotypical)", {"RESS": 5, "NEOAUG": 4, "COMMUN": 4, "BENED": 3, "TRAD": -2}],
            ["The East venerates the Theotokos as 'more honorable than the Cherubim' and prays 'through her intercessions, save us,' but without the juridical Latin categories of 'mediatrix' or 'co-redemptrix.' (Eastern / Patristic)", {"EASTECC": 8, "PALAM": 4, "EASTSAC": 4, "ORTHOPH": 4, "EORTHO": 3}],
            ["Marian titles beyond 'Mother of God' risk detracting from Christ's unique mediation (1 Tim 2:5); the Church should adopt a more Christocentric and scripturally restrained Mariology. (Minimalist / Ecumenical)", {"PROG": 4, "LIBCATH": 4, "ECUMON": 6, "ANGLICAN": 2, "TRAD": -4, "CSSR": -3}]
        ],
        "axis_weights": {"PIETY": 4, "PAPAL": 2, "LIT": 1}
    },
    {
        "text": "What form of Marian devotion best reflects authentic Catholic liturgical piety?",
        "options": [
            ["The solemn Marian antiphons of the Divine Office—Salve Regina, Alma Redemptoris Mater, Ave Regina Caelorum, Regina Caeli—represent the Church's most sublime and doctrinally precise Marian prayer, rooted in the Fathers. (Liturgical Traditionalist / Benedictine)", {"BENED": 5, "TRAD": 5, "TRIDSAC": 4, "OCSO": 4, "CHART": 3, "OPRAEM": 3, "ROTR": 3, "PROG": -3}],
            ["The Holy Rosary, particularly the traditional fifteen mysteries contemplated daily, remains the pre-eminent Marian devotion for the faithful and the surest path to Marian consecration. (Dominican / Popular Traditional)", {"DOM": 5, "TRAD": 4, "CSSR": 4, "OSM": 3, "FRAN": 3, "OPUS": 2, "PROG": -2}],
            ["The Byzantine Akathist Hymn and the rich Eastern Marian troparia preserve the Christological and patristic balance that some Western devotions—particularly post-Tridentine maximalism—have occasionally lost. (Eastern Liturgical)", {"EASTECC": 10, "EASTSAC": 4, "PALAM": 4, "ORTHOPH": 4, "RESS": 2}],
            ["Marian devotion today should emphasize Mary as the first disciple, model of faith, and icon of the pilgrim Church—expressed through contemporary hymnody, inclusive language, and scriptural foundations rather than medieval accretions. (Progressive / Pastoral)", {"PROG": 5, "LIBCATH": 4, "PERSMOR": 3, "SDB": 3, "SYNOD": 2, "TRAD": -4, "TRIDSAC": -3}],
            ["All authentic forms of Marian devotion—whether Office antiphons, Rosary, Scapular, Akathist, or contemporary hymns—are valuable when they lead souls to Christ; no single form should be privileged over others. (Mainstream / Inclusive)", {"STD": 4, "PAPMOD": 3, "CM": 3, "JES": 2, "ORAT": 2, "DEVPROG": 2, "FRAN": 2}]
        ],
        "axis_weights": {"LIT": 5, "PIETY": 4, "RIGOR": 1}
    },
    {
        "text": "What is your view on the possibility of an 'empty hell' (Balthasar's hope)?",
        "options": [
            ["Permissible - we may dare to hope all are saved. God's mercy is infinite. (Communio School, Progressive)", {"COMMUN": 4, "PROG": 4, "LIBCATH": 4, "TRAD": -4, "AUGP": -4, "JANS": -4}],
            ["Heretical or temerarious. Scripture and Tradition attest many are damned. (Strict Augustinian, Jansenist)", {"AUGP": 5, "JANS": 4, "TRAD": 4, "NEOSCH": 3, "ANTIMOD": 3, "COMMUN": -4}],
            ["We can hope for individuals but the Church teaches hell is populated. (Mainstream, Thomist)", {"STD": 4, "THOM": 3, "PAPMOD": 2, "AUG": 2}],
            ["Speculative. Focus on your own salvation, not universal questions. (Carmelite, Carthusian)", {"CARM": 3, "CHART": 3, "STD": 2, "BENED": 2}]
        ],
        "axis_weights": {"ESCH": 4, "RIGOR": 3}
    },
    {
        "text": "What is your position on Humanae Vitae's teaching on contraception?",
        "options": [
            ["Prophetic and absolutely binding. NFP is the only moral option. (Traditionalist, Neo-Scholastic)", {"TRAD": 5, "NEOSCH": 5, "OPUS": 4, "THOMMOR": 4, "INTEG": 3}],
            ["True but pastoral sensitivity needed. Distinguish grave matter from mortal sin. (Mainstream, Moderate Papalist)", {"STD": 4, "PAPMOD": 3, "PERSMOR": 2}],
            ["The principle is right but application involves prudential judgment. (Personalist, Casuist)", {"PERSMOR": 4, "CASUIST": 3, "PROG": 2, "NEOSCH": -3}],
            ["Should be reconsidered. Sensus fidelium has rejected it. (Liberal Catholic, Progressive)", {"PROG": 4, "LIBCATH": 5, "SYNOD": 2, "TRAD": -6, "NEOSCH": -5}]
        ],
        "axis_weights": {"RIGOR": 5}
    },
    {
        "text": "Carmelite spirituality (Teresa of Ávila, John of the Cross) emphasizes:",
        "options": [
            ["Interior prayer and mystical union - the soul's journey through mansions to divine marriage. (Carmelite)", {"CARM": 6, "EUCHMYST": 3, "CHART": 2, "PIETY": 3}],
            ["Valuable for contemplatives but most Catholics need active, engaged spirituality. (Jesuit, Dominican)", {"JES": 3, "DOM": 2, "SDB": 2, "OPUS": 2}],
            ["The 'dark night' teaches detachment from consolations - demanding but transformative. (Carmelite)", {"CARM": 5, "OCSO": 3, "CHART": 3, "CP": 2}],
            ["Mysticism is dangerous without strong doctrinal grounding and ecclesial oversight. (Neo-Scholastic, Traditionalist)", {"NEOSCH": 3, "TRAD": 2, "DOM": 2, "CARM": -2}]
        ],
        "axis_weights": {"PIETY": 5}
    },
    {
        "text": "The Mercedarian fourth vow - to give one's life for captives if necessary - represents:",
        "options": [
            ["Heroic charity. The willingness to die for another's freedom is profoundly Christlike. (Mercedarian)", {"MERC": 6, "CM": 3, "FRAN": 2, "CP": 2}],
            ["A noble historical charism that should be adapted for modern forms of captivity (trafficking, addiction). (Mercedarian, Vincentian)", {"MERC": 4, "CM": 3, "WORKERCATH": 2, "PROG": 2}],
            ["Inspiring but exceptional. Most are not called to such radical sacrifice. (Mainstream, Moderate Papalist)", {"STD": 3, "PAPMOD": 2}],
            ["All religious should have this spirit of total self-gift, even if not vowed. (Carthusian, Cistercian/Trappist)", {"CHART": 3, "OCSO": 2, "CARM": 2, "MERC": 2}]
        ],
        "axis_weights": {"PIETY": 2}
    },
    {
        "text": "How should the Church relate to modern culture?",
        "options": [
            ["Resist: Modern culture is largely hostile to faith and natural law (Traditionalist, Integralist)", {"TRAD": 3, "INTEG": 3, "SSPX": 3, "NEOSCH": 2}],
            ["Engage critically: Affirm what is good, reject what contradicts faith (Mainstream, Reform of Reform)", {"STD": 2, "ROTR": 2, "PAPMOD": 2}],
            ["Adapt: The Church must speak modern language to be heard (Progressive, Liberal Catholic)", {"PROG": 3, "LIBCATH": 2}],
            ["Ressourcement: Return to sources to address modern questions freshly (Ressourcement, Neo-Augustinian)", {"RESS": 3, "NEOAUG": 2}]
        ],
        "axis_weights": {"LIT": 2}
    },
    {
        "text": "What is the value of Scholasticism today?",
        "options": [
            ["Perennially valid: Thomistic philosophy and theology remain normative", {"THOMMETA": 3, "THOM": 3, "DOM": 2, "NEOSCH": 3}],
            ["Valuable but not exclusively: Other traditions have insights (Mainstream, Ressourcement)", {"STD": 2, "RESS": 2}],
            ["Historically important but modern thought has surpassed it (Progressive)", {"PROG": 2, "LIBCATH": 1}],
            ["One approach among many; Scotist, Augustinian alternatives are equally valid", {"SCOT": 2, "FRANC": 2, "AUG": 1}]
        ],
        "axis_weights": {}
    },
    {
        "text": "What is your view on the 'fewness of the saved' — the traditional teaching that few attain eternal salvation?",
        "options": [
            ["A virtual consensus of the Fathers, Doctors, and saints. Our Lord's words 'narrow is the gate' should be taken at face value. (Strict Augustinian, Jansenist)", {"AUGP": 5, "JANS": 4, "TRAD": 4, "NEOSCH": 3, "ANTIMOD": 3, "COMMUN": -3, "PROG": -4}],
            ["Most are likely lost through their own fault, but the elect may be more numerous and surprising in composition than some expect. Garrigou-Lagrange held this nuanced view. (Thomist, Dominican)", {"THOM": 4, "DOM": 3, "AUG": 3, "STD": 2, "BANEZ": 2, "TRAD": 2}],
            ["We may hope that a significant portion of practicing Christians receive the grace of final perseverance, though certainty eludes us. (Mainstream, Moderate Papalist)", {"STD": 4, "PAPMOD": 3, "CARM": 2, "BENED": 2, "JES": 2, "DEVPROG": 2}],
            ["The question reflects an overly pessimistic spirituality. God's salvific will is universal and His mercy should inspire confidence, not fear. (Progressive, Liberal Catholic)", {"PROG": 4, "LIBCATH": 4, "COMMUN": 3, "PERSMOR": 2, "TRAD": -4, "AUGP": -3}],
            ["Speculative questions about numbers distract from the call to personal holiness. Work out your own salvation with fear and trembling. (Carmelite, Carthusian)", {"CARM": 4, "CHART": 3, "BENED": 3, "OPUS": 2, "STD": 2}]
        ],
        "axis_weights": {"ESCH": 4, "RIGOR": 3, "GRACE": 2}
    },
    {
        "text": "How should we understand 'Extra Ecclesiam nulla salus' (Outside the Church there is no salvation)?",
        "options": [
            ["Strictly: Only those validly baptized who die within the visible bounds of the Roman Catholic Church can be saved. No exceptions. (Sedevacantist, SSPX-leaning)", {"SEDE": 5, "SSPX": 4, "ANTIMOD": 3, "TRAD": 3, "NEOSCH": 2, "PROG": -5, "LIBCATH": -5}],
            ["The Church is the ordinary and normative means of salvation, but invincible ignorance and baptism of desire are genuine possibilities recognized by Tradition. (Thomist, Mainstream)", {"THOM": 4, "STD": 4, "PAPMOD": 3, "DOM": 2, "DEVPROG": 2, "TRAD": 2}],
            ["Separated Christians have real though imperfect communion; their obligation is to seek truth, but diminished culpability is possible. (Thomist, Dominican)", {"THOM": 3, "DOM": 3, "ECUMON": 5, "DEVPROG": 3, "PAPMOD": 2, "SEDE": -3}],
            ["All who die in the state of grace are saved, however they came to it. The Church's boundaries are more mysterious than juridical. (Progressive, Liberal Catholic)", {"PROG": 4, "LIBCATH": 4, "COMMUN": 3, "RESS": 2, "EASTECC": 2, "TRAD": -3, "NEOSCH": -3}],
            ["Those with valid sacraments (Eastern Orthodox, some Anglicans) are in a different category than Protestant communities without valid orders.", {"ORTHOPH": 4, "EASTECC": 4, "ORDINAR": 3, "TRAD": 2, "THOM": 2, "ECUMON": 2}]
        ],
        "axis_weights": {"PAPAL": 1, "RIGOR": 2, "ESCH": 2}
    },
    {
        "text": "What is the status of the deuterocanonical books (e.g., Sirach, Wisdom, Maccabees)?",
        "options": [
            ["Fully canonical Scripture, equal in authority to all other biblical books. (Tridentine, Thomist)", {"TRIDSAC": 4, "THOM": 3, "STD": 3, "JANS": 2, "BENED": 2}],
            ["Valuable for edification but not for establishing doctrine (apocrypha). (Reformed, Lutheran)", {"REFORM": 4, "LUTHERAN": 3}],
            ["Deuterocanonical: secondary canon, useful and often read liturgically. (Anglican, Methodist)", {"ANGLICAN": 5}],
            ["The question of the canon should be approached with more nuance than rigid categories. (Progressive)", {"PROG": 3, "LIBCATH": 2}]
        ],
        "axis_weights": {"SCRIPT": 3}
    },
    {
        "text": "How many Ecumenical Councils are binding on the Church?",
        "options": [
            ["Twenty-one, from Nicaea I (325) to Vatican II (1962-65). (Mainstream, Ultramontane)", {"STD": 4, "ULTRA": 3, "PAPMOD": 3, "TRIDSAC": 2}],
            ["Seven, from Nicaea I to Nicaea II (787); later councils are Western synods. (Eastern Orthodox)", {"EORTHO": 5, "ORTHOPH": 4, "EASTECC": 2}],
            ["Three, through Ephesus (431); Chalcedon introduced divisive innovations. (Oriental Orthodox, Coptic Orthodox)", {"EORTHO": 10}],
            ["The number is less important than continuity with apostolic tradition. (Ressourcement, Developmental)", {"RESS": 3, "DEVPROG": 3, "COMMUN": 2}]
        ],
        "axis_weights": {"PAPAL": 3, "SCRIPT": 2}
    },
    {
        "text": "What is the proper understanding of original sin?",
        "options": [
            ["Inherited guilt and corruption: all humanity sinned 'in Adam' and inherits both guilt and concupiscence. (Augustinian, Thomist)", {"AUG": 4, "THOM": 2, "JANS": 3, "TRIDSAC": 2}],
            ["Inherited mortality and corruption but not personal guilt; we sin because we are mortal. (Eastern Orthodox)", {"EORTHO": 4, "ORTHOPH": 3, "EASTECC": 3, "PALAM": 2}],
            ["Original sin is primarily privation: loss of original justice and sanctifying grace. (Thomist, Mainstream)", {"THOM": 4, "STD": 3, "TRIDSAC": 2}],
            ["The doctrine needs restatement: evolutionary science changes how we understand human origins. (Progressive, Liberal Catholic)", {"PROG": 4, "LIBCATH": 3}]
        ],
        "axis_weights": {"GRACE": 4}
    },
    {
        "text": "Which figure would you most like to see the Catholic Church canonize or rehabilitate?",
        "options": [
            ["Blaise Pascal - defender of Augustinian grace against Jesuit laxism. (Jansenist, Strict Augustinian)", {"JANS": 5, "AUGP": 4, "AUG": 3, "TUTIOR": 2}],
            ["Réginald Garrigou-Lagrange, O.P. - champion of strict Thomism and spiritual master. (Strict Thomist, Dominican)", {"THOM": 8, "DOM": 4, "TRAD": 2, "ANTIMOD": 2}],
            ["Meister Eckhart, O.P. - profound mystic whose condemnation was perhaps too hasty. (Neo-Platonist, Dominican)", {"NEOPLAT": 5, "DOM": 3, "CARM": 2, "EUCHMYST": 2, "RESS": 2}],
            ["Marsilio Ficino - Christian Platonist who harmonized faith and ancient wisdom. (Neo-Platonist, Ressourcement)", {"NEOPLAT": 5, "RESS": 3, "COMMUN": 2, "RADORTH": 2}],
            ["Antonio Rosmini - philosopher vindicated after long suspicion, model of patient orthodoxy. (Developmental, Ressourcement)", {"DEVPROG": 4, "RESS": 3, "COMMUN": 3, "LIBCATH": 2}],
            ["Henri de Lubac, S.J. - ressourcement giant who suffered and was vindicated. (Ressourcement, Communio School)", {"RESS": 5, "COMMUN": 4, "NEOAUG": 3, "JES": 2}],
            ["Archbishop Marcel Lefebvre - defender of Tradition against modernist corruption. (SSPX-leaning, Traditionalist)", {"SSPX": 5, "TRAD": 4, "SEDE": 2, "ANTIMOD": 3}],
            ["Dorothy Day - model of radical Gospel poverty and works of mercy. (Worker-Catholic, Distributist)", {"WORKERCATH": 5, "DISTRIBUT": 4, "SOCDEM": 3, "FRAN": 2}]
        ],
        "axis_weights": {"PIETY": 3, "RIGOR": 2}
    },
    {
        "text": "How ought the Pope deal with regional Bishops' Conferences in defiance of orthodox teaching, such as the Synodal Path in Germany?",
        "options": [
            ["Swift and decisive suppression. The Pope should use his full authority to discipline wayward bishops, remove those who persist in error, and if necessary suppress the conference entirely. Heterodoxy cannot be tolerated. (Ultramontane, Integralist)", {"ULTRA": 4, "INTEG": 7, "ANTIMOD": 3, "NEOSCH": 2, "TRAD": 2}],
            ["Firm correction within traditional structures. The Pope should clearly restate orthodox doctrine, require retraction of errors, and use canonical measures against persistent dissenters - but through established processes, not raw power. (Reform of the Reform, Traditionalist)", {"ROTR": 4, "TRAD": 3, "PAPMOD": 3, "COMMUN": 2, "BENED": 2, "STD": 1}],
            ["Patient dialogue and accompaniment. The Church must listen to the concerns driving these movements, discern what the Spirit may be saying through them, and find ways to maintain communion while allowing legitimate diversity. (Progressive, Synodalist)", {"PROG": 4, "SYNOD": 4, "LIBCATH": 3, "PERSMOR": 2, "DEVPROG": 2}],
            ["Formal doctrinal intervention but respect for subsidiarity. The CDF should issue corrections and the Pope should teach clearly, but local churches have legitimate autonomy. Heavy-handed centralization would be counter-productive. (Moderate Papalist, Standard Catholic)", {"PAPMOD": 3, "STD": 3, "EASTECC": 2, "PAPMIN": 2, "CONCIL": 1}]
        ],
        "axis_weights": {"PAPAL": 4, "RIGOR": 2}
    },
    {
        "text": "Do you agree with Benedict XVI's vision of a smaller, more orthodox Church as potentially ideal?",
        "options": [
            ["Yes, and it would be the best thing to happen to the Church. A smaller, fervent remnant living authentic Catholicism is preferable to a bloated institution full of nominal believers and heterodox clergy. Quality over quantity. (Traditionalist, SSPX-leaning)", {"TRAD": 4, "SSPX": 3, "INTEG": 3, "ANTIMOD": 3, "ROTR": 2, "COMMUN": 2}],
            ["The problems of laxist, progressive clergy and lukewarm piety are generational. Progress is already being made among priests and laity under 50. Organic renewal is happening without requiring a dramatic purge. (Reform of the Reform, Communio School)", {"ROTR": 4, "COMMUN": 4, "STD": 3, "BENED": 2, "DEVPROG": 2}],
            ["This would require clarifying the ambiguities built into Vatican II. The Council's documents admit of both traditional and progressive readings; only authoritative clarification in a traditional direction could achieve genuine renewal. (Traditionalist, Integralist)", {"TRAD": 3, "INTEG": 3, "ROTR": 2, "ANTIMOD": 2, "NEOSCH": 2, "THOM": 1}],
            ["This would require undoing the errors of Vatican II. The Council itself, not just its implementation, introduced novelties incompatible with Tradition. Only a future Council or Pope correcting these errors can restore the Church. (SSPX-leaning, Sedevacantist-adjacent)", {"SSPX": 4, "SEDE": 2, "TRAD": 3, "ANTIMOD": 3, "INTEG": 2}],
            ["No. Growth from the Church in the Global South will supersede Europe, and we must not have a Eurocentric church based on strict interpretations of rules and dogma. The future is inculturation and pastoral flexibility. (Progressive, Catholic Universalist)", {"PROG": 4, "CATHUNIV": 4, "LIBCATH": 3, "SYNOD": 2, "PERSMOR": 2}],
            ["In the West this would be ideal, but the Church is growing in the Global South. We should accept a smaller Western church while celebrating growth elsewhere. Different regions may need different pastoral approaches. (Standard Catholic, Moderate)", {"STD": 3, "PAPMOD": 2, "CATHUNIV": 2, "COMMUN": 2, "EASTECC": 1}]
        ],
        "axis_weights": {"LIT": 2, "RIGOR": 3, "PAPAL": 1}
    },
    {
        "text": "Which post-conciliar Pope do you most admire?",
        "options": [
            ["Paul VI - He faithfully implemented the Council while holding the line on Humanae Vitae. His suffering witness during the post-conciliar crisis was heroic. (Progressive-Moderate, Standard Catholic)", {"PROG": 2, "STD": 3, "PAPMOD": 3, "DEVPROG": 2, "TRADUM": 2}],
            ["John Paul I - His brief pontificate suggested a simpler, more pastoral papacy. We can only imagine what renewal he might have brought. (Progressive, Pastoral)", {"PROG": 2, "LIBCATH": 2, "PERSMOR": 2, "STD": 2, "PAPMIN": 1}],
            ["St. John Paul II - The Great Pope who defeated Communism, taught magnificently on faith and morals, and revitalized Catholic identity worldwide. (Standard Catholic, Personalist)", {"STD": 4, "PERSMOR": 4, "PAPMOD": 3, "INTEG": 2, "THOMMOR": 2, "COMMUN": 2}],
            ["Benedict XVI - The theologian-Pope who diagnosed the dictatorship of relativism, promoted liturgical renewal, and offered the hermeneutic of continuity. (Reform of the Reform, Communio School)", {"ROTR": 5, "COMMUN": 5, "TRAD": 3, "BENED": 3, "RESS": 2, "THOM": 2}],
            ["Francis - The Pope of mercy, peripheries, and synodality who is renewing the Church for the 21st century and refocusing on the poor and marginalized. (Progressive, Synodalist)", {"PROG": 4, "SYNOD": 4, "LIBCATH": 3, "CATHUNIV": 3, "WORKERCATH": 2, "FRAN": 2}],
            ["None of them adequately preserved Tradition. The post-conciliar papacy has been a disaster requiring future correction. (SSPX-leaning, Sedevacantist-adjacent)", {"SSPX": 4, "SEDE": 3, "TRAD": 2, "ANTIMOD": 3, "INTEG": 2}]
        ],
        "axis_weights": {"PAPAL": 2, "LIT": 2}
    },
    {
        "text": "What is your personal outlook for the future of the Catholic Church?",
        "options": [
            ["Optimistic - The gates of hell shall not prevail. Despite current troubles, renewal movements, young orthodox vocations, and the growth of the Global South Church point to a bright future. (Standard Catholic, Hopeful)", {"STD": 4, "PAPMOD": 2, "CATHUNIV": 2, "DEVPROG": 2, "COMMUN": 2}],
            ["Cautiously hopeful - A smaller, purer Church is emerging in the West while the faith flourishes elsewhere. The 'biological solution' will resolve many current problems. (Reform of the Reform, Communio School)", {"ROTR": 4, "COMMUN": 4, "TRAD": 2, "BENED": 2, "STD": 2}],
            ["Concerned but trusting Divine Providence - We are in a deep crisis, perhaps the worst since the Arian heresy. But God will raise up saints to renew the Church as He always has. (Traditionalist, Prayerful)", {"TRAD": 4, "CARM": 2, "BENED": 2, "INTEG": 2, "ANTIMOD": 2, "SSPX": 1}],
            ["Dark before the dawn - Things will get worse before they get better. A great chastisement or major supernatural intervention may be necessary. Fatima's warnings remain unfulfilled. (Traditionalist Apocalyptic, Marian)", {"TRAD": 3, "SSPX": 3, "INTEG": 2, "ANTIMOD": 2, "SEDE": 1, "CARM": 2}],
            ["Progressive transformation - The Church is finally updating for the modern world. What looks like decline to some is actually healthy pruning and the Spirit leading us to new forms of being Church. (Progressive, Developmental)", {"PROG": 4, "DEVPROG": 3, "LIBCATH": 3, "SYNOD": 2, "PERSMOR": 2}],
            ["The institutional Church may collapse, but the Faith will endure in remnant communities maintaining Tradition until restoration comes. (SSPX-leaning, Remnant)", {"SSPX": 4, "SEDE": 2, "TRAD": 3, "INTEG": 2, "ANTIMOD": 2}]
        ],
        "axis_weights": {"ESCH": 3, "LIT": 1}
    },
    {
        "text": "How do you view the SSPX's irregular canonical status and their announced intention to consecrate bishops again?",
        "options": [
                [
                        "The real issue is doctrinal: Vatican II's teaching on religious liberty, ecumenism, and collegiality contradicts prior magisterium. The Church persecutes the SSPX while tolerating far worse from China and the German synodal path.",
                        {"SSPX": 5, "TRAD": 3, "ANTIMOD": 3, "SEDE": 2, "INTEG": 2}
                ],
                [
                        "Without Lefebvre, the FSSP, IBP, ICKSP, and diocesan TLM communities wouldn't exist. He preserved what would have been lost. History will vindicate him.",
                        {"SSPX": 4, "TRAD": 3, "ROTR": 1, "ANTIMOD": 2}
                ],
                [
                        "Consecrating bishops without mandate was wrong, and doing it again is worse \u2014 but I sympathize with those who love our liturgical heritage. I hope we can correct bad interpretations of Vatican II, reform the Novus Ordo toward Sacrosanctum Concilium, and unite the Church as Benedict XVI wanted.",
                        {"ROTR": 4, "COMMUN": 3, "BENED": 2, "TRAD": 2, "STD": 2}
                ],
                [
                        "I appreciate the TLM, but the SSPX are in open defiance of the Magisterium. Summorum Pontificum should be restored so people can attend the TLM through Ecclesia Dei communities and diocesan parishes without schism.",
                        {"STD": 3, "PAPMOD": 3, "ROTR": 2, "TRAD": 1, "BENED": 1}
                ],
                [
                        "I have mixed feelings about liturgical abuses, but the reformed Mass is the Church's standard for good reason. The SSPX needs to accept this and regularize.",
                        {"STD": 2, "PAPMOD": 2, "PROG": 2, "TRADUM": 2}
                ],
                [
                        "They represent the worst of the traditionalist movement \u2014 making an idol of a Mass that was antiquated, inflexible, and often celebrated irreverently in the decades before Vatican II.",
                        {"PROG": 4, "LIBCATH": 3, "TRADUM": 3, "SYNOD": 2, "TRAD": -3, "SSPX": -4}
                ]
        ],
        "axis_weights": {"LIT": 4, "PAPAL": 3}
}
];

const QUESTION_TOPICS = {
    0: {
        topic: "Biblical Hermeneutics and Interpretation",
        description: "The proper method of interpreting Scripture: patristic spiritual exegesis, scholastic literal-sense priority, historical-critical methods, or contemporary approaches.",
        reading: "Dei Verbum §§11-13, Pontifical Biblical Commission documents, de Lubac\'s \'Medieval Exegesis\', Ratzinger\'s \'Jesus of Nazareth\' preface",
        prompt: "What are the main approaches to biblical interpretation in Catholic theology? Explain patristic four-fold exegesis, Thomistic interpretation, historical-critical method, and canonical approaches. Present each fairly."
    },
    1: {
        topic: "Bible Translation Philosophy",
        description: "Approaches to Bible translation: formal equivalence, dynamic equivalence, liturgical tradition, and pastoral accessibility.",
        reading: "Liturgiam Authenticam (2001), Comme le Prévoit (1969), various Bible translation prefaces",
        prompt: "What are the main philosophies of Bible translation? Explain formal equivalence, dynamic equivalence, and liturgical translation principles. How do different Catholic perspectives view the balance?"
    },
    2: {
        topic: "Catholicism and Nationalism",
        description: "Catholic approaches to national identity and loyalty.",
        reading: "Mit brennender Sorge, Summi Pontificatus, Fratelli Tutti, MacIntyre on patriotism",
        prompt: "What are Catholic approaches to nationalism? Explain legitimate patriotism, the dangers of excessive nationalism, Catholic universalism, and how to balance local and universal loyalties."
    },
    3: {
        topic: "Digital Evangelization",
        description: "How Catholics should engage lay apostolate and evangelization online.",
        reading: "Various Vatican documents on media, Bishop Barron\'s approach",
        prompt: "How should Catholics approach lay apostolates and evangelization in the digital space? What opportunities and dangers exist? How can social media serve the Gospel?"
    },
    4: {
        topic: "Loss of Salvation",
        description: "Whether a justified person can fall from grace and lose salvation.",
        reading: "Trent Session 6, Hebrews 6, \'Once saved always saved\' debate",
        prompt: "Can a justified person lose salvation? Explain the Catholic position, compare with \'once saved always saved\' (perseverance of the saints), and the biblical evidence."
    },
    5: {
        topic: "The Problem of Universals",
        description: "The metaphysical status of universal concepts like \'humanity\' or \'justice\'.",
        reading: "Aquinas\' De Ente et Essentia, Boethius, medieval commentaries on Porphyry",
        prompt: "What is the problem of universals? Explain realism, nominalism, and moderate realism (conceptualism). Where does Thomism fall and why does it matter theologically?"
    },
    6: {
        topic: "The Analogy of Being",
        description: "How human concepts can apply meaningfully to God - analogy versus univocity.",
        reading: "Aquinas ST I q.13, Fourth Lateran Council, Scotus on univocity, Przywara\'s \'Analogia Entis\'",
        prompt: "What is the analogy of being (analogia entis)? How do Thomists and Scotists differ on how we can speak meaningfully about God? Why does this matter theologically?"
    },
    7: {
        topic: "Sacramental Theology Preferences",
        description: "Which approach to sacramental theology resonates most.",
        reading: "Aquinas ST III, Eastern sacramental theology, Scheeben",
        prompt: "What are the different approaches to sacramental theology? Compare Thomist (causality focus), Augustinian (sign focus), and Eastern (mystical-transformative) approaches."
    },
    8: {
        topic: "Nominalism Assessment",
        description: "Evaluating the nominalist tradition and its influence.",
        reading: "Ockham\'s writings, Gillespie\'s \'Theological Origins of Modernity\'",
        prompt: "How should we assess the nominalist tradition (Ockham, etc.)? Did it undermine realist metaphysics destructively, or offer valuable insights? What is its legacy?"
    },
    9: {
        topic: "Theosis/Divinization",
        description: "How central is theosis to understanding salvation.",
        reading: "Athanasius, Eastern Fathers, de Lubac, Catechism §460",
        prompt: "How central is theosis (divinization) to understanding salvation? Explain the patristic teaching, its place in Eastern theology, and whether Latin theology adequately incorporates it."
    },
    10: {
        topic: "The Goal of the Christian Life",
        description: "What the Christian life is ultimately oriented toward - beatific vision, theosis, or other framings.",
        reading: "Catechism §§1-3, 1023-1029; Aquinas ST I-II q.3 (on beatitude); Eastern theology on theosis",
        prompt: "What is the ultimate goal of the Christian life according to Catholic teaching? Explain beatific vision, theosis/divinization, and how different theological traditions frame the end of human life."
    },
    11: {
        topic: "The Absolute Primacy of Christ",
        description: "Whether the Incarnation would have occurred without the Fall.",
        reading: "Scotus\' Ordinatio III, Aquinas ST III q.1 a.3, Col 1:15-20",
        prompt: "Would Christ have become incarnate if Adam had not sinned? Explain the Scotist position (absolute primacy) versus the Thomist position (Incarnation for redemption)."
    },
    12: {
        topic: "Mental Prayer in Christian Life",
        description: "The importance and practice of discursive meditation.",
        reading: "Teresa of Avila, Francis de Sales\' \'Introduction to the Devout Life\', Catechism §§2705-2708",
        prompt: "How important is mental prayer in the Christian life? Explain its necessity for spiritual growth, methods of meditation, and different schools of mental prayer."
    },
    13: {
        topic: "Christ\'s Human Knowledge",
        description: "What Jesus knew during His earthly life and how He knew it.",
        reading: "Aquinas ST III q.9-12, Pius XII\'s \'Mystici Corporis\', CDF 1985 notification",
        prompt: "How should we understand Christ\'s human knowledge during His earthly life? Did He know everything? Explain beatific, infused, and acquired knowledge in Christ\'s human intellect."
    },
    14: {
        topic: "Christ\'s Divine and Human Wills",
        description: "How Jesus\' two wills relate - dyothelitism versus monothelitism.",
        reading: "Third Council of Constantinople (681), Aquinas ST III q.18, Catechism §475",
        prompt: "What is the relationship between Christ\'s divine and human wills? Explain dyothelitism (two wills), why monothelitism was condemned, and how the wills cooperate."
    },
    15: {
        topic: "Communication of Idioms",
        description: "How attributes of one nature can be predicated of Christ in the other nature.",
        reading: "Cyril of Alexandria, Council of Ephesus, Aquinas ST III q.16",
        prompt: "What is the communication of idioms (communicatio idiomatum)? Explain how we can say \'God died\' and \'Mary is the Mother of God\' and what limits apply to such statements."
    },
    16: {
        topic: "Christ\'s Descent into Hell",
        description: "What happened between Christ\'s death and resurrection.",
        reading: "1 Peter 3:19-20, Catechism §§631-635, Balthasar\'s \'Mysterium Paschale\'",
        prompt: "What did Christ do between His death and resurrection? Explain the descent into hell/Sheol, liberation of the righteous dead, and the theological significance of Holy Saturday."
    },
    17: {
        topic: "Lutheran-Catholic Convergence",
        description: "Whether Lutheran positions on Eucharist and justification could be reconciled with Catholicism.",
        reading: "Joint Declaration (1999), Ratzinger on Luther, Group of Dombes",
        prompt: "Could Lutheran positions on Eucharist and justification be reconciled with Catholic teaching? What modifications would be needed? What did the Joint Declaration achieve?"
    },
    18: {
        topic: "The Filioque Controversy",
        description: "Whether the Filioque can be omitted from the Creed for reunion.",
        reading: "Council of Florence, Photius, Councils on the Filioque, Siecienski\'s \'The Filioque\'",
        prompt: "Can we omit the Filioque from the Creed for reunion with the Orthodox? Explain the theological issues, historical development, and various Catholic positions on this question."
    },
    19: {
        topic: "Carmelite Spirituality",
        description: "The mystical teaching of Teresa of Ávila and John of the Cross.",
        reading: "Teresa\'s \'Interior Castle\', John\'s \'Ascent of Mount Carmel\', \'Dark Night\'",
        prompt: "What does Carmelite spirituality (Teresa of Ávila, John of the Cross) emphasize? Explain stages of prayer, dark nights, and the goal of transforming union."
    },
    20: {
        topic: "The Doctrine of Justification",
        description: "How sinners are reconciled to God - through infused righteousness, participation in Christ, or forensic declaration.",
        reading: "Council of Trent Session 6, Joint Declaration on Justification (1999), Catechism §§1987-2029, Aquinas ST I-II q.113",
        prompt: "Explain the Catholic doctrine of justification. How does it differ from Protestant views? What are the various emphases within Catholic theology - Thomist infusion, Augustinian participation, and others?"
    },
    21: {
        topic: "Growth in Justification",
        description: "Whether and how justification can increase after baptism through cooperation with grace.",
        reading: "Council of Trent Session 6, Chapters 10-11; Catechism §2010; Aquinas ST I-II q.114",
        prompt: "Can justification increase after baptism according to Catholic teaching? Explain the Tridentine doctrine of growth in grace and various theological interpretations."
    },
    22: {
        topic: "Justification and Sanctification",
        description: "The relationship between being declared/made righteous and the process of being made holy.",
        reading: "Trent Session 6, Joint Declaration on Justification (1999), Catechism §§1989-1995",
        prompt: "How are justification and sanctification related in Catholic theology? Are they the same thing or distinct? Compare Catholic, Lutheran, and Reformed understandings."
    },
    23: {
        topic: "Concupiscence After Baptism",
        description: "The nature and moral status of disordered desires remaining after baptismal regeneration.",
        reading: "Trent Session 5 (Decree on Original Sin), Catechism §§1264, 2515; Augustine\'s anti-Pelagian writings",
        prompt: "What is concupiscence and how does Catholic theology understand its status after baptism? Is it sin, the \'tinder of sin,\' or morally neutral? Compare Catholic and Protestant views."
    },
    24: {
        topic: "Assurance of Salvation",
        description: "Whether Christians can have certainty about their present state of grace.",
        reading: "Trent Session 6, Chapter 9 & Canon 13-14; Catechism §2005; 1 John 5:13",
        prompt: "Can a Christian know with certainty they are in the state of grace? Explain the Catholic position (moral certainty vs. absolute certainty) versus Protestant views on assurance."
    },
    25: {
        topic: "Final Perseverance",
        description: "The gift of persisting in grace until death - is it guaranteed, a special gift, or uncertain?",
        reading: "Trent Session 6, Chapter 13; Augustine\'s \'De Dono Perseverantiae\'; Catechism §2016, 162",
        prompt: "What is final perseverance in Catholic theology? Is it a special gift, the ordinary result of cooperation with grace, or uncertain? Compare Augustinian, Thomist, and Molinist views."
    },
    26: {
        topic: "Grace and Human Freedom",
        description: "How divine grace relates to human free will in salvation.",
        reading: "Trent Session 6, Catechism §§1993-2000, De Auxiliis controversy documents",
        prompt: "How does God\'s grace relate to human freedom in salvation? Explain Thomist (Bañezian), Molinist, and Augustinian positions on the grace-freedom relationship."
    },
    27: {
        topic: "Predestination",
        description: "God\'s eternal decree regarding salvation - unconditional, conditional, or based on foreseen merits.",
        reading: "Romans 8-9, Aquinas ST I q.23, Catechism §600, Council of Orange (529)",
        prompt: "How should Catholics understand predestination? Explain the range from double predestination to predestination post praevisa merita, and where Catholic teaching draws boundaries."
    },
    28: {
        topic: "Infralapsarianism vs Supralapsarianism",
        description: "Whether God\'s decree of predestination logically precedes or follows His permission of the Fall.",
        reading: "Aquinas ST I q.23, Garrigou-Lagrange\'s \'Predestination\', Reformed confessions for comparison",
        prompt: "What is the difference between infralapsarianism and supralapsarianism? How do Catholic theologians approach this question of the logical order of divine decrees?"
    },
    29: {
        topic: "Sufficient and Efficacious Grace",
        description: "The distinction between grace that enables and grace that achieves its salvific effect.",
        reading: "De Auxiliis controversy documents, Garrigou-Lagrange, Molina\'s \'Concordia\'",
        prompt: "What is the difference between sufficient and efficacious grace? Explain how Thomists, Molinists, and Augustinians understand why some grace achieves its effect and some does not."
    },
    30: {
        topic: "Sacramental Causality",
        description: "How the sacraments cause grace - physical, moral, or instrumental causality.",
        reading: "Aquinas ST III q.62, Catechism §§1127-1129, Scheeben\'s \'The Mysteries of Christianity\'",
        prompt: "How do the sacraments cause grace? Explain ex opere operato, instrumental causality, and the debate between physical and moral causality theories."
    },
    31: {
        topic: "Historical Catholic Soteriology and Monergism",
        description: "Whether early Catholic teaching was essentially monergistic.",
        reading: "Augustine, Prosper, Council of Orange (529), Gregory the Great",
        prompt: "Was historical Catholic soteriology (Augustine, Prosper, Council of Orange) essentially monergistic? What role did human cooperation play? How did this develop over time?"
    },
    32: {
        topic: "Assessing Jansenism",
        description: "How to evaluate the Jansenist movement.",
        reading: "Augustine\'s anti-Pelagian writings, Jansen\'s \'Augustinus\', papal condemnations",
        prompt: "How should we assess the Jansenist movement? Was it authentic Augustinianism or heresy? Explain its teachings, the papal condemnations, and its lasting influence."
    },
    33: {
        topic: "Eucharistic Presence Across Traditions",
        description: "How Christ is present in the Eucharist according to different traditions.",
        reading: "Trent, Lutheran confessions, Reformed views, Orthodox theology",
        prompt: "How is Christ present in the Eucharist according to different Christian traditions? Compare transubstantiation, sacramental union, spiritual presence, and Eastern approaches."
    },
    34: {
        topic: "The Filioque",
        description: "Understanding the clause \'and the Son\' in the Creed.",
        reading: "Council of Florence, Photius, Siecienski\'s \'The Filioque\'",
        prompt: "How should we understand the filioque clause? Explain the Western position (Spirit proceeds from Father and Son), Eastern objection, and whether reconciliation is possible."
    },
    35: {
        topic: "Chalcedonian Christology",
        description: "How to understand the \'two natures\' formula.",
        reading: "Council of Chalcedon, Cyril of Alexandria, modern Christological debates",
        prompt: "How should we understand Chalcedon\'s \'two natures\' Christology? Explain Alexandrian versus Antiochene emphases, and how to avoid Nestorianism and Monophysitism."
    },
    36: {
        topic: "Church Unity",
        description: "How the Church\'s unity is properly maintained.",
        reading: "Lumen Gentium, Unitatis Redintegratio, various ecclesiologies",
        prompt: "How is the Church\'s unity properly maintained? Compare Roman primacy, conciliarity, doctrinal agreement, and communion models. What constitutes full versus partial communion?"
    },
    37: {
        topic: "Eucharistic Presence: Theological Models",
        description: "How Christ is present in the Eucharist — exploring Thomist transubstantiation, Scotist formal-metaphysical approaches, Suarezian non-corporeal presence, Augustinian sign-reality models, patristic veiled presence, Eastern liturgical-mystical participation, and Ratramnian spiritual-real presence.",
        reading: "Trent Session 13, Catechism §§1373-1381, Aquinas ST III q.75-77, Mysterium Fidei (Paul VI), Scotus Ordinatio IV d.11, Suárez De Eucharistia, Ratzinger \'God is Near Us\'",
        prompt: "Explain the various Catholic theological models of Eucharistic presence: Thomist transubstantiation, Scotist formal-metaphysical approach, Suárezian non-corporeal substance, Augustinian sacramentum-res, patristic veiled presence, Eastern mystical participation, and Ratramnian spiritual-real presence. Present each fairly."
    },
    38: {
        topic: "Ex Opere Operato",
        description: "The principle that sacraments work by the rite performed, not the minister\'s holiness.",
        reading: "Trent Session 7, Catechism §§1127-1128, Augustine against the Donatists",
        prompt: "What does ex opere operato mean? What are its limits? Explain the difference between valid and fruitful sacraments, and how recipient disposition matters."
    },
    39: {
        topic: "Liturgical Orientation (Ad Orientem)",
        description: "Which direction the priest should face during the Eucharistic Prayer.",
        reading: "Ratzinger\'s \'Spirit of the Liturgy\', Lang\'s \'Turning Towards the Lord\', GIRM",
        prompt: "Which direction should the priest face during the Eucharistic Prayer? Explain ad orientem (toward the East/altar) versus versus populum (toward the people) and the theological arguments."
    },
    40: {
        topic: "Manner of Receiving Communion",
        description: "How Holy Communion should be received - kneeling/standing, tongue/hand.",
        reading: "Redemptionis Sacramentum, Memoriale Domini (1969), GIRM adaptations",
        prompt: "How should Holy Communion be received? Explain the arguments for communion on the tongue while kneeling versus in the hand while standing. What does Church law permit?"
    },
    41: {
        topic: "Post-Vatican II Liturgical Reform",
        description: "Evaluating the liturgical changes after the Council.",
        reading: "Sacrosanctum Concilium, Ratzinger\'s writings, Gamber\'s \'Reform of the Roman Liturgy\'",
        prompt: "How should we evaluate the post-Vatican II liturgical reforms? Did they faithfully implement the Council or go beyond it? Present traditionalist, reform-of-reform, and progressive views."
    },
    42: {
        topic: "The Traditional Latin Mass Today",
        description: "The proper place of the 1962 Missal in today\'s Church.",
        reading: "Summorum Pontificum (2007), Traditionis Custodes (2021), Quo Primum",
        prompt: "What is the proper place of the Traditional Latin Mass today? Explain the arguments for wide availability, restricted use, and eventual abolition. What did Benedict XVI and Francis teach?"
    },
    43: {
        topic: "Silence in the Liturgy",
        description: "The role of sacred silence in Catholic worship.",
        reading: "Sacrosanctum Concilium §30, GIRM §45, Sarah\'s \'The Power of Silence\'",
        prompt: "What is the role of silence in the liturgy? Explain different types of liturgical silence and how various Catholic perspectives value contemplative quiet versus active participation."
    },
    44: {
        topic: "Rubrical Exactness",
        description: "How important is precise adherence to liturgical rubrics.",
        reading: "Redemptionis Sacramentum, Summorum Pontificum, various liturgical legislation",
        prompt: "How important is rubrical exactness in liturgy? Explain the arguments for strict adherence versus pastoral flexibility, and what the Church\'s liturgical law actually requires."
    },
    45: {
        topic: "Non-Catholic Soteriology",
        description: "Which non-Catholic view of salvation is most compatible with Catholicism.",
        reading: "Joint Declaration on Justification, Catholic-Orthodox dialogues, comparative soteriology",
        prompt: "Which non-Catholic view of soteriology is most compatible with Catholic faith? Compare Lutheran, Reformed, Methodist, and Orthodox approaches to salvation."
    },
    46: {
        topic: "Assessing Vatican II",
        description: "Overall evaluation of the Second Vatican Council.",
        reading: "Council documents, de Mattei\'s \'Second Vatican Council\', O\'Malley\'s \'What Happened at Vatican II\'",
        prompt: "How should we assess the Second Vatican Council overall? Present traditionalist, conservative, moderate, and progressive evaluations of its teaching and implementation."
    },
    47: {
        topic: "Moral Theology Systems",
        description: "Which moral system one favors - probabilism, equiprobabilism, or tutiorism.",
        reading: "Alphonsus Liguori, manualist tradition, contemporary debates",
        prompt: "In moral theology, which system do you favor? Explain probabilism, equiprobabilism, probabiliorism, and tutiorism. What are the practical implications of each?"
    },
    48: {
        topic: "The Deuterocanonical Books",
        description: "The status of books like Sirach, Wisdom, and Maccabees.",
        reading: "Trent Session 4, Jerome\'s prologues, Protestant position",
        prompt: "What is the status of the deuterocanonical books? Explain the Catholic position (fully canonical), Protestant view (apocrypha), and the historical development of the canon."
    },
    49: {
        topic: "The Rule of Faith: Scripture, Tradition, and Magisterium",
        description: "The relationship between the three sources of Catholic authority and how they should be ranked or related.",
        reading: "Dei Verbum (Vatican II), Catechism §§74-100, Congar\'s \'Tradition and Traditions\', Ratzinger\'s \'God\'s Word\'",
        prompt: "Explain the Catholic understanding of the relationship between Scripture, Tradition, and the Magisterium. Present Ressourcement, Thomist, Ultramontane, and Traditionalist perspectives fairly without advocating for any position."
    },
    50: {
        topic: "Papal Authority",
        description: "The extent and limits of the pope\'s authority in the Church.",
        reading: "Pastor Aeternus (Vatican I), Lumen Gentium Ch. 3, Catechism §§880-887",
        prompt: "What is the extent of papal authority? Explain Ultramontane, moderate, and minimalist views. What are the limits of papal power according to Catholic teaching?"
    },
    51: {
        topic: "Episcopal Authority",
        description: "Where bishops\' authority comes from - directly from Christ or through the pope.",
        reading: "Lumen Gentium Ch. 3, Catechism §§880-887, Apostolos Suos (1998)",
        prompt: "Where does episcopal authority come from? Explain the debate between those who see it as immediately from Christ versus mediated through papal jurisdiction."
    },
    52: {
        topic: "Models of Church Unity",
        description: "What properly constitutes the unity of the Church - Roman primacy, communion, or federation.",
        reading: "Unitatis Redintegratio, Dominus Iesus (2000), Lumen Gentium §8",
        prompt: "What is the proper model of Church unity? Explain Roman centralization, communion ecclesiology, and conciliar models. How do these affect ecumenical dialogue?"
    },
    53: {
        topic: "Catholic Rulers and Episcopal Guidance",
        description: "Whether and how Catholic political leaders should defer to Church authority on faith and morals.",
        reading: "Quas Primas (Pius XI), Dignitatis Humanae, medieval political theology",
        prompt: "Should Catholic rulers defer to bishops on matters of faith and morals? Explain the historical relationship and how Vatican II\'s teaching on religious liberty affects this question."
    },
    54: {
        topic: "Vatican II\'s Doctrinal Status",
        description: "How to understand the authority of the Council\'s teachings.",
        reading: "Lumen Gentium, Nota Praevia, Benedict XVI\'s \'hermeneutic of continuity\' address (2005)",
        prompt: "How should we understand Vatican II\'s doctrinal status? Was it pastoral or doctrinal? Infallible or reformable? Explain different Catholic interpretations of the Council\'s authority."
    },
    55: {
        topic: "Evaluating Post-1958 Popes",
        description: "How to assess the pontificates from John XXIII onward.",
        reading: "Various papal biographies and assessments, Weigel, de Mattei, Faggioli",
        prompt: "How should Catholics evaluate the post-1958 popes? Present traditionalist, conservative, moderate, and progressive assessments of John XXIII through Francis."
    },
    56: {
        topic: "Resisting Roman Directives",
        description: "Whether and when a Catholic can resist or disobey papal or curial commands.",
        reading: "Aquinas on fraternal correction, Bellarmine on resisting a pope, Canon law on obedience",
        prompt: "Can a Catholic resist or disobey Roman directives? Explain the tradition of legitimate resistance, limits of papal authority, and when obedience may or must be withheld."
    },
    57: {
        topic: "Church Hierarchy and Immigration",
        description: "Evaluating episcopal statements on immigration policy.",
        reading: "USCCB statements, Catechism §2241, various episcopal conferences",
        prompt: "How should Catholics view the Church hierarchy\'s approach to immigration? Is it too liberal, appropriate, or insufficient? How do prudential judgments relate to binding teaching?"
    },
    58: {
        topic: "The De Auxiliis Controversy",
        description: "The Bañezian-Molinist debate on grace and freedom.",
        reading: "De Auxiliis documents, Garrigou-Lagrange, Molina\'s \'Concordia\'",
        prompt: "What was the De Auxiliis controversy between Bañezians and Molinists? Explain physical premotion versus middle knowledge, and why the Church declined to settle the question."
    },
    59: {
        topic: "Theological Certainty and Faith",
        description: "What degree of certainty theology can achieve.",
        reading: "Dei Filius, Aquinas on faith and reason, theological notes",
        prompt: "What degree of certainty can theology achieve? Explain the relationship between faith, theological reasoning, and different levels of doctrinal authority (de fide, sententia certa, etc.)."
    },
    60: {
        topic: "Divine Essence and Energies",
        description: "The Orthodox distinction between God\'s essence and energies.",
        reading: "Palamas, Council of Florence, Catholic-Orthodox dialogue",
        prompt: "What is the proper understanding of God\'s essence and energies? Explain the Palamite distinction, Thomist critique, and recent attempts at reconciliation."
    },
    61: {
        topic: "Icons in Christian Worship",
        description: "The role and theology of sacred images.",
        reading: "Nicaea II (787), Catechism §§1159-1162, Orthodox icon theology",
        prompt: "What is the role of icons in Christian worship? Explain the theology of icons, the iconoclast controversy, and the difference between veneration and worship."
    },
    62: {
        topic: "Papal Response to Heterodox Bishops\' Conferences",
        description: "How the Pope should respond to regional episcopal conferences that deviate from orthodox teaching.",
        reading: "Pastor Aeternus, Apostolos Suos (1998), CDF documents on the German Synodal Path",
        prompt: "How should the Pope respond to bishops\' conferences that deviate from orthodox teaching? Explain Ultramontane, traditionalist, progressive, and moderate approaches."
    },
    63: {
        topic: "Dissent from Non-Definitive Teaching",
        description: "The proper Catholic response when ordinary magisterial teaching seems doubtful or problematic.",
        reading: "Donum Veritatis (CDF 1990), Lumen Gentium §25, Catechism §892, Canon 752-753",
        prompt: "What is the proper Catholic posture toward non-definitive magisterial teaching that seems doubtful? Explain religious submission of intellect and will, and when legitimate dissent might be possible."
    },
    64: {
        topic: "Moral Theological Method",
        description: "The best approach to moral theology - natural law, virtue ethics, personalism, or manualism.",
        reading: "Veritatis Splendor, Aquinas ST I-II, Servais Pinckaers\' \'Sources of Christian Ethics\'",
        prompt: "What is the best approach to moral theology? Compare natural law, manualist tradition, virtue ethics revival, and personalist approaches. What are each\'s strengths and weaknesses?"
    },
    65: {
        topic: "Moral Absolutes and Exceptions",
        description: "Whether universal moral norms admit exceptions in concrete circumstances.",
        reading: "Veritatis Splendor §§79-83, Aquinas on intrinsically evil acts, proportionalism debates",
        prompt: "Do universal moral norms admit exceptions in concrete circumstances? Explain intrinsically evil acts, proportionalism, and why John Paul II rejected consequentialist reasoning."
    },
    66: {
        topic: "Probabilism in Moral Theology",
        description: "How confessors should handle doubtful moral cases.",
        reading: "St. Alphonsus Liguori\'s Moral Theology, Deman\'s \'Probabilisme\'",
        prompt: "What is probabilism and how should a confessor handle doubtful cases? Explain probabilism, probabiliorism, equiprobabilism, and tutiorism. What did Alphonsus Liguori teach?"
    },
    67: {
        topic: "The Manualist Tradition",
        description: "The value and limits of the moral theology manuals used in seminary formation.",
        reading: "Noldin, Davis, Prümmer manuals; Pinckaers\' critique; Cessario\'s defense",
        prompt: "What is the value of the manualist tradition in moral theology? Explain its strengths (clarity, practicality) and criticisms (legalism, minimalism). Should it be recovered?"
    },
    68: {
        topic: "Choosing a Religious Order",
        description: "Which religious order\'s charism and spirituality best fits one\'s vocation.",
        reading: "Various order constitutions, \'A Right to Be Merry\' (Franciscan), Dominican and Jesuit spirituality texts",
        prompt: "What are the distinctive charisms and spiritualities of the major Catholic religious orders? Compare Dominican, Franciscan, Jesuit, Carmelite, and Benedictine approaches to religious life."
    },
    69: {
        topic: "Forms of Religious Life",
        description: "The relative merits of contemplative, active, and mixed religious life.",
        reading: "Aquinas ST II-II q.182-188, Perfectae Caritatis (Vatican II), various rules",
        prompt: "What is the highest form of religious life? Compare purely contemplative (Carthusian), purely active (Vincentian), and mixed (Dominican \'contemplata aliis tradere\') vocations."
    },
    70: {
        topic: "Approaches to Religious Life",
        description: "Different emphases in religious vocation - contemplative, apostolic, or mixed.",
        reading: "Perfectae Caritatis, various religious constitutions, Aquinas ST II-II q.188",
        prompt: "What are the different approaches to religious life? Compare contemplative (Carthusian/Carmelite), apostolic (Jesuit/Vincentian), and mixed (Dominican) vocations."
    },
    71: {
        topic: "Cistercian/Trappist Spirituality",
        description: "The emphases of the Cistercian reform and Trappist tradition.",
        reading: "St. Bernard\'s writings, \'Charter of Charity\', Thomas Merton",
        prompt: "What does Cistercian/Trappist spirituality emphasize? Explain the return to strict Benedictine observance, manual labor, silence, and the mystical tradition of St. Bernard."
    },
    72: {
        topic: "Salesian Spirituality",
        description: "Don Bosco\'s approach to youth ministry and holiness.",
        reading: "Don Bosco\'s \'Memoirs of the Oratory\', \'Preventive System\', Salesian constitutions",
        prompt: "What does Salesian spirituality center on? Explain Don Bosco\'s Preventive System (reason, religion, loving-kindness), focus on youth, and joyful approach to holiness."
    },
    73: {
        topic: "Vincentian Spirituality",
        description: "St. Vincent de Paul\'s spirituality of service to the poor.",
        reading: "Vincent de Paul\'s conferences, Vincentian constitutions, Louise de Marillac",
        prompt: "What does Vincentian spirituality emphasize? Explain seeing Christ in the poor, simplicity, humility, and the integration of contemplation with active service."
    },
    74: {
        topic: "Passionist Spirituality",
        description: "The Passionist focus on the memory of Christ\'s Passion.",
        reading: "Paul of the Cross\' letters, Passionist constitutions",
        prompt: "What characterizes Passionist spirituality? Explain the \'memoria passionis\' (memory of Christ\'s suffering), its role in preaching and contemplation, and the fourth vow."
    },
    75: {
        topic: "Founder Charisms",
        description: "Which religious founder\'s charism most resonates personally.",
        reading: "Various founder biographies and spiritual writings",
        prompt: "What are the distinctive charisms of major religious founders? Compare Dominic, Francis, Ignatius, Teresa, Benedict, Vincent, and others. How do their charisms differ?"
    },
    76: {
        topic: "Doubtful Law in Moral Theology",
        description: "How to act when it\'s unclear whether a law binds.",
        reading: "Alphonsus Liguori, probabilism tradition, \'lex dubia non obligat\'",
        prompt: "In moral theology, how should one act when facing a doubtful law? Explain the principle \'lex dubia non obligat\', probabilism, and when one may follow the opinion for liberty."
    },
    77: {
        topic: "Catholic Agrarian Life",
        description: "The value of rural and farming life in Catholic thought.",
        reading: "Chesterton and Belloc on agriculture, \'Catholic Land Movement\', Rerum Novarum",
        prompt: "How should Catholic rural/agrarian life be valued? Explain the distributist vision of widespread land ownership, subsidiarity, and the dignity of agricultural work."
    },
    78: {
        topic: "Memoria Passionis",
        description: "The Passionist emphasis on remembering Christ\'s suffering.",
        reading: "Paul of the Cross, Passionist spirituality texts",
        prompt: "What is the Passionist emphasis on \'memoria passionis\' (memory of Christ\'s suffering)? How does contemplating the Passion lead to transformation and apostolate?"
    },
    79: {
        topic: "The Mercedarian Fourth Vow",
        description: "The vow to give one\'s life for captives if necessary.",
        reading: "Mercedarian constitutions, Peter Nolasco",
        prompt: "What does the Mercedarian fourth vow - to give one\'s life for captives if necessary - represent? Explain its historical context and contemporary spiritual meaning."
    },
    80: {
        topic: "Church and Modern Culture",
        description: "How the Church should relate to contemporary society.",
        reading: "Gaudium et Spes, Communio-Concilium debates, MacIntyre",
        prompt: "How should the Church relate to modern culture? Explain engagement, resistance, and transformation models. What can the Church affirm and what must she reject?"
    },
    81: {
        topic: "Church and State Relations",
        description: "The proper relationship between religious and civil authority.",
        reading: "Dignitatis Humanae, Quas Primas, Gelasian doctrine, Immortale Dei (Leo XIII)",
        prompt: "What is the proper relationship between Church and State? Explain integralism, separation, cooperation, and how Catholic teaching has developed from Gelasius to Vatican II."
    },
    82: {
        topic: "Christ\'s Kingship and Political Order",
        description: "How the social reign of Christ relates to political arrangements.",
        reading: "Quas Primas (Pius XI), Catechism §2105, integralist literature",
        prompt: "What is the relationship between Christ\'s kingship and political order? Explain the Feast of Christ the King\'s meaning, integralist views, and liberal Catholic alternatives."
    },
    83: {
        topic: "Catholic Economic Vision",
        description: "Which economic system best reflects Catholic social teaching.",
        reading: "Rerum Novarum, Quadragesimo Anno, Centesimus Annus, Caritas in Veritate",
        prompt: "Which economic vision best reflects Catholic social teaching? Explain distributism, social market economy, corporatism, and where capitalism and socialism fall short."
    },
    84: {
        topic: "The Living Wage",
        description: "Whether employers have a strict moral obligation to pay a family-sustaining wage.",
        reading: "Rerum Novarum §45, Quadragesimo Anno, Catechism §2434",
        prompt: "Is a living wage a strict moral obligation according to Catholic social teaching? Explain the tradition from Leo XIII forward and various interpretations of this obligation."
    },
    85: {
        topic: "Labor Unions in Catholic Social Teaching",
        description: "The role and value of labor organizations in Catholic thought.",
        reading: "Rerum Novarum, Laborem Exercens, Catechism §2430",
        prompt: "What is the role of unions in Catholic social teaching? Explain the right to organize, limits of union power, and how this teaching developed from Leo XIII to John Paul II."
    },
    86: {
        topic: "Private Property",
        description: "The scope and limits of the right to private property in Catholic teaching.",
        reading: "Rerum Novarum, Quadragesimo Anno §§45-46, Catechism §§2401-2406",
        prompt: "What is the proper scope of private property according to Catholic social teaching? Explain the universal destination of goods, the right to property, and its social mortgage."
    },
    87: {
        topic: "National Identity and Catholicism",
        description: "How Catholics should view national identity - patriotism, nationalism, or universalism.",
        reading: "Mit brennender Sorge, Fratelli Tutti, Summi Pontificatus",
        prompt: "How should Catholics view national identity? Explain legitimate patriotism versus excessive nationalism, and how Catholic universalism relates to particular national loyalties."
    },
    88: {
        topic: "Immigration and Catholic Teaching",
        description: "How Catholic nations should approach immigration - open borders, restriction, or prudential balance.",
        reading: "Pacem in Terris, Catechism §2241, USCCB statements on immigration",
        prompt: "How should Catholic nations approach immigration? Explain the right to emigrate, the right of nations to control borders, and how to balance these in Catholic teaching."
    },
    89: {
        topic: "The Church and International Institutions",
        description: "Whether the Church should resist or cooperate with international bodies promoting secular values.",
        reading: "Sollicitudo Rei Socialis, Caritas in Veritate, Vatican statements at the UN",
        prompt: "Should the Church resist international institutions promoting secular values? Explain Catholic approaches to international cooperation, subsidiarity, and moral limits."
    },
    90: {
        topic: "Reforming the Novus Ordo",
        description: "Whether the ordinary form should be reformed toward traditional liturgy.",
        reading: "Ratzinger\'s \'Spirit of the Liturgy\', Lang\'s \'Turning Towards the Lord\', GIRM options",
        prompt: "Should the Novus Ordo be reformed toward a vernacular TLM (like Orthodox Divine Liturgy)? Explain \'reform of the reform\' ideas, arguments for and against, and practical possibilities."
    },
    91: {
        topic: "Fundamental Theological Orientation",
        description: "Self-identification along the theological spectrum.",
        reading: "Various theological school descriptions",
        prompt: "What are the main theological orientations in contemporary Catholicism? Explain traditionalist, conservative, ressourcement, communio, and progressive positions."
    },
    92: {
        topic: "Theological Method and Norms",
        description: "What should govern theological reasoning - Scripture, metaphysical systems, or the living Magisterium.",
        reading: "Fides et Ratio (John Paul II), Aeterni Patris (Leo XIII), Dei Filius (Vatican I)",
        prompt: "In Catholic theology, what should be the primary norm for resolving theological disputes? Explain views prioritizing Scripture, metaphysical frameworks, magisterial teaching, or theological pluralism."
    },
    93: {
        topic: "Habitual Vice and Moral Culpability",
        description: "How prior sinful choices that form habits affect present moral responsibility.",
        reading: "Aquinas ST I-II q.78 (on causes of sin), Catechism §§1865-1866, 1735",
        prompt: "How does habitual vice formed by prior voluntary sin affect moral culpability for present acts? Does it diminish or aggravate guilt? Explain the Catholic moral tradition."
    },
    94: {
        topic: "The Doctrine of Purgatory",
        description: "The nature and purpose of purification after death.",
        reading: "Catechism §§1030-1032, Council of Florence, Trent Session 25, 2 Maccabees 12:46",
        prompt: "Explain the Catholic doctrine of purgatory. What are the various models - satisfaction for temporal punishment, purification, spiritual maturation? What is its biblical and historical basis?"
    },
    95: {
        topic: "The Role of Theologians",
        description: "How theologians serve the Church in relation to the Magisterium.",
        reading: "Donum Veritatis (CDF 1990), Veritatis Gaudium, Sapientia Christiana",
        prompt: "How do theologians serve the Church according to Catholic teaching? What is their proper relationship to the Magisterium? Can they legitimately critique or must they only explain?"
    },
    96: {
        topic: "Fallen Nature and Natural Goodness",
        description: "What fallen humans can do without grace - total depravity versus wounded but capable nature.",
        reading: "Trent Session 6, Catechism §§405-409, Orange II (529), Augustine vs. Pelagius",
        prompt: "What is the relationship between fallen human nature and the ability to do good? Explain the spectrum from Semi-Pelagianism to strict Augustinianism, and where Catholic teaching falls."
    },
    97: {
        topic: "Divine Will and Intellect",
        description: "The relationship between God\'s will and God\'s knowledge - intellectualism versus voluntarism.",
        reading: "Aquinas ST I q.19, Scotus\' Ordinatio, Ockham\'s writings",
        prompt: "What is the relationship between God\'s will and intellect? Does God will something because it is good, or is it good because God wills it? Explain intellectualist and voluntarist positions."
    },
    98: {
        topic: "The Foundation of Morality",
        description: "What grounds moral obligations - natural law, divine command, or human nature.",
        reading: "Aquinas ST I-II q.90-94, Veritatis Splendor, natural law tradition",
        prompt: "What is the source of moral obligations according to Catholic theology? Explain natural law theory, divine command theory, and how they relate in Catholic moral theology."
    },
    99: {
        topic: "Early Church Governance",
        description: "How authority functioned in the early Church - monarchical bishop, collegial, or congregational.",
        reading: "Acts, Didache, Ignatius of Antioch, 1 Clement, Irenaeus",
        prompt: "How did the early Church function in terms of governance? What models of authority existed? How do Catholics, Orthodox, and Protestants read this history differently?"
    },
    100: {
        topic: "The Confessional State",
        description: "Whether a formally Catholic state remains the ideal even after Vatican II.",
        reading: "Dignitatis Humanae, Quas Primas, Libertas (Leo XIII), Pink\'s articles on DH",
        prompt: "Is a confessional Catholic state still the ideal? Explain how different Catholics interpret Vatican II\'s Dignitatis Humanae - as development, rupture, or pastoral accommodation."
    },
    101: {
        topic: "Forms of Prayer",
        description: "The highest form of prayer - liturgical, mental, contemplative, or devotional.",
        reading: "Sacrosanctum Concilium §10, Teresa of Avila\'s \'Interior Castle\', Catechism §§2697-2719",
        prompt: "What is the highest form of prayer? Compare liturgical prayer, lectio divina, mental prayer, contemplation, and popular devotions. How do different spiritualities rank these?"
    },
    102: {
        topic: "Mystical Experiences",
        description: "How to understand and evaluate mystical phenomena.",
        reading: "John of the Cross, Teresa of Avila, Poulain\'s \'Graces of Interior Prayer\', Catechism §2014",
        prompt: "How should we understand mystical experiences? Explain the stages of mystical prayer, extraordinary phenomena (visions, locutions), and how to discern authentic from false mysticism."
    },
    103: {
        topic: "Frequency of Confession",
        description: "How often a devout Catholic should receive the sacrament of penance.",
        reading: "Pius XII\'s \'Mystici Corporis\' §88, Catechism §1458, various spiritual directors",
        prompt: "How often should a devout Catholic go to confession? Explain the minimum obligation, the tradition of frequent confession, and different spiritual traditions\' recommendations."
    },
    104: {
        topic: "The Purpose of the Incarnation",
        description: "Why the Son of God became incarnate - redemption, theosis, or cosmic recapitulation.",
        reading: "Athanasius\' \'On the Incarnation\', Anselm\'s \'Cur Deus Homo\', Irenaeus",
        prompt: "Why did the Son of God become incarnate? Explain redemption from sin (Anselm), theosis/divinization (Athanasius), and recapitulation (Irenaeus) theories of the Incarnation\'s purpose."
    },
    105: {
        topic: "Redemptorist Spirituality",
        description: "St. Alphonsus Liguori and the Redemptorist charism.",
        reading: "Alphonsus\' \'Practice of the Love of Jesus Christ\', Redemptorist constitutions",
        prompt: "What are St. Alphonsus Liguori and the Redemptorists known for? Explain their focus on the poor, moral theology, Marian devotion, and preaching missions."
    },
    106: {
        topic: "Scripture\'s Multiple Senses",
        description: "The relationship between literal and spiritual senses of Scripture.",
        reading: "Catechism §§115-119, de Lubac\'s \'Medieval Exegesis\', Aquinas ST I q.1 a.10",
        prompt: "What are Scripture\'s literal and spiritual senses? Explain the four senses (literal, allegorical, moral, anagogical), how they relate, and their place in modern exegesis."
    },
    107: {
        topic: "Religious Liberty (Dignitatis Humanae)",
        description: "Understanding Vatican II\'s teaching on religious freedom.",
        reading: "Dignitatis Humanae, Murray\'s \'We Hold These Truths\', Pink\'s articles, Lefebvre\'s objections",
        prompt: "How should we understand Vatican II\'s teaching on religious liberty? Does it contradict earlier teaching or develop it? Explain development, rupture, and continuity interpretations."
    },
    108: {
        topic: "Clerical Celibacy",
        description: "Whether mandatory celibacy for Latin Rite priests should continue.",
        reading: "Sacerdotalis Caelibatus (Paul VI), Eastern practice, Cochini\'s \'Apostolic Origins of Priestly Celibacy\'",
        prompt: "What is your view on mandatory clerical celibacy in the Latin Rite? Explain the arguments for maintaining, relaxing, or abolishing the discipline. What is its theological basis?"
    },
    109: {
        topic: "Traditionis Custodes and the TLM",
        description: "Evaluating Pope Francis\'s restrictions on the Traditional Latin Mass.",
        reading: "Traditionis Custodes (2021), Summorum Pontificum (2007), various commentaries",
        prompt: "How should Catholics view Pope Francis\'s restrictions on the Traditional Latin Mass? Explain the arguments defending Traditionis Custodes and those criticizing it."
    },
    110: {
        topic: "Hermeneutic of Continuity",
        description: "Benedict XVI\'s proposal for interpreting Vatican II.",
        reading: "Benedict XVI\'s December 2005 address, Marchetto\'s \'Council Ecumenical Vatican II\'",
        prompt: "What is the \'hermeneutic of continuity\' proposed by Benedict XVI? Contrast it with the \'hermeneutic of rupture\'. How should Vatican II be interpreted in relation to tradition?"
    },
    111: {
        topic: "Protestant-Catholic Compatibility on Justification",
        description: "Whether Reformed and Lutheran views can be reconciled with Catholic schools.",
        reading: "Joint Declaration, Trent, various ecumenical dialogues",
        prompt: "Are Reformed and Lutheran views of justification compatible with some Catholic schools? Compare Protestant positions with Augustinian, Thomist, and Molinist Catholic views."
    },
    112: {
        topic: "Economic Systems and Catholic Teaching",
        description: "Which economic arrangement best reflects Catholic social principles.",
        reading: "Centesimus Annus, Caritas in Veritate, distributist literature",
        prompt: "Which economic arrangement best reflects Catholic Social Teaching? Compare market economy with social safety net, distributism, democratic socialism, and other options."
    },
    113: {
        topic: "Marian Apparitions",
        description: "How to evaluate private revelations like Fatima and Lourdes.",
        reading: "CDF norms on apparitions, approved apparition documentation, Catechism §67",
        prompt: "How should Catholics view Marian apparitions? Explain the approval process, the status of \'worthy of belief\', and different levels of Catholic devotion to apparitions."
    },
    114: {
        topic: "Universal Salvation (Hope for an Empty Hell)",
        description: "Balthasar\'s hope that all might be saved.",
        reading: "Balthasar\'s \'Dare We Hope\', Catechism §§1033-1037, Aquinas on hell",
        prompt: "What is the Catholic position on universal salvation? Explain Balthasar\'s \'hope for an empty hell\', traditional teaching on hell\'s population, and whether universalism is compatible with faith."
    },
    115: {
        topic: "Amoris Laetitia and Communion",
        description: "Whether divorced and remarried Catholics can receive communion.",
        reading: "Amoris Laetitia Chapter 8, Familiaris Consortio §84, dubia and responses",
        prompt: "What is your view on Amoris Laetitia and communion for the divorced and remarried? Explain the traditional discipline, Chapter 8\'s approach, and various interpretations."
    },
    116: {
        topic: "Humanae Vitae and Contraception",
        description: "The Church\'s teaching on artificial contraception.",
        reading: "Humanae Vitae, John Paul II\'s Theology of the Body, Majority Report controversy",
        prompt: "What is your position on Humanae Vitae\'s teaching on contraception? Explain the theological arguments, reception of the encyclical, and ongoing debates."
    },
    117: {
        topic: "Church and Liberal Democracy",
        description: "How the Church should relate to secular democratic systems.",
        reading: "Centesimus Annus, Dignitatis Humanae, Ratzinger\'s political writings",
        prompt: "How should the Church relate to secular liberal democracy? Can she affirm it, must she tolerate it, or should she seek alternatives? What are the limits of Catholic engagement?"
    },
    118: {
        topic: "Papal Authority Self-Identification",
        description: "Where one falls on views of papal power.",
        reading: "Pastor Aeternus, Lumen Gentium, various ecclesiologies",
        prompt: "What are the different views of papal authority among Catholics? Explain ultramontane, moderate papalist, and minimalist positions. What does each emphasize or de-emphasize?"
    },
    119: {
        topic: "The Value of Scholasticism Today",
        description: "Whether scholastic philosophy and theology remain valuable.",
        reading: "Aeterni Patris, neo-scholastic manuals, ressourcement critiques",
        prompt: "What is the value of Scholasticism today? Should it be recovered, supplemented, or superseded? What are its enduring contributions and limitations?"
    },
    120: {
        topic: "The Fewness of the Saved",
        description: "The traditional teaching that few attain eternal salvation.",
        reading: "Matthew 7:13-14, Augustine, Aquinas, Balthasar\'s alternative",
        prompt: "What is the traditional teaching on the \'fewness of the saved\'? Is it still tenable? Explain the biblical basis, patristic teaching, and modern challenges to this view."
    },
    121: {
        topic: "Extra Ecclesiam Nulla Salus",
        description: "How to understand \'Outside the Church there is no salvation\'.",
        reading: "Florence, Pius IX, Lumen Gentium §16, Dominus Iesus",
        prompt: "How should we understand \'Extra Ecclesiam nulla salus\'? Explain rigorist, moderate, and liberal interpretations. How has the Church\'s understanding developed?"
    },
    122: {
        topic: "Papal Infallibility\'s Historical Basis",
        description: "Whether infallibility was an ancient constant tradition.",
        reading: "Pastor Aeternus, patristic evidence, Newman\'s development theory",
        prompt: "Was papal infallibility an ancient and constant tradition of the Church? Explain the historical evidence, development theory, and traditionalist versus historical-critical views."
    },
    123: {
        topic: "Latin Catholics and Eastern Traditions",
        description: "How Western Catholics should regard Byzantine and Eastern liturgies.",
        reading: "Orientalium Ecclesiarum, Orientale Lumen, Code of Canons of Eastern Churches",
        prompt: "How should Latin Catholics regard Byzantine and Eastern liturgical traditions? Explain equality of rites, mutual enrichment, and avoiding Latinization of Eastern practice."
    },
    124: {
        topic: "Faith and Works in Salvation",
        description: "The relationship between faith and works in the order of salvation.",
        reading: "James 2, Trent Session 6, Joint Declaration",
        prompt: "What is the relationship between faith and works in salvation? Compare Catholic, Lutheran, and Reformed positions. How did Trent and the Joint Declaration address this?"
    },
    125: {
        topic: "Assurance of Salvation Across Traditions",
        description: "Different Christian views on knowing one is saved.",
        reading: "Trent, Westminster Confession, Methodist position",
        prompt: "What is the assurance of salvation according to different traditions? Compare Catholic moral certainty, Reformed \'perseverance of the saints\', and Methodist assurance through the Spirit."
    },
    126: {
        topic: "Canonization and Rehabilitation",
        description: "Which figures Catholics would like to see recognized or rehabilitated.",
        reading: "Canonization processes, historical controversies",
        prompt: "What figures would Catholics like to see canonized or rehabilitated? Explain figures like Eckhart, Rosmini, and Lefebvre and the debates surrounding them."
    },
    127: {
        topic: "Benedict XVI\'s \'Smaller, Purer Church\'",
        description: "Whether a smaller, more orthodox Church would be preferable to a larger but less fervent one.",
        reading: "Ratzinger\'s \'Faith and the Future\' (1969), various Benedict XVI writings",
        prompt: "What did Benedict XVI mean by a \'smaller, purer Church\'? Explain the various perspectives on whether numerical decline might lead to spiritual renewal."
    },
    128: {
        topic: "The Future of the Catholic Church",
        description: "Personal outlook on where the Church is headed.",
        reading: "Various contemporary Catholic analysis and commentary",
        prompt: "What are the different Catholic perspectives on the future of the Church? Explain optimistic, cautiously hopeful, traditionalist concerned, progressive transformative, and remnant views."
    },
    129: {
        topic: "How ought the Pope deal with regional Bishops\' Conferences in defiance of orthodox teaching, such as the Synodal Path in Germany?",
        description: "This question explores how ought the pope deal with regional bishops\' conferences in defiance of orthodox teaching, such as the synodal path in germany.",
        reading: "Catechism of the Catholic Church, relevant conciliar documents",
        prompt: "Explain the theological perspectives on: How ought the Pope deal with regional Bishops\' Conferences in defiance of orthodox teaching, such as the Synodal Path in Germany?"
    },
    130: {
        topic: "Do you agree with Benedict XVI\'s vision of a smaller, more orthodox Church as potentially ideal?",
        description: "This question explores do you agree with benedict xvi\'s vision of a smaller, more orthodox church as potentially ideal.",
        reading: "Catechism of the Catholic Church, relevant conciliar documents",
        prompt: "Explain the theological perspectives on: Do you agree with Benedict XVI\'s vision of a smaller, more orthodox Church as potentially ideal?"
    },
    131: {
        topic: "Which post-conciliar Pope do you most admire?",
        description: "This question explores which post-conciliar pope do you most admire.",
        reading: "Catechism of the Catholic Church, relevant conciliar documents",
        prompt: "Explain the theological perspectives on: Which post-conciliar Pope do you most admire?"
    },
    132: {
        topic: "What is your personal outlook for the future of the Catholic Church?",
        description: "This question explores what is your personal outlook for the future of the catholic church.",
        reading: "Catechism of the Catholic Church, relevant conciliar documents",
        prompt: "Explain the theological perspectives on: What is your personal outlook for the future of the Catholic Church?"
    },
    133: {
        topic: "How do you view the SSPX\'s irregular canonical status and their announced intention to consecrate bishops again?",
        description: "This question explores how do you view the sspx\'s irregular canonical status and their announced intention to consecrate bishops again.",
        reading: "Catechism of the Catholic Church, relevant conciliar documents",
        prompt: "Explain the theological perspectives on: How do you view the SSPX\'s irregular canonical status and their announced intention to consecrate bishops again?"
    }
};

const SAINT_VIEWS = {
    0: [
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Patristic exegesis (literal + spiritual senses) should normally govern; historical criticism is secondary and constrained.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Historical-grammatical meaning is primary; spiritual senses are real but must be controlled by the literal sense.", optionIndex: 1 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Historical-grammatical meaning is primary; spiritual senses are real but must be controlled by the literal sense.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Historical-critical methods are useful and often necessary, but must be disciplined by dogma and the Church\'s rule of faith.", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Historical-critical methods are useful and often necessary, but must be disciplined by dogma and the Church\'s rule of faith.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The text\'s meaning is best read through contemporary experience and community reception.", optionIndex: 3 },
        { saint: "St. John Paul II", era: "1920–2005", position: "The text\'s meaning is best read through contemporary experience and community reception.", optionIndex: 3 }
    ],
    1: [
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Liturgical stability and doctrinal continuity: a formal, traditional Catholic translation style.", optionIndex: 0 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Liturgical stability and doctrinal continuity: a formal, traditional Catholic translation style.", optionIndex: 0 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Critical-text precision: modern scholarly editions are valuable so long as doctrine governs interpretation.", optionIndex: 1 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Critical-text precision: modern scholarly editions are valuable so long as doctrine governs interpretation.", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Pastoral accessibility: clarity for modern readers is the priority.", optionIndex: 2 },
        { saint: "St. John Paul II", era: "1920–2005", position: "Pastoral accessibility: clarity for modern readers is the priority.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Different translations for different uses (liturgy vs study vs devotion).", optionIndex: 3 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Different translations for different uses (liturgy vs study vs devotion).", optionIndex: 3 }
    ],
    2: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Literal foundational; spiritual senses controlled by it.", optionIndex: 0 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Literal foundational; spiritual senses controlled by it.", optionIndex: 0 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Spiritual senses reveal deepest meaning; Fathers normative.", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Historical-critical establishes literal; spiritual is devotional.", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Historical-critical establishes literal; spiritual is devotional.", optionIndex: 2 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "All four senses work together; Scripture inexhaustibly rich.", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "All four senses work together; Scripture inexhaustibly rich.", optionIndex: 3 }
    ],
    3: [
        { saint: "Joseph Ratzinger", era: "1927–2022", position: "Essential and correct. Vatican II must be read in continuity with all prior councils.", optionIndex: 0 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Essential and correct. Vatican II must be read in continuity with all prior councils.", optionIndex: 0 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Noble attempt, but the texts themselves contain ambiguities enabling rupturist readings.", optionIndex: 1 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Noble attempt, but the texts themselves contain ambiguities enabling rupturist readings.", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Continuity is a fiction. Vatican II was a new beginning, and that\'s good.", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Continuity is a fiction. Vatican II was a new beginning, and that\'s good.", optionIndex: 2 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Partially valid but insufficient. Some texts genuinely conflict with prior magisterium.", optionIndex: 3 },
        { saint: "Various Authors", era: "20th–21st c.", position: "Partially valid but insufficient. Some texts genuinely conflict with prior magisterium.", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "A pastoral strategy more than theological argument. Useful for maintaining unity.", optionIndex: 4 }
    ],
    4: [
        { saint: "Alexander Schmemann", era: "1921–1983", position: "Eastern liturgies preserved ancient forms often lost in the West. Latin Catholics can learn much from their reverence, iconography, and theological depth.", optionIndex: 0 },
        { saint: "St. Photios the Great", era: "c. 810–893", position: "Eastern liturgies preserved ancient forms often lost in the West. Latin Catholics can learn much from their reverence, iconography, and theological depth.", optionIndex: 0 },
        { saint: "Joseph de Maistre", era: "1753–1821", position: "The Roman Rite is the Church\'s preeminent liturgy; Eastern rites are legitimate but the Latin tradition is normative and superior in precision.", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "The Roman Rite is the Church\'s preeminent liturgy; Eastern rites are legitimate but the Latin tradition is normative and superior in precision.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Both traditions are apostolic and complementary. The \'two lungs\' imagery of John Paul II captures the Church\'s need for both.", optionIndex: 2 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "Eastern Catholics should be fully Eastern, not Latinized. The Melkite and Ukrainian traditions suffered from Roman centralization.", optionIndex: 3 },
        { saint: "Alexander Schmemann", era: "1921–1983", position: "Eastern Catholics should be fully Eastern, not Latinized. The Melkite and Ukrainian traditions suffered from Roman centralization.", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "The liturgy is the liturgy. Excessive focus on rite distinctions distracts from the essential: valid Mass, real presence, sacrifice.", optionIndex: 4 },
        { saint: "St. Josemaría Escrivá", era: "1902–1975", position: "The liturgy is the liturgy. Excessive focus on rite distinctions distracts from the essential: valid Mass, real presence, sacrifice.", optionIndex: 4 }
    ],
    5: [
        { saint: "Étienne Gilson", era: "1884–1978", position: "Moderate realism: Universals exist in things as real natures (Thomist (Realist), Thomist)", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Moderate realism: Universals exist in things as real natures (Thomist (Realist), Thomist)", optionIndex: 0 },
        { saint: "William of Ockham", era: "c. 1287–1347", position: "Nominalism: Universals are only names/mental concepts; only particulars exist", optionIndex: 1 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Nominalism: Universals are only names/mental concepts; only particulars exist", optionIndex: 1 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "Platonic/Participatory: Universals exist primarily in the divine mind; things participate", optionIndex: 2 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Platonic/Participatory: Universals exist primarily in the divine mind; things participate", optionIndex: 2 },
        { saint: "Charles Sanders Peirce", era: "1839–1914", position: "Scotist: Universals have a \'formal distinction\'—less than real but more than nominal", optionIndex: 3 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Scotist: Universals have a \'formal distinction\'—less than real but more than nominal", optionIndex: 3 }
    ],
    6: [
        { saint: "Étienne Gilson", era: "1884–1978", position: "Analogy of being (Analogia Entis): Being is predicated analogically between God and creatures—neither univocally nor equivocally, but proportionally. (Thomist, Thomist (Realist))", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Analogy of being (Analogia Entis): Being is predicated analogically between God and creatures—neither univocally nor equivocally, but proportionally. (Thomist, Thomist (Realist))", optionIndex: 0 },
        { saint: "Charles Sanders Peirce", era: "1839–1914", position: "Univocity of being: Being is predicated in the same fundamental sense of God and creatures, though infinitely different in mode and perfection.", optionIndex: 1 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Univocity of being: Being is predicated in the same fundamental sense of God and creatures, though infinitely different in mode and perfection.", optionIndex: 1 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "Participatory/Emanation: Creatures participate in or emanate from divine being through a hierarchy of degrees; emphasis on return to the One.", optionIndex: 2 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Participatory/Emanation: Creatures participate in or emanate from divine being through a hierarchy of degrees; emphasis on return to the One.", optionIndex: 2 },
        { saint: "William of Ockham", era: "c. 1287–1347", position: "The question is too abstract and speculative; focus on God\'s revealed names and salvation history rather than metaphysical speculation.", optionIndex: 3 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "The question is too abstract and speculative; focus on God\'s revealed names and salvation history rather than metaphysical speculation.", optionIndex: 3 }
    ],
    7: [
        { saint: "Domingo Báñez, O.P.", era: "1528–1604", position: "Bañez - physical premotion, intrinsically efficacious grace, predestination ante praevisa merita.", optionIndex: 0 },
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "Bañez - physical premotion, intrinsically efficacious grace, predestination ante praevisa merita.", optionIndex: 0 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Molina - middle knowledge, extrinsically efficacious grace, libertarian freedom preserved.", optionIndex: 1 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Molina - middle knowledge, extrinsically efficacious grace, libertarian freedom preserved.", optionIndex: 1 },
        { saint: "St. Robert Bellarmine, S.J.", era: "1542–1621", position: "Congruism - a mediating position. Grace is suited to circumstances God foresees.", optionIndex: 2 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Congruism - a mediating position. Grace is suited to circumstances God foresees.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "The Church left it open. Both are permissible opinions within Catholic bounds.", optionIndex: 3 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "I lean Augustinian/Bañezian but wouldn\'t call Molinism heresy.", optionIndex: 4 },
        { saint: "Domingo Báñez, O.P.", era: "1528–1604", position: "I lean Augustinian/Bañezian but wouldn\'t call Molinism heresy.", optionIndex: 4 }
    ],
    8: [
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "Strict Tridentine - ex opere operato, transubstantiation precisely defined, seven sacraments.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Strict Tridentine - ex opere operato, transubstantiation precisely defined, seven sacraments.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Thomistic - sacraments as instrumental efficient causes, Christ the principal cause.", optionIndex: 1 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Augustinian - emphasis on faith, interiority, sacraments as \'visible words.\'", optionIndex: 2 },
        { saint: "St. John Chrysostom", era: "c. 349–407", position: "Eastern - holy mysteries, epiclesis centrality, theosis orientation.", optionIndex: 3 },
        { saint: "Alexander Schmemann", era: "1921–1983", position: "Eastern - holy mysteries, epiclesis centrality, theosis orientation.", optionIndex: 3 },
        { saint: "Edward Schillebeeckx, O.P.", era: "1914–2009", position: "Open to transignification language as complementary to transubstantiation.", optionIndex: 4 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Open to transignification language as complementary to transubstantiation.", optionIndex: 4 },
        { saint: "St. John of the Cross", era: "1542–1591", position: "Eucharistic mysticism - personal encounter, adoration, transformative union.", optionIndex: 5 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Eucharistic mysticism - personal encounter, adoration, transformative union.", optionIndex: 5 }
    ],
    9: [
        { saint: "John Milbank", era: "1952–present", position: "Secular reason is \'heresy\' - modernity\'s autonomy from theology must be rejected root and branch.", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Secular reason is \'heresy\' - modernity\'s autonomy from theology must be rejected root and branch.", optionIndex: 0 },
        { saint: "Joseph Ratzinger", era: "1927–2022", position: "Interesting critique of secularism but sometimes overstates the case against modernity.", optionIndex: 1 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Interesting critique of secularism but sometimes overstates the case against modernity.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Too academic and obscure. Practical pastoral concerns matter more than philosophical critique.", optionIndex: 2 },
        { saint: "St. Vincent de Paul", era: "1581–1660", position: "Too academic and obscure. Practical pastoral concerns matter more than philosophical critique.", optionIndex: 2 },
        { saint: "John Milbank", era: "1952–present", position: "Essentially correct - all truth participates in divine truth. There is no \'neutral\' reason.", optionIndex: 3 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "Essentially correct - all truth participates in divine truth. There is no \'neutral\' reason.", optionIndex: 3 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Dangerous flirtation with fideism. Reason has its own integrity under grace.", optionIndex: 4 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Dangerous flirtation with fideism. Reason has its own integrity under grace.", optionIndex: 4 }
    ],
    10: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "The Beatific Vision: loving contemplation of God as final end.", optionIndex: 0 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "The Beatific Vision: loving contemplation of God as final end.", optionIndex: 0 },
        { saint: "Blaise Pascal", era: "1623–1662", position: "Final judgment and salvation from damnation: vigilance, penitence, and fear of the Lord.", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Final judgment and salvation from damnation: vigilance, penitence, and fear of the Lord.", optionIndex: 1 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "Theosis/deification: participation in divine life as transformative communion.", optionIndex: 2 },
        { saint: "St. John Chrysostom", era: "c. 349–407", position: "Theosis/deification: participation in divine life as transformative communion.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Renewal of the world and social holiness: the Church\'s mission in history.", optionIndex: 3 },
        { saint: "Jacques Maritain", era: "1882–1973", position: "Renewal of the world and social holiness: the Church\'s mission in history.", optionIndex: 3 }
    ],
    11: [
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Yes—Christ is the absolute primacy of creation, independent of sin", optionIndex: 0 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "Yes—Christ is the absolute primacy of creation, independent of sin", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "No—the Incarnation was ordered primarily to redemption from sin", optionIndex: 1 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "No—the Incarnation was ordered primarily to redemption from sin", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Probably not, but the question is speculative", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Yes, but the mode would have been different (glorious rather than suffering)", optionIndex: 3 }
    ],
    12: [
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Essential: Daily mental prayer is morally necessary for serious Christians", optionIndex: 0 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Essential: Daily mental prayer is morally necessary for serious Christians", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Very important but vocal prayer and sacraments can suffice for some", optionIndex: 1 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Very important but vocal prayer and sacraments can suffice for some", optionIndex: 1 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Helpful but not essential; the liturgy is sufficient", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Overemphasized in some traditions; action and service matter more", optionIndex: 3 }
    ],
    13: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Christ possessed the beatific vision from conception, giving comprehensive knowledge.", optionIndex: 0 },
        { saint: "St. Cyril of Alexandria", era: "c. 376–444", position: "Christ possessed the beatific vision from conception, giving comprehensive knowledge.", optionIndex: 0 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "Christ\'s human knowledge was genuinely limited; He learned and grew authentically.", optionIndex: 1 },
        { saint: "Hans Urs von Balthasar", era: "1905–1988", position: "Christ\'s human knowledge was genuinely limited; He learned and grew authentically.", optionIndex: 1 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Christ had infused knowledge sufficient for His mission, without unlimited knowledge.", optionIndex: 2 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "Christ had infused knowledge sufficient for His mission, without unlimited knowledge.", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "The mystery exceeds our categories; emphasize soteriological sufficiency.", optionIndex: 3 }
    ],
    14: [
        { saint: "St. Cyril of Alexandria", era: "c. 376–444", position: "Two distinct wills in perfect harmony; human will freely conforms to divine.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Two distinct wills in perfect harmony; human will freely conforms to divine.", optionIndex: 0 },
        { saint: "Hans Urs von Balthasar", era: "1905–1988", position: "Divine will primary, human will its instrument; unity with dyothelitism.", optionIndex: 1 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Divine will primary, human will its instrument; unity with dyothelitism.", optionIndex: 1 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "Christ\'s human will genuinely struggled before conforming; soteriologically important.", optionIndex: 2 },
        { saint: "Hans Urs von Balthasar", era: "1905–1988", position: "Christ\'s human will genuinely struggled before conforming; soteriologically important.", optionIndex: 2 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "Maximus\'s synthesis: natural human will always good; gnomic willing absent.", optionIndex: 3 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "Maximus\'s synthesis: natural human will always good; gnomic willing absent.", optionIndex: 3 }
    ],
    15: [
        { saint: "St. Cyril of Alexandria", era: "c. 376–444", position: "Predicates of either nature attributed to the Person, carefully avoiding mixing natures.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Predicates of either nature attributed to the Person, carefully avoiding mixing natures.", optionIndex: 0 },
        { saint: "Hans Urs von Balthasar", era: "1905–1988", position: "Profound exchange: \'God suffered,\' \'this man is omnipotent\' — Incarnation in speech.", optionIndex: 1 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Profound exchange: \'God suffered,\' \'this man is omnipotent\' — Incarnation in speech.", optionIndex: 1 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "Shows divine condescension: God truly entered human weakness and suffering.", optionIndex: 2 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "Shows divine condescension: God truly entered human weakness and suffering.", optionIndex: 2 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Liturgically: \'O admirabile commercium\' — God becomes man that man might become God.", optionIndex: 3 },
        { saint: "St. John Chrysostom", era: "c. 349–407", position: "Liturgically: \'O admirabile commercium\' — God becomes man that man might become God.", optionIndex: 3 }
    ],
    16: [
        { saint: "John Calvin", era: "1509–1564", position: "Christ stood under the full weight of the Father\'s forensic wrath as one legally counted a sinner; God treated Him as if He had committed all our sins, pouring out punitive hatr...", optionIndex: 0 },
        { saint: "Martin Luther", era: "1483–1546", position: "Christ stood under the full weight of the Father\'s forensic wrath as one legally counted a sinner; God treated Him as if He had committed all our sins, pouring out punitive hatr...", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Christ, as our innocent Surety and Guarantor, freely accepted a real abandonment by the Father—not as one hated, but as one bearing the just debt of our impieties. His sacrifice...", optionIndex: 1 },
        { saint: "St. Alphonsus Liguori", era: "1696–1787", position: "Christ, as our innocent Surety and Guarantor, freely accepted a real abandonment by the Father—not as one hated, but as one bearing the just debt of our impieties. His sacrifice...", optionIndex: 1 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "The Cross was primarily Christ\'s triumphant victory over the powers of sin, death, and the devil, liberating humanity from bondage and recapitulating Adam\'s fall through His obe...", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "The Cross was primarily Christ\'s triumphant victory over the powers of sin, death, and the devil, liberating humanity from bondage and recapitulating Adam\'s fall through His obe...", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The Cross is supremely the revelation of God\'s boundless love, designed to move our hearts to repentance and kindle a response of love in return; juridical categories are second...", optionIndex: 3 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "The Cross is supremely the revelation of God\'s boundless love, designed to move our hearts to repentance and kindle a response of love in return; juridical categories are second...", optionIndex: 3 },
        { saint: "St. Paul of the Cross", era: "1694–1775", position: "The Cross is the \'Primordial Sacrament\' where Christ enters into the depths of human suffering and God-forsakenness, sanctifying all human anguish and opening the path to mystic...", optionIndex: 4 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "The Cross is the \'Primordial Sacrament\' where Christ enters into the depths of human suffering and God-forsakenness, sanctifying all human anguish and opening the path to mystic...", optionIndex: 4 }
    ],
    17: [
        { saint: "George Lindbeck", era: "1923–2018", position: "Lutheran - if \'faith alone\' is properly understood and sacramental realism affirmed, we\'re close.", optionIndex: 0 },
        { saint: "Louis Bouyer", era: "1913–2004", position: "Lutheran - if \'faith alone\' is properly understood and sacramental realism affirmed, we\'re close.", optionIndex: 0 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "Eastern Orthodox - patristic synthesis preserved. Theosis, synergy, mystery are deeply Catholic.", optionIndex: 1 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "Eastern Orthodox - patristic synthesis preserved. Theosis, synergy, mystery are deeply Catholic.", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "None. Extra Ecclesiam nulla salus. Protestant communities lack valid sacraments.", optionIndex: 2 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "None. Extra Ecclesiam nulla salus. Protestant communities lack valid sacraments.", optionIndex: 2 },
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "Reformed - they take grace seriously. Augustinian roots are shared.", optionIndex: 3 },
        { saint: "Blaise Pascal", era: "1623–1662", position: "Reformed - they take grace seriously. Augustinian roots are shared.", optionIndex: 3 },
        { saint: "Msgr. Jeffrey Steenson", era: "1952–present", position: "Anglican - via media, sacramental emphasis, liturgical beauty. The Ordinariate shows convergence.", optionIndex: 4 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Anglican - via media, sacramental emphasis, liturgical beauty. The Ordinariate shows convergence.", optionIndex: 4 }
    ],
    18: [
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Correct. The Fathers and Orange taught even the beginning of faith is God\'s gift.", optionIndex: 0 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Correct. The Fathers and Orange taught even the beginning of faith is God\'s gift.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Partially true, but \'monergism\' is anachronistic. Fathers affirmed grace\'s priority AND cooperation.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Partially true, but \'monergism\' is anachronistic. Fathers affirmed grace\'s priority AND cooperation.", optionIndex: 1 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Overstated. Orange affirmed free will\'s role. Catholic teaching has always been synergistic.", optionIndex: 2 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Overstated. Orange affirmed free will\'s role. Catholic teaching has always been synergistic.", optionIndex: 2 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Augustinian tradition was later balanced by Aquinas and Jesuits. Don\'t overcorrect.", optionIndex: 3 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Augustinian tradition was later balanced by Aquinas and Jesuits. Don\'t overcorrect.", optionIndex: 3 }
    ],
    19: [
        { saint: "Étienne Gilson", era: "1884–1978", position: "Analogy (Analogia Entis): Being is said in many ways. God and creatures share being analogically—neither identically nor equivocally, but proportionally. This preserves divine t...", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Analogy (Analogia Entis): Being is said in many ways. God and creatures share being analogically—neither identically nor equivocally, but proportionally. This preserves divine t...", optionIndex: 0 },
        { saint: "Charles Sanders Peirce", era: "1839–1914", position: "Univocity: Being must be predicated univocally for our language about God to be meaningful at all. Without a common concept, theology collapses into equivocation.", optionIndex: 1 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Univocity: Being must be predicated univocally for our language about God to be meaningful at all. Without a common concept, theology collapses into equivocation.", optionIndex: 1 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "Participatory/Neoplatonic: Creatures participate in divine being through emanation and return; theological language is primarily symbolic, apophatic, and mystical rather than st...", optionIndex: 2 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "Participatory/Neoplatonic: Creatures participate in divine being through emanation and return; theological language is primarily symbolic, apophatic, and mystical rather than st...", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Both capture important insights; the debate is often overblown by partisans. The Church has not definitively settled this metaphysical question.", optionIndex: 3 },
        { saint: "John Milbank", era: "1952–present", position: "Univocity opened the door to modern errors (nominalism, secularism); Analogia entis is non-negotiable for sound metaphysics and safeguarding divine transcendence. (Radical Ortho...", optionIndex: 4 },
        { saint: "Étienne Gilson", era: "1884–1978", position: "Univocity opened the door to modern errors (nominalism, secularism); Analogia entis is non-negotiable for sound metaphysics and safeguarding divine transcendence. (Radical Ortho...", optionIndex: 4 }
    ],
    20: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Real interior renewal through infused sanctifying grace: God makes the soul truly righteous, not merely declared so.", optionIndex: 0 },
        { saint: "Blaise Pascal", era: "1623–1662", position: "Real interior renewal through infused sanctifying grace: God makes the soul truly righteous, not merely declared so.", optionIndex: 0 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Real participation in Christ Himself: union with Christ is the core, with forensic language secondary.", optionIndex: 1 },
        { saint: "John Calvin", era: "1509–1564", position: "Primarily a forensic declaration (acquittal) with sanctification following as a distinct work.", optionIndex: 2 },
        { saint: "Martin Luther", era: "1483–1546", position: "Primarily a forensic declaration (acquittal) with sanctification following as a distinct work.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Covenantal status within the people of God; categories of \'infused habit\' are less central.", optionIndex: 3 },
        { saint: "St. John Paul II", era: "1920–2005", position: "Covenantal status within the people of God; categories of \'infused habit\' are less central.", optionIndex: 3 }
    ],
    21: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Yes: one can truly grow in grace and righteousness (while remaining entirely dependent on grace).", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Yes: one can truly grow in grace and righteousness (while remaining entirely dependent on grace).", optionIndex: 0 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Yes, best described as deeper participation/union with Christ rather than as a \'quantity\' of righteousness.", optionIndex: 1 },
        { saint: "John Calvin", era: "1509–1564", position: "No: justification is complete as a verdict; only sanctification increases.", optionIndex: 2 },
        { saint: "Martin Luther", era: "1483–1546", position: "No: justification is complete as a verdict; only sanctification increases.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The question is misleading; use primarily relational language.", optionIndex: 3 },
        { saint: "St. John Paul II", era: "1920–2005", position: "The question is misleading; use primarily relational language.", optionIndex: 3 }
    ],
    22: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Distinct but inseparable graces: God both forgives and makes holy; separating them distorts the Gospel.", optionIndex: 0 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Distinct but inseparable graces: God both forgives and makes holy; separating them distorts the Gospel.", optionIndex: 0 },
        { saint: "John Calvin", era: "1509–1564", position: "Justification is logically prior; sanctification follows as fruit, and confusing them risks works-righteousness.", optionIndex: 1 },
        { saint: "Martin Luther", era: "1483–1546", position: "Justification is logically prior; sanctification follows as fruit, and confusing them risks works-righteousness.", optionIndex: 1 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Union with Christ is prior: both justification and sanctification flow from participation in Christ.", optionIndex: 2 },
        { saint: "St. John Paul II", era: "1920–2005", position: "Pastoral framing matters more than precise distinctions; emphasize accompaniment and growth.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Pastoral framing matters more than precise distinctions; emphasize accompaniment and growth.", optionIndex: 3 }
    ],
    23: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "A disordered inclination that remains as a wound and penalty, but is not sin unless consented to. (Thomist, Thomist (Natural Law))", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Not formally sinful (guilt/reatus removed in baptism), though materially sinful (disordered inclination). Remains \'for the contest\' (ad agonem); culpability attaches only to con...", optionIndex: 1 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Not formally sinful (guilt/reatus removed in baptism), though materially sinful (disordered inclination). Remains \'for the contest\' (ad agonem); culpability attaches only to con...", optionIndex: 1 },
        { saint: "John Calvin", era: "1509–1564", position: "In itself it is truly sin in the regenerate (even without consent), though not always imputable in the same way.", optionIndex: 2 },
        { saint: "Martin Luther", era: "1483–1546", position: "In itself it is truly sin in the regenerate (even without consent), though not always imputable in the same way.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Primarily a psychological phenomenon; \'sin\' language should be reserved for conscious harmful choices.", optionIndex: 3 },
        { saint: "St. John Paul II", era: "1920–2005", position: "Primarily a psychological phenomenon; \'sin\' language should be reserved for conscious harmful choices.", optionIndex: 3 }
    ],
    24: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Not absolute certainty, but moral confidence through signs of grace, humility, and faithful sacramental life.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Not absolute certainty, but moral confidence through signs of grace, humility, and faithful sacramental life.", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Hopeful trust without seeking firm assurance; fear and humility protect against presumption.", optionIndex: 1 },
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "Hopeful trust without seeking firm assurance; fear and humility protect against presumption.", optionIndex: 1 },
        { saint: "Blaise Pascal", era: "1623–1662", position: "Strong assurance is spiritually dangerous and usually presumption; emphasize penitence and the fewness of the saved.", optionIndex: 2 },
        { saint: "Giovanni Patuzzi, O.P.", era: "1700–1769", position: "Strong assurance is spiritually dangerous and usually presumption; emphasize penitence and the fewness of the saved.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Interior peace from the Holy Spirit is a sufficient indicator; excessive anxiety about grace is spiritually unhealthy.", optionIndex: 3 },
        { saint: "St. John Paul II", era: "1920–2005", position: "Interior peace from the Holy Spirit is a sufficient indicator; excessive anxiety about grace is spiritually unhealthy.", optionIndex: 3 },
        { saint: "John Calvin", era: "1509–1564", position: "The truly elect will certainly persevere; assurance is a gift of faith rooted in God\'s promises.", optionIndex: 4 },
        { saint: "Martin Luther", era: "1483–1546", position: "The truly elect will certainly persevere; assurance is a gift of faith rooted in God\'s promises.", optionIndex: 4 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Conditional assurance: We can know we are in grace now, but final perseverance remains uncertain and requires ongoing cooperation.", optionIndex: 5 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Conditional assurance: We can know we are in grace now, but final perseverance remains uncertain and requires ongoing cooperation.", optionIndex: 5 }
    ],
    25: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "A special grace to be humbly prayed for; not guaranteed, but God is faithful.", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "A special grace to be humbly prayed for; not guaranteed, but God is faithful.", optionIndex: 0 },
        { saint: "John Calvin", era: "1509–1564", position: "Infallibly granted to those truly predestined; the elect cannot finally fall away.", optionIndex: 1 },
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "Infallibly granted to those truly predestined; the elect cannot finally fall away.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "A mystery better handled pastorally than speculatively; emphasize fidelity in the present.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Assurance of salvation is central to the Gospel\'s comfort; excessive emphasis on uncertainty is harmful.", optionIndex: 3 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Assurance of salvation is central to the Gospel\'s comfort; excessive emphasis on uncertainty is harmful.", optionIndex: 3 }
    ],
    26: [
        { saint: "Domingo Báñez, O.P.", era: "1528–1604", position: "Grace is intrinsically efficacious—it infallibly moves the will while preserving freedom", optionIndex: 0 },
        { saint: "Reginald Garrigou-Lagrange, O.P.", era: "1877–1964", position: "Grace is intrinsically efficacious—it infallibly moves the will while preserving freedom", optionIndex: 0 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Grace is extrinsically efficacious through God\'s middle knowledge of free response", optionIndex: 1 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Grace is extrinsically efficacious through God\'s middle knowledge of free response", optionIndex: 1 },
        { saint: "St. Robert Bellarmine, S.J.", era: "1542–1621", position: "Grace is congruous—fitted to circumstances so it will be freely accepted", optionIndex: 2 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Grace is congruous—fitted to circumstances so it will be freely accepted", optionIndex: 2 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Grace heals and elevates nature, enabling but not determining free response", optionIndex: 3 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Grace heals and elevates nature, enabling but not determining free response", optionIndex: 3 },
        { saint: "St. Francis de Sales", era: "1567–1622", position: "Grace is offered universally; efficacy depends wholly on human cooperation", optionIndex: 4 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Grace is offered universally; efficacy depends wholly on human cooperation", optionIndex: 4 }
    ],
    27: [
        { saint: "Gottschalk of Orbais", era: "c. 808–867", position: "God actively elects some to glory and, with equal sovereignty and by a parallel act of will, positively decrees the damnation of the rest for His glory.", optionIndex: 0 },
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "God actively elects some to glory and, with equal sovereignty and by a parallel act of will, positively decrees the damnation of the rest for His glory.", optionIndex: 0 },
        { saint: "Domingo Báñez, O.P.", era: "1528–1604", position: "God actively elects some to glory by an efficacious decree, but merely \'passes over\' (preteritio) the rest, justly permitting them to fall into the end their sins deserve withou...", optionIndex: 1 },
        { saint: "John Calvin", era: "1509–1564", position: "God actively elects some to glory by an efficacious decree, but merely \'passes over\' (preteritio) the rest, justly permitting them to fall into the end their sins deserve withou...", optionIndex: 1 },
        { saint: "Martin Luther", era: "1483–1546", position: "We should only speak of God predestining the elect to salvation; the loss of the reprobate is entirely a mystery of human rejection and resistance to grace, not a divine decree.", optionIndex: 2 },
        { saint: "Thomas Cranmer", era: "1489–1556", position: "We should only speak of God predestining the elect to salvation; the loss of the reprobate is entirely a mystery of human rejection and resistance to grace, not a divine decree.", optionIndex: 2 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Predestination is grounded in God\'s infallible foreknowledge (scientia media) of how each person would freely cooperate with grace in any given circumstance.", optionIndex: 3 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Predestination is grounded in God\'s infallible foreknowledge (scientia media) of how each person would freely cooperate with grace in any given circumstance.", optionIndex: 3 }
    ],
    28: [
        { saint: "Gottschalk of Orbais", era: "c. 808–867", position: "Supralapsarian: The decree of election logically precedes the decree to permit the Fall (Sovereignty emphasis).", optionIndex: 0 },
        { saint: "John Calvin", era: "1509–1564", position: "Supralapsarian: The decree of election logically precedes the decree to permit the Fall (Sovereignty emphasis).", optionIndex: 0 },
        { saint: "Francisco Suárez, S.J.", era: "1548–1617", position: "Infralapsarian: The decree of election logically follows the decree to permit the Fall (Mercy emphasis).", optionIndex: 1 },
        { saint: "Domingo Báñez, O.P.", era: "1528–1604", position: "Infralapsarian: The decree of election logically follows the decree to permit the Fall (Mercy emphasis).", optionIndex: 1 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "The decree is based on God\'s \'Middle Knowledge\' of how a person would freely respond in any given circumstance.", optionIndex: 2 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "The decree is based on God\'s \'Middle Knowledge\' of how a person would freely respond in any given circumstance.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "These scholastic categories are overly speculative and may distort the simplicity of the Gospel.", optionIndex: 3 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "These scholastic categories are overly speculative and may distort the simplicity of the Gospel.", optionIndex: 3 }
    ],
    29: [
        { saint: "Domingo Báñez, O.P.", era: "1528–1604", position: "Sufficient grace gives real power to act but becomes efficacious only with God\'s further motion", optionIndex: 0 },
        { saint: "Reginald Garrigou-Lagrange, O.P.", era: "1877–1964", position: "Sufficient grace gives real power to act but becomes efficacious only with God\'s further motion", optionIndex: 0 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Sufficient grace becomes efficacious through human free cooperation foreseen by middle knowledge", optionIndex: 1 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Sufficient grace becomes efficacious through human free cooperation foreseen by middle knowledge", optionIndex: 1 },
        { saint: "John Calvin", era: "1509–1564", position: "The distinction between sufficient and efficacious grace is largely verbal", optionIndex: 2 },
        { saint: "Martin Luther", era: "1483–1546", position: "The distinction between sufficient and efficacious grace is largely verbal", optionIndex: 2 },
        { saint: "St. Francis de Sales", era: "1567–1622", position: "Sufficient grace truly enables, and its becoming efficacious involves genuine synergy", optionIndex: 3 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Sufficient grace truly enables, and its becoming efficacious involves genuine synergy", optionIndex: 3 }
    ],
    30: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Instrumental efficient causality—sacraments are true instruments that cause grace", optionIndex: 0 },
        { saint: "Various Modern Theologians", era: "20th century", position: "Moral causality—sacraments move God to give grace, not physical instruments", optionIndex: 1 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Moral causality—sacraments move God to give grace, not physical instruments", optionIndex: 1 },
        { saint: "William of Ockham", era: "c. 1287–1347", position: "Occasional causality—God gives grace on the occasion of sacramental rites", optionIndex: 2 },
        { saint: "Various Modern Theologians", era: "20th century", position: "Occasional causality—God gives grace on the occasion of sacramental rites", optionIndex: 2 },
        { saint: "St. John Chrysostom", era: "c. 349–407", position: "Mystical/symbolic causality—sacraments participate in and manifest grace", optionIndex: 3 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "Mystical/symbolic causality—sacraments participate in and manifest grace", optionIndex: 3 }
    ],
    31: [
        { saint: "George Lindbeck", era: "1923–2018", position: "Agree - Augustinian and Bañezian positions share significant common ground. JDDJ was right.", optionIndex: 0 },
        { saint: "Louis Bouyer", era: "1913–2004", position: "Agree - Augustinian and Bañezian positions share significant common ground. JDDJ was right.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Partially - overlap on grace\'s priority exists, but merit and sacraments differ substantially.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Partially - overlap on grace\'s priority exists, but merit and sacraments differ substantially.", optionIndex: 1 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Disagree - Protestant soteriology is forensic and extrinsic. Catholic justification is real transformation.", optionIndex: 2 },
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "Disagree - Protestant soteriology is forensic and extrinsic. Catholic justification is real transformation.", optionIndex: 2 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Strongly disagree - Trent definitively condemned sola fide as Protestants teach it.", optionIndex: 3 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Strongly disagree - Trent definitively condemned sola fide as Protestants teach it.", optionIndex: 3 }
    ],
    32: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "\'Grace does not destroy nature but perfects it.\' The Thomistic synthesis is perennially valid.", optionIndex: 0 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "\'Grace does not destroy nature but perfects it.\' The Thomistic synthesis is perennially valid.", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "\'Our hearts are restless until they rest in Thee.\' Augustine\'s interiority and grace theology are primary.", optionIndex: 1 },
        { saint: "St. Monica", era: "c. 331–387", position: "\'Our hearts are restless until they rest in Thee.\' Augustine\'s interiority and grace theology are primary.", optionIndex: 1 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "\'Finding God in all things.\' Ignatian discernment and active engagement with the world.", optionIndex: 2 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "\'Finding God in all things.\' Ignatian discernment and active engagement with the world.", optionIndex: 2 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "\'Pray and work.\' The Benedictine balance of liturgy, labor, and stability.", optionIndex: 3 },
        { saint: "St. Bernard of Clairvaux", era: "1090–1153", position: "\'Pray and work.\' The Benedictine balance of liturgy, labor, and stability.", optionIndex: 3 },
        { saint: "St. Francis of Assisi", era: "1181–1226", position: "\'Lady Poverty.\' Franciscan simplicity, creation spirituality, and joyful service.", optionIndex: 4 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "\'Lady Poverty.\' Franciscan simplicity, creation spirituality, and joyful service.", optionIndex: 4 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Ressourcement - return to Fathers and Scripture to renew the Church.", optionIndex: 5 }
    ],
    33: [
        { saint: "Jacques-Bénigne Bossuet", era: "1627–1704", position: "Papal authority as exercised today is a late innovation. Haec Sancta (1415) and early conciliar practice show a more collegial original model.", optionIndex: 0 },
        { saint: "Jean Gerson", era: "1363–1429", position: "Papal authority as exercised today is a late innovation. Haec Sancta (1415) and early conciliar practice show a more collegial original model.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Newman\'s development of doctrine applies: the seed of papal authority was always present, growing organically to Vatican I\'s definition.", optionIndex: 1 },
        { saint: "Joseph de Maistre", era: "1753–1821", position: "Papal primacy and jurisdiction were clearly exercised from the earliest centuries. Vatican I defined what was always believed and practiced.", optionIndex: 2 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Papal primacy and jurisdiction were clearly exercised from the earliest centuries. Vatican I defined what was always believed and practiced.", optionIndex: 2 },
        { saint: "Johann Adam Möhler", era: "1796–1838", position: "The charism is real but over-centralization is a legitimate concern. Subsidiarity should govern how papal authority is exercised in practice.", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "The charism is real but over-centralization is a legitimate concern. Subsidiarity should govern how papal authority is exercised in practice.", optionIndex: 3 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "Papal authority as currently practiced is a Western development the East never accepted. Its maximalist form is a major obstacle to reunion.", optionIndex: 4 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "Papal authority as currently practiced is a Western development the East never accepted. Its maximalist form is a major obstacle to reunion.", optionIndex: 4 }
    ],
    34: [
        { saint: "John Calvin", era: "1509–1564", position: "No: the truly elect will certainly persevere; apparent apostasy proves one was never truly saved.", optionIndex: 0 },
        { saint: "Gottschalk of Orbais", era: "c. 808–867", position: "No: the truly elect will certainly persevere; apparent apostasy proves one was never truly saved.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Yes: mortal sin destroys justifying grace, but it can be restored through penance.", optionIndex: 1 },
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "Yes: mortal sin destroys justifying grace, but it can be restored through penance.", optionIndex: 1 },
        { saint: "Martin Luther", era: "1483–1546", position: "Possible but difficult: believers can fall from grace but God\'s preserving work is powerful.", optionIndex: 2 },
        { saint: "John Wesley", era: "1703–1791", position: "Possible but difficult: believers can fall from grace but God\'s preserving work is powerful.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The question framed wrongly: focus on God\'s faithfulness and our response in the present.", optionIndex: 3 },
        { saint: "St. John Paul II", era: "1920–2005", position: "The question framed wrongly: focus on God\'s faithfulness and our response in the present.", optionIndex: 3 }
    ],
    35: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Saints intercede for us; we may invoke their prayers and venerate relics and images.", optionIndex: 0 },
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "Saints intercede for us; we may invoke their prayers and venerate relics and images.", optionIndex: 0 },
        { saint: "John Calvin", era: "1509–1564", position: "Saints are examples of faith; invocation is unbiblical and borders on idolatry.", optionIndex: 1 },
        { saint: "Martin Luther", era: "1483–1546", position: "Saints are examples of faith; invocation is unbiblical and borders on idolatry.", optionIndex: 1 },
        { saint: "Thomas Cranmer", era: "1489–1556", position: "Saints are honored as examples; limited invocation may be permissible.", optionIndex: 2 },
        { saint: "Martin Luther", era: "1483–1546", position: "Saints are honored as examples; limited invocation may be permissible.", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "The communion of saints includes mutual prayer; the details are mysterious.", optionIndex: 3 }
    ],
    36: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Dogmatically binding: Christ has two complete natures, divine and human, without confusion or separation.", optionIndex: 0 },
        { saint: "St. Cyril of Alexandria", era: "c. 376–444", position: "Dogmatically binding: Christ has two complete natures, divine and human, without confusion or separation.", optionIndex: 0 },
        { saint: "St. Photios the Great", era: "c. 810–893", position: "Correct but the \'one nature\' (miaphysite) formula of Cyril is also orthodox if properly understood.", optionIndex: 1 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Correct but the \'one nature\' (miaphysite) formula of Cyril is also orthodox if properly understood.", optionIndex: 1 },
        { saint: "St. Athanasius", era: "c. 296–373", position: "Chalcedon betrayed Cyril: \'one incarnate nature of God the Word\' is the authentic formula.", optionIndex: 2 },
        { saint: "St. Cyril of Alexandria", era: "c. 376–444", position: "Chalcedon betrayed Cyril: \'one incarnate nature of God the Word\' is the authentic formula.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The terminology matters less than confessing Christ as truly God and truly man.", optionIndex: 3 },
        { saint: "Louis Bouyer", era: "1913–2004", position: "The terminology matters less than confessing Christ as truly God and truly man.", optionIndex: 3 }
    ],
    37: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Aristotelian-Thomist Transubstantiation: The substance of bread and wine becomes Christ\'s Body and Blood; accidents remain. Christ is present per modum substantiae, not locally.", optionIndex: 0 },
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "Aristotelian-Thomist Transubstantiation: The substance of bread and wine becomes Christ\'s Body and Blood; accidents remain. Christ is present per modum substantiae, not locally.", optionIndex: 0 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Scotist Formal-Metaphysical Presence: Real conversion affirmed, but explained via formal distinctions and haecceity rather than strict Aristotelian substance-accident categories.", optionIndex: 1 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "Scotist Formal-Metaphysical Presence: Real conversion affirmed, but explained via formal distinctions and haecceity rather than strict Aristotelian substance-accident categories.", optionIndex: 1 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Non-Corporeal Substantial Presence: Christ is fully and truly present in substance, but not as a quantitative body in the mode of extension. Emphasizes sacramental mode of exist...", optionIndex: 2 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Non-Corporeal Substantial Presence: Christ is fully and truly present in substance, but not as a quantitative body in the mode of extension. Emphasizes sacramental mode of exist...", optionIndex: 2 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Sign-Reality (Sacramentum–Res) Model: Distinguishes objective sacramental sign from spiritual union received fruitfully by faith. Augustinian sacramental theology.", optionIndex: 3 },
        { saint: "St. John of the Cross", era: "1542–1591", position: "Veiled Objective Reality: Christ is truly present but hidden under sacramental appearances; faith pierces the veil. Patristic emphasis on mystery and invisibility.", optionIndex: 4 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Veiled Objective Reality: Christ is truly present but hidden under sacramental appearances; faith pierces the veil. Patristic emphasis on mystery and invisibility.", optionIndex: 4 },
        { saint: "St. John Chrysostom", era: "c. 349–407", position: "Liturgical-Mystical Participation (Eastern): The Eucharist as transforming communion in the deified Christ. Less focus on metaphysical mechanism, more on participation in divine...", optionIndex: 5 },
        { saint: "St. John of the Cross", era: "1542–1591", position: "Liturgical-Mystical Participation (Eastern): The Eucharist as transforming communion in the deified Christ. Less focus on metaphysical mechanism, more on participation in divine...", optionIndex: 5 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Ratramnian Spiritual-Real Presence: Christ truly present but not in a crude bodily manner; emphasizes spiritual reality and ecclesial faith over physical identity.", optionIndex: 6 },
        { saint: "Edward Schillebeeckx, O.P.", era: "1914–2009", position: "Ratramnian Spiritual-Real Presence: Christ truly present but not in a crude bodily manner; emphasizes spiritual reality and ecclesial faith over physical identity.", optionIndex: 6 }
    ],
    38: [
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "Strongly affirm: Grace is given by valid administration regardless of minister\'s holiness", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Strongly affirm: Grace is given by valid administration regardless of minister\'s holiness", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Affirm, but recipient\'s disposition significantly affects fruitfulness", optionIndex: 1 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Affirm, but recipient\'s disposition significantly affects fruitfulness", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The emphasis can obscure the importance of faith and community", optionIndex: 2 },
        { saint: "Edward Schillebeeckx, O.P.", era: "1914–2009", position: "The emphasis can obscure the importance of faith and community", optionIndex: 2 },
        { saint: "St. John Chrysostom", era: "c. 349–407", position: "Valid but the Eastern tradition emphasizes epiclesis and mystery over mechanism", optionIndex: 3 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "Valid but the Eastern tradition emphasizes epiclesis and mystery over mechanism", optionIndex: 3 }
    ],
    39: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Ad orientem (same direction as people): Expresses common worship toward God", optionIndex: 0 },
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "Ad orientem (same direction as people): Expresses common worship toward God", optionIndex: 0 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Versus populum (facing people): Emphasizes community and participation", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Either is legitimate depending on circumstances", optionIndex: 2 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Either is legitimate depending on circumstances", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "The question is secondary to interior participation", optionIndex: 3 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "The question is secondary to interior participation", optionIndex: 3 }
    ],
    40: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "On the tongue while kneeling: Traditional and most reverent", optionIndex: 0 },
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "On the tongue while kneeling: Traditional and most reverent", optionIndex: 0 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "On the tongue standing: Traditional but adapted", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "On the tongue standing: Traditional but adapted", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "In the hand is legitimate and can express lay dignity", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Either way with proper reverence; interior disposition matters most", optionIndex: 3 }
    ],
    41: [
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Largely mistaken: The Novus Ordo represents a break with tradition. The TLM should be normative again.", optionIndex: 0 },
        { saint: "Various Authors", era: "20th–21st c.", position: "Largely mistaken: The Novus Ordo represents a break with tradition. The TLM should be normative again.", optionIndex: 0 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Good intentions but badly implemented. A \'reform of the reform\' is needed — reforming the Novus Ordo toward Sacrosanctum Concilium\'s actual vision, perhaps toward a reverent ver...", optionIndex: 1 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Good intentions but badly implemented. A \'reform of the reform\' is needed — reforming the Novus Ordo toward Sacrosanctum Concilium\'s actual vision, perhaps toward a reverent ver...", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Generally positive: The reforms made liturgy more accessible and participatory; further inculturation should continue.", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Generally positive: The reforms made liturgy more accessible and participatory; further inculturation should continue.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Both forms have value. The Ordinary and Extraordinary Forms should coexist peacefully as mutual enrichment.", optionIndex: 3 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Both forms have value. The Ordinary and Extraordinary Forms should coexist peacefully as mutual enrichment.", optionIndex: 3 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "The Eastern Catholic liturgies show what reverent vernacular worship looks like. The West should learn from them rather than fight over Latin vs. vernacular.", optionIndex: 4 },
        { saint: "Alexander Schmemann", era: "1921–1983", position: "The Eastern Catholic liturgies show what reverent vernacular worship looks like. The West should learn from them rather than fight over Latin vs. vernacular.", optionIndex: 4 }
    ],
    42: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Should be the normative form or at least freely available everywhere", optionIndex: 0 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Should be the normative form or at least freely available everywhere", optionIndex: 0 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "A legitimate option that enriches the Church\'s liturgical life", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "A legitimate option that enriches the Church\'s liturgical life", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Of historical interest but the reformed liturgy is the Church\'s lex orandi", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Should be restricted to prevent division", optionIndex: 3 }
    ],
    43: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Essential: Sacred silence enables contemplation and encounter with mystery", optionIndex: 0 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Essential: Sacred silence enables contemplation and encounter with mystery", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Important but balanced with congregational participation", optionIndex: 1 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Important but balanced with congregational participation", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Often excessive in pre-conciliar liturgy; active participation is key", optionIndex: 2 },
        { saint: "St. John Chrysostom", era: "c. 349–407", position: "Deeply valued in Eastern liturgy as part of the mystery", optionIndex: 3 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "Deeply valued in Eastern liturgy as part of the mystery", optionIndex: 3 }
    ],
    44: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Very important: Rubrics protect the sacred and express theology", optionIndex: 0 },
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "Very important: Rubrics protect the sacred and express theology", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Important but not at the expense of pastoral adaptation", optionIndex: 1 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Important but not at the expense of pastoral adaptation", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Secondary: The spirit of the liturgy matters more than exact rubrics", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Secondary: The spirit of the liturgy matters more than exact rubrics", optionIndex: 2 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Rubrics serve the mystery and should be followed with understanding", optionIndex: 3 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Rubrics serve the mystery and should be followed with understanding", optionIndex: 3 }
    ],
    45: [
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Necessary to prevent the TLM from becoming a flag for rejecting Vatican II.", optionIndex: 0 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Necessary to prevent the TLM from becoming a flag for rejecting Vatican II.", optionIndex: 0 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Pastorally devastating. Summorum Pontificum was working. Benedict XVI was right.", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Pastorally devastating. Summorum Pontificum was working. Benedict XVI was right.", optionIndex: 1 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "An unjust suppression. I attend TLM regardless of canonical regularity.", optionIndex: 2 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "An unjust suppression. I attend TLM regardless of canonical regularity.", optionIndex: 2 },
        { saint: "Pope Francis", era: "1936–present", position: "The Pope has authority to regulate liturgy. I obey even if I preferred the old policy.", optionIndex: 3 },
        { saint: "Joseph de Maistre", era: "1753–1821", position: "The Pope has authority to regulate liturgy. I obey even if I preferred the old policy.", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Understandable concern but heavy-handed. Dialogue would have been better.", optionIndex: 4 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Understandable concern but heavy-handed. Dialogue would have been better.", optionIndex: 4 }
    ],
    46: [
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "The dogma magnificently vindicates Augustine: Mary\'s singular exemption proves how universal and inescapable original sin truly is—only an extraordinary divine intervention coul...", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "The dogma magnificently vindicates Augustine: Mary\'s singular exemption proves how universal and inescapable original sin truly is—only an extraordinary divine intervention coul...", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "The Immaculate Conception represents a harmonious synthesis: Mary was preserved by grace applied in anticipation of Christ\'s merits, fully consistent with Augustinian hamartiolo...", optionIndex: 1 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "The Immaculate Conception represents a harmonious synthesis: Mary was preserved by grace applied in anticipation of Christ\'s merits, fully consistent with Augustinian hamartiolo...", optionIndex: 1 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Bl. Scotus rightly saw that God could, and therefore did, preserve Mary entirely from the stain of original sin from the first instant—a \'more perfect redemption\' that requires ...", optionIndex: 2 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "Bl. Scotus rightly saw that God could, and therefore did, preserve Mary entirely from the stain of original sin from the first instant—a \'more perfect redemption\' that requires ...", optionIndex: 2 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "The East honors Mary as the \'All-Holy\' (Panagia) and \'Immaculate\' without the Latin juridical framework of inherited guilt or \'original sin\' in the Augustinian sense; both tradi...", optionIndex: 3 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "The East honors Mary as the \'All-Holy\' (Panagia) and \'Immaculate\' without the Latin juridical framework of inherited guilt or \'original sin\' in the Augustinian sense; both tradi...", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The dogma was a medieval development driven largely by popular piety and Franciscan advocacy, not strict theological necessity; Augustine\'s severe view of inherited guilt makes ...", optionIndex: 4 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "The dogma was a medieval development driven largely by popular piety and Franciscan advocacy, not strict theological necessity; Augustine\'s severe view of inherited guilt makes ...", optionIndex: 4 }
    ],
    47: [
        { saint: "Blaise Pascal", era: "1623–1662", position: "Authentic Augustinianism unjustly condemned due to Jesuit political maneuvering.", optionIndex: 0 },
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "Authentic Augustinianism unjustly condemned due to Jesuit political maneuvering.", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Contained genuine insights about grace but went too far into rigorism and near-Calvinism.", optionIndex: 1 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Contained genuine insights about grace but went too far into rigorism and near-Calvinism.", optionIndex: 1 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Rightly condemned. Its rigorism harmed souls and its ecclesiology was schismatic.", optionIndex: 2 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Rightly condemned. Its rigorism harmed souls and its ecclesiology was schismatic.", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "A complex phenomenon. Some Jansenists were holy; the label was applied too broadly.", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "A complex phenomenon. Some Jansenists were holy; the label was applied too broadly.", optionIndex: 3 }
    ],
    48: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Theology is a true science with demonstrative certainty, proceeding from principles known by divine faith to conclusions known by theological reason.", optionIndex: 0 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Theology is a true science with demonstrative certainty, proceeding from principles known by divine faith to conclusions known by theological reason.", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Theology is wisdom more than science — sapiential knowledge rooted in contemplative union with God, not merely syllogistic demonstration.", optionIndex: 1 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "Theology is wisdom more than science — sapiential knowledge rooted in contemplative union with God, not merely syllogistic demonstration.", optionIndex: 1 },
        { saint: "William of Ockham", era: "c. 1287–1347", position: "Theological conclusions are probable opinions, not demonstrations. Only Scripture and defined dogma are certain; the rest is theological opinion.", optionIndex: 2 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Theological conclusions are probable opinions, not demonstrations. Only Scripture and defined dogma are certain; the rest is theological opinion.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Theology must be done in dialogue with contemporary philosophy and science; its \'certainties\' are always culturally conditioned and revisable.", optionIndex: 3 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Theology must be done in dialogue with contemporary philosophy and science; its \'certainties\' are always culturally conditioned and revisable.", optionIndex: 3 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "The Eastern tradition emphasizes apophatic theology — God is known through what He is not. Western \'certainty\' can become rationalist presumption.", optionIndex: 4 },
        { saint: "St. Photios the Great", era: "c. 810–893", position: "The Eastern tradition emphasizes apophatic theology — God is known through what He is not. Western \'certainty\' can become rationalist presumption.", optionIndex: 4 }
    ],
    49: [
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Scripture has the highest dignity and is the supreme norm, but only as read within apostolic Tradition and the Church\'s infallible teaching.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Scripture and Tradition are co-equal fonts of revelation, while the Magisterium is their authoritative interpreter and guardian. (Thomist, Thomist (Realist))", optionIndex: 1 },
        { saint: "Étienne Gilson", era: "1884–1978", position: "Scripture and Tradition are co-equal fonts of revelation, while the Magisterium is their authoritative interpreter and guardian. (Thomist, Thomist (Realist))", optionIndex: 1 },
        { saint: "Joseph de Maistre", era: "1753–1821", position: "In practice, the Magisterium is the proximate rule of faith; Scripture and Tradition are received through that living authority.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "In practice, the Magisterium is the proximate rule of faith; Scripture and Tradition are received through that living authority.", optionIndex: 2 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "The hierarchy can err widely in non-definitive matters; Scripture and the Fathers supply the main corrective.", optionIndex: 3 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "The hierarchy can err widely in non-definitive matters; Scripture and the Fathers supply the main corrective.", optionIndex: 3 }
    ],
    50: [
        { saint: "Joseph de Maistre", era: "1753–1821", position: "Full, immediate, ordinary jurisdiction over the entire Church; the ordinary magisterium shares in a broad practical infallibility.", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Full, immediate, ordinary jurisdiction over the entire Church; the ordinary magisterium shares in a broad practical infallibility.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Real primacy with ordinary jurisdiction, exercised with restraint; infallibility is rare but the ordinary magisterium binds seriously.", optionIndex: 1 },
        { saint: "Johann Adam Möhler", era: "1796–1838", position: "Primacy of honor with jurisdiction of final appeal; infallibility is strictly and rarely applied to ex cathedra definitions only.", optionIndex: 2 },
        { saint: "Jacques-Bénigne Bossuet", era: "1627–1704", position: "Primacy of honor with jurisdiction of final appeal; infallibility is strictly and rarely applied to ex cathedra definitions only.", optionIndex: 2 },
        { saint: "Jean Gerson", era: "1363–1429", position: "Conciliar authority is supreme in emergencies; the pope is bound by councils and tradition, not above them.", optionIndex: 3 },
        { saint: "Jacques-Bénigne Bossuet", era: "1627–1704", position: "Conciliar authority is supreme in emergencies; the pope is bound by councils and tradition, not above them.", optionIndex: 3 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "Communion ecclesiology: The pope is head of a communion of local churches, each with proper autonomy; patriarchal structures should be restored.", optionIndex: 4 },
        { saint: "Cardinal Walter Kasper", era: "1933–present", position: "Communion ecclesiology: The pope is head of a communion of local churches, each with proper autonomy; patriarchal structures should be restored.", optionIndex: 4 }
    ],
    51: [
        { saint: "Joseph de Maistre", era: "1753–1821", position: "Directly from the Pope; bishops are essentially papal delegates", optionIndex: 0 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "From Christ through episcopal consecration, but exercised in communion with Rome", optionIndex: 1 },
        { saint: "Johann Adam Möhler", era: "1796–1838", position: "From Christ through episcopal consecration, but exercised in communion with Rome", optionIndex: 1 },
        { saint: "Jacques-Bénigne Bossuet", era: "1627–1704", position: "From Christ through consecration; Rome has primacy but not source of jurisdiction", optionIndex: 2 },
        { saint: "Jean Gerson", era: "1363–1429", position: "From Christ through consecration; Rome has primacy but not source of jurisdiction", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Bishops are true ordinaries with proper authority; papal primacy is real but limited", optionIndex: 3 }
    ],
    52: [
        { saint: "Joseph de Maistre", era: "1753–1821", position: "Juridical unity under papal authority with doctrinal uniformity enforced from Rome. Unity requires obedience.", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Juridical unity under papal authority with doctrinal uniformity enforced from Rome. Unity requires obedience.", optionIndex: 0 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "Communion of churches united in faith, sacraments, and fellowship with Rome, respecting legitimate diversity.", optionIndex: 1 },
        { saint: "Cardinal Walter Kasper", era: "1933–present", position: "Communion of churches united in faith, sacraments, and fellowship with Rome, respecting legitimate diversity.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Unity in essentials, liberty in doubtful matters, charity in all. The papacy preserves unity without crushing diversity.", optionIndex: 2 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Through shared liturgical tradition, doctrinal fidelity, and resistance to modernist innovations that fracture the faith.", optionIndex: 3 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Through shared liturgical tradition, doctrinal fidelity, and resistance to modernist innovations that fracture the faith.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Through ongoing synodal dialogue, inculturation, and the sensus fidei of the whole people of God.", optionIndex: 4 },
        { saint: "Cardinal Walter Kasper", era: "1933–present", position: "Through ongoing synodal dialogue, inculturation, and the sensus fidei of the whole people of God.", optionIndex: 4 }
    ],
    53: [
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Yes, always—temporal authority is subordinate to spiritual in these matters", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Yes, always—temporal authority is subordinate to spiritual in these matters", optionIndex: 0 },
        { saint: "Thomas Pink", era: "Contemporary", position: "Generally yes, but rulers have their own prudential competence", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Generally yes, but rulers have their own prudential competence", optionIndex: 1 },
        { saint: "Jacques-Bénigne Bossuet", era: "1627–1704", position: "Only when the teaching is clear and definitive", optionIndex: 2 },
        { saint: "Johann Adam Möhler", era: "1796–1838", position: "Only when the teaching is clear and definitive", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "No—temporal and spiritual authority should be strictly separate", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "No—temporal and spiritual authority should be strictly separate", optionIndex: 3 }
    ],
    54: [
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "A fully authoritative ecumenical council whose teachings are binding; its pastoral fruits, while imperfect, represent genuine renewal.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "A fully authoritative ecumenical council whose teachings are binding; its pastoral fruits, while imperfect, represent genuine renewal.", optionIndex: 0 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Authoritative but pastoral in character — it defined no new dogma. Its ambiguities have been exploited, requiring a hermeneutic of continuity.", optionIndex: 1 },
        { saint: "Joseph Ratzinger", era: "1927–2022", position: "Authoritative but pastoral in character — it defined no new dogma. Its ambiguities have been exploited, requiring a hermeneutic of continuity.", optionIndex: 1 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Contains serious ambiguities and ruptures with prior teaching (religious liberty, ecumenism, collegiality) that need formal correction.", optionIndex: 2 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Contains serious ambiguities and ruptures with prior teaching (religious liberty, ecumenism, collegiality) that need formal correction.", optionIndex: 2 },
        { saint: "Various Authors", era: "20th–21st c.", position: "A robber council or invalid assembly that deviated from the Faith; its documents lack binding force.", optionIndex: 3 },
        { saint: "Bp. Guérard des Lauriers", era: "1898–1988", position: "A robber council or invalid assembly that deviated from the Faith; its documents lack binding force.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The \'event\' of Vatican II — its spirit of dialogue, openness, and reform — matters more than its letter. The Council opened windows the Church should keep open.", optionIndex: 4 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "The \'event\' of Vatican II — its spirit of dialogue, openness, and reform — matters more than its letter. The Council opened windows the Church should keep open.", optionIndex: 4 }
    ],
    55: [
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Fully legitimate popes with ordinary magisterial authority", optionIndex: 0 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Legitimate but their prudential decisions can be resisted when conflicting with Tradition", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Legitimate but their prudential decisions can be resisted when conflicting with Tradition", optionIndex: 1 },
        { saint: "Bp. Guérard des Lauriers", era: "1898–1988", position: "Material but not formal popes", optionIndex: 2 },
        { saint: "Various Authors", era: "20th–21st c.", position: "Not true popes at all; the See has been vacant", optionIndex: 3 }
    ],
    56: [
        { saint: "Joseph de Maistre", era: "1753–1821", position: "Never: Submission to Rome is essential to Catholic identity", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Never: Submission to Rome is essential to Catholic identity", optionIndex: 0 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Only in extreme cases where directives clearly contradict defined doctrine", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Only in extreme cases where directives clearly contradict defined doctrine", optionIndex: 1 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Yes, when they conflict with Sacred Tradition and the sensus fidelium", optionIndex: 2 },
        { saint: "Various Authors", era: "20th–21st c.", position: "Yes, when they conflict with Sacred Tradition and the sensus fidelium", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Prudent disagreement is possible but public resistance is rarely justified", optionIndex: 3 }
    ],
    57: [
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Nations may legitimately negotiate appointment rights and synodal authority with Rome, provided they don\'t strongarm the Holy See.", optionIndex: 0 },
        { saint: "Juan Donoso Cortés", era: "1809–1853", position: "Would make sense with stable Catholic monarchies, but impractical in modern liberal democracies.", optionIndex: 1 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Would make sense with stable Catholic monarchies, but impractical in modern liberal democracies.", optionIndex: 1 },
        { saint: "Joseph de Maistre", era: "1753–1821", position: "A dangerous affront to papal authority. The Pope\'s universal jurisdiction must not be compromised.", optionIndex: 2 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "A dangerous affront to papal authority. The Pope\'s universal jurisdiction must not be compromised.", optionIndex: 2 },
        { saint: "Pope Francis", era: "1936–present", position: "Risks enabling nationalists to co-opt the Church and undermine her transnational mission.", optionIndex: 3 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Risks enabling nationalists to co-opt the Church and undermine her transnational mission.", optionIndex: 3 }
    ],
    58: [
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Reject it - Christendom should be restored. Christ must reign socially.", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Reject it - Christendom should be restored. Christ must reign socially.", optionIndex: 0 },
        { saint: "Thomas Pink", era: "Contemporary", position: "Accept pragmatically but work for culture\'s conversion over time.", optionIndex: 1 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Accept pragmatically but work for culture\'s conversion over time.", optionIndex: 1 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Liberal democracy, rightly understood, is compatible with Catholicism.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Liberal democracy, rightly understood, is compatible with Catholicism.", optionIndex: 2 },
        { saint: "G.K. Chesterton", era: "1874–1936", position: "Fine but must be limited by natural law and subsidiarity.", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Fine but must be limited by natural law and subsidiarity.", optionIndex: 3 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Church should focus on souls, not political arrangements.", optionIndex: 4 },
        { saint: "St. Bruno of Cologne", era: "c. 1030–1101", position: "Church should focus on souls, not political arrangements.", optionIndex: 4 }
    ],
    59: [
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Yes: Patristic retrieval corrected neo-scholastic narrowness", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Partially: Some good insights but also problematic tendencies", optionIndex: 1 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Partially: Some good insights but also problematic tendencies", optionIndex: 1 },
        { saint: "Cardinal Alfredo Ottaviani", era: "1890–1979", position: "No: It undermined sound theology and paved way for modernism", optionIndex: 2 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "No: It undermined sound theology and paved way for modernism", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "It\'s complicated: Need to distinguish various authors and claims", optionIndex: 3 }
    ],
    60: [
        { saint: "Joseph de Maistre", era: "1753–1821", position: "Episcopal: bishops in apostolic succession are essential to the Church\'s structure.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Episcopal: bishops in apostolic succession are essential to the Church\'s structure.", optionIndex: 0 },
        { saint: "John Calvin", era: "1509–1564", position: "Presbyterian: governance by elders in graded courts (session, presbytery, synod, assembly).", optionIndex: 1 },
        { saint: "John Calvin", era: "1509–1564", position: "Congregational: each local congregation is autonomous under Christ.", optionIndex: 2 },
        { saint: "Joseph de Maistre", era: "1753–1821", position: "The Pope holds supreme jurisdiction; episcopal authority derives from him.", optionIndex: 3 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "The Pope holds supreme jurisdiction; episcopal authority derives from him.", optionIndex: 3 },
        { saint: "St. Photios the Great", era: "c. 810–893", position: "Synodal/collegial: bishops govern together; Rome has primacy of honor, not jurisdiction.", optionIndex: 4 },
        { saint: "Cardinal Walter Kasper", era: "1933–present", position: "Synodal/collegial: bishops govern together; Rome has primacy of honor, not jurisdiction.", optionIndex: 4 }
    ],
    61: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "A legitimate and necessary doctrinal development clarifying Trinitarian relations.", optionIndex: 0 },
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "A legitimate and necessary doctrinal development clarifying Trinitarian relations.", optionIndex: 0 },
        { saint: "Louis Bouyer", era: "1913–2004", position: "Theologically defensible but pastorally unwise to have added unilaterally; dialogue needed.", optionIndex: 1 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Theologically defensible but pastorally unwise to have added unilaterally; dialogue needed.", optionIndex: 1 },
        { saint: "St. Photios the Great", era: "c. 810–893", position: "A Western addition that distorts Trinitarian theology; the Spirit proceeds from the Father alone.", optionIndex: 2 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "A Western addition that distorts Trinitarian theology; the Spirit proceeds from the Father alone.", optionIndex: 2 },
        { saint: "Jean Gerson", era: "1363–1429", position: "The original Creed should be restored; Rome overstepped in adding to an ecumenical formula.", optionIndex: 3 },
        { saint: "Jacques-Bénigne Bossuet", era: "1627–1704", position: "The original Creed should be restored; Rome overstepped in adding to an ecumenical formula.", optionIndex: 3 }
    ],
    62: [
        { saint: "St. Photios the Great", era: "c. 810–893", position: "Icons are windows to heaven; veneration is essential to Orthodox piety and theology.", optionIndex: 0 },
        { saint: "Alexander Schmemann", era: "1921–1983", position: "Icons are windows to heaven; veneration is essential to Orthodox piety and theology.", optionIndex: 0 },
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "Sacred images are legitimate aids to devotion, distinct from idolatry.", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Sacred images are legitimate aids to devotion, distinct from idolatry.", optionIndex: 1 },
        { saint: "Martin Luther", era: "1483–1546", position: "Images are acceptable but not essential; the Word preached is primary.", optionIndex: 2 },
        { saint: "John Calvin", era: "1509–1564", position: "Images are acceptable but not essential; the Word preached is primary.", optionIndex: 2 },
        { saint: "John Calvin", era: "1509–1564", position: "Icons risk becoming idols; worship should focus on God alone.", optionIndex: 3 }
    ],
    63: [
        { saint: "Joseph de Maistre", era: "1753–1821", position: "Interior assent is normally required; public disagreement risks scandal and disobedience.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Interior assent is normally required; public disagreement risks scandal and disobedience.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Religious submission is owed, but one may withhold interior assent cautiously while seeking clarification and remaining obedient.", optionIndex: 1 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Respectful, reasoned critique is sometimes necessary; the Fathers and Tradition can correct modern confusions.", optionIndex: 2 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "If it conflicts with Tradition, public resistance is justified.", optionIndex: 3 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "If it conflicts with Tradition, public resistance is justified.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Conscience is supreme; dissent can be fully legitimate.", optionIndex: 4 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Conscience is supreme; dissent can be fully legitimate.", optionIndex: 4 }
    ],
    64: [
        { saint: "Alasdair MacIntyre", era: "1929–present", position: "Virtue ethics: Focus on character formation and the virtues (Virtue Ethics, Thomist (Natural Law))", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Virtue ethics: Focus on character formation and the virtues (Virtue Ethics, Thomist (Natural Law))", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Natural law: Universal norms knowable by reason, applied through casuistry (Thomist (Natural Law), Manualist)", optionIndex: 1 },
        { saint: "Henry Davis, S.J.", era: "1866–1952", position: "Natural law: Universal norms knowable by reason, applied through casuistry (Thomist (Natural Law), Manualist)", optionIndex: 1 },
        { saint: "St. John Paul II", era: "1920–2005", position: "Personalist: Emphasis on human dignity and concrete situations", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Personalist: Emphasis on human dignity and concrete situations", optionIndex: 2 },
        { saint: "Henry Davis, S.J.", era: "1866–1952", position: "Manualist: Clear rules and cases for confessional practice", optionIndex: 3 },
        { saint: "Cardinal Alfredo Ottaviani", era: "1890–1979", position: "Manualist: Clear rules and cases for confessional practice", optionIndex: 3 }
    ],
    65: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Never for intrinsically evil acts; prudence applies norms, doesn\'t create exceptions (Thomist (Natural Law), Manualist)", optionIndex: 0 },
        { saint: "Henry Davis, S.J.", era: "1866–1952", position: "Never for intrinsically evil acts; prudence applies norms, doesn\'t create exceptions (Thomist (Natural Law), Manualist)", optionIndex: 0 },
        { saint: "Richard McCormick, S.J.", era: "1922–2000", position: "Proportionate reason can justify apparent exceptions", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Proportionate reason can justify apparent exceptions", optionIndex: 1 },
        { saint: "St. John Paul II", era: "1920–2005", position: "Pastoral discernment may find that a norm doesn\'t apply in a particular case", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Pastoral discernment may find that a norm doesn\'t apply in a particular case", optionIndex: 2 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Epikeia allows departure from law\'s letter to fulfill its spirit", optionIndex: 3 },
        { saint: "Alasdair MacIntyre", era: "1929–present", position: "Epikeia allows departure from law\'s letter to fulfill its spirit", optionIndex: 3 }
    ],
    66: [
        { saint: "Bartolomé de Medina, O.P.", era: "1527–1580", position: "Probabilism: A solidly probable opinion favoring liberty may be followed, even if the opinion for the law is more probable.", optionIndex: 0 },
        { saint: "St. Alphonsus Liguori", era: "1696–1787", position: "Probabilism: A solidly probable opinion favoring liberty may be followed, even if the opinion for the law is more probable.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Equiprobabilism: One may follow the opinion favoring liberty only when it is equally or nearly as probable as the one favoring the law.", optionIndex: 1 },
        { saint: "St. Alphonsus Liguori", era: "1696–1787", position: "Equiprobabilism: One may follow the opinion favoring liberty only when it is equally or nearly as probable as the one favoring the law.", optionIndex: 1 },
        { saint: "Giovanni Patuzzi, O.P.", era: "1700–1769", position: "Tutiorism: One must always follow the safer opinion favoring the law. In doubt, the stricter path is morally required.", optionIndex: 2 },
        { saint: "Blaise Pascal", era: "1623–1662", position: "Tutiorism: One must always follow the safer opinion favoring the law. In doubt, the stricter path is morally required.", optionIndex: 2 },
        { saint: "St. John Paul II", era: "1920–2005", position: "Prudential discernment case-by-case: The confessor uses practical wisdom and pastoral sensitivity, not rigid systems.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Prudential discernment case-by-case: The confessor uses practical wisdom and pastoral sensitivity, not rigid systems.", optionIndex: 3 },
        { saint: "Henry Davis, S.J.", era: "1866–1952", position: "The manualist tradition provides clear, time-tested categories that aid confessors and penitents alike.", optionIndex: 4 },
        { saint: "Cardinal Alfredo Ottaviani", era: "1890–1979", position: "The manualist tradition provides clear, time-tested categories that aid confessors and penitents alike.", optionIndex: 4 }
    ],
    67: [
        { saint: "Henry Davis, S.J.", era: "1866–1952", position: "Essential: Provides clarity, precision, and practical guidance for confessors", optionIndex: 0 },
        { saint: "Cardinal Alfredo Ottaviani", era: "1890–1979", position: "Essential: Provides clarity, precision, and practical guidance for confessors", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Useful but needs integration with virtue ethics and Scripture (Thomist (Natural Law), Mainstream)", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Useful but needs integration with virtue ethics and Scripture (Thomist (Natural Law), Mainstream)", optionIndex: 1 },
        { saint: "Alasdair MacIntyre", era: "1929–present", position: "Problematic: Legalistic, minimalistic, and detached from spiritual growth", optionIndex: 2 },
        { saint: "St. John Paul II", era: "1920–2005", position: "Problematic: Legalistic, minimalistic, and detached from spiritual growth", optionIndex: 2 },
        { saint: "Richard McCormick, S.J.", era: "1922–2000", position: "Outdated and should be largely set aside", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Outdated and should be largely set aside", optionIndex: 3 }
    ],
    68: [
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Dominican: Contemplation for preaching; truth and intellectual apostolate", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Dominican: Contemplation for preaching; truth and intellectual apostolate", optionIndex: 0 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Jesuit: Finding God in all things; discernment, adaptability, active mission", optionIndex: 1 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Jesuit: Finding God in all things; discernment, adaptability, active mission", optionIndex: 1 },
        { saint: "St. Francis of Assisi", era: "1181–1226", position: "Franciscan: Poverty, simplicity, creation spirituality, affective devotion", optionIndex: 2 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "Franciscan: Poverty, simplicity, creation spirituality, affective devotion", optionIndex: 2 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Carmelite: Contemplative prayer, mystical ascent, interior transformation", optionIndex: 3 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "Carmelite: Contemplative prayer, mystical ascent, interior transformation", optionIndex: 3 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Benedictine: Liturgy, stability, ora et labora, monastic rhythm", optionIndex: 4 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Benedictine: Liturgy, stability, ora et labora, monastic rhythm", optionIndex: 4 },
        { saint: "St. Josemaría Escrivá", era: "1902–1975", position: "Opus Dei: Sanctification of ordinary work, lay spirituality", optionIndex: 5 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Opus Dei: Sanctification of ordinary work, lay spirituality", optionIndex: 5 },
        { saint: "St. Philip Neri", era: "1515–1595", position: "Oratorian: Community of secular priests, intellectual and pastoral", optionIndex: 6 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Oratorian: Community of secular priests, intellectual and pastoral", optionIndex: 6 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "No particular preference / diocesan spirituality", optionIndex: 7 }
    ],
    69: [
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Contemplative life ordered to preaching and teaching", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Contemplative life ordered to preaching and teaching", optionIndex: 0 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Pure contemplation in solitude", optionIndex: 1 },
        { saint: "St. Bruno of Cologne", era: "c. 1030–1101", position: "Pure contemplation in solitude", optionIndex: 1 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Active apostolate for the greater glory of God", optionIndex: 2 },
        { saint: "St. Josemaría Escrivá", era: "1902–1975", position: "Active apostolate for the greater glory of God", optionIndex: 2 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Liturgical prayer as the Church\'s public worship", optionIndex: 3 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Liturgical prayer as the Church\'s public worship", optionIndex: 3 },
        { saint: "St. Francis of Assisi", era: "1181–1226", position: "Evangelical poverty and simplicity among the people", optionIndex: 4 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "Evangelical poverty and simplicity among the people", optionIndex: 4 },
        { saint: "St. Josemaría Escrivá", era: "1902–1975", position: "Sanctification in ordinary secular life", optionIndex: 5 }
    ],
    70: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Triumphant proclamation and liberation of righteous — Harrowing of Hell.", optionIndex: 0 },
        { saint: "St. John Chrysostom", era: "c. 349–407", position: "Triumphant proclamation and liberation of righteous — Harrowing of Hell.", optionIndex: 0 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "Christ truly experienced full human death, including darkness, before rising.", optionIndex: 1 },
        { saint: "Hans Urs von Balthasar", era: "1905–1988", position: "Christ truly experienced full human death, including darkness, before rising.", optionIndex: 1 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Soteriological completion: saving work extends to those who died before.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Soteriological completion: saving work extends to those who died before.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Primarily creedal affirmation; avoid excessive speculation.", optionIndex: 3 },
        { saint: "Cardinal Alfredo Ottaviani", era: "1890–1979", position: "Primarily creedal affirmation; avoid excessive speculation.", optionIndex: 3 }
    ],
    71: [
        { saint: "St. Monica", era: "c. 331–387", position: "Interior journey: \'Return to yourself; truth dwells in the inner man.\'", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Interior journey: \'Return to yourself; truth dwells in the inner man.\'", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Ordered love (ordo amoris): rightly ordering desires toward God.", optionIndex: 1 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Grace and predestination: absolute priority of God\'s initiative.", optionIndex: 2 },
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "Grace and predestination: absolute priority of God\'s initiative.", optionIndex: 2 },
        { saint: "St. Monica", era: "c. 331–387", position: "Community life: \'One mind and one heart intent upon God.\'", optionIndex: 3 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Community life: \'One mind and one heart intent upon God.\'", optionIndex: 3 }
    ],
    72: [
        { saint: "St. Alphonsus Liguori", era: "1696–1787", position: "Moral theology: equiprobabilism between rigorism and laxism.", optionIndex: 0 },
        { saint: "Bartolomé de Medina, O.P.", era: "1527–1580", position: "Moral theology: equiprobabilism between rigorism and laxism.", optionIndex: 0 },
        { saint: "St. Alphonsus Liguori", era: "1696–1787", position: "Popular missions preaching \'abundant redemption\' to abandoned.", optionIndex: 1 },
        { saint: "St. Vincent de Paul", era: "1581–1660", position: "Popular missions preaching \'abundant redemption\' to abandoned.", optionIndex: 1 },
        { saint: "St. Alphonsus Liguori", era: "1696–1787", position: "Marian devotion: \'Glories of Mary\' and confidence in intercession.", optionIndex: 2 },
        { saint: "The Seven Holy Founders", era: "13th century", position: "Marian devotion: \'Glories of Mary\' and confidence in intercession.", optionIndex: 2 },
        { saint: "St. Alphonsus Liguori", era: "1696–1787", position: "Practical pastoral approach: meeting people where they are.", optionIndex: 3 },
        { saint: "St. Vincent de Paul", era: "1581–1660", position: "Practical pastoral approach: meeting people where they are.", optionIndex: 3 }
    ],
    73: [
        { saint: "St. John Bosco", era: "1815–1888", position: "Preventive system: reason, religion, loving-kindness in education.", optionIndex: 0 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Preventive system: reason, religion, loving-kindness in education.", optionIndex: 0 },
        { saint: "St. John Bosco", era: "1815–1888", position: "Joy and cheerfulness as essential witness, especially to youth.", optionIndex: 1 },
        { saint: "St. Francis of Assisi", era: "1181–1226", position: "Joy and cheerfulness as essential witness, especially to youth.", optionIndex: 1 },
        { saint: "St. John Bosco", era: "1815–1888", position: "Practical holiness in everyday life, accessible to all.", optionIndex: 2 },
        { saint: "St. Josemaría Escrivá", era: "1902–1975", position: "Practical holiness in everyday life, accessible to all.", optionIndex: 2 },
        { saint: "St. John Bosco", era: "1815–1888", position: "Devotion to Mary Help of Christians and the Eucharist.", optionIndex: 3 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Devotion to Mary Help of Christians and the Eucharist.", optionIndex: 3 }
    ],
    74: [
        { saint: "St. Vincent de Paul", era: "1581–1660", position: "\'The poor are our lords and masters\' — radical service to marginalized.", optionIndex: 0 },
        { saint: "St. Francis of Assisi", era: "1181–1226", position: "\'The poor are our lords and masters\' — radical service to marginalized.", optionIndex: 0 },
        { saint: "St. Vincent de Paul", era: "1581–1660", position: "Formation of clergy: holy priests transform the Church.", optionIndex: 1 },
        { saint: "St. Philip Neri", era: "1515–1595", position: "Formation of clergy: holy priests transform the Church.", optionIndex: 1 },
        { saint: "St. Vincent de Paul", era: "1581–1660", position: "Simplicity, humility, meekness as core virtues.", optionIndex: 2 },
        { saint: "St. Francis of Assisi", era: "1181–1226", position: "Simplicity, humility, meekness as core virtues.", optionIndex: 2 },
        { saint: "St. Vincent de Paul", era: "1581–1660", position: "Practical charity: \'Love is inventive to infinity.\'", optionIndex: 3 },
        { saint: "St. John Paul II", era: "1920–2005", position: "Practical charity: \'Love is inventive to infinity.\'", optionIndex: 3 }
    ],
    75: [
        { saint: "St. Paul of the Cross", era: "1694–1775", position: "Central to Christian life: Meditating on the Passion transforms the soul and fuels preaching missions of conversion.", optionIndex: 0 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Central to Christian life: Meditating on the Passion transforms the soul and fuels preaching missions of conversion.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Important but must be balanced with Resurrection joy and hope — the Cross without Easter is incomplete.", optionIndex: 1 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Important but must be balanced with Resurrection joy and hope — the Cross without Easter is incomplete.", optionIndex: 1 },
        { saint: "St. Paul of the Cross", era: "1694–1775", position: "The memoria passionis connects us to the crucified peoples of today — solidarity with those who suffer now.", optionIndex: 2 },
        { saint: "St. Vincent de Paul", era: "1581–1660", position: "The memoria passionis connects us to the crucified peoples of today — solidarity with those who suffer now.", optionIndex: 2 },
        { saint: "St. Paul of the Cross", era: "1694–1775", position: "Reparation for sin through contemplation of the Passion is a powerful but demanding spiritual path.", optionIndex: 3 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Reparation for sin through contemplation of the Passion is a powerful but demanding spiritual path.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Can become morbid or masochistic. Better to focus on Christ\'s victory and the joy of the Resurrection.", optionIndex: 4 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Can become morbid or masochistic. Better to focus on Christ\'s victory and the joy of the Resurrection.", optionIndex: 4 }
    ],
    76: [
        { saint: "The Seven Holy Founders", era: "13th century", position: "Standing with Mary at Cross transforms suffering into redemption.", optionIndex: 0 },
        { saint: "St. Paul of the Cross", era: "1694–1775", position: "Standing with Mary at Cross transforms suffering into redemption.", optionIndex: 0 },
        { saint: "The Seven Holy Founders", era: "13th century", position: "Compassion (suffering-with) is central to Christian life.", optionIndex: 1 },
        { saint: "St. Vincent de Paul", era: "1581–1660", position: "Compassion (suffering-with) is central to Christian life.", optionIndex: 1 },
        { saint: "The Seven Holy Founders", era: "13th century", position: "Marian devotion leads to deeper union with Christ.", optionIndex: 2 },
        { saint: "St. Alphonsus Liguori", era: "1696–1787", position: "Marian devotion leads to deeper union with Christ.", optionIndex: 2 },
        { saint: "The Seven Holy Founders", era: "13th century", position: "Seven Sorrows are a school of discipleship.", optionIndex: 3 },
        { saint: "St. Paul of the Cross", era: "1694–1775", position: "Seven Sorrows are a school of discipleship.", optionIndex: 3 }
    ],
    77: [
        { saint: "St. Bruno of Cologne", era: "c. 1030–1101", position: "Highest Christian life: pure contemplation, hidden intercession.", optionIndex: 0 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Highest Christian life: pure contemplation, hidden intercession.", optionIndex: 0 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Valid but exceptional; active apostolate normative for most.", optionIndex: 1 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Valid but exceptional; active apostolate normative for most.", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Important witness, but Church needs engaged presence.", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Important witness, but Church needs engaged presence.", optionIndex: 2 },
        { saint: "St. Bruno of Cologne", era: "c. 1030–1101", position: "Desert tradition: \'flee, be silent, pray\' as perennial wisdom.", optionIndex: 3 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "Desert tradition: \'flee, be silent, pray\' as perennial wisdom.", optionIndex: 3 }
    ],
    78: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "A disaster that led to voluntarism, fideism, and ultimately secularism. (Thomist, Thomist (Realist))", optionIndex: 0 },
        { saint: "Étienne Gilson", era: "1884–1978", position: "A disaster that led to voluntarism, fideism, and ultimately secularism. (Thomist, Thomist (Realist))", optionIndex: 0 },
        { saint: "William of Ockham", era: "c. 1287–1347", position: "Contains genuine insights about parsimony and the limits of metaphysical speculation.", optionIndex: 1 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Contains genuine insights about parsimony and the limits of metaphysical speculation.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "An interesting historical episode with little relevance to contemporary theology.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "An interesting historical episode with little relevance to contemporary theology.", optionIndex: 2 },
        { saint: "William of Ockham", era: "c. 1287–1347", position: "Ockham was a faithful Catholic; his positions are defensible within tradition.", optionIndex: 3 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Ockham was a faithful Catholic; his positions are defensible within tradition.", optionIndex: 3 }
    ],
    79: [
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "The essence-energies distinction is true and essential: God\'s unknowable essence is distinguished from His participated uncreated energies, making theosis possible.", optionIndex: 0 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "The essence-energies distinction is true and essential: God\'s unknowable essence is distinguished from His participated uncreated energies, making theosis possible.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Possibly compatible with Thomism if properly understood. Worth serious ecumenical dialogue.", optionIndex: 1 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Incompatible with divine simplicity as understood in Western theology. The West rightly rejected it.", optionIndex: 2 },
        { saint: "Étienne Gilson", era: "1884–1978", position: "Incompatible with divine simplicity as understood in Western theology. The West rightly rejected it.", optionIndex: 2 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "A distinctly Eastern approach that enriches Catholic theology without replacing the Thomist framework. Both lungs can breathe.", optionIndex: 3 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "A distinctly Eastern approach that enriches Catholic theology without replacing the Thomist framework. Both lungs can breathe.", optionIndex: 3 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Scotist formal distinctions offer an orthodox Western interpretation: a real formal distinction in God between essence and operations, without Palamas\'s specific framework.", optionIndex: 4 },
        { saint: "Charles Sanders Peirce", era: "1839–1914", position: "Scotist formal distinctions offer an orthodox Western interpretation: a real formal distinction in God between essence and operations, without Palamas\'s specific framework.", optionIndex: 4 }
    ],
    80: [
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "Central - \'God became man that man might become God.\' This is the heart of soteriology.", optionIndex: 0 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "Central - \'God became man that man might become God.\' This is the heart of soteriology.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Important but must be balanced with juridical/forensic categories. Both-and, not either-or.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Important but must be balanced with juridical/forensic categories. Both-and, not either-or.", optionIndex: 1 },
        { saint: "Cardinal Alfredo Ottaviani", era: "1890–1979", position: "Western theology rightly emphasizes justification. Theosis language risks pantheism.", optionIndex: 2 },
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "Western theology rightly emphasizes justification. Theosis language risks pantheism.", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "A beautiful Eastern emphasis the West should recover through ressourcement.", optionIndex: 3 }
    ],
    81: [
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Hard integralism: State must formally recognize Church and suppress public heresy", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Hard integralism: State must formally recognize Church and suppress public heresy", optionIndex: 0 },
        { saint: "Thomas Pink", era: "Contemporary", position: "Soft integralism: State should favor true religion with prudential tolerance", optionIndex: 1 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Soft integralism: State should favor true religion with prudential tolerance", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Separation with cooperation: Distinct spheres cooperating for human flourishing", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Liberal Catholic: Religious liberty is a genuine right; separation protects both", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Liberal Catholic: Religious liberty is a genuine right; separation protects both", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Depends entirely on circumstances; no model universally normative", optionIndex: 4 }
    ],
    82: [
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Christ is King of nations; states should formally acknowledge this", optionIndex: 0 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Christ is King of nations; states should formally acknowledge this", optionIndex: 0 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Christ\'s kingship is primarily spiritual; political acknowledgment is optional", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Christ\'s kingship is primarily spiritual; political acknowledgment is optional", optionIndex: 1 },
        { saint: "Thomas Pink", era: "Contemporary", position: "Social kingship is real but expressed through culture more than law", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Social kingship is real but expressed through culture more than law", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Christ\'s kingdom is not of this world in a political sense", optionIndex: 3 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Christ\'s kingdom is not of this world in a political sense", optionIndex: 3 }
    ],
    83: [
        { saint: "G.K. Chesterton", era: "1874–1936", position: "Distributism: Wide property distribution; neither capitalism nor socialism", optionIndex: 0 },
        { saint: "Hilaire Belloc", era: "1870–1953", position: "Distributism: Wide property distribution; neither capitalism nor socialism", optionIndex: 0 },
        { saint: "Heinrich Pesch, S.J.", era: "1854–1926", position: "Corporatism/Solidarism: Vocational groups mediate between individual and state", optionIndex: 1 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Corporatism/Solidarism: Vocational groups mediate between individual and state", optionIndex: 1 },
        { saint: "Jacques Maritain", era: "1882–1973", position: "Social market economy: Free markets with strong social safety net and worker protections", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Social market economy: Free markets with strong social safety net and worker protections", optionIndex: 2 },
        { saint: "Michael Novak", era: "1933–2017", position: "Free market without cronyism: Competitive markets with strong regulation against rent-seeking, monopoly, and corporate welfare, ensuring affordable housing and energy", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Free market without cronyism: Competitive markets with strong regulation against rent-seeking, monopoly, and corporate welfare, ensuring affordable housing and energy", optionIndex: 3 },
        { saint: "Dorothy Day", era: "1897–1980", position: "Worker cooperatives and strong unions as primary vehicles for economic justice", optionIndex: 4 },
        { saint: "Jacques Maritain", era: "1882–1973", position: "Worker cooperatives and strong unions as primary vehicles for economic justice", optionIndex: 4 },
        { saint: "Hilaire Belloc", era: "1870–1953", position: "Catholic agrarianism: Return to the land and local economies", optionIndex: 5 },
        { saint: "G.K. Chesterton", era: "1874–1936", position: "Catholic agrarianism: Return to the land and local economies", optionIndex: 5 }
    ],
    84: [
        { saint: "Dorothy Day", era: "1897–1980", position: "Yes—employers must pay wages sufficient for dignified family support", optionIndex: 0 },
        { saint: "G.K. Chesterton", era: "1874–1936", position: "Yes—employers must pay wages sufficient for dignified family support", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "It\'s a strong moral ideal but circumstances may prevent it", optionIndex: 1 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "It\'s a strong moral ideal but circumstances may prevent it", optionIndex: 1 },
        { saint: "Michael Novak", era: "1933–2017", position: "Market wages are just if freely agreed; charity handles insufficiency", optionIndex: 2 },
        { saint: "Jacques Maritain", era: "1882–1973", position: "Yes, and the state should enforce it when employers fail", optionIndex: 3 },
        { saint: "Dorothy Day", era: "1897–1980", position: "Yes, and the state should enforce it when employers fail", optionIndex: 3 }
    ],
    85: [
        { saint: "Dorothy Day", era: "1897–1980", position: "Essential: Workers have a natural right to organize that must be respected", optionIndex: 0 },
        { saint: "G.K. Chesterton", era: "1874–1936", position: "Essential: Workers have a natural right to organize that must be respected", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Generally positive but can become corrupt or politically captured", optionIndex: 1 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Generally positive but can become corrupt or politically captured", optionIndex: 1 },
        { saint: "Michael Novak", era: "1933–2017", position: "Unnecessary in a truly free market; often harmful", optionIndex: 2 },
        { saint: "Heinrich Pesch, S.J.", era: "1854–1926", position: "Useful within a corporatist structure that includes all vocational groups", optionIndex: 3 }
    ],
    86: [
        { saint: "G.K. Chesterton", era: "1874–1936", position: "Wide distribution is essential; concentrated ownership is problematic", optionIndex: 0 },
        { saint: "Dorothy Day", era: "1897–1980", position: "Wide distribution is essential; concentrated ownership is problematic", optionIndex: 0 },
        { saint: "Michael Novak", era: "1933–2017", position: "Private property is a natural right with minimal restrictions", optionIndex: 1 },
        { saint: "Jacques Maritain", era: "1882–1973", position: "Property has a social mortgage; regulation for common good is justified", optionIndex: 2 },
        { saint: "Dorothy Day", era: "1897–1980", position: "Property has a social mortgage; regulation for common good is justified", optionIndex: 2 },
        { saint: "Heinrich Pesch, S.J.", era: "1854–1926", position: "Property should be organized through vocational/corporate bodies", optionIndex: 3 }
    ],
    87: [
        { saint: "Juan Donoso Cortés", era: "1809–1853", position: "Nations are natural communities willed by God; Catholicism should be inculturated nationally and borders defended.", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Nations are natural communities willed by God; Catholicism should be inculturated nationally and borders defended.", optionIndex: 0 },
        { saint: "Pope Francis", era: "1936–present", position: "The Church transcends nations; nationalism easily becomes idolatrous and must be subordinated to universal solidarity.", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The Church transcends nations; nationalism easily becomes idolatrous and must be subordinated to universal solidarity.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Moderate patriotism is healthy and natural, but always subordinate to Catholic identity and the common good.", optionIndex: 2 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Catholic integralism properly channels national identity: the state serves Christ\'s kingship within its particular cultural context.", optionIndex: 3 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Catholic integralism properly channels national identity: the state serves Christ\'s kingship within its particular cultural context.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "National identity is a cultural gift but must be purified by the Gospel; solidarity with immigrants and refugees takes priority.", optionIndex: 4 },
        { saint: "Dorothy Day", era: "1897–1980", position: "National identity is a cultural gift but must be purified by the Gospel; solidarity with immigrants and refugees takes priority.", optionIndex: 4 }
    ],
    88: [
        { saint: "Juan Donoso Cortés", era: "1809–1853", position: "Prioritize cultural and religious compatibility over economic factors", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Prioritize cultural and religious compatibility over economic factors", optionIndex: 0 },
        { saint: "Pope Francis", era: "1936–present", position: "Welcome the stranger as a Gospel imperative; borders are secondary", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Welcome the stranger as a Gospel imperative; borders are secondary", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Balance hospitality with legitimate concerns for common good", optionIndex: 2 },
        { saint: "G.K. Chesterton", era: "1874–1936", position: "Local communities should decide without centralized immigration policy", optionIndex: 3 },
        { saint: "Michael Novak", era: "1933–2017", position: "Local communities should decide without centralized immigration policy", optionIndex: 3 }
    ],
    89: [
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Yes, strongly—these institutions are hostile to natural law and faith", optionIndex: 0 },
        { saint: "Juan Donoso Cortés", era: "1809–1853", position: "Yes, strongly—these institutions are hostile to natural law and faith", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Engage critically but don\'t refuse all cooperation", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Support international cooperation for peace and human rights", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Support international cooperation for peace and human rights", optionIndex: 2 },
        { saint: "G.K. Chesterton", era: "1874–1936", position: "Focus on local and national levels; international institutions are secondary", optionIndex: 3 },
        { saint: "Juan Donoso Cortés", era: "1809–1853", position: "Focus on local and national levels; international institutions are secondary", optionIndex: 3 }
    ],
    90: [
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "A generational matter. Once older bishops retire, I\'m optimistic about better balance.", optionIndex: 0 },
        { saint: "Cardinal Walter Kasper", era: "1933–present", position: "A generational matter. Once older bishops retire, I\'m optimistic about better balance.", optionIndex: 0 },
        { saint: "Juan Donoso Cortés", era: "1809–1853", position: "Some nationalist governments have acted excessively, but prudential judgment on borders isn\'t sinful. National consciousness is legitimate.", optionIndex: 1 },
        { saint: "Thomas Pink", era: "Contemporary", position: "Some nationalist governments have acted excessively, but prudential judgment on borders isn\'t sinful. National consciousness is legitimate.", optionIndex: 1 },
        { saint: "Pope Francis", era: "1936–present", position: "A welcome prophetic stance against the pagan idols of nationalism and kinism.", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "A welcome prophetic stance against the pagan idols of nationalism and kinism.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Balanced - the clergy can be naive about practical realities, but their intentions are good.", optionIndex: 3 }
    ],
    91: [
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "A development allowing pastoral discernment in complex situations.", optionIndex: 0 },
        { saint: "Cardinal Walter Kasper", era: "1933–present", position: "A development allowing pastoral discernment in complex situations.", optionIndex: 0 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Ambiguous document misused by progressives. The dubia remain unanswered.", optionIndex: 1 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Ambiguous document misused by progressives. The dubia remain unanswered.", optionIndex: 1 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Heretical. Contradicts Familiaris Consortio and perennial teaching.", optionIndex: 2 },
        { saint: "Various Authors", era: "20th–21st c.", position: "Heretical. Contradicts Familiaris Consortio and perennial teaching.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Pastoral accompaniment is good but doesn\'t change the discipline.", optionIndex: 3 }
    ],
    92: [
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Scripture (as received in the Church) judges theology; systems must be revised to fit Scripture\'s full witness.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Dogma and metaphysics provide the framework that stabilizes interpretation; Scripture is read within that settled grammar. (Thomist, Thomist (Realist))", optionIndex: 1 },
        { saint: "Étienne Gilson", era: "1884–1978", position: "Dogma and metaphysics provide the framework that stabilizes interpretation; Scripture is read within that settled grammar. (Thomist, Thomist (Realist))", optionIndex: 1 },
        { saint: "Joseph de Maistre", era: "1753–1821", position: "The living Magisterium provides the proximate norm; speculative resolution is less important than obedience.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "The living Magisterium provides the proximate norm; speculative resolution is less important than obedience.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Multiple theologies can legitimately coexist; Scripture underdetermines systematic disputes.", optionIndex: 3 }
    ],
    93: [
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Can incur guilt through culpable omission: failure to pursue virtue and remedies becomes morally weighty.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Is a dangerous disposition, but guilt attaches only to present voluntary acts and consent. (Thomist, Thomist (Natural Law))", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Shows that the will is deeply bound; strict ascetic discipline and frequent confession are the safest path.", optionIndex: 2 },
        { saint: "Henry Davis, S.J.", era: "1866–1952", position: "Shows that the will is deeply bound; strict ascetic discipline and frequent confession are the safest path.", optionIndex: 2 },
        { saint: "St. John Paul II", era: "1920–2005", position: "The Church should avoid scrupulosity: focus on healing and gradual growth.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The Church should avoid scrupulosity: focus on healing and gradual growth.", optionIndex: 3 }
    ],
    94: [
        { saint: "Henry Davis, S.J.", era: "1866–1952", position: "Satisfaction and purification from temporal punishment due to sin.", optionIndex: 0 },
        { saint: "Cardinal Alfredo Ottaviani", era: "1890–1979", position: "Satisfaction and purification from temporal punishment due to sin.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Final purification of love: removal of attachments so the soul can see God.", optionIndex: 1 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Final purification of love: removal of attachments so the soul can see God.", optionIndex: 1 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "An encounter with divine fire that heals and illumines (Eastern-leaning emphasis).", optionIndex: 2 },
        { saint: "St. John Chrysostom", era: "c. 349–407", position: "An encounter with divine fire that heals and illumines (Eastern-leaning emphasis).", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "A symbol pointing to God\'s mercy; details shouldn\'t be systematized.", optionIndex: 3 },
        { saint: "St. John Paul II", era: "1920–2005", position: "A symbol pointing to God\'s mercy; details shouldn\'t be systematized.", optionIndex: 3 }
    ],
    95: [
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Clarifying and defending settled doctrine with precision (often scholastic).", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Clarifying and defending settled doctrine with precision (often scholastic).", optionIndex: 0 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Retrieving the Fathers and liturgical tradition to renew theology (ressourcement).", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Mediating doctrine pastorally for modern contexts while preserving essentials.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Testing boundaries and developing new paradigms to meet contemporary needs.", optionIndex: 3 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Testing boundaries and developing new paradigms to meet contemporary needs.", optionIndex: 3 }
    ],
    96: [
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Fallen humans can do natural goods but absolutely cannot move toward salvation without prevenient grace", optionIndex: 0 },
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "Fallen humans can do natural goods but absolutely cannot move toward salvation without prevenient grace", optionIndex: 0 },
        { saint: "St. Francis de Sales", era: "1567–1622", position: "Fallen humans retain significant natural capacity; grace assists but doesn\'t wholly initiate", optionIndex: 1 },
        { saint: "Luis de Molina, S.J.", era: "1535–1600", position: "Fallen humans retain significant natural capacity; grace assists but doesn\'t wholly initiate", optionIndex: 1 },
        { saint: "John Calvin", era: "1509–1564", position: "Human nature is so corrupted that even natural goods are tainted without grace", optionIndex: 2 },
        { saint: "Martin Luther", era: "1483–1546", position: "Human nature is so corrupted that even natural goods are tainted without grace", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Grace and nature cooperate from the start; the distinction is somewhat artificial", optionIndex: 3 }
    ],
    97: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Intellectualist: God wills things because they are good; goodness is prior to willing. The divine intellect apprehends the good, and the will necessarily follows.", optionIndex: 0 },
        { saint: "William of Ockham", era: "c. 1287–1347", position: "Radical Voluntarist: Things are good solely because God wills them; divine will alone is the arbitrary source of all moral order.", optionIndex: 1 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Radical Voluntarist: Things are good solely because God wills them; divine will alone is the arbitrary source of all moral order.", optionIndex: 1 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Moderate Voluntarism: God\'s will is formally primary and free, but always acts according to wisdom and the divine nature—never arbitrarily.", optionIndex: 2 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "Moderate Voluntarism: God\'s will is formally primary and free, but always acts according to wisdom and the divine nature—never arbitrarily.", optionIndex: 2 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "The distinction is artificial; will and intellect are identical in God and mutually implicate each other in the divine simplicity.", optionIndex: 3 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "The distinction is artificial; will and intellect are identical in God and mutually implicate each other in the divine simplicity.", optionIndex: 3 }
    ],
    98: [
        { saint: "William of Ockham", era: "c. 1287–1347", position: "Radical divine command—things are good/evil solely because God wills them so; there is no independent rational order prior to the divine decree.", optionIndex: 0 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Radical divine command—things are good/evil solely because God wills them so; there is no independent rational order prior to the divine decree.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "The nature of things known by reason—God wills them because they are good. Natural law is grounded in eternal reason, not arbitrary will.", optionIndex: 1 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "God\'s will freely establishes the moral order, but this will is always guided by wisdom and the divine nature, never arbitrary or irrational.", optionIndex: 2 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "God\'s will freely establishes the moral order, but this will is always guided by wisdom and the divine nature, never arbitrary or irrational.", optionIndex: 2 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Participation in eternal law, which is both rational and willed—the law written on our hearts reflects both divine wisdom and divine decree.", optionIndex: 3 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "Participation in eternal law, which is both rational and willed—the law written on our hearts reflects both divine wisdom and divine decree.", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "A combination: God\'s will establishes positive/ceremonial law, but natural law reflects the rational order of creation.", optionIndex: 4 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "A combination: God\'s will establishes positive/ceremonial law, but natural law reflects the rational order of creation.", optionIndex: 4 }
    ],
    99: [
        { saint: "Joseph de Maistre", era: "1753–1821", position: "Essentially as today—with Roman primacy and centralized authority", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Essentially as today—with Roman primacy and centralized authority", optionIndex: 0 },
        { saint: "Cardinal Walter Kasper", era: "1933–present", position: "More synodally and collegially, with Roman primacy developing over time", optionIndex: 1 },
        { saint: "Jean Gerson", era: "1363–1429", position: "More synodally and collegially, with Roman primacy developing over time", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "With real Roman primacy but more subsidiarity than later periods", optionIndex: 2 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "As a communion of local churches with Rome as first among equals", optionIndex: 3 },
        { saint: "Cardinal Walter Kasper", era: "1933–present", position: "As a communion of local churches with Rome as first among equals", optionIndex: 3 }
    ],
    100: [
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Yes, absolutely—this is the perennial teaching of the Church", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Yes, absolutely—this is the perennial teaching of the Church", optionIndex: 0 },
        { saint: "Thomas Pink", era: "Contemporary", position: "In principle yes, but rarely prudent in modern pluralist societies", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "In principle yes, but rarely prudent in modern pluralist societies", optionIndex: 1 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "No—Dignitatis Humanae represents genuine doctrinal development", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "No—Dignitatis Humanae represents genuine doctrinal development", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "The question is more complex than a simple yes/no", optionIndex: 3 }
    ],
    101: [
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Contemplative prayer: Simple loving gaze upon God", optionIndex: 0 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "Contemplative prayer: Simple loving gaze upon God", optionIndex: 0 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "The Holy Sacrifice of the Mass", optionIndex: 1 },
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "The Holy Sacrifice of the Mass", optionIndex: 1 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Liturgy of the Hours as the Church\'s official prayer", optionIndex: 2 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Liturgy of the Hours as the Church\'s official prayer", optionIndex: 2 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Lectio Divina: Prayerful reading of Scripture", optionIndex: 3 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Lectio Divina: Prayerful reading of Scripture", optionIndex: 3 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Ignatian meditation with imagination and application of senses", optionIndex: 4 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "All are valid paths suited to different vocations", optionIndex: 5 }
    ],
    102: [
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Extraordinary graces given to some; not to be sought but accepted", optionIndex: 0 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Extraordinary graces given to some; not to be sought but accepted", optionIndex: 0 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "The normal flowering of the life of grace available to all who persevere", optionIndex: 1 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "The normal flowering of the life of grace available to all who persevere", optionIndex: 1 },
        { saint: "Henry Davis, S.J.", era: "1866–1952", position: "Suspect: Focus on ordinary virtue and sacraments instead", optionIndex: 2 },
        { saint: "Cardinal Alfredo Ottaviani", era: "1890–1979", position: "Suspect: Focus on ordinary virtue and sacraments instead", optionIndex: 2 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "Central to Eastern spirituality: Theosis/deification is the goal", optionIndex: 3 },
        { saint: "St. John Chrysostom", era: "c. 349–407", position: "Central to Eastern spirituality: Theosis/deification is the goal", optionIndex: 3 }
    ],
    103: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Weekly or at least fortnightly, even without mortal sin", optionIndex: 0 },
        { saint: "St. Josemaría Escrivá", era: "1902–1975", position: "Weekly or at least fortnightly, even without mortal sin", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Monthly for devotional confession; more often if in mortal sin", optionIndex: 1 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Monthly for devotional confession; more often if in mortal sin", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Whenever conscious of serious sin; otherwise a few times a year", optionIndex: 2 },
        { saint: "St. John Chrysostom", era: "c. 349–407", position: "The Eastern tradition emphasizes spiritual direction over frequent confession", optionIndex: 3 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "The Eastern tradition emphasizes spiritual direction over frequent confession", optionIndex: 3 }
    ],
    104: [
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Primarily to redeem from sin; without Fall, no Incarnation.", optionIndex: 0 },
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Primarily to redeem from sin; without Fall, no Incarnation.", optionIndex: 0 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "Christ would have come even without sin; Incarnation is creation\'s crown.", optionIndex: 1 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "Christ would have come even without sin; Incarnation is creation\'s crown.", optionIndex: 1 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "Both redemption and divinization: save from sin AND unite to God in theosis.", optionIndex: 2 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "Both redemption and divinization: save from sin AND unite to God in theosis.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "The question is speculative; focus on actual economy revealed.", optionIndex: 3 }
    ],
    105: [
        { saint: "St. Bernard of Clairvaux", era: "1090–1153", position: "Strict silence and solitude as essential for encountering God.", optionIndex: 0 },
        { saint: "St. Bruno of Cologne", era: "c. 1030–1101", position: "Strict silence and solitude as essential for encountering God.", optionIndex: 0 },
        { saint: "St. Bernard of Clairvaux", era: "1090–1153", position: "Manual labor as prayer: working with hands sanctifies.", optionIndex: 1 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Manual labor as prayer: working with hands sanctifies.", optionIndex: 1 },
        { saint: "St. Bernard of Clairvaux", era: "1090–1153", position: "Simplicity and austerity: stripping away to find essential.", optionIndex: 2 },
        { saint: "St. Bruno of Cologne", era: "c. 1030–1101", position: "Simplicity and austerity: stripping away to find essential.", optionIndex: 2 },
        { saint: "St. Bernard of Clairvaux", era: "1090–1153", position: "Liturgical beauty in pure, unadorned Benedictine form.", optionIndex: 3 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Liturgical beauty in pure, unadorned Benedictine form.", optionIndex: 3 }
    ],
    106: [
        { saint: "Hilaire Belloc", era: "1870–1953", position: "Land-based life forms virtue uniquely; prefer smallholdings.", optionIndex: 0 },
        { saint: "G.K. Chesterton", era: "1874–1936", position: "Land-based life forms virtue uniquely; prefer smallholdings.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Has value but industrialization not inherently evil.", optionIndex: 1 },
        { saint: "Jacques Maritain", era: "1882–1973", position: "Has value but industrialization not inherently evil.", optionIndex: 1 },
        { saint: "Dorothy Day", era: "1897–1980", position: "Romantic nostalgia; address actual worker conditions.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Romantic nostalgia; address actual worker conditions.", optionIndex: 2 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Rural parishes preserve faith; special concern for farmers.", optionIndex: 3 },
        { saint: "Hilaire Belloc", era: "1870–1953", position: "Rural parishes preserve faith; special concern for farmers.", optionIndex: 3 }
    ],
    107: [
        { saint: "Joseph de Maistre", era: "1753–1821", position: "Return to Rome under papal authority as Vatican I defined. No compromises on primacy.", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Return to Rome under papal authority as Vatican I defined. No compromises on primacy.", optionIndex: 0 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "A \'Sister Churches\' model with restored communion but preserved Eastern autonomy.", optionIndex: 1 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "A \'Sister Churches\' model with restored communion but preserved Eastern autonomy.", optionIndex: 1 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Focus on resolving theological issues (Filioque, essence-energies) before structural questions.", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Focus on resolving theological issues (Filioque, essence-energies) before structural questions.", optionIndex: 2 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Ecumenism has gone too far. Maintain clear boundaries until they accept all Catholic dogma.", optionIndex: 3 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Ecumenism has gone too far. Maintain clear boundaries until they accept all Catholic dogma.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Practical cooperation first; doctrinal unity will follow organically.", optionIndex: 4 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Practical cooperation first; doctrinal unity will follow organically.", optionIndex: 4 }
    ],
    108: [
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Legitimate development - the state shouldn\'t coerce conscience, though truth remains objective.", optionIndex: 0 },
        { saint: "Thomas Pink", era: "Contemporary", position: "A prudential adaptation for pluralist societies, not reversal of prior teaching.", optionIndex: 1 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "A prudential adaptation for pluralist societies, not reversal of prior teaching.", optionIndex: 1 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "A rupture with Tradition. Quanta Cura condemned exactly what DH teaches.", optionIndex: 2 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "A rupture with Tradition. Quanta Cura condemned exactly what DH teaches.", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "The Church finally embraced freedom of conscience as foundational to human dignity.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The Church finally embraced freedom of conscience as foundational to human dignity.", optionIndex: 3 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Ambiguously worded; needs authoritative clarification to reconcile with prior magisterium.", optionIndex: 4 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Ambiguously worded; needs authoritative clarification to reconcile with prior magisterium.", optionIndex: 4 }
    ],
    109: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Precious discipline that should never be relaxed. Frees priests for total dedication.", optionIndex: 0 },
        { saint: "St. Josemaría Escrivá", era: "1902–1975", position: "Precious discipline that should never be relaxed. Frees priests for total dedication.", optionIndex: 0 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "Valuable but could permit married priests in mission territories, as Eastern Catholics do.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Valuable but could permit married priests in mission territories, as Eastern Catholics do.", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Should be entirely optional. Many good men are lost; the Apostles were married.", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Should be entirely optional. Many good men are lost; the Apostles were married.", optionIndex: 2 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Essential for eschatological witness. It images heavenly life.", optionIndex: 3 },
        { saint: "St. Bruno of Cologne", era: "c. 1030–1101", position: "Essential for eschatological witness. It images heavenly life.", optionIndex: 3 },
        { saint: "Msgr. Jeffrey Steenson", era: "1952–present", position: "The Ordinariate exception shows flexibility is possible. Expand it carefully.", optionIndex: 4 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "The Ordinariate exception shows flexibility is possible. Expand it carefully.", optionIndex: 4 }
    ],
    110: [
        { saint: "George Lindbeck", era: "1923–2018", position: "No - properly understood, these need not be impediments. JDDJ showed real convergence.", optionIndex: 0 },
        { saint: "Louis Bouyer", era: "1913–2004", position: "No - properly understood, these need not be impediments. JDDJ showed real convergence.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Possibly not, but we\'d still need agreement on papacy, Marian dogmas, purgatory.", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Yes - Lutheran theology is fundamentally incompatible. Trent\'s condemnations stand.", optionIndex: 2 },
        { saint: "Cardinal Alfredo Ottaviani", era: "1890–1979", position: "Yes - Lutheran theology is fundamentally incompatible. Trent\'s condemnations stand.", optionIndex: 2 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "This hypothetical concedes too much. Lutheranism doesn\'t actually affirm these things.", optionIndex: 3 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "This hypothetical concedes too much. Lutheranism doesn\'t actually affirm these things.", optionIndex: 3 }
    ],
    111: [
        { saint: "St. John Bosco", era: "1815–1888", position: "Embrace fully. Social media is the new Areopagus. Memes and podcasts reach millions.", optionIndex: 0 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Embrace fully. Social media is the new Areopagus. Memes and podcasts reach millions.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Cautiously useful, but nothing replaces parish life and sacramental encounter.", optionIndex: 1 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Cautiously useful, but nothing replaces parish life and sacramental encounter.", optionIndex: 1 },
        { saint: "St. Bruno of Cologne", era: "c. 1030–1101", position: "Dangerous - breeds pride and controversy-seeking. Focus on real community.", optionIndex: 2 },
        { saint: "St. Bernard of Clairvaux", era: "1090–1153", position: "Dangerous - breeds pride and controversy-seeking. Focus on real community.", optionIndex: 2 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Essential for reaching the young, but must be done with theological competence.", optionIndex: 3 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Essential for reaching the young, but must be done with theological competence.", optionIndex: 3 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Lay apostolates online have revived tradition more than the hierarchy. Keep going.", optionIndex: 4 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Lay apostolates online have revived tradition more than the hierarchy. Keep going.", optionIndex: 4 }
    ],
    112: [
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Female deacons should be restored; women should lead wherever ordination isn\'t required.", optionIndex: 0 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Female deacons should be restored; women should lead wherever ordination isn\'t required.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Women already have vital roles. Recognize existing contributions, don\'t invent offices.", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "The push reflects secular feminism infiltrating the Church. Resist it.", optionIndex: 2 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "The push reflects secular feminism infiltrating the Church. Resist it.", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Study historical evidence for deaconesses carefully; proceed with tradition.", optionIndex: 3 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "Study historical evidence for deaconesses carefully; proceed with tradition.", optionIndex: 3 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Religious sisters already exercise profound spiritual authority. This is the feminine genius.", optionIndex: 4 },
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "Religious sisters already exercise profound spiritual authority. This is the feminine genius.", optionIndex: 4 }
    ],
    113: [
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The Old Covenant remains valid. Jews have a unique path not requiring explicit Christian faith.", optionIndex: 0 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "The Old Covenant remains valid. Jews have a unique path not requiring explicit Christian faith.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Nostra Aetate condemned antisemitism but didn\'t change the necessity of Christ for salvation.", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "The Church has overcorrected. Supersessionism is traditional and shouldn\'t be abandoned.", optionIndex: 2 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "The Church has overcorrected. Supersessionism is traditional and shouldn\'t be abandoned.", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Complex - honor Jewish roots, condemn antisemitism, maintain missionary mandate to all.", optionIndex: 3 }
    ],
    114: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Essential to Catholic piety. The Fatima consecration should be taken seriously.", optionIndex: 0 },
        { saint: "St. Alphonsus Liguori", era: "1696–1787", position: "Essential to Catholic piety. The Fatima consecration should be taken seriously.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Approved apparitions are credible but private revelation is never obligatory.", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Often verge on superstition. Focus on Scripture and Sacraments.", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Often verge on superstition. Focus on Scripture and Sacraments.", optionIndex: 2 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Some are solid (Fatima, Lourdes) but others (Medjugorje) are likely fraudulent.", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Some are solid (Fatima, Lourdes) but others (Medjugorje) are likely fraudulent.", optionIndex: 3 }
    ],
    115: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Mary truly cooperated in our redemption in a unique and subordinate manner; the titles \'Mediatrix of All Graces\' and \'Co-redemptrix\' should be solemnly defined to crown Catholic...", optionIndex: 0 },
        { saint: "St. Alphonsus Liguori", era: "1696–1787", position: "Mary truly cooperated in our redemption in a unique and subordinate manner; the titles \'Mediatrix of All Graces\' and \'Co-redemptrix\' should be solemnly defined to crown Catholic...", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "These titles, while capable of orthodox interpretation, risk serious misunderstanding and ecumenical harm; the Church should refrain from dogmatic definition while permitting pr...", optionIndex: 1 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Mary is best understood as the \'Archetype\' or \'Type\' of the Church—the first and most perfect disciple who models receptivity to grace. Maximalist titles obscure this ecclesioty...", optionIndex: 2 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "The East venerates the Theotokos as \'more honorable than the Cherubim\' and prays \'through her intercessions, save us,\' but without the juridical Latin categories of \'mediatrix\' ...", optionIndex: 3 },
        { saint: "St. Gregory Palamas", era: "1296–1359", position: "The East venerates the Theotokos as \'more honorable than the Cherubim\' and prays \'through her intercessions, save us,\' but without the juridical Latin categories of \'mediatrix\' ...", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Marian titles beyond \'Mother of God\' risk detracting from Christ\'s unique mediation (1 Tim 2:5); the Church should adopt a more Christocentric and scripturally restrained Mariol...", optionIndex: 4 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Marian titles beyond \'Mother of God\' risk detracting from Christ\'s unique mediation (1 Tim 2:5); the Church should adopt a more Christocentric and scripturally restrained Mariol...", optionIndex: 4 }
    ],
    116: [
        { saint: "St. Benedict of Nursia", era: "c. 480–547", position: "The solemn Marian antiphons of the Divine Office—Salve Regina, Alma Redemptoris Mater, Ave Regina Caelorum, Regina Caeli—represent the Church\'s most sublime and doctrinally prec...", optionIndex: 0 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "The solemn Marian antiphons of the Divine Office—Salve Regina, Alma Redemptoris Mater, Ave Regina Caelorum, Regina Caeli—represent the Church\'s most sublime and doctrinally prec...", optionIndex: 0 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "The Holy Rosary, particularly the traditional fifteen mysteries contemplated daily, remains the pre-eminent Marian devotion for the faithful and the surest path to Marian consec...", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "The Holy Rosary, particularly the traditional fifteen mysteries contemplated daily, remains the pre-eminent Marian devotion for the faithful and the surest path to Marian consec...", optionIndex: 1 },
        { saint: "Alexander Schmemann", era: "1921–1983", position: "The Byzantine Akathist Hymn and the rich Eastern Marian troparia preserve the Christological and patristic balance that some Western devotions—particularly post-Tridentine maxim...", optionIndex: 2 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "The Byzantine Akathist Hymn and the rich Eastern Marian troparia preserve the Christological and patristic balance that some Western devotions—particularly post-Tridentine maxim...", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Marian devotion today should emphasize Mary as the first disciple, model of faith, and icon of the pilgrim Church—expressed through contemporary hymnody, inclusive language, and...", optionIndex: 3 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Marian devotion today should emphasize Mary as the first disciple, model of faith, and icon of the pilgrim Church—expressed through contemporary hymnody, inclusive language, and...", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "All authentic forms of Marian devotion—whether Office antiphons, Rosary, Scapular, Akathist, or contemporary hymns—are valuable when they lead souls to Christ; no single form sh...", optionIndex: 4 }
    ],
    117: [
        { saint: "Joseph Ratzinger", era: "1927–2022", position: "Permissible - we may dare to hope all are saved. God\'s mercy is infinite.", optionIndex: 0 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Permissible - we may dare to hope all are saved. God\'s mercy is infinite.", optionIndex: 0 },
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "Heretical or temerarious. Scripture and Tradition attest many are damned.", optionIndex: 1 },
        { saint: "Blaise Pascal", era: "1623–1662", position: "Heretical or temerarious. Scripture and Tradition attest many are damned.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "We can hope for individuals but the Church teaches hell is populated.", optionIndex: 2 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "We can hope for individuals but the Church teaches hell is populated.", optionIndex: 2 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Speculative. Focus on your own salvation, not universal questions.", optionIndex: 3 },
        { saint: "St. Bruno of Cologne", era: "c. 1030–1101", position: "Speculative. Focus on your own salvation, not universal questions.", optionIndex: 3 }
    ],
    118: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Prophetic and absolutely binding. NFP is the only moral option.", optionIndex: 0 },
        { saint: "Cardinal Alfredo Ottaviani", era: "1890–1979", position: "Prophetic and absolutely binding. NFP is the only moral option.", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "True but pastoral sensitivity needed. Distinguish grave matter from mortal sin.", optionIndex: 1 },
        { saint: "St. John Paul II", era: "1920–2005", position: "The principle is right but application involves prudential judgment.", optionIndex: 2 },
        { saint: "St. Alphonsus Liguori", era: "1696–1787", position: "The principle is right but application involves prudential judgment.", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Should be reconsidered. Sensus fidelium has rejected it.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Should be reconsidered. Sensus fidelium has rejected it.", optionIndex: 3 }
    ],
    119: [
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Interior prayer and mystical union - the soul\'s journey through mansions to divine marriage.", optionIndex: 0 },
        { saint: "St. John of the Cross", era: "1542–1591", position: "Interior prayer and mystical union - the soul\'s journey through mansions to divine marriage.", optionIndex: 0 },
        { saint: "St. Ignatius of Loyola", era: "1491–1556", position: "Valuable for contemplatives but most Catholics need active, engaged spirituality.", optionIndex: 1 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Valuable for contemplatives but most Catholics need active, engaged spirituality.", optionIndex: 1 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "The \'dark night\' teaches detachment from consolations - demanding but transformative.", optionIndex: 2 },
        { saint: "St. Bernard of Clairvaux", era: "1090–1153", position: "The \'dark night\' teaches detachment from consolations - demanding but transformative.", optionIndex: 2 },
        { saint: "Cardinal Alfredo Ottaviani", era: "1890–1979", position: "Mysticism is dangerous without strong doctrinal grounding and ecclesial oversight.", optionIndex: 3 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Mysticism is dangerous without strong doctrinal grounding and ecclesial oversight.", optionIndex: 3 }
    ],
    120: [
        { saint: "St. Peter Nolasco", era: "c. 1189–1256", position: "Heroic charity. The willingness to die for another\'s freedom is profoundly Christlike.", optionIndex: 0 },
        { saint: "St. Vincent de Paul", era: "1581–1660", position: "Heroic charity. The willingness to die for another\'s freedom is profoundly Christlike.", optionIndex: 0 },
        { saint: "St. Peter Nolasco", era: "c. 1189–1256", position: "A noble historical charism that should be adapted for modern forms of captivity (trafficking, addiction).", optionIndex: 1 },
        { saint: "St. Vincent de Paul", era: "1581–1660", position: "A noble historical charism that should be adapted for modern forms of captivity (trafficking, addiction).", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Inspiring but exceptional. Most are not called to such radical sacrifice.", optionIndex: 2 },
        { saint: "St. Bruno of Cologne", era: "c. 1030–1101", position: "All religious should have this spirit of total self-gift, even if not vowed.", optionIndex: 3 },
        { saint: "St. Bernard of Clairvaux", era: "1090–1153", position: "All religious should have this spirit of total self-gift, even if not vowed.", optionIndex: 3 }
    ],
    121: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Resist: Modern culture is largely hostile to faith and natural law", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Resist: Modern culture is largely hostile to faith and natural law", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Engage critically: Affirm what is good, reject what contradicts faith", optionIndex: 1 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Engage critically: Affirm what is good, reject what contradicts faith", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Adapt: The Church must speak modern language to be heard", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Adapt: The Church must speak modern language to be heard", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Ressourcement: Return to sources to address modern questions freshly", optionIndex: 3 }
    ],
    122: [
        { saint: "Étienne Gilson", era: "1884–1978", position: "Perennially valid: Thomistic philosophy and theology remain normative", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Perennially valid: Thomistic philosophy and theology remain normative", optionIndex: 0 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Valuable but not exclusively: Other traditions have insights", optionIndex: 1 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Valuable but not exclusively: Other traditions have insights", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Historically important but modern thought has surpassed it", optionIndex: 2 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "Historically important but modern thought has surpassed it", optionIndex: 2 },
        { saint: "Bl. John Duns Scotus", era: "c. 1266–1308", position: "One approach among many; Scotist, Augustinian alternatives are equally valid", optionIndex: 3 },
        { saint: "St. Bonaventure", era: "1221–1274", position: "One approach among many; Scotist, Augustinian alternatives are equally valid", optionIndex: 3 }
    ],
    123: [
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "A virtual consensus of the Fathers, Doctors, and saints. Our Lord\'s words \'narrow is the gate\' should be taken at face value.", optionIndex: 0 },
        { saint: "Blaise Pascal", era: "1623–1662", position: "A virtual consensus of the Fathers, Doctors, and saints. Our Lord\'s words \'narrow is the gate\' should be taken at face value.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Most are likely lost through their own fault, but the elect may be more numerous and surprising in composition than some expect. Garrigou-Lagrange held this nuanced view.", optionIndex: 1 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Most are likely lost through their own fault, but the elect may be more numerous and surprising in composition than some expect. Garrigou-Lagrange held this nuanced view.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "We may hope that a significant portion of practicing Christians receive the grace of final perseverance, though certainty eludes us.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The question reflects an overly pessimistic spirituality. God\'s salvific will is universal and His mercy should inspire confidence, not fear.", optionIndex: 3 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "The question reflects an overly pessimistic spirituality. God\'s salvific will is universal and His mercy should inspire confidence, not fear.", optionIndex: 3 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Speculative questions about numbers distract from the call to personal holiness. Work out your own salvation with fear and trembling.", optionIndex: 4 },
        { saint: "St. Bruno of Cologne", era: "c. 1030–1101", position: "Speculative questions about numbers distract from the call to personal holiness. Work out your own salvation with fear and trembling.", optionIndex: 4 }
    ],
    124: [
        { saint: "Various Authors", era: "20th–21st c.", position: "Strictly: Only those validly baptized who die within the visible bounds of the Roman Catholic Church can be saved. No exceptions.", optionIndex: 0 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Strictly: Only those validly baptized who die within the visible bounds of the Roman Catholic Church can be saved. No exceptions.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "The Church is the ordinary and normative means of salvation, but invincible ignorance and baptism of desire are genuine possibilities recognized by Tradition.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "The Church is the ordinary and normative means of salvation, but invincible ignorance and baptism of desire are genuine possibilities recognized by Tradition.", optionIndex: 1 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Separated Christians have real though imperfect communion; their obligation is to seek truth, but diminished culpability is possible.", optionIndex: 2 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Separated Christians have real though imperfect communion; their obligation is to seek truth, but diminished culpability is possible.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "All who die in the state of grace are saved, however they came to it. The Church\'s boundaries are more mysterious than juridical.", optionIndex: 3 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "All who die in the state of grace are saved, however they came to it. The Church\'s boundaries are more mysterious than juridical.", optionIndex: 3 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "Those with valid sacraments (Eastern Orthodox, some Anglicans) are in a different category than Protestant communities without valid orders.", optionIndex: 4 },
        { saint: "Metropolitan Andrey Sheptytsky", era: "1865–1944", position: "Those with valid sacraments (Eastern Orthodox, some Anglicans) are in a different category than Protestant communities without valid orders.", optionIndex: 4 }
    ],
    125: [
        { saint: "St. Charles Borromeo", era: "1538–1584", position: "Fully canonical Scripture, equal in authority to all other biblical books.", optionIndex: 0 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Fully canonical Scripture, equal in authority to all other biblical books.", optionIndex: 0 },
        { saint: "John Calvin", era: "1509–1564", position: "Valuable for edification but not for establishing doctrine (apocrypha).", optionIndex: 1 },
        { saint: "Martin Luther", era: "1483–1546", position: "Valuable for edification but not for establishing doctrine (apocrypha).", optionIndex: 1 },
        { saint: "Thomas Cranmer", era: "1489–1556", position: "Deuterocanonical: secondary canon, useful and often read liturgically.", optionIndex: 2 },
        { saint: "John Wesley", era: "1703–1791", position: "Deuterocanonical: secondary canon, useful and often read liturgically.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The question of the canon should be approached with more nuance than rigid categories.", optionIndex: 3 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "The question of the canon should be approached with more nuance than rigid categories.", optionIndex: 3 }
    ],
    126: [
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Twenty-one, from Nicaea I (325) to Vatican II (1962-65).", optionIndex: 0 },
        { saint: "Joseph de Maistre", era: "1753–1821", position: "Twenty-one, from Nicaea I (325) to Vatican II (1962-65).", optionIndex: 0 },
        { saint: "St. Photios the Great", era: "c. 810–893", position: "Seven, from Nicaea I to Nicaea II (787); later councils are Western synods.", optionIndex: 1 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "Seven, from Nicaea I to Nicaea II (787); later councils are Western synods.", optionIndex: 1 },
        { saint: "St. Cyril of Alexandria", era: "c. 376–444", position: "Three, through Ephesus (431); Chalcedon introduced divisive innovations.", optionIndex: 2 },
        { saint: "St. Athanasius", era: "c. 296–373", position: "Three, through Ephesus (431); Chalcedon introduced divisive innovations.", optionIndex: 2 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "The number is less important than continuity with apostolic tradition.", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "The number is less important than continuity with apostolic tradition.", optionIndex: 3 }
    ],
    127: [
        { saint: "St. Augustine of Hippo", era: "354–430", position: "Inherited guilt and corruption: all humanity sinned \'in Adam\' and inherits both guilt and concupiscence.", optionIndex: 0 },
        { saint: "Blaise Pascal", era: "1623–1662", position: "Inherited guilt and corruption: all humanity sinned \'in Adam\' and inherits both guilt and concupiscence.", optionIndex: 0 },
        { saint: "St. Photios the Great", era: "c. 810–893", position: "Inherited mortality and corruption but not personal guilt; we sin because we are mortal.", optionIndex: 1 },
        { saint: "Sergei Bulgakov", era: "1871–1944", position: "Inherited mortality and corruption but not personal guilt; we sin because we are mortal.", optionIndex: 1 },
        { saint: "St. Thomas Aquinas", era: "1225–1274", position: "Original sin is primarily privation: loss of original justice and sanctifying grace.", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Original sin is primarily privation: loss of original justice and sanctifying grace.", optionIndex: 2 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "The doctrine needs restatement: evolutionary science changes how we understand human origins.", optionIndex: 3 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "The doctrine needs restatement: evolutionary science changes how we understand human origins.", optionIndex: 3 }
    ],
    128: [
        { saint: "Blaise Pascal", era: "1623–1662", position: "Blaise Pascal - defender of Augustinian grace against Jesuit laxism.", optionIndex: 0 },
        { saint: "Prosper of Aquitaine", era: "c. 390–455", position: "Blaise Pascal - defender of Augustinian grace against Jesuit laxism.", optionIndex: 0 },
        { saint: "Reginald Garrigou-Lagrange, O.P.", era: "1877–1964", position: "Réginald Garrigou-Lagrange, O.P. - champion of strict Thomism and spiritual master.", optionIndex: 1 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Réginald Garrigou-Lagrange, O.P. - champion of strict Thomism and spiritual master.", optionIndex: 1 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "Meister Eckhart, O.P. - profound mystic whose condemnation was perhaps too hasty.", optionIndex: 2 },
        { saint: "St. Dominic de Guzmán", era: "1170–1221", position: "Meister Eckhart, O.P. - profound mystic whose condemnation was perhaps too hasty.", optionIndex: 2 },
        { saint: "Pseudo-Dionysius", era: "c. 5th–6th century", position: "Marsilio Ficino - Christian Platonist who harmonized faith and ancient wisdom.", optionIndex: 3 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Marsilio Ficino - Christian Platonist who harmonized faith and ancient wisdom.", optionIndex: 3 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Antonio Rosmini - philosopher vindicated after long suspicion, model of patient orthodoxy.", optionIndex: 4 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Antonio Rosmini - philosopher vindicated after long suspicion, model of patient orthodoxy.", optionIndex: 4 },
        { saint: "Henri de Lubac, S.J.", era: "1896–1991", position: "Henri de Lubac, S.J. - ressourcement giant who suffered and was vindicated.", optionIndex: 5 },
        { saint: "Joseph Ratzinger", era: "1927–2022", position: "Henri de Lubac, S.J. - ressourcement giant who suffered and was vindicated.", optionIndex: 5 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Archbishop Marcel Lefebvre - defender of Tradition against modernist corruption.", optionIndex: 6 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Archbishop Marcel Lefebvre - defender of Tradition against modernist corruption.", optionIndex: 6 },
        { saint: "Dorothy Day", era: "1897–1980", position: "Dorothy Day - model of radical Gospel poverty and works of mercy.", optionIndex: 7 },
        { saint: "G.K. Chesterton", era: "1874–1936", position: "Dorothy Day - model of radical Gospel poverty and works of mercy.", optionIndex: 7 }
    ],
    129: [
        { saint: "Joseph de Maistre", era: "1753–1821", position: "Swift and decisive suppression. The Pope should use his full authority to discipline wayward bishops, remove those who persist in error, and if necessary suppress the conference...", optionIndex: 0 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "Swift and decisive suppression. The Pope should use his full authority to discipline wayward bishops, remove those who persist in error, and if necessary suppress the conference...", optionIndex: 0 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Firm correction within traditional structures. The Pope should clearly restate orthodox doctrine, require retraction of errors, and use canonical measures against persistent dis...", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Firm correction within traditional structures. The Pope should clearly restate orthodox doctrine, require retraction of errors, and use canonical measures against persistent dis...", optionIndex: 1 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Patient dialogue and accompaniment. The Church must listen to the concerns driving these movements, discern what the Spirit may be saying through them, and find ways to maintain...", optionIndex: 2 },
        { saint: "Cardinal Walter Kasper", era: "1933–present", position: "Patient dialogue and accompaniment. The Church must listen to the concerns driving these movements, discern what the Spirit may be saying through them, and find ways to maintain...", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Formal doctrinal intervention but respect for subsidiarity. The CDF should issue corrections and the Pope should teach clearly, but local churches have legitimate autonomy. Heav...", optionIndex: 3 }
    ],
    130: [
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Yes, and it would be the best thing to happen to the Church. A smaller, fervent remnant living authentic Catholicism is preferable to a bloated institution full of nominal belie...", optionIndex: 0 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Yes, and it would be the best thing to happen to the Church. A smaller, fervent remnant living authentic Catholicism is preferable to a bloated institution full of nominal belie...", optionIndex: 0 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "The problems of laxist, progressive clergy and lukewarm piety are generational. Progress is already being made among priests and laity under 50. Organic renewal is happening wit...", optionIndex: 1 },
        { saint: "Joseph Ratzinger", era: "1927–2022", position: "The problems of laxist, progressive clergy and lukewarm piety are generational. Progress is already being made among priests and laity under 50. Organic renewal is happening wit...", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "This would require clarifying the ambiguities built into Vatican II. The Council\'s documents admit of both traditional and progressive readings; only authoritative clarification...", optionIndex: 2 },
        { saint: "Pope St. Pius X", era: "1835–1914", position: "This would require clarifying the ambiguities built into Vatican II. The Council\'s documents admit of both traditional and progressive readings; only authoritative clarification...", optionIndex: 2 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "This would require undoing the errors of Vatican II. The Council itself, not just its implementation, introduced novelties incompatible with Tradition. Only a future Council or ...", optionIndex: 3 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "This would require undoing the errors of Vatican II. The Council itself, not just its implementation, introduced novelties incompatible with Tradition. Only a future Council or ...", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "No. Growth from the Church in the Global South will supersede Europe, and we must not have a Eurocentric church based on strict interpretations of rules and dogma. The future is...", optionIndex: 4 },
        { saint: "Pope Francis", era: "1936–present", position: "No. Growth from the Church in the Global South will supersede Europe, and we must not have a Eurocentric church based on strict interpretations of rules and dogma. The future is...", optionIndex: 4 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "In the West this would be ideal, but the Church is growing in the Global South. We should accept a smaller Western church while celebrating growth elsewhere. Different regions m...", optionIndex: 5 }
    ],
    131: [
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Paul VI - He faithfully implemented the Council while holding the line on Humanae Vitae. His suffering witness during the post-conciliar crisis was heroic.", optionIndex: 0 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "John Paul I - His brief pontificate suggested a simpler, more pastoral papacy. We can only imagine what renewal he might have brought.", optionIndex: 1 },
        { saint: "John Courtney Murray, S.J.", era: "1904–1967", position: "John Paul I - His brief pontificate suggested a simpler, more pastoral papacy. We can only imagine what renewal he might have brought.", optionIndex: 1 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "St. John Paul II - The Great Pope who defeated Communism, taught magnificently on faith and morals, and revitalized Catholic identity worldwide.", optionIndex: 2 },
        { saint: "St. John Paul II", era: "1920–2005", position: "St. John Paul II - The Great Pope who defeated Communism, taught magnificently on faith and morals, and revitalized Catholic identity worldwide.", optionIndex: 2 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Benedict XVI - The theologian-Pope who diagnosed the dictatorship of relativism, promoted liturgical renewal, and offered the hermeneutic of continuity.", optionIndex: 3 },
        { saint: "Joseph Ratzinger", era: "1927–2022", position: "Benedict XVI - The theologian-Pope who diagnosed the dictatorship of relativism, promoted liturgical renewal, and offered the hermeneutic of continuity.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Francis - The Pope of mercy, peripheries, and synodality who is renewing the Church for the 21st century and refocusing on the poor and marginalized.", optionIndex: 4 },
        { saint: "Cardinal Walter Kasper", era: "1933–present", position: "Francis - The Pope of mercy, peripheries, and synodality who is renewing the Church for the 21st century and refocusing on the poor and marginalized.", optionIndex: 4 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "None of them adequately preserved Tradition. The post-conciliar papacy has been a disaster requiring future correction.", optionIndex: 5 },
        { saint: "Various Authors", era: "20th–21st c.", position: "None of them adequately preserved Tradition. The post-conciliar papacy has been a disaster requiring future correction.", optionIndex: 5 }
    ],
    132: [
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Optimistic - The gates of hell shall not prevail. Despite current troubles, renewal movements, young orthodox vocations, and the growth of the Global South Church point to a bri...", optionIndex: 0 },
        { saint: "Pope Benedict XVI", era: "1927–2022", position: "Cautiously hopeful - A smaller, purer Church is emerging in the West while the faith flourishes elsewhere. The \'biological solution\' will resolve many current problems.", optionIndex: 1 },
        { saint: "Joseph Ratzinger", era: "1927–2022", position: "Cautiously hopeful - A smaller, purer Church is emerging in the West while the faith flourishes elsewhere. The \'biological solution\' will resolve many current problems.", optionIndex: 1 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Concerned but trusting Divine Providence - We are in a deep crisis, perhaps the worst since the Arian heresy. But God will raise up saints to renew the Church as He always has.", optionIndex: 2 },
        { saint: "St. Teresa of Ávila", era: "1515–1582", position: "Concerned but trusting Divine Providence - We are in a deep crisis, perhaps the worst since the Arian heresy. But God will raise up saints to renew the Church as He always has.", optionIndex: 2 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "Dark before the dawn - Things will get worse before they get better. A great chastisement or major supernatural intervention may be necessary. Fatima\'s warnings remain unfulfilled.", optionIndex: 3 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "Dark before the dawn - Things will get worse before they get better. A great chastisement or major supernatural intervention may be necessary. Fatima\'s warnings remain unfulfilled.", optionIndex: 3 },
        { saint: "Karl Rahner, S.J.", era: "1904–1984", position: "Progressive transformation - The Church is finally updating for the modern world. What looks like decline to some is actually healthy pruning and the Spirit leading us to new fo...", optionIndex: 4 },
        { saint: "St. John Henry Newman", era: "1801–1890", position: "Progressive transformation - The Church is finally updating for the modern world. What looks like decline to some is actually healthy pruning and the Spirit leading us to new fo...", optionIndex: 4 },
        { saint: "Archbishop Marcel Lefebvre", era: "1905–1991", position: "The institutional Church may collapse, but the Faith will endure in remnant communities maintaining Tradition until restoration comes.", optionIndex: 5 },
        { saint: "Dietrich von Hildebrand", era: "1889–1977", position: "The institutional Church may collapse, but the Faith will endure in remnant communities maintaining Tradition until restoration comes.", optionIndex: 5 }
    ],
    133: [
        { saint: "Archbishop Marcel Lefebvre", era: "1905-1991", position: "Vatican II's teachings on religious liberty and ecumenism contradict prior magisterium; the consecrations were necessary to preserve Tradition", optionIndex: 0 },
        { saint: "Pope Benedict XVI", era: "1927-2022", position: "Sought reconciliation through dialogue; restored the TLM via Summorum Pontificum; lifted excommunications to heal the schism", optionIndex: 2 },
        { saint: "St. John Henry Newman", era: "1801-1890", position: "Development of doctrine is organic; legitimate concerns must be raised within communion, not outside it", optionIndex: 3 },
        { saint: "Pope Francis", era: "1936-", position: "The reformed liturgy is the unique expression of the Roman Rite; restrictions on the old Mass serve ecclesial unity", optionIndex: 4 }
    ]
};

const MIN_QUESTIONS_THRESHOLD = 5;

// =============================================
// STATE
// =============================================
let scores = {};
let axisScores = {};
let answers = [];
let selectedQuestions = [];
let currentQuestion = 0;
let quizLength = 134;
let categoryQuestions = {};
let matchCounts = {};

// =============================================
// MAGISTERIUM AI INTEGRATION
// =============================================

function openMagisterium() {
    const qIndex = selectedQuestions[currentQuestion];
    const q = QUESTIONS[qIndex];
    const cat = getCategoryForQuestion(qIndex);
    const topic = getQuestionTopic(qIndex);
    
    let prompt = `I am taking a Catholic theology quiz and need help understanding this question.\n\n`;
    prompt += `Topic: ${topic.topic}\n`;
    prompt += `Question: "${q.text}"\n\n`;
    prompt += `The options are:\n`;
    q.options.forEach((opt, i) => {
        prompt += `${i + 1}. ${opt[0]}\n`;
    });
    prompt += `\nPlease explain what each option means theologically, which saints or theologians held each view, and what the key distinctions are. Do NOT tell me which to pick — help me understand so I can decide based on my own beliefs.`;
    
    // Copy to clipboard
    navigator.clipboard.writeText(prompt).then(() => {
        const btn = document.getElementById('magisterium-btn');
        const original = btn.innerHTML;
        btn.innerHTML = '✓ Prompt Copied! Opening Magisterium...';
        btn.style.background = 'rgba(40, 167, 69, 0.3)';
        setTimeout(() => {
            btn.innerHTML = original;
            btn.style.background = '';
        }, 2500);
        window.open('https://www.magisterium.com/', '_blank');
    }).catch(() => {
        // Fallback: just open
        window.open('https://www.magisterium.com/', '_blank');
    });
}
function openMagisteriumPanel() {
  const panel = document.getElementById('magisterium-panel');
  const iframe = document.getElementById('magisterium-iframe');
  const status = document.getElementById('mag-panel-status');

  panel.classList.remove('hidden');
  status.textContent = "Loading… If this stays blank, Magisterium likely blocks embedding; we’ll open it in a new tab.";

  // Attempt to embed
  iframe.src = "https://www.magisterium.com/";

  // If the iframe is blocked, it may stay blank or throw; we can’t reliably read cross-origin,
  // so we use a timeout-based fallback that preserves your QA-required behavior.
  const fallbackMs = 1600;
  setTimeout(() => {
    // Heuristic: if the iframe never fired load, or still looks blank, fall back.
    // (We can't inspect contents cross-origin, so keep it simple and user-friendly.)
    status.textContent = "If Magisterium is not visible, click 'Open in New Tab' (prompt is copied).";
  }, fallbackMs);
}

function closeMagisteriumPanel() {
  const panel = document.getElementById('magisterium-panel');
  const iframe = document.getElementById('magisterium-iframe');
  panel.classList.add('hidden');
  iframe.src = "about:blank";
}

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
    const totalQuestions = QUESTIONS.length;
    categoryQuestions = {};
    
    CATEGORIES.forEach(cat => {
        const catTotal = cat.questions.length;
        const proportion = catTotal / totalQuestions;
        let numToSelect = Math.max(1, Math.round(count * proportion));
        numToSelect = Math.min(numToSelect, catTotal);
        
        const shuffled = [...cat.questions].sort(() => Math.random() - 0.5);
        categoryQuestions[cat.id] = shuffled.slice(0, numToSelect).sort((a, b) => a - b);
    });
    
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
    matchCounts = {};
    SCHOOLS.forEach(([code]) => matchCounts[code] = 0);
}

function startQuiz() {
    document.getElementById('start-screen').classList.add('hidden');
    document.getElementById('magisterium-btn').style.display = '';
    document.getElementById('quiz-screen').classList.remove('hidden');
    initScores();
    selectedQuestions = selectQuestionsForQuiz(quizLength);
    answers = new Array(selectedQuestions.length).fill(null);
    currentQuestion = 0;
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
        
        let answered = 0;
        catQs.forEach(qIdx => {
            const selIdx = selectedQuestions.indexOf(qIdx);
            if (selIdx !== -1 && answers[selIdx] !== null) answered++;
        });
        
        const progressSpan = btn.querySelector('.cat-progress');
        if (progressSpan) progressSpan.textContent = `${answered}/${catQs.length}`;
        btn.classList.toggle('completed', answered === catQs.length && catQs.length > 0);
        
        const currentQIdx = selectedQuestions[currentQuestion];
        const isCurrentCat = catQs.includes(currentQIdx);
        btn.classList.toggle('active', isCurrentCat);
    });
}

function jumpToCategory(catIdx) {
    const cat = CATEGORIES[catIdx];
    const catQs = categoryQuestions[cat.id] || [];
    if (catQs.length === 0) return;
    
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

function getQuestionTopic(qIdx) {
    return QUESTION_TOPICS[qIdx] || {
        topic: QUESTIONS[qIdx].text,
        description: '',
        reading: 'Catechism of the Catholic Church',
        prompt: ''
    };
}

function renderQuestion() {
    const qIndex = selectedQuestions[currentQuestion];
    const q = QUESTIONS[qIndex];
    const cat = getCategoryForQuestion(qIndex);
    
    // Progress
    document.getElementById('progress-text').textContent = `Question ${currentQuestion + 1} of ${selectedQuestions.length}`;
    const answeredCount = answers.filter(a => a !== null).length;
    document.getElementById('answered-count').textContent = `Answered: ${answeredCount} / ${selectedQuestions.length}`;
    document.getElementById('progress-fill').style.width = `${(answeredCount / selectedQuestions.length) * 100}%`;
    
    const romanNumerals = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII','XXIII','XXIV','XXV','XXVI','XXVII','XXVIII','XXIX','XXX','XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL','XLI','XLII','XLIII','XLIV','XLV','XLVI','XLVII','XLVIII','XLIX','L','LI','LII','LIII','LIV','LV','LVI','LVII','LVIII','LIX','LX','LXI','LXII','LXIII','LXIV','LXV','LXVI','LXVII','LXVIII','LXIX','LXX','LXXI','LXXII','LXXIII','LXXIV','LXXV','LXXVI','LXXVII','LXXVIII','LXXIX','LXXX','LXXXI','LXXXII','LXXXIII','LXXXIV','LXXXV','LXXXVI','LXXXVII','LXXXVIII','LXXXIX','XC','XCI','XCII','XCIII','XCIV','XCV','XCVI','XCVII','XCVIII','XCIX','C','CI','CII','CIII','CIV','CV','CVI','CVII','CVIII','CIX','CX','CXI','CXII','CXIII','CXIV','CXV','CXVI','CXVII','CXVIII','CXIX','CXX','CXXI','CXXII','CXXIII','CXXIV','CXXV','CXXVI','CXXVII','CXXVIII','CXXIX','CXXX','CXXXI','CXXXII','CXXXIII','CXXXIV'];
    
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
    
    // IDK button state
    const idkBtn = document.getElementById('idk-btn');
    idkBtn.classList.toggle('selected', answers[currentQuestion] === -1);
    
    // Saints
    renderSaints(qIndex);
    
    // Sources
    renderSources(qIndex);
    
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
    
    // Close panels
    document.getElementById('saints-toggle').classList.remove('open');
    document.getElementById('saints-content').classList.remove('open');
    document.getElementById('sources-toggle').classList.remove('open');
    document.getElementById('sources-content').classList.remove('open');
}

function renderSaints(qIndex) {
    const list = document.getElementById('saints-list');
    list.innerHTML = '';
    const views = SAINT_VIEWS[qIndex];
    if (!views || views.length === 0) {
        list.innerHTML = '<div class="no-saints">No specific saint/theologian mappings available for this question yet.</div>';
        return;
    }
    views.forEach(v => {
        const card = document.createElement('div');
        card.className = 'saint-card' + (answers[currentQuestion] === v.optionIndex ? ' active' : '');
        card.innerHTML = `
            <div class="saint-card-opt">Aligns with Option ${v.optionIndex + 1}</div>
            <div class="saint-card-name">${v.saint}</div>
            <div class="saint-card-era">${v.era}</div>
            <div class="saint-card-pos">${v.position}</div>
        `;
        card.onclick = () => {
            selectOption(v.optionIndex);
            renderQuestion();
        };
        list.appendChild(card);
    });
}

function renderSources(qIndex) {
    const list = document.getElementById('sources-list');
    const topic = getQuestionTopic(qIndex);
    list.innerHTML = `
        <div class="source-topic">📚 ${topic.topic}</div>
        <div class="source-desc">${topic.description}</div>
        <div class="source-reading"><strong>Further Reading:</strong> ${topic.reading}</div>
    `;
}

function toggleSaints() {
    document.getElementById('saints-toggle').classList.toggle('open');
    document.getElementById('saints-content').classList.toggle('open');
}

function toggleSources() {
    document.getElementById('sources-toggle').classList.toggle('open');
    document.getElementById('sources-content').classList.toggle('open');
}

// =============================================
// ANSWER SELECTION
// =============================================

function selectOption(index) {
    answers[currentQuestion] = index;
    document.querySelectorAll('.option').forEach((opt, i) => opt.classList.toggle('selected', i === index));
    document.getElementById('idk-btn').classList.remove('selected');
    updateQuestionNav();
    updateProgressDisplay();
}

function selectIDK() {
    answers[currentQuestion] = -1;
    document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
    document.getElementById('idk-btn').classList.add('selected');
    updateQuestionNav();
    updateProgressDisplay();
}

function updateProgressDisplay() {
    const answeredCount = answers.filter(a => a !== null).length;
    document.getElementById('answered-count').textContent = `Answered: ${answeredCount} / ${selectedQuestions.length}`;
    document.getElementById('progress-fill').style.width = `${(answeredCount / selectedQuestions.length) * 100}%`;
}

function nextQuestion() {
    if (answers[currentQuestion] === null) {
        if (!confirm('You have not selected an answer. Skip this question?')) return;
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
    matchCounts = {};
    SCHOOLS.forEach(([code]) => matchCounts[code] = 0);
    
    for (let i = 0; i < selectedQuestions.length; i++) {
        const answer = answers[i];
        if (answer === null || answer === -1) continue;
        
        const qIndex = selectedQuestions[i];
        const q = QUESTIONS[qIndex];
        const option = q.options[answer];
        if (!option) continue;
        
        const weights = option[1];
        for (const [school, weight] of Object.entries(weights)) {
            if (scores[school] !== undefined) {
                scores[school] += weight;
                if (weight > 0) matchCounts[school]++;
            }
        }
        
        if (q.axis_weights) {
            for (const [axis, weight] of Object.entries(q.axis_weights)) {
                if (axisScores[axis] !== undefined) {
                    axisScores[axis] += weight * (answer < q.options.length / 2 ? -1 : 1);
                }
            }
        }
    }
}

function showResults() {
    calculateScores();
    document.getElementById('quiz-screen').classList.add('hidden');
    document.getElementById('results-screen').style.display = 'block';
    document.getElementById('magisterium-btn').style.display = 'none';
    
    // Sort schools by score
    const ranked = SCHOOLS
        .map(([code, name]) => ({ code, name, score: scores[code] || 0, count: matchCounts[code] || 0 }))
        .filter(s => s.score > 0)
        .sort((a, b) => b.score - a.score);
    
    if (ranked.length === 0) return;
    
    const top = ranked[0];
    const desc = SCHOOL_DESC[top.code] || { summary: '', affirmations: [] };
    const figure = SCHOOL_FIGURES[top.code] || { figure: '', era: '', bio: '', works: '' };
    const maxScore = MAX_POSSIBLE_SCORES[top.code] || 100;
    
    document.getElementById('top-match-container').innerHTML = `
        <div class="top-match">
            <div class="top-match-label">Your Closest Match</div>
            <div class="top-match-name">${top.name}</div>
            <div class="top-match-score">${top.score} points (${Math.round(top.score / maxScore * 100)}% alignment)</div>
            <div class="top-match-summary">${desc.summary}</div>
            <div class="top-match-affirmations">
                ${(desc.affirmations || []).map(a => `<span class="affirmation-tag">${a}</span>`).join('')}
            </div>
            <div class="figure-section">
                <div class="figure-label">Key Figure</div>
                <div class="figure-name">${figure.figure}</div>
                <div class="figure-era">${figure.era}</div>
                <div class="figure-bio">${figure.bio}</div>
            </div>
        </div>
    `;
    
    // Rankings table
    const tbody = document.getElementById('rankings-body');
    tbody.innerHTML = '';
    ranked.slice(0, 30).forEach((school, i) => {
        const maxS = MAX_POSSIBLE_SCORES[school.code] || 100;
        const pct = Math.round(school.score / maxS * 100);
        const hetero = (typeof HETERODOXY_STATUS !== 'undefined') ? HETERODOXY_STATUS[school.code] : null;
        let warning = '';
        if (hetero) warning = ` <span title="${hetero.title}" style="cursor:help;">⚠️</span>`;
        tbody.innerHTML += `
            <tr>
                <td class="rank-num ${i < 3 ? 'top-3' : ''}">${i + 1}</td>
                <td class="school-name">${school.name}${warning} <span class="question-count">(${school.count} q)</span></td>
                <td><div class="score-bar-container"><div class="score-bar"><div class="score-bar-fill" style="width:${pct}%"></div></div><div class="score-value">${school.score} / ${maxS} (${pct}%)</div></div></td>
            </tr>
        `;
    });
    
    // Axes
    const axesDiv = document.getElementById('axes-content');
    axesDiv.innerHTML = '';
    AXES.forEach(([code, name]) => {
        const raw = axisScores[code] || 0;
        const mult = AXIS_MULTIPLIER[code] || 3;
        const max = selectedQuestions.length * mult;
        const pct = Math.max(0, Math.min(100, 50 + (raw / max) * 50));
        const endpoints = AXIS_ENDPOINTS[code] || ['Left', 'Right'];
        axesDiv.innerHTML += `
            <div class="axis-row">
                <div class="axis-header"><span class="axis-name">${name}</span><span class="axis-score">${raw > 0 ? '+' : ''}${raw}</span></div>
                <div class="axis-bar">
                    <div class="axis-labels"><span>${endpoints[0]}</span><span>${endpoints[1]}</span></div>
                    <div class="axis-marker" style="left:calc(${pct}% - 9px)"></div>
                </div>
            </div>
        `;
    });
    
    window.scrollTo(0, 0);
}

function switchTab(tabName) {
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(tc => tc.classList.remove('active'));
    const activeBtn = document.querySelector(`.tab-btn[onclick*="${tabName}"]`);
    if (activeBtn) activeBtn.classList.add('active');
    document.getElementById(tabName + '-tab').classList.add('active');
}

function retakeQuiz() {
    document.getElementById('results-screen').style.display = 'none';
    document.getElementById('quiz-screen').classList.add('hidden');
    document.getElementById('start-screen').classList.remove('hidden');
    document.getElementById('magisterium-btn').style.display = 'none';
}

// =============================================
// INIT
// =============================================

document.addEventListener('DOMContentLoaded', () => {
    initScores();
    setQuizLength(134);
});
    </script>

<!-- Magisterium Panel (optional iframe view with fallback) -->
<div id="magisterium-panel" class="mag-panel hidden" role="dialog" aria-modal="true" aria-label="Magisterium Panel">
  <div class="mag-panel-header">
    <div class="mag-panel-title">Magisterium (embedded view)</div>
    <div class="mag-panel-actions">
      <button class="mag-panel-btn" onclick="openMagisteriumPanel()">Open Within the Window</button>
      <button class="mag-panel-btn" onclick="openMagisterium()">Copy Prompt &amp; Open in New Tab</button>
      <button class="mag-panel-btn" onclick="closeMagisteriumPanel()">Close</button>
    </div>
  </div>

  <div class="mag-panel-body">
    <div id="mag-panel-status" class="mag-panel-status">
      Loading… If this stays blank, Magisterium likely blocks embedding; we’ll open it in a new tab.
    </div>
    <iframe
      id="magisterium-iframe"
      title="Magisterium"
      class="mag-iframe"
      referrerpolicy="no-referrer"
      sandbox="allow-forms allow-scripts allow-same-origin allow-popups"
    ></iframe>
  </div>
</div>

</body>
</html>
