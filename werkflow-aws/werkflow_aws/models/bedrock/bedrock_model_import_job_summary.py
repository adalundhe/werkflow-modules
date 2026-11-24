from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockModelImportJobSummary(BaseModel):
    jobArn: StrictStr | None = None
    jobName: StrictStr | None = None
    status: StrictStr | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    importedModelArn: StrictStr | None = None
    importedModelName: StrictStr | None = None
