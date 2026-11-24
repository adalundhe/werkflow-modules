from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2StatusException(BaseModel):
    Exception: StrictStr | None = None
    Message: StrictStr | None = None
