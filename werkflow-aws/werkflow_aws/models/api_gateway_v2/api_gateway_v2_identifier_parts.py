from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2IdentifierParts(BaseModel):
    Method: StrictStr | None = None
    Path: StrictStr | None = None
    RestApiId: StrictStr | None = None
    Stage: StrictStr | None = None
