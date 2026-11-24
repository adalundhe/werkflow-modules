from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSResource(BaseModel):
    URI: StrictStr | None = None
    AccountId: StrictStr | None = None
