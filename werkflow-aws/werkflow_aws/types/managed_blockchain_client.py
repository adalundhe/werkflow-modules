from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class ManagedBlockchainClient(ABC):

    @abstractmethod
    def create_accessor(
        self,
        *,
        ClientRequestToken: str,
        AccessorType: str,
        Tags: dict[str, str] | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_member(
        self,
        *,
        ClientRequestToken: str,
        InvitationId: str,
        NetworkId: str,
        MemberConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_network(
        self,
        *,
        ClientRequestToken: str,
        Name: str,
        Framework: str,
        FrameworkVersion: str,
        VotingPolicy: dict[str, Any],
        MemberConfiguration: dict[str, Any],
        Description: str | None = None,
        FrameworkConfiguration: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_node(
        self,
        *,
        ClientRequestToken: str,
        NetworkId: str,
        NodeConfiguration: dict[str, Any],
        MemberId: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_proposal(
        self,
        *,
        ClientRequestToken: str,
        NetworkId: str,
        MemberId: str,
        Actions: dict[str, Any],
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_accessor(
        self,
        *,
        AccessorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_member(
        self,
        *,
        NetworkId: str,
        MemberId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_node(
        self,
        *,
        NetworkId: str,
        NodeId: str,
        MemberId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_accessor(
        self,
        *,
        AccessorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_member(
        self,
        *,
        NetworkId: str,
        MemberId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_network(
        self,
        *,
        NetworkId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_node(
        self,
        *,
        NetworkId: str,
        NodeId: str,
        MemberId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_proposal(
        self,
        *,
        NetworkId: str,
        ProposalId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_accessors(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        NetworkType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_invitations(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_members(
        self,
        *,
        NetworkId: str,
        Name: str | None = None,
        Status: str | None = None,
        IsOwned: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_networks(
        self,
        *,
        Name: str | None = None,
        Framework: str | None = None,
        Status: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_nodes(
        self,
        *,
        NetworkId: str,
        MemberId: str | None = None,
        Status: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_proposal_votes(
        self,
        *,
        NetworkId: str,
        ProposalId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_proposals(
        self,
        *,
        NetworkId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_invitation(
        self,
        *,
        InvitationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_member(
        self,
        *,
        NetworkId: str,
        MemberId: str,
        LogPublishingConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_node(
        self,
        *,
        NetworkId: str,
        NodeId: str,
        MemberId: str | None = None,
        LogPublishingConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def vote_on_proposal(
        self,
        *,
        NetworkId: str,
        ProposalId: str,
        VoterMemberId: str,
        Vote: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
