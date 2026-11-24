from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_disassociation_mode import DynamoDBDisassociationMode


class DynamoDBDisassociateReplicationGroupMemberAction(BaseModel):
    RegionName: StrictStr
    DisassociationMode: DynamoDBDisassociationMode
