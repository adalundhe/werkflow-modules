from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightFolderSummary(BaseModel):
    Arn: StrictStr | None = None
    FolderId: StrictStr | None = None
    Name: StrictStr | None = None
    FolderType: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    SharingModel: StrictStr | None = None
