from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_ebs_storage_settings import SageMakerEbsStorageSettings


class SageMakerSpaceStorageSettings(BaseModel):
    EbsStorageSettings: SageMakerEbsStorageSettings | None = None
