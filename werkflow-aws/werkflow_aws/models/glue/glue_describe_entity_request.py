from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDescribeEntityRequest(BaseModel):
    ConnectionName: StrictStr
    EntityName: StrictStr
    CatalogId: StrictStr | None = None
    NextToken: StrictStr | None = None
    DataStoreApiVersion: StrictStr | None = None
