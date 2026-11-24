from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2ImageAncestryEntry(BaseModel):
    CreationDate: datetime.datetime | StrictStr | None = None
    ImageId: StrictStr | None = None
    ImageOwnerAlias: StrictStr | None = None
    SourceImageId: StrictStr | None = None
    SourceImageRegion: StrictStr | None = None
