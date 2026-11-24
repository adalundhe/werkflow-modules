from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_resource import LakeFormationResource


class LakeFormationListPermissionsRequest(BaseModel):
    CatalogId: StrictStr | None = None
    Principal: LakeFormationDataLakePrincipal | None = None
    ResourceType: Literal['ANY_RESOURCE', 'CATALOG', 'DATABASE', 'TABLE', 'DATA_LOCATION', 'LF_TAG', 'LF_TAG_POLICY', 'LF_TAG_POLICY_DATABASE', 'LF_TAG_POLICY_TABLE', 'LF_NAMED_TAG_EXPRESSION', 'USER_DEFINED_FUNCTION'] | None = None
    Resource: LakeFormationResource | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    IncludeRelated: StrictStr | None = None
