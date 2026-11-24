from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_instance_association_status_info import SSMInstanceAssociationStatusInfo


class SSMDescribeInstanceAssociationsStatusResponse(BaseModel):
    InstanceAssociationStatusInfos: list[SSMInstanceAssociationStatusInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
