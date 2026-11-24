from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDescribeDaemonTaskDefinitionRequest(BaseModel):
    daemonTaskDefinition: StrictStr
