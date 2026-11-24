from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_cfn_template_provider_detail import SageMakerCfnTemplateProviderDetail


class SageMakerTemplateProviderDetail(BaseModel):
    CfnTemplateProviderDetail: SageMakerCfnTemplateProviderDetail | None = None
