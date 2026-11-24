from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_crawler import GlueCrawler


class GlueGetCrawlerResponse(BaseModel):
    Crawler: GlueCrawler | None = None
    ResponseMetadata: dict[str, Any] | None = None
