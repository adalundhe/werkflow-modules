from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayV2ImportApiRequest(BaseModel):
    Body: StrictStr
    Basepath: StrictStr | None = None
    FailOnWarnings: StrictBool | None = None
