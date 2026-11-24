from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_tag import SESTag
from .ses_topic import SESTopic


class SESCreateContactListRequest(BaseModel):
    ContactListName: StrictStr
    Topics: list[SESTopic] | None = None
    Description: StrictStr | None = None
    Tags: list[SESTag] | None = None
