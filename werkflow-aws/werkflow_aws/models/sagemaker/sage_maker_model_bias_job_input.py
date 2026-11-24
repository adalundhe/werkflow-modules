from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_batch_transform_input import SageMakerBatchTransformInput
from .sage_maker_endpoint_input import SageMakerEndpointInput
from .sage_maker_monitoring_ground_truth_s3_input import SageMakerMonitoringGroundTruthS3Input


class SageMakerModelBiasJobInput(BaseModel):
    EndpointInput: SageMakerEndpointInput | None = None
    BatchTransformInput: SageMakerBatchTransformInput | None = None
    GroundTruthS3Input: SageMakerMonitoringGroundTruthS3Input | None = None
