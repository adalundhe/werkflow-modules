from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_guru_repository_association import CodeGuruRepositoryAssociation


class CodeGuruAssociateRepositoryResponse(BaseModel):
    RepositoryAssociation: CodeGuruRepositoryAssociation | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
