from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightBigQueryParameters(BaseModel):
    ProjectId: StrictStr | None = None
    DataSetRegion: StrictStr | None = None
