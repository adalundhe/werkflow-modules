from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_file_share_info import StorageGatewayFileShareInfo


class StorageGatewayListFileSharesResponse(BaseModel):
    Marker: StrictStr | None = None
    NextMarker: StrictStr | None = None
    FileShareInfoList: list[StorageGatewayFileShareInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
