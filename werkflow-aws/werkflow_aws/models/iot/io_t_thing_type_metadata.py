from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class IoTThingTypeMetadata(BaseModel):
    deprecated: StrictBool | None = None
    deprecationDate: datetime.datetime | StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
