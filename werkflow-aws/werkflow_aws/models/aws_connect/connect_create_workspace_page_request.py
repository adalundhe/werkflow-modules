from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCreateWorkspacePageRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
    ResourceArn: StrictStr
    Page: StrictStr
    Slug: StrictStr | None = None
    InputData: StrictStr | None = None
