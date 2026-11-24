from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_custom_file_system import SageMakerCustomFileSystem
from .sage_maker_jupyter_server_app_settings import SageMakerJupyterServerAppSettings
from .sage_maker_kernel_gateway_app_settings import SageMakerKernelGatewayAppSettings
from .sage_maker_space_code_editor_app_settings import SageMakerSpaceCodeEditorAppSettings
from .sage_maker_space_jupyter_lab_app_settings import SageMakerSpaceJupyterLabAppSettings
from .sage_maker_space_storage_settings import SageMakerSpaceStorageSettings


class SageMakerSpaceSettings(BaseModel):
    JupyterServerAppSettings: SageMakerJupyterServerAppSettings | None = None
    KernelGatewayAppSettings: SageMakerKernelGatewayAppSettings | None = None
    CodeEditorAppSettings: SageMakerSpaceCodeEditorAppSettings | None = None
    JupyterLabAppSettings: SageMakerSpaceJupyterLabAppSettings | None = None
    AppType: StrictStr | None = None
    SpaceStorageSettings: SageMakerSpaceStorageSettings | None = None
    SpaceManagedResources: StrictStr | None = None
    CustomFileSystems: list[SageMakerCustomFileSystem] | None = None
    RemoteAccess: StrictStr | None = None
