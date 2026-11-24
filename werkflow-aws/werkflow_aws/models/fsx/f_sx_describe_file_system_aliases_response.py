from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_alias import FSxAlias


class FSxDescribeFileSystemAliasesResponse(BaseModel):
    Aliases: list[FSxAlias] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
