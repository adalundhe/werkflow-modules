from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .managed_grafana_update_instruction import ManagedGrafanaUpdateInstruction


class ManagedGrafanaUpdateError(BaseModel):
    code: StrictInt | None = None
    message: StrictStr | None = None
    causedBy: ManagedGrafanaUpdateInstruction | None = None
