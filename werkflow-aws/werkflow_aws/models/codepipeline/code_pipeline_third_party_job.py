from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineThirdPartyJob(BaseModel):
    clientId: StrictStr | None = None
    jobId: StrictStr | None = None
