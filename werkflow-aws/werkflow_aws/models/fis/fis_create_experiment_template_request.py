from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_create_experiment_template_action_input import FISCreateExperimentTemplateActionInput
from .fis_create_experiment_template_experiment_options_input import FISCreateExperimentTemplateExperimentOptionsInput
from .fis_create_experiment_template_log_configuration_input import FISCreateExperimentTemplateLogConfigurationInput
from .fis_create_experiment_template_report_configuration_input import FISCreateExperimentTemplateReportConfigurationInput
from .fis_create_experiment_template_stop_condition_input import FISCreateExperimentTemplateStopConditionInput
from .fis_create_experiment_template_target_input import FISCreateExperimentTemplateTargetInput


class FISCreateExperimentTemplateRequest(BaseModel):
    clientToken: StrictStr
    description: StrictStr
    stopConditions: list[FISCreateExperimentTemplateStopConditionInput]
    actions: dict[StrictStr, FISCreateExperimentTemplateActionInput]
    roleArn: StrictStr
    targets: dict[StrictStr, FISCreateExperimentTemplateTargetInput] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    logConfiguration: FISCreateExperimentTemplateLogConfigurationInput | None = None
    experimentOptions: FISCreateExperimentTemplateExperimentOptionsInput | None = None
    experimentReportConfiguration: FISCreateExperimentTemplateReportConfigurationInput | None = None
