from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodePipelineArtifactRevision(BaseModel):
    name: StrictStr | None = None
    revisionId: StrictStr | None = None
    revisionChangeIdentifier: StrictStr | None = None
    revisionSummary: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    revisionUrl: StrictStr | None = None
