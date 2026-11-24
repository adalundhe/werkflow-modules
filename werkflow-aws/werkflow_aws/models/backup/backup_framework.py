from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class BackupFramework(BaseModel):
    FrameworkName: StrictStr | None = None
    FrameworkArn: StrictStr | None = None
    FrameworkDescription: StrictStr | None = None
    NumberOfControls: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    DeploymentStatus: StrictStr | None = None
