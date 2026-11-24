from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_trigger import GlueTrigger


class GlueUpdateTriggerResponse(BaseModel):
    Trigger: GlueTrigger | None = None
    ResponseMetadata: dict[str, Any] | None = None
