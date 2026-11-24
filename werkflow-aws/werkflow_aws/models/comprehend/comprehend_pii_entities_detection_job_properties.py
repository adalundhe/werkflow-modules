from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .comprehend_input_data_config import ComprehendInputDataConfig
from .comprehend_pii_output_data_config import ComprehendPiiOutputDataConfig
from .comprehend_redaction_config import ComprehendRedactionConfig


class ComprehendPiiEntitiesDetectionJobProperties(BaseModel):
    JobId: StrictStr | None = None
    JobArn: StrictStr | None = None
    JobName: StrictStr | None = None
    JobStatus: StrictStr | None = None
    Message: StrictStr | None = None
    SubmitTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    InputDataConfig: ComprehendInputDataConfig | None = None
    OutputDataConfig: ComprehendPiiOutputDataConfig | None = None
    RedactionConfig: ComprehendRedactionConfig | None = None
    LanguageCode: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    Mode: StrictStr | None = None
