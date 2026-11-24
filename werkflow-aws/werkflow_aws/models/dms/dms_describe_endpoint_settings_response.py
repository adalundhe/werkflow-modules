from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_endpoint_setting import DMSEndpointSetting


class DMSDescribeEndpointSettingsResponse(BaseModel):
    Marker: StrictStr | None = None
    EndpointSettings: list[DMSEndpointSetting] | None = None
    ResponseMetadata: dict[str, Any] | None = None
