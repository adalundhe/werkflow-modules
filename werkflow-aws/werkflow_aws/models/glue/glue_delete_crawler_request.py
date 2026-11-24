from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteCrawlerRequest(BaseModel):
    Name: StrictStr
