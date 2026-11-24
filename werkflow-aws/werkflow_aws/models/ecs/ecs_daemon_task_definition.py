from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_daemon_container_definition import ECSDaemonContainerDefinition
from .ecs_daemon_volume import ECSDaemonVolume


class ECSDaemonTaskDefinition(BaseModel):
    daemonTaskDefinitionArn: StrictStr | None = None
    family: StrictStr | None = None
    revision: StrictInt | None = None
    taskRoleArn: StrictStr | None = None
    executionRoleArn: StrictStr | None = None
    containerDefinitions: list[ECSDaemonContainerDefinition] | None = None
    volumes: list[ECSDaemonVolume] | None = None
    cpu: StrictStr | None = None
    memory: StrictStr | None = None
    status: StrictStr | None = None
    registeredAt: datetime.datetime | StrictStr | None = None
    deleteRequestedAt: datetime.datetime | StrictStr | None = None
    registeredBy: StrictStr | None = None
    pidMode: StrictStr | None = None
    ipcMode: StrictStr | None = None
