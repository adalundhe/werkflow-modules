from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .fis_experiment_template_action import FISExperimentTemplateAction
from .fis_experiment_template_experiment_options import FISExperimentTemplateExperimentOptions
from .fis_experiment_template_log_configuration import FISExperimentTemplateLogConfiguration
from .fis_experiment_template_report_configuration import FISExperimentTemplateReportConfiguration
from .fis_experiment_template_stop_condition import FISExperimentTemplateStopCondition
from .fis_experiment_template_target import FISExperimentTemplateTarget


class FISExperimentTemplate(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    description: StrictStr | None = None
    targets: dict[StrictStr, FISExperimentTemplateTarget] | None = None
    actions: dict[StrictStr, FISExperimentTemplateAction] | None = None
    stopConditions: list[FISExperimentTemplateStopCondition] | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastUpdateTime: datetime.datetime | StrictStr | None = None
    roleArn: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    logConfiguration: FISExperimentTemplateLogConfiguration | None = None
    experimentOptions: FISExperimentTemplateExperimentOptions | None = None
    targetAccountConfigurationsCount: StrictInt | None = None
    experimentReportConfiguration: FISExperimentTemplateReportConfiguration | None = None
