from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceGcpConnectorConfiguration(BaseModel):
    gcpOrganizationId: StrictStr | None = None
    serviceAccountEmail: StrictStr | None = None
    workloadIdentityPoolProvider: StrictStr | None = None
