from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesDeleteClientBrandingRequest(BaseModel):
    ResourceId: StrictStr
    Platforms: list[Literal['DeviceTypeWindows', 'DeviceTypeOsx', 'DeviceTypeAndroid', 'DeviceTypeIos', 'DeviceTypeLinux', 'DeviceTypeWeb']]
