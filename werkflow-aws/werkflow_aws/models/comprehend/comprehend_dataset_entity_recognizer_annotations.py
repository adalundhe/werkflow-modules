from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDatasetEntityRecognizerAnnotations(BaseModel):
    S3Uri: StrictStr
