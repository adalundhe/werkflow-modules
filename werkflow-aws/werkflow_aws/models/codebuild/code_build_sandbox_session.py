from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_build_logs_location import CodeBuildLogsLocation
from .code_build_network_interface import CodeBuildNetworkInterface
from .code_build_sandbox_session_phase import CodeBuildSandboxSessionPhase


class CodeBuildSandboxSession(BaseModel):
    id: StrictStr | None = None
    status: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    currentPhase: StrictStr | None = None
    phases: list[CodeBuildSandboxSessionPhase] | None = None
    resolvedSourceVersion: StrictStr | None = None
    logs: CodeBuildLogsLocation | None = None
    networkInterface: CodeBuildNetworkInterface | None = None
