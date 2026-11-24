from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class IoTProvisioningTemplateSummary(BaseModel):
    templateArn: StrictStr | None = None
    templateName: StrictStr | None = None
    description: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    enabled: StrictBool | None = None
    type: StrictStr | None = None
