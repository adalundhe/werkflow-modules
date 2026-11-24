from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_component_deployment_config import SageMakerInferenceComponentDeploymentConfig
from .sage_maker_inference_component_runtime_config_summary import SageMakerInferenceComponentRuntimeConfigSummary
from .sage_maker_inference_component_specification_summary import SageMakerInferenceComponentSpecificationSummary


class SageMakerDescribeInferenceComponentResponse(BaseModel):
    InferenceComponentName: StrictStr | None = None
    InferenceComponentArn: StrictStr | None = None
    EndpointName: StrictStr | None = None
    EndpointArn: StrictStr | None = None
    VariantName: StrictStr | None = None
    FailureReason: StrictStr | None = None
    Specification: SageMakerInferenceComponentSpecificationSummary | None = None
    Specifications: list[SageMakerInferenceComponentSpecificationSummary] | None = None
    RuntimeConfig: SageMakerInferenceComponentRuntimeConfigSummary | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    InferenceComponentStatus: StrictStr | None = None
    LastDeploymentConfig: SageMakerInferenceComponentDeploymentConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
