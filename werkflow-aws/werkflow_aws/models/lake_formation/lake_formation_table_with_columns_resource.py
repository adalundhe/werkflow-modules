from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_column_wildcard import LakeFormationColumnWildcard


class LakeFormationTableWithColumnsResource(BaseModel):
    CatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    Name: StrictStr | None = None
    ColumnNames: list[StrictStr] | None = None
    ColumnWildcard: LakeFormationColumnWildcard | None = None
