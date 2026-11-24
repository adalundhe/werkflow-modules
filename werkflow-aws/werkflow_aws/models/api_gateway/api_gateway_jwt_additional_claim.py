from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayJwtAdditionalClaim(BaseModel):
    claimName: StrictStr | None = None
    format: StrictStr | None = None
    required: StrictBool | None = None
    expectedValues: list[StrictStr] | None = None
