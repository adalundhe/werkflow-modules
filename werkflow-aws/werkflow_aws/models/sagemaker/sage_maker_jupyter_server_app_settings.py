from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_code_repository import SageMakerCodeRepository
from .sage_maker_resource_spec import SageMakerResourceSpec


class SageMakerJupyterServerAppSettings(BaseModel):
    DefaultResourceSpec: SageMakerResourceSpec | None = None
    LifecycleConfigArns: list[StrictStr] | None = None
    CodeRepositories: list[SageMakerCodeRepository] | None = None
