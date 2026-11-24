from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDatasetEntityRecognizerEntityList(BaseModel):
    S3Uri: StrictStr
