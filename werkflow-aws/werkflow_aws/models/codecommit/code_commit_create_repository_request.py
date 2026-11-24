from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitCreateRepositoryRequest(BaseModel):
    repositoryName: StrictStr
    repositoryDescription: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    kmsKeyId: StrictStr | None = None
