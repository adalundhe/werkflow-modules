from __future__ import annotations
from pydantic import BaseModel
from .ecs_execute_command_configuration import ECSExecuteCommandConfiguration
from .ecs_managed_storage_configuration import ECSManagedStorageConfiguration


class ECSClusterConfiguration(BaseModel):
    executeCommandConfiguration: ECSExecuteCommandConfiguration | None = None
    managedStorageConfiguration: ECSManagedStorageConfiguration | None = None
