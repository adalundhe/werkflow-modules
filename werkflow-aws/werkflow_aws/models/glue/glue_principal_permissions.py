from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_data_lake_principal import GlueDataLakePrincipal


class GluePrincipalPermissions(BaseModel):
    Principal: GlueDataLakePrincipal | None = None
    Permissions: list[StrictStr] | None = None
