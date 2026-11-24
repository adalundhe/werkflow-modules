from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_file_system_config import SageMakerFileSystemConfig
from .sage_maker_kernel_spec import SageMakerKernelSpec


class SageMakerKernelGatewayImageConfig(BaseModel):
    KernelSpecs: list[SageMakerKernelSpec] | None = None
    FileSystemConfig: SageMakerFileSystemConfig | None = None
