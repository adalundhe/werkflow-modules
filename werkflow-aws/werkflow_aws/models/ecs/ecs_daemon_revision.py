from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_daemon_container_image import ECSDaemonContainerImage


class ECSDaemonRevision(BaseModel):
    daemonRevisionArn: StrictStr | None = None
    clusterArn: StrictStr | None = None
    daemonArn: StrictStr | None = None
    daemonTaskDefinitionArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    containerImages: list[ECSDaemonContainerImage] | None = None
    propagateTags: StrictStr | None = None
    enableECSManagedTags: StrictBool | None = None
    enableExecuteCommand: StrictBool | None = None
    critical: StrictBool | None = None
