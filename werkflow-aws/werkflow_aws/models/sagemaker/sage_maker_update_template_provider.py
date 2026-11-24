from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_cfn_update_template_provider import SageMakerCfnUpdateTemplateProvider


class SageMakerUpdateTemplateProvider(BaseModel):
    CfnTemplateProvider: SageMakerCfnUpdateTemplateProvider | None = None
