from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KendraDeletePrincipalMappingRequest(BaseModel):
    IndexId: StrictStr
    GroupId: StrictStr
    DataSourceId: StrictStr | None = None
    OrderingId: StrictInt | None = None
