from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_column_wildcard import LakeFormationColumnWildcard
from .lake_formation_row_filter import LakeFormationRowFilter


class LakeFormationDataCellsFilter(BaseModel):
    TableCatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    Name: StrictStr | None = None
    RowFilter: LakeFormationRowFilter | None = None
    ColumnNames: list[StrictStr] | None = None
    ColumnWildcard: LakeFormationColumnWildcard | None = None
    VersionId: StrictStr | None = None
