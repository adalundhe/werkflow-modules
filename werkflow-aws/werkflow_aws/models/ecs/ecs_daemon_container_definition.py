from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ecs_container_dependency import ECSContainerDependency
from .ecs_container_restart_policy import ECSContainerRestartPolicy
from .ecs_daemon_linux_parameters import ECSDaemonLinuxParameters
from .ecs_environment_file import ECSEnvironmentFile
from .ecs_firelens_configuration import ECSFirelensConfiguration
from .ecs_health_check import ECSHealthCheck
from .ecs_key_value_pair import ECSKeyValuePair
from .ecs_log_configuration import ECSLogConfiguration
from .ecs_mount_point import ECSMountPoint
from .ecs_repository_credentials import ECSRepositoryCredentials
from .ecs_secret import ECSSecret
from .ecs_system_control import ECSSystemControl
from .ecs_ulimit import ECSUlimit


class ECSDaemonContainerDefinition(BaseModel):
    name: StrictStr | None = None
    image: StrictStr | None = None
    memory: StrictInt | None = None
    memoryReservation: StrictInt | None = None
    repositoryCredentials: ECSRepositoryCredentials | None = None
    healthCheck: ECSHealthCheck | None = None
    cpu: StrictInt | None = None
    essential: StrictBool | None = None
    entryPoint: list[StrictStr] | None = None
    command: list[StrictStr] | None = None
    workingDirectory: StrictStr | None = None
    environmentFiles: list[ECSEnvironmentFile] | None = None
    environment: list[ECSKeyValuePair] | None = None
    secrets: list[ECSSecret] | None = None
    readonlyRootFilesystem: StrictBool | None = None
    mountPoints: list[ECSMountPoint] | None = None
    logConfiguration: ECSLogConfiguration | None = None
    firelensConfiguration: ECSFirelensConfiguration | None = None
    privileged: StrictBool | None = None
    user: StrictStr | None = None
    ulimits: list[ECSUlimit] | None = None
    linuxParameters: ECSDaemonLinuxParameters | None = None
    dependsOn: list[ECSContainerDependency] | None = None
    startTimeout: StrictInt | None = None
    stopTimeout: StrictInt | None = None
    systemControls: list[ECSSystemControl] | None = None
    interactive: StrictBool | None = None
    pseudoTerminal: StrictBool | None = None
    restartPolicy: ECSContainerRestartPolicy | None = None
