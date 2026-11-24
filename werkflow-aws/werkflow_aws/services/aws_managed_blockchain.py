from werkflow_aws.models.managed_blockchain import (
    ManagedBlockchainCreateAccessorRequest,
    ManagedBlockchainCreateAccessorResponse,
    ManagedBlockchainCreateMemberRequest,
    ManagedBlockchainCreateMemberResponse,
    ManagedBlockchainCreateNetworkRequest,
    ManagedBlockchainCreateNetworkResponse,
    ManagedBlockchainCreateNodeRequest,
    ManagedBlockchainCreateNodeResponse,
    ManagedBlockchainCreateProposalRequest,
    ManagedBlockchainCreateProposalResponse,
    ManagedBlockchainDeleteAccessorRequest,
    ManagedBlockchainDeleteAccessorResponse,
    ManagedBlockchainDeleteMemberRequest,
    ManagedBlockchainDeleteMemberResponse,
    ManagedBlockchainDeleteNodeRequest,
    ManagedBlockchainDeleteNodeResponse,
    ManagedBlockchainGetAccessorRequest,
    ManagedBlockchainGetAccessorResponse,
    ManagedBlockchainGetMemberRequest,
    ManagedBlockchainGetMemberResponse,
    ManagedBlockchainGetNetworkRequest,
    ManagedBlockchainGetNetworkResponse,
    ManagedBlockchainGetNodeRequest,
    ManagedBlockchainGetNodeResponse,
    ManagedBlockchainGetProposalRequest,
    ManagedBlockchainGetProposalResponse,
    ManagedBlockchainListAccessorsRequest,
    ManagedBlockchainListAccessorsResponse,
    ManagedBlockchainListInvitationsRequest,
    ManagedBlockchainListInvitationsResponse,
    ManagedBlockchainListMembersRequest,
    ManagedBlockchainListMembersResponse,
    ManagedBlockchainListNetworksRequest,
    ManagedBlockchainListNetworksResponse,
    ManagedBlockchainListNodesRequest,
    ManagedBlockchainListNodesResponse,
    ManagedBlockchainListProposalVotesRequest,
    ManagedBlockchainListProposalVotesResponse,
    ManagedBlockchainListProposalsRequest,
    ManagedBlockchainListProposalsResponse,
    ManagedBlockchainListTagsForResourceRequest,
    ManagedBlockchainListTagsForResourceResponse,
    ManagedBlockchainRejectInvitationRequest,
    ManagedBlockchainRejectInvitationResponse,
    ManagedBlockchainTagResourceRequest,
    ManagedBlockchainTagResourceResponse,
    ManagedBlockchainUntagResourceRequest,
    ManagedBlockchainUntagResourceResponse,
    ManagedBlockchainUpdateMemberRequest,
    ManagedBlockchainUpdateMemberResponse,
    ManagedBlockchainUpdateNodeRequest,
    ManagedBlockchainUpdateNodeResponse,
    ManagedBlockchainVoteOnProposalRequest,
    ManagedBlockchainVoteOnProposalResponse,
)
from werkflow_aws.types.managed_blockchain_client import ManagedBlockchainClient
from .base import AWSBaseService


class AWSManagedBlockchain(AWSBaseService[ManagedBlockchainClient]):
    service_name = 'managed-blockchain'
    boto3_service_name = 'managedblockchain'

    def __init__(self) -> None:
        super().__init__(service_name='managed-blockchain', boto3_service_name='managedblockchain')

    async def create_accessor(
        self,
        request: ManagedBlockchainCreateAccessorRequest,
    ) -> ManagedBlockchainCreateAccessorResponse:
        client = self._require_client()
        return await self._execute(client.create_accessor, request, ManagedBlockchainCreateAccessorResponse)

    async def create_member(
        self,
        request: ManagedBlockchainCreateMemberRequest,
    ) -> ManagedBlockchainCreateMemberResponse:
        client = self._require_client()
        return await self._execute(client.create_member, request, ManagedBlockchainCreateMemberResponse)

    async def create_network(
        self,
        request: ManagedBlockchainCreateNetworkRequest,
    ) -> ManagedBlockchainCreateNetworkResponse:
        client = self._require_client()
        return await self._execute(client.create_network, request, ManagedBlockchainCreateNetworkResponse)

    async def create_node(
        self,
        request: ManagedBlockchainCreateNodeRequest,
    ) -> ManagedBlockchainCreateNodeResponse:
        client = self._require_client()
        return await self._execute(client.create_node, request, ManagedBlockchainCreateNodeResponse)

    async def create_proposal(
        self,
        request: ManagedBlockchainCreateProposalRequest,
    ) -> ManagedBlockchainCreateProposalResponse:
        client = self._require_client()
        return await self._execute(client.create_proposal, request, ManagedBlockchainCreateProposalResponse)

    async def delete_accessor(
        self,
        request: ManagedBlockchainDeleteAccessorRequest,
    ) -> ManagedBlockchainDeleteAccessorResponse:
        client = self._require_client()
        return await self._execute(client.delete_accessor, request, ManagedBlockchainDeleteAccessorResponse)

    async def delete_member(
        self,
        request: ManagedBlockchainDeleteMemberRequest,
    ) -> ManagedBlockchainDeleteMemberResponse:
        client = self._require_client()
        return await self._execute(client.delete_member, request, ManagedBlockchainDeleteMemberResponse)

    async def delete_node(
        self,
        request: ManagedBlockchainDeleteNodeRequest,
    ) -> ManagedBlockchainDeleteNodeResponse:
        client = self._require_client()
        return await self._execute(client.delete_node, request, ManagedBlockchainDeleteNodeResponse)

    async def get_accessor(
        self,
        request: ManagedBlockchainGetAccessorRequest,
    ) -> ManagedBlockchainGetAccessorResponse:
        client = self._require_client()
        return await self._execute(client.get_accessor, request, ManagedBlockchainGetAccessorResponse)

    async def get_member(
        self,
        request: ManagedBlockchainGetMemberRequest,
    ) -> ManagedBlockchainGetMemberResponse:
        client = self._require_client()
        return await self._execute(client.get_member, request, ManagedBlockchainGetMemberResponse)

    async def get_network(
        self,
        request: ManagedBlockchainGetNetworkRequest,
    ) -> ManagedBlockchainGetNetworkResponse:
        client = self._require_client()
        return await self._execute(client.get_network, request, ManagedBlockchainGetNetworkResponse)

    async def get_node(
        self,
        request: ManagedBlockchainGetNodeRequest,
    ) -> ManagedBlockchainGetNodeResponse:
        client = self._require_client()
        return await self._execute(client.get_node, request, ManagedBlockchainGetNodeResponse)

    async def get_proposal(
        self,
        request: ManagedBlockchainGetProposalRequest,
    ) -> ManagedBlockchainGetProposalResponse:
        client = self._require_client()
        return await self._execute(client.get_proposal, request, ManagedBlockchainGetProposalResponse)

    async def list_accessors(
        self,
        request: ManagedBlockchainListAccessorsRequest | None = None,
    ) -> ManagedBlockchainListAccessorsResponse:
        client = self._require_client()
        return await self._execute(client.list_accessors, request, ManagedBlockchainListAccessorsResponse)

    async def list_accessors_paginated(
        self,
        request: ManagedBlockchainListAccessorsRequest | None = None,
    ) -> list[ManagedBlockchainListAccessorsResponse]:
        return await self._paginate('list_accessors', request, ManagedBlockchainListAccessorsResponse)

    async def list_invitations(
        self,
        request: ManagedBlockchainListInvitationsRequest | None = None,
    ) -> ManagedBlockchainListInvitationsResponse:
        client = self._require_client()
        return await self._execute(client.list_invitations, request, ManagedBlockchainListInvitationsResponse)

    async def list_members(
        self,
        request: ManagedBlockchainListMembersRequest,
    ) -> ManagedBlockchainListMembersResponse:
        client = self._require_client()
        return await self._execute(client.list_members, request, ManagedBlockchainListMembersResponse)

    async def list_networks(
        self,
        request: ManagedBlockchainListNetworksRequest | None = None,
    ) -> ManagedBlockchainListNetworksResponse:
        client = self._require_client()
        return await self._execute(client.list_networks, request, ManagedBlockchainListNetworksResponse)

    async def list_nodes(
        self,
        request: ManagedBlockchainListNodesRequest,
    ) -> ManagedBlockchainListNodesResponse:
        client = self._require_client()
        return await self._execute(client.list_nodes, request, ManagedBlockchainListNodesResponse)

    async def list_proposal_votes(
        self,
        request: ManagedBlockchainListProposalVotesRequest,
    ) -> ManagedBlockchainListProposalVotesResponse:
        client = self._require_client()
        return await self._execute(client.list_proposal_votes, request, ManagedBlockchainListProposalVotesResponse)

    async def list_proposals(
        self,
        request: ManagedBlockchainListProposalsRequest,
    ) -> ManagedBlockchainListProposalsResponse:
        client = self._require_client()
        return await self._execute(client.list_proposals, request, ManagedBlockchainListProposalsResponse)

    async def list_tags_for_resource(
        self,
        request: ManagedBlockchainListTagsForResourceRequest,
    ) -> ManagedBlockchainListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, ManagedBlockchainListTagsForResourceResponse)

    async def reject_invitation(
        self,
        request: ManagedBlockchainRejectInvitationRequest,
    ) -> ManagedBlockchainRejectInvitationResponse:
        client = self._require_client()
        return await self._execute(client.reject_invitation, request, ManagedBlockchainRejectInvitationResponse)

    async def tag_resource(
        self,
        request: ManagedBlockchainTagResourceRequest,
    ) -> ManagedBlockchainTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, ManagedBlockchainTagResourceResponse)

    async def untag_resource(
        self,
        request: ManagedBlockchainUntagResourceRequest,
    ) -> ManagedBlockchainUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, ManagedBlockchainUntagResourceResponse)

    async def update_member(
        self,
        request: ManagedBlockchainUpdateMemberRequest,
    ) -> ManagedBlockchainUpdateMemberResponse:
        client = self._require_client()
        return await self._execute(client.update_member, request, ManagedBlockchainUpdateMemberResponse)

    async def update_node(
        self,
        request: ManagedBlockchainUpdateNodeRequest,
    ) -> ManagedBlockchainUpdateNodeResponse:
        client = self._require_client()
        return await self._execute(client.update_node, request, ManagedBlockchainUpdateNodeResponse)

    async def vote_on_proposal(
        self,
        request: ManagedBlockchainVoteOnProposalRequest,
    ) -> ManagedBlockchainVoteOnProposalResponse:
        client = self._require_client()
        return await self._execute(client.vote_on_proposal, request, ManagedBlockchainVoteOnProposalResponse)
