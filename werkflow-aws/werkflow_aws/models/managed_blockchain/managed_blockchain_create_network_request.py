from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .managed_blockchain_member_configuration import ManagedBlockchainMemberConfiguration
from .managed_blockchain_network_framework_configuration import ManagedBlockchainNetworkFrameworkConfiguration
from .managed_blockchain_voting_policy import ManagedBlockchainVotingPolicy


class ManagedBlockchainCreateNetworkRequest(BaseModel):
    ClientRequestToken: StrictStr
    Name: StrictStr
    Framework: Literal['HYPERLEDGER_FABRIC', 'ETHEREUM']
    FrameworkVersion: StrictStr
    VotingPolicy: ManagedBlockchainVotingPolicy
    MemberConfiguration: ManagedBlockchainMemberConfiguration
    Description: StrictStr | None = None
    FrameworkConfiguration: ManagedBlockchainNetworkFrameworkConfiguration | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
