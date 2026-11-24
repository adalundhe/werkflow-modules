from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_lora_config import SageMakerLoraConfig
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_training_session_model_config import SageMakerTrainingSessionModelConfig
from .sage_maker_training_session_output_config import SageMakerTrainingSessionOutputConfig
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerCreateTrainingSessionRequest(BaseModel):
    TrainingSessionName: StrictStr
    LoraConfig: SageMakerLoraConfig
    RoleArn: StrictStr
    ModelConfig: SageMakerTrainingSessionModelConfig
    OutputConfig: SageMakerTrainingSessionOutputConfig
    ModelPackageGroupArn: StrictStr | None = None
    VpcConfig: SageMakerVpcConfigModel | None = None
    Tags: list[SageMakerTagModel] | None = None
