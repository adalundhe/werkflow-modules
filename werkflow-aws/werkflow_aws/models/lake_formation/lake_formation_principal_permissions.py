from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal


class LakeFormationPrincipalPermissions(BaseModel):
    Principal: LakeFormationDataLakePrincipal | None = None
    Permissions: list[StrictStr] | None = None
