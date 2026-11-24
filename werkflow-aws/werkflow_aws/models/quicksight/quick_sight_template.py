from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_template_version import QuickSightTemplateVersion


class QuickSightTemplate(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Version: QuickSightTemplateVersion | None = None
    TemplateId: StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
