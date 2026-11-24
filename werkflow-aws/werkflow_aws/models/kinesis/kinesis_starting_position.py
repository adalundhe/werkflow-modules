from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class KinesisStartingPosition(BaseModel):
    Type: Literal['AT_SEQUENCE_NUMBER', 'AFTER_SEQUENCE_NUMBER', 'TRIM_HORIZON', 'LATEST', 'AT_TIMESTAMP']
    SequenceNumber: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
