from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_batch_data_capture_config import SageMakerBatchDataCaptureConfig
from .sage_maker_data_processing import SageMakerDataProcessing
from .sage_maker_experiment_config_model import SageMakerExperimentConfigModel
from .sage_maker_model_client_config import SageMakerModelClientConfig
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_transform_input import SageMakerTransformInput
from .sage_maker_transform_output import SageMakerTransformOutput
from .sage_maker_transform_resources import SageMakerTransformResources


class SageMakerCreateTransformJobRequest(BaseModel):
    TransformJobName: StrictStr
    ModelName: StrictStr
    TransformInput: SageMakerTransformInput
    TransformOutput: SageMakerTransformOutput
    TransformResources: SageMakerTransformResources
    MaxConcurrentTransforms: StrictInt | None = None
    ModelClientConfig: SageMakerModelClientConfig | None = None
    MaxPayloadInMB: StrictInt | None = None
    BatchStrategy: Literal['MultiRecord', 'SingleRecord'] | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    DataCaptureConfig: SageMakerBatchDataCaptureConfig | None = None
    DataProcessing: SageMakerDataProcessing | None = None
    Tags: list[SageMakerTagModel] | None = None
    ExperimentConfig: SageMakerExperimentConfigModel | None = None
