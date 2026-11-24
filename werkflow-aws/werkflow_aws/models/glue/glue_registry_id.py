from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueRegistryId(BaseModel):
    RegistryName: StrictStr | None = None
    RegistryArn: StrictStr | None = None
