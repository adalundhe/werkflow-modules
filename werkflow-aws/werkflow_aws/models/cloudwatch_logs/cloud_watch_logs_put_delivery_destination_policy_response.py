from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_policy import CloudWatchLogsPolicy


class CloudWatchLogsPutDeliveryDestinationPolicyResponse(BaseModel):
    policy: CloudWatchLogsPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
