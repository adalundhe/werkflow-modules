from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .storage_gateway_file_system_association_info import StorageGatewayFileSystemAssociationInfo


class StorageGatewayDescribeFileSystemAssociationsResponse(BaseModel):
    FileSystemAssociationInfoList: list[StorageGatewayFileSystemAssociationInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
