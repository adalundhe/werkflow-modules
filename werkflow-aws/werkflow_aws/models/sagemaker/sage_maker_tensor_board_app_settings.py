from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_resource_spec import SageMakerResourceSpec


class SageMakerTensorBoardAppSettings(BaseModel):
    DefaultResourceSpec: SageMakerResourceSpec | None = None
