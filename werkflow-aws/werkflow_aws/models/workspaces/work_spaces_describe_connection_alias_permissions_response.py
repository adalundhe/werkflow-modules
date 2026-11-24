from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_connection_alias_permission import WorkSpacesConnectionAliasPermission


class WorkSpacesDescribeConnectionAliasPermissionsResponse(BaseModel):
    AliasId: StrictStr | None = None
    ConnectionAliasPermissions: list[WorkSpacesConnectionAliasPermission] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
