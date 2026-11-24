from __future__ import annotations
from pydantic import BaseModel
from .glue_registry_id import GlueRegistryId


class GlueDeleteRegistryRequest(BaseModel):
    RegistryId: GlueRegistryId
