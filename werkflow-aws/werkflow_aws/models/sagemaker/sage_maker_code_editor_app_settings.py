from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_app_lifecycle_management import SageMakerAppLifecycleManagement
from .sage_maker_custom_image import SageMakerCustomImage
from .sage_maker_resource_spec import SageMakerResourceSpec


class SageMakerCodeEditorAppSettings(BaseModel):
    DefaultResourceSpec: SageMakerResourceSpec | None = None
    CustomImages: list[SageMakerCustomImage] | None = None
    LifecycleConfigArns: list[StrictStr] | None = None
    AppLifecycleManagement: SageMakerAppLifecycleManagement | None = None
    BuiltInLifecycleConfigArn: StrictStr | None = None
