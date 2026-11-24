from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class APIGatewayV2Cors(BaseModel):
    AllowCredentials: StrictBool | None = None
    AllowHeaders: list[StrictStr] | None = None
    AllowMethods: list[StrictStr] | None = None
    AllowOrigins: list[StrictStr] | None = None
    ExposeHeaders: list[StrictStr] | None = None
    MaxAge: StrictInt | None = None
