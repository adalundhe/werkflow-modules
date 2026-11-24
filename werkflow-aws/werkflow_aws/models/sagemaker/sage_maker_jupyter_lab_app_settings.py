from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_app_lifecycle_management import SageMakerAppLifecycleManagement
from .sage_maker_code_repository import SageMakerCodeRepository
from .sage_maker_custom_image import SageMakerCustomImage
from .sage_maker_emr_settings import SageMakerEmrSettings
from .sage_maker_resource_spec import SageMakerResourceSpec


class SageMakerJupyterLabAppSettings(BaseModel):
    DefaultResourceSpec: SageMakerResourceSpec | None = None
    CustomImages: list[SageMakerCustomImage] | None = None
    LifecycleConfigArns: list[StrictStr] | None = None
    CodeRepositories: list[SageMakerCodeRepository] | None = None
    AppLifecycleManagement: SageMakerAppLifecycleManagement | None = None
    EmrSettings: SageMakerEmrSettings | None = None
    BuiltInLifecycleConfigArn: StrictStr | None = None
