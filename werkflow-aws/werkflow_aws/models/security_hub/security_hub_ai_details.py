from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAIDetails(BaseModel):
    HostResourceGuid: StrictStr | None = None
    HostResourceType: StrictStr | None = None
    CanonicalId: StrictStr | None = None
    SelfHostedAIModelResourceCount: StrictInt | None = None
    SelfHostedAIAgentResourceCount: StrictInt | None = None
    SelfHostedAIModelServingResourceCount: StrictInt | None = None
    SelfHostedAIExternalEndpointResourceCount: StrictInt | None = None
    SelfHostedAIDevelopmentResourceCount: StrictInt | None = None
    SelfHostedAIAgentFrameworkResourceCount: StrictInt | None = None
    SelfHostedAIAgentToolsAndIdentityResourceCount: StrictInt | None = None
    SelfHostedTotalAIResourceCount: StrictInt | None = None
