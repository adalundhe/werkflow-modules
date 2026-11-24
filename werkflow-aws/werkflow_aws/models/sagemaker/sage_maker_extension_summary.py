from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerExtensionSummary(BaseModel):
    ExtensionArn: StrictStr | None = None
    ExtensionName: StrictStr | None = None
    ExtensionVersion: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
