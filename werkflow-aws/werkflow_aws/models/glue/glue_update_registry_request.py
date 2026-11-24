from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_registry_id import GlueRegistryId


class GlueUpdateRegistryRequest(BaseModel):
    RegistryId: GlueRegistryId
    Description: StrictStr
