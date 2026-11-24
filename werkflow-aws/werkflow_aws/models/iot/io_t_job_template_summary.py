from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTJobTemplateSummary(BaseModel):
    jobTemplateArn: StrictStr | None = None
    jobTemplateId: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
