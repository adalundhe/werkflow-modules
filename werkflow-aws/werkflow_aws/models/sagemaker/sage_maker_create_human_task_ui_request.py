from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_ui_template import SageMakerUiTemplate


class SageMakerCreateHumanTaskUiRequest(BaseModel):
    HumanTaskUiName: StrictStr
    UiTemplate: SageMakerUiTemplate
    Tags: list[SageMakerTagModel] | None = None
