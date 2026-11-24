from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESTenantResource(BaseModel):
    ResourceType: StrictStr | None = None
    ResourceArn: StrictStr | None = None
