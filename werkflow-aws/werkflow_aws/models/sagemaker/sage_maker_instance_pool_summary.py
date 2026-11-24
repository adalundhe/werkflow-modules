from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_production_variant_instance_type import SageMakerProductionVariantInstanceType


class SageMakerInstancePoolSummary(BaseModel):
    InstanceType: SageMakerProductionVariantInstanceType | None = None
    CurrentInstanceCount: StrictInt | None = None
