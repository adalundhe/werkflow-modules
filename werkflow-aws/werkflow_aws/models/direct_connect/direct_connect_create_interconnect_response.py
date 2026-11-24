from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .direct_connect_mac_sec_key import DirectConnectMacSecKey
from .direct_connect_tag import DirectConnectTag


class DirectConnectCreateInterconnectResponse(BaseModel):
    interconnectId: StrictStr | None = None
    interconnectName: StrictStr | None = None
    interconnectState: StrictStr | None = None
    region: StrictStr | None = None
    location: StrictStr | None = None
    bandwidth: StrictStr | None = None
    loaIssueTime: datetime.datetime | StrictStr | None = None
    lagId: StrictStr | None = None
    awsDevice: StrictStr | None = None
    jumboFrameCapable: StrictBool | None = None
    awsDeviceV2: StrictStr | None = None
    awsLogicalDeviceId: StrictStr | None = None
    hasLogicalRedundancy: StrictStr | None = None
    tags: list[DirectConnectTag] | None = None
    providerName: StrictStr | None = None
    macSecCapable: StrictBool | None = None
    portEncryptionStatus: StrictStr | None = None
    encryptionMode: StrictStr | None = None
    macSecKeys: list[DirectConnectMacSecKey] | None = None
    ResponseMetadata: dict[str, Any] | None = None
