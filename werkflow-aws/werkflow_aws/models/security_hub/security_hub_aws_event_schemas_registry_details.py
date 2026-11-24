from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEventSchemasRegistryDetails(BaseModel):
    Description: StrictStr | None = None
    RegistryArn: StrictStr | None = None
    RegistryName: StrictStr | None = None
