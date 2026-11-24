from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_list_source_repository_branches_item import CodeCatalystListSourceRepositoryBranchesItem


class CodeCatalystListSourceRepositoryBranchesResponse(BaseModel):
    nextToken: StrictStr | None = None
    items: list[CodeCatalystListSourceRepositoryBranchesItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
