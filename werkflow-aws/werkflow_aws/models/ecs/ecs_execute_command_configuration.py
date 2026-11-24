from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_execute_command_log_configuration import ECSExecuteCommandLogConfiguration


class ECSExecuteCommandConfiguration(BaseModel):
    kmsKeyId: StrictStr | None = None
    logging: StrictStr | None = None
    logConfiguration: ECSExecuteCommandLogConfiguration | None = None
