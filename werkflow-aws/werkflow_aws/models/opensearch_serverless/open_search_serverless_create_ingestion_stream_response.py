from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_ingestion_stream_detail import OpenSearchServerlessIngestionStreamDetail


class OpenSearchServerlessCreateIngestionStreamResponse(BaseModel):
    ingestionStreamDetail: OpenSearchServerlessIngestionStreamDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
