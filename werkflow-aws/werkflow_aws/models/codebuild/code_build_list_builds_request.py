from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeBuildListBuildsRequest(BaseModel):
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    nextToken: StrictStr | None = None
