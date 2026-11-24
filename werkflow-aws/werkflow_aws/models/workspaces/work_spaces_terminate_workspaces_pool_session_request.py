from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesTerminateWorkspacesPoolSessionRequest(BaseModel):
    SessionId: StrictStr
