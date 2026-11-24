from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3CORSRuleInput(BaseModel):
    AllowedMethods: list[StrictStr]
    AllowedOrigins: list[StrictStr]
    ID: StrictStr | None = None
    AllowedHeaders: list[StrictStr] | None = None
    ExposeHeaders: list[StrictStr] | None = None
    MaxAgeSeconds: StrictInt | None = None
