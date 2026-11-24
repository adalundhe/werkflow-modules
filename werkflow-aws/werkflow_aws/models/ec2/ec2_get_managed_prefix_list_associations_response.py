from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_prefix_list_association import EC2PrefixListAssociation


class EC2GetManagedPrefixListAssociationsResponse(BaseModel):
    PrefixListAssociations: list[EC2PrefixListAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
