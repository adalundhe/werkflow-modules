from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerExtensionDetails(BaseModel):
    ClusterArn: StrictStr | None = None
    ExtensionArn: StrictStr | None = None
    ExtensionName: StrictStr | None = None
    ExtensionVersion: StrictStr | None = None
    Status: StrictStr | None = None
    ConfigurationValues: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
