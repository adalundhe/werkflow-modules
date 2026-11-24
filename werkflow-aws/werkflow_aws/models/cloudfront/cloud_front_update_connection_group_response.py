from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_connection_group import CloudFrontConnectionGroup


class CloudFrontUpdateConnectionGroupResponse(BaseModel):
    ConnectionGroup: CloudFrontConnectionGroup | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
