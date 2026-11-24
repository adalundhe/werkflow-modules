from __future__ import annotations
from pydantic import BaseModel
from .lake_formation_redshift_connect import LakeFormationRedshiftConnect


class LakeFormationRedshiftScopeUnion(BaseModel):
    RedshiftConnect: LakeFormationRedshiftConnect | None = None
