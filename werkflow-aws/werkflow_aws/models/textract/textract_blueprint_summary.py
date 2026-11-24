from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TextractBlueprintSummary(BaseModel):
    BlueprintArn: StrictStr | None = None
    BlueprintName: StrictStr | None = None
    BlueprintVersion: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
