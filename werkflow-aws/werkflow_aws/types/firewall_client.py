from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class FMSClient(ABC):

    @abstractmethod
    def associate_admin_account(
        self,
        *,
        AdminAccount: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_third_party_firewall(
        self,
        *,
        ThirdPartyFirewall: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_associate_resource(
        self,
        *,
        ResourceSetIdentifier: str,
        Items: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_disassociate_resource(
        self,
        *,
        ResourceSetIdentifier: str,
        Items: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_apps_list(
        self,
        *,
        ListId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_notification_channel(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy(
        self,
        *,
        PolicyId: str,
        DeleteAllPolicyResources: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_protocols_list(
        self,
        *,
        ListId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_set(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_admin_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_third_party_firewall(
        self,
        *,
        ThirdPartyFirewall: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_admin_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_admin_scope(
        self,
        *,
        AdminAccount: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_apps_list(
        self,
        *,
        ListId: str,
        DefaultList: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_compliance_detail(
        self,
        *,
        PolicyId: str,
        MemberAccount: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_notification_channel(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy(
        self,
        *,
        PolicyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_protection_status(
        self,
        *,
        PolicyId: str,
        MemberAccountId: str | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_protocols_list(
        self,
        *,
        ListId: str,
        DefaultList: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_set(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_third_party_firewall_association_status(
        self,
        *,
        ThirdPartyFirewall: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_violation_details(
        self,
        *,
        PolicyId: str,
        MemberAccount: str,
        ResourceId: str,
        ResourceType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_admin_accounts_for_organization(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_admins_managing_account(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_apps_lists(
        self,
        *,
        MaxResults: int,
        DefaultLists: bool | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_compliance_status(
        self,
        *,
        PolicyId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_discovered_resources(
        self,
        *,
        MemberAccountIds: list[str],
        ResourceType: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_member_accounts(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policies(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_protocols_lists(
        self,
        *,
        MaxResults: int,
        DefaultLists: bool | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_set_resources(
        self,
        *,
        Identifier: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_sets(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
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
    def list_third_party_firewall_firewall_policies(
        self,
        *,
        ThirdPartyFirewall: str,
        MaxResults: int,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_admin_account(
        self,
        *,
        AdminAccount: str,
        AdminScope: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_apps_list(
        self,
        *,
        AppsList: dict[str, Any],
        TagList: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_notification_channel(
        self,
        *,
        SnsTopicArn: str,
        SnsRoleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_policy(
        self,
        *,
        Policy: dict[str, Any],
        TagList: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_protocols_list(
        self,
        *,
        ProtocolsList: dict[str, Any],
        TagList: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_set(
        self,
        *,
        ResourceSet: dict[str, Any],
        TagList: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        TagList: list[dict[str, Any]],
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
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
