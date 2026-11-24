from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_connection_group_summary import CloudFrontConnectionGroupSummary


class CloudFrontListConnectionGroupsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    ConnectionGroups: list[CloudFrontConnectionGroupSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
