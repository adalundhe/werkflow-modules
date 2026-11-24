from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_default_space_settings import SageMakerDefaultSpaceSettings
from .sage_maker_domain_settings import SageMakerDomainSettings
from .sage_maker_user_settings import SageMakerUserSettings


class SageMakerDescribeDomainResponse(BaseModel):
    DomainArn: StrictStr | None = None
    DomainId: StrictStr | None = None
    DomainName: StrictStr | None = None
    HomeEfsFileSystemId: StrictStr | None = None
    SingleSignOnManagedApplicationInstanceId: StrictStr | None = None
    SingleSignOnApplicationArn: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    SecurityGroupIdForDomainBoundary: StrictStr | None = None
    AuthMode: StrictStr | None = None
    DefaultUserSettings: SageMakerUserSettings | None = None
    DomainSettings: SageMakerDomainSettings | None = None
    AppNetworkAccessType: StrictStr | None = None
    HomeEfsFileSystemKmsKeyId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    Url: StrictStr | None = None
    VpcId: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    AppSecurityGroupManagement: StrictStr | None = None
    HomeEfsFileSystemCreation: StrictStr | None = None
    TagPropagation: StrictStr | None = None
    DefaultSpaceSettings: SageMakerDefaultSpaceSettings | None = None
    ResponseMetadata: dict[str, Any] | None = None
