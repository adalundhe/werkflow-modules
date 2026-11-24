from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_condition import LakeFormationCondition
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_resource import LakeFormationResource


class LakeFormationBatchPermissionsRequestEntry(BaseModel):
    Id: StrictStr | None = None
    Principal: LakeFormationDataLakePrincipal | None = None
    Resource: LakeFormationResource | None = None
    Permissions: list[StrictStr] | None = None
    Condition: LakeFormationCondition | None = None
    PermissionsWithGrantOption: list[StrictStr] | None = None
