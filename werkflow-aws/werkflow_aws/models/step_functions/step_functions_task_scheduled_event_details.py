from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .step_functions_task_credentials import StepFunctionsTaskCredentials


class StepFunctionsTaskScheduledEventDetails(BaseModel):
    resourceType: StrictStr | None = None
    resource: StrictStr | None = None
    region: StrictStr | None = None
    parameters: StrictStr | None = None
    timeoutInSeconds: StrictInt | None = None
    heartbeatInSeconds: StrictInt | None = None
    taskCredentials: StepFunctionsTaskCredentials | None = None
