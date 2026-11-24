from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .resilience_hub_failure_policy import ResilienceHubFailurePolicy


class ResilienceHubResiliencyPolicy(BaseModel):
    creationTime: datetime.datetime | StrictStr | None = None
    dataLocationConstraint: StrictStr | None = None
    estimatedCostTier: StrictStr | None = None
    policy: dict[StrictStr, ResilienceHubFailurePolicy] | None = None
    policyArn: StrictStr | None = None
    policyDescription: StrictStr | None = None
    policyName: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    tier: StrictStr | None = None
