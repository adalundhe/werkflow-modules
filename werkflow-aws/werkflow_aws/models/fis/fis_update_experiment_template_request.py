from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_update_experiment_template_action_input_item import FISUpdateExperimentTemplateActionInputItem
from .fis_update_experiment_template_experiment_options_input import FISUpdateExperimentTemplateExperimentOptionsInput
from .fis_update_experiment_template_log_configuration_input import FISUpdateExperimentTemplateLogConfigurationInput
from .fis_update_experiment_template_report_configuration_input import FISUpdateExperimentTemplateReportConfigurationInput
from .fis_update_experiment_template_stop_condition_input import FISUpdateExperimentTemplateStopConditionInput
from .fis_update_experiment_template_target_input import FISUpdateExperimentTemplateTargetInput


class FISUpdateExperimentTemplateRequest(BaseModel):
    id: StrictStr
    description: StrictStr | None = None
    stopConditions: list[FISUpdateExperimentTemplateStopConditionInput] | None = None
    targets: dict[StrictStr, FISUpdateExperimentTemplateTargetInput] | None = None
    actions: dict[StrictStr, FISUpdateExperimentTemplateActionInputItem] | None = None
    roleArn: StrictStr | None = None
    logConfiguration: FISUpdateExperimentTemplateLogConfigurationInput | None = None
    experimentOptions: FISUpdateExperimentTemplateExperimentOptionsInput | None = None
    experimentReportConfiguration: FISUpdateExperimentTemplateReportConfigurationInput | None = None
