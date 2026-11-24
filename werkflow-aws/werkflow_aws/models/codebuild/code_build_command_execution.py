from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_build_logs_location import CodeBuildLogsLocation


class CodeBuildCommandExecution(BaseModel):
    id: StrictStr | None = None
    sandboxId: StrictStr | None = None
    submitTime: datetime.datetime | StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    command: StrictStr | None = None
    type: StrictStr | None = None
    exitCode: StrictStr | None = None
    standardOutputContent: StrictStr | None = None
    standardErrContent: StrictStr | None = None
    logs: CodeBuildLogsLocation | None = None
    sandboxArn: StrictStr | None = None
