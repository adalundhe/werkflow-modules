from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSDaemonDeploymentSummary(BaseModel):
    daemonDeploymentArn: StrictStr | None = None
    daemonArn: StrictStr | None = None
    clusterArn: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    targetDaemonRevisionArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    stoppedAt: datetime.datetime | StrictStr | None = None
    finishedAt: datetime.datetime | StrictStr | None = None
