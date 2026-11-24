from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_cfn_stack_update_parameter import SageMakerCfnStackUpdateParameter


class SageMakerCfnUpdateTemplateProvider(BaseModel):
    TemplateName: StrictStr
    TemplateURL: StrictStr
    Parameters: list[SageMakerCfnStackUpdateParameter] | None = None
