# CheatCodes Hub content contract v1

## Entry point
`manifest.json` -> `catalog.json` -> on-demand `games/{gameId}.json`. `sources.json` is loaded when citations are displayed. `images.json` is optional content inventory.

## Image policy
`iconUrl` / `coverImageUrl` are nullable remote HTTPS URLs. `localIconAsset` and `localCoverAsset` are bundled paths for offline fallback. Remote images are only used after commercial rights review. When remote fetch fails, display local asset. Never derive URL from a title.

## Platform behavior
`supportedPlatformIds` means the game supports that platform, **not** that matching cheat inputs exist. The app must only expose a cheat/platform pair when that cheat has matching `inputs[].platformIds`; if none exist, say 'Codes not available for this platform yet'. Never reuse PC text inputs on a PlayStation or Xbox panel.

## Cheat and source behaviors
Keep `verification.status` verbatim. `single_source_not_device_tested` is **not** equivalent to confirmed; never show a green Verified badge for it. When `cheats` is empty, display an honest no-verified-codes state. Details should include title, description, code/sequence, method, source links, verification and favorite. Never copy external site descriptions or bulk data without rights review.

## Updating
Compare `manifest.dataVersion` and per-file hashes. Download to a temp file, validate JSON, IDs, hashes and schema, then atomically replace cached data. On failure keep last-known-good data. User can access cached and bundled content offline. New games must be addable by catalog + game JSON only.
