from werkflow_aws.models.app_runner import (
    AppRunnerAssociateCustomDomainRequest,
    AppRunnerAssociateCustomDomainResponse,
    AppRunnerCreateAutoScalingConfigurationRequest,
    AppRunnerCreateAutoScalingConfigurationResponse,
    AppRunnerCreateConnectionRequest,
    AppRunnerCreateConnectionResponse,
    AppRunnerCreateObservabilityConfigurationRequest,
    AppRunnerCreateObservabilityConfigurationResponse,
    AppRunnerCreateServiceRequest,
    AppRunnerCreateServiceResponse,
    AppRunnerCreateVpcConnectorRequest,
    AppRunnerCreateVpcConnectorResponse,
    AppRunnerCreateVpcIngressConnectionRequest,
    AppRunnerCreateVpcIngressConnectionResponse,
    AppRunnerDeleteAutoScalingConfigurationRequest,
    AppRunnerDeleteAutoScalingConfigurationResponse,
    AppRunnerDeleteConnectionRequest,
    AppRunnerDeleteConnectionResponse,
    AppRunnerDeleteObservabilityConfigurationRequest,
    AppRunnerDeleteObservabilityConfigurationResponse,
    AppRunnerDeleteServiceRequest,
    AppRunnerDeleteServiceResponse,
    AppRunnerDeleteVpcConnectorRequest,
    AppRunnerDeleteVpcConnectorResponse,
    AppRunnerDeleteVpcIngressConnectionRequest,
    AppRunnerDeleteVpcIngressConnectionResponse,
    AppRunnerDescribeAutoScalingConfigurationRequest,
    AppRunnerDescribeAutoScalingConfigurationResponse,
    AppRunnerDescribeCustomDomainsRequest,
    AppRunnerDescribeCustomDomainsResponse,
    AppRunnerDescribeObservabilityConfigurationRequest,
    AppRunnerDescribeObservabilityConfigurationResponse,
    AppRunnerDescribeServiceRequest,
    AppRunnerDescribeServiceResponse,
    AppRunnerDescribeVpcConnectorRequest,
    AppRunnerDescribeVpcConnectorResponse,
    AppRunnerDescribeVpcIngressConnectionRequest,
    AppRunnerDescribeVpcIngressConnectionResponse,
    AppRunnerDisassociateCustomDomainRequest,
    AppRunnerDisassociateCustomDomainResponse,
    AppRunnerListAutoScalingConfigurationsRequest,
    AppRunnerListAutoScalingConfigurationsResponse,
    AppRunnerListConnectionsRequest,
    AppRunnerListConnectionsResponse,
    AppRunnerListObservabilityConfigurationsRequest,
    AppRunnerListObservabilityConfigurationsResponse,
    AppRunnerListOperationsRequest,
    AppRunnerListOperationsResponse,
    AppRunnerListServicesForAutoScalingConfigurationRequest,
    AppRunnerListServicesForAutoScalingConfigurationResponse,
    AppRunnerListServicesRequest,
    AppRunnerListServicesResponse,
    AppRunnerListTagsForResourceRequest,
    AppRunnerListTagsForResourceResponse,
    AppRunnerListVpcConnectorsRequest,
    AppRunnerListVpcConnectorsResponse,
    AppRunnerListVpcIngressConnectionsRequest,
    AppRunnerListVpcIngressConnectionsResponse,
    AppRunnerPauseServiceRequest,
    AppRunnerPauseServiceResponse,
    AppRunnerResumeServiceRequest,
    AppRunnerResumeServiceResponse,
    AppRunnerStartDeploymentRequest,
    AppRunnerStartDeploymentResponse,
    AppRunnerTagResourceRequest,
    AppRunnerTagResourceResponse,
    AppRunnerUntagResourceRequest,
    AppRunnerUntagResourceResponse,
    AppRunnerUpdateDefaultAutoScalingConfigurationRequest,
    AppRunnerUpdateDefaultAutoScalingConfigurationResponse,
    AppRunnerUpdateServiceRequest,
    AppRunnerUpdateServiceResponse,
    AppRunnerUpdateVpcIngressConnectionRequest,
    AppRunnerUpdateVpcIngressConnectionResponse,
)
from werkflow_aws.types.app_runner_client import AppRunnerClient
from .base import AWSBaseService


class AWSAppRunner(AWSBaseService[AppRunnerClient]):
    service_name = 'app-runner'
    boto3_service_name = 'apprunner'

    def __init__(self) -> None:
        super().__init__(service_name='app-runner', boto3_service_name='apprunner')

    async def associate_custom_domain(
        self,
        request: AppRunnerAssociateCustomDomainRequest,
    ) -> AppRunnerAssociateCustomDomainResponse:
        client = self._require_client()
        return await self._execute(client.associate_custom_domain, request, AppRunnerAssociateCustomDomainResponse)

    async def create_auto_scaling_configuration(
        self,
        request: AppRunnerCreateAutoScalingConfigurationRequest,
    ) -> AppRunnerCreateAutoScalingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_auto_scaling_configuration, request, AppRunnerCreateAutoScalingConfigurationResponse)

    async def create_connection(
        self,
        request: AppRunnerCreateConnectionRequest,
    ) -> AppRunnerCreateConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_connection, request, AppRunnerCreateConnectionResponse)

    async def create_observability_configuration(
        self,
        request: AppRunnerCreateObservabilityConfigurationRequest,
    ) -> AppRunnerCreateObservabilityConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_observability_configuration, request, AppRunnerCreateObservabilityConfigurationResponse)

    async def create_service(
        self,
        request: AppRunnerCreateServiceRequest,
    ) -> AppRunnerCreateServiceResponse:
        client = self._require_client()
        return await self._execute(client.create_service, request, AppRunnerCreateServiceResponse)

    async def create_vpc_connector(
        self,
        request: AppRunnerCreateVpcConnectorRequest,
    ) -> AppRunnerCreateVpcConnectorResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_connector, request, AppRunnerCreateVpcConnectorResponse)

    async def create_vpc_ingress_connection(
        self,
        request: AppRunnerCreateVpcIngressConnectionRequest,
    ) -> AppRunnerCreateVpcIngressConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_ingress_connection, request, AppRunnerCreateVpcIngressConnectionResponse)

    async def delete_auto_scaling_configuration(
        self,
        request: AppRunnerDeleteAutoScalingConfigurationRequest,
    ) -> AppRunnerDeleteAutoScalingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_auto_scaling_configuration, request, AppRunnerDeleteAutoScalingConfigurationResponse)

    async def delete_connection(
        self,
        request: AppRunnerDeleteConnectionRequest,
    ) -> AppRunnerDeleteConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_connection, request, AppRunnerDeleteConnectionResponse)

    async def delete_observability_configuration(
        self,
        request: AppRunnerDeleteObservabilityConfigurationRequest,
    ) -> AppRunnerDeleteObservabilityConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_observability_configuration, request, AppRunnerDeleteObservabilityConfigurationResponse)

    async def delete_service(
        self,
        request: AppRunnerDeleteServiceRequest,
    ) -> AppRunnerDeleteServiceResponse:
        client = self._require_client()
        return await self._execute(client.delete_service, request, AppRunnerDeleteServiceResponse)

    async def delete_vpc_connector(
        self,
        request: AppRunnerDeleteVpcConnectorRequest,
    ) -> AppRunnerDeleteVpcConnectorResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_connector, request, AppRunnerDeleteVpcConnectorResponse)

    async def delete_vpc_ingress_connection(
        self,
        request: AppRunnerDeleteVpcIngressConnectionRequest,
    ) -> AppRunnerDeleteVpcIngressConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_ingress_connection, request, AppRunnerDeleteVpcIngressConnectionResponse)

    async def describe_auto_scaling_configuration(
        self,
        request: AppRunnerDescribeAutoScalingConfigurationRequest,
    ) -> AppRunnerDescribeAutoScalingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_auto_scaling_configuration, request, AppRunnerDescribeAutoScalingConfigurationResponse)

    async def describe_custom_domains(
        self,
        request: AppRunnerDescribeCustomDomainsRequest,
    ) -> AppRunnerDescribeCustomDomainsResponse:
        client = self._require_client()
        return await self._execute(client.describe_custom_domains, request, AppRunnerDescribeCustomDomainsResponse)

    async def describe_observability_configuration(
        self,
        request: AppRunnerDescribeObservabilityConfigurationRequest,
    ) -> AppRunnerDescribeObservabilityConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_observability_configuration, request, AppRunnerDescribeObservabilityConfigurationResponse)

    async def describe_service(
        self,
        request: AppRunnerDescribeServiceRequest,
    ) -> AppRunnerDescribeServiceResponse:
        client = self._require_client()
        return await self._execute(client.describe_service, request, AppRunnerDescribeServiceResponse)

    async def describe_vpc_connector(
        self,
        request: AppRunnerDescribeVpcConnectorRequest,
    ) -> AppRunnerDescribeVpcConnectorResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_connector, request, AppRunnerDescribeVpcConnectorResponse)

    async def describe_vpc_ingress_connection(
        self,
        request: AppRunnerDescribeVpcIngressConnectionRequest,
    ) -> AppRunnerDescribeVpcIngressConnectionResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_ingress_connection, request, AppRunnerDescribeVpcIngressConnectionResponse)

    async def disassociate_custom_domain(
        self,
        request: AppRunnerDisassociateCustomDomainRequest,
    ) -> AppRunnerDisassociateCustomDomainResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_custom_domain, request, AppRunnerDisassociateCustomDomainResponse)

    async def list_auto_scaling_configurations(
        self,
        request: AppRunnerListAutoScalingConfigurationsRequest | None = None,
    ) -> AppRunnerListAutoScalingConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_auto_scaling_configurations, request, AppRunnerListAutoScalingConfigurationsResponse)

    async def list_connections(
        self,
        request: AppRunnerListConnectionsRequest | None = None,
    ) -> AppRunnerListConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_connections, request, AppRunnerListConnectionsResponse)

    async def list_observability_configurations(
        self,
        request: AppRunnerListObservabilityConfigurationsRequest | None = None,
    ) -> AppRunnerListObservabilityConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_observability_configurations, request, AppRunnerListObservabilityConfigurationsResponse)

    async def list_operations(
        self,
        request: AppRunnerListOperationsRequest,
    ) -> AppRunnerListOperationsResponse:
        client = self._require_client()
        return await self._execute(client.list_operations, request, AppRunnerListOperationsResponse)

    async def list_services(
        self,
        request: AppRunnerListServicesRequest | None = None,
    ) -> AppRunnerListServicesResponse:
        client = self._require_client()
        return await self._execute(client.list_services, request, AppRunnerListServicesResponse)

    async def list_services_for_auto_scaling_configuration(
        self,
        request: AppRunnerListServicesForAutoScalingConfigurationRequest,
    ) -> AppRunnerListServicesForAutoScalingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.list_services_for_auto_scaling_configuration, request, AppRunnerListServicesForAutoScalingConfigurationResponse)

    async def list_tags_for_resource(
        self,
        request: AppRunnerListTagsForResourceRequest,
    ) -> AppRunnerListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, AppRunnerListTagsForResourceResponse)

    async def list_vpc_connectors(
        self,
        request: AppRunnerListVpcConnectorsRequest | None = None,
    ) -> AppRunnerListVpcConnectorsResponse:
        client = self._require_client()
        return await self._execute(client.list_vpc_connectors, request, AppRunnerListVpcConnectorsResponse)

    async def list_vpc_ingress_connections(
        self,
        request: AppRunnerListVpcIngressConnectionsRequest | None = None,
    ) -> AppRunnerListVpcIngressConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_vpc_ingress_connections, request, AppRunnerListVpcIngressConnectionsResponse)

    async def pause_service(
        self,
        request: AppRunnerPauseServiceRequest,
    ) -> AppRunnerPauseServiceResponse:
        client = self._require_client()
        return await self._execute(client.pause_service, request, AppRunnerPauseServiceResponse)

    async def resume_service(
        self,
        request: AppRunnerResumeServiceRequest,
    ) -> AppRunnerResumeServiceResponse:
        client = self._require_client()
        return await self._execute(client.resume_service, request, AppRunnerResumeServiceResponse)

    async def start_deployment(
        self,
        request: AppRunnerStartDeploymentRequest,
    ) -> AppRunnerStartDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.start_deployment, request, AppRunnerStartDeploymentResponse)

    async def tag_resource(
        self,
        request: AppRunnerTagResourceRequest,
    ) -> AppRunnerTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, AppRunnerTagResourceResponse)

    async def untag_resource(
        self,
        request: AppRunnerUntagResourceRequest,
    ) -> AppRunnerUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, AppRunnerUntagResourceResponse)

    async def update_default_auto_scaling_configuration(
        self,
        request: AppRunnerUpdateDefaultAutoScalingConfigurationRequest,
    ) -> AppRunnerUpdateDefaultAutoScalingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_default_auto_scaling_configuration, request, AppRunnerUpdateDefaultAutoScalingConfigurationResponse)

    async def update_service(
        self,
        request: AppRunnerUpdateServiceRequest,
    ) -> AppRunnerUpdateServiceResponse:
        client = self._require_client()
        return await self._execute(client.update_service, request, AppRunnerUpdateServiceResponse)

    async def update_vpc_ingress_connection(
        self,
        request: AppRunnerUpdateVpcIngressConnectionRequest,
    ) -> AppRunnerUpdateVpcIngressConnectionResponse:
        client = self._require_client()
        return await self._execute(client.update_vpc_ingress_connection, request, AppRunnerUpdateVpcIngressConnectionResponse)
