from __future__ import annotations
from pydantic import BaseModel
from .mwaa_module_logging_configuration_input import MWAAModuleLoggingConfigurationInput


class MWAALoggingConfigurationInput(BaseModel):
    DagProcessingLogs: MWAAModuleLoggingConfigurationInput | None = None
    SchedulerLogs: MWAAModuleLoggingConfigurationInput | None = None
    WebserverLogs: MWAAModuleLoggingConfigurationInput | None = None
    WorkerLogs: MWAAModuleLoggingConfigurationInput | None = None
    TaskLogs: MWAAModuleLoggingConfigurationInput | None = None
