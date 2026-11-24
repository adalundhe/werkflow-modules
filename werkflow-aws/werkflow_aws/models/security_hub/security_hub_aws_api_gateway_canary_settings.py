from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class SecurityHubAwsApiGatewayCanarySettings(BaseModel):
    PercentTraffic: StrictFloat | StrictInt | None = None
    DeploymentId: StrictStr | None = None
    StageVariableOverrides: dict[StrictStr, StrictStr] | None = None
    UseStageCache: StrictBool | None = None
