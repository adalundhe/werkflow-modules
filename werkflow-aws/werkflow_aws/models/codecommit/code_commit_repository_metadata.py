from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodeCommitRepositoryMetadata(BaseModel):
    accountId: StrictStr | None = None
    repositoryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    repositoryDescription: StrictStr | None = None
    defaultBranch: StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    cloneUrlHttp: StrictStr | None = None
    cloneUrlSsh: StrictStr | None = None
    Arn: StrictStr | None = None
    kmsKeyId: StrictStr | None = None
