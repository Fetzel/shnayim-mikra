# שנים מקרא ואחד תרגום — Android app

The reader lives in `src/` (one HTML page, plus `data/` and `fonts/`). `npm run sync` wraps it and copies it into the Android project.

## Getting the APK

**Option A, GitHub (no tools on your computer):** push this folder to a GitHub repository. The workflow in `.github/workflows/android.yml` builds the app on every push and attaches `app-debug.apk` to a new Release. Open the Release on the tablet, download the APK, and allow installing from that source when Android asks.

**Option B, Android Studio:** install Node.js and Android Studio, then:

```
npm install
npm run sync
npx cap open android
```

In Android Studio choose Build ▸ Build App Bundle(s) / APK(s) ▸ Build APK(s).

## Sources and licenses
- Torah text: Miqra according to the Masorah (MAM), CC BY-SA 4.0, with Ashkenazi scroll spellings applied from its notes.
- Onkelos (public domain) and Rashi (Rosenbaum & Silbermann, public domain) via the Sefaria export.
- Aliyah divisions and parsha calendar: Hebcal (`@hebcal/leyning`, `@hebcal/core`), BSD-2-Clause.
- Fonts: Culmus fonts (GPL with font exception), Shlomo Stam (SIL OFL), Mekorot Rashi (LPPL).
