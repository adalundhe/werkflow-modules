from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .bedrock_project_data_retention import BedrockProjectDataRetention


class BedrockProjectSummary(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    archivedAt: datetime.datetime | StrictStr | None = None
    dataRetention: BedrockProjectDataRetention | None = None
