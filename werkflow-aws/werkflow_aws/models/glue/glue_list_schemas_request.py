from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_registry_id import GlueRegistryId


class GlueListSchemasRequest(BaseModel):
    RegistryId: GlueRegistryId | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
