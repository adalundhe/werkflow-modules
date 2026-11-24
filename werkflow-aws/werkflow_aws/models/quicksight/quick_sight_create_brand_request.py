from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_brand_definition import QuickSightBrandDefinition
from .quick_sight_tag import QuickSightTag


class QuickSightCreateBrandRequest(BaseModel):
    AwsAccountId: StrictStr
    BrandId: StrictStr
    BrandDefinition: QuickSightBrandDefinition | None = None
    Tags: list[QuickSightTag] | None = None
