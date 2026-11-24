from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_default_ebs_storage_settings import SageMakerDefaultEbsStorageSettings


class SageMakerDefaultSpaceStorageSettings(BaseModel):
    DefaultEbsStorageSettings: SageMakerDefaultEbsStorageSettings | None = None
