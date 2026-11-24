from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayListTagsForResourceResponse(BaseModel):
    ResourceARN: StrictStr | None = None
    Marker: StrictStr | None = None
    Tags: list[StorageGatewayTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
