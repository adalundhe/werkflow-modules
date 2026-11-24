from werkflow_aws.models.device_farm import (
    DeviceFarmCreateDevicePoolRequest,
    DeviceFarmCreateDevicePoolResponse,
    DeviceFarmCreateInstanceProfileRequest,
    DeviceFarmCreateInstanceProfileResponse,
    DeviceFarmCreateNetworkProfileRequest,
    DeviceFarmCreateNetworkProfileResponse,
    DeviceFarmCreateProjectRequest,
    DeviceFarmCreateProjectResponse,
    DeviceFarmCreateRemoteAccessSessionRequest,
    DeviceFarmCreateRemoteAccessSessionResponse,
    DeviceFarmCreateTestGridProjectRequest,
    DeviceFarmCreateTestGridProjectResponse,
    DeviceFarmCreateTestGridUrlRequest,
    DeviceFarmCreateTestGridUrlResponse,
    DeviceFarmCreateUploadRequest,
    DeviceFarmCreateUploadResponse,
    DeviceFarmCreateVPCEConfigurationRequest,
    DeviceFarmCreateVPCEConfigurationResponse,
    DeviceFarmDeleteDevicePoolRequest,
    DeviceFarmDeleteDevicePoolResponse,
    DeviceFarmDeleteInstanceProfileRequest,
    DeviceFarmDeleteInstanceProfileResponse,
    DeviceFarmDeleteNetworkProfileRequest,
    DeviceFarmDeleteNetworkProfileResponse,
    DeviceFarmDeleteProjectRequest,
    DeviceFarmDeleteProjectResponse,
    DeviceFarmDeleteRemoteAccessSessionRequest,
    DeviceFarmDeleteRemoteAccessSessionResponse,
    DeviceFarmDeleteRunRequest,
    DeviceFarmDeleteRunResponse,
    DeviceFarmDeleteTestGridProjectRequest,
    DeviceFarmDeleteTestGridProjectResponse,
    DeviceFarmDeleteUploadRequest,
    DeviceFarmDeleteUploadResponse,
    DeviceFarmDeleteVPCEConfigurationRequest,
    DeviceFarmDeleteVPCEConfigurationResponse,
    DeviceFarmGetAccountSettingsRequest,
    DeviceFarmGetAccountSettingsResponse,
    DeviceFarmGetDeviceInstanceRequest,
    DeviceFarmGetDeviceInstanceResponse,
    DeviceFarmGetDevicePoolCompatibilityRequest,
    DeviceFarmGetDevicePoolCompatibilityResponse,
    DeviceFarmGetDevicePoolRequest,
    DeviceFarmGetDevicePoolResponse,
    DeviceFarmGetDeviceRequest,
    DeviceFarmGetDeviceResponse,
    DeviceFarmGetInstanceProfileRequest,
    DeviceFarmGetInstanceProfileResponse,
    DeviceFarmGetJobRequest,
    DeviceFarmGetJobResponse,
    DeviceFarmGetNetworkProfileRequest,
    DeviceFarmGetNetworkProfileResponse,
    DeviceFarmGetOfferingStatusRequest,
    DeviceFarmGetOfferingStatusResponse,
    DeviceFarmGetProjectRequest,
    DeviceFarmGetProjectResponse,
    DeviceFarmGetRemoteAccessSessionRequest,
    DeviceFarmGetRemoteAccessSessionResponse,
    DeviceFarmGetRunRequest,
    DeviceFarmGetRunResponse,
    DeviceFarmGetSuiteRequest,
    DeviceFarmGetSuiteResponse,
    DeviceFarmGetTestGridProjectRequest,
    DeviceFarmGetTestGridProjectResponse,
    DeviceFarmGetTestGridSessionRequest,
    DeviceFarmGetTestGridSessionResponse,
    DeviceFarmGetTestRequest,
    DeviceFarmGetTestResponse,
    DeviceFarmGetUploadRequest,
    DeviceFarmGetUploadResponse,
    DeviceFarmGetVPCEConfigurationRequest,
    DeviceFarmGetVPCEConfigurationResponse,
    DeviceFarmInstallToRemoteAccessSessionRequest,
    DeviceFarmInstallToRemoteAccessSessionResponse,
    DeviceFarmListArtifactsRequest,
    DeviceFarmListArtifactsResponse,
    DeviceFarmListDeviceInstancesRequest,
    DeviceFarmListDeviceInstancesResponse,
    DeviceFarmListDevicePoolsRequest,
    DeviceFarmListDevicePoolsResponse,
    DeviceFarmListDevicesRequest,
    DeviceFarmListDevicesResponse,
    DeviceFarmListInstanceProfilesRequest,
    DeviceFarmListInstanceProfilesResponse,
    DeviceFarmListJobsRequest,
    DeviceFarmListJobsResponse,
    DeviceFarmListNetworkProfilesRequest,
    DeviceFarmListNetworkProfilesResponse,
    DeviceFarmListOfferingPromotionsRequest,
    DeviceFarmListOfferingPromotionsResponse,
    DeviceFarmListOfferingTransactionsRequest,
    DeviceFarmListOfferingTransactionsResponse,
    DeviceFarmListOfferingsRequest,
    DeviceFarmListOfferingsResponse,
    DeviceFarmListProjectsRequest,
    DeviceFarmListProjectsResponse,
    DeviceFarmListRemoteAccessSessionsRequest,
    DeviceFarmListRemoteAccessSessionsResponse,
    DeviceFarmListRunsRequest,
    DeviceFarmListRunsResponse,
    DeviceFarmListSamplesRequest,
    DeviceFarmListSamplesResponse,
    DeviceFarmListSuitesRequest,
    DeviceFarmListSuitesResponse,
    DeviceFarmListTagsForResourceRequest,
    DeviceFarmListTagsForResourceResponse,
    DeviceFarmListTestGridProjectsRequest,
    DeviceFarmListTestGridProjectsResponse,
    DeviceFarmListTestGridSessionActionsRequest,
    DeviceFarmListTestGridSessionActionsResponse,
    DeviceFarmListTestGridSessionArtifactsRequest,
    DeviceFarmListTestGridSessionArtifactsResponse,
    DeviceFarmListTestGridSessionsRequest,
    DeviceFarmListTestGridSessionsResponse,
    DeviceFarmListTestsRequest,
    DeviceFarmListTestsResponse,
    DeviceFarmListUniqueProblemsRequest,
    DeviceFarmListUniqueProblemsResponse,
    DeviceFarmListUploadsRequest,
    DeviceFarmListUploadsResponse,
    DeviceFarmListVPCEConfigurationsRequest,
    DeviceFarmListVPCEConfigurationsResponse,
    DeviceFarmPurchaseOfferingRequest,
    DeviceFarmPurchaseOfferingResponse,
    DeviceFarmRenewOfferingRequest,
    DeviceFarmRenewOfferingResponse,
    DeviceFarmScheduleRunRequest,
    DeviceFarmScheduleRunResponse,
    DeviceFarmStopJobRequest,
    DeviceFarmStopJobResponse,
    DeviceFarmStopRemoteAccessSessionRequest,
    DeviceFarmStopRemoteAccessSessionResponse,
    DeviceFarmStopRunRequest,
    DeviceFarmStopRunResponse,
    DeviceFarmTagResourceRequest,
    DeviceFarmTagResourceResponse,
    DeviceFarmUntagResourceRequest,
    DeviceFarmUntagResourceResponse,
    DeviceFarmUpdateDeviceInstanceRequest,
    DeviceFarmUpdateDeviceInstanceResponse,
    DeviceFarmUpdateDevicePoolRequest,
    DeviceFarmUpdateDevicePoolResponse,
    DeviceFarmUpdateInstanceProfileRequest,
    DeviceFarmUpdateInstanceProfileResponse,
    DeviceFarmUpdateNetworkProfileRequest,
    DeviceFarmUpdateNetworkProfileResponse,
    DeviceFarmUpdateProjectRequest,
    DeviceFarmUpdateProjectResponse,
    DeviceFarmUpdateTestGridProjectRequest,
    DeviceFarmUpdateTestGridProjectResponse,
    DeviceFarmUpdateUploadRequest,
    DeviceFarmUpdateUploadResponse,
    DeviceFarmUpdateVPCEConfigurationRequest,
    DeviceFarmUpdateVPCEConfigurationResponse,
)
from werkflow_aws.types.device_farm_client import DeviceFarmClient
from .base import AWSBaseService


class AWSDeviceFarm(AWSBaseService[DeviceFarmClient]):
    service_name = 'device-farm'
    boto3_service_name = 'devicefarm'

    def __init__(self) -> None:
        super().__init__(service_name='device-farm', boto3_service_name='devicefarm')

    async def create_device_pool(
        self,
        request: DeviceFarmCreateDevicePoolRequest,
    ) -> DeviceFarmCreateDevicePoolResponse:
        client = self._require_client()
        return await self._execute(client.create_device_pool, request, DeviceFarmCreateDevicePoolResponse)

    async def create_instance_profile(
        self,
        request: DeviceFarmCreateInstanceProfileRequest,
    ) -> DeviceFarmCreateInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_instance_profile, request, DeviceFarmCreateInstanceProfileResponse)

    async def create_network_profile(
        self,
        request: DeviceFarmCreateNetworkProfileRequest,
    ) -> DeviceFarmCreateNetworkProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_network_profile, request, DeviceFarmCreateNetworkProfileResponse)

    async def create_project(
        self,
        request: DeviceFarmCreateProjectRequest,
    ) -> DeviceFarmCreateProjectResponse:
        client = self._require_client()
        return await self._execute(client.create_project, request, DeviceFarmCreateProjectResponse)

    async def create_remote_access_session(
        self,
        request: DeviceFarmCreateRemoteAccessSessionRequest,
    ) -> DeviceFarmCreateRemoteAccessSessionResponse:
        client = self._require_client()
        return await self._execute(client.create_remote_access_session, request, DeviceFarmCreateRemoteAccessSessionResponse)

    async def create_test_grid_project(
        self,
        request: DeviceFarmCreateTestGridProjectRequest,
    ) -> DeviceFarmCreateTestGridProjectResponse:
        client = self._require_client()
        return await self._execute(client.create_test_grid_project, request, DeviceFarmCreateTestGridProjectResponse)

    async def create_test_grid_url(
        self,
        request: DeviceFarmCreateTestGridUrlRequest,
    ) -> DeviceFarmCreateTestGridUrlResponse:
        client = self._require_client()
        return await self._execute(client.create_test_grid_url, request, DeviceFarmCreateTestGridUrlResponse)

    async def create_upload(
        self,
        request: DeviceFarmCreateUploadRequest,
    ) -> DeviceFarmCreateUploadResponse:
        client = self._require_client()
        return await self._execute(client.create_upload, request, DeviceFarmCreateUploadResponse)

    async def create_vpce_configuration(
        self,
        request: DeviceFarmCreateVPCEConfigurationRequest,
    ) -> DeviceFarmCreateVPCEConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_vpce_configuration, request, DeviceFarmCreateVPCEConfigurationResponse)

    async def delete_device_pool(
        self,
        request: DeviceFarmDeleteDevicePoolRequest,
    ) -> DeviceFarmDeleteDevicePoolResponse:
        client = self._require_client()
        return await self._execute(client.delete_device_pool, request, DeviceFarmDeleteDevicePoolResponse)

    async def delete_instance_profile(
        self,
        request: DeviceFarmDeleteInstanceProfileRequest,
    ) -> DeviceFarmDeleteInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_instance_profile, request, DeviceFarmDeleteInstanceProfileResponse)

    async def delete_network_profile(
        self,
        request: DeviceFarmDeleteNetworkProfileRequest,
    ) -> DeviceFarmDeleteNetworkProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_network_profile, request, DeviceFarmDeleteNetworkProfileResponse)

    async def delete_project(
        self,
        request: DeviceFarmDeleteProjectRequest,
    ) -> DeviceFarmDeleteProjectResponse:
        client = self._require_client()
        return await self._execute(client.delete_project, request, DeviceFarmDeleteProjectResponse)

    async def delete_remote_access_session(
        self,
        request: DeviceFarmDeleteRemoteAccessSessionRequest,
    ) -> DeviceFarmDeleteRemoteAccessSessionResponse:
        client = self._require_client()
        return await self._execute(client.delete_remote_access_session, request, DeviceFarmDeleteRemoteAccessSessionResponse)

    async def delete_run(
        self,
        request: DeviceFarmDeleteRunRequest,
    ) -> DeviceFarmDeleteRunResponse:
        client = self._require_client()
        return await self._execute(client.delete_run, request, DeviceFarmDeleteRunResponse)

    async def delete_test_grid_project(
        self,
        request: DeviceFarmDeleteTestGridProjectRequest,
    ) -> DeviceFarmDeleteTestGridProjectResponse:
        client = self._require_client()
        return await self._execute(client.delete_test_grid_project, request, DeviceFarmDeleteTestGridProjectResponse)

    async def delete_upload(
        self,
        request: DeviceFarmDeleteUploadRequest,
    ) -> DeviceFarmDeleteUploadResponse:
        client = self._require_client()
        return await self._execute(client.delete_upload, request, DeviceFarmDeleteUploadResponse)

    async def delete_vpce_configuration(
        self,
        request: DeviceFarmDeleteVPCEConfigurationRequest,
    ) -> DeviceFarmDeleteVPCEConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpce_configuration, request, DeviceFarmDeleteVPCEConfigurationResponse)

    async def get_account_settings(
        self,
        request: DeviceFarmGetAccountSettingsRequest | None = None,
    ) -> DeviceFarmGetAccountSettingsResponse:
        client = self._require_client()
        return await self._execute(client.get_account_settings, request, DeviceFarmGetAccountSettingsResponse)

    async def get_device(
        self,
        request: DeviceFarmGetDeviceRequest,
    ) -> DeviceFarmGetDeviceResponse:
        client = self._require_client()
        return await self._execute(client.get_device, request, DeviceFarmGetDeviceResponse)

    async def get_device_instance(
        self,
        request: DeviceFarmGetDeviceInstanceRequest,
    ) -> DeviceFarmGetDeviceInstanceResponse:
        client = self._require_client()
        return await self._execute(client.get_device_instance, request, DeviceFarmGetDeviceInstanceResponse)

    async def get_device_pool(
        self,
        request: DeviceFarmGetDevicePoolRequest,
    ) -> DeviceFarmGetDevicePoolResponse:
        client = self._require_client()
        return await self._execute(client.get_device_pool, request, DeviceFarmGetDevicePoolResponse)

    async def get_device_pool_compatibility(
        self,
        request: DeviceFarmGetDevicePoolCompatibilityRequest,
    ) -> DeviceFarmGetDevicePoolCompatibilityResponse:
        client = self._require_client()
        return await self._execute(client.get_device_pool_compatibility, request, DeviceFarmGetDevicePoolCompatibilityResponse)

    async def get_instance_profile(
        self,
        request: DeviceFarmGetInstanceProfileRequest,
    ) -> DeviceFarmGetInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_instance_profile, request, DeviceFarmGetInstanceProfileResponse)

    async def get_job(
        self,
        request: DeviceFarmGetJobRequest,
    ) -> DeviceFarmGetJobResponse:
        client = self._require_client()
        return await self._execute(client.get_job, request, DeviceFarmGetJobResponse)

    async def get_network_profile(
        self,
        request: DeviceFarmGetNetworkProfileRequest,
    ) -> DeviceFarmGetNetworkProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_network_profile, request, DeviceFarmGetNetworkProfileResponse)

    async def get_offering_status(
        self,
        request: DeviceFarmGetOfferingStatusRequest | None = None,
    ) -> DeviceFarmGetOfferingStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_offering_status, request, DeviceFarmGetOfferingStatusResponse)

    async def get_offering_status_paginated(
        self,
        request: DeviceFarmGetOfferingStatusRequest | None = None,
    ) -> list[DeviceFarmGetOfferingStatusResponse]:
        return await self._paginate('get_offering_status', request, DeviceFarmGetOfferingStatusResponse)

    async def get_project(
        self,
        request: DeviceFarmGetProjectRequest,
    ) -> DeviceFarmGetProjectResponse:
        client = self._require_client()
        return await self._execute(client.get_project, request, DeviceFarmGetProjectResponse)

    async def get_remote_access_session(
        self,
        request: DeviceFarmGetRemoteAccessSessionRequest,
    ) -> DeviceFarmGetRemoteAccessSessionResponse:
        client = self._require_client()
        return await self._execute(client.get_remote_access_session, request, DeviceFarmGetRemoteAccessSessionResponse)

    async def get_run(
        self,
        request: DeviceFarmGetRunRequest,
    ) -> DeviceFarmGetRunResponse:
        client = self._require_client()
        return await self._execute(client.get_run, request, DeviceFarmGetRunResponse)

    async def get_suite(
        self,
        request: DeviceFarmGetSuiteRequest,
    ) -> DeviceFarmGetSuiteResponse:
        client = self._require_client()
        return await self._execute(client.get_suite, request, DeviceFarmGetSuiteResponse)

    async def get_test(
        self,
        request: DeviceFarmGetTestRequest,
    ) -> DeviceFarmGetTestResponse:
        client = self._require_client()
        return await self._execute(client.get_test, request, DeviceFarmGetTestResponse)

    async def get_test_grid_project(
        self,
        request: DeviceFarmGetTestGridProjectRequest,
    ) -> DeviceFarmGetTestGridProjectResponse:
        client = self._require_client()
        return await self._execute(client.get_test_grid_project, request, DeviceFarmGetTestGridProjectResponse)

    async def get_test_grid_session(
        self,
        request: DeviceFarmGetTestGridSessionRequest | None = None,
    ) -> DeviceFarmGetTestGridSessionResponse:
        client = self._require_client()
        return await self._execute(client.get_test_grid_session, request, DeviceFarmGetTestGridSessionResponse)

    async def get_upload(
        self,
        request: DeviceFarmGetUploadRequest,
    ) -> DeviceFarmGetUploadResponse:
        client = self._require_client()
        return await self._execute(client.get_upload, request, DeviceFarmGetUploadResponse)

    async def get_vpce_configuration(
        self,
        request: DeviceFarmGetVPCEConfigurationRequest,
    ) -> DeviceFarmGetVPCEConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_vpce_configuration, request, DeviceFarmGetVPCEConfigurationResponse)

    async def install_to_remote_access_session(
        self,
        request: DeviceFarmInstallToRemoteAccessSessionRequest,
    ) -> DeviceFarmInstallToRemoteAccessSessionResponse:
        client = self._require_client()
        return await self._execute(client.install_to_remote_access_session, request, DeviceFarmInstallToRemoteAccessSessionResponse)

    async def list_artifacts(
        self,
        request: DeviceFarmListArtifactsRequest,
    ) -> DeviceFarmListArtifactsResponse:
        client = self._require_client()
        return await self._execute(client.list_artifacts, request, DeviceFarmListArtifactsResponse)

    async def list_artifacts_paginated(
        self,
        request: DeviceFarmListArtifactsRequest,
    ) -> list[DeviceFarmListArtifactsResponse]:
        return await self._paginate('list_artifacts', request, DeviceFarmListArtifactsResponse)

    async def list_device_instances(
        self,
        request: DeviceFarmListDeviceInstancesRequest | None = None,
    ) -> DeviceFarmListDeviceInstancesResponse:
        client = self._require_client()
        return await self._execute(client.list_device_instances, request, DeviceFarmListDeviceInstancesResponse)

    async def list_device_instances_paginated(
        self,
        request: DeviceFarmListDeviceInstancesRequest | None = None,
    ) -> list[DeviceFarmListDeviceInstancesResponse]:
        return await self._paginate('list_device_instances', request, DeviceFarmListDeviceInstancesResponse)

    async def list_device_pools(
        self,
        request: DeviceFarmListDevicePoolsRequest,
    ) -> DeviceFarmListDevicePoolsResponse:
        client = self._require_client()
        return await self._execute(client.list_device_pools, request, DeviceFarmListDevicePoolsResponse)

    async def list_device_pools_paginated(
        self,
        request: DeviceFarmListDevicePoolsRequest,
    ) -> list[DeviceFarmListDevicePoolsResponse]:
        return await self._paginate('list_device_pools', request, DeviceFarmListDevicePoolsResponse)

    async def list_devices(
        self,
        request: DeviceFarmListDevicesRequest | None = None,
    ) -> DeviceFarmListDevicesResponse:
        client = self._require_client()
        return await self._execute(client.list_devices, request, DeviceFarmListDevicesResponse)

    async def list_devices_paginated(
        self,
        request: DeviceFarmListDevicesRequest | None = None,
    ) -> list[DeviceFarmListDevicesResponse]:
        return await self._paginate('list_devices', request, DeviceFarmListDevicesResponse)

    async def list_instance_profiles(
        self,
        request: DeviceFarmListInstanceProfilesRequest | None = None,
    ) -> DeviceFarmListInstanceProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_instance_profiles, request, DeviceFarmListInstanceProfilesResponse)

    async def list_instance_profiles_paginated(
        self,
        request: DeviceFarmListInstanceProfilesRequest | None = None,
    ) -> list[DeviceFarmListInstanceProfilesResponse]:
        return await self._paginate('list_instance_profiles', request, DeviceFarmListInstanceProfilesResponse)

    async def list_jobs(
        self,
        request: DeviceFarmListJobsRequest,
    ) -> DeviceFarmListJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_jobs, request, DeviceFarmListJobsResponse)

    async def list_jobs_paginated(
        self,
        request: DeviceFarmListJobsRequest,
    ) -> list[DeviceFarmListJobsResponse]:
        return await self._paginate('list_jobs', request, DeviceFarmListJobsResponse)

    async def list_network_profiles(
        self,
        request: DeviceFarmListNetworkProfilesRequest,
    ) -> DeviceFarmListNetworkProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_network_profiles, request, DeviceFarmListNetworkProfilesResponse)

    async def list_network_profiles_paginated(
        self,
        request: DeviceFarmListNetworkProfilesRequest,
    ) -> list[DeviceFarmListNetworkProfilesResponse]:
        return await self._paginate('list_network_profiles', request, DeviceFarmListNetworkProfilesResponse)

    async def list_offering_promotions(
        self,
        request: DeviceFarmListOfferingPromotionsRequest | None = None,
    ) -> DeviceFarmListOfferingPromotionsResponse:
        client = self._require_client()
        return await self._execute(client.list_offering_promotions, request, DeviceFarmListOfferingPromotionsResponse)

    async def list_offering_promotions_paginated(
        self,
        request: DeviceFarmListOfferingPromotionsRequest | None = None,
    ) -> list[DeviceFarmListOfferingPromotionsResponse]:
        return await self._paginate('list_offering_promotions', request, DeviceFarmListOfferingPromotionsResponse)

    async def list_offering_transactions(
        self,
        request: DeviceFarmListOfferingTransactionsRequest | None = None,
    ) -> DeviceFarmListOfferingTransactionsResponse:
        client = self._require_client()
        return await self._execute(client.list_offering_transactions, request, DeviceFarmListOfferingTransactionsResponse)

    async def list_offering_transactions_paginated(
        self,
        request: DeviceFarmListOfferingTransactionsRequest | None = None,
    ) -> list[DeviceFarmListOfferingTransactionsResponse]:
        return await self._paginate('list_offering_transactions', request, DeviceFarmListOfferingTransactionsResponse)

    async def list_offerings(
        self,
        request: DeviceFarmListOfferingsRequest | None = None,
    ) -> DeviceFarmListOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.list_offerings, request, DeviceFarmListOfferingsResponse)

    async def list_offerings_paginated(
        self,
        request: DeviceFarmListOfferingsRequest | None = None,
    ) -> list[DeviceFarmListOfferingsResponse]:
        return await self._paginate('list_offerings', request, DeviceFarmListOfferingsResponse)

    async def list_projects(
        self,
        request: DeviceFarmListProjectsRequest | None = None,
    ) -> DeviceFarmListProjectsResponse:
        client = self._require_client()
        return await self._execute(client.list_projects, request, DeviceFarmListProjectsResponse)

    async def list_projects_paginated(
        self,
        request: DeviceFarmListProjectsRequest | None = None,
    ) -> list[DeviceFarmListProjectsResponse]:
        return await self._paginate('list_projects', request, DeviceFarmListProjectsResponse)

    async def list_remote_access_sessions(
        self,
        request: DeviceFarmListRemoteAccessSessionsRequest,
    ) -> DeviceFarmListRemoteAccessSessionsResponse:
        client = self._require_client()
        return await self._execute(client.list_remote_access_sessions, request, DeviceFarmListRemoteAccessSessionsResponse)

    async def list_remote_access_sessions_paginated(
        self,
        request: DeviceFarmListRemoteAccessSessionsRequest,
    ) -> list[DeviceFarmListRemoteAccessSessionsResponse]:
        return await self._paginate('list_remote_access_sessions', request, DeviceFarmListRemoteAccessSessionsResponse)

    async def list_runs(
        self,
        request: DeviceFarmListRunsRequest,
    ) -> DeviceFarmListRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_runs, request, DeviceFarmListRunsResponse)

    async def list_runs_paginated(
        self,
        request: DeviceFarmListRunsRequest,
    ) -> list[DeviceFarmListRunsResponse]:
        return await self._paginate('list_runs', request, DeviceFarmListRunsResponse)

    async def list_samples(
        self,
        request: DeviceFarmListSamplesRequest,
    ) -> DeviceFarmListSamplesResponse:
        client = self._require_client()
        return await self._execute(client.list_samples, request, DeviceFarmListSamplesResponse)

    async def list_samples_paginated(
        self,
        request: DeviceFarmListSamplesRequest,
    ) -> list[DeviceFarmListSamplesResponse]:
        return await self._paginate('list_samples', request, DeviceFarmListSamplesResponse)

    async def list_suites(
        self,
        request: DeviceFarmListSuitesRequest,
    ) -> DeviceFarmListSuitesResponse:
        client = self._require_client()
        return await self._execute(client.list_suites, request, DeviceFarmListSuitesResponse)

    async def list_suites_paginated(
        self,
        request: DeviceFarmListSuitesRequest,
    ) -> list[DeviceFarmListSuitesResponse]:
        return await self._paginate('list_suites', request, DeviceFarmListSuitesResponse)

    async def list_tags_for_resource(
        self,
        request: DeviceFarmListTagsForResourceRequest,
    ) -> DeviceFarmListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, DeviceFarmListTagsForResourceResponse)

    async def list_test_grid_projects(
        self,
        request: DeviceFarmListTestGridProjectsRequest | None = None,
    ) -> DeviceFarmListTestGridProjectsResponse:
        client = self._require_client()
        return await self._execute(client.list_test_grid_projects, request, DeviceFarmListTestGridProjectsResponse)

    async def list_test_grid_session_actions(
        self,
        request: DeviceFarmListTestGridSessionActionsRequest,
    ) -> DeviceFarmListTestGridSessionActionsResponse:
        client = self._require_client()
        return await self._execute(client.list_test_grid_session_actions, request, DeviceFarmListTestGridSessionActionsResponse)

    async def list_test_grid_session_artifacts(
        self,
        request: DeviceFarmListTestGridSessionArtifactsRequest,
    ) -> DeviceFarmListTestGridSessionArtifactsResponse:
        client = self._require_client()
        return await self._execute(client.list_test_grid_session_artifacts, request, DeviceFarmListTestGridSessionArtifactsResponse)

    async def list_test_grid_sessions(
        self,
        request: DeviceFarmListTestGridSessionsRequest,
    ) -> DeviceFarmListTestGridSessionsResponse:
        client = self._require_client()
        return await self._execute(client.list_test_grid_sessions, request, DeviceFarmListTestGridSessionsResponse)

    async def list_tests(
        self,
        request: DeviceFarmListTestsRequest,
    ) -> DeviceFarmListTestsResponse:
        client = self._require_client()
        return await self._execute(client.list_tests, request, DeviceFarmListTestsResponse)

    async def list_tests_paginated(
        self,
        request: DeviceFarmListTestsRequest,
    ) -> list[DeviceFarmListTestsResponse]:
        return await self._paginate('list_tests', request, DeviceFarmListTestsResponse)

    async def list_unique_problems(
        self,
        request: DeviceFarmListUniqueProblemsRequest,
    ) -> DeviceFarmListUniqueProblemsResponse:
        client = self._require_client()
        return await self._execute(client.list_unique_problems, request, DeviceFarmListUniqueProblemsResponse)

    async def list_unique_problems_paginated(
        self,
        request: DeviceFarmListUniqueProblemsRequest,
    ) -> list[DeviceFarmListUniqueProblemsResponse]:
        return await self._paginate('list_unique_problems', request, DeviceFarmListUniqueProblemsResponse)

    async def list_uploads(
        self,
        request: DeviceFarmListUploadsRequest,
    ) -> DeviceFarmListUploadsResponse:
        client = self._require_client()
        return await self._execute(client.list_uploads, request, DeviceFarmListUploadsResponse)

    async def list_uploads_paginated(
        self,
        request: DeviceFarmListUploadsRequest,
    ) -> list[DeviceFarmListUploadsResponse]:
        return await self._paginate('list_uploads', request, DeviceFarmListUploadsResponse)

    async def list_vpce_configurations(
        self,
        request: DeviceFarmListVPCEConfigurationsRequest | None = None,
    ) -> DeviceFarmListVPCEConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_vpce_configurations, request, DeviceFarmListVPCEConfigurationsResponse)

    async def list_vpce_configurations_paginated(
        self,
        request: DeviceFarmListVPCEConfigurationsRequest | None = None,
    ) -> list[DeviceFarmListVPCEConfigurationsResponse]:
        return await self._paginate('list_vpce_configurations', request, DeviceFarmListVPCEConfigurationsResponse)

    async def purchase_offering(
        self,
        request: DeviceFarmPurchaseOfferingRequest,
    ) -> DeviceFarmPurchaseOfferingResponse:
        client = self._require_client()
        return await self._execute(client.purchase_offering, request, DeviceFarmPurchaseOfferingResponse)

    async def renew_offering(
        self,
        request: DeviceFarmRenewOfferingRequest,
    ) -> DeviceFarmRenewOfferingResponse:
        client = self._require_client()
        return await self._execute(client.renew_offering, request, DeviceFarmRenewOfferingResponse)

    async def schedule_run(
        self,
        request: DeviceFarmScheduleRunRequest,
    ) -> DeviceFarmScheduleRunResponse:
        client = self._require_client()
        return await self._execute(client.schedule_run, request, DeviceFarmScheduleRunResponse)

    async def stop_job(
        self,
        request: DeviceFarmStopJobRequest,
    ) -> DeviceFarmStopJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_job, request, DeviceFarmStopJobResponse)

    async def stop_remote_access_session(
        self,
        request: DeviceFarmStopRemoteAccessSessionRequest,
    ) -> DeviceFarmStopRemoteAccessSessionResponse:
        client = self._require_client()
        return await self._execute(client.stop_remote_access_session, request, DeviceFarmStopRemoteAccessSessionResponse)

    async def stop_run(
        self,
        request: DeviceFarmStopRunRequest,
    ) -> DeviceFarmStopRunResponse:
        client = self._require_client()
        return await self._execute(client.stop_run, request, DeviceFarmStopRunResponse)

    async def tag_resource(
        self,
        request: DeviceFarmTagResourceRequest,
    ) -> DeviceFarmTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, DeviceFarmTagResourceResponse)

    async def untag_resource(
        self,
        request: DeviceFarmUntagResourceRequest,
    ) -> DeviceFarmUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, DeviceFarmUntagResourceResponse)

    async def update_device_instance(
        self,
        request: DeviceFarmUpdateDeviceInstanceRequest,
    ) -> DeviceFarmUpdateDeviceInstanceResponse:
        client = self._require_client()
        return await self._execute(client.update_device_instance, request, DeviceFarmUpdateDeviceInstanceResponse)

    async def update_device_pool(
        self,
        request: DeviceFarmUpdateDevicePoolRequest,
    ) -> DeviceFarmUpdateDevicePoolResponse:
        client = self._require_client()
        return await self._execute(client.update_device_pool, request, DeviceFarmUpdateDevicePoolResponse)

    async def update_instance_profile(
        self,
        request: DeviceFarmUpdateInstanceProfileRequest,
    ) -> DeviceFarmUpdateInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_instance_profile, request, DeviceFarmUpdateInstanceProfileResponse)

    async def update_network_profile(
        self,
        request: DeviceFarmUpdateNetworkProfileRequest,
    ) -> DeviceFarmUpdateNetworkProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_network_profile, request, DeviceFarmUpdateNetworkProfileResponse)

    async def update_project(
        self,
        request: DeviceFarmUpdateProjectRequest,
    ) -> DeviceFarmUpdateProjectResponse:
        client = self._require_client()
        return await self._execute(client.update_project, request, DeviceFarmUpdateProjectResponse)

    async def update_test_grid_project(
        self,
        request: DeviceFarmUpdateTestGridProjectRequest,
    ) -> DeviceFarmUpdateTestGridProjectResponse:
        client = self._require_client()
        return await self._execute(client.update_test_grid_project, request, DeviceFarmUpdateTestGridProjectResponse)

    async def update_upload(
        self,
        request: DeviceFarmUpdateUploadRequest,
    ) -> DeviceFarmUpdateUploadResponse:
        client = self._require_client()
        return await self._execute(client.update_upload, request, DeviceFarmUpdateUploadResponse)

    async def update_vpce_configuration(
        self,
        request: DeviceFarmUpdateVPCEConfigurationRequest,
    ) -> DeviceFarmUpdateVPCEConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_vpce_configuration, request, DeviceFarmUpdateVPCEConfigurationResponse)
