from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_anycast_ip_list_collection import CloudFrontAnycastIpListCollection


class CloudFrontListAnycastIpListsResponse(BaseModel):
    AnycastIpLists: CloudFrontAnycastIpListCollection | None = None
    ResponseMetadata: dict[str, Any] | None = None
