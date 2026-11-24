from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lake_formation_condition import LakeFormationCondition
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_resource import LakeFormationResource


class LakeFormationOptInsInfo(BaseModel):
    Resource: LakeFormationResource | None = None
    Principal: LakeFormationDataLakePrincipal | None = None
    Condition: LakeFormationCondition | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    LastUpdatedBy: StrictStr | None = None
