from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStartExportLabelsTaskRunRequest(BaseModel):
    TransformId: StrictStr
    OutputS3Path: StrictStr
