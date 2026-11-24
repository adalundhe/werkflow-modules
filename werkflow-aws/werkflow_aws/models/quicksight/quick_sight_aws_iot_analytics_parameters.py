from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAwsIotAnalyticsParameters(BaseModel):
    DataSetName: StrictStr | None = None
