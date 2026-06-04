# OOD Generalization Manim Video

Project Manim for the Lab01 video:
`Out-of-Distribution Generalization: Shortcuts, Spuriousness & Stability`.

## Quick Start

Render a preview scene:

```powershell
manim -pql src/module0_hook.py OpeningClinicalNotes
```

Render all scenes at low quality:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/render_all.ps1 -Quality l
```

Generate subtitles and narration text from `kich_ban_v2_OOD_3b1b.md`:

```powershell
python scripts/extract_assets.py
```

Generate Vietnamese voiceover with Windows SAPI, then subtitle files:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/make_voiceover.ps1
```

If Vietnamese TTS quality is poor, record English/Vietnamese narration manually from
`assets/narration/voiceover_script.md` and keep the generated `.srt` timing as a draft.

## Structure

- `src/common.py`: shared Manim colors, helper shapes, scene base class.
- `src/module*.py`: video scenes mapped from the markdown script.
- `scripts/extract_assets.py`: extracts AUDIO blocks, creates narration script and draft SRT.
- `scripts/render_all.ps1`: renders all scenes.
- `scripts/make_voiceover.ps1`: creates per-scene WAV files via Windows SAPI.

