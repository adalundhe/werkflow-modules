from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_cfn_stack_create_parameter import SageMakerCfnStackCreateParameter


class SageMakerCfnCreateTemplateProvider(BaseModel):
    TemplateName: StrictStr
    TemplateURL: StrictStr
    RoleARN: StrictStr | None = None
    Parameters: list[SageMakerCfnStackCreateParameter] | None = None
