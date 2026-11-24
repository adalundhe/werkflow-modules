from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueStartImportLabelsTaskRunRequest(BaseModel):
    TransformId: StrictStr
    InputS3Path: StrictStr
    ReplaceAllLabels: StrictBool | None = None
