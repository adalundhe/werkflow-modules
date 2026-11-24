from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_input_config import SageMakerInputConfig
from .sage_maker_neo_vpc_config import SageMakerNeoVpcConfig
from .sage_maker_output_config import SageMakerOutputConfig
from .sage_maker_stopping_condition_model import SageMakerStoppingConditionModel
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateCompilationJobRequest(BaseModel):
    CompilationJobName: StrictStr
    RoleArn: StrictStr
    OutputConfig: SageMakerOutputConfig
    StoppingCondition: SageMakerStoppingConditionModel
    ModelPackageVersionArn: StrictStr | None = None
    InputConfig: SageMakerInputConfig | None = None
    VpcConfig: SageMakerNeoVpcConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
