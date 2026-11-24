from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_renderable_task import SageMakerRenderableTask
from .sage_maker_ui_template import SageMakerUiTemplate


class SageMakerRenderUiTemplateRequest(BaseModel):
    Task: SageMakerRenderableTask
    RoleArn: StrictStr
    UiTemplate: SageMakerUiTemplate | None = None
    HumanTaskUiArn: StrictStr | None = None
