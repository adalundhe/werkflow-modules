from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .config_service_execution_controls import ConfigServiceExecutionControls
from .config_service_remediation_parameter_value import ConfigServiceRemediationParameterValue


class ConfigServiceRemediationConfiguration(BaseModel):
    ConfigRuleName: StrictStr | None = None
    TargetType: StrictStr | None = None
    TargetId: StrictStr | None = None
    TargetVersion: StrictStr | None = None
    Parameters: dict[StrictStr, ConfigServiceRemediationParameterValue] | None = None
    ResourceType: StrictStr | None = None
    Automatic: StrictBool | None = None
    ExecutionControls: ConfigServiceExecutionControls | None = None
    MaximumAutomaticAttempts: StrictInt | None = None
    RetryAttemptSeconds: StrictInt | None = None
    Arn: StrictStr | None = None
    CreatedByService: StrictStr | None = None
