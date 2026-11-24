from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .storage_gateway_smb_local_groups import StorageGatewaySMBLocalGroups


class StorageGatewayDescribeSMBSettingsResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    DomainName: StrictStr | None = None
    ActiveDirectoryStatus: StrictStr | None = None
    SMBGuestPasswordSet: StrictBool | None = None
    SMBSecurityStrategy: StrictStr | None = None
    FileSharesVisible: StrictBool | None = None
    SMBLocalGroups: StorageGatewaySMBLocalGroups | None = None
    ResponseMetadata: dict[str, Any] | None = None
