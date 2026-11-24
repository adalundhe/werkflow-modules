from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_account_attribute import EC2AccountAttribute


class EC2DescribeAccountAttributesResponse(BaseModel):
    AccountAttributes: list[EC2AccountAttribute] | None = None
    ResponseMetadata: dict[str, Any] | None = None
