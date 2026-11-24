from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .macie_last_run_error_status import MacieLastRunErrorStatus
from .macie_s3_bucket_criteria_for_job import MacieS3BucketCriteriaForJob
from .macie_s3_bucket_definition_for_job import MacieS3BucketDefinitionForJob
from .macie_user_paused_details import MacieUserPausedDetails


class MacieJobSummary(BaseModel):
    bucketCriteria: MacieS3BucketCriteriaForJob | None = None
    bucketDefinitions: list[MacieS3BucketDefinitionForJob] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    jobId: StrictStr | None = None
    jobStatus: StrictStr | None = None
    jobType: StrictStr | None = None
    lastRunErrorStatus: MacieLastRunErrorStatus | None = None
    name: StrictStr | None = None
    userPausedDetails: MacieUserPausedDetails | None = None
