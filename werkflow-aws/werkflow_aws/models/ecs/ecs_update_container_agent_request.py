from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSUpdateContainerAgentRequest(BaseModel):
    containerInstance: StrictStr
    cluster: StrictStr | None = None
