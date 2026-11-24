from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationGetDataCellsFilterRequest(BaseModel):
    TableCatalogId: StrictStr
    DatabaseName: StrictStr
    TableName: StrictStr
    Name: StrictStr
