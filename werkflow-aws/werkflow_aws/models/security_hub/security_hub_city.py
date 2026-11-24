from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubCity(BaseModel):
    CityName: StrictStr | None = None
