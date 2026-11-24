from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_processing_instance_type import SageMakerProcessingInstanceType


class SageMakerDebugRuleConfiguration(BaseModel):
    RuleConfigurationName: StrictStr | None = None
    LocalPath: StrictStr | None = None
    S3OutputPath: StrictStr | None = None
    RuleEvaluatorImage: StrictStr | None = None
    InstanceType: SageMakerProcessingInstanceType | None = None
    VolumeSizeInGB: StrictInt | None = None
    RuleParameters: dict[StrictStr, StrictStr] | None = None
