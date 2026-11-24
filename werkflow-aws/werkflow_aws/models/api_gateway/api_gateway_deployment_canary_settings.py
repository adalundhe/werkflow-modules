from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class APIGatewayDeploymentCanarySettings(BaseModel):
    percentTraffic: StrictFloat | StrictInt | None = None
    stageVariableOverrides: dict[StrictStr, StrictStr] | None = None
    useStageCache: StrictBool | None = None
