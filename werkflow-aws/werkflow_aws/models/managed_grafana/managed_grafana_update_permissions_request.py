from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .managed_grafana_update_instruction import ManagedGrafanaUpdateInstruction


class ManagedGrafanaUpdatePermissionsRequest(BaseModel):
    updateInstructionBatch: list[ManagedGrafanaUpdateInstruction]
    workspaceId: StrictStr
