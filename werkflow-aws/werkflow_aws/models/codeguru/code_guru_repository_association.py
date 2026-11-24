from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_guru_kms_key_details import CodeGuruKMSKeyDetails
from .code_guru_s3_repository_details import CodeGuruS3RepositoryDetails


class CodeGuruRepositoryAssociation(BaseModel):
    AssociationId: StrictStr | None = None
    AssociationArn: StrictStr | None = None
    ConnectionArn: StrictStr | None = None
    Name: StrictStr | None = None
    Owner: StrictStr | None = None
    ProviderType: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    LastUpdatedTimeStamp: datetime.datetime | StrictStr | None = None
    CreatedTimeStamp: datetime.datetime | StrictStr | None = None
    KMSKeyDetails: CodeGuruKMSKeyDetails | None = None
    S3RepositoryDetails: CodeGuruS3RepositoryDetails | None = None
