from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerCompilationJobSummary(BaseModel):
    CompilationJobName: StrictStr | None = None
    CompilationJobArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CompilationStartTime: datetime.datetime | StrictStr | None = None
    CompilationEndTime: datetime.datetime | StrictStr | None = None
    CompilationTargetDevice: StrictStr | None = None
    CompilationTargetPlatformOs: StrictStr | None = None
    CompilationTargetPlatformArch: StrictStr | None = None
    CompilationTargetPlatformAccelerator: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CompilationJobStatus: StrictStr | None = None
