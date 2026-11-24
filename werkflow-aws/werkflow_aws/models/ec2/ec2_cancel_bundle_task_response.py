from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_bundle_task import EC2BundleTask


class EC2CancelBundleTaskResponse(BaseModel):
    BundleTask: EC2BundleTask | None = None
    ResponseMetadata: dict[str, Any] | None = None
