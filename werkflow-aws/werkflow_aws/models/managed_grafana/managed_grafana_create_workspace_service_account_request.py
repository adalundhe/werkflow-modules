from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ManagedGrafanaCreateWorkspaceServiceAccountRequest(BaseModel):
    name: StrictStr
    grafanaRole: Literal['ADMIN', 'EDITOR', 'VIEWER']
    workspaceId: StrictStr
