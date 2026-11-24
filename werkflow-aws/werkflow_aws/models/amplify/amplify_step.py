from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AmplifyStep(BaseModel):
    stepName: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    logUrl: StrictStr | None = None
    artifactsUrl: StrictStr | None = None
    testArtifactsUrl: StrictStr | None = None
    testConfigUrl: StrictStr | None = None
    screenshots: dict[StrictStr, StrictStr] | None = None
    statusReason: StrictStr | None = None
    context: StrictStr | None = None
