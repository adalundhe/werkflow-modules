from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_channel_model import SageMakerChannelModel
from .sage_maker_output_data_config_model import SageMakerOutputDataConfigModel
from .sage_maker_resource_config_model import SageMakerResourceConfigModel
from .sage_maker_stopping_condition_model import SageMakerStoppingConditionModel


class SageMakerTrainingJobDefinition(BaseModel):
    TrainingInputMode: StrictStr | None = None
    HyperParameters: dict[StrictStr, StrictStr] | None = None
    InputDataConfig: list[SageMakerChannelModel] | None = None
    OutputDataConfig: SageMakerOutputDataConfigModel | None = None
    ResourceConfig: SageMakerResourceConfigModel | None = None
    StoppingCondition: SageMakerStoppingConditionModel | None = None
