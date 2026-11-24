from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudSearchDescribeSuggestersRequest(BaseModel):
    DomainName: StrictStr
    SuggesterNames: list[StrictStr] | None = None
    Deployed: StrictBool | None = None
