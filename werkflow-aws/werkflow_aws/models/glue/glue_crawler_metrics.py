from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class GlueCrawlerMetrics(BaseModel):
    CrawlerName: StrictStr | None = None
    TimeLeftSeconds: StrictFloat | StrictInt | None = None
    StillEstimating: StrictBool | None = None
    LastRuntimeSeconds: StrictFloat | StrictInt | None = None
    MedianRuntimeSeconds: StrictFloat | StrictInt | None = None
    TablesCreated: StrictInt | None = None
    TablesUpdated: StrictInt | None = None
    TablesDeleted: StrictInt | None = None
