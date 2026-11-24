from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ManagedGrafanaDescribeWorkspaceConfigurationResponse(BaseModel):
    configuration: StrictStr | None = None
    grafanaVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
