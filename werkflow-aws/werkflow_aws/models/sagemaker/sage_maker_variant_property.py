from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_variant_property_type import SageMakerVariantPropertyType


class SageMakerVariantProperty(BaseModel):
    VariantPropertyType: SageMakerVariantPropertyType
