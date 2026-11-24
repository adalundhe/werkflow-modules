from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sns_tag import SNSTag


class SNSCreateTopicRequest(BaseModel):
    Name: StrictStr
    Attributes: dict[StrictStr, StrictStr] | None = None
    Tags: list[SNSTag] | None = None
    DataProtectionPolicy: StrictStr | None = None
