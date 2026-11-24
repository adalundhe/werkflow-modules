from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_application_status_check_association_object import EC2ApplicationStatusCheckAssociationObject
from .ec2_tag_model import EC2TagModel


class EC2DescribeApplicationStatusCheckAssociationsResponse(BaseModel):
    Associations: list[EC2ApplicationStatusCheckAssociationObject] | None = None
    NextToken: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
