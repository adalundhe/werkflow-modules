from __future__ import annotations
from pydantic import BaseModel
from .glue_trigger import GlueTrigger


class GlueTriggerNodeDetails(BaseModel):
    Trigger: GlueTrigger | None = None
