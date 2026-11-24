from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchDeleteIndexFieldRequest(BaseModel):
    DomainName: StrictStr
    IndexFieldName: StrictStr
