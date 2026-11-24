from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .managed_blockchain_network_framework_attributes import ManagedBlockchainNetworkFrameworkAttributes
from .managed_blockchain_voting_policy import ManagedBlockchainVotingPolicy


class ManagedBlockchainNetwork(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Framework: StrictStr | None = None
    FrameworkVersion: StrictStr | None = None
    FrameworkAttributes: ManagedBlockchainNetworkFrameworkAttributes | None = None
    VpcEndpointServiceName: StrictStr | None = None
    VotingPolicy: ManagedBlockchainVotingPolicy | None = None
    Status: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Arn: StrictStr | None = None
