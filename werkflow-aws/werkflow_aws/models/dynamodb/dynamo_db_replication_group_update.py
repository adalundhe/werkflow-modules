from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_create_replication_group_member_action import DynamoDBCreateReplicationGroupMemberAction
from .dynamo_db_delete_replication_group_member_action import DynamoDBDeleteReplicationGroupMemberAction
from .dynamo_db_disassociate_replication_group_member_action import DynamoDBDisassociateReplicationGroupMemberAction
from .dynamo_db_update_replication_group_member_action import DynamoDBUpdateReplicationGroupMemberAction


class DynamoDBReplicationGroupUpdate(BaseModel):
    Create: DynamoDBCreateReplicationGroupMemberAction | None = None
    Update: DynamoDBUpdateReplicationGroupMemberAction | None = None
    Delete: DynamoDBDeleteReplicationGroupMemberAction | None = None
    Disassociate: DynamoDBDisassociateReplicationGroupMemberAction | None = None
