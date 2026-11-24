from __future__ import annotations
from pydantic import BaseModel
from .open_search_serverless_ingestion_stream_s3_source import OpenSearchServerlessIngestionStreamS3Source


class OpenSearchServerlessIngestionStreamSource(BaseModel):
    s3: OpenSearchServerlessIngestionStreamS3Source | None = None
