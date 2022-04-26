from __future__ import annotations

from types import TracebackType
from typing import Optional, Type

import atoti as tt

from .config import Config
from .load_tables import load_tables
from .start_session import start_session


class App:
    """Regroup the session with other resources so that they can be closed together."""

    def __init__(self, *, config: Config) -> None:
        # The config is kept private to deter passing an App to functions when a Config is all they need.
        self._session = start_session(config=config)
        load_tables(self.session, config=config)

    @property
    def session(self) -> tt.Session:
        return self._session

    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> App:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        self.close()
