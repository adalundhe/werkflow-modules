from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .resilience_hub_failure_policy import ResilienceHubFailurePolicy


class ResilienceHubUpdateResiliencyPolicyRequest(BaseModel):
    policyArn: StrictStr
    dataLocationConstraint: Literal['AnyLocation', 'SameContinent', 'SameCountry'] | None = None
    policy: dict[Literal['Software', 'Hardware', 'AZ', 'Region'], ResilienceHubFailurePolicy] | None = None
    policyDescription: StrictStr | None = None
    policyName: StrictStr | None = None
    tier: Literal['MissionCritical', 'Critical', 'Important', 'CoreServices', 'NonCritical', 'NotApplicable'] | None = None
