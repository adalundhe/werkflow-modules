from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_transform_input import SageMakerTransformInput
from .sage_maker_transform_output import SageMakerTransformOutput
from .sage_maker_transform_resources import SageMakerTransformResources


class SageMakerTransformJobDefinition(BaseModel):
    MaxConcurrentTransforms: StrictInt | None = None
    MaxPayloadInMB: StrictInt | None = None
    BatchStrategy: StrictStr | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    TransformInput: SageMakerTransformInput | None = None
    TransformOutput: SageMakerTransformOutput | None = None
    TransformResources: SageMakerTransformResources | None = None
