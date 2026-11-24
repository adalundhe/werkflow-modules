from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_default_import_client_branding_attributes import WorkSpacesDefaultImportClientBrandingAttributes
from .work_spaces_ios_import_client_branding_attributes import WorkSpacesIosImportClientBrandingAttributes


class WorkSpacesImportClientBrandingRequest(BaseModel):
    ResourceId: StrictStr
    DeviceTypeWindows: WorkSpacesDefaultImportClientBrandingAttributes | None = None
    DeviceTypeOsx: WorkSpacesDefaultImportClientBrandingAttributes | None = None
    DeviceTypeAndroid: WorkSpacesDefaultImportClientBrandingAttributes | None = None
    DeviceTypeIos: WorkSpacesIosImportClientBrandingAttributes | None = None
    DeviceTypeLinux: WorkSpacesDefaultImportClientBrandingAttributes | None = None
    DeviceTypeWeb: WorkSpacesDefaultImportClientBrandingAttributes | None = None
