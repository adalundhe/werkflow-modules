from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3CORSRule(BaseModel):
    ID: StrictStr | None = None
    AllowedHeaders: list[StrictStr] | None = None
    AllowedMethods: list[StrictStr] | None = None
    AllowedOrigins: list[StrictStr] | None = None
    ExposeHeaders: list[StrictStr] | None = None
    MaxAgeSeconds: StrictInt | None = None
