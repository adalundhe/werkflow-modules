from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .target_to_sources_mapping import TargetToSourcesMapping


class IssueBulkMovePayload(BaseModel):
    sendBulkNotification: StrictBool | None = None
    targetToSourcesMapping: dict[StrictStr, TargetToSourcesMapping] | None = None
