from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerDefaultEbsStorageSettings(BaseModel):
    DefaultEbsVolumeSizeInGb: StrictInt | None = None
    MaximumEbsVolumeSizeInGb: StrictInt | None = None
