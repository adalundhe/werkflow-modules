from __future__ import annotations
from pydantic import BaseModel
from .ec2_packet_header_statement_request import EC2PacketHeaderStatementRequest
from .ec2_resource_statement_request import EC2ResourceStatementRequest


class EC2PathStatementRequest(BaseModel):
    PacketHeaderStatement: EC2PacketHeaderStatementRequest | None = None
    ResourceStatement: EC2ResourceStatementRequest | None = None
