from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lake_formation_condition import LakeFormationCondition
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_details_map import LakeFormationDetailsMap
from .lake_formation_resource import LakeFormationResource


class LakeFormationPrincipalResourcePermissions(BaseModel):
    Principal: LakeFormationDataLakePrincipal | None = None
    Resource: LakeFormationResource | None = None
    Condition: LakeFormationCondition | None = None
    Permissions: list[StrictStr] | None = None
    PermissionsWithGrantOption: list[StrictStr] | None = None
    AdditionalDetails: LakeFormationDetailsMap | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    LastUpdatedBy: StrictStr | None = None
