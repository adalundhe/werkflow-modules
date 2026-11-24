from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2ListResourcesForWebACLRequest(BaseModel):
    WebACLArn: StrictStr
    ResourceType: Literal['APPLICATION_LOAD_BALANCER', 'API_GATEWAY', 'APPSYNC', 'COGNITO_USER_POOL', 'APP_RUNNER_SERVICE', 'VERIFIED_ACCESS_INSTANCE', 'AMPLIFY', 'AGENTCORE_GATEWAY'] | None = None
