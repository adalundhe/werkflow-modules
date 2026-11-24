from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_tag import DirectoryServiceTag


class DirectoryServiceAddTagsToResourceRequest(BaseModel):
    ResourceId: StrictStr
    Tags: list[DirectoryServiceTag]
