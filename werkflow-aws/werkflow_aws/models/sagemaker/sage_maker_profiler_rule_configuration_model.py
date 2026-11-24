from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerProfilerRuleConfigurationModel(BaseModel):
    RuleConfigurationName: StrictStr | None = None
    LocalPath: StrictStr | None = None
    S3OutputPath: StrictStr | None = None
    RuleEvaluatorImage: StrictStr | None = None
    InstanceType: StrictStr | None = None
    VolumeSizeInGB: StrictInt | None = None
    RuleParameters: dict[StrictStr, StrictStr] | None = None
