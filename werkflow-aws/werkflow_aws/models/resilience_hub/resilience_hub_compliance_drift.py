from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_disruption_compliance import ResilienceHubDisruptionCompliance


class ResilienceHubComplianceDrift(BaseModel):
    actualReferenceId: StrictStr | None = None
    actualValue: dict[StrictStr, ResilienceHubDisruptionCompliance] | None = None
    appId: StrictStr | None = None
    appVersion: StrictStr | None = None
    diffType: StrictStr | None = None
    driftType: StrictStr | None = None
    entityId: StrictStr | None = None
    entityType: StrictStr | None = None
    expectedReferenceId: StrictStr | None = None
    expectedValue: dict[StrictStr, ResilienceHubDisruptionCompliance] | None = None
