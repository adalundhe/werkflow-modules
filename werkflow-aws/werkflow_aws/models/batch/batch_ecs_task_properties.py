from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .batch_ephemeral_storage import BatchEphemeralStorage
from .batch_network_configuration import BatchNetworkConfiguration
from .batch_runtime_platform import BatchRuntimePlatform
from .batch_task_container_properties import BatchTaskContainerProperties
from .batch_volume import BatchVolume


class BatchEcsTaskProperties(BaseModel):
    containers: list[BatchTaskContainerProperties] | None = None
    ephemeralStorage: BatchEphemeralStorage | None = None
    executionRoleArn: StrictStr | None = None
    platformVersion: StrictStr | None = None
    ipcMode: StrictStr | None = None
    taskRoleArn: StrictStr | None = None
    pidMode: StrictStr | None = None
    networkConfiguration: BatchNetworkConfiguration | None = None
    runtimePlatform: BatchRuntimePlatform | None = None
    volumes: list[BatchVolume] | None = None
    enableExecuteCommand: StrictBool | None = None
    networkMode: StrictStr | None = None
