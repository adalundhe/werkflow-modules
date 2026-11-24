from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceAzureConnectorConfiguration(BaseModel):
    tenantIdentifier: StrictStr | None = None
    clientIdentifier: StrictStr | None = None
