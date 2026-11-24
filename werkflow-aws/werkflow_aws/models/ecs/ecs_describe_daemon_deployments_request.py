from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDescribeDaemonDeploymentsRequest(BaseModel):
    daemonDeploymentArns: list[StrictStr]
