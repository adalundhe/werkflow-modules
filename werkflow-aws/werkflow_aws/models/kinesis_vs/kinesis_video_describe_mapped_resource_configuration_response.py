from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_video_mapped_resource_configuration_list_item import KinesisVideoMappedResourceConfigurationListItem


class KinesisVideoDescribeMappedResourceConfigurationResponse(BaseModel):
    MappedResourceConfigurationList: list[KinesisVideoMappedResourceConfigurationListItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
