from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class ConfigServiceConfigurationRecorderStatus(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    lastStartTime: datetime.datetime | StrictStr | None = None
    lastStopTime: datetime.datetime | StrictStr | None = None
    recording: StrictBool | None = None
    lastStatus: StrictStr | None = None
    lastErrorCode: StrictStr | None = None
    lastErrorMessage: StrictStr | None = None
    lastStatusChangeTime: datetime.datetime | StrictStr | None = None
    servicePrincipal: StrictStr | None = None
