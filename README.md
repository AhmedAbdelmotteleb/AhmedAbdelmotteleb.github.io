# ahmedabdelmotteleb.github.io

Personal research website of Ahmed Abdelmotteleb, served by GitHub Pages from `main`.
Plain HTML and one stylesheet: no build step, no framework, no trackers.

## Layout

| Path | What it is |
| --- | --- |
| `index.html` | Home page |
| `research/index.html` | Research themes (plain-language summary + "For physicists" details) |
| `publications/index.html` | Selected papers, proceedings, talks and lectures |
| `cv/index.html` | Web CV; the PDF lives at `cv/Ahmed_Abdelmotteleb_CV.pdf` |
| `404.html` | Not-found page |
| `assets/css/site.css` | All styles. Colours, type and spacing are tokens at the top (light + dark) |
| `assets/js/site.js` | Optional enhancement (gallery buttons). The site works without it |
| `assets/icons.svg` | SVG icon sprite, used as `<svg><use href="/assets/icons.svg#i-github"/></svg>` |
| `assets/img/` | Optimised WebP images used by the pages |
| `assets/fonts/` | Self-hosted Inter and Source Serif 4 (latin subset) |
| `images/` | Original photos (sources for `assets/img/`). `*_upscaled.png` are AI-upscaled masters (Real-ESRGAN x4, blended 55/45 with the original to keep faces natural) |
| `assets/img/originals/` | Previous web versions of images that were replaced by upscaled ones (not used by the pages) |

## Common updates

- **New paper or talk:** copy an existing `<li>` in `publications/index.html` and edit it. If it should
  appear on the home page too, update the "Selected publications" / "Recent talks" lists in `index.html`.
- **New CV:** replace `cv/Ahmed_Abdelmotteleb_CV.pdf` (keep the file name) and update `cv/index.html` if needed.
- **New photo:** add a resized `.webp` to `assets/img/` (about 600 px tall for the gallery) and add an
  `<li><figure>` to the gallery in `index.html` with `width`, `height`, `alt` and a caption.
- **"Updated" date:** in the footer of each page and in `sitemap.xml`.

## LHCb news

`.github/workflows/actions.yml` runs `main.py` daily. It reads the
[LHCb outreach RSS feed](https://lhcb-outreach.web.cern.ch/feed/) and rewrites the list between the
`LHCB-NEWS:START` / `LHCB-NEWS:END` markers in `index.html`, committing only if something changed.
If the feed is unreachable it leaves the page as it is. Run it locally with `python main.py`
(standard library only).

## Preview locally

```sh
python -m http.server 8000
```

then open http://localhost:8000. Root-relative links (`/research/`) need a server rather than `file://`.
