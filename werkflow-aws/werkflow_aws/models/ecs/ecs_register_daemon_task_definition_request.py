from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ecs_daemon_container_definition import ECSDaemonContainerDefinition
from .ecs_daemon_volume import ECSDaemonVolume
from .ecs_tag import ECSTag


class ECSRegisterDaemonTaskDefinitionRequest(BaseModel):
    family: StrictStr
    containerDefinitions: list[ECSDaemonContainerDefinition]
    taskRoleArn: StrictStr | None = None
    executionRoleArn: StrictStr | None = None
    cpu: StrictStr | None = None
    memory: StrictStr | None = None
    volumes: list[ECSDaemonVolume] | None = None
    tags: list[ECSTag] | None = None
    pidMode: Literal['none', 'shared'] | None = None
    ipcMode: Literal['none', 'shared'] | None = None
