from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_auto_ml_candidate import SageMakerAutoMLCandidate
from .sage_maker_auto_ml_channel import SageMakerAutoMLChannel
from .sage_maker_auto_ml_job_artifacts import SageMakerAutoMLJobArtifacts
from .sage_maker_auto_ml_job_config import SageMakerAutoMLJobConfig
from .sage_maker_auto_ml_job_objective import SageMakerAutoMLJobObjective
from .sage_maker_auto_ml_output_data_config import SageMakerAutoMLOutputDataConfig
from .sage_maker_auto_ml_partial_failure_reason import SageMakerAutoMLPartialFailureReason
from .sage_maker_model_deploy_config import SageMakerModelDeployConfig
from .sage_maker_model_deploy_result import SageMakerModelDeployResult
from .sage_maker_resolved_attributes import SageMakerResolvedAttributes


class SageMakerDescribeAutoMLJobResponse(BaseModel):
    AutoMLJobName: StrictStr | None = None
    AutoMLJobArn: StrictStr | None = None
    InputDataConfig: list[SageMakerAutoMLChannel] | None = None
    OutputDataConfig: SageMakerAutoMLOutputDataConfig | None = None
    RoleArn: StrictStr | None = None
    AutoMLJobObjective: SageMakerAutoMLJobObjective | None = None
    ProblemType: StrictStr | None = None
    AutoMLJobConfig: SageMakerAutoMLJobConfig | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    PartialFailureReasons: list[SageMakerAutoMLPartialFailureReason] | None = None
    BestCandidate: SageMakerAutoMLCandidate | None = None
    AutoMLJobStatus: StrictStr | None = None
    AutoMLJobSecondaryStatus: StrictStr | None = None
    GenerateCandidateDefinitionsOnly: StrictBool | None = None
    AutoMLJobArtifacts: SageMakerAutoMLJobArtifacts | None = None
    ResolvedAttributes: SageMakerResolvedAttributes | None = None
    ModelDeployConfig: SageMakerModelDeployConfig | None = None
    ModelDeployResult: SageMakerModelDeployResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
