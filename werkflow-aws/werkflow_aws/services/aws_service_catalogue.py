from werkflow_aws.models.service_catalogue import (
    ServiceCatalogAcceptPortfolioShareRequest,
    ServiceCatalogAcceptPortfolioShareResponse,
    ServiceCatalogAssociateBudgetWithResourceRequest,
    ServiceCatalogAssociateBudgetWithResourceResponse,
    ServiceCatalogAssociatePrincipalWithPortfolioRequest,
    ServiceCatalogAssociatePrincipalWithPortfolioResponse,
    ServiceCatalogAssociateProductWithPortfolioRequest,
    ServiceCatalogAssociateProductWithPortfolioResponse,
    ServiceCatalogAssociateServiceActionWithProvisioningArtifactRequest,
    ServiceCatalogAssociateServiceActionWithProvisioningArtifactResponse,
    ServiceCatalogAssociateTagOptionWithResourceRequest,
    ServiceCatalogAssociateTagOptionWithResourceResponse,
    ServiceCatalogBatchAssociateServiceActionWithProvisioningArtifactRequest,
    ServiceCatalogBatchAssociateServiceActionWithProvisioningArtifactResponse,
    ServiceCatalogBatchDisassociateServiceActionFromProvisioningArtifactRequest,
    ServiceCatalogBatchDisassociateServiceActionFromProvisioningArtifactResponse,
    ServiceCatalogCopyProductRequest,
    ServiceCatalogCopyProductResponse,
    ServiceCatalogCreateConstraintRequest,
    ServiceCatalogCreateConstraintResponse,
    ServiceCatalogCreatePortfolioRequest,
    ServiceCatalogCreatePortfolioResponse,
    ServiceCatalogCreatePortfolioShareRequest,
    ServiceCatalogCreatePortfolioShareResponse,
    ServiceCatalogCreateProductRequest,
    ServiceCatalogCreateProductResponse,
    ServiceCatalogCreateProvisionedProductPlanRequest,
    ServiceCatalogCreateProvisionedProductPlanResponse,
    ServiceCatalogCreateProvisioningArtifactRequest,
    ServiceCatalogCreateProvisioningArtifactResponse,
    ServiceCatalogCreateServiceActionRequest,
    ServiceCatalogCreateServiceActionResponse,
    ServiceCatalogCreateTagOptionRequest,
    ServiceCatalogCreateTagOptionResponse,
    ServiceCatalogDeleteConstraintRequest,
    ServiceCatalogDeleteConstraintResponse,
    ServiceCatalogDeletePortfolioRequest,
    ServiceCatalogDeletePortfolioResponse,
    ServiceCatalogDeletePortfolioShareRequest,
    ServiceCatalogDeletePortfolioShareResponse,
    ServiceCatalogDeleteProductRequest,
    ServiceCatalogDeleteProductResponse,
    ServiceCatalogDeleteProvisionedProductPlanRequest,
    ServiceCatalogDeleteProvisionedProductPlanResponse,
    ServiceCatalogDeleteProvisioningArtifactRequest,
    ServiceCatalogDeleteProvisioningArtifactResponse,
    ServiceCatalogDeleteServiceActionRequest,
    ServiceCatalogDeleteServiceActionResponse,
    ServiceCatalogDeleteTagOptionRequest,
    ServiceCatalogDeleteTagOptionResponse,
    ServiceCatalogDescribeConstraintRequest,
    ServiceCatalogDescribeConstraintResponse,
    ServiceCatalogDescribeCopyProductStatusRequest,
    ServiceCatalogDescribeCopyProductStatusResponse,
    ServiceCatalogDescribePortfolioRequest,
    ServiceCatalogDescribePortfolioResponse,
    ServiceCatalogDescribePortfolioShareStatusRequest,
    ServiceCatalogDescribePortfolioShareStatusResponse,
    ServiceCatalogDescribePortfolioSharesRequest,
    ServiceCatalogDescribePortfolioSharesResponse,
    ServiceCatalogDescribeProductAsAdminRequest,
    ServiceCatalogDescribeProductAsAdminResponse,
    ServiceCatalogDescribeProductRequest,
    ServiceCatalogDescribeProductResponse,
    ServiceCatalogDescribeProductViewRequest,
    ServiceCatalogDescribeProductViewResponse,
    ServiceCatalogDescribeProvisionedProductPlanRequest,
    ServiceCatalogDescribeProvisionedProductPlanResponse,
    ServiceCatalogDescribeProvisionedProductRequest,
    ServiceCatalogDescribeProvisionedProductResponse,
    ServiceCatalogDescribeProvisioningArtifactRequest,
    ServiceCatalogDescribeProvisioningArtifactResponse,
    ServiceCatalogDescribeProvisioningParametersRequest,
    ServiceCatalogDescribeProvisioningParametersResponse,
    ServiceCatalogDescribeRecordRequest,
    ServiceCatalogDescribeRecordResponse,
    ServiceCatalogDescribeServiceActionExecutionParametersRequest,
    ServiceCatalogDescribeServiceActionExecutionParametersResponse,
    ServiceCatalogDescribeServiceActionRequest,
    ServiceCatalogDescribeServiceActionResponse,
    ServiceCatalogDescribeTagOptionRequest,
    ServiceCatalogDescribeTagOptionResponse,
    ServiceCatalogDisableAWSOrganizationsAccessRequest,
    ServiceCatalogDisableAWSOrganizationsAccessResponse,
    ServiceCatalogDisassociateBudgetFromResourceRequest,
    ServiceCatalogDisassociateBudgetFromResourceResponse,
    ServiceCatalogDisassociatePrincipalFromPortfolioRequest,
    ServiceCatalogDisassociatePrincipalFromPortfolioResponse,
    ServiceCatalogDisassociateProductFromPortfolioRequest,
    ServiceCatalogDisassociateProductFromPortfolioResponse,
    ServiceCatalogDisassociateServiceActionFromProvisioningArtifactRequest,
    ServiceCatalogDisassociateServiceActionFromProvisioningArtifactResponse,
    ServiceCatalogDisassociateTagOptionFromResourceRequest,
    ServiceCatalogDisassociateTagOptionFromResourceResponse,
    ServiceCatalogEnableAWSOrganizationsAccessRequest,
    ServiceCatalogEnableAWSOrganizationsAccessResponse,
    ServiceCatalogExecuteProvisionedProductPlanRequest,
    ServiceCatalogExecuteProvisionedProductPlanResponse,
    ServiceCatalogExecuteProvisionedProductServiceActionRequest,
    ServiceCatalogExecuteProvisionedProductServiceActionResponse,
    ServiceCatalogGetAWSOrganizationsAccessStatusRequest,
    ServiceCatalogGetAWSOrganizationsAccessStatusResponse,
    ServiceCatalogGetProvisionedProductOutputsRequest,
    ServiceCatalogGetProvisionedProductOutputsResponse,
    ServiceCatalogImportAsProvisionedProductRequest,
    ServiceCatalogImportAsProvisionedProductResponse,
    ServiceCatalogListAcceptedPortfolioSharesRequest,
    ServiceCatalogListAcceptedPortfolioSharesResponse,
    ServiceCatalogListBudgetsForResourceRequest,
    ServiceCatalogListBudgetsForResourceResponse,
    ServiceCatalogListConstraintsForPortfolioRequest,
    ServiceCatalogListConstraintsForPortfolioResponse,
    ServiceCatalogListLaunchPathsRequest,
    ServiceCatalogListLaunchPathsResponse,
    ServiceCatalogListOrganizationPortfolioAccessRequest,
    ServiceCatalogListOrganizationPortfolioAccessResponse,
    ServiceCatalogListPortfolioAccessRequest,
    ServiceCatalogListPortfolioAccessResponse,
    ServiceCatalogListPortfoliosForProductRequest,
    ServiceCatalogListPortfoliosForProductResponse,
    ServiceCatalogListPortfoliosRequest,
    ServiceCatalogListPortfoliosResponse,
    ServiceCatalogListPrincipalsForPortfolioRequest,
    ServiceCatalogListPrincipalsForPortfolioResponse,
    ServiceCatalogListProvisionedProductPlansRequest,
    ServiceCatalogListProvisionedProductPlansResponse,
    ServiceCatalogListProvisioningArtifactsForServiceActionRequest,
    ServiceCatalogListProvisioningArtifactsForServiceActionResponse,
    ServiceCatalogListProvisioningArtifactsRequest,
    ServiceCatalogListProvisioningArtifactsResponse,
    ServiceCatalogListRecordHistoryRequest,
    ServiceCatalogListRecordHistoryResponse,
    ServiceCatalogListResourcesForTagOptionRequest,
    ServiceCatalogListResourcesForTagOptionResponse,
    ServiceCatalogListServiceActionsForProvisioningArtifactRequest,
    ServiceCatalogListServiceActionsForProvisioningArtifactResponse,
    ServiceCatalogListServiceActionsRequest,
    ServiceCatalogListServiceActionsResponse,
    ServiceCatalogListStackInstancesForProvisionedProductRequest,
    ServiceCatalogListStackInstancesForProvisionedProductResponse,
    ServiceCatalogListTagOptionsRequest,
    ServiceCatalogListTagOptionsResponse,
    ServiceCatalogNotifyProvisionProductEngineWorkflowResultRequest,
    ServiceCatalogNotifyProvisionProductEngineWorkflowResultResponse,
    ServiceCatalogNotifyTerminateProvisionedProductEngineWorkflowResultRequest,
    ServiceCatalogNotifyTerminateProvisionedProductEngineWorkflowResultResponse,
    ServiceCatalogNotifyUpdateProvisionedProductEngineWorkflowResultRequest,
    ServiceCatalogNotifyUpdateProvisionedProductEngineWorkflowResultResponse,
    ServiceCatalogProvisionProductRequest,
    ServiceCatalogProvisionProductResponse,
    ServiceCatalogRejectPortfolioShareRequest,
    ServiceCatalogRejectPortfolioShareResponse,
    ServiceCatalogScanProvisionedProductsRequest,
    ServiceCatalogScanProvisionedProductsResponse,
    ServiceCatalogSearchProductsAsAdminRequest,
    ServiceCatalogSearchProductsAsAdminResponse,
    ServiceCatalogSearchProductsRequest,
    ServiceCatalogSearchProductsResponse,
    ServiceCatalogSearchProvisionedProductsRequest,
    ServiceCatalogSearchProvisionedProductsResponse,
    ServiceCatalogTerminateProvisionedProductRequest,
    ServiceCatalogTerminateProvisionedProductResponse,
    ServiceCatalogUpdateConstraintRequest,
    ServiceCatalogUpdateConstraintResponse,
    ServiceCatalogUpdatePortfolioRequest,
    ServiceCatalogUpdatePortfolioResponse,
    ServiceCatalogUpdatePortfolioShareRequest,
    ServiceCatalogUpdatePortfolioShareResponse,
    ServiceCatalogUpdateProductRequest,
    ServiceCatalogUpdateProductResponse,
    ServiceCatalogUpdateProvisionedProductPropertiesRequest,
    ServiceCatalogUpdateProvisionedProductPropertiesResponse,
    ServiceCatalogUpdateProvisionedProductRequest,
    ServiceCatalogUpdateProvisionedProductResponse,
    ServiceCatalogUpdateProvisioningArtifactRequest,
    ServiceCatalogUpdateProvisioningArtifactResponse,
    ServiceCatalogUpdateServiceActionRequest,
    ServiceCatalogUpdateServiceActionResponse,
    ServiceCatalogUpdateTagOptionRequest,
    ServiceCatalogUpdateTagOptionResponse,
)
from werkflow_aws.types.service_catalogue_client import ServiceCatalogClient
from .base import AWSBaseService


class AWSServiceCatalog(AWSBaseService[ServiceCatalogClient]):
    service_name = 'service-catalogue'
    boto3_service_name = 'servicecatalog'

    def __init__(self) -> None:
        super().__init__(service_name='service-catalogue', boto3_service_name='servicecatalog')

    async def accept_portfolio_share(
        self,
        request: ServiceCatalogAcceptPortfolioShareRequest,
    ) -> ServiceCatalogAcceptPortfolioShareResponse:
        client = self._require_client()
        return await self._execute(client.accept_portfolio_share, request, ServiceCatalogAcceptPortfolioShareResponse)

    async def associate_budget_with_resource(
        self,
        request: ServiceCatalogAssociateBudgetWithResourceRequest,
    ) -> ServiceCatalogAssociateBudgetWithResourceResponse:
        client = self._require_client()
        return await self._execute(client.associate_budget_with_resource, request, ServiceCatalogAssociateBudgetWithResourceResponse)

    async def associate_principal_with_portfolio(
        self,
        request: ServiceCatalogAssociatePrincipalWithPortfolioRequest,
    ) -> ServiceCatalogAssociatePrincipalWithPortfolioResponse:
        client = self._require_client()
        return await self._execute(client.associate_principal_with_portfolio, request, ServiceCatalogAssociatePrincipalWithPortfolioResponse)

    async def associate_product_with_portfolio(
        self,
        request: ServiceCatalogAssociateProductWithPortfolioRequest,
    ) -> ServiceCatalogAssociateProductWithPortfolioResponse:
        client = self._require_client()
        return await self._execute(client.associate_product_with_portfolio, request, ServiceCatalogAssociateProductWithPortfolioResponse)

    async def associate_service_action_with_provisioning_artifact(
        self,
        request: ServiceCatalogAssociateServiceActionWithProvisioningArtifactRequest,
    ) -> ServiceCatalogAssociateServiceActionWithProvisioningArtifactResponse:
        client = self._require_client()
        return await self._execute(client.associate_service_action_with_provisioning_artifact, request, ServiceCatalogAssociateServiceActionWithProvisioningArtifactResponse)

    async def associate_tag_option_with_resource(
        self,
        request: ServiceCatalogAssociateTagOptionWithResourceRequest,
    ) -> ServiceCatalogAssociateTagOptionWithResourceResponse:
        client = self._require_client()
        return await self._execute(client.associate_tag_option_with_resource, request, ServiceCatalogAssociateTagOptionWithResourceResponse)

    async def batch_associate_service_action_with_provisioning_artifact(
        self,
        request: ServiceCatalogBatchAssociateServiceActionWithProvisioningArtifactRequest,
    ) -> ServiceCatalogBatchAssociateServiceActionWithProvisioningArtifactResponse:
        client = self._require_client()
        return await self._execute(client.batch_associate_service_action_with_provisioning_artifact, request, ServiceCatalogBatchAssociateServiceActionWithProvisioningArtifactResponse)

    async def batch_disassociate_service_action_from_provisioning_artifact(
        self,
        request: ServiceCatalogBatchDisassociateServiceActionFromProvisioningArtifactRequest,
    ) -> ServiceCatalogBatchDisassociateServiceActionFromProvisioningArtifactResponse:
        client = self._require_client()
        return await self._execute(client.batch_disassociate_service_action_from_provisioning_artifact, request, ServiceCatalogBatchDisassociateServiceActionFromProvisioningArtifactResponse)

    async def copy_product(
        self,
        request: ServiceCatalogCopyProductRequest,
    ) -> ServiceCatalogCopyProductResponse:
        client = self._require_client()
        return await self._execute(client.copy_product, request, ServiceCatalogCopyProductResponse)

    async def create_constraint(
        self,
        request: ServiceCatalogCreateConstraintRequest,
    ) -> ServiceCatalogCreateConstraintResponse:
        client = self._require_client()
        return await self._execute(client.create_constraint, request, ServiceCatalogCreateConstraintResponse)

    async def create_portfolio(
        self,
        request: ServiceCatalogCreatePortfolioRequest,
    ) -> ServiceCatalogCreatePortfolioResponse:
        client = self._require_client()
        return await self._execute(client.create_portfolio, request, ServiceCatalogCreatePortfolioResponse)

    async def create_portfolio_share(
        self,
        request: ServiceCatalogCreatePortfolioShareRequest,
    ) -> ServiceCatalogCreatePortfolioShareResponse:
        client = self._require_client()
        return await self._execute(client.create_portfolio_share, request, ServiceCatalogCreatePortfolioShareResponse)

    async def create_product(
        self,
        request: ServiceCatalogCreateProductRequest,
    ) -> ServiceCatalogCreateProductResponse:
        client = self._require_client()
        return await self._execute(client.create_product, request, ServiceCatalogCreateProductResponse)

    async def create_provisioned_product_plan(
        self,
        request: ServiceCatalogCreateProvisionedProductPlanRequest,
    ) -> ServiceCatalogCreateProvisionedProductPlanResponse:
        client = self._require_client()
        return await self._execute(client.create_provisioned_product_plan, request, ServiceCatalogCreateProvisionedProductPlanResponse)

    async def create_provisioning_artifact(
        self,
        request: ServiceCatalogCreateProvisioningArtifactRequest,
    ) -> ServiceCatalogCreateProvisioningArtifactResponse:
        client = self._require_client()
        return await self._execute(client.create_provisioning_artifact, request, ServiceCatalogCreateProvisioningArtifactResponse)

    async def create_service_action(
        self,
        request: ServiceCatalogCreateServiceActionRequest,
    ) -> ServiceCatalogCreateServiceActionResponse:
        client = self._require_client()
        return await self._execute(client.create_service_action, request, ServiceCatalogCreateServiceActionResponse)

    async def create_tag_option(
        self,
        request: ServiceCatalogCreateTagOptionRequest,
    ) -> ServiceCatalogCreateTagOptionResponse:
        client = self._require_client()
        return await self._execute(client.create_tag_option, request, ServiceCatalogCreateTagOptionResponse)

    async def delete_constraint(
        self,
        request: ServiceCatalogDeleteConstraintRequest,
    ) -> ServiceCatalogDeleteConstraintResponse:
        client = self._require_client()
        return await self._execute(client.delete_constraint, request, ServiceCatalogDeleteConstraintResponse)

    async def delete_portfolio(
        self,
        request: ServiceCatalogDeletePortfolioRequest,
    ) -> ServiceCatalogDeletePortfolioResponse:
        client = self._require_client()
        return await self._execute(client.delete_portfolio, request, ServiceCatalogDeletePortfolioResponse)

    async def delete_portfolio_share(
        self,
        request: ServiceCatalogDeletePortfolioShareRequest,
    ) -> ServiceCatalogDeletePortfolioShareResponse:
        client = self._require_client()
        return await self._execute(client.delete_portfolio_share, request, ServiceCatalogDeletePortfolioShareResponse)

    async def delete_product(
        self,
        request: ServiceCatalogDeleteProductRequest,
    ) -> ServiceCatalogDeleteProductResponse:
        client = self._require_client()
        return await self._execute(client.delete_product, request, ServiceCatalogDeleteProductResponse)

    async def delete_provisioned_product_plan(
        self,
        request: ServiceCatalogDeleteProvisionedProductPlanRequest,
    ) -> ServiceCatalogDeleteProvisionedProductPlanResponse:
        client = self._require_client()
        return await self._execute(client.delete_provisioned_product_plan, request, ServiceCatalogDeleteProvisionedProductPlanResponse)

    async def delete_provisioning_artifact(
        self,
        request: ServiceCatalogDeleteProvisioningArtifactRequest,
    ) -> ServiceCatalogDeleteProvisioningArtifactResponse:
        client = self._require_client()
        return await self._execute(client.delete_provisioning_artifact, request, ServiceCatalogDeleteProvisioningArtifactResponse)

    async def delete_service_action(
        self,
        request: ServiceCatalogDeleteServiceActionRequest,
    ) -> ServiceCatalogDeleteServiceActionResponse:
        client = self._require_client()
        return await self._execute(client.delete_service_action, request, ServiceCatalogDeleteServiceActionResponse)

    async def delete_tag_option(
        self,
        request: ServiceCatalogDeleteTagOptionRequest,
    ) -> ServiceCatalogDeleteTagOptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_tag_option, request, ServiceCatalogDeleteTagOptionResponse)

    async def describe_constraint(
        self,
        request: ServiceCatalogDescribeConstraintRequest,
    ) -> ServiceCatalogDescribeConstraintResponse:
        client = self._require_client()
        return await self._execute(client.describe_constraint, request, ServiceCatalogDescribeConstraintResponse)

    async def describe_copy_product_status(
        self,
        request: ServiceCatalogDescribeCopyProductStatusRequest,
    ) -> ServiceCatalogDescribeCopyProductStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_copy_product_status, request, ServiceCatalogDescribeCopyProductStatusResponse)

    async def describe_portfolio(
        self,
        request: ServiceCatalogDescribePortfolioRequest,
    ) -> ServiceCatalogDescribePortfolioResponse:
        client = self._require_client()
        return await self._execute(client.describe_portfolio, request, ServiceCatalogDescribePortfolioResponse)

    async def describe_portfolio_share_status(
        self,
        request: ServiceCatalogDescribePortfolioShareStatusRequest,
    ) -> ServiceCatalogDescribePortfolioShareStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_portfolio_share_status, request, ServiceCatalogDescribePortfolioShareStatusResponse)

    async def describe_portfolio_shares(
        self,
        request: ServiceCatalogDescribePortfolioSharesRequest,
    ) -> ServiceCatalogDescribePortfolioSharesResponse:
        client = self._require_client()
        return await self._execute(client.describe_portfolio_shares, request, ServiceCatalogDescribePortfolioSharesResponse)

    async def describe_product(
        self,
        request: ServiceCatalogDescribeProductRequest | None = None,
    ) -> ServiceCatalogDescribeProductResponse:
        client = self._require_client()
        return await self._execute(client.describe_product, request, ServiceCatalogDescribeProductResponse)

    async def describe_product_as_admin(
        self,
        request: ServiceCatalogDescribeProductAsAdminRequest | None = None,
    ) -> ServiceCatalogDescribeProductAsAdminResponse:
        client = self._require_client()
        return await self._execute(client.describe_product_as_admin, request, ServiceCatalogDescribeProductAsAdminResponse)

    async def describe_product_view(
        self,
        request: ServiceCatalogDescribeProductViewRequest,
    ) -> ServiceCatalogDescribeProductViewResponse:
        client = self._require_client()
        return await self._execute(client.describe_product_view, request, ServiceCatalogDescribeProductViewResponse)

    async def describe_provisioned_product(
        self,
        request: ServiceCatalogDescribeProvisionedProductRequest | None = None,
    ) -> ServiceCatalogDescribeProvisionedProductResponse:
        client = self._require_client()
        return await self._execute(client.describe_provisioned_product, request, ServiceCatalogDescribeProvisionedProductResponse)

    async def describe_provisioned_product_plan(
        self,
        request: ServiceCatalogDescribeProvisionedProductPlanRequest,
    ) -> ServiceCatalogDescribeProvisionedProductPlanResponse:
        client = self._require_client()
        return await self._execute(client.describe_provisioned_product_plan, request, ServiceCatalogDescribeProvisionedProductPlanResponse)

    async def describe_provisioning_artifact(
        self,
        request: ServiceCatalogDescribeProvisioningArtifactRequest | None = None,
    ) -> ServiceCatalogDescribeProvisioningArtifactResponse:
        client = self._require_client()
        return await self._execute(client.describe_provisioning_artifact, request, ServiceCatalogDescribeProvisioningArtifactResponse)

    async def describe_provisioning_parameters(
        self,
        request: ServiceCatalogDescribeProvisioningParametersRequest | None = None,
    ) -> ServiceCatalogDescribeProvisioningParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_provisioning_parameters, request, ServiceCatalogDescribeProvisioningParametersResponse)

    async def describe_record(
        self,
        request: ServiceCatalogDescribeRecordRequest,
    ) -> ServiceCatalogDescribeRecordResponse:
        client = self._require_client()
        return await self._execute(client.describe_record, request, ServiceCatalogDescribeRecordResponse)

    async def describe_service_action(
        self,
        request: ServiceCatalogDescribeServiceActionRequest,
    ) -> ServiceCatalogDescribeServiceActionResponse:
        client = self._require_client()
        return await self._execute(client.describe_service_action, request, ServiceCatalogDescribeServiceActionResponse)

    async def describe_service_action_execution_parameters(
        self,
        request: ServiceCatalogDescribeServiceActionExecutionParametersRequest,
    ) -> ServiceCatalogDescribeServiceActionExecutionParametersResponse:
        client = self._require_client()
        return await self._execute(client.describe_service_action_execution_parameters, request, ServiceCatalogDescribeServiceActionExecutionParametersResponse)

    async def describe_tag_option(
        self,
        request: ServiceCatalogDescribeTagOptionRequest,
    ) -> ServiceCatalogDescribeTagOptionResponse:
        client = self._require_client()
        return await self._execute(client.describe_tag_option, request, ServiceCatalogDescribeTagOptionResponse)

    async def disable_aws_organizations_access(
        self,
        request: ServiceCatalogDisableAWSOrganizationsAccessRequest | None = None,
    ) -> ServiceCatalogDisableAWSOrganizationsAccessResponse:
        client = self._require_client()
        return await self._execute(client.disable_aws_organizations_access, request, ServiceCatalogDisableAWSOrganizationsAccessResponse)

    async def disassociate_budget_from_resource(
        self,
        request: ServiceCatalogDisassociateBudgetFromResourceRequest,
    ) -> ServiceCatalogDisassociateBudgetFromResourceResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_budget_from_resource, request, ServiceCatalogDisassociateBudgetFromResourceResponse)

    async def disassociate_principal_from_portfolio(
        self,
        request: ServiceCatalogDisassociatePrincipalFromPortfolioRequest,
    ) -> ServiceCatalogDisassociatePrincipalFromPortfolioResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_principal_from_portfolio, request, ServiceCatalogDisassociatePrincipalFromPortfolioResponse)

    async def disassociate_product_from_portfolio(
        self,
        request: ServiceCatalogDisassociateProductFromPortfolioRequest,
    ) -> ServiceCatalogDisassociateProductFromPortfolioResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_product_from_portfolio, request, ServiceCatalogDisassociateProductFromPortfolioResponse)

    async def disassociate_service_action_from_provisioning_artifact(
        self,
        request: ServiceCatalogDisassociateServiceActionFromProvisioningArtifactRequest,
    ) -> ServiceCatalogDisassociateServiceActionFromProvisioningArtifactResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_service_action_from_provisioning_artifact, request, ServiceCatalogDisassociateServiceActionFromProvisioningArtifactResponse)

    async def disassociate_tag_option_from_resource(
        self,
        request: ServiceCatalogDisassociateTagOptionFromResourceRequest,
    ) -> ServiceCatalogDisassociateTagOptionFromResourceResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_tag_option_from_resource, request, ServiceCatalogDisassociateTagOptionFromResourceResponse)

    async def enable_aws_organizations_access(
        self,
        request: ServiceCatalogEnableAWSOrganizationsAccessRequest | None = None,
    ) -> ServiceCatalogEnableAWSOrganizationsAccessResponse:
        client = self._require_client()
        return await self._execute(client.enable_aws_organizations_access, request, ServiceCatalogEnableAWSOrganizationsAccessResponse)

    async def execute_provisioned_product_plan(
        self,
        request: ServiceCatalogExecuteProvisionedProductPlanRequest,
    ) -> ServiceCatalogExecuteProvisionedProductPlanResponse:
        client = self._require_client()
        return await self._execute(client.execute_provisioned_product_plan, request, ServiceCatalogExecuteProvisionedProductPlanResponse)

    async def execute_provisioned_product_service_action(
        self,
        request: ServiceCatalogExecuteProvisionedProductServiceActionRequest,
    ) -> ServiceCatalogExecuteProvisionedProductServiceActionResponse:
        client = self._require_client()
        return await self._execute(client.execute_provisioned_product_service_action, request, ServiceCatalogExecuteProvisionedProductServiceActionResponse)

    async def get_aws_organizations_access_status(
        self,
        request: ServiceCatalogGetAWSOrganizationsAccessStatusRequest | None = None,
    ) -> ServiceCatalogGetAWSOrganizationsAccessStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_aws_organizations_access_status, request, ServiceCatalogGetAWSOrganizationsAccessStatusResponse)

    async def get_provisioned_product_outputs(
        self,
        request: ServiceCatalogGetProvisionedProductOutputsRequest | None = None,
    ) -> ServiceCatalogGetProvisionedProductOutputsResponse:
        client = self._require_client()
        return await self._execute(client.get_provisioned_product_outputs, request, ServiceCatalogGetProvisionedProductOutputsResponse)

    async def import_as_provisioned_product(
        self,
        request: ServiceCatalogImportAsProvisionedProductRequest,
    ) -> ServiceCatalogImportAsProvisionedProductResponse:
        client = self._require_client()
        return await self._execute(client.import_as_provisioned_product, request, ServiceCatalogImportAsProvisionedProductResponse)

    async def list_accepted_portfolio_shares(
        self,
        request: ServiceCatalogListAcceptedPortfolioSharesRequest | None = None,
    ) -> ServiceCatalogListAcceptedPortfolioSharesResponse:
        client = self._require_client()
        return await self._execute(client.list_accepted_portfolio_shares, request, ServiceCatalogListAcceptedPortfolioSharesResponse)

    async def list_accepted_portfolio_shares_paginated(
        self,
        request: ServiceCatalogListAcceptedPortfolioSharesRequest | None = None,
    ) -> list[ServiceCatalogListAcceptedPortfolioSharesResponse]:
        return await self._paginate('list_accepted_portfolio_shares', request, ServiceCatalogListAcceptedPortfolioSharesResponse)

    async def list_budgets_for_resource(
        self,
        request: ServiceCatalogListBudgetsForResourceRequest,
    ) -> ServiceCatalogListBudgetsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_budgets_for_resource, request, ServiceCatalogListBudgetsForResourceResponse)

    async def list_constraints_for_portfolio(
        self,
        request: ServiceCatalogListConstraintsForPortfolioRequest,
    ) -> ServiceCatalogListConstraintsForPortfolioResponse:
        client = self._require_client()
        return await self._execute(client.list_constraints_for_portfolio, request, ServiceCatalogListConstraintsForPortfolioResponse)

    async def list_constraints_for_portfolio_paginated(
        self,
        request: ServiceCatalogListConstraintsForPortfolioRequest,
    ) -> list[ServiceCatalogListConstraintsForPortfolioResponse]:
        return await self._paginate('list_constraints_for_portfolio', request, ServiceCatalogListConstraintsForPortfolioResponse)

    async def list_launch_paths(
        self,
        request: ServiceCatalogListLaunchPathsRequest,
    ) -> ServiceCatalogListLaunchPathsResponse:
        client = self._require_client()
        return await self._execute(client.list_launch_paths, request, ServiceCatalogListLaunchPathsResponse)

    async def list_launch_paths_paginated(
        self,
        request: ServiceCatalogListLaunchPathsRequest,
    ) -> list[ServiceCatalogListLaunchPathsResponse]:
        return await self._paginate('list_launch_paths', request, ServiceCatalogListLaunchPathsResponse)

    async def list_organization_portfolio_access(
        self,
        request: ServiceCatalogListOrganizationPortfolioAccessRequest,
    ) -> ServiceCatalogListOrganizationPortfolioAccessResponse:
        client = self._require_client()
        return await self._execute(client.list_organization_portfolio_access, request, ServiceCatalogListOrganizationPortfolioAccessResponse)

    async def list_organization_portfolio_access_paginated(
        self,
        request: ServiceCatalogListOrganizationPortfolioAccessRequest,
    ) -> list[ServiceCatalogListOrganizationPortfolioAccessResponse]:
        return await self._paginate('list_organization_portfolio_access', request, ServiceCatalogListOrganizationPortfolioAccessResponse)

    async def list_portfolio_access(
        self,
        request: ServiceCatalogListPortfolioAccessRequest,
    ) -> ServiceCatalogListPortfolioAccessResponse:
        client = self._require_client()
        return await self._execute(client.list_portfolio_access, request, ServiceCatalogListPortfolioAccessResponse)

    async def list_portfolios(
        self,
        request: ServiceCatalogListPortfoliosRequest | None = None,
    ) -> ServiceCatalogListPortfoliosResponse:
        client = self._require_client()
        return await self._execute(client.list_portfolios, request, ServiceCatalogListPortfoliosResponse)

    async def list_portfolios_paginated(
        self,
        request: ServiceCatalogListPortfoliosRequest | None = None,
    ) -> list[ServiceCatalogListPortfoliosResponse]:
        return await self._paginate('list_portfolios', request, ServiceCatalogListPortfoliosResponse)

    async def list_portfolios_for_product(
        self,
        request: ServiceCatalogListPortfoliosForProductRequest,
    ) -> ServiceCatalogListPortfoliosForProductResponse:
        client = self._require_client()
        return await self._execute(client.list_portfolios_for_product, request, ServiceCatalogListPortfoliosForProductResponse)

    async def list_portfolios_for_product_paginated(
        self,
        request: ServiceCatalogListPortfoliosForProductRequest,
    ) -> list[ServiceCatalogListPortfoliosForProductResponse]:
        return await self._paginate('list_portfolios_for_product', request, ServiceCatalogListPortfoliosForProductResponse)

    async def list_principals_for_portfolio(
        self,
        request: ServiceCatalogListPrincipalsForPortfolioRequest,
    ) -> ServiceCatalogListPrincipalsForPortfolioResponse:
        client = self._require_client()
        return await self._execute(client.list_principals_for_portfolio, request, ServiceCatalogListPrincipalsForPortfolioResponse)

    async def list_principals_for_portfolio_paginated(
        self,
        request: ServiceCatalogListPrincipalsForPortfolioRequest,
    ) -> list[ServiceCatalogListPrincipalsForPortfolioResponse]:
        return await self._paginate('list_principals_for_portfolio', request, ServiceCatalogListPrincipalsForPortfolioResponse)

    async def list_provisioned_product_plans(
        self,
        request: ServiceCatalogListProvisionedProductPlansRequest | None = None,
    ) -> ServiceCatalogListProvisionedProductPlansResponse:
        client = self._require_client()
        return await self._execute(client.list_provisioned_product_plans, request, ServiceCatalogListProvisionedProductPlansResponse)

    async def list_provisioned_product_plans_paginated(
        self,
        request: ServiceCatalogListProvisionedProductPlansRequest | None = None,
    ) -> list[ServiceCatalogListProvisionedProductPlansResponse]:
        return await self._paginate('list_provisioned_product_plans', request, ServiceCatalogListProvisionedProductPlansResponse)

    async def list_provisioning_artifacts(
        self,
        request: ServiceCatalogListProvisioningArtifactsRequest,
    ) -> ServiceCatalogListProvisioningArtifactsResponse:
        client = self._require_client()
        return await self._execute(client.list_provisioning_artifacts, request, ServiceCatalogListProvisioningArtifactsResponse)

    async def list_provisioning_artifacts_for_service_action(
        self,
        request: ServiceCatalogListProvisioningArtifactsForServiceActionRequest,
    ) -> ServiceCatalogListProvisioningArtifactsForServiceActionResponse:
        client = self._require_client()
        return await self._execute(client.list_provisioning_artifacts_for_service_action, request, ServiceCatalogListProvisioningArtifactsForServiceActionResponse)

    async def list_provisioning_artifacts_for_service_action_paginated(
        self,
        request: ServiceCatalogListProvisioningArtifactsForServiceActionRequest,
    ) -> list[ServiceCatalogListProvisioningArtifactsForServiceActionResponse]:
        return await self._paginate('list_provisioning_artifacts_for_service_action', request, ServiceCatalogListProvisioningArtifactsForServiceActionResponse)

    async def list_record_history(
        self,
        request: ServiceCatalogListRecordHistoryRequest | None = None,
    ) -> ServiceCatalogListRecordHistoryResponse:
        client = self._require_client()
        return await self._execute(client.list_record_history, request, ServiceCatalogListRecordHistoryResponse)

    async def list_record_history_paginated(
        self,
        request: ServiceCatalogListRecordHistoryRequest | None = None,
    ) -> list[ServiceCatalogListRecordHistoryResponse]:
        return await self._paginate('list_record_history', request, ServiceCatalogListRecordHistoryResponse)

    async def list_resources_for_tag_option(
        self,
        request: ServiceCatalogListResourcesForTagOptionRequest,
    ) -> ServiceCatalogListResourcesForTagOptionResponse:
        client = self._require_client()
        return await self._execute(client.list_resources_for_tag_option, request, ServiceCatalogListResourcesForTagOptionResponse)

    async def list_resources_for_tag_option_paginated(
        self,
        request: ServiceCatalogListResourcesForTagOptionRequest,
    ) -> list[ServiceCatalogListResourcesForTagOptionResponse]:
        return await self._paginate('list_resources_for_tag_option', request, ServiceCatalogListResourcesForTagOptionResponse)

    async def list_service_actions(
        self,
        request: ServiceCatalogListServiceActionsRequest | None = None,
    ) -> ServiceCatalogListServiceActionsResponse:
        client = self._require_client()
        return await self._execute(client.list_service_actions, request, ServiceCatalogListServiceActionsResponse)

    async def list_service_actions_paginated(
        self,
        request: ServiceCatalogListServiceActionsRequest | None = None,
    ) -> list[ServiceCatalogListServiceActionsResponse]:
        return await self._paginate('list_service_actions', request, ServiceCatalogListServiceActionsResponse)

    async def list_service_actions_for_provisioning_artifact(
        self,
        request: ServiceCatalogListServiceActionsForProvisioningArtifactRequest,
    ) -> ServiceCatalogListServiceActionsForProvisioningArtifactResponse:
        client = self._require_client()
        return await self._execute(client.list_service_actions_for_provisioning_artifact, request, ServiceCatalogListServiceActionsForProvisioningArtifactResponse)

    async def list_service_actions_for_provisioning_artifact_paginated(
        self,
        request: ServiceCatalogListServiceActionsForProvisioningArtifactRequest,
    ) -> list[ServiceCatalogListServiceActionsForProvisioningArtifactResponse]:
        return await self._paginate('list_service_actions_for_provisioning_artifact', request, ServiceCatalogListServiceActionsForProvisioningArtifactResponse)

    async def list_stack_instances_for_provisioned_product(
        self,
        request: ServiceCatalogListStackInstancesForProvisionedProductRequest,
    ) -> ServiceCatalogListStackInstancesForProvisionedProductResponse:
        client = self._require_client()
        return await self._execute(client.list_stack_instances_for_provisioned_product, request, ServiceCatalogListStackInstancesForProvisionedProductResponse)

    async def list_stack_instances_for_provisioned_product_paginated(
        self,
        request: ServiceCatalogListStackInstancesForProvisionedProductRequest,
    ) -> list[ServiceCatalogListStackInstancesForProvisionedProductResponse]:
        return await self._paginate('list_stack_instances_for_provisioned_product', request, ServiceCatalogListStackInstancesForProvisionedProductResponse)

    async def list_tag_options(
        self,
        request: ServiceCatalogListTagOptionsRequest | None = None,
    ) -> ServiceCatalogListTagOptionsResponse:
        client = self._require_client()
        return await self._execute(client.list_tag_options, request, ServiceCatalogListTagOptionsResponse)

    async def list_tag_options_paginated(
        self,
        request: ServiceCatalogListTagOptionsRequest | None = None,
    ) -> list[ServiceCatalogListTagOptionsResponse]:
        return await self._paginate('list_tag_options', request, ServiceCatalogListTagOptionsResponse)

    async def notify_provision_product_engine_workflow_result(
        self,
        request: ServiceCatalogNotifyProvisionProductEngineWorkflowResultRequest,
    ) -> ServiceCatalogNotifyProvisionProductEngineWorkflowResultResponse:
        client = self._require_client()
        return await self._execute(client.notify_provision_product_engine_workflow_result, request, ServiceCatalogNotifyProvisionProductEngineWorkflowResultResponse)

    async def notify_terminate_provisioned_product_engine_workflow_result(
        self,
        request: ServiceCatalogNotifyTerminateProvisionedProductEngineWorkflowResultRequest,
    ) -> ServiceCatalogNotifyTerminateProvisionedProductEngineWorkflowResultResponse:
        client = self._require_client()
        return await self._execute(client.notify_terminate_provisioned_product_engine_workflow_result, request, ServiceCatalogNotifyTerminateProvisionedProductEngineWorkflowResultResponse)

    async def notify_update_provisioned_product_engine_workflow_result(
        self,
        request: ServiceCatalogNotifyUpdateProvisionedProductEngineWorkflowResultRequest,
    ) -> ServiceCatalogNotifyUpdateProvisionedProductEngineWorkflowResultResponse:
        client = self._require_client()
        return await self._execute(client.notify_update_provisioned_product_engine_workflow_result, request, ServiceCatalogNotifyUpdateProvisionedProductEngineWorkflowResultResponse)

    async def provision_product(
        self,
        request: ServiceCatalogProvisionProductRequest,
    ) -> ServiceCatalogProvisionProductResponse:
        client = self._require_client()
        return await self._execute(client.provision_product, request, ServiceCatalogProvisionProductResponse)

    async def reject_portfolio_share(
        self,
        request: ServiceCatalogRejectPortfolioShareRequest,
    ) -> ServiceCatalogRejectPortfolioShareResponse:
        client = self._require_client()
        return await self._execute(client.reject_portfolio_share, request, ServiceCatalogRejectPortfolioShareResponse)

    async def scan_provisioned_products(
        self,
        request: ServiceCatalogScanProvisionedProductsRequest | None = None,
    ) -> ServiceCatalogScanProvisionedProductsResponse:
        client = self._require_client()
        return await self._execute(client.scan_provisioned_products, request, ServiceCatalogScanProvisionedProductsResponse)

    async def scan_provisioned_products_paginated(
        self,
        request: ServiceCatalogScanProvisionedProductsRequest | None = None,
    ) -> list[ServiceCatalogScanProvisionedProductsResponse]:
        return await self._paginate('scan_provisioned_products', request, ServiceCatalogScanProvisionedProductsResponse)

    async def search_products(
        self,
        request: ServiceCatalogSearchProductsRequest | None = None,
    ) -> ServiceCatalogSearchProductsResponse:
        client = self._require_client()
        return await self._execute(client.search_products, request, ServiceCatalogSearchProductsResponse)

    async def search_products_as_admin(
        self,
        request: ServiceCatalogSearchProductsAsAdminRequest | None = None,
    ) -> ServiceCatalogSearchProductsAsAdminResponse:
        client = self._require_client()
        return await self._execute(client.search_products_as_admin, request, ServiceCatalogSearchProductsAsAdminResponse)

    async def search_products_as_admin_paginated(
        self,
        request: ServiceCatalogSearchProductsAsAdminRequest | None = None,
    ) -> list[ServiceCatalogSearchProductsAsAdminResponse]:
        return await self._paginate('search_products_as_admin', request, ServiceCatalogSearchProductsAsAdminResponse)

    async def search_provisioned_products(
        self,
        request: ServiceCatalogSearchProvisionedProductsRequest | None = None,
    ) -> ServiceCatalogSearchProvisionedProductsResponse:
        client = self._require_client()
        return await self._execute(client.search_provisioned_products, request, ServiceCatalogSearchProvisionedProductsResponse)

    async def terminate_provisioned_product(
        self,
        request: ServiceCatalogTerminateProvisionedProductRequest,
    ) -> ServiceCatalogTerminateProvisionedProductResponse:
        client = self._require_client()
        return await self._execute(client.terminate_provisioned_product, request, ServiceCatalogTerminateProvisionedProductResponse)

    async def update_constraint(
        self,
        request: ServiceCatalogUpdateConstraintRequest,
    ) -> ServiceCatalogUpdateConstraintResponse:
        client = self._require_client()
        return await self._execute(client.update_constraint, request, ServiceCatalogUpdateConstraintResponse)

    async def update_portfolio(
        self,
        request: ServiceCatalogUpdatePortfolioRequest,
    ) -> ServiceCatalogUpdatePortfolioResponse:
        client = self._require_client()
        return await self._execute(client.update_portfolio, request, ServiceCatalogUpdatePortfolioResponse)

    async def update_portfolio_share(
        self,
        request: ServiceCatalogUpdatePortfolioShareRequest,
    ) -> ServiceCatalogUpdatePortfolioShareResponse:
        client = self._require_client()
        return await self._execute(client.update_portfolio_share, request, ServiceCatalogUpdatePortfolioShareResponse)

    async def update_product(
        self,
        request: ServiceCatalogUpdateProductRequest,
    ) -> ServiceCatalogUpdateProductResponse:
        client = self._require_client()
        return await self._execute(client.update_product, request, ServiceCatalogUpdateProductResponse)

    async def update_provisioned_product(
        self,
        request: ServiceCatalogUpdateProvisionedProductRequest,
    ) -> ServiceCatalogUpdateProvisionedProductResponse:
        client = self._require_client()
        return await self._execute(client.update_provisioned_product, request, ServiceCatalogUpdateProvisionedProductResponse)

    async def update_provisioned_product_properties(
        self,
        request: ServiceCatalogUpdateProvisionedProductPropertiesRequest,
    ) -> ServiceCatalogUpdateProvisionedProductPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.update_provisioned_product_properties, request, ServiceCatalogUpdateProvisionedProductPropertiesResponse)

    async def update_provisioning_artifact(
        self,
        request: ServiceCatalogUpdateProvisioningArtifactRequest,
    ) -> ServiceCatalogUpdateProvisioningArtifactResponse:
        client = self._require_client()
        return await self._execute(client.update_provisioning_artifact, request, ServiceCatalogUpdateProvisioningArtifactResponse)

    async def update_service_action(
        self,
        request: ServiceCatalogUpdateServiceActionRequest,
    ) -> ServiceCatalogUpdateServiceActionResponse:
        client = self._require_client()
        return await self._execute(client.update_service_action, request, ServiceCatalogUpdateServiceActionResponse)

    async def update_tag_option(
        self,
        request: ServiceCatalogUpdateTagOptionRequest,
    ) -> ServiceCatalogUpdateTagOptionResponse:
        client = self._require_client()
        return await self._execute(client.update_tag_option, request, ServiceCatalogUpdateTagOptionResponse)
