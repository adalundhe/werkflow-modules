from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_custom_file_system_config import SageMakerCustomFileSystemConfig
from .sage_maker_custom_posix_user_config import SageMakerCustomPosixUserConfig
from .sage_maker_default_space_storage_settings import SageMakerDefaultSpaceStorageSettings
from .sage_maker_jupyter_lab_app_settings import SageMakerJupyterLabAppSettings
from .sage_maker_jupyter_server_app_settings import SageMakerJupyterServerAppSettings
from .sage_maker_kernel_gateway_app_settings import SageMakerKernelGatewayAppSettings


class SageMakerDefaultSpaceSettings(BaseModel):
    ExecutionRole: StrictStr | None = None
    SecurityGroups: list[StrictStr] | None = None
    JupyterServerAppSettings: SageMakerJupyterServerAppSettings | None = None
    KernelGatewayAppSettings: SageMakerKernelGatewayAppSettings | None = None
    JupyterLabAppSettings: SageMakerJupyterLabAppSettings | None = None
    SpaceStorageSettings: SageMakerDefaultSpaceStorageSettings | None = None
    CustomPosixUserConfig: SageMakerCustomPosixUserConfig | None = None
    CustomFileSystemConfigs: list[SageMakerCustomFileSystemConfig] | None = None
