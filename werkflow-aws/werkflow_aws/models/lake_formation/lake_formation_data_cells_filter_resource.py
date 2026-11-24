from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDataCellsFilterResource(BaseModel):
    TableCatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    Name: StrictStr | None = None
