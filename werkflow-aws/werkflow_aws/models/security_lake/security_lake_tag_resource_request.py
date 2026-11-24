from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_tag import SecurityLakeTag


class SecurityLakeTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[SecurityLakeTag]
