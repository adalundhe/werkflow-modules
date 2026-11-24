from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_code_repository import SageMakerCodeRepository
from .sage_maker_resource_spec import SageMakerResourceSpec
from .sage_maker_space_app_lifecycle_management import SageMakerSpaceAppLifecycleManagement


class SageMakerSpaceJupyterLabAppSettings(BaseModel):
    DefaultResourceSpec: SageMakerResourceSpec | None = None
    CodeRepositories: list[SageMakerCodeRepository] | None = None
    AppLifecycleManagement: SageMakerSpaceAppLifecycleManagement | None = None
