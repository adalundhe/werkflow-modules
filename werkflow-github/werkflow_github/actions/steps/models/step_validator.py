import datetime
from typing import Optional

from pydantic import BaseModel, StrictInt, StrictStr

from werkflow_github.actions.common.models.conclusion import Conclusion
from werkflow_github.actions.common.models.status import Status


class StepValidator(BaseModel):
    name: StrictStr
    status: Status
    conclusion: Optional[Conclusion] = None
    number: StrictInt
    started_at: Optional[datetime.datetime] = None
    completed_at: Optional[datetime.datetime] = None
