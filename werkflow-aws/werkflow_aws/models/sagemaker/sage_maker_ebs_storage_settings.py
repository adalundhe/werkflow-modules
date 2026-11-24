from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerEbsStorageSettings(BaseModel):
    EbsVolumeSizeInGb: StrictInt | None = None
