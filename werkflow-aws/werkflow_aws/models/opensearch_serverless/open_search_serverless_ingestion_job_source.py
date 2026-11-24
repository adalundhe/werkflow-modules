from __future__ import annotations
from pydantic import BaseModel
from .open_search_serverless_ingestion_job_s3_source import OpenSearchServerlessIngestionJobS3Source


class OpenSearchServerlessIngestionJobSource(BaseModel):
    s3: OpenSearchServerlessIngestionJobS3Source | None = None
