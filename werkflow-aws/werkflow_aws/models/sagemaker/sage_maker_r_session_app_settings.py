from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_custom_image import SageMakerCustomImage
from .sage_maker_resource_spec import SageMakerResourceSpec


class SageMakerRSessionAppSettings(BaseModel):
    DefaultResourceSpec: SageMakerResourceSpec | None = None
    CustomImages: list[SageMakerCustomImage] | None = None
