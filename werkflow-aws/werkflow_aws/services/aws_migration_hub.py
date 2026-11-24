from werkflow_aws.models.migration_hub import (
    MigrationHubCreateApplicationRequest,
    MigrationHubCreateApplicationResponse,
    MigrationHubCreateEnvironmentRequest,
    MigrationHubCreateEnvironmentResponse,
    MigrationHubCreateRouteRequest,
    MigrationHubCreateRouteResponse,
    MigrationHubCreateServiceRequest,
    MigrationHubCreateServiceResponse,
    MigrationHubDeleteApplicationRequest,
    MigrationHubDeleteApplicationResponse,
    MigrationHubDeleteEnvironmentRequest,
    MigrationHubDeleteEnvironmentResponse,
    MigrationHubDeleteResourcePolicyRequest,
    MigrationHubDeleteResourcePolicyResponse,
    MigrationHubDeleteRouteRequest,
    MigrationHubDeleteRouteResponse,
    MigrationHubDeleteServiceRequest,
    MigrationHubDeleteServiceResponse,
    MigrationHubGetApplicationRequest,
    MigrationHubGetApplicationResponse,
    MigrationHubGetEnvironmentRequest,
    MigrationHubGetEnvironmentResponse,
    MigrationHubGetResourcePolicyRequest,
    MigrationHubGetResourcePolicyResponse,
    MigrationHubGetRouteRequest,
    MigrationHubGetRouteResponse,
    MigrationHubGetServiceRequest,
    MigrationHubGetServiceResponse,
    MigrationHubListApplicationsRequest,
    MigrationHubListApplicationsResponse,
    MigrationHubListEnvironmentVpcsRequest,
    MigrationHubListEnvironmentVpcsResponse,
    MigrationHubListEnvironmentsRequest,
    MigrationHubListEnvironmentsResponse,
    MigrationHubListRoutesRequest,
    MigrationHubListRoutesResponse,
    MigrationHubListServicesRequest,
    MigrationHubListServicesResponse,
    MigrationHubListTagsForResourceRequest,
    MigrationHubListTagsForResourceResponse,
    MigrationHubPutResourcePolicyRequest,
    MigrationHubPutResourcePolicyResponse,
    MigrationHubTagResourceRequest,
    MigrationHubTagResourceResponse,
    MigrationHubUntagResourceRequest,
    MigrationHubUntagResourceResponse,
    MigrationHubUpdateRouteRequest,
    MigrationHubUpdateRouteResponse,
)
from werkflow_aws.types.migration_hub_client import MigrationHubClient
from .base import AWSBaseService


class AWSMigrationHub(AWSBaseService[MigrationHubClient]):
    service_name = 'migration-hub'
    boto3_service_name = 'migration-hub-refactor-spaces'

    def __init__(self) -> None:
        super().__init__(service_name='migration-hub', boto3_service_name='migration-hub-refactor-spaces')

    async def create_application(
        self,
        request: MigrationHubCreateApplicationRequest,
    ) -> MigrationHubCreateApplicationResponse:
        client = self._require_client()
        return await self._execute(client.create_application, request, MigrationHubCreateApplicationResponse)

    async def create_environment(
        self,
        request: MigrationHubCreateEnvironmentRequest,
    ) -> MigrationHubCreateEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.create_environment, request, MigrationHubCreateEnvironmentResponse)

    async def create_route(
        self,
        request: MigrationHubCreateRouteRequest,
    ) -> MigrationHubCreateRouteResponse:
        client = self._require_client()
        return await self._execute(client.create_route, request, MigrationHubCreateRouteResponse)

    async def create_service(
        self,
        request: MigrationHubCreateServiceRequest,
    ) -> MigrationHubCreateServiceResponse:
        client = self._require_client()
        return await self._execute(client.create_service, request, MigrationHubCreateServiceResponse)

    async def delete_application(
        self,
        request: MigrationHubDeleteApplicationRequest,
    ) -> MigrationHubDeleteApplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_application, request, MigrationHubDeleteApplicationResponse)

    async def delete_environment(
        self,
        request: MigrationHubDeleteEnvironmentRequest,
    ) -> MigrationHubDeleteEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_environment, request, MigrationHubDeleteEnvironmentResponse)

    async def delete_resource_policy(
        self,
        request: MigrationHubDeleteResourcePolicyRequest,
    ) -> MigrationHubDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, MigrationHubDeleteResourcePolicyResponse)

    async def delete_route(
        self,
        request: MigrationHubDeleteRouteRequest,
    ) -> MigrationHubDeleteRouteResponse:
        client = self._require_client()
        return await self._execute(client.delete_route, request, MigrationHubDeleteRouteResponse)

    async def delete_service(
        self,
        request: MigrationHubDeleteServiceRequest,
    ) -> MigrationHubDeleteServiceResponse:
        client = self._require_client()
        return await self._execute(client.delete_service, request, MigrationHubDeleteServiceResponse)

    async def get_application(
        self,
        request: MigrationHubGetApplicationRequest,
    ) -> MigrationHubGetApplicationResponse:
        client = self._require_client()
        return await self._execute(client.get_application, request, MigrationHubGetApplicationResponse)

    async def get_environment(
        self,
        request: MigrationHubGetEnvironmentRequest,
    ) -> MigrationHubGetEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.get_environment, request, MigrationHubGetEnvironmentResponse)

    async def get_resource_policy(
        self,
        request: MigrationHubGetResourcePolicyRequest,
    ) -> MigrationHubGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, MigrationHubGetResourcePolicyResponse)

    async def get_route(
        self,
        request: MigrationHubGetRouteRequest,
    ) -> MigrationHubGetRouteResponse:
        client = self._require_client()
        return await self._execute(client.get_route, request, MigrationHubGetRouteResponse)

    async def get_service(
        self,
        request: MigrationHubGetServiceRequest,
    ) -> MigrationHubGetServiceResponse:
        client = self._require_client()
        return await self._execute(client.get_service, request, MigrationHubGetServiceResponse)

    async def list_applications(
        self,
        request: MigrationHubListApplicationsRequest,
    ) -> MigrationHubListApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.list_applications, request, MigrationHubListApplicationsResponse)

    async def list_applications_paginated(
        self,
        request: MigrationHubListApplicationsRequest,
    ) -> list[MigrationHubListApplicationsResponse]:
        return await self._paginate('list_applications', request, MigrationHubListApplicationsResponse)

    async def list_environment_vpcs(
        self,
        request: MigrationHubListEnvironmentVpcsRequest,
    ) -> MigrationHubListEnvironmentVpcsResponse:
        client = self._require_client()
        return await self._execute(client.list_environment_vpcs, request, MigrationHubListEnvironmentVpcsResponse)

    async def list_environment_vpcs_paginated(
        self,
        request: MigrationHubListEnvironmentVpcsRequest,
    ) -> list[MigrationHubListEnvironmentVpcsResponse]:
        return await self._paginate('list_environment_vpcs', request, MigrationHubListEnvironmentVpcsResponse)

    async def list_environments(
        self,
        request: MigrationHubListEnvironmentsRequest | None = None,
    ) -> MigrationHubListEnvironmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_environments, request, MigrationHubListEnvironmentsResponse)

    async def list_environments_paginated(
        self,
        request: MigrationHubListEnvironmentsRequest | None = None,
    ) -> list[MigrationHubListEnvironmentsResponse]:
        return await self._paginate('list_environments', request, MigrationHubListEnvironmentsResponse)

    async def list_routes(
        self,
        request: MigrationHubListRoutesRequest,
    ) -> MigrationHubListRoutesResponse:
        client = self._require_client()
        return await self._execute(client.list_routes, request, MigrationHubListRoutesResponse)

    async def list_routes_paginated(
        self,
        request: MigrationHubListRoutesRequest,
    ) -> list[MigrationHubListRoutesResponse]:
        return await self._paginate('list_routes', request, MigrationHubListRoutesResponse)

    async def list_services(
        self,
        request: MigrationHubListServicesRequest,
    ) -> MigrationHubListServicesResponse:
        client = self._require_client()
        return await self._execute(client.list_services, request, MigrationHubListServicesResponse)

    async def list_services_paginated(
        self,
        request: MigrationHubListServicesRequest,
    ) -> list[MigrationHubListServicesResponse]:
        return await self._paginate('list_services', request, MigrationHubListServicesResponse)

    async def list_tags_for_resource(
        self,
        request: MigrationHubListTagsForResourceRequest,
    ) -> MigrationHubListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, MigrationHubListTagsForResourceResponse)

    async def put_resource_policy(
        self,
        request: MigrationHubPutResourcePolicyRequest,
    ) -> MigrationHubPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, MigrationHubPutResourcePolicyResponse)

    async def tag_resource(
        self,
        request: MigrationHubTagResourceRequest,
    ) -> MigrationHubTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, MigrationHubTagResourceResponse)

    async def untag_resource(
        self,
        request: MigrationHubUntagResourceRequest,
    ) -> MigrationHubUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, MigrationHubUntagResourceResponse)

    async def update_route(
        self,
        request: MigrationHubUpdateRouteRequest,
    ) -> MigrationHubUpdateRouteResponse:
        client = self._require_client()
        return await self._execute(client.update_route, request, MigrationHubUpdateRouteResponse)
