from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_verified_access_instance_logging_configuration import EC2VerifiedAccessInstanceLoggingConfiguration


class EC2DescribeVerifiedAccessInstanceLoggingConfigurationsResponse(BaseModel):
    LoggingConfigurations: list[EC2VerifiedAccessInstanceLoggingConfiguration] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
