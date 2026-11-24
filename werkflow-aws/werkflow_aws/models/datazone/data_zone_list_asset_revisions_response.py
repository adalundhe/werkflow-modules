from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_asset_revision import DataZoneAssetRevision


class DataZoneListAssetRevisionsResponse(BaseModel):
    items: list[DataZoneAssetRevision] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
