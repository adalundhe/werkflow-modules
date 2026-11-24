from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_cost import ResilienceHubCost
from .resilience_hub_disruption_compliance import ResilienceHubDisruptionCompliance
from .resilience_hub_resiliency_score import ResilienceHubResiliencyScore


class ResilienceHubAppComponentCompliance(BaseModel):
    appComponentName: StrictStr | None = None
    compliance: dict[StrictStr, ResilienceHubDisruptionCompliance] | None = None
    cost: ResilienceHubCost | None = None
    message: StrictStr | None = None
    resiliencyScore: ResilienceHubResiliencyScore | None = None
    status: StrictStr | None = None
