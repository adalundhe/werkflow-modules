from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontKeyGroupConfig(BaseModel):
    Name: StrictStr | None = None
    Items: list[StrictStr] | None = None
    Comment: StrictStr | None = None
