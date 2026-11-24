from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .resilience_hub_failure_policy import ResilienceHubFailurePolicy


class ResilienceHubCreateResiliencyPolicyRequest(BaseModel):
    policy: dict[Literal['Software', 'Hardware', 'AZ', 'Region'], ResilienceHubFailurePolicy]
    policyName: StrictStr
    tier: Literal['MissionCritical', 'Critical', 'Important', 'CoreServices', 'NonCritical', 'NotApplicable']
    clientToken: StrictStr | None = None
    dataLocationConstraint: Literal['AnyLocation', 'SameContinent', 'SameCountry'] | None = None
    policyDescription: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
