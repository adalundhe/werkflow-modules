from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission
from .quick_sight_tag import QuickSightTag


class QuickSightCreateFolderRequest(BaseModel):
    AwsAccountId: StrictStr
    FolderId: StrictStr
    Name: StrictStr | None = None
    FolderType: Literal['SHARED', 'RESTRICTED'] | None = None
    ParentFolderArn: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    Tags: list[QuickSightTag] | None = None
    SharingModel: Literal['ACCOUNT', 'NAMESPACE'] | None = None
