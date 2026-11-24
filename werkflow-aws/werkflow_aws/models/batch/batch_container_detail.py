from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .batch_ephemeral_storage import BatchEphemeralStorage
from .batch_fargate_platform_configuration import BatchFargatePlatformConfiguration
from .batch_key_value_pair import BatchKeyValuePair
from .batch_linux_parameters import BatchLinuxParameters
from .batch_log_configuration import BatchLogConfiguration
from .batch_mount_point import BatchMountPoint
from .batch_network_configuration import BatchNetworkConfiguration
from .batch_network_interface import BatchNetworkInterface
from .batch_repository_credentials import BatchRepositoryCredentials
from .batch_resource_requirement import BatchResourceRequirement
from .batch_runtime_platform import BatchRuntimePlatform
from .batch_secret import BatchSecret
from .batch_ulimit import BatchUlimit
from .batch_volume import BatchVolume


class BatchContainerDetail(BaseModel):
    image: StrictStr | None = None
    vcpus: StrictInt | None = None
    memory: StrictInt | None = None
    command: list[StrictStr] | None = None
    jobRoleArn: StrictStr | None = None
    executionRoleArn: StrictStr | None = None
    volumes: list[BatchVolume] | None = None
    environment: list[BatchKeyValuePair] | None = None
    mountPoints: list[BatchMountPoint] | None = None
    readonlyRootFilesystem: StrictBool | None = None
    ulimits: list[BatchUlimit] | None = None
    privileged: StrictBool | None = None
    user: StrictStr | None = None
    exitCode: StrictInt | None = None
    reason: StrictStr | None = None
    containerInstanceArn: StrictStr | None = None
    taskArn: StrictStr | None = None
    logStreamName: StrictStr | None = None
    instanceType: StrictStr | None = None
    networkInterfaces: list[BatchNetworkInterface] | None = None
    resourceRequirements: list[BatchResourceRequirement] | None = None
    linuxParameters: BatchLinuxParameters | None = None
    logConfiguration: BatchLogConfiguration | None = None
    secrets: list[BatchSecret] | None = None
    networkConfiguration: BatchNetworkConfiguration | None = None
    fargatePlatformConfiguration: BatchFargatePlatformConfiguration | None = None
    ephemeralStorage: BatchEphemeralStorage | None = None
    runtimePlatform: BatchRuntimePlatform | None = None
    repositoryCredentials: BatchRepositoryCredentials | None = None
    enableExecuteCommand: StrictBool | None = None
