from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDataSourceRunLineageSummary(BaseModel):
    importStatus: StrictStr | None = None
