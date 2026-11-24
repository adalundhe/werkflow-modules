from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class APIGatewayCanarySettings(BaseModel):
    percentTraffic: StrictFloat | StrictInt | None = None
    deploymentId: StrictStr | None = None
    stageVariableOverrides: dict[StrictStr, StrictStr] | None = None
    useStageCache: StrictBool | None = None
