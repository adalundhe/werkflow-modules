from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_model_package_container_definition import SageMakerModelPackageContainerDefinition


class SageMakerInferenceSpecification(BaseModel):
    Containers: list[SageMakerModelPackageContainerDefinition] | None = None
    SupportedTransformInstanceTypes: list[StrictStr] | None = None
    SupportedRealtimeInferenceInstanceTypes: list[StrictStr] | None = None
    SupportedContentTypes: list[StrictStr] | None = None
    SupportedResponseMIMETypes: list[StrictStr] | None = None
