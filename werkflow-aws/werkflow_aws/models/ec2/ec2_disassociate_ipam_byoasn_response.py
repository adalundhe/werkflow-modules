from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_asn_association import EC2AsnAssociation


class EC2DisassociateIpamByoasnResponse(BaseModel):
    AsnAssociation: EC2AsnAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
