from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_created_by_info import ConnectCreatedByInfo
from .connect_upload_url_metadata import ConnectUploadUrlMetadata


class ConnectStartAttachedFileUploadResponse(BaseModel):
    FileArn: StrictStr | None = None
    FileId: StrictStr | None = None
    CreationTime: StrictStr | None = None
    FileStatus: StrictStr | None = None
    CreatedBy: ConnectCreatedByInfo | None = None
    UploadUrlMetadata: ConnectUploadUrlMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None
