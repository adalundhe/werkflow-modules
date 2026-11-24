from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCondition(BaseModel):
    LogicalOperator: StrictStr | None = None
    JobName: StrictStr | None = None
    State: StrictStr | None = None
    CrawlerName: StrictStr | None = None
    CrawlState: StrictStr | None = None
