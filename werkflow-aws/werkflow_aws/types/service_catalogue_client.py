from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class ServiceCatalogClient(ABC):

    @abstractmethod
    def accept_portfolio_share(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str | None = None,
        PortfolioShareType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_budget_with_resource(
        self,
        *,
        BudgetName: str,
        ResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_principal_with_portfolio(
        self,
        *,
        PortfolioId: str,
        PrincipalARN: str,
        PrincipalType: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_product_with_portfolio(
        self,
        *,
        ProductId: str,
        PortfolioId: str,
        AcceptLanguage: str | None = None,
        SourcePortfolioId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_service_action_with_provisioning_artifact(
        self,
        *,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str | None = None,
        IdempotencyToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_tag_option_with_resource(
        self,
        *,
        ResourceId: str,
        TagOptionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_associate_service_action_with_provisioning_artifact(
        self,
        *,
        ServiceActionAssociations: list[dict[str, Any]],
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_disassociate_service_action_from_provisioning_artifact(
        self,
        *,
        ServiceActionAssociations: list[dict[str, Any]],
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_product(
        self,
        *,
        SourceProductArn: str,
        IdempotencyToken: str,
        AcceptLanguage: str | None = None,
        TargetProductId: str | None = None,
        TargetProductName: str | None = None,
        SourceProvisioningArtifactIdentifiers: list[dict[str, str]] | None = None,
        CopyOptions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_constraint(
        self,
        *,
        PortfolioId: str,
        ProductId: str,
        Parameters: str,
        Type: str,
        IdempotencyToken: str,
        AcceptLanguage: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_portfolio(
        self,
        *,
        DisplayName: str,
        ProviderName: str,
        IdempotencyToken: str,
        AcceptLanguage: str | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_portfolio_share(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str | None = None,
        AccountId: str | None = None,
        OrganizationNode: dict[str, Any] | None = None,
        ShareTagOptions: bool | None = None,
        SharePrincipals: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_product(
        self,
        *,
        Name: str,
        Owner: str,
        ProductType: str,
        IdempotencyToken: str,
        AcceptLanguage: str | None = None,
        Description: str | None = None,
        Distributor: str | None = None,
        SupportDescription: str | None = None,
        SupportEmail: str | None = None,
        SupportUrl: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ProvisioningArtifactParameters: dict[str, Any] | None = None,
        SourceConnection: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_provisioned_product_plan(
        self,
        *,
        PlanName: str,
        PlanType: str,
        ProductId: str,
        ProvisionedProductName: str,
        ProvisioningArtifactId: str,
        IdempotencyToken: str,
        AcceptLanguage: str | None = None,
        NotificationArns: list[str] | None = None,
        PathId: str | None = None,
        ProvisioningParameters: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_provisioning_artifact(
        self,
        *,
        ProductId: str,
        Parameters: dict[str, Any],
        IdempotencyToken: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_service_action(
        self,
        *,
        Name: str,
        DefinitionType: str,
        Definition: dict[str, str],
        IdempotencyToken: str,
        Description: str | None = None,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tag_option(
        self,
        *,
        Key: str,
        Value: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_constraint(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_portfolio(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_portfolio_share(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str | None = None,
        AccountId: str | None = None,
        OrganizationNode: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_product(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_provisioned_product_plan(
        self,
        *,
        PlanId: str,
        AcceptLanguage: str | None = None,
        IgnoreErrors: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_provisioning_artifact(
        self,
        *,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_service_action(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
        IdempotencyToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tag_option(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_constraint(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_copy_product_status(
        self,
        *,
        CopyProductToken: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_portfolio(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_portfolio_share_status(
        self,
        *,
        PortfolioShareToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_portfolio_shares(
        self,
        *,
        PortfolioId: str,
        Type: str,
        PageToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_product(
        self,
        *,
        AcceptLanguage: str | None = None,
        Id: str | None = None,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_product_as_admin(
        self,
        *,
        AcceptLanguage: str | None = None,
        Id: str | None = None,
        Name: str | None = None,
        SourcePortfolioId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_product_view(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_provisioned_product(
        self,
        *,
        AcceptLanguage: str | None = None,
        Id: str | None = None,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_provisioned_product_plan(
        self,
        *,
        PlanId: str,
        AcceptLanguage: str | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_provisioning_artifact(
        self,
        *,
        AcceptLanguage: str | None = None,
        ProvisioningArtifactId: str | None = None,
        ProductId: str | None = None,
        ProvisioningArtifactName: str | None = None,
        ProductName: str | None = None,
        Verbose: bool | None = None,
        IncludeProvisioningArtifactParameters: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_provisioning_parameters(
        self,
        *,
        AcceptLanguage: str | None = None,
        ProductId: str | None = None,
        ProductName: str | None = None,
        ProvisioningArtifactId: str | None = None,
        ProvisioningArtifactName: str | None = None,
        PathId: str | None = None,
        PathName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_record(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
        PageToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service_action(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service_action_execution_parameters(
        self,
        *,
        ProvisionedProductId: str,
        ServiceActionId: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tag_option(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_aws_organizations_access(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_budget_from_resource(
        self,
        *,
        BudgetName: str,
        ResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_principal_from_portfolio(
        self,
        *,
        PortfolioId: str,
        PrincipalARN: str,
        AcceptLanguage: str | None = None,
        PrincipalType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_product_from_portfolio(
        self,
        *,
        ProductId: str,
        PortfolioId: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_service_action_from_provisioning_artifact(
        self,
        *,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str | None = None,
        IdempotencyToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_tag_option_from_resource(
        self,
        *,
        ResourceId: str,
        TagOptionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_aws_organizations_access(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute_provisioned_product_plan(
        self,
        *,
        PlanId: str,
        IdempotencyToken: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute_provisioned_product_service_action(
        self,
        *,
        ProvisionedProductId: str,
        ServiceActionId: str,
        ExecuteToken: str,
        AcceptLanguage: str | None = None,
        Parameters: dict[str, list[str]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_aws_organizations_access_status(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_provisioned_product_outputs(
        self,
        *,
        AcceptLanguage: str | None = None,
        ProvisionedProductId: str | None = None,
        ProvisionedProductName: str | None = None,
        OutputKeys: list[str] | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_as_provisioned_product(
        self,
        *,
        ProductId: str,
        ProvisioningArtifactId: str,
        ProvisionedProductName: str,
        PhysicalId: str,
        IdempotencyToken: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_accepted_portfolio_shares(
        self,
        *,
        AcceptLanguage: str | None = None,
        PageToken: str | None = None,
        PageSize: int | None = None,
        PortfolioShareType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_budgets_for_resource(
        self,
        *,
        ResourceId: str,
        AcceptLanguage: str | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_constraints_for_portfolio(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str | None = None,
        ProductId: str | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_launch_paths(
        self,
        *,
        ProductId: str,
        AcceptLanguage: str | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_organization_portfolio_access(
        self,
        *,
        PortfolioId: str,
        OrganizationNodeType: str,
        AcceptLanguage: str | None = None,
        PageToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_portfolio_access(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str | None = None,
        OrganizationParentId: str | None = None,
        PageToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_portfolios(
        self,
        *,
        AcceptLanguage: str | None = None,
        PageToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_portfolios_for_product(
        self,
        *,
        ProductId: str,
        AcceptLanguage: str | None = None,
        PageToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_principals_for_portfolio(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_provisioned_product_plans(
        self,
        *,
        AcceptLanguage: str | None = None,
        ProvisionProductId: str | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
        AccessLevelFilter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_provisioning_artifacts(
        self,
        *,
        ProductId: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_provisioning_artifacts_for_service_action(
        self,
        *,
        ServiceActionId: str,
        PageSize: int | None = None,
        PageToken: str | None = None,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_record_history(
        self,
        *,
        AcceptLanguage: str | None = None,
        AccessLevelFilter: dict[str, Any] | None = None,
        SearchFilter: dict[str, Any] | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resources_for_tag_option(
        self,
        *,
        TagOptionId: str,
        ResourceType: str | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_service_actions(
        self,
        *,
        AcceptLanguage: str | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_service_actions_for_provisioning_artifact(
        self,
        *,
        ProductId: str,
        ProvisioningArtifactId: str,
        PageSize: int | None = None,
        PageToken: str | None = None,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stack_instances_for_provisioned_product(
        self,
        *,
        ProvisionedProductId: str,
        AcceptLanguage: str | None = None,
        PageToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tag_options(
        self,
        *,
        Filters: dict[str, Any] | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def notify_provision_product_engine_workflow_result(
        self,
        *,
        WorkflowToken: str,
        RecordId: str,
        Status: str,
        IdempotencyToken: str,
        FailureReason: str | None = None,
        ResourceIdentifier: dict[str, Any] | None = None,
        Outputs: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def notify_terminate_provisioned_product_engine_workflow_result(
        self,
        *,
        WorkflowToken: str,
        RecordId: str,
        Status: str,
        IdempotencyToken: str,
        FailureReason: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def notify_update_provisioned_product_engine_workflow_result(
        self,
        *,
        WorkflowToken: str,
        RecordId: str,
        Status: str,
        IdempotencyToken: str,
        FailureReason: str | None = None,
        Outputs: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def provision_product(
        self,
        *,
        ProvisionedProductName: str,
        ProvisionToken: str,
        AcceptLanguage: str | None = None,
        ProductId: str | None = None,
        ProductName: str | None = None,
        ProvisioningArtifactId: str | None = None,
        ProvisioningArtifactName: str | None = None,
        PathId: str | None = None,
        PathName: str | None = None,
        ProvisioningParameters: list[dict[str, Any]] | None = None,
        ProvisioningPreferences: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        NotificationArns: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_portfolio_share(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str | None = None,
        PortfolioShareType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def scan_provisioned_products(
        self,
        *,
        AcceptLanguage: str | None = None,
        AccessLevelFilter: dict[str, Any] | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_products(
        self,
        *,
        AcceptLanguage: str | None = None,
        Filters: dict[str, list[str]] | None = None,
        PageSize: int | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_products_as_admin(
        self,
        *,
        AcceptLanguage: str | None = None,
        PortfolioId: str | None = None,
        Filters: dict[str, list[str]] | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        PageToken: str | None = None,
        PageSize: int | None = None,
        ProductSource: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_provisioned_products(
        self,
        *,
        AcceptLanguage: str | None = None,
        AccessLevelFilter: dict[str, Any] | None = None,
        Filters: dict[str, list[str]] | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        PageSize: int | None = None,
        PageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_provisioned_product(
        self,
        *,
        TerminateToken: str,
        ProvisionedProductName: str | None = None,
        ProvisionedProductId: str | None = None,
        IgnoreErrors: bool | None = None,
        AcceptLanguage: str | None = None,
        RetainPhysicalResources: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_constraint(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
        Description: str | None = None,
        Parameters: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_portfolio(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
        DisplayName: str | None = None,
        Description: str | None = None,
        ProviderName: str | None = None,
        AddTags: list[dict[str, Any]] | None = None,
        RemoveTags: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_portfolio_share(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str | None = None,
        AccountId: str | None = None,
        OrganizationNode: dict[str, Any] | None = None,
        ShareTagOptions: bool | None = None,
        SharePrincipals: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_product(
        self,
        *,
        Id: str,
        AcceptLanguage: str | None = None,
        Name: str | None = None,
        Owner: str | None = None,
        Description: str | None = None,
        Distributor: str | None = None,
        SupportDescription: str | None = None,
        SupportEmail: str | None = None,
        SupportUrl: str | None = None,
        AddTags: list[dict[str, Any]] | None = None,
        RemoveTags: list[str] | None = None,
        SourceConnection: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_provisioned_product(
        self,
        *,
        UpdateToken: str,
        AcceptLanguage: str | None = None,
        ProvisionedProductName: str | None = None,
        ProvisionedProductId: str | None = None,
        ProductId: str | None = None,
        ProductName: str | None = None,
        ProvisioningArtifactId: str | None = None,
        ProvisioningArtifactName: str | None = None,
        PathId: str | None = None,
        PathName: str | None = None,
        ProvisioningParameters: list[dict[str, Any]] | None = None,
        ProvisioningPreferences: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_provisioned_product_properties(
        self,
        *,
        ProvisionedProductId: str,
        ProvisionedProductProperties: dict[str, str],
        IdempotencyToken: str,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_provisioning_artifact(
        self,
        *,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str | None = None,
        Name: str | None = None,
        Description: str | None = None,
        Active: bool | None = None,
        Guidance: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_service_action(
        self,
        *,
        Id: str,
        Name: str | None = None,
        Definition: dict[str, str] | None = None,
        Description: str | None = None,
        AcceptLanguage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_tag_option(
        self,
        *,
        Id: str,
        Value: str | None = None,
        Active: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
