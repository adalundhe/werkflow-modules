from __future__ import annotations
from pydantic import BaseModel
from .managed_blockchain_invite_action import ManagedBlockchainInviteAction
from .managed_blockchain_remove_action import ManagedBlockchainRemoveAction


class ManagedBlockchainProposalActions(BaseModel):
    Invitations: list[ManagedBlockchainInviteAction] | None = None
    Removals: list[ManagedBlockchainRemoveAction] | None = None
