from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_canvas_app_settings import SageMakerCanvasAppSettings
from .sage_maker_code_editor_app_settings import SageMakerCodeEditorAppSettings
from .sage_maker_custom_file_system_config import SageMakerCustomFileSystemConfig
from .sage_maker_custom_posix_user_config import SageMakerCustomPosixUserConfig
from .sage_maker_default_space_storage_settings import SageMakerDefaultSpaceStorageSettings
from .sage_maker_jupyter_lab_app_settings import SageMakerJupyterLabAppSettings
from .sage_maker_jupyter_server_app_settings import SageMakerJupyterServerAppSettings
from .sage_maker_kernel_gateway_app_settings import SageMakerKernelGatewayAppSettings
from .sage_maker_r_session_app_settings import SageMakerRSessionAppSettings
from .sage_maker_r_studio_server_pro_app_settings import SageMakerRStudioServerProAppSettings
from .sage_maker_sharing_settings import SageMakerSharingSettings
from .sage_maker_studio_web_portal_settings import SageMakerStudioWebPortalSettings
from .sage_maker_tensor_board_app_settings import SageMakerTensorBoardAppSettings


class SageMakerUserSettings(BaseModel):
    ExecutionRole: StrictStr | None = None
    SecurityGroups: list[StrictStr] | None = None
    SharingSettings: SageMakerSharingSettings | None = None
    JupyterServerAppSettings: SageMakerJupyterServerAppSettings | None = None
    KernelGatewayAppSettings: SageMakerKernelGatewayAppSettings | None = None
    TensorBoardAppSettings: SageMakerTensorBoardAppSettings | None = None
    RStudioServerProAppSettings: SageMakerRStudioServerProAppSettings | None = None
    RSessionAppSettings: SageMakerRSessionAppSettings | None = None
    CanvasAppSettings: SageMakerCanvasAppSettings | None = None
    CodeEditorAppSettings: SageMakerCodeEditorAppSettings | None = None
    JupyterLabAppSettings: SageMakerJupyterLabAppSettings | None = None
    SpaceStorageSettings: SageMakerDefaultSpaceStorageSettings | None = None
    DefaultLandingUri: StrictStr | None = None
    StudioWebPortal: StrictStr | None = None
    CustomPosixUserConfig: SageMakerCustomPosixUserConfig | None = None
    CustomFileSystemConfigs: list[SageMakerCustomFileSystemConfig] | None = None
    StudioWebPortalSettings: SageMakerStudioWebPortalSettings | None = None
    AutoMountHomeEFS: StrictStr | None = None
