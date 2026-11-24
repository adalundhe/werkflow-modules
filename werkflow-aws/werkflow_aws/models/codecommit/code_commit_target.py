from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitTarget(BaseModel):
    repositoryName: StrictStr
    sourceReference: StrictStr
    destinationReference: StrictStr | None = None
