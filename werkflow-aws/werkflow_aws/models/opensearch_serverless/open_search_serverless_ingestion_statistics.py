from __future__ import annotations
from pydantic import BaseModel
from .open_search_serverless_s3_statistics import OpenSearchServerlessS3Statistics


class OpenSearchServerlessIngestionStatistics(BaseModel):
    s3: OpenSearchServerlessS3Statistics | None = None
