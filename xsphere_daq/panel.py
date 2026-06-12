"""xsphere-daq fast-control panel — the top-level web surface.

Composes the fast-control subsystems into one panel: a dashboard at ``/`` and each
subsystem mounted beneath it. The camera dock (``camera_dock.webapp``) is mounted at
``/cameras`` as the first subsystem; future fast-control subsystems mount alongside.

The parent app owns the lifecycle (connect/start the camera sessions on startup, stop
on shutdown) and mounts the camera app with ``manage_lifecycle=False`` so there is a
single, top-level place that brings the rig up and down.

Run it::

    python -m xsphere_daq.panel basler zelux --host 0.0.0.0 --port 8000

Then open http://<host>:<port>/ for the dashboard (cameras live under /cameras/).
"""

from __future__ import annotations

import argparse
import os
import sys

# The camera dock is a submodule at <repo>/xsphere-camera-dock; put it on the path
# so ``camera_dock`` imports. Dependency direction is top -> subsystems.
_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DOCK = os.path.join(_REPO, "xsphere-camera-dock")
if _DOCK not in sys.path:
    sys.path.insert(0, _DOCK)

from camera_dock import webapp  # noqa: E402  (after sys.path wiring)


_DASHBOARD = """<!doctype html>
<html><head><meta charset="utf-8"><title>xsphere-daq fast control</title>
<style>
  body { margin:0; background:#111; color:#ddd; font-family:system-ui,sans-serif; }
  header { padding:12px 18px; background:#000; font-size:18px; }
  .sub { color:#888; font-size:13px; }
  .grid { display:flex; flex-wrap:wrap; gap:16px; padding:18px; }
  .tile { background:#1a1a1a; border:1px solid #333; border-radius:8px; padding:16px 20px; min-width:220px; }
  .tile h3 { margin:0 0 6px; } a { color:#8cf; text-decoration:none; } a:hover { text-decoration:underline; }
  .muted { color:#666; } .muted h3 { color:#888; }
</style></head>
<body>
  <header><b>xsphere-daq</b> &mdash; fast control
    <div class="sub">cameras and other fast-control subsystems · slow control is a separate system</div></header>
  <div class="grid">
    <div class="tile"><h3><a href="/cameras/">Cameras &rarr;</a></h3>
      <div>live streams · exposure / gain / ROI · recording · presets</div></div>
    <div class="tile muted"><h3>More subsystems</h3>
      <div>future fast-control subsystems mount here</div></div>
  </div>
</body></html>"""


def create_panel(sessions: dict):
    """Build the top-level FastAPI panel: dashboard at / + camera dock at /cameras."""
    from contextlib import asynccontextmanager

    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse

    cam_app = webapp.create_app(sessions, manage_lifecycle=False)

    @asynccontextmanager
    async def lifespan(app):
        webapp.start_all(sessions)        # bring the rig up
        try:
            yield
        finally:
            webapp.stop_all(sessions)

    app = FastAPI(lifespan=lifespan, title="xsphere-daq fast control")

    @app.get("/")
    def dashboard():
        return HTMLResponse(_DASHBOARD)

    app.mount("/cameras", cam_app)
    return app


def serve(camera_names, host: str = "127.0.0.1", port: int = 8000) -> None:
    import uvicorn
    sessions = {n: webapp.CameraSession(n, webapp._make_camera(n)) for n in camera_names}
    uvicorn.run(create_panel(sessions), host=host, port=port)


def main() -> None:
    parser = argparse.ArgumentParser(description="Launch the xsphere-daq fast-control panel.")
    parser.add_argument("cameras", nargs="+", choices=["basler", "zelux", "hayear"],
                        help="cameras to bring up")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    serve(args.cameras, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
