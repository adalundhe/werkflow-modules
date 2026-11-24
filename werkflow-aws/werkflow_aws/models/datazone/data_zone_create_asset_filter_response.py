from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_asset_filter_configuration import DataZoneAssetFilterConfiguration


class DataZoneCreateAssetFilterResponse(BaseModel):
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    assetId: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
    configuration: DataZoneAssetFilterConfiguration | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    errorMessage: StrictStr | None = None
    effectiveColumnNames: list[StrictStr] | None = None
    effectiveRowFilter: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
