from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComprehendEndpointFilter(BaseModel):
    ModelArn: StrictStr | None = None
    Status: Literal['CREATING', 'DELETING', 'FAILED', 'IN_SERVICE', 'UPDATING'] | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
