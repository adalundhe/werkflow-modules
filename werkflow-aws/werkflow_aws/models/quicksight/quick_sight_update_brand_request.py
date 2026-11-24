from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_brand_definition import QuickSightBrandDefinition


class QuickSightUpdateBrandRequest(BaseModel):
    AwsAccountId: StrictStr
    BrandId: StrictStr
    BrandDefinition: QuickSightBrandDefinition | None = None
