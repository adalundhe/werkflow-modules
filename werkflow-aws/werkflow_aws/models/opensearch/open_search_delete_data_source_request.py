from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDeleteDataSourceRequest(BaseModel):
    DomainName: StrictStr
    Name: StrictStr
