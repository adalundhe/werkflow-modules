from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_formation_batch_describe_type_configurations_error import CloudFormationBatchDescribeTypeConfigurationsError
from .cloud_formation_type_configuration_details import CloudFormationTypeConfigurationDetails
from .cloud_formation_type_configuration_identifier import CloudFormationTypeConfigurationIdentifier


class CloudFormationBatchDescribeTypeConfigurationsResponse(BaseModel):
    Errors: list[CloudFormationBatchDescribeTypeConfigurationsError] | None = None
    UnprocessedTypeConfigurations: list[CloudFormationTypeConfigurationIdentifier] | None = None
    TypeConfigurations: list[CloudFormationTypeConfigurationDetails] | None = None
    ResponseMetadata: dict[str, Any] | None = None
