from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_instance_metadata_defaults_response import EC2InstanceMetadataDefaultsResponse


class EC2GetInstanceMetadataDefaultsResponse(BaseModel):
    AccountLevel: EC2InstanceMetadataDefaultsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
