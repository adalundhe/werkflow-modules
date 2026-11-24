from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_created_by_info import ConnectCreatedByInfo


class ConnectAttachedFile(BaseModel):
    CreationTime: StrictStr | None = None
    FileArn: StrictStr | None = None
    FileId: StrictStr | None = None
    FileName: StrictStr | None = None
    FileSizeInBytes: StrictInt | None = None
    FileStatus: StrictStr | None = None
    CreatedBy: ConnectCreatedByInfo | None = None
    FileUseCaseType: StrictStr | None = None
    AssociatedResourceArn: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
