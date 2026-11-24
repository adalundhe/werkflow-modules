from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_vpn_connection_device_type import EC2VpnConnectionDeviceType


class EC2GetVpnConnectionDeviceTypesResponse(BaseModel):
    VpnConnectionDeviceTypes: list[EC2VpnConnectionDeviceType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
