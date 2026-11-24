from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .mwaa_update_error import MWAAUpdateError


class MWAALastUpdate(BaseModel):
    Status: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    Error: MWAAUpdateError | None = None
    Source: StrictStr | None = None
    WorkerReplacementStrategy: StrictStr | None = None
