from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_billable_token_usage import SageMakerBillableTokenUsage
from .sage_maker_lora_config import SageMakerLoraConfig
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_training_session_model_config import SageMakerTrainingSessionModelConfig
from .sage_maker_training_session_output_config import SageMakerTrainingSessionOutputConfig
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerTrainingSessionDetail(BaseModel):
    TrainingSessionArn: StrictStr | None = None
    TrainingSessionName: StrictStr | None = None
    TrainingSessionStatus: StrictStr | None = None
    ModelPackageGroupArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ErrorDetails: StrictStr | None = None
    LastReceivedSequenceNumber: StrictInt | None = None
    BillableTokenUsage: SageMakerBillableTokenUsage | None = None
    VpcConfig: SageMakerVpcConfigModel | None = None
    RoleArn: StrictStr | None = None
    LoraConfig: SageMakerLoraConfig | None = None
    ModelConfig: SageMakerTrainingSessionModelConfig | None = None
    OutputConfig: SageMakerTrainingSessionOutputConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
