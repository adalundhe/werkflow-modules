from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_compliance import ConfigServiceCompliance


class ConfigServiceComplianceByResource(BaseModel):
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    Compliance: ConfigServiceCompliance | None = None
