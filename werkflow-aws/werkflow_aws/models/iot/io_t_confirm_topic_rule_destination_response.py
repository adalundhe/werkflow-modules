from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class IoTConfirmTopicRuleDestinationResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
