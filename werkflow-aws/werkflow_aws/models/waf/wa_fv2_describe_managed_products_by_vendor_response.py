from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_managed_product_descriptor import WAFv2ManagedProductDescriptor


class WAFv2DescribeManagedProductsByVendorResponse(BaseModel):
    ManagedProducts: list[WAFv2ManagedProductDescriptor] | None = None
    ResponseMetadata: dict[str, Any] | None = None
