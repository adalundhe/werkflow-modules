from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsOpenSearchResourceConfig(BaseModel):
    dataSourceRoleArn: StrictStr
    dashboardViewerPrincipals: list[StrictStr]
    retentionDays: StrictInt
    kmsKeyArn: StrictStr | None = None
    applicationArn: StrictStr | None = None
