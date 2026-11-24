from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPUserImportJobType(BaseModel):
    JobName: StrictStr | None = None
    JobId: StrictStr | None = None
    UserPoolId: StrictStr | None = None
    PreSignedUrl: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    CompletionDate: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    CloudWatchLogsRoleArn: StrictStr | None = None
    ImportedUsers: StrictInt | None = None
    SkippedUsers: StrictInt | None = None
    FailedUsers: StrictInt | None = None
    CompletionMessage: StrictStr | None = None
    PasswordHashingAlgorithm: StrictStr | None = None
