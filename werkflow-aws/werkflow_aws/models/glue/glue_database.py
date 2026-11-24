from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_database_identifier import GlueDatabaseIdentifier
from .glue_federated_database import GlueFederatedDatabase
from .glue_principal_permissions import GluePrincipalPermissions


class GlueDatabase(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    LocationUri: StrictStr | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    CreateTableDefaultPermissions: list[GluePrincipalPermissions] | None = None
    TargetDatabase: GlueDatabaseIdentifier | None = None
    CatalogId: StrictStr | None = None
    FederatedDatabase: GlueFederatedDatabase | None = None
