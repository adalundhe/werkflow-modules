from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSExpressGatewayScalingTarget(BaseModel):
    minTaskCount: StrictInt | None = None
    maxTaskCount: StrictInt | None = None
    autoScalingMetric: StrictStr | None = None
    autoScalingTargetValue: StrictInt | None = None
