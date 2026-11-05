# Infina Sans

A typeface for Infina, built on [Lexend](https://github.com/googlefonts/lexend) by Bonnie Shaver-Troup and Thomas Jockin, and released under the SIL Open Font License 1.1.

| | |
|---|---|
| Format | Variable font, one axis |
| Weight (`wght`) | 100 – 900, default 400 (Regular) |
| Named weights | Thin, ExtraLight, Light, Regular, Medium, SemiBold, Bold, ExtraBold, Black |
| Version | **1.004** |

## What changed from Lexend

1. **Tighter letters, original numbers.** Letters are 2% tighter (−0.02 em, the same as Figma letter spacing −2%). This covers all Vietnamese letters, ligatures such as fi and fl, and the word space. Digits 0–9 and the symbols used with numbers (`. , : % ₫ + − /`) keep Lexend's original spacing, so amounts such as `1.234.567.890 ₫` and `7,25%` keep an even rhythm and number columns still line up.
2. **Logo-style "fi" in the brand name.** When you type `infina` or `Infina`, the f and i join the way they do in the Infina logo: the f crossbar sits on the x-height and runs across to become the top of a dotless i. Other words (fintech, profile, wifi) are not affected. The joined form takes exactly the width of f + i, so line length does not change.
3. **Optional join everywhere.** Stylistic Set 2 (`ss02`) applies the logo-style join to every f + i. It is off by default. Stylistic Set 1 (`ss01`) is Lexend's own and is unchanged.

Uppercase `INFINA` does not join, because the logo is lowercase. Kerning, the other ligatures and stylistic sets, and all Vietnamese characters from Lexend are kept.

Typed text matches the logo's f–i join, but it is not the logo. The logo has its own spacing and f hook, so wherever the logo is meant, use the logo file.

## Files

| File | Use |
|---|---|
| `InfinaSans-VF.ttf` | Install on desktop (Figma, Office, Adobe) |
| `InfinaSans-VF.woff2` | Web |
| `OFL.txt` | License. Ship it with the fonts. |
| `README.md` | This file |

## Installing

1. Remove any earlier Infina Sans (versions 1.000 to 1.003). They share the same family name, so the system or Figma may keep showing the old one.
   - **macOS:** open Font Book, search "Infina Sans", delete every match.
   - **Windows:** Settings → Personalization → Fonts, search "Infina Sans", uninstall.
2. Quit apps that use the font (Figma desktop, Word, Adobe apps).
3. Install `InfinaSans-VF.ttf`, then reopen the apps. If the old version still shows, restart the computer.

To check, Font Book → select the font → Get Info should show **Version 1.004**.

In design apps, the join inside "infina" works without any setting. To join every fi, turn on Stylistic Set 2 in the app's OpenType options.

## Using on the web

```css
@font-face {
  font-family: "Infina Sans";
  src: url("InfinaSans-VF.woff2") format("woff2");
  font-weight: 100 900;
  font-display: swap;
}

body { font-family: "Infina Sans", system-ui, sans-serif; }

/* join every f + i like the logo */
.fi-everywhere { font-feature-settings: "ss02" 1; }

/* turn the join off, even inside "infina" */
.no-logo-fi { font-feature-settings: "calt" 0; }
```


## License

Infina Sans is a Modified Version of Lexend, distributed under the SIL Open Font License 1.1 (see `OFL.txt`). You may use it freely, including commercially, and bundle it with software. When you redistribute the font files, include `OFL.txt`. The font may not be sold on its own, and any derivative must also stay under the OFL.

Lexend's license reserves the font name "RevReading Lexend". To respect that, this font does not use "Lexend" in its name.

## Credits

- Original design: Lexend, © 2018 The Lexend Project Authors (Bonnie Shaver-Troup, Thomas Jockin)
- Modifications: Infina, 2026
