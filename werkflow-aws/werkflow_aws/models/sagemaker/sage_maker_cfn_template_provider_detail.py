from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_cfn_stack_detail import SageMakerCfnStackDetail
from .sage_maker_cfn_stack_parameter import SageMakerCfnStackParameter


class SageMakerCfnTemplateProviderDetail(BaseModel):
    TemplateName: StrictStr | None = None
    TemplateURL: StrictStr | None = None
    RoleARN: StrictStr | None = None
    Parameters: list[SageMakerCfnStackParameter] | None = None
    StackDetail: SageMakerCfnStackDetail | None = None
