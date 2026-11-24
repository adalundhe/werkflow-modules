from __future__ import annotations
from pydantic import BaseModel
from .mwaa_module_logging_configuration import MWAAModuleLoggingConfiguration


class MWAALoggingConfiguration(BaseModel):
    DagProcessingLogs: MWAAModuleLoggingConfiguration | None = None
    SchedulerLogs: MWAAModuleLoggingConfiguration | None = None
    WebserverLogs: MWAAModuleLoggingConfiguration | None = None
    WorkerLogs: MWAAModuleLoggingConfiguration | None = None
    TaskLogs: MWAAModuleLoggingConfiguration | None = None
