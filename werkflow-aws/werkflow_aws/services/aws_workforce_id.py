from werkflow_aws.models.workforce_id import (
    IdentityStoreCreateGroupMembershipRequest,
    IdentityStoreCreateGroupMembershipResponse,
    IdentityStoreCreateGroupRequest,
    IdentityStoreCreateGroupResponse,
    IdentityStoreCreateUserRequest,
    IdentityStoreCreateUserResponse,
    IdentityStoreDeleteGroupMembershipRequest,
    IdentityStoreDeleteGroupMembershipResponse,
    IdentityStoreDeleteGroupRequest,
    IdentityStoreDeleteGroupResponse,
    IdentityStoreDeleteUserRequest,
    IdentityStoreDeleteUserResponse,
    IdentityStoreDescribeGroupMembershipRequest,
    IdentityStoreDescribeGroupMembershipResponse,
    IdentityStoreDescribeGroupRequest,
    IdentityStoreDescribeGroupResponse,
    IdentityStoreDescribeIdentityStoreRequest,
    IdentityStoreDescribeIdentityStoreResponse,
    IdentityStoreDescribeUserRequest,
    IdentityStoreDescribeUserResponse,
    IdentityStoreGetGroupIdRequest,
    IdentityStoreGetGroupIdResponse,
    IdentityStoreGetGroupMembershipIdRequest,
    IdentityStoreGetGroupMembershipIdResponse,
    IdentityStoreGetUserIdRequest,
    IdentityStoreGetUserIdResponse,
    IdentityStoreIsMemberInGroupsRequest,
    IdentityStoreIsMemberInGroupsResponse,
    IdentityStoreListGroupMembershipsForMemberRequest,
    IdentityStoreListGroupMembershipsForMemberResponse,
    IdentityStoreListGroupMembershipsRequest,
    IdentityStoreListGroupMembershipsResponse,
    IdentityStoreListGroupsRequest,
    IdentityStoreListGroupsResponse,
    IdentityStoreListIdentityStoresRequest,
    IdentityStoreListIdentityStoresResponse,
    IdentityStoreListUsersRequest,
    IdentityStoreListUsersResponse,
    IdentityStoreUpdateGroupRequest,
    IdentityStoreUpdateGroupResponse,
    IdentityStoreUpdateIdentityStoreRequest,
    IdentityStoreUpdateIdentityStoreResponse,
    IdentityStoreUpdateUserRequest,
    IdentityStoreUpdateUserResponse,
)
from werkflow_aws.types.workforce_id_client import IdentityStoreClient
from .base import AWSBaseService


class AWSIdentityStore(AWSBaseService[IdentityStoreClient]):
    service_name = 'workforce-id'
    boto3_service_name = 'identitystore'

    def __init__(self) -> None:
        super().__init__(service_name='workforce-id', boto3_service_name='identitystore')

    async def create_group(
        self,
        request: IdentityStoreCreateGroupRequest,
    ) -> IdentityStoreCreateGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_group, request, IdentityStoreCreateGroupResponse)

    async def create_group_membership(
        self,
        request: IdentityStoreCreateGroupMembershipRequest,
    ) -> IdentityStoreCreateGroupMembershipResponse:
        client = self._require_client()
        return await self._execute(client.create_group_membership, request, IdentityStoreCreateGroupMembershipResponse)

    async def create_user(
        self,
        request: IdentityStoreCreateUserRequest,
    ) -> IdentityStoreCreateUserResponse:
        client = self._require_client()
        return await self._execute(client.create_user, request, IdentityStoreCreateUserResponse)

    async def delete_group(
        self,
        request: IdentityStoreDeleteGroupRequest,
    ) -> IdentityStoreDeleteGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_group, request, IdentityStoreDeleteGroupResponse)

    async def delete_group_membership(
        self,
        request: IdentityStoreDeleteGroupMembershipRequest,
    ) -> IdentityStoreDeleteGroupMembershipResponse:
        client = self._require_client()
        return await self._execute(client.delete_group_membership, request, IdentityStoreDeleteGroupMembershipResponse)

    async def delete_user(
        self,
        request: IdentityStoreDeleteUserRequest,
    ) -> IdentityStoreDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.delete_user, request, IdentityStoreDeleteUserResponse)

    async def describe_group(
        self,
        request: IdentityStoreDescribeGroupRequest,
    ) -> IdentityStoreDescribeGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_group, request, IdentityStoreDescribeGroupResponse)

    async def describe_group_membership(
        self,
        request: IdentityStoreDescribeGroupMembershipRequest,
    ) -> IdentityStoreDescribeGroupMembershipResponse:
        client = self._require_client()
        return await self._execute(client.describe_group_membership, request, IdentityStoreDescribeGroupMembershipResponse)

    async def describe_identity_store(
        self,
        request: IdentityStoreDescribeIdentityStoreRequest,
    ) -> IdentityStoreDescribeIdentityStoreResponse:
        client = self._require_client()
        return await self._execute(client.describe_identity_store, request, IdentityStoreDescribeIdentityStoreResponse)

    async def describe_user(
        self,
        request: IdentityStoreDescribeUserRequest,
    ) -> IdentityStoreDescribeUserResponse:
        client = self._require_client()
        return await self._execute(client.describe_user, request, IdentityStoreDescribeUserResponse)

    async def get_group_id(
        self,
        request: IdentityStoreGetGroupIdRequest,
    ) -> IdentityStoreGetGroupIdResponse:
        client = self._require_client()
        return await self._execute(client.get_group_id, request, IdentityStoreGetGroupIdResponse)

    async def get_group_membership_id(
        self,
        request: IdentityStoreGetGroupMembershipIdRequest,
    ) -> IdentityStoreGetGroupMembershipIdResponse:
        client = self._require_client()
        return await self._execute(client.get_group_membership_id, request, IdentityStoreGetGroupMembershipIdResponse)

    async def get_user_id(
        self,
        request: IdentityStoreGetUserIdRequest,
    ) -> IdentityStoreGetUserIdResponse:
        client = self._require_client()
        return await self._execute(client.get_user_id, request, IdentityStoreGetUserIdResponse)

    async def is_member_in_groups(
        self,
        request: IdentityStoreIsMemberInGroupsRequest,
    ) -> IdentityStoreIsMemberInGroupsResponse:
        client = self._require_client()
        return await self._execute(client.is_member_in_groups, request, IdentityStoreIsMemberInGroupsResponse)

    async def list_group_memberships(
        self,
        request: IdentityStoreListGroupMembershipsRequest,
    ) -> IdentityStoreListGroupMembershipsResponse:
        client = self._require_client()
        return await self._execute(client.list_group_memberships, request, IdentityStoreListGroupMembershipsResponse)

    async def list_group_memberships_paginated(
        self,
        request: IdentityStoreListGroupMembershipsRequest,
    ) -> list[IdentityStoreListGroupMembershipsResponse]:
        return await self._paginate('list_group_memberships', request, IdentityStoreListGroupMembershipsResponse)

    async def list_group_memberships_for_member(
        self,
        request: IdentityStoreListGroupMembershipsForMemberRequest,
    ) -> IdentityStoreListGroupMembershipsForMemberResponse:
        client = self._require_client()
        return await self._execute(client.list_group_memberships_for_member, request, IdentityStoreListGroupMembershipsForMemberResponse)

    async def list_group_memberships_for_member_paginated(
        self,
        request: IdentityStoreListGroupMembershipsForMemberRequest,
    ) -> list[IdentityStoreListGroupMembershipsForMemberResponse]:
        return await self._paginate('list_group_memberships_for_member', request, IdentityStoreListGroupMembershipsForMemberResponse)

    async def list_groups(
        self,
        request: IdentityStoreListGroupsRequest,
    ) -> IdentityStoreListGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_groups, request, IdentityStoreListGroupsResponse)

    async def list_groups_paginated(
        self,
        request: IdentityStoreListGroupsRequest,
    ) -> list[IdentityStoreListGroupsResponse]:
        return await self._paginate('list_groups', request, IdentityStoreListGroupsResponse)

    async def list_identity_stores(
        self,
        request: IdentityStoreListIdentityStoresRequest | None = None,
    ) -> IdentityStoreListIdentityStoresResponse:
        client = self._require_client()
        return await self._execute(client.list_identity_stores, request, IdentityStoreListIdentityStoresResponse)

    async def list_identity_stores_paginated(
        self,
        request: IdentityStoreListIdentityStoresRequest | None = None,
    ) -> list[IdentityStoreListIdentityStoresResponse]:
        return await self._paginate('list_identity_stores', request, IdentityStoreListIdentityStoresResponse)

    async def list_users(
        self,
        request: IdentityStoreListUsersRequest,
    ) -> IdentityStoreListUsersResponse:
        client = self._require_client()
        return await self._execute(client.list_users, request, IdentityStoreListUsersResponse)

    async def list_users_paginated(
        self,
        request: IdentityStoreListUsersRequest,
    ) -> list[IdentityStoreListUsersResponse]:
        return await self._paginate('list_users', request, IdentityStoreListUsersResponse)

    async def update_group(
        self,
        request: IdentityStoreUpdateGroupRequest,
    ) -> IdentityStoreUpdateGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_group, request, IdentityStoreUpdateGroupResponse)

    async def update_identity_store(
        self,
        request: IdentityStoreUpdateIdentityStoreRequest,
    ) -> IdentityStoreUpdateIdentityStoreResponse:
        client = self._require_client()
        return await self._execute(client.update_identity_store, request, IdentityStoreUpdateIdentityStoreResponse)

    async def update_user(
        self,
        request: IdentityStoreUpdateUserRequest,
    ) -> IdentityStoreUpdateUserResponse:
        client = self._require_client()
        return await self._execute(client.update_user, request, IdentityStoreUpdateUserResponse)
