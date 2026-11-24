from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudTrailLookupAttribute(BaseModel):
    AttributeKey: Literal['EventId', 'EventName', 'ReadOnly', 'Username', 'ResourceType', 'ResourceName', 'EventSource', 'AccessKeyId']
    AttributeValue: StrictStr
