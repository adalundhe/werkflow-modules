from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListWorkspacePagesRequest(BaseModel):
    InstanceId: StrictStr
    WorkspaceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
