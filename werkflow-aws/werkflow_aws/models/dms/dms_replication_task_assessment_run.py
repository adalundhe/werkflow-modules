from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .dms_replication_task_assessment_run_progress import DMSReplicationTaskAssessmentRunProgress
from .dms_replication_task_assessment_run_result_statistic import DMSReplicationTaskAssessmentRunResultStatistic


class DMSReplicationTaskAssessmentRun(BaseModel):
    ReplicationTaskAssessmentRunArn: StrictStr | None = None
    ReplicationTaskArn: StrictStr | None = None
    Status: StrictStr | None = None
    ReplicationTaskAssessmentRunCreationDate: datetime.datetime | StrictStr | None = None
    AssessmentProgress: DMSReplicationTaskAssessmentRunProgress | None = None
    LastFailureMessage: StrictStr | None = None
    ServiceAccessRoleArn: StrictStr | None = None
    ResultLocationBucket: StrictStr | None = None
    ResultLocationFolder: StrictStr | None = None
    ResultEncryptionMode: StrictStr | None = None
    ResultKmsKeyArn: StrictStr | None = None
    AssessmentRunName: StrictStr | None = None
    IsLatestTaskAssessmentRun: StrictBool | None = None
    ResultStatistic: DMSReplicationTaskAssessmentRunResultStatistic | None = None
