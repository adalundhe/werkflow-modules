from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails(BaseModel):
    Hostname: StrictStr | None = None
    IpAddress: StrictStr | None = None
