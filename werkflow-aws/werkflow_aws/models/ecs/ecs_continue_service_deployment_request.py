from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSContinueServiceDeploymentRequest(BaseModel):
    serviceDeploymentArn: StrictStr
    hookId: StrictStr
    action: Literal['ROLLBACK', 'CONTINUE'] | None = None
