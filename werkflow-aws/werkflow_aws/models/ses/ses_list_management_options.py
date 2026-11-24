from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESListManagementOptions(BaseModel):
    ContactListName: StrictStr
    TopicName: StrictStr | None = None
