from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_formation_logging_config import CloudFormationLoggingConfig


class CloudFormationActivateTypeRequest(BaseModel):
    Type: Literal['RESOURCE', 'MODULE', 'HOOK'] | None = None
    PublicTypeArn: StrictStr | None = None
    PublisherId: StrictStr | None = None
    TypeName: StrictStr | None = None
    TypeNameAlias: StrictStr | None = None
    AutoUpdate: StrictBool | None = None
    LoggingConfig: CloudFormationLoggingConfig | None = None
    ExecutionRoleArn: StrictStr | None = None
    VersionBump: Literal['MAJOR', 'MINOR'] | None = None
    MajorVersion: StrictInt | None = None
