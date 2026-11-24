from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_brand_summary import QuickSightBrandSummary


class QuickSightListBrandsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Brands: list[QuickSightBrandSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
