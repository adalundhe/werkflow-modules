from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_catalyst_filter import CodeCatalystFilter


class CodeCatalystListDevEnvironmentsRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr | None = None
    filters: list[CodeCatalystFilter] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
