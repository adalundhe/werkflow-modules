from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_daemon_detail import ECSDaemonDetail


class ECSDescribeDaemonResponse(BaseModel):
    daemon: ECSDaemonDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
