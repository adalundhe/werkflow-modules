from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFrontDomainItem(BaseModel):
    Domain: StrictStr
    ServeOn: Literal['any', 'anycast-ip-list-only'] | None = None
