# Changelog

All notable changes to RacerAPI are documented here.

## [1.0.0] - 2026-11-22

### Stable baseline
- Adopt Poetry and poetry-core as the sole project/dependency/build manager.
- Define Python 3.11+ support and bounded runtime dependency ranges.
- Publish a documented public application factory through `racerapi.create_app`.
- Consolidate app creation through the plugin-aware bootstrap path.
- Keep the legacy `racerapi.app.create_app` import as a compatibility alias.
- Make module discovery fail visibly on invalid module registration rather than silently starting an incomplete application.
- Add application-scoped DI bootstrap and expose a deterministic router registry reset for tests.
- Align generated project metadata with Poetry.
- Rebuild CI and nightly validation around the Poetry lock/install flow.
- Consolidate documentation deployment and correct the MkDocs root path.
- Add package build metadata and distribution validation.

### Compatibility
- Previous 0.x releases were experimental and are not guaranteed to be compatible.
- Python 3.10 is no longer supported.
- The documented public API is `racerapi.create_app` and the `racerapi` CLI.

## [0.0.7] - 2026-04-15
- Experimental framework release; see GitHub release notes.
