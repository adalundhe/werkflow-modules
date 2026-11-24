from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_resource import LakeFormationResource


class LakeFormationListRLSPolicyAttachmentsRequest(BaseModel):
    Resource: LakeFormationResource | None = None
    Principal: LakeFormationDataLakePrincipal | None = None
    PolicyName: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
