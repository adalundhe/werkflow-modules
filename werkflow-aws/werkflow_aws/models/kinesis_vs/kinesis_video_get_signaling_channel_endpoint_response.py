from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_video_resource_endpoint_list_item import KinesisVideoResourceEndpointListItem


class KinesisVideoGetSignalingChannelEndpointResponse(BaseModel):
    ResourceEndpointList: list[KinesisVideoResourceEndpointListItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
