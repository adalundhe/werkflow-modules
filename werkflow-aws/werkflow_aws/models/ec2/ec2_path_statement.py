from __future__ import annotations
from pydantic import BaseModel
from .ec2_packet_header_statement import EC2PacketHeaderStatement
from .ec2_resource_statement import EC2ResourceStatement


class EC2PathStatement(BaseModel):
    PacketHeaderStatement: EC2PacketHeaderStatement | None = None
    ResourceStatement: EC2ResourceStatement | None = None
