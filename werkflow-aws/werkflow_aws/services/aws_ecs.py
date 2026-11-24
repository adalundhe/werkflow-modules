from werkflow_aws.models.ecs import (
    ECSAssociateGatewayWithClusterRequest,
    ECSAssociateGatewayWithClusterResponse,
    ECSContinueServiceDeploymentRequest,
    ECSContinueServiceDeploymentResponse,
    ECSCreateCapacityProviderRequest,
    ECSCreateCapacityProviderResponse,
    ECSCreateClusterRequest,
    ECSCreateClusterResponse,
    ECSCreateDaemonRequest,
    ECSCreateDaemonResponse,
    ECSCreateExpressGatewayServiceRequest,
    ECSCreateExpressGatewayServiceResponse,
    ECSCreateGatewayRequest,
    ECSCreateGatewayResponse,
    ECSCreateServiceRequest,
    ECSCreateServiceResponse,
    ECSCreateTaskSetRequest,
    ECSCreateTaskSetResponse,
    ECSDeleteAccountSettingRequest,
    ECSDeleteAccountSettingResponse,
    ECSDeleteAttributesRequest,
    ECSDeleteAttributesResponse,
    ECSDeleteCapacityProviderRequest,
    ECSDeleteCapacityProviderResponse,
    ECSDeleteClusterRequest,
    ECSDeleteClusterResponse,
    ECSDeleteDaemonRequest,
    ECSDeleteDaemonResponse,
    ECSDeleteDaemonTaskDefinitionRequest,
    ECSDeleteDaemonTaskDefinitionResponse,
    ECSDeleteExpressGatewayServiceRequest,
    ECSDeleteExpressGatewayServiceResponse,
    ECSDeleteGatewayRequest,
    ECSDeleteGatewayResponse,
    ECSDeleteServiceRequest,
    ECSDeleteServiceResponse,
    ECSDeleteTaskDefinitionsRequest,
    ECSDeleteTaskDefinitionsResponse,
    ECSDeleteTaskSetRequest,
    ECSDeleteTaskSetResponse,
    ECSDeregisterContainerInstanceRequest,
    ECSDeregisterContainerInstanceResponse,
    ECSDeregisterTaskDefinitionRequest,
    ECSDeregisterTaskDefinitionResponse,
    ECSDescribeCapacityProvidersRequest,
    ECSDescribeCapacityProvidersResponse,
    ECSDescribeClustersRequest,
    ECSDescribeClustersResponse,
    ECSDescribeContainerInstancesRequest,
    ECSDescribeContainerInstancesResponse,
    ECSDescribeDaemonDeploymentsRequest,
    ECSDescribeDaemonDeploymentsResponse,
    ECSDescribeDaemonRequest,
    ECSDescribeDaemonResponse,
    ECSDescribeDaemonRevisionsRequest,
    ECSDescribeDaemonRevisionsResponse,
    ECSDescribeDaemonTaskDefinitionRequest,
    ECSDescribeDaemonTaskDefinitionResponse,
    ECSDescribeExpressGatewayServiceRequest,
    ECSDescribeExpressGatewayServiceResponse,
    ECSDescribeGatewayRequest,
    ECSDescribeGatewayResourcesRequest,
    ECSDescribeGatewayResourcesResponse,
    ECSDescribeGatewayResponse,
    ECSDescribeGatewayRouteRequest,
    ECSDescribeGatewayRouteResponse,
    ECSDescribeServiceDeploymentsRequest,
    ECSDescribeServiceDeploymentsResponse,
    ECSDescribeServiceRevisionsRequest,
    ECSDescribeServiceRevisionsResponse,
    ECSDescribeServicesRequest,
    ECSDescribeServicesResponse,
    ECSDescribeTaskDefinitionRequest,
    ECSDescribeTaskDefinitionResponse,
    ECSDescribeTaskSetsRequest,
    ECSDescribeTaskSetsResponse,
    ECSDescribeTasksRequest,
    ECSDescribeTasksResponse,
    ECSDisassociateGatewayFromClusterRequest,
    ECSDisassociateGatewayFromClusterResponse,
    ECSDiscoverPollEndpointRequest,
    ECSDiscoverPollEndpointResponse,
    ECSExecuteCommandRequest,
    ECSExecuteCommandResponse,
    ECSGetTaskProtectionRequest,
    ECSGetTaskProtectionResponse,
    ECSListAccountSettingsRequest,
    ECSListAccountSettingsResponse,
    ECSListAttributesRequest,
    ECSListAttributesResponse,
    ECSListClustersRequest,
    ECSListClustersResponse,
    ECSListContainerInstancesRequest,
    ECSListContainerInstancesResponse,
    ECSListDaemonDeploymentsRequest,
    ECSListDaemonDeploymentsResponse,
    ECSListDaemonTaskDefinitionsRequest,
    ECSListDaemonTaskDefinitionsResponse,
    ECSListDaemonsRequest,
    ECSListDaemonsResponse,
    ECSListGatewayClusterAssociationsRequest,
    ECSListGatewayClusterAssociationsResponse,
    ECSListGatewayRoutesRequest,
    ECSListGatewayRoutesResponse,
    ECSListGatewaysRequest,
    ECSListGatewaysResponse,
    ECSListServiceDeploymentsRequest,
    ECSListServiceDeploymentsResponse,
    ECSListServicesByNamespaceRequest,
    ECSListServicesByNamespaceResponse,
    ECSListServicesRequest,
    ECSListServicesResponse,
    ECSListTagsForResourceRequest,
    ECSListTagsForResourceResponse,
    ECSListTaskDefinitionFamiliesRequest,
    ECSListTaskDefinitionFamiliesResponse,
    ECSListTaskDefinitionsRequest,
    ECSListTaskDefinitionsResponse,
    ECSListTasksRequest,
    ECSListTasksResponse,
    ECSPutAccountSettingDefaultRequest,
    ECSPutAccountSettingDefaultResponse,
    ECSPutAccountSettingRequest,
    ECSPutAccountSettingResponse,
    ECSPutAttributesRequest,
    ECSPutAttributesResponse,
    ECSPutClusterCapacityProvidersRequest,
    ECSPutClusterCapacityProvidersResponse,
    ECSRegisterContainerInstanceRequest,
    ECSRegisterContainerInstanceResponse,
    ECSRegisterDaemonTaskDefinitionRequest,
    ECSRegisterDaemonTaskDefinitionResponse,
    ECSRegisterTaskDefinitionRequest,
    ECSRegisterTaskDefinitionResponse,
    ECSRunTaskRequest,
    ECSRunTaskResponse,
    ECSStartTaskRequest,
    ECSStartTaskResponse,
    ECSStopServiceDeploymentRequest,
    ECSStopServiceDeploymentResponse,
    ECSStopTaskRequest,
    ECSStopTaskResponse,
    ECSSubmitAttachmentStateChangesRequest,
    ECSSubmitAttachmentStateChangesResponse,
    ECSSubmitContainerStateChangeRequest,
    ECSSubmitContainerStateChangeResponse,
    ECSSubmitTaskStateChangeRequest,
    ECSSubmitTaskStateChangeResponse,
    ECSTagResourceRequest,
    ECSTagResourceResponse,
    ECSUntagResourceRequest,
    ECSUntagResourceResponse,
    ECSUpdateCapacityProviderRequest,
    ECSUpdateCapacityProviderResponse,
    ECSUpdateClusterRequest,
    ECSUpdateClusterResponse,
    ECSUpdateClusterSettingsRequest,
    ECSUpdateClusterSettingsResponse,
    ECSUpdateContainerAgentRequest,
    ECSUpdateContainerAgentResponse,
    ECSUpdateContainerInstancesStateRequest,
    ECSUpdateContainerInstancesStateResponse,
    ECSUpdateDaemonRequest,
    ECSUpdateDaemonResponse,
    ECSUpdateExpressGatewayServiceRequest,
    ECSUpdateExpressGatewayServiceResponse,
    ECSUpdateGatewayRequest,
    ECSUpdateGatewayResponse,
    ECSUpdateServicePrimaryTaskSetRequest,
    ECSUpdateServicePrimaryTaskSetResponse,
    ECSUpdateServiceRequest,
    ECSUpdateServiceResponse,
    ECSUpdateTaskProtectionRequest,
    ECSUpdateTaskProtectionResponse,
    ECSUpdateTaskSetRequest,
    ECSUpdateTaskSetResponse,
)
from werkflow_aws.types.ecs_client import ECSClient
from .base import AWSBaseService


class AWSECS(AWSBaseService[ECSClient]):
    service_name = 'ecs'
    boto3_service_name = 'ecs'

    def __init__(self) -> None:
        super().__init__(service_name='ecs', boto3_service_name='ecs')

    async def associate_gateway_with_cluster(
        self,
        request: ECSAssociateGatewayWithClusterRequest,
    ) -> ECSAssociateGatewayWithClusterResponse:
        client = self._require_client()
        return await self._execute(client.associate_gateway_with_cluster, request, ECSAssociateGatewayWithClusterResponse)

    async def continue_service_deployment(
        self,
        request: ECSContinueServiceDeploymentRequest,
    ) -> ECSContinueServiceDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.continue_service_deployment, request, ECSContinueServiceDeploymentResponse)

    async def create_capacity_provider(
        self,
        request: ECSCreateCapacityProviderRequest,
    ) -> ECSCreateCapacityProviderResponse:
        client = self._require_client()
        return await self._execute(client.create_capacity_provider, request, ECSCreateCapacityProviderResponse)

    async def create_cluster(
        self,
        request: ECSCreateClusterRequest | None = None,
    ) -> ECSCreateClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster, request, ECSCreateClusterResponse)

    async def create_daemon(
        self,
        request: ECSCreateDaemonRequest,
    ) -> ECSCreateDaemonResponse:
        client = self._require_client()
        return await self._execute(client.create_daemon, request, ECSCreateDaemonResponse)

    async def create_express_gateway_service(
        self,
        request: ECSCreateExpressGatewayServiceRequest,
    ) -> ECSCreateExpressGatewayServiceResponse:
        client = self._require_client()
        return await self._execute(client.create_express_gateway_service, request, ECSCreateExpressGatewayServiceResponse)

    async def create_gateway(
        self,
        request: ECSCreateGatewayRequest,
    ) -> ECSCreateGatewayResponse:
        client = self._require_client()
        return await self._execute(client.create_gateway, request, ECSCreateGatewayResponse)

    async def create_service(
        self,
        request: ECSCreateServiceRequest,
    ) -> ECSCreateServiceResponse:
        client = self._require_client()
        return await self._execute(client.create_service, request, ECSCreateServiceResponse)

    async def create_task_set(
        self,
        request: ECSCreateTaskSetRequest,
    ) -> ECSCreateTaskSetResponse:
        client = self._require_client()
        return await self._execute(client.create_task_set, request, ECSCreateTaskSetResponse)

    async def delete_account_setting(
        self,
        request: ECSDeleteAccountSettingRequest,
    ) -> ECSDeleteAccountSettingResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_setting, request, ECSDeleteAccountSettingResponse)

    async def delete_attributes(
        self,
        request: ECSDeleteAttributesRequest,
    ) -> ECSDeleteAttributesResponse:
        client = self._require_client()
        return await self._execute(client.delete_attributes, request, ECSDeleteAttributesResponse)

    async def delete_capacity_provider(
        self,
        request: ECSDeleteCapacityProviderRequest,
    ) -> ECSDeleteCapacityProviderResponse:
        client = self._require_client()
        return await self._execute(client.delete_capacity_provider, request, ECSDeleteCapacityProviderResponse)

    async def delete_cluster(
        self,
        request: ECSDeleteClusterRequest,
    ) -> ECSDeleteClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster, request, ECSDeleteClusterResponse)

    async def delete_daemon(
        self,
        request: ECSDeleteDaemonRequest,
    ) -> ECSDeleteDaemonResponse:
        client = self._require_client()
        return await self._execute(client.delete_daemon, request, ECSDeleteDaemonResponse)

    async def delete_daemon_task_definition(
        self,
        request: ECSDeleteDaemonTaskDefinitionRequest,
    ) -> ECSDeleteDaemonTaskDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_daemon_task_definition, request, ECSDeleteDaemonTaskDefinitionResponse)

    async def delete_express_gateway_service(
        self,
        request: ECSDeleteExpressGatewayServiceRequest,
    ) -> ECSDeleteExpressGatewayServiceResponse:
        client = self._require_client()
        return await self._execute(client.delete_express_gateway_service, request, ECSDeleteExpressGatewayServiceResponse)

    async def delete_gateway(
        self,
        request: ECSDeleteGatewayRequest,
    ) -> ECSDeleteGatewayResponse:
        client = self._require_client()
        return await self._execute(client.delete_gateway, request, ECSDeleteGatewayResponse)

    async def delete_service(
        self,
        request: ECSDeleteServiceRequest,
    ) -> ECSDeleteServiceResponse:
        client = self._require_client()
        return await self._execute(client.delete_service, request, ECSDeleteServiceResponse)

    async def delete_task_definitions(
        self,
        request: ECSDeleteTaskDefinitionsRequest,
    ) -> ECSDeleteTaskDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.delete_task_definitions, request, ECSDeleteTaskDefinitionsResponse)

    async def delete_task_set(
        self,
        request: ECSDeleteTaskSetRequest,
    ) -> ECSDeleteTaskSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_task_set, request, ECSDeleteTaskSetResponse)

    async def deregister_container_instance(
        self,
        request: ECSDeregisterContainerInstanceRequest,
    ) -> ECSDeregisterContainerInstanceResponse:
        client = self._require_client()
        return await self._execute(client.deregister_container_instance, request, ECSDeregisterContainerInstanceResponse)

    async def deregister_task_definition(
        self,
        request: ECSDeregisterTaskDefinitionRequest,
    ) -> ECSDeregisterTaskDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.deregister_task_definition, request, ECSDeregisterTaskDefinitionResponse)

    async def describe_capacity_providers(
        self,
        request: ECSDescribeCapacityProvidersRequest | None = None,
    ) -> ECSDescribeCapacityProvidersResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_providers, request, ECSDescribeCapacityProvidersResponse)

    async def describe_clusters(
        self,
        request: ECSDescribeClustersRequest | None = None,
    ) -> ECSDescribeClustersResponse:
        client = self._require_client()
        return await self._execute(client.describe_clusters, request, ECSDescribeClustersResponse)

    async def describe_container_instances(
        self,
        request: ECSDescribeContainerInstancesRequest,
    ) -> ECSDescribeContainerInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_container_instances, request, ECSDescribeContainerInstancesResponse)

    async def describe_daemon(
        self,
        request: ECSDescribeDaemonRequest,
    ) -> ECSDescribeDaemonResponse:
        client = self._require_client()
        return await self._execute(client.describe_daemon, request, ECSDescribeDaemonResponse)

    async def describe_daemon_deployments(
        self,
        request: ECSDescribeDaemonDeploymentsRequest,
    ) -> ECSDescribeDaemonDeploymentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_daemon_deployments, request, ECSDescribeDaemonDeploymentsResponse)

    async def describe_daemon_revisions(
        self,
        request: ECSDescribeDaemonRevisionsRequest,
    ) -> ECSDescribeDaemonRevisionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_daemon_revisions, request, ECSDescribeDaemonRevisionsResponse)

    async def describe_daemon_task_definition(
        self,
        request: ECSDescribeDaemonTaskDefinitionRequest,
    ) -> ECSDescribeDaemonTaskDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_daemon_task_definition, request, ECSDescribeDaemonTaskDefinitionResponse)

    async def describe_express_gateway_service(
        self,
        request: ECSDescribeExpressGatewayServiceRequest,
    ) -> ECSDescribeExpressGatewayServiceResponse:
        client = self._require_client()
        return await self._execute(client.describe_express_gateway_service, request, ECSDescribeExpressGatewayServiceResponse)

    async def describe_gateway(
        self,
        request: ECSDescribeGatewayRequest,
    ) -> ECSDescribeGatewayResponse:
        client = self._require_client()
        return await self._execute(client.describe_gateway, request, ECSDescribeGatewayResponse)

    async def describe_gateway_resources(
        self,
        request: ECSDescribeGatewayResourcesRequest,
    ) -> ECSDescribeGatewayResourcesResponse:
        client = self._require_client()
        return await self._execute(client.describe_gateway_resources, request, ECSDescribeGatewayResourcesResponse)

    async def describe_gateway_route(
        self,
        request: ECSDescribeGatewayRouteRequest,
    ) -> ECSDescribeGatewayRouteResponse:
        client = self._require_client()
        return await self._execute(client.describe_gateway_route, request, ECSDescribeGatewayRouteResponse)

    async def describe_service_deployments(
        self,
        request: ECSDescribeServiceDeploymentsRequest,
    ) -> ECSDescribeServiceDeploymentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_service_deployments, request, ECSDescribeServiceDeploymentsResponse)

    async def describe_service_revisions(
        self,
        request: ECSDescribeServiceRevisionsRequest,
    ) -> ECSDescribeServiceRevisionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_service_revisions, request, ECSDescribeServiceRevisionsResponse)

    async def describe_services(
        self,
        request: ECSDescribeServicesRequest,
    ) -> ECSDescribeServicesResponse:
        client = self._require_client()
        return await self._execute(client.describe_services, request, ECSDescribeServicesResponse)

    async def describe_task_definition(
        self,
        request: ECSDescribeTaskDefinitionRequest,
    ) -> ECSDescribeTaskDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_task_definition, request, ECSDescribeTaskDefinitionResponse)

    async def describe_task_sets(
        self,
        request: ECSDescribeTaskSetsRequest,
    ) -> ECSDescribeTaskSetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_task_sets, request, ECSDescribeTaskSetsResponse)

    async def describe_tasks(
        self,
        request: ECSDescribeTasksRequest,
    ) -> ECSDescribeTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_tasks, request, ECSDescribeTasksResponse)

    async def disassociate_gateway_from_cluster(
        self,
        request: ECSDisassociateGatewayFromClusterRequest,
    ) -> ECSDisassociateGatewayFromClusterResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_gateway_from_cluster, request, ECSDisassociateGatewayFromClusterResponse)

    async def discover_poll_endpoint(
        self,
        request: ECSDiscoverPollEndpointRequest | None = None,
    ) -> ECSDiscoverPollEndpointResponse:
        client = self._require_client()
        return await self._execute(client.discover_poll_endpoint, request, ECSDiscoverPollEndpointResponse)

    async def execute_command(
        self,
        request: ECSExecuteCommandRequest,
    ) -> ECSExecuteCommandResponse:
        client = self._require_client()
        return await self._execute(client.execute_command, request, ECSExecuteCommandResponse)

    async def get_task_protection(
        self,
        request: ECSGetTaskProtectionRequest,
    ) -> ECSGetTaskProtectionResponse:
        client = self._require_client()
        return await self._execute(client.get_task_protection, request, ECSGetTaskProtectionResponse)

    async def list_account_settings(
        self,
        request: ECSListAccountSettingsRequest | None = None,
    ) -> ECSListAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.list_account_settings, request, ECSListAccountSettingsResponse)

    async def list_account_settings_paginated(
        self,
        request: ECSListAccountSettingsRequest | None = None,
    ) -> list[ECSListAccountSettingsResponse]:
        return await self._paginate('list_account_settings', request, ECSListAccountSettingsResponse)

    async def list_attributes(
        self,
        request: ECSListAttributesRequest,
    ) -> ECSListAttributesResponse:
        client = self._require_client()
        return await self._execute(client.list_attributes, request, ECSListAttributesResponse)

    async def list_attributes_paginated(
        self,
        request: ECSListAttributesRequest,
    ) -> list[ECSListAttributesResponse]:
        return await self._paginate('list_attributes', request, ECSListAttributesResponse)

    async def list_clusters(
        self,
        request: ECSListClustersRequest | None = None,
    ) -> ECSListClustersResponse:
        client = self._require_client()
        return await self._execute(client.list_clusters, request, ECSListClustersResponse)

    async def list_clusters_paginated(
        self,
        request: ECSListClustersRequest | None = None,
    ) -> list[ECSListClustersResponse]:
        return await self._paginate('list_clusters', request, ECSListClustersResponse)

    async def list_container_instances(
        self,
        request: ECSListContainerInstancesRequest | None = None,
    ) -> ECSListContainerInstancesResponse:
        client = self._require_client()
        return await self._execute(client.list_container_instances, request, ECSListContainerInstancesResponse)

    async def list_container_instances_paginated(
        self,
        request: ECSListContainerInstancesRequest | None = None,
    ) -> list[ECSListContainerInstancesResponse]:
        return await self._paginate('list_container_instances', request, ECSListContainerInstancesResponse)

    async def list_daemon_deployments(
        self,
        request: ECSListDaemonDeploymentsRequest,
    ) -> ECSListDaemonDeploymentsResponse:
        client = self._require_client()
        return await self._execute(client.list_daemon_deployments, request, ECSListDaemonDeploymentsResponse)

    async def list_daemon_task_definitions(
        self,
        request: ECSListDaemonTaskDefinitionsRequest | None = None,
    ) -> ECSListDaemonTaskDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.list_daemon_task_definitions, request, ECSListDaemonTaskDefinitionsResponse)

    async def list_daemons(
        self,
        request: ECSListDaemonsRequest | None = None,
    ) -> ECSListDaemonsResponse:
        client = self._require_client()
        return await self._execute(client.list_daemons, request, ECSListDaemonsResponse)

    async def list_gateway_cluster_associations(
        self,
        request: ECSListGatewayClusterAssociationsRequest | None = None,
    ) -> ECSListGatewayClusterAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_gateway_cluster_associations, request, ECSListGatewayClusterAssociationsResponse)

    async def list_gateway_cluster_associations_paginated(
        self,
        request: ECSListGatewayClusterAssociationsRequest | None = None,
    ) -> list[ECSListGatewayClusterAssociationsResponse]:
        return await self._paginate('list_gateway_cluster_associations', request, ECSListGatewayClusterAssociationsResponse)

    async def list_gateway_routes(
        self,
        request: ECSListGatewayRoutesRequest | None = None,
    ) -> ECSListGatewayRoutesResponse:
        client = self._require_client()
        return await self._execute(client.list_gateway_routes, request, ECSListGatewayRoutesResponse)

    async def list_gateway_routes_paginated(
        self,
        request: ECSListGatewayRoutesRequest | None = None,
    ) -> list[ECSListGatewayRoutesResponse]:
        return await self._paginate('list_gateway_routes', request, ECSListGatewayRoutesResponse)

    async def list_gateways(
        self,
        request: ECSListGatewaysRequest | None = None,
    ) -> ECSListGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.list_gateways, request, ECSListGatewaysResponse)

    async def list_gateways_paginated(
        self,
        request: ECSListGatewaysRequest | None = None,
    ) -> list[ECSListGatewaysResponse]:
        return await self._paginate('list_gateways', request, ECSListGatewaysResponse)

    async def list_service_deployments(
        self,
        request: ECSListServiceDeploymentsRequest,
    ) -> ECSListServiceDeploymentsResponse:
        client = self._require_client()
        return await self._execute(client.list_service_deployments, request, ECSListServiceDeploymentsResponse)

    async def list_services(
        self,
        request: ECSListServicesRequest | None = None,
    ) -> ECSListServicesResponse:
        client = self._require_client()
        return await self._execute(client.list_services, request, ECSListServicesResponse)

    async def list_services_paginated(
        self,
        request: ECSListServicesRequest | None = None,
    ) -> list[ECSListServicesResponse]:
        return await self._paginate('list_services', request, ECSListServicesResponse)

    async def list_services_by_namespace(
        self,
        request: ECSListServicesByNamespaceRequest,
    ) -> ECSListServicesByNamespaceResponse:
        client = self._require_client()
        return await self._execute(client.list_services_by_namespace, request, ECSListServicesByNamespaceResponse)

    async def list_services_by_namespace_paginated(
        self,
        request: ECSListServicesByNamespaceRequest,
    ) -> list[ECSListServicesByNamespaceResponse]:
        return await self._paginate('list_services_by_namespace', request, ECSListServicesByNamespaceResponse)

    async def list_tags_for_resource(
        self,
        request: ECSListTagsForResourceRequest,
    ) -> ECSListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, ECSListTagsForResourceResponse)

    async def list_task_definition_families(
        self,
        request: ECSListTaskDefinitionFamiliesRequest | None = None,
    ) -> ECSListTaskDefinitionFamiliesResponse:
        client = self._require_client()
        return await self._execute(client.list_task_definition_families, request, ECSListTaskDefinitionFamiliesResponse)

    async def list_task_definition_families_paginated(
        self,
        request: ECSListTaskDefinitionFamiliesRequest | None = None,
    ) -> list[ECSListTaskDefinitionFamiliesResponse]:
        return await self._paginate('list_task_definition_families', request, ECSListTaskDefinitionFamiliesResponse)

    async def list_task_definitions(
        self,
        request: ECSListTaskDefinitionsRequest | None = None,
    ) -> ECSListTaskDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.list_task_definitions, request, ECSListTaskDefinitionsResponse)

    async def list_task_definitions_paginated(
        self,
        request: ECSListTaskDefinitionsRequest | None = None,
    ) -> list[ECSListTaskDefinitionsResponse]:
        return await self._paginate('list_task_definitions', request, ECSListTaskDefinitionsResponse)

    async def list_tasks(
        self,
        request: ECSListTasksRequest | None = None,
    ) -> ECSListTasksResponse:
        client = self._require_client()
        return await self._execute(client.list_tasks, request, ECSListTasksResponse)

    async def list_tasks_paginated(
        self,
        request: ECSListTasksRequest | None = None,
    ) -> list[ECSListTasksResponse]:
        return await self._paginate('list_tasks', request, ECSListTasksResponse)

    async def put_account_setting(
        self,
        request: ECSPutAccountSettingRequest,
    ) -> ECSPutAccountSettingResponse:
        client = self._require_client()
        return await self._execute(client.put_account_setting, request, ECSPutAccountSettingResponse)

    async def put_account_setting_default(
        self,
        request: ECSPutAccountSettingDefaultRequest,
    ) -> ECSPutAccountSettingDefaultResponse:
        client = self._require_client()
        return await self._execute(client.put_account_setting_default, request, ECSPutAccountSettingDefaultResponse)

    async def put_attributes(
        self,
        request: ECSPutAttributesRequest,
    ) -> ECSPutAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_attributes, request, ECSPutAttributesResponse)

    async def put_cluster_capacity_providers(
        self,
        request: ECSPutClusterCapacityProvidersRequest,
    ) -> ECSPutClusterCapacityProvidersResponse:
        client = self._require_client()
        return await self._execute(client.put_cluster_capacity_providers, request, ECSPutClusterCapacityProvidersResponse)

    async def register_container_instance(
        self,
        request: ECSRegisterContainerInstanceRequest | None = None,
    ) -> ECSRegisterContainerInstanceResponse:
        client = self._require_client()
        return await self._execute(client.register_container_instance, request, ECSRegisterContainerInstanceResponse)

    async def register_daemon_task_definition(
        self,
        request: ECSRegisterDaemonTaskDefinitionRequest,
    ) -> ECSRegisterDaemonTaskDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.register_daemon_task_definition, request, ECSRegisterDaemonTaskDefinitionResponse)

    async def register_task_definition(
        self,
        request: ECSRegisterTaskDefinitionRequest,
    ) -> ECSRegisterTaskDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.register_task_definition, request, ECSRegisterTaskDefinitionResponse)

    async def run_task(
        self,
        request: ECSRunTaskRequest,
    ) -> ECSRunTaskResponse:
        client = self._require_client()
        return await self._execute(client.run_task, request, ECSRunTaskResponse)

    async def start_task(
        self,
        request: ECSStartTaskRequest,
    ) -> ECSStartTaskResponse:
        client = self._require_client()
        return await self._execute(client.start_task, request, ECSStartTaskResponse)

    async def stop_service_deployment(
        self,
        request: ECSStopServiceDeploymentRequest,
    ) -> ECSStopServiceDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.stop_service_deployment, request, ECSStopServiceDeploymentResponse)

    async def stop_task(
        self,
        request: ECSStopTaskRequest,
    ) -> ECSStopTaskResponse:
        client = self._require_client()
        return await self._execute(client.stop_task, request, ECSStopTaskResponse)

    async def submit_attachment_state_changes(
        self,
        request: ECSSubmitAttachmentStateChangesRequest,
    ) -> ECSSubmitAttachmentStateChangesResponse:
        client = self._require_client()
        return await self._execute(client.submit_attachment_state_changes, request, ECSSubmitAttachmentStateChangesResponse)

    async def submit_container_state_change(
        self,
        request: ECSSubmitContainerStateChangeRequest | None = None,
    ) -> ECSSubmitContainerStateChangeResponse:
        client = self._require_client()
        return await self._execute(client.submit_container_state_change, request, ECSSubmitContainerStateChangeResponse)

    async def submit_task_state_change(
        self,
        request: ECSSubmitTaskStateChangeRequest | None = None,
    ) -> ECSSubmitTaskStateChangeResponse:
        client = self._require_client()
        return await self._execute(client.submit_task_state_change, request, ECSSubmitTaskStateChangeResponse)

    async def tag_resource(
        self,
        request: ECSTagResourceRequest,
    ) -> ECSTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, ECSTagResourceResponse)

    async def untag_resource(
        self,
        request: ECSUntagResourceRequest,
    ) -> ECSUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, ECSUntagResourceResponse)

    async def update_capacity_provider(
        self,
        request: ECSUpdateCapacityProviderRequest,
    ) -> ECSUpdateCapacityProviderResponse:
        client = self._require_client()
        return await self._execute(client.update_capacity_provider, request, ECSUpdateCapacityProviderResponse)

    async def update_cluster(
        self,
        request: ECSUpdateClusterRequest,
    ) -> ECSUpdateClusterResponse:
        client = self._require_client()
        return await self._execute(client.update_cluster, request, ECSUpdateClusterResponse)

    async def update_cluster_settings(
        self,
        request: ECSUpdateClusterSettingsRequest,
    ) -> ECSUpdateClusterSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_cluster_settings, request, ECSUpdateClusterSettingsResponse)

    async def update_container_agent(
        self,
        request: ECSUpdateContainerAgentRequest,
    ) -> ECSUpdateContainerAgentResponse:
        client = self._require_client()
        return await self._execute(client.update_container_agent, request, ECSUpdateContainerAgentResponse)

    async def update_container_instances_state(
        self,
        request: ECSUpdateContainerInstancesStateRequest,
    ) -> ECSUpdateContainerInstancesStateResponse:
        client = self._require_client()
        return await self._execute(client.update_container_instances_state, request, ECSUpdateContainerInstancesStateResponse)

    async def update_daemon(
        self,
        request: ECSUpdateDaemonRequest,
    ) -> ECSUpdateDaemonResponse:
        client = self._require_client()
        return await self._execute(client.update_daemon, request, ECSUpdateDaemonResponse)

    async def update_express_gateway_service(
        self,
        request: ECSUpdateExpressGatewayServiceRequest,
    ) -> ECSUpdateExpressGatewayServiceResponse:
        client = self._require_client()
        return await self._execute(client.update_express_gateway_service, request, ECSUpdateExpressGatewayServiceResponse)

    async def update_gateway(
        self,
        request: ECSUpdateGatewayRequest,
    ) -> ECSUpdateGatewayResponse:
        client = self._require_client()
        return await self._execute(client.update_gateway, request, ECSUpdateGatewayResponse)

    async def update_service(
        self,
        request: ECSUpdateServiceRequest,
    ) -> ECSUpdateServiceResponse:
        client = self._require_client()
        return await self._execute(client.update_service, request, ECSUpdateServiceResponse)

    async def update_service_primary_task_set(
        self,
        request: ECSUpdateServicePrimaryTaskSetRequest,
    ) -> ECSUpdateServicePrimaryTaskSetResponse:
        client = self._require_client()
        return await self._execute(client.update_service_primary_task_set, request, ECSUpdateServicePrimaryTaskSetResponse)

    async def update_task_protection(
        self,
        request: ECSUpdateTaskProtectionRequest,
    ) -> ECSUpdateTaskProtectionResponse:
        client = self._require_client()
        return await self._execute(client.update_task_protection, request, ECSUpdateTaskProtectionResponse)

    async def update_task_set(
        self,
        request: ECSUpdateTaskSetRequest,
    ) -> ECSUpdateTaskSetResponse:
        client = self._require_client()
        return await self._execute(client.update_task_set, request, ECSUpdateTaskSetResponse)
