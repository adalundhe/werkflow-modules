from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class OrganizationsClient(ABC):

    @abstractmethod
    def list_accounts(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account(
        self,
        *,
        AccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_roots(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_organizational_units_for_parent(
        self,
        *,
        ParentId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_accounts_for_parent(
        self,
        *,
        ParentId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policies(
        self,
        *,
        Filter: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_policy(
        self,
        *,
        PolicyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceId: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceId: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceId: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_handshake(
        self,
        *,
        HandshakeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_policy(
        self,
        *,
        PolicyId: str,
        TargetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_handshake(
        self,
        *,
        HandshakeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def close_account(
        self,
        *,
        AccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_account(
        self,
        *,
        Email: str,
        AccountName: str,
        RoleName: str | None = None,
        IamUserAccessToBilling: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_gov_cloud_account(
        self,
        *,
        Email: str,
        AccountName: str,
        RoleName: str | None = None,
        IamUserAccessToBilling: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_organization(
        self,
        *,
        FeatureSet: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_organizational_unit(
        self,
        *,
        ParentId: str,
        Name: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_policy(
        self,
        *,
        Content: str,
        Description: str,
        Name: str,
        Type: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def decline_handshake(
        self,
        *,
        HandshakeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_organization(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_organizational_unit(
        self,
        *,
        OrganizationalUnitId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy(
        self,
        *,
        PolicyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_delegated_administrator(
        self,
        *,
        AccountId: str,
        ServicePrincipal: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_create_account_status(
        self,
        *,
        CreateAccountRequestId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_effective_policy(
        self,
        *,
        PolicyType: str,
        TargetId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_handshake(
        self,
        *,
        HandshakeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organizational_unit(
        self,
        *,
        OrganizationalUnitId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resource_policy(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_responsibility_transfer(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_policy(
        self,
        *,
        PolicyId: str,
        TargetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_aws_service_access(
        self,
        *,
        ServicePrincipal: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_policy_type(
        self,
        *,
        RootId: str,
        PolicyType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_aws_service_access(
        self,
        *,
        ServicePrincipal: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_all_features(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_policy_type(
        self,
        *,
        RootId: str,
        PolicyType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invite_account_to_organization(
        self,
        *,
        Target: dict[str, Any],
        Notes: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invite_organization_to_transfer_responsibility(
        self,
        *,
        Type: str,
        Target: dict[str, Any],
        StartTimestamp: datetime.datetime | str,
        SourceName: str,
        Notes: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def leave_organization(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_aws_service_access_for_organization(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_accounts_with_invalid_effective_policy(
        self,
        *,
        PolicyType: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_children(
        self,
        *,
        ParentId: str,
        ChildType: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_create_account_status(
        self,
        *,
        States: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_delegated_administrators(
        self,
        *,
        ServicePrincipal: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_delegated_services_for_account(
        self,
        *,
        AccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_effective_policy_validation_errors(
        self,
        *,
        AccountId: str,
        PolicyType: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_handshakes_for_account(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_handshakes_for_organization(
        self,
        *,
        Filter: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_inbound_responsibility_transfers(
        self,
        *,
        Type: str,
        Id: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_outbound_responsibility_transfers(
        self,
        *,
        Type: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_parents(
        self,
        *,
        ChildId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policies_for_target(
        self,
        *,
        TargetId: str,
        Filter: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_targets_for_policy(
        self,
        *,
        PolicyId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def move_account(
        self,
        *,
        AccountId: str,
        SourceParentId: str,
        DestinationParentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        Content: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_delegated_administrator(
        self,
        *,
        AccountId: str,
        ServicePrincipal: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_account_from_organization(
        self,
        *,
        AccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_responsibility_transfer(
        self,
        *,
        Id: str,
        EndTimestamp: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_organizational_unit(
        self,
        *,
        OrganizationalUnitId: str,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_policy(
        self,
        *,
        PolicyId: str,
        Name: str | None = None,
        Description: str | None = None,
        Content: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_responsibility_transfer(
        self,
        *,
        Id: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
