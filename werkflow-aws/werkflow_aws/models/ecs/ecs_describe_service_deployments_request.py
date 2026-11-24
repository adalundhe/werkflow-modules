from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDescribeServiceDeploymentsRequest(BaseModel):
    serviceDeploymentArns: list[StrictStr]
