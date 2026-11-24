from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_file_system_association_summary import StorageGatewayFileSystemAssociationSummary


class StorageGatewayListFileSystemAssociationsResponse(BaseModel):
    Marker: StrictStr | None = None
    NextMarker: StrictStr | None = None
    FileSystemAssociationSummaryList: list[StorageGatewayFileSystemAssociationSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
