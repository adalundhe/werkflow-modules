from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_connection_alias import WorkSpacesConnectionAlias


class WorkSpacesDescribeConnectionAliasesResponse(BaseModel):
    ConnectionAliases: list[WorkSpacesConnectionAlias] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
