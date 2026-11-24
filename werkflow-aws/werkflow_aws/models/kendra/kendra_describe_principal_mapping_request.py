from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDescribePrincipalMappingRequest(BaseModel):
    IndexId: StrictStr
    GroupId: StrictStr
    DataSourceId: StrictStr | None = None
