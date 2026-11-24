from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dev_ops_guru_service_integration_config import DevOpsGuruServiceIntegrationConfig


class DevOpsGuruDescribeServiceIntegrationResponse(BaseModel):
    ServiceIntegration: DevOpsGuruServiceIntegrationConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
