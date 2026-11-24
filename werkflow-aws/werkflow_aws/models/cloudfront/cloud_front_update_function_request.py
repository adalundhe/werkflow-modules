from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .cloud_front_function_config import CloudFrontFunctionConfig


class CloudFrontUpdateFunctionRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Name: StrictStr
    IfMatch: StrictStr
    FunctionConfig: CloudFrontFunctionConfig
    FunctionCode: StrictBytes | BinaryIO | StrictStr
