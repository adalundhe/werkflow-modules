from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .personalize_batch_segment_job_input import PersonalizeBatchSegmentJobInput
from .personalize_batch_segment_job_output import PersonalizeBatchSegmentJobOutput
from .personalize_tag import PersonalizeTag


class PersonalizeCreateBatchSegmentJobRequest(BaseModel):
    jobName: StrictStr
    solutionVersionArn: StrictStr
    jobInput: PersonalizeBatchSegmentJobInput
    jobOutput: PersonalizeBatchSegmentJobOutput
    roleArn: StrictStr
    filterArn: StrictStr | None = None
    numResults: StrictInt | None = None
    tags: list[PersonalizeTag] | None = None
