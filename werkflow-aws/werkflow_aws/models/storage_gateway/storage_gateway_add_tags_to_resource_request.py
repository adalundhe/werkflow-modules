from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayAddTagsToResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[StorageGatewayTag]
