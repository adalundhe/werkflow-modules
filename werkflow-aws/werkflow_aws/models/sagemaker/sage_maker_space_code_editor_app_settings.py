from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_resource_spec import SageMakerResourceSpec
from .sage_maker_space_app_lifecycle_management import SageMakerSpaceAppLifecycleManagement


class SageMakerSpaceCodeEditorAppSettings(BaseModel):
    DefaultResourceSpec: SageMakerResourceSpec | None = None
    AppLifecycleManagement: SageMakerSpaceAppLifecycleManagement | None = None
