from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_instance_metadata_options_response import EC2InstanceMetadataOptionsResponse


class EC2ModifyInstanceMetadataOptionsResponse(BaseModel):
    InstanceId: StrictStr | None = None
    InstanceMetadataOptions: EC2InstanceMetadataOptionsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
