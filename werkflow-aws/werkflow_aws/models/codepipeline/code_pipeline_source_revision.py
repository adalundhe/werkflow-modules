from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineSourceRevision(BaseModel):
    actionName: StrictStr | None = None
    revisionId: StrictStr | None = None
    revisionSummary: StrictStr | None = None
    revisionUrl: StrictStr | None = None
