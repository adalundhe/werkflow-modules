from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_instance_association import SSMInstanceAssociation


class SSMDescribeEffectiveInstanceAssociationsResponse(BaseModel):
    Associations: list[SSMInstanceAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
