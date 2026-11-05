# Infina Fonts

Web font for Infina, served from this repository through the jsDelivr CDN.

| Family | Based on | Weights | Notes |
|---|---|---|---|
| **Infina Sans** | Lexend | 100 – 900 | Lexend letter spacing, word space −2%, lighter Regular, smaller comma; "infina" joins f–i like the logo |

Details are in [`infina-sans/README.md`](infina-sans/README.md).

## Use on a website

Add one line to the page's `<head>`, replacing `<owner>` and the version tag:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/<owner>/infina-fonts@v1.0.0/fonts.css">
```

Then use it in CSS:

```css
body { font-family: "Infina Sans", system-ui, sans-serif; }
```

The word spacing is built into the font, so leave `letter-spacing` and `word-spacing` at `0`.

Optional, to load the font sooner:

```html
<link rel="preload" as="font" type="font/woff2" crossorigin
      href="https://cdn.jsdelivr.net/gh/<owner>/infina-fonts@v1.0.0/infina-sans/InfinaSans-VF.woff2">
```

### Always pin a version

Use a release tag such as `@v1.0.0` in the URL, never a branch name. A tagged URL never changes, so browsers and the CDN can cache it for a year. When the font changes, publish a new tag (`v1.1.0`) and update the URL on each site. That also avoids the old-version cache problem.

## Releasing a new version

1. Replace the font files (keep the same file names).
2. Commit, then create a tag: `git tag v1.1.0 && git push origin v1.1.0`
3. Update the version in the `<link>` URL on the websites that should switch.

jsDelivr picks up the new tag automatically. Nothing needs to be uploaded elsewhere.

## Install on a computer

Download `infina-sans/InfinaSans-VF.ttf`. See [`infina-sans/README.md`](infina-sans/README.md) for clean-install steps (remove older versions first).

## License

Infina Sans is released under the SIL Open Font License 1.1 (see [`infina-sans/OFL.txt`](infina-sans/OFL.txt)). You may use it freely, including commercially, and redistribute it with its `OFL.txt`. It may not be sold on its own.

- Modified from Lexend, © 2018 The Lexend Project Authors (Reserved Font Name "RevReading Lexend")
- Modifications: Infina, 2026
