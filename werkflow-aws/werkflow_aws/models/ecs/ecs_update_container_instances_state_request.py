from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSUpdateContainerInstancesStateRequest(BaseModel):
    containerInstances: list[StrictStr]
    status: Literal['ACTIVE', 'DRAINING', 'REGISTERING', 'DEREGISTERING', 'REGISTRATION_FAILED']
    cluster: StrictStr | None = None
