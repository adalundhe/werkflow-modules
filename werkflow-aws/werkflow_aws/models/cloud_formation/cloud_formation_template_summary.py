from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationTemplateSummary(BaseModel):
    GeneratedTemplateId: StrictStr | None = None
    GeneratedTemplateName: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    NumberOfResources: StrictInt | None = None
