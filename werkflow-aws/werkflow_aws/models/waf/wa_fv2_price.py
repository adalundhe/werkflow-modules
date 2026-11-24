from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2Price(BaseModel):
    Amount: StrictStr | None = None
    Currency: StrictStr | None = None
