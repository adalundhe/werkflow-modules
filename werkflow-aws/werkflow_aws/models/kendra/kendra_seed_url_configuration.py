from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraSeedUrlConfiguration(BaseModel):
    SeedUrls: list[StrictStr] | None = None
    WebCrawlerMode: StrictStr | None = None
