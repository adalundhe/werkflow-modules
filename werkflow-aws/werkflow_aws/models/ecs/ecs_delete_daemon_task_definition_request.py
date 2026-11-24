from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDeleteDaemonTaskDefinitionRequest(BaseModel):
    daemonTaskDefinition: StrictStr
