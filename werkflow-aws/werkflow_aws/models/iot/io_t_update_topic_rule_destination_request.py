from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IoTUpdateTopicRuleDestinationRequest(BaseModel):
    arn: StrictStr
    status: Literal['ENABLED', 'IN_PROGRESS', 'DISABLED', 'ERROR', 'DELETING']
