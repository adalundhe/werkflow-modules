from __future__ import annotations
from pydantic import BaseModel
from .redshift_lake_formation_query import RedshiftLakeFormationQuery


class RedshiftLakeFormationScopeUnion(BaseModel):
    LakeFormationQuery: RedshiftLakeFormationQuery | None = None
