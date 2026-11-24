from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_auto_ml_channel import SageMakerAutoMLChannel
from .sage_maker_auto_ml_job_config import SageMakerAutoMLJobConfig
from .sage_maker_auto_ml_job_objective import SageMakerAutoMLJobObjective
from .sage_maker_auto_ml_output_data_config import SageMakerAutoMLOutputDataConfig
from .sage_maker_model_deploy_config import SageMakerModelDeployConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateAutoMLJobRequest(BaseModel):
    AutoMLJobName: StrictStr
    InputDataConfig: list[SageMakerAutoMLChannel]
    OutputDataConfig: SageMakerAutoMLOutputDataConfig
    RoleArn: StrictStr
    ProblemType: Literal['BinaryClassification', 'MulticlassClassification', 'Regression'] | None = None
    AutoMLJobObjective: SageMakerAutoMLJobObjective | None = None
    AutoMLJobConfig: SageMakerAutoMLJobConfig | None = None
    GenerateCandidateDefinitionsOnly: StrictBool | None = None
    Tags: list[SageMakerTagModel] | None = None
    ModelDeployConfig: SageMakerModelDeployConfig | None = None
