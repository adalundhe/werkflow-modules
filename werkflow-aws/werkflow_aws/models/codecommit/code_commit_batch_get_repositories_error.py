from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitBatchGetRepositoriesError(BaseModel):
    repositoryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    errorCode: StrictStr | None = None
    errorMessage: StrictStr | None = None
