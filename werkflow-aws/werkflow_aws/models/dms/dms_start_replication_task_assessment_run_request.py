from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_tag import DMSTag


class DMSStartReplicationTaskAssessmentRunRequest(BaseModel):
    ReplicationTaskArn: StrictStr
    ServiceAccessRoleArn: StrictStr
    ResultLocationBucket: StrictStr
    AssessmentRunName: StrictStr
    ResultLocationFolder: StrictStr | None = None
    ResultEncryptionMode: StrictStr | None = None
    ResultKmsKeyArn: StrictStr | None = None
    IncludeOnly: list[StrictStr] | None = None
    Exclude: list[StrictStr] | None = None
    Tags: list[DMSTag] | None = None
