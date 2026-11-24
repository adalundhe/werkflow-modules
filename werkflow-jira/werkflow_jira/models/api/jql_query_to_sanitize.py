from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JqlQueryToSanitize(BaseModel):
    accountId: StrictStr | None = None
    query: StrictStr | None = None
