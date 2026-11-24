from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_candidate import SageMakerAutoMLCandidate
from .sage_maker_auto_ml_compute_config import SageMakerAutoMLComputeConfig
from .sage_maker_auto_ml_data_split_config import SageMakerAutoMLDataSplitConfig
from .sage_maker_auto_ml_job_artifacts import SageMakerAutoMLJobArtifacts
from .sage_maker_auto_ml_job_channel import SageMakerAutoMLJobChannel
from .sage_maker_auto_ml_job_objective import SageMakerAutoMLJobObjective
from .sage_maker_auto_ml_output_data_config import SageMakerAutoMLOutputDataConfig
from .sage_maker_auto_ml_partial_failure_reason import SageMakerAutoMLPartialFailureReason
from .sage_maker_auto_ml_problem_type_config import SageMakerAutoMLProblemTypeConfig
from .sage_maker_auto_ml_resolved_attributes import SageMakerAutoMLResolvedAttributes
from .sage_maker_auto_ml_security_config import SageMakerAutoMLSecurityConfig
from .sage_maker_model_deploy_config import SageMakerModelDeployConfig
from .sage_maker_model_deploy_result import SageMakerModelDeployResult


class SageMakerDescribeAutoMLJobV2Response(BaseModel):
    AutoMLJobName: StrictStr | None = None
    AutoMLJobArn: StrictStr | None = None
    AutoMLJobInputDataConfig: list[SageMakerAutoMLJobChannel] | None = None
    OutputDataConfig: SageMakerAutoMLOutputDataConfig | None = None
    RoleArn: StrictStr | None = None
    AutoMLJobObjective: SageMakerAutoMLJobObjective | None = None
    AutoMLProblemTypeConfig: SageMakerAutoMLProblemTypeConfig | None = None
    AutoMLProblemTypeConfigName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    PartialFailureReasons: list[SageMakerAutoMLPartialFailureReason] | None = None
    BestCandidate: SageMakerAutoMLCandidate | None = None
    AutoMLJobStatus: StrictStr | None = None
    AutoMLJobSecondaryStatus: StrictStr | None = None
    AutoMLJobArtifacts: SageMakerAutoMLJobArtifacts | None = None
    ResolvedAttributes: SageMakerAutoMLResolvedAttributes | None = None
    ModelDeployConfig: SageMakerModelDeployConfig | None = None
    ModelDeployResult: SageMakerModelDeployResult | None = None
    DataSplitConfig: SageMakerAutoMLDataSplitConfig | None = None
    SecurityConfig: SageMakerAutoMLSecurityConfig | None = None
    AutoMLComputeConfig: SageMakerAutoMLComputeConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
