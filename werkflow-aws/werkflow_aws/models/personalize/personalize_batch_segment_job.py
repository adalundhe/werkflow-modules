from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .personalize_batch_segment_job_input import PersonalizeBatchSegmentJobInput
from .personalize_batch_segment_job_output import PersonalizeBatchSegmentJobOutput


class PersonalizeBatchSegmentJob(BaseModel):
    jobName: StrictStr | None = None
    batchSegmentJobArn: StrictStr | None = None
    filterArn: StrictStr | None = None
    failureReason: StrictStr | None = None
    solutionVersionArn: StrictStr | None = None
    numResults: StrictInt | None = None
    jobInput: PersonalizeBatchSegmentJobInput | None = None
    jobOutput: PersonalizeBatchSegmentJobOutput | None = None
    roleArn: StrictStr | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
