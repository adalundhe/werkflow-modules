from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_smb_local_groups import StorageGatewaySMBLocalGroups


class StorageGatewayUpdateSMBLocalGroupsRequest(BaseModel):
    GatewayARN: StrictStr
    SMBLocalGroups: StorageGatewaySMBLocalGroups
