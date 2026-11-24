from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_crawls_filter import GlueCrawlsFilter


class GlueListCrawlsRequest(BaseModel):
    CrawlerName: StrictStr
    MaxResults: StrictInt | None = None
    Filters: list[GlueCrawlsFilter] | None = None
    NextToken: StrictStr | None = None
