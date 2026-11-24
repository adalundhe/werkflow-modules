from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceSchemaExtensionInfo(BaseModel):
    DirectoryId: StrictStr | None = None
    SchemaExtensionId: StrictStr | None = None
    Description: StrictStr | None = None
    SchemaExtensionStatus: StrictStr | None = None
    SchemaExtensionStatusReason: StrictStr | None = None
    StartDateTime: datetime.datetime | StrictStr | None = None
    EndDateTime: datetime.datetime | StrictStr | None = None
