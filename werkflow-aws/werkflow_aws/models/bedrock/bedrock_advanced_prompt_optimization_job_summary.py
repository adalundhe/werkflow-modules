from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockAdvancedPromptOptimizationJobSummary(BaseModel):
    jobArn: StrictStr | None = None
    jobName: StrictStr | None = None
    jobStatus: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
