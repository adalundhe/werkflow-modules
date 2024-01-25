import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt
)
from werkflow_github.actions.common.models.conclusion import Conclusion
from werkflow_github.actions.common.models.status import Status


class StepValidator(BaseModel):
    name: StrictStr
    status: Status
    conclusion: Conclusion
    number: StrictInt
    started_at: datetime.datetime
    completed_at: datetime.datetime