from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_dashboard_validation_message import CloudWatchDashboardValidationMessage


class CloudWatchPutDashboardResponse(BaseModel):
    DashboardValidationMessages: list[CloudWatchDashboardValidationMessage] | None = None
    ResponseMetadata: dict[str, Any] | None = None
