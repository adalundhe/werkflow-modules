from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_daemon_revision import ECSDaemonRevision
from .ecs_failure import ECSFailure


class ECSDescribeDaemonRevisionsResponse(BaseModel):
    daemonRevisions: list[ECSDaemonRevision] | None = None
    failures: list[ECSFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
