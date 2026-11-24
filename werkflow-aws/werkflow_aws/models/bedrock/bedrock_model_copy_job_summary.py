from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .bedrock_tag import BedrockTag


class BedrockModelCopyJobSummary(BaseModel):
    jobArn: StrictStr | None = None
    status: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    targetModelArn: StrictStr | None = None
    targetModelName: StrictStr | None = None
    sourceAccountId: StrictStr | None = None
    sourceModelArn: StrictStr | None = None
    targetModelKmsKeyArn: StrictStr | None = None
    targetModelTags: list[BedrockTag] | None = None
    failureMessage: StrictStr | None = None
    sourceModelName: StrictStr | None = None
