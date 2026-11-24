from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_resource import LakeFormationResource


class LakeFormationListLakeFormationOptInsRequest(BaseModel):
    Principal: LakeFormationDataLakePrincipal | None = None
    Resource: LakeFormationResource | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
