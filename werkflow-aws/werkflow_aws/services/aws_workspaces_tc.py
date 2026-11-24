from werkflow_aws.models.workspaces_tc import (
    WorkSpacesThinClientCreateEnvironmentRequest,
    WorkSpacesThinClientCreateEnvironmentResponse,
    WorkSpacesThinClientDeleteDeviceRequest,
    WorkSpacesThinClientDeleteDeviceResponse,
    WorkSpacesThinClientDeleteEnvironmentRequest,
    WorkSpacesThinClientDeleteEnvironmentResponse,
    WorkSpacesThinClientDeregisterDeviceRequest,
    WorkSpacesThinClientDeregisterDeviceResponse,
    WorkSpacesThinClientGetDeviceRequest,
    WorkSpacesThinClientGetDeviceResponse,
    WorkSpacesThinClientGetEnvironmentRequest,
    WorkSpacesThinClientGetEnvironmentResponse,
    WorkSpacesThinClientGetSoftwareSetRequest,
    WorkSpacesThinClientGetSoftwareSetResponse,
    WorkSpacesThinClientListDevicesRequest,
    WorkSpacesThinClientListDevicesResponse,
    WorkSpacesThinClientListEnvironmentsRequest,
    WorkSpacesThinClientListEnvironmentsResponse,
    WorkSpacesThinClientListSoftwareSetsRequest,
    WorkSpacesThinClientListSoftwareSetsResponse,
    WorkSpacesThinClientListTagsForResourceRequest,
    WorkSpacesThinClientListTagsForResourceResponse,
    WorkSpacesThinClientTagResourceRequest,
    WorkSpacesThinClientTagResourceResponse,
    WorkSpacesThinClientUntagResourceRequest,
    WorkSpacesThinClientUntagResourceResponse,
    WorkSpacesThinClientUpdateDeviceRequest,
    WorkSpacesThinClientUpdateDeviceResponse,
    WorkSpacesThinClientUpdateEnvironmentRequest,
    WorkSpacesThinClientUpdateEnvironmentResponse,
    WorkSpacesThinClientUpdateSoftwareSetRequest,
    WorkSpacesThinClientUpdateSoftwareSetResponse,
)
from werkflow_aws.types.workspaces_tc_client import WorkSpacesThinClientClient
from .base import AWSBaseService


class AWSWorkSpacesThinClient(AWSBaseService[WorkSpacesThinClientClient]):
    service_name = 'workspaces-tc'
    boto3_service_name = 'workspaces-thin-client'

    def __init__(self) -> None:
        super().__init__(service_name='workspaces-tc', boto3_service_name='workspaces-thin-client')

    async def create_environment(
        self,
        request: WorkSpacesThinClientCreateEnvironmentRequest,
    ) -> WorkSpacesThinClientCreateEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.create_environment, request, WorkSpacesThinClientCreateEnvironmentResponse)

    async def delete_device(
        self,
        request: WorkSpacesThinClientDeleteDeviceRequest,
    ) -> WorkSpacesThinClientDeleteDeviceResponse:
        client = self._require_client()
        return await self._execute(client.delete_device, request, WorkSpacesThinClientDeleteDeviceResponse)

    async def delete_environment(
        self,
        request: WorkSpacesThinClientDeleteEnvironmentRequest,
    ) -> WorkSpacesThinClientDeleteEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_environment, request, WorkSpacesThinClientDeleteEnvironmentResponse)

    async def deregister_device(
        self,
        request: WorkSpacesThinClientDeregisterDeviceRequest,
    ) -> WorkSpacesThinClientDeregisterDeviceResponse:
        client = self._require_client()
        return await self._execute(client.deregister_device, request, WorkSpacesThinClientDeregisterDeviceResponse)

    async def get_device(
        self,
        request: WorkSpacesThinClientGetDeviceRequest,
    ) -> WorkSpacesThinClientGetDeviceResponse:
        client = self._require_client()
        return await self._execute(client.get_device, request, WorkSpacesThinClientGetDeviceResponse)

    async def get_environment(
        self,
        request: WorkSpacesThinClientGetEnvironmentRequest,
    ) -> WorkSpacesThinClientGetEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.get_environment, request, WorkSpacesThinClientGetEnvironmentResponse)

    async def get_software_set(
        self,
        request: WorkSpacesThinClientGetSoftwareSetRequest,
    ) -> WorkSpacesThinClientGetSoftwareSetResponse:
        client = self._require_client()
        return await self._execute(client.get_software_set, request, WorkSpacesThinClientGetSoftwareSetResponse)

    async def list_devices(
        self,
        request: WorkSpacesThinClientListDevicesRequest | None = None,
    ) -> WorkSpacesThinClientListDevicesResponse:
        client = self._require_client()
        return await self._execute(client.list_devices, request, WorkSpacesThinClientListDevicesResponse)

    async def list_devices_paginated(
        self,
        request: WorkSpacesThinClientListDevicesRequest | None = None,
    ) -> list[WorkSpacesThinClientListDevicesResponse]:
        return await self._paginate('list_devices', request, WorkSpacesThinClientListDevicesResponse)

    async def list_environments(
        self,
        request: WorkSpacesThinClientListEnvironmentsRequest | None = None,
    ) -> WorkSpacesThinClientListEnvironmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_environments, request, WorkSpacesThinClientListEnvironmentsResponse)

    async def list_environments_paginated(
        self,
        request: WorkSpacesThinClientListEnvironmentsRequest | None = None,
    ) -> list[WorkSpacesThinClientListEnvironmentsResponse]:
        return await self._paginate('list_environments', request, WorkSpacesThinClientListEnvironmentsResponse)

    async def list_software_sets(
        self,
        request: WorkSpacesThinClientListSoftwareSetsRequest | None = None,
    ) -> WorkSpacesThinClientListSoftwareSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_software_sets, request, WorkSpacesThinClientListSoftwareSetsResponse)

    async def list_software_sets_paginated(
        self,
        request: WorkSpacesThinClientListSoftwareSetsRequest | None = None,
    ) -> list[WorkSpacesThinClientListSoftwareSetsResponse]:
        return await self._paginate('list_software_sets', request, WorkSpacesThinClientListSoftwareSetsResponse)

    async def list_tags_for_resource(
        self,
        request: WorkSpacesThinClientListTagsForResourceRequest,
    ) -> WorkSpacesThinClientListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, WorkSpacesThinClientListTagsForResourceResponse)

    async def tag_resource(
        self,
        request: WorkSpacesThinClientTagResourceRequest,
    ) -> WorkSpacesThinClientTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, WorkSpacesThinClientTagResourceResponse)

    async def untag_resource(
        self,
        request: WorkSpacesThinClientUntagResourceRequest,
    ) -> WorkSpacesThinClientUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, WorkSpacesThinClientUntagResourceResponse)

    async def update_device(
        self,
        request: WorkSpacesThinClientUpdateDeviceRequest,
    ) -> WorkSpacesThinClientUpdateDeviceResponse:
        client = self._require_client()
        return await self._execute(client.update_device, request, WorkSpacesThinClientUpdateDeviceResponse)

    async def update_environment(
        self,
        request: WorkSpacesThinClientUpdateEnvironmentRequest,
    ) -> WorkSpacesThinClientUpdateEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.update_environment, request, WorkSpacesThinClientUpdateEnvironmentResponse)

    async def update_software_set(
        self,
        request: WorkSpacesThinClientUpdateSoftwareSetRequest,
    ) -> WorkSpacesThinClientUpdateSoftwareSetResponse:
        client = self._require_client()
        return await self._execute(client.update_software_set, request, WorkSpacesThinClientUpdateSoftwareSetResponse)
