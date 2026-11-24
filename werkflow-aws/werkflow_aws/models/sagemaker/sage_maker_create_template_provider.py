from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_cfn_create_template_provider import SageMakerCfnCreateTemplateProvider


class SageMakerCreateTemplateProvider(BaseModel):
    CfnTemplateProvider: SageMakerCfnCreateTemplateProvider | None = None
