from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lake_formation_condition import LakeFormationCondition
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_resource import LakeFormationResource


class LakeFormationRLSPolicyAttachment(BaseModel):
    CatalogId: StrictStr | None = None
    PolicyName: StrictStr | None = None
    Principal: LakeFormationDataLakePrincipal | None = None
    Resource: LakeFormationResource | None = None
    Condition: LakeFormationCondition | None = None
    DefaultRLSPolicy: StrictBool | None = None
