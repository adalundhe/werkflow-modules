from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_evaluation_mode_configuration import ConfigServiceEvaluationModeConfiguration
from .config_service_scope import ConfigServiceScope
from .config_service_source import ConfigServiceSource


class ConfigServiceConfigRule(BaseModel):
    ConfigRuleName: StrictStr | None = None
    ConfigRuleArn: StrictStr | None = None
    ConfigRuleId: StrictStr | None = None
    Description: StrictStr | None = None
    Scope: ConfigServiceScope | None = None
    Source: ConfigServiceSource | None = None
    InputParameters: StrictStr | None = None
    MaximumExecutionFrequency: StrictStr | None = None
    ConfigRuleState: StrictStr | None = None
    CreatedBy: StrictStr | None = None
    EvaluationModes: list[ConfigServiceEvaluationModeConfiguration] | None = None
    RuleEvaluationVisibility: StrictStr | None = None
