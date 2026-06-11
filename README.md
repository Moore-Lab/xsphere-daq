# xsphere-daq

Data acquisition and centralized control for the xsphere experiment.

The long-term vision is a single control surface for the whole experiment — preferably
a **web app**, so the rig can be driven and monitored remotely (e.g. camera feeds
streaming into an embedded window). DAQ subsystems are organized as git submodules so
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

Sibling project: [xsphere-slow-control](https://github.com/Moore-Lab/xsphere-slow-control).

## Status

Scaffolding only — repo + submodule structure in place; development plan to follow.
