from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayV2ReimportApiRequest(BaseModel):
    ApiId: StrictStr
    Body: StrictStr
    Basepath: StrictStr | None = None
    FailOnWarnings: StrictBool | None = None
