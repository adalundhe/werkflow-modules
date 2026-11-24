from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EMRBlockPublicAccessConfigurationMetadata(BaseModel):
    CreationDateTime: datetime.datetime | StrictStr | None = None
    CreatedByArn: StrictStr | None = None
