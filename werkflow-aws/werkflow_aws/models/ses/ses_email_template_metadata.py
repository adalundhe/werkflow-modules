from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESEmailTemplateMetadata(BaseModel):
    TemplateName: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
