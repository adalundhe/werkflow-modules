from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .storage_gateway_smb_file_share_info import StorageGatewaySMBFileShareInfo


class StorageGatewayDescribeSMBFileSharesResponse(BaseModel):
    SMBFileShareInfoList: list[StorageGatewaySMBFileShareInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
