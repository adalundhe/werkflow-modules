from __future__ import annotations
from pydantic import BaseModel
from .glue_crawl import GlueCrawl


class GlueCrawlerNodeDetails(BaseModel):
    Crawls: list[GlueCrawl] | None = None
