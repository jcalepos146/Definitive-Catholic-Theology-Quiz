# v10 — Modern Scholastic UI & Scoring Overhaul

## Interface

- Replaced the default CRT-first interface with a 12Axes-inspired academic layout.
- New landing page explains the output before asking for settings.
- Quiz depths renamed Essential (30), Standard (60), Advanced (90), and Complete (130).
- Standard (60) is the default.
- Advanced settings now hold category focus and Formation/Examination controls.
- Quiz screen removes persistent category and question-number grids from the visible UI.
- Answer cards show propositions only; school labels are hidden.
- Representatives and sources are expandable secondary material.
- Results now foreground the headline Catholic family and doctrine axes.
- Detailed schools, ecclesial analogues, approach map, categories, review, comparison, reading, timeline, and neighbor map are placed under “Explore detailed analysis.”
- New warm ivory / burgundy academic visual system and responsive mobile rules.
- Old DOS boot code is disabled by default.

## School weighting

- Added question-level reliability modifiers on top of category weights.
- High-discrimination dogmatic/theological questions receive 1.15×.
- Preference/spirituality items receive 0.55×.
- Prudential/current-application items receive 0.72×.
- Other questions remain 1.00×.
- Category weights were moderated so no one topic swamps the result.
- Conviction changed from 0.55 / 1.00 / 1.45 to 0.80 / 1.00 / 1.20.

## Doctrine-axis system

Axis scores are now independent of school matching. Each axis uses explicit question rules and per-option coordinates.

1. Synergism ↔ Monergism
2. Molinism ↔ Physical Premotion
3. Univocity of Being ↔ Analogy of Being
4. Voluntarism ↔ Intellectualism
5. Fall-Contingent Incarnation ↔ Absolute Primacy of Christ
6. Forensic Justification ↔ Transformative Justification
7. Memorialism ↔ Sacramental Realism
8. Conciliarism ↔ Ultramontanism
9. Historical-Critical ↔ Patristic-Figural
10. Liturgical Reformism ↔ Liturgical Traditionalism
11. Probabilism ↔ Tutiorism
12. Universalist Hope ↔ Restrictivism

- Removed category weighting from axis calculations.
- Removed tanh distortion; axis coordinates are linearly normalized.
- Added a central midpoint marker and a short definition for every spectrum.
- Essential, Standard, and Advanced modes force one direct anchor question for all 12 axes before filling remaining slots through balanced category sampling.

## Other fixes

- Fixed an option-rendering regression from v9 (`parsed.clean` -> displayed proposition text).
- Fixed the startup script so Standard 60, rather than Complete 130, is the actual default.
- Updated the share card to 1080×1350 and the new visual identity.
