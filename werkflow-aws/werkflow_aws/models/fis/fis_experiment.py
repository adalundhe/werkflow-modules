from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .fis_experiment_action import FISExperimentAction
from .fis_experiment_log_configuration import FISExperimentLogConfiguration
from .fis_experiment_options import FISExperimentOptions
from .fis_experiment_report import FISExperimentReport
from .fis_experiment_report_configuration import FISExperimentReportConfiguration
from .fis_experiment_state import FISExperimentState
from .fis_experiment_stop_condition import FISExperimentStopCondition
from .fis_experiment_target import FISExperimentTarget


class FISExperiment(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    experimentTemplateId: StrictStr | None = None
    roleArn: StrictStr | None = None
    state: FISExperimentState | None = None
    targets: dict[StrictStr, FISExperimentTarget] | None = None
    actions: dict[StrictStr, FISExperimentAction] | None = None
    stopConditions: list[FISExperimentStopCondition] | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    logConfiguration: FISExperimentLogConfiguration | None = None
    experimentOptions: FISExperimentOptions | None = None
    targetAccountConfigurationsCount: StrictInt | None = None
    experimentReportConfiguration: FISExperimentReportConfiguration | None = None
    experimentReport: FISExperimentReport | None = None
