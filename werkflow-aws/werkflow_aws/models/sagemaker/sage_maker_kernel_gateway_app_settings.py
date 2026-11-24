from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_custom_image import SageMakerCustomImage
from .sage_maker_resource_spec import SageMakerResourceSpec


class SageMakerKernelGatewayAppSettings(BaseModel):
    DefaultResourceSpec: SageMakerResourceSpec | None = None
    CustomImages: list[SageMakerCustomImage] | None = None
    LifecycleConfigArns: list[StrictStr] | None = None
