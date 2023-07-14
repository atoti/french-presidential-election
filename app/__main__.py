from __future__ import annotations

import logging

from . import App, Config

config = Config()

with App(config=config) as app:
    logging.info(f"Session listening on port {app.session.port}")
    app.session.wait()
