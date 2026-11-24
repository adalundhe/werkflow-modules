from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_serverless_ingestion_stream_source import OpenSearchServerlessIngestionStreamSource
from .open_search_serverless_tag import OpenSearchServerlessTag


class OpenSearchServerlessCreateIngestionStreamRequest(BaseModel):
    collectionId: StrictStr
    ingestionStreamName: StrictStr
    indexName: StrictStr
    source: OpenSearchServerlessIngestionStreamSource
    roleArn: StrictStr
    failureIndexName: StrictStr | None = None
    tags: list[OpenSearchServerlessTag] | None = None
    clientToken: StrictStr | None = None
