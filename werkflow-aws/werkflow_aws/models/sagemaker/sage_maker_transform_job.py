from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_batch_data_capture_config import SageMakerBatchDataCaptureConfig
from .sage_maker_data_processing import SageMakerDataProcessing
from .sage_maker_experiment_config_model import SageMakerExperimentConfigModel
from .sage_maker_model_client_config import SageMakerModelClientConfig
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_transform_input import SageMakerTransformInput
from .sage_maker_transform_output import SageMakerTransformOutput
from .sage_maker_transform_resources import SageMakerTransformResources


class SageMakerTransformJob(BaseModel):
    TransformJobName: StrictStr | None = None
    TransformJobArn: StrictStr | None = None
    TransformJobStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
    ModelName: StrictStr | None = None
    MaxConcurrentTransforms: StrictInt | None = None
    ModelClientConfig: SageMakerModelClientConfig | None = None
    MaxPayloadInMB: StrictInt | None = None
    BatchStrategy: StrictStr | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    TransformInput: SageMakerTransformInput | None = None
    TransformOutput: SageMakerTransformOutput | None = None
    DataCaptureConfig: SageMakerBatchDataCaptureConfig | None = None
    TransformResources: SageMakerTransformResources | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    TransformStartTime: datetime.datetime | StrictStr | None = None
    TransformEndTime: datetime.datetime | StrictStr | None = None
    LabelingJobArn: StrictStr | None = None
    AutoMLJobArn: StrictStr | None = None
    DataProcessing: SageMakerDataProcessing | None = None
    ExperimentConfig: SageMakerExperimentConfigModel | None = None
    Tags: list[SageMakerTagModel] | None = None
