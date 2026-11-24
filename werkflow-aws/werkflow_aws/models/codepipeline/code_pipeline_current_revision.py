from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodePipelineCurrentRevision(BaseModel):
    revision: StrictStr
    changeIdentifier: StrictStr
    created: datetime.datetime | StrictStr | None = None
    revisionSummary: StrictStr | None = None
