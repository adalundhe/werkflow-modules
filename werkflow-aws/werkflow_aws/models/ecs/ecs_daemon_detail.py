from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ecs_daemon_revision_detail import ECSDaemonRevisionDetail


class ECSDaemonDetail(BaseModel):
    daemonArn: StrictStr | None = None
    clusterArn: StrictStr | None = None
    status: StrictStr | None = None
    currentRevisions: list[ECSDaemonRevisionDetail] | None = None
    deploymentArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
