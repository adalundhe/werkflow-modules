from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_access_endpoint_config import WorkSpacesAccessEndpointConfig


class WorkSpacesWorkspaceAccessProperties(BaseModel):
    DeviceTypeWindows: StrictStr | None = None
    DeviceTypeOsx: StrictStr | None = None
    DeviceTypeWeb: StrictStr | None = None
    DeviceTypeIos: StrictStr | None = None
    DeviceTypeAndroid: StrictStr | None = None
    DeviceTypeChromeOs: StrictStr | None = None
    DeviceTypeZeroClient: StrictStr | None = None
    DeviceTypeLinux: StrictStr | None = None
    DeviceTypeWorkSpacesThinClient: StrictStr | None = None
    AccessEndpointConfig: WorkSpacesAccessEndpointConfig | None = None
