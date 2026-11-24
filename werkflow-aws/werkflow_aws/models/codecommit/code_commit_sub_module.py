from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitSubModule(BaseModel):
    commitId: StrictStr | None = None
    absolutePath: StrictStr | None = None
    relativePath: StrictStr | None = None
