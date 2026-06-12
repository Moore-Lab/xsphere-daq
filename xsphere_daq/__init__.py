"""xsphere-daq — the fast control system for the xsphere experiment.

Top-level control surface that composes the fast-control subsystems into one web
panel. Cameras (``xsphere-camera-dock``) are the first subsystem; more will be
mounted here as they come online. This is separate from the experiment's slow
control system (``xsphere-slow-control``) — the two are not integrated.

Launch the panel with :mod:`xsphere_daq.panel`.
"""
