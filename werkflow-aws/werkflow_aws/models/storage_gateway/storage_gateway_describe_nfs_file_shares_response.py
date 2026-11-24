from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .storage_gateway_nfs_file_share_info import StorageGatewayNFSFileShareInfo


class StorageGatewayDescribeNFSFileSharesResponse(BaseModel):
    NFSFileShareInfoList: list[StorageGatewayNFSFileShareInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
