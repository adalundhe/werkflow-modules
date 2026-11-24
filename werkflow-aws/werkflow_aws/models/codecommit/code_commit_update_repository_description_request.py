from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUpdateRepositoryDescriptionRequest(BaseModel):
    repositoryName: StrictStr
    repositoryDescription: StrictStr | None = None
