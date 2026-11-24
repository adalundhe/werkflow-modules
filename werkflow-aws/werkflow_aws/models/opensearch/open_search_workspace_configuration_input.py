from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchWorkspaceConfigurationInput(BaseModel):
    name: StrictStr
    workspaceType: StrictStr
