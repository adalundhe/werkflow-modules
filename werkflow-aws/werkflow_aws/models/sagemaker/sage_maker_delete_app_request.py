from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerDeleteAppRequest(BaseModel):
    DomainId: StrictStr
    AppType: Literal['JupyterServer', 'KernelGateway', 'DetailedProfiler', 'TensorBoard', 'CodeEditor', 'JupyterLab', 'RStudioServerPro', 'RSessionGateway', 'Canvas']
    AppName: StrictStr
    UserProfileName: StrictStr | None = None
    SpaceName: StrictStr | None = None
