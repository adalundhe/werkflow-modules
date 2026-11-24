from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStartCrawlerRequest(BaseModel):
    Name: StrictStr
