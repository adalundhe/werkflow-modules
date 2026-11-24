from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .bedrock_status_details import BedrockStatusDetails


class BedrockModelCustomizationJobSummary(BaseModel):
    jobArn: StrictStr | None = None
    baseModelArn: StrictStr | None = None
    jobName: StrictStr | None = None
    status: StrictStr | None = None
    statusDetails: BedrockStatusDetails | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    customModelArn: StrictStr | None = None
    customModelName: StrictStr | None = None
    customizationType: StrictStr | None = None
