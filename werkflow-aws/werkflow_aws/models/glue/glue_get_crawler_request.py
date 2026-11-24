from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetCrawlerRequest(BaseModel):
    Name: StrictStr
