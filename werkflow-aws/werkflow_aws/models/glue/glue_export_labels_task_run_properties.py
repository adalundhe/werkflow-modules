from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueExportLabelsTaskRunProperties(BaseModel):
    OutputS3Path: StrictStr | None = None
