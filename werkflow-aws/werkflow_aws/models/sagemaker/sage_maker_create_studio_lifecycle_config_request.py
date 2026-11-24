from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateStudioLifecycleConfigRequest(BaseModel):
    StudioLifecycleConfigName: StrictStr
    StudioLifecycleConfigContent: StrictStr
    StudioLifecycleConfigAppType: Literal['JupyterServer', 'KernelGateway', 'CodeEditor', 'JupyterLab']
    Tags: list[SageMakerTagModel] | None = None
