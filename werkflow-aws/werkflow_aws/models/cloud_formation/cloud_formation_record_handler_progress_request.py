from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationRecordHandlerProgressRequest(BaseModel):
    BearerToken: StrictStr
    OperationStatus: Literal['PENDING', 'IN_PROGRESS', 'SUCCESS', 'FAILED']
    CurrentOperationStatus: Literal['PENDING', 'IN_PROGRESS', 'SUCCESS', 'FAILED'] | None = None
    StatusMessage: StrictStr | None = None
    ErrorCode: Literal['NotUpdatable', 'InvalidRequest', 'AccessDenied', 'InvalidCredentials', 'AlreadyExists', 'NotFound', 'ResourceConflict', 'Throttling', 'ServiceLimitExceeded', 'NotStabilized', 'GeneralServiceException', 'ServiceInternalError', 'NetworkFailure', 'InternalFailure', 'InvalidTypeConfiguration', 'HandlerInternalFailure', 'NonCompliant', 'Unknown', 'UnsupportedTarget'] | None = None
    ResourceModel: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
