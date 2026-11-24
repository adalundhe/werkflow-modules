from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class GlueGetDatabasesRequest(BaseModel):
    CatalogId: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ResourceShareType: Literal['FOREIGN', 'ALL', 'FEDERATED'] | None = None
    AttributesToGet: list[Literal['NAME', 'TARGET_DATABASE']] | None = None
