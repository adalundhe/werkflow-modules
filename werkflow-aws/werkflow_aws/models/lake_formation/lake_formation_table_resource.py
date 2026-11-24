from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_table_wildcard import LakeFormationTableWildcard


class LakeFormationTableResource(BaseModel):
    CatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    Name: StrictStr | None = None
    TableWildcard: LakeFormationTableWildcard | None = None
