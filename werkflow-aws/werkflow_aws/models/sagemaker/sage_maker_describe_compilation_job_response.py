from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_derived_information import SageMakerDerivedInformation
from .sage_maker_input_config import SageMakerInputConfig
from .sage_maker_model_artifacts_model import SageMakerModelArtifactsModel
from .sage_maker_model_digests import SageMakerModelDigests
from .sage_maker_neo_vpc_config import SageMakerNeoVpcConfig
from .sage_maker_output_config import SageMakerOutputConfig
from .sage_maker_stopping_condition_model import SageMakerStoppingConditionModel


class SageMakerDescribeCompilationJobResponse(BaseModel):
    CompilationJobName: StrictStr | None = None
    CompilationJobArn: StrictStr | None = None
    CompilationJobStatus: StrictStr | None = None
    CompilationStartTime: datetime.datetime | StrictStr | None = None
    CompilationEndTime: datetime.datetime | StrictStr | None = None
    StoppingCondition: SageMakerStoppingConditionModel | None = None
    InferenceImage: StrictStr | None = None
    ModelPackageVersionArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    ModelArtifacts: SageMakerModelArtifactsModel | None = None
    ModelDigests: SageMakerModelDigests | None = None
    RoleArn: StrictStr | None = None
    InputConfig: SageMakerInputConfig | None = None
    OutputConfig: SageMakerOutputConfig | None = None
    VpcConfig: SageMakerNeoVpcConfig | None = None
    DerivedInformation: SageMakerDerivedInformation | None = None
    ResponseMetadata: dict[str, Any] | None = None
