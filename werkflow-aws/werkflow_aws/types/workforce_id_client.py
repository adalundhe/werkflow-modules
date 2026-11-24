from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class IdentityStoreClient(ABC):

    @abstractmethod
    def create_group(
        self,
        *,
        IdentityStoreId: str,
        DisplayName: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_group_membership(
        self,
        *,
        IdentityStoreId: str,
        GroupId: str,
        MemberId: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user(
        self,
        *,
        IdentityStoreId: str,
        UserName: str | None = None,
        Name: dict[str, Any] | None = None,
        DisplayName: str | None = None,
        NickName: str | None = None,
        ProfileUrl: str | None = None,
        Emails: list[dict[str, Any]] | None = None,
        Addresses: list[dict[str, Any]] | None = None,
        PhoneNumbers: list[dict[str, Any]] | None = None,
        UserType: str | None = None,
        Title: str | None = None,
        PreferredLanguage: str | None = None,
        Locale: str | None = None,
        Timezone: str | None = None,
        Photos: list[dict[str, Any]] | None = None,
        Website: str | None = None,
        Birthdate: str | None = None,
        Roles: list[dict[str, Any]] | None = None,
        Extensions: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_group(
        self,
        *,
        IdentityStoreId: str,
        GroupId: str,
        Revision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_group_membership(
        self,
        *,
        IdentityStoreId: str,
        MembershipId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        IdentityStoreId: str,
        UserId: str,
        Revision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_group(
        self,
        *,
        IdentityStoreId: str,
        GroupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_group_membership(
        self,
        *,
        IdentityStoreId: str,
        MembershipId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_identity_store(
        self,
        *,
        IdentityStoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user(
        self,
        *,
        IdentityStoreId: str,
        UserId: str,
        Extensions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_group_id(
        self,
        *,
        IdentityStoreId: str,
        AlternateIdentifier: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_group_membership_id(
        self,
        *,
        IdentityStoreId: str,
        GroupId: str,
        MemberId: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_id(
        self,
        *,
        IdentityStoreId: str,
        AlternateIdentifier: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def is_member_in_groups(
        self,
        *,
        IdentityStoreId: str,
        MemberId: dict[str, Any],
        GroupIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_group_memberships(
        self,
        *,
        IdentityStoreId: str,
        GroupId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_group_memberships_for_member(
        self,
        *,
        IdentityStoreId: str,
        MemberId: dict[str, Any],
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_groups(
        self,
        *,
        IdentityStoreId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_identity_stores(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_users(
        self,
        *,
        IdentityStoreId: str,
        Extensions: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_group(
        self,
        *,
        IdentityStoreId: str,
        GroupId: str,
        Operations: list[dict[str, Any]],
        Revision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_identity_store(
        self,
        *,
        IdentityStoreId: str,
        NetworkConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user(
        self,
        *,
        IdentityStoreId: str,
        UserId: str,
        Operations: list[dict[str, Any]],
        Revision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
