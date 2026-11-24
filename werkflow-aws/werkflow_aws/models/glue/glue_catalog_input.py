from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_catalog_properties import GlueCatalogProperties
from .glue_federated_catalog import GlueFederatedCatalog
from .glue_principal_permissions import GluePrincipalPermissions
from .glue_target_redshift_catalog import GlueTargetRedshiftCatalog


class GlueCatalogInput(BaseModel):
    Description: StrictStr | None = None
    FederatedCatalog: GlueFederatedCatalog | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
    TargetRedshiftCatalog: GlueTargetRedshiftCatalog | None = None
    CatalogProperties: GlueCatalogProperties | None = None
    CreateTableDefaultPermissions: list[GluePrincipalPermissions] | None = None
    CreateDatabaseDefaultPermissions: list[GluePrincipalPermissions] | None = None
    AllowFullTableExternalDataAccess: Literal['True', 'False'] | None = None
    OverwriteChildResourcePermissionsWithDefault: Literal['Accept', 'Deny'] | None = None
