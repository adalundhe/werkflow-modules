from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueLabelingSetGenerationTaskRunProperties(BaseModel):
    OutputS3Path: StrictStr | None = None
