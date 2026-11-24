from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchListDataSourcesRequest(BaseModel):
    DomainName: StrictStr
