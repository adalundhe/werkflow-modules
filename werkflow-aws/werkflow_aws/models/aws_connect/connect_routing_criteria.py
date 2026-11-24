from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_step import ConnectStep


class ConnectRoutingCriteria(BaseModel):
    Steps: list[ConnectStep] | None = None
    ActivationTimestamp: datetime.datetime | StrictStr | None = None
    Index: StrictInt | None = None
