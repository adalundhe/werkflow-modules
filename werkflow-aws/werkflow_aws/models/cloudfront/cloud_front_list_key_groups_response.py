from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_key_group_list import CloudFrontKeyGroupList


class CloudFrontListKeyGroupsResponse(BaseModel):
    KeyGroupList: CloudFrontKeyGroupList | None = None
    ResponseMetadata: dict[str, Any] | None = None
