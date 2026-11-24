from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueListEntitiesRequest(BaseModel):
    ConnectionName: StrictStr | None = None
    CatalogId: StrictStr | None = None
    ParentEntityName: StrictStr | None = None
    NextToken: StrictStr | None = None
    DataStoreApiVersion: StrictStr | None = None
