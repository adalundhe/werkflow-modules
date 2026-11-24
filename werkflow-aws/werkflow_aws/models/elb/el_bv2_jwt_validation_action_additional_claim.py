from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2JwtValidationActionAdditionalClaim(BaseModel):
    Format: StrictStr | None = None
    Name: StrictStr | None = None
    Values: list[StrictStr] | None = None
