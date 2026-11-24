from __future__ import annotations
from pydantic import BaseModel
from .lake_formation_redshift_scope_union import LakeFormationRedshiftScopeUnion


class LakeFormationServiceIntegrationUnion(BaseModel):
    Redshift: list[LakeFormationRedshiftScopeUnion] | None = None
