from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .batch_firelens_configuration import BatchFirelensConfiguration
from .batch_key_value_pair import BatchKeyValuePair
from .batch_linux_parameters import BatchLinuxParameters
from .batch_log_configuration import BatchLogConfiguration
from .batch_mount_point import BatchMountPoint
from .batch_network_interface import BatchNetworkInterface
from .batch_repository_credentials import BatchRepositoryCredentials
from .batch_resource_requirement import BatchResourceRequirement
from .batch_secret import BatchSecret
from .batch_task_container_dependency import BatchTaskContainerDependency
from .batch_ulimit import BatchUlimit


class BatchTaskContainerDetails(BaseModel):
    command: list[StrictStr] | None = None
    dependsOn: list[BatchTaskContainerDependency] | None = None
    environment: list[BatchKeyValuePair] | None = None
    essential: StrictBool | None = None
    firelensConfiguration: BatchFirelensConfiguration | None = None
    image: StrictStr | None = None
    linuxParameters: BatchLinuxParameters | None = None
    logConfiguration: BatchLogConfiguration | None = None
    mountPoints: list[BatchMountPoint] | None = None
    name: StrictStr | None = None
    privileged: StrictBool | None = None
    readonlyRootFilesystem: StrictBool | None = None
    repositoryCredentials: BatchRepositoryCredentials | None = None
    resourceRequirements: list[BatchResourceRequirement] | None = None
    secrets: list[BatchSecret] | None = None
    ulimits: list[BatchUlimit] | None = None
    user: StrictStr | None = None
    startTimeout: StrictInt | None = None
    stopTimeout: StrictInt | None = None
    exitCode: StrictInt | None = None
    reason: StrictStr | None = None
    logStreamName: StrictStr | None = None
    networkInterfaces: list[BatchNetworkInterface] | None = None
