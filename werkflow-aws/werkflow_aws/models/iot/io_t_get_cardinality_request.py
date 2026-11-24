from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTGetCardinalityRequest(BaseModel):
    queryString: StrictStr
    indexName: StrictStr | None = None
    aggregationField: StrictStr | None = None
    queryVersion: StrictStr | None = None
