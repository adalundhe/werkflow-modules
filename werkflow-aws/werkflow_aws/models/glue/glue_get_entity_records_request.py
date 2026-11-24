from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueGetEntityRecordsRequest(BaseModel):
    EntityName: StrictStr
    Limit: StrictInt
    ConnectionName: StrictStr | None = None
    CatalogId: StrictStr | None = None
    NextToken: StrictStr | None = None
    DataStoreApiVersion: StrictStr | None = None
    ConnectionOptions: dict[StrictStr, StrictStr] | None = None
    FilterPredicate: StrictStr | None = None
    OrderBy: StrictStr | None = None
    SelectedFields: list[StrictStr] | None = None
