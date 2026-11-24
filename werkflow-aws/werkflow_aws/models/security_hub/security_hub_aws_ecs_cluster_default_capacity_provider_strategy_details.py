from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEcsClusterDefaultCapacityProviderStrategyDetails(BaseModel):
    Base: StrictInt | None = None
    CapacityProvider: StrictStr | None = None
    Weight: StrictInt | None = None
