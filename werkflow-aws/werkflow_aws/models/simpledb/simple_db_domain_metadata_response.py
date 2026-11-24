from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class SimpleDBDomainMetadataResponse(BaseModel):
    ItemCount: StrictInt | None = None
    ItemNamesSizeBytes: StrictInt | None = None
    AttributeNameCount: StrictInt | None = None
    AttributeNamesSizeBytes: StrictInt | None = None
    AttributeValueCount: StrictInt | None = None
    AttributeValuesSizeBytes: StrictInt | None = None
    Timestamp: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
