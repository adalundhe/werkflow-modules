from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class IoTGetPercentilesRequest(BaseModel):
    queryString: StrictStr
    indexName: StrictStr | None = None
    aggregationField: StrictStr | None = None
    queryVersion: StrictStr | None = None
    percents: list[StrictFloat | StrictInt] | None = None
