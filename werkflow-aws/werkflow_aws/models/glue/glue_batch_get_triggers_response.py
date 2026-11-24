from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_trigger import GlueTrigger


class GlueBatchGetTriggersResponse(BaseModel):
    Triggers: list[GlueTrigger] | None = None
    TriggersNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
