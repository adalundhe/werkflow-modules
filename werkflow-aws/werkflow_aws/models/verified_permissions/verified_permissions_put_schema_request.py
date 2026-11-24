from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_schema_definition import VerifiedPermissionsSchemaDefinition


class VerifiedPermissionsPutSchemaRequest(BaseModel):
    policyStoreId: StrictStr
    definition: VerifiedPermissionsSchemaDefinition
