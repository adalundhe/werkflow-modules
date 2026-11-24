from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecs_daemon_summary import ECSDaemonSummary


class ECSListDaemonsResponse(BaseModel):
    daemonSummariesList: list[ECSDaemonSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
