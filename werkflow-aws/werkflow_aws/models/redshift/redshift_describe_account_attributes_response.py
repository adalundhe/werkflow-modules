from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_account_attribute import RedshiftAccountAttribute


class RedshiftDescribeAccountAttributesResponse(BaseModel):
    AccountAttributes: list[RedshiftAccountAttribute] | None = None
    ResponseMetadata: dict[str, Any] | None = None
