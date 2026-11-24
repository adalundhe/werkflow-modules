from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchDeleteSuggesterRequest(BaseModel):
    DomainName: StrictStr
    SuggesterName: StrictStr
