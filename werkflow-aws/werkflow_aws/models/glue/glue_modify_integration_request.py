from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_integration_config import GlueIntegrationConfig


class GlueModifyIntegrationRequest(BaseModel):
    IntegrationIdentifier: StrictStr
    Description: StrictStr | None = None
    DataFilter: StrictStr | None = None
    IntegrationConfig: GlueIntegrationConfig | None = None
    IntegrationName: StrictStr | None = None
