from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionSegmentTypeInfo(BaseModel):
    Type: StrictStr | None = None
    ModelVersion: StrictStr | None = None
