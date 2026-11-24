from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_alias import FSxAlias


class FSxAssociateFileSystemAliasesResponse(BaseModel):
    Aliases: list[FSxAlias] | None = None
    ResponseMetadata: dict[str, Any] | None = None
