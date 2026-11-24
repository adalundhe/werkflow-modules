from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lake_formation_table_resource import LakeFormationTableResource


class LakeFormationListDataCellsFilterRequest(BaseModel):
    Table: LakeFormationTableResource | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
