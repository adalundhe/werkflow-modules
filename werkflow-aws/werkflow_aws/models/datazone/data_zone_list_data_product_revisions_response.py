from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_data_product_revision import DataZoneDataProductRevision


class DataZoneListDataProductRevisionsResponse(BaseModel):
    items: list[DataZoneDataProductRevision] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
