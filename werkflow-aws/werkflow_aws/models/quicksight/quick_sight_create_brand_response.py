from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_brand_definition import QuickSightBrandDefinition
from .quick_sight_brand_detail import QuickSightBrandDetail


class QuickSightCreateBrandResponse(BaseModel):
    RequestId: StrictStr | None = None
    BrandDetail: QuickSightBrandDetail | None = None
    BrandDefinition: QuickSightBrandDefinition | None = None
    ResponseMetadata: dict[str, Any] | None = None
