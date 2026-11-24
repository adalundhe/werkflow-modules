from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportJobFolderOverrideParameters(BaseModel):
    FolderId: StrictStr | None = None
    Name: StrictStr | None = None
    ParentFolderArn: StrictStr | None = None
