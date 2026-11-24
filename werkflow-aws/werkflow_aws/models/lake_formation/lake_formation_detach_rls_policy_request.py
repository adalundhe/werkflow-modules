from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lake_formation_condition import LakeFormationCondition
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_resource import LakeFormationResource


class LakeFormationDetachRLSPolicyRequest(BaseModel):
    Name: StrictStr
    Resource: LakeFormationResource
    Principal: LakeFormationDataLakePrincipal | None = None
    Condition: LakeFormationCondition | None = None
    RemoveDefault: StrictBool | None = None
