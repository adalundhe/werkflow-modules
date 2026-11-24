from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_container_config import SageMakerContainerConfig
from .sage_maker_file_system_config import SageMakerFileSystemConfig


class SageMakerJupyterLabAppImageConfig(BaseModel):
    FileSystemConfig: SageMakerFileSystemConfig | None = None
    ContainerConfig: SageMakerContainerConfig | None = None
