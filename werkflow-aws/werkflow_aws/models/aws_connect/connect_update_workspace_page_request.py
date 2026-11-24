from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateWorkspacePageRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
    Page: StrictStr
    NewPage: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    Slug: StrictStr | None = None
    InputData: StrictStr | None = None
