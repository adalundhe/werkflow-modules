from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_serverless_ingestion_job_source import OpenSearchServerlessIngestionJobSource
from .open_search_serverless_tag import OpenSearchServerlessTag


class OpenSearchServerlessCreateIngestionJobRequest(BaseModel):
    collectionId: StrictStr
    ingestionJobName: StrictStr
    indexName: StrictStr
    source: OpenSearchServerlessIngestionJobSource
    failureIndexName: StrictStr | None = None
    tags: list[OpenSearchServerlessTag] | None = None
    clientToken: StrictStr | None = None
