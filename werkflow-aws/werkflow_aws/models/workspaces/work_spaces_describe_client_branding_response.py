from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_default_client_branding_attributes import WorkSpacesDefaultClientBrandingAttributes
from .work_spaces_ios_client_branding_attributes import WorkSpacesIosClientBrandingAttributes


class WorkSpacesDescribeClientBrandingResponse(BaseModel):
    DeviceTypeWindows: WorkSpacesDefaultClientBrandingAttributes | None = None
    DeviceTypeOsx: WorkSpacesDefaultClientBrandingAttributes | None = None
    DeviceTypeAndroid: WorkSpacesDefaultClientBrandingAttributes | None = None
    DeviceTypeIos: WorkSpacesIosClientBrandingAttributes | None = None
    DeviceTypeLinux: WorkSpacesDefaultClientBrandingAttributes | None = None
    DeviceTypeWeb: WorkSpacesDefaultClientBrandingAttributes | None = None
    ResponseMetadata: dict[str, Any] | None = None
