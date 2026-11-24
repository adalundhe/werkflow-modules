from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SecurityHubAwsCorsConfiguration(BaseModel):
    AllowOrigins: list[StrictStr] | None = None
    AllowCredentials: StrictBool | None = None
    ExposeHeaders: list[StrictStr] | None = None
    MaxAge: StrictInt | None = None
    AllowMethods: list[StrictStr] | None = None
    AllowHeaders: list[StrictStr] | None = None
