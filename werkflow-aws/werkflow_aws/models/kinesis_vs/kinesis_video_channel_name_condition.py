from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KinesisVideoChannelNameCondition(BaseModel):
    ComparisonOperator: Literal['BEGINS_WITH'] | None = None
    ComparisonValue: StrictStr | None = None
