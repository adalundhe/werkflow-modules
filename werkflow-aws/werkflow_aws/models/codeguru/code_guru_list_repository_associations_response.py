from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_guru_repository_association_summary import CodeGuruRepositoryAssociationSummary


class CodeGuruListRepositoryAssociationsResponse(BaseModel):
    RepositoryAssociationSummaries: list[CodeGuruRepositoryAssociationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
