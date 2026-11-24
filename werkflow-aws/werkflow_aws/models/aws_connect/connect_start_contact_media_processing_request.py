from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectStartContactMediaProcessingRequest(BaseModel):
    InstanceId: StrictStr | None = None
    ContactId: StrictStr | None = None
    ProcessorArn: StrictStr | None = None
    FailureMode: Literal['DELIVER_UNPROCESSED_MESSAGE', 'DO_NOT_DELIVER_UNPROCESSED_MESSAGE'] | None = None
