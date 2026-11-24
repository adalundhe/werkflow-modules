from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_formation_logging_config import CloudFormationLoggingConfig


class CloudFormationRegisterTypeRequest(BaseModel):
    TypeName: StrictStr
    SchemaHandlerPackage: StrictStr
    Type: Literal['RESOURCE', 'MODULE', 'HOOK'] | None = None
    LoggingConfig: CloudFormationLoggingConfig | None = None
    ExecutionRoleArn: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
