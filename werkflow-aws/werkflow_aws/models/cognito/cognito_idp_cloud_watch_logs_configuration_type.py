from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPCloudWatchLogsConfigurationType(BaseModel):
    LogGroupArn: StrictStr | None = None
