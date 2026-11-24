from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRStepAdditionalInfo(BaseModel):
    ResourceManagerApplicationIds: list[StrictStr] | None = None
    ResourceManager: StrictStr | None = None
