from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_tape_archive import StorageGatewayTapeArchive


class StorageGatewayDescribeTapeArchivesResponse(BaseModel):
    TapeArchives: list[StorageGatewayTapeArchive] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
