from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_connection_alias_permission import WorkSpacesConnectionAliasPermission


class WorkSpacesUpdateConnectionAliasPermissionRequest(BaseModel):
    AliasId: StrictStr
    ConnectionAliasPermission: WorkSpacesConnectionAliasPermission
