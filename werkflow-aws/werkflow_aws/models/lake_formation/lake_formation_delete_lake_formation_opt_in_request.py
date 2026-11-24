from __future__ import annotations
from pydantic import BaseModel
from .lake_formation_condition import LakeFormationCondition
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_resource import LakeFormationResource


class LakeFormationDeleteLakeFormationOptInRequest(BaseModel):
    Principal: LakeFormationDataLakePrincipal
    Resource: LakeFormationResource
    Condition: LakeFormationCondition | None = None
