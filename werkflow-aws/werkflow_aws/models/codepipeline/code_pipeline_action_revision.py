from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodePipelineActionRevision(BaseModel):
    revisionId: StrictStr | None = None
    revisionChangeId: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
