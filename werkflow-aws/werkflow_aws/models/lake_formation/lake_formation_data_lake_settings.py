from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lake_formation_data_lake_principal import LakeFormationDataLakePrincipal
from .lake_formation_principal_permissions import LakeFormationPrincipalPermissions


class LakeFormationDataLakeSettings(BaseModel):
    DataLakeAdmins: list[LakeFormationDataLakePrincipal] | None = None
    ReadOnlyAdmins: list[LakeFormationDataLakePrincipal] | None = None
    CreateDatabaseDefaultPermissions: list[LakeFormationPrincipalPermissions] | None = None
    CreateTableDefaultPermissions: list[LakeFormationPrincipalPermissions] | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
    TrustedResourceOwners: list[StrictStr] | None = None
    AllowExternalDataFiltering: StrictBool | None = None
    AllowFullTableExternalDataAccess: StrictBool | None = None
    ExternalDataFilteringAllowList: list[LakeFormationDataLakePrincipal] | None = None
    AuthorizedSessionTagValueList: list[StrictStr] | None = None
