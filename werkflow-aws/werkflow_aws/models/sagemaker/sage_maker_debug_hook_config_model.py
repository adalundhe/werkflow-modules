from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_collection_configuration_model import SageMakerCollectionConfigurationModel


class SageMakerDebugHookConfigModel(BaseModel):
    LocalPath: StrictStr | None = None
    S3OutputPath: StrictStr | None = None
    HookParameters: dict[StrictStr, StrictStr] | None = None
    CollectionConfigurations: list[SageMakerCollectionConfigurationModel] | None = None
