from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSServiceDeploymentBrief(BaseModel):
    serviceDeploymentArn: StrictStr | None = None
    serviceArn: StrictStr | None = None
    clusterArn: StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    finishedAt: datetime.datetime | StrictStr | None = None
    targetServiceRevisionArn: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
