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

## 2026-06-12 — Top-level fast-control panel (xsphere_daq.panel)

Promoted the camera dock into the top-level control surface (README direction step 2:
"centralize"). New `xsphere_daq` package:

- `xsphere_daq/panel.py` — a parent FastAPI app with a fast-control **dashboard at `/`**
  that mounts the camera dock (`camera_dock.webapp`) at **`/cameras`** as the first
  subsystem. The parent owns the lifecycle (brings the cameras up on startup, down on
  shutdown via `webapp.start_all`/`stop_all`; the camera app is built with
  `manage_lifecycle=False`). Future fast-control subsystems mount alongside.
- `python -m xsphere_daq.panel basler zelux --host 0.0.0.0 --port 8000`.
- Added a top-level `requirements.txt` (`-r xsphere-camera-dock/requirements.txt`) and a
  "Running the fast-control panel" section to the README.

**Validated on hardware (Basler + Zelux):** dashboard at `/`; cameras at `/cameras/`
with all links correctly prefixed; mounted info/controls/stream work; both cameras
brought up by the parent lifecycle. (Required a webapp mountability fix — see the dock
log.)

## 2026-06-12 — Reframe README: this is the fast control system

User clarified the architecture: the experiment has two **separate** control systems —
**slow control** (sibling repo `xsphere-slow-control`) and **fast control**. `xsphere-daq`
**is the fast control system**; cameras are its starting point, with more fast-control
subsystems to follow. The two systems are **not** integrated (corrects an earlier wrong
assumption that slow-control was an integration target).

- Reframed the top-level README intro accordingly; clarified the slow-control repo is a
  separate, non-integrated system (was listed as a "sibling project").
- Refreshed the stale Status section to reflect current state (both cameras validated;
  shared engine + recorder; multi-camera web app with controls + presets; Hayear
  scaffolded). Recorded in memory `fast-vs-slow-control-architecture`.

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
