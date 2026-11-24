from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .emr_tag import EMRTag


class EMRPersistentAppUI(BaseModel):
    PersistentAppUIId: StrictStr | None = None
    PersistentAppUITypeList: list[StrictStr] | None = None
    PersistentAppUIStatus: StrictStr | None = None
    AuthorId: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastStateChangeReason: StrictStr | None = None
    Tags: list[EMRTag] | None = None
