from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_dry_run_result import CloudWatchLogsDryRunResult


class CloudWatchLogsDeleteAccountPolicyResponse(BaseModel):
    dryRunResult: CloudWatchLogsDryRunResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
