# CheatCodes Hub — GitHub content repository (v1 handoff)

This repository is intended for GitHub Pages static HTTPS hosting. It is a **research starter**, not a complete production cheat collection.

## Paths
- `manifest.json`: version and file checksums
- `catalog.json`: game metadata, visual fallbacks and server paths
- `games/*.json`: per-game cheat entries, platform inputs and verification
- `sources.json`: research bibliography and unresolved reuse status
- `images.json`: per-game image inventory
- `assets/games/<id>/icon.webp`, `cover.webp`: original illustrated local fallback imagery
- `coverage-report.json`: honest input counts by platform
- `schema/contract.md`: implementation rules

## Hosting
Publish **the contents of this directory** at the root of your static GitHub Pages site. App base URL is `https://<owner>.github.io/<repo>/`. Fetch `manifest.json` first, then `catalog.json`, then game JSON on demand. Do not embed a GitHub `blob/` page as a JSON endpoint.

## Offline
Bundle the entire `catalog.json`, all current `games/*.json`, `sources.json` and `assets/games/**/*.webp` into app resources at build time. The app must work on first launch with no network. Sync remote updates opportunistically in the background and keep last known good snapshots.

## Warnings
Current data is partial. The prior research starter listed 48 cheats across 8 games, primarily PC. GTA V PS/Xbox inputs and GTA VI verified inputs remain missing. Do not misrepresent counts or verification. Image generation does not guarantee IP clearance; review and avoid recognizable protected assets.

## Validation
Run: `python validate_content.py`.
