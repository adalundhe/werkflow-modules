from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_created_by_info import ConnectCreatedByInfo
from .connect_download_url_metadata import ConnectDownloadUrlMetadata


class ConnectGetAttachedFileResponse(BaseModel):
    FileArn: StrictStr | None = None
    FileId: StrictStr | None = None
    CreationTime: StrictStr | None = None
    FileStatus: StrictStr | None = None
    FileName: StrictStr | None = None
    FileSizeInBytes: StrictInt | None = None
    AssociatedResourceArn: StrictStr | None = None
    FileUseCaseType: StrictStr | None = None
    CreatedBy: ConnectCreatedByInfo | None = None
    DownloadUrlMetadata: ConnectDownloadUrlMetadata | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
