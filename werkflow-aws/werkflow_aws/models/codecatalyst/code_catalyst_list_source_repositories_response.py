from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_list_source_repositories_item import CodeCatalystListSourceRepositoriesItem


class CodeCatalystListSourceRepositoriesResponse(BaseModel):
    items: list[CodeCatalystListSourceRepositoriesItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
