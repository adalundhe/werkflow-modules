from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_database_identifier import GlueDatabaseIdentifier
from .glue_federated_database import GlueFederatedDatabase
from .glue_principal_permissions import GluePrincipalPermissions


class GlueDatabaseInput(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    LocationUri: StrictStr | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
    CreateTableDefaultPermissions: list[GluePrincipalPermissions] | None = None
    TargetDatabase: GlueDatabaseIdentifier | None = None
    FederatedDatabase: GlueFederatedDatabase | None = None
