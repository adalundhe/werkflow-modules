from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_type_configuration_identifier import CloudFormationTypeConfigurationIdentifier


class CloudFormationBatchDescribeTypeConfigurationsError(BaseModel):
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    TypeConfigurationIdentifier: CloudFormationTypeConfigurationIdentifier | None = None
