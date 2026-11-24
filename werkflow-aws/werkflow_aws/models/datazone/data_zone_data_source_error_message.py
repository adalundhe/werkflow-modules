from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDataSourceErrorMessage(BaseModel):
    errorType: StrictStr | None = None
    errorDetail: StrictStr | None = None
