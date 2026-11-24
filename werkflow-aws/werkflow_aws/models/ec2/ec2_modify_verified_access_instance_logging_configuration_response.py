from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_verified_access_instance_logging_configuration import EC2VerifiedAccessInstanceLoggingConfiguration


class EC2ModifyVerifiedAccessInstanceLoggingConfigurationResponse(BaseModel):
    LoggingConfiguration: EC2VerifiedAccessInstanceLoggingConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
