# xsphere-daq — Development Session Log

Running, chronological record of development for **this repo only** (`xsphere-daq`, the
top level). Changes inside a submodule are logged in *that submodule's* own
`docs/session-log.md` — write to the log of the repo you're actually modifying.

Scope of this log: top-level structure, submodule pointer bumps, top-level docs, and
(eventually) the centralized DAQ control panel / web app.

Per-repo logs:
- `xsphere-daq` — this file.
- `xsphere-camera-dock/docs/session-log.md`
- `xsphere-camera-dock/basler-acA1440/docs/session-log.md`
- `xsphere-camera-dock/zelux-cs165mu/docs/session-log.md`

Newest entries first. Keep entries short and factual; convert relative dates to absolute.
See the [README](../README.md) for project vision.

---

## 2026-06-11 — Per-repo session logs established

**Context.** First logged session. Reviewed the README hierarchy and code to baseline the
project, then set up development tracking.

- Added `docs/session-log.md` to **each** repo (`xsphere-daq`, `xsphere-camera-dock`,
  `basler-acA1440`, `zelux-cs165mu`). Convention: write to the log of the repo being
  modified. Lower-level camera repos will stop accruing entries once their drivers are
  done; activity then moves up to the dock and top level.
- Linked each log from its repo's README Status section.

**Top-level state.** Scaffolding: repo + nested submodule structure in place
(`xsphere-camera-dock` → `basler-acA1440`, `zelux-cs165mu`). No top-level DAQ control
panel or web app yet.

**Next (top-level):** nothing actionable here until the dock matures — the centralized
control panel / web app (README direction steps 2–3) comes after the dock's integration
layer exists.
