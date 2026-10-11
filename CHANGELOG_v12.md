# v12 — Portraits

- Real portraits for all 103 detailed results and the Conciliar–Pastoral Renewal family (104 images), replacing the drawn SVG portraits wherever an image exists. The SVGs remain as a fallback.
- Portraits live in `portraits.js` as embedded JPEGs (about 3 MB), loaded after the page. Embedding keeps the share card working when `index.html` is opened directly from disk.
- Results screen: headline portrait with name, dates and image credit; avatar beside the closest detailed school; small portraits on family cards and school rankings; a “Portrait credits” list for every image shown.
- Share card shows the headline figure's portrait in the top-right corner, and the doctrine-axis rows were tightened so the last axis no longer overlaps the footer.
- The header logo now loads from the same folder instead of an absolute GitHub URL, so it also works offline and on forks.
- Added `PORTRAIT_CREDITS.md` and `tools/portrait_fetcher.html`.
- The old `catholic_quiz_IMPROVED.py` (actually an early 134-question HTML build) moved to `legacy/catholic_quiz_legacy_134q.html`.

## To verify before publishing

- Seven portraits have no recorded source or licence (marked in `PORTRAIT_CREDITS.md`): Congar, de Lubac, Pseudo-Dionysius, Báñez, Steenson, Gury, McCormick; plus Pope Francis and Cardinal Kasper, whose licence was not recorded.
