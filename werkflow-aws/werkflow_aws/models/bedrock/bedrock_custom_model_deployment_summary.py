from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockCustomModelDeploymentSummary(BaseModel):
    customModelDeploymentArn: StrictStr | None = None
    customModelDeploymentName: StrictStr | None = None
    modelArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    failureMessage: StrictStr | None = None
