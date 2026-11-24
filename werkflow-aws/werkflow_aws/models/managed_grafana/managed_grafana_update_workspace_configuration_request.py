from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaUpdateWorkspaceConfigurationRequest(BaseModel):
    configuration: StrictStr
    workspaceId: StrictStr
    grafanaVersion: StrictStr | None = None
