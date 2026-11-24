from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .cloud_front_function_config import CloudFrontFunctionConfig


class CloudFrontUpdateConnectionFunctionRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Id: StrictStr
    IfMatch: StrictStr
    ConnectionFunctionConfig: CloudFrontFunctionConfig
    ConnectionFunctionCode: StrictBytes | BinaryIO | StrictStr
