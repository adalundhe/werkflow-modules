from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .dms_processed_object import DMSProcessedObject


class DMSProgress(BaseModel):
    ProgressPercent: StrictFloat | StrictInt | None = None
    TotalObjects: StrictInt | None = None
    ProgressStep: StrictStr | None = None
    ProcessedObject: DMSProcessedObject | None = None
