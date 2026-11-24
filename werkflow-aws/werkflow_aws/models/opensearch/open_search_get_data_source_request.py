from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchGetDataSourceRequest(BaseModel):
    DomainName: StrictStr
    Name: StrictStr
