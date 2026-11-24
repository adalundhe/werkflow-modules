from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_function_association import CloudFrontFunctionAssociation


class CloudFrontFunctionAssociations(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontFunctionAssociation] | None = None
