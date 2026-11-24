from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class DetectiveClient(ABC):

    @abstractmethod
    def accept_invitation(
        self,
        *,
        GraphArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_graph_member_datasources(
        self,
        *,
        GraphArn: str,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_membership_datasources(
        self,
        *,
        GraphArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_graph(
        self,
        *,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_members(
        self,
        *,
        GraphArn: str,
        Accounts: list[dict[str, Any]],
        Message: str | None = None,
        DisableEmailNotification: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_graph(
        self,
        *,
        GraphArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_members(
        self,
        *,
        GraphArn: str,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organization_configuration(
        self,
        *,
        GraphArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_organization_admin_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_membership(
        self,
        *,
        GraphArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_organization_admin_account(
        self,
        *,
        AccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_investigation(
        self,
        *,
        GraphArn: str,
        InvestigationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_members(
        self,
        *,
        GraphArn: str,
        AccountIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_datasource_packages(
        self,
        *,
        GraphArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_graphs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_indicators(
        self,
        *,
        GraphArn: str,
        InvestigationId: str,
        IndicatorType: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_investigations(
        self,
        *,
        GraphArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        FilterCriteria: dict[str, Any] | None = None,
        SortCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_invitations(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_members(
        self,
        *,
        GraphArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_organization_admin_accounts(
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
    def reject_invitation(
        self,
        *,
        GraphArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_investigation(
        self,
        *,
        GraphArn: str,
        EntityArn: str,
        ScopeStartTime: datetime.datetime | str,
        ScopeEndTime: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_monitoring_member(
        self,
        *,
        GraphArn: str,
        AccountId: str,
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
    def update_datasource_packages(
        self,
        *,
        GraphArn: str,
        DatasourcePackages: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_investigation_state(
        self,
        *,
        GraphArn: str,
        InvestigationId: str,
        State: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_organization_configuration(
        self,
        *,
        GraphArn: str,
        AutoEnable: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
