from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .cloud_front_function_config import CloudFrontFunctionConfig
from .cloud_front_tags import CloudFrontTags


class CloudFrontCreateConnectionFunctionRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Name: StrictStr
    ConnectionFunctionConfig: CloudFrontFunctionConfig
    ConnectionFunctionCode: StrictBytes | BinaryIO | StrictStr
    Tags: CloudFrontTags | None = None
