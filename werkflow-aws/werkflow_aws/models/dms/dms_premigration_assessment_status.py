from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .dms_replication_task_assessment_run_progress import DMSReplicationTaskAssessmentRunProgress
from .dms_replication_task_assessment_run_result_statistic import DMSReplicationTaskAssessmentRunResultStatistic


class DMSPremigrationAssessmentStatus(BaseModel):
    PremigrationAssessmentRunArn: StrictStr | None = None
    FailOnAssessmentFailure: StrictBool | None = None
    Status: StrictStr | None = None
    PremigrationAssessmentRunCreationDate: datetime.datetime | StrictStr | None = None
    AssessmentProgress: DMSReplicationTaskAssessmentRunProgress | None = None
    LastFailureMessage: StrictStr | None = None
    ResultLocationBucket: StrictStr | None = None
    ResultLocationFolder: StrictStr | None = None
    ResultEncryptionMode: StrictStr | None = None
    ResultKmsKeyArn: StrictStr | None = None
    ResultStatistic: DMSReplicationTaskAssessmentRunResultStatistic | None = None
