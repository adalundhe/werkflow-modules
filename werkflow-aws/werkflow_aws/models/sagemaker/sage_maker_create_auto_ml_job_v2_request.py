from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_compute_config import SageMakerAutoMLComputeConfig
from .sage_maker_auto_ml_data_split_config import SageMakerAutoMLDataSplitConfig
from .sage_maker_auto_ml_job_channel import SageMakerAutoMLJobChannel
from .sage_maker_auto_ml_job_objective import SageMakerAutoMLJobObjective
from .sage_maker_auto_ml_output_data_config import SageMakerAutoMLOutputDataConfig
from .sage_maker_auto_ml_problem_type_config import SageMakerAutoMLProblemTypeConfig
from .sage_maker_auto_ml_security_config import SageMakerAutoMLSecurityConfig
from .sage_maker_model_deploy_config import SageMakerModelDeployConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateAutoMLJobV2Request(BaseModel):
    AutoMLJobName: StrictStr
    AutoMLJobInputDataConfig: list[SageMakerAutoMLJobChannel]
    OutputDataConfig: SageMakerAutoMLOutputDataConfig
    AutoMLProblemTypeConfig: SageMakerAutoMLProblemTypeConfig
    RoleArn: StrictStr
    Tags: list[SageMakerTagModel] | None = None
    SecurityConfig: SageMakerAutoMLSecurityConfig | None = None
    AutoMLJobObjective: SageMakerAutoMLJobObjective | None = None
    ModelDeployConfig: SageMakerModelDeployConfig | None = None
    DataSplitConfig: SageMakerAutoMLDataSplitConfig | None = None
    AutoMLComputeConfig: SageMakerAutoMLComputeConfig | None = None
