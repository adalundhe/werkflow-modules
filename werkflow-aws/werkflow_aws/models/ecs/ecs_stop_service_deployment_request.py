from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSStopServiceDeploymentRequest(BaseModel):
    serviceDeploymentArn: StrictStr
    stopType: Literal['ABORT', 'ROLLBACK'] | None = None
