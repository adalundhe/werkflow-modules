from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class DevOpsGuruRemoveNotificationChannelResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
