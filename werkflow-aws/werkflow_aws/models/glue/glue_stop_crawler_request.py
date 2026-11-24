from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStopCrawlerRequest(BaseModel):
    Name: StrictStr
