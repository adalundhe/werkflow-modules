from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .code_build_phase_context import CodeBuildPhaseContext


class CodeBuildSandboxSessionPhase(BaseModel):
    phaseType: StrictStr | None = None
    phaseStatus: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    durationInSeconds: StrictInt | None = None
    contexts: list[CodeBuildPhaseContext] | None = None
