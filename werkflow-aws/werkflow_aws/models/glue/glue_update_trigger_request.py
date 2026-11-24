from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_trigger_update import GlueTriggerUpdate


class GlueUpdateTriggerRequest(BaseModel):
    Name: StrictStr
    TriggerUpdate: GlueTriggerUpdate
