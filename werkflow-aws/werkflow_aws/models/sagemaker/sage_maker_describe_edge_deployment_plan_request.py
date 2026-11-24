from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerDescribeEdgeDeploymentPlanRequest(BaseModel):
    EdgeDeploymentPlanName: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
