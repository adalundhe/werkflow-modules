from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_topic import SESTopic


class SESUpdateContactListRequest(BaseModel):
    ContactListName: StrictStr
    Topics: list[SESTopic] | None = None
    Description: StrictStr | None = None
