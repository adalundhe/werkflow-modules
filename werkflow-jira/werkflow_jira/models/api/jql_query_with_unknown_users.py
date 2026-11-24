from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JQLQueryWithUnknownUsers(BaseModel):
    convertedQuery: StrictStr | None = None
    originalQuery: StrictStr | None = None
