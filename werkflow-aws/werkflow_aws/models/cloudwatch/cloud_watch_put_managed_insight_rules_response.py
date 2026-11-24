from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_partial_failure import CloudWatchPartialFailure


class CloudWatchPutManagedInsightRulesResponse(BaseModel):
    Failures: list[CloudWatchPartialFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
