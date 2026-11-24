from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lake_formation_condition import LakeFormationCondition
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_resource import LakeFormationResource


class LakeFormationGrantPermissionsRequest(BaseModel):
    Principal: LakeFormationDataLakePrincipal
    Resource: LakeFormationResource
    Permissions: list[Literal['ALL', 'SELECT', 'ALTER', 'DROP', 'DELETE', 'INSERT', 'DESCRIBE', 'CREATE_DATABASE', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'CREATE_LF_TAG', 'ASSOCIATE', 'GRANT_WITH_LF_TAG_EXPRESSION', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_CATALOG', 'SUPER_USER', 'EXECUTE']]
    CatalogId: StrictStr | None = None
    Condition: LakeFormationCondition | None = None
    PermissionsWithGrantOption: list[Literal['ALL', 'SELECT', 'ALTER', 'DROP', 'DELETE', 'INSERT', 'DESCRIBE', 'CREATE_DATABASE', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'CREATE_LF_TAG', 'ASSOCIATE', 'GRANT_WITH_LF_TAG_EXPRESSION', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_CATALOG', 'SUPER_USER', 'EXECUTE']] | None = None
