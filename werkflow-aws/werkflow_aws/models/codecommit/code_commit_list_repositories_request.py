from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeCommitListRepositoriesRequest(BaseModel):
    nextToken: StrictStr | None = None
    sortBy: Literal['repositoryName', 'lastModifiedDate'] | None = None
    order: Literal['ascending', 'descending'] | None = None
