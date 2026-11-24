from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_batch_transform_input import SageMakerBatchTransformInput
from .sage_maker_endpoint_input import SageMakerEndpointInput


class SageMakerDataQualityJobInput(BaseModel):
    EndpointInput: SageMakerEndpointInput | None = None
    BatchTransformInput: SageMakerBatchTransformInput | None = None
