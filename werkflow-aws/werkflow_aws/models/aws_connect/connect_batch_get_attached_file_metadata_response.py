from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_attached_file import ConnectAttachedFile
from .connect_attached_file_error import ConnectAttachedFileError


class ConnectBatchGetAttachedFileMetadataResponse(BaseModel):
    Files: list[ConnectAttachedFile] | None = None
    Errors: list[ConnectAttachedFileError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
