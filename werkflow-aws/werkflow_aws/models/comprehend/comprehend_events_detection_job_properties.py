from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .comprehend_input_data_config import ComprehendInputDataConfig
from .comprehend_output_data_config import ComprehendOutputDataConfig


class ComprehendEventsDetectionJobProperties(BaseModel):
    JobId: StrictStr | None = None
    JobArn: StrictStr | None = None
    JobName: StrictStr | None = None
    JobStatus: StrictStr | None = None
    Message: StrictStr | None = None
    SubmitTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    InputDataConfig: ComprehendInputDataConfig | None = None
    OutputDataConfig: ComprehendOutputDataConfig | None = None
    LanguageCode: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    TargetEventTypes: list[StrictStr] | None = None
