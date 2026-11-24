from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AthenaListTableMetadataRequest(BaseModel):
    CatalogName: StrictStr
    DatabaseName: StrictStr
    Expression: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    WorkGroup: StrictStr | None = None
    AttributesToGet: list[Literal['NAME', 'TABLE_TYPE']] | None = None
