from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_monitored_resource_identifier import DevOpsGuruMonitoredResourceIdentifier


class DevOpsGuruListMonitoredResourcesResponse(BaseModel):
    MonitoredResourceIdentifiers: list[DevOpsGuruMonitoredResourceIdentifier] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
