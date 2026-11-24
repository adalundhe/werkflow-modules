from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTProvisioningTemplateVersionSummary(BaseModel):
    versionId: StrictInt | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    isDefaultVersion: StrictBool | None = None
