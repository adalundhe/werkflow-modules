from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyCountry(BaseModel):
    CountryCode: StrictStr | None = None
    CountryName: StrictStr | None = None
