from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DisplayContent(BaseModel):
    Body: StrictStr | None = None
    Title: StrictStr | None = None
