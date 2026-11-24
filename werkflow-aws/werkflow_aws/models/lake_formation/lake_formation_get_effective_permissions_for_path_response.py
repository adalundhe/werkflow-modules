from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_principal_resource_permissions import LakeFormationPrincipalResourcePermissions


class LakeFormationGetEffectivePermissionsForPathResponse(BaseModel):
    Permissions: list[LakeFormationPrincipalResourcePermissions] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
