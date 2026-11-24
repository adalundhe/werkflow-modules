from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_formation_logging_config import CloudFormationLoggingConfig
from .cloud_formation_required_activated_type import CloudFormationRequiredActivatedType


class CloudFormationDescribeTypeResponse(BaseModel):
    Arn: StrictStr | None = None
    Type: StrictStr | None = None
    TypeName: StrictStr | None = None
    DefaultVersionId: StrictStr | None = None
    IsDefaultVersion: StrictBool | None = None
    TypeTestsStatus: StrictStr | None = None
    TypeTestsStatusDescription: StrictStr | None = None
    Description: StrictStr | None = None
    Schema: StrictStr | None = None
    ProvisioningType: StrictStr | None = None
    DeprecatedStatus: StrictStr | None = None
    LoggingConfig: CloudFormationLoggingConfig | None = None
    RequiredActivatedTypes: list[CloudFormationRequiredActivatedType] | None = None
    ExecutionRoleArn: StrictStr | None = None
    Visibility: StrictStr | None = None
    SourceUrl: StrictStr | None = None
    DocumentationUrl: StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    TimeCreated: datetime.datetime | StrictStr | None = None
    ConfigurationSchema: StrictStr | None = None
    PublisherId: StrictStr | None = None
    OriginalTypeName: StrictStr | None = None
    OriginalTypeArn: StrictStr | None = None
    PublicVersionNumber: StrictStr | None = None
    LatestPublicVersion: StrictStr | None = None
    IsActivated: StrictBool | None = None
    AutoUpdate: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
