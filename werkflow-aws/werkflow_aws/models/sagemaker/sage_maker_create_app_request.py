from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_resource_spec import SageMakerResourceSpec
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateAppRequest(BaseModel):
    DomainId: StrictStr
    AppType: Literal['JupyterServer', 'KernelGateway', 'DetailedProfiler', 'TensorBoard', 'CodeEditor', 'JupyterLab', 'RStudioServerPro', 'RSessionGateway', 'Canvas']
    AppName: StrictStr
    UserProfileName: StrictStr | None = None
    SpaceName: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
    ResourceSpec: SageMakerResourceSpec | None = None
    RecoveryMode: StrictBool | None = None
