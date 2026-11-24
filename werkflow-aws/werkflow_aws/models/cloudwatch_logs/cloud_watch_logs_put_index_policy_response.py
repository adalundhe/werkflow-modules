from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_index_policy import CloudWatchLogsIndexPolicy


class CloudWatchLogsPutIndexPolicyResponse(BaseModel):
    indexPolicy: CloudWatchLogsIndexPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
