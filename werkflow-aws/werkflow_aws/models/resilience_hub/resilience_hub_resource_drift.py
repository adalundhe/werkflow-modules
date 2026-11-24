from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_resource_identifier import ResilienceHubResourceIdentifier


class ResilienceHubResourceDrift(BaseModel):
    appArn: StrictStr | None = None
    appVersion: StrictStr | None = None
    diffType: StrictStr | None = None
    referenceId: StrictStr | None = None
    resourceIdentifier: ResilienceHubResourceIdentifier | None = None
