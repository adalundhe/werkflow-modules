from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_catalog_properties_output import GlueCatalogPropertiesOutput
from .glue_federated_catalog import GlueFederatedCatalog
from .glue_principal_permissions import GluePrincipalPermissions
from .glue_target_redshift_catalog import GlueTargetRedshiftCatalog


class GlueCatalog(BaseModel):
    CatalogId: StrictStr | None = None
    Name: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    Description: StrictStr | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    TargetRedshiftCatalog: GlueTargetRedshiftCatalog | None = None
    FederatedCatalog: GlueFederatedCatalog | None = None
    CatalogProperties: GlueCatalogPropertiesOutput | None = None
    CreateTableDefaultPermissions: list[GluePrincipalPermissions] | None = None
    CreateDatabaseDefaultPermissions: list[GluePrincipalPermissions] | None = None
    AllowFullTableExternalDataAccess: StrictStr | None = None
