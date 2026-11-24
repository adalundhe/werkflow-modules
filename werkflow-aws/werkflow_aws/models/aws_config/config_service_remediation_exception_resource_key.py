from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceRemediationExceptionResourceKey(BaseModel):
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
