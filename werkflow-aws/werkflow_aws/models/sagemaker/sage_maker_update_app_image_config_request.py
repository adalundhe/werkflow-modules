from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_code_editor_app_image_config import SageMakerCodeEditorAppImageConfig
from .sage_maker_jupyter_lab_app_image_config import SageMakerJupyterLabAppImageConfig
from .sage_maker_kernel_gateway_image_config import SageMakerKernelGatewayImageConfig


class SageMakerUpdateAppImageConfigRequest(BaseModel):
    AppImageConfigName: StrictStr
    KernelGatewayImageConfig: SageMakerKernelGatewayImageConfig | None = None
    JupyterLabAppImageConfig: SageMakerJupyterLabAppImageConfig | None = None
    CodeEditorAppImageConfig: SageMakerCodeEditorAppImageConfig | None = None
