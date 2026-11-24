from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ecs_container_dependency import ECSContainerDependency
from .ecs_container_restart_policy import ECSContainerRestartPolicy
from .ecs_environment_file import ECSEnvironmentFile
from .ecs_firelens_configuration import ECSFirelensConfiguration
from .ecs_health_check import ECSHealthCheck
from .ecs_host_entry import ECSHostEntry
from .ecs_key_value_pair import ECSKeyValuePair
from .ecs_linux_parameters import ECSLinuxParameters
from .ecs_log_configuration import ECSLogConfiguration
from .ecs_mount_point import ECSMountPoint
from .ecs_port_mapping import ECSPortMapping
from .ecs_repository_credentials import ECSRepositoryCredentials
from .ecs_resource_requirement import ECSResourceRequirement
from .ecs_secret import ECSSecret
from .ecs_system_control import ECSSystemControl
from .ecs_ulimit import ECSUlimit
from .ecs_volume_from import ECSVolumeFrom


class ECSContainerDefinition(BaseModel):
    name: StrictStr | None = None
    image: StrictStr | None = None
    repositoryCredentials: ECSRepositoryCredentials | None = None
    cpu: StrictInt | None = None
    memory: StrictInt | None = None
    memoryReservation: StrictInt | None = None
    links: list[StrictStr] | None = None
    portMappings: list[ECSPortMapping] | None = None
    essential: StrictBool | None = None
    restartPolicy: ECSContainerRestartPolicy | None = None
    entryPoint: list[StrictStr] | None = None
    command: list[StrictStr] | None = None
    environment: list[ECSKeyValuePair] | None = None
    environmentFiles: list[ECSEnvironmentFile] | None = None
    mountPoints: list[ECSMountPoint] | None = None
    volumesFrom: list[ECSVolumeFrom] | None = None
    linuxParameters: ECSLinuxParameters | None = None
    secrets: list[ECSSecret] | None = None
    dependsOn: list[ECSContainerDependency] | None = None
    startTimeout: StrictInt | None = None
    stopTimeout: StrictInt | None = None
    versionConsistency: StrictStr | None = None
    hostname: StrictStr | None = None
    user: StrictStr | None = None
    workingDirectory: StrictStr | None = None
    disableNetworking: StrictBool | None = None
    privileged: StrictBool | None = None
    readonlyRootFilesystem: StrictBool | None = None
    dnsServers: list[StrictStr] | None = None
    dnsSearchDomains: list[StrictStr] | None = None
    extraHosts: list[ECSHostEntry] | None = None
    dockerSecurityOptions: list[StrictStr] | None = None
    interactive: StrictBool | None = None
    pseudoTerminal: StrictBool | None = None
    dockerLabels: dict[StrictStr, StrictStr] | None = None
    ulimits: list[ECSUlimit] | None = None
    logConfiguration: ECSLogConfiguration | None = None
    healthCheck: ECSHealthCheck | None = None
    systemControls: list[ECSSystemControl] | None = None
    resourceRequirements: list[ECSResourceRequirement] | None = None
    firelensConfiguration: ECSFirelensConfiguration | None = None
    credentialSpecs: list[StrictStr] | None = None
