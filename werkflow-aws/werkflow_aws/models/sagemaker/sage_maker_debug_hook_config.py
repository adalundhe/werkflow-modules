from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_collection_configuration import SageMakerCollectionConfiguration


class SageMakerDebugHookConfig(BaseModel):
    LocalPath: StrictStr | None = None
    S3OutputPath: StrictStr | None = None
    HookParameters: dict[StrictStr, StrictStr] | None = None
    CollectionConfigurations: list[SageMakerCollectionConfiguration] | None = None
