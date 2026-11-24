from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECRPublicRegistryAlias(BaseModel):
    name: StrictStr | None = None
    status: StrictStr | None = None
    primaryRegistryAlias: StrictBool | None = None
    defaultRegistryAlias: StrictBool | None = None
