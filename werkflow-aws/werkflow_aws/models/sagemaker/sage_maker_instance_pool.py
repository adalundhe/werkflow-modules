from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_production_variant_instance_type import SageMakerProductionVariantInstanceType


class SageMakerInstancePool(BaseModel):
    InstanceType: SageMakerProductionVariantInstanceType | None = None
    ModelNameOverride: StrictStr | None = None
    Priority: StrictInt | None = None
