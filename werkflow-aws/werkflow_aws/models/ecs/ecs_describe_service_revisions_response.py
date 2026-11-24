from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_failure import ECSFailure
from .ecs_service_revision import ECSServiceRevision


class ECSDescribeServiceRevisionsResponse(BaseModel):
    serviceRevisions: list[ECSServiceRevision] | None = None
    failures: list[ECSFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
