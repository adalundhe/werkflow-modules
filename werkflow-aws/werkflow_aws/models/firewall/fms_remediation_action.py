from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_create_network_acl_action import FMSCreateNetworkAclAction
from .fms_create_network_acl_entries_action import FMSCreateNetworkAclEntriesAction
from .fms_delete_network_acl_entries_action import FMSDeleteNetworkAclEntriesAction
from .fmsec2_associate_route_table_action import FMSEC2AssociateRouteTableAction
from .fmsec2_copy_route_table_action import FMSEC2CopyRouteTableAction
from .fmsec2_create_route_action import FMSEC2CreateRouteAction
from .fmsec2_create_route_table_action import FMSEC2CreateRouteTableAction
from .fmsec2_delete_route_action import FMSEC2DeleteRouteAction
from .fmsec2_replace_route_action import FMSEC2ReplaceRouteAction
from .fmsec2_replace_route_table_association_action import FMSEC2ReplaceRouteTableAssociationAction
from .fms_policy_update_firewall_creation_config_action import FMSPolicyUpdateFirewallCreationConfigAction as _FMSPolicyUpdateFirewallCreationConfigActionType
from .fms_replace_network_acl_association_action import FMSReplaceNetworkAclAssociationAction


class FMSRemediationAction(BaseModel):
    Description: StrictStr | None = None
    EC2CreateRouteAction: FMSEC2CreateRouteAction | None = None
    EC2ReplaceRouteAction: FMSEC2ReplaceRouteAction | None = None
    EC2DeleteRouteAction: FMSEC2DeleteRouteAction | None = None
    EC2CopyRouteTableAction: FMSEC2CopyRouteTableAction | None = None
    EC2ReplaceRouteTableAssociationAction: FMSEC2ReplaceRouteTableAssociationAction | None = None
    EC2AssociateRouteTableAction: FMSEC2AssociateRouteTableAction | None = None
    EC2CreateRouteTableAction: FMSEC2CreateRouteTableAction | None = None
    FMSPolicyUpdateFirewallCreationConfigAction: _FMSPolicyUpdateFirewallCreationConfigActionType | None = None
    CreateNetworkAclAction: FMSCreateNetworkAclAction | None = None
    ReplaceNetworkAclAssociationAction: FMSReplaceNetworkAclAssociationAction | None = None
    CreateNetworkAclEntriesAction: FMSCreateNetworkAclEntriesAction | None = None
    DeleteNetworkAclEntriesAction: FMSDeleteNetworkAclEntriesAction | None = None
