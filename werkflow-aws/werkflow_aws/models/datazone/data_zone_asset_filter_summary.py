from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneAssetFilterSummary(BaseModel):
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    assetId: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
    effectiveColumnNames: list[StrictStr] | None = None
    effectiveRowFilter: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    errorMessage: StrictStr | None = None
