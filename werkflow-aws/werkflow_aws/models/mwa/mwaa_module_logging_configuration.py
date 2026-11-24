from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MWAAModuleLoggingConfiguration(BaseModel):
    Enabled: StrictBool | None = None
    LogLevel: StrictStr | None = None
    CloudWatchLogGroupArn: StrictStr | None = None
