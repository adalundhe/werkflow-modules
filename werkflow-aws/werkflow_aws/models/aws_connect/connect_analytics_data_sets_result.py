from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAnalyticsDataSetsResult(BaseModel):
    DataSetId: StrictStr | None = None
    DataSetName: StrictStr | None = None
