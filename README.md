# xsphere-daq

The **fast control system** for the xsphere experiment — data acquisition and real-time
control. **Cameras are the starting point**; further fast-control subsystems will follow
under this repo.

This is distinct from the experiment's **slow control** system, which is a separate
project ([xsphere-slow-control](https://github.com/Moore-Lab/xsphere-slow-control)) — the
two are independent and are **not** integrated.

The long-term vision is a single control surface for the fast-control subsystems —
preferably a **web app**, so the rig can be driven and monitored remotely (e.g. camera
feeds streaming into an embedded window). Subsystems are organized as git submodules so
each can be developed and tested independently before being composed here.

## Submodules

| Path | Purpose | Repo |
|------|---------|------|
| `xsphere-camera-dock` | Connect to and combine the experiment's cameras | [Moore-Lab/xsphere-camera-dock](https://github.com/Moore-Lab/xsphere-camera-dock) |

The camera dock in turn nests one submodule per camera brand
(`basler-acA1440`, `zelux-cs165mu`), each an independent driver/API + test GUI.

## Cloning

```bash
git clone --recurse-submodules https://github.com/Moore-Lab/xsphere-daq.git
# or, after a plain clone:
git submodule update --init --recursive
```

## Direction

1. **Cameras first** — get each camera working in isolation (driver + test GUI), then
   combine their feeds in `xsphere-camera-dock`. Priority features: frame rate, exposure,
   snapshots, recording.
2. **Centralize** — promote the dock into the top-level DAQ control panel.
3. **Remote** — expose everything as a web app for remote operation and monitoring.

## Status

Camera fast-control is well underway. Both cameras (`basler-acA1440`, `zelux-cs165mu`)
have hardware-validated drivers behind a shared `CameraBase` interface, with a shared
acquisition engine + hybrid recorder (records at full data rate) and per-camera test
GUIs. The dock web app (`camera_dock.webapp`) streams and controls **multiple cameras**
at once — live exposure/gain/ROI/auto-exposure, timestamped recording, and reproducible
settings presets. A Hayear (ToupTek-OEM) camera driver is scaffolded, pending hardware.

Development is tracked per repo in `docs/session-log.md` (this repo's:
[`docs/session-log.md`](docs/session-log.md)) — write to the log of the repo being
modified.
