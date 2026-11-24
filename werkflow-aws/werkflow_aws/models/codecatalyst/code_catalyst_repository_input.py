from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystRepositoryInput(BaseModel):
    repositoryName: StrictStr
    branchName: StrictStr | None = None
