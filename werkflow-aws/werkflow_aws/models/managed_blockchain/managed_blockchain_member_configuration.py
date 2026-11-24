from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .managed_blockchain_member_framework_configuration import ManagedBlockchainMemberFrameworkConfiguration
from .managed_blockchain_member_log_publishing_configuration import ManagedBlockchainMemberLogPublishingConfiguration


class ManagedBlockchainMemberConfiguration(BaseModel):
    Name: StrictStr
    FrameworkConfiguration: ManagedBlockchainMemberFrameworkConfiguration
    Description: StrictStr | None = None
    LogPublishingConfiguration: ManagedBlockchainMemberLogPublishingConfiguration | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    KmsKeyArn: StrictStr | None = None
