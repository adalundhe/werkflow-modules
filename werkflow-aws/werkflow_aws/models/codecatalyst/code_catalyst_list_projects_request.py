from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_catalyst_project_list_filter import CodeCatalystProjectListFilter


class CodeCatalystListProjectsRequest(BaseModel):
    spaceName: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filters: list[CodeCatalystProjectListFilter] | None = None
