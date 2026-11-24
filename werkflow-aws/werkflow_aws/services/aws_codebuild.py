from werkflow_aws.models.codebuild import (
    CodeBuildBatchDeleteBuildsRequest,
    CodeBuildBatchDeleteBuildsResponse,
    CodeBuildBatchGetBuildBatchesRequest,
    CodeBuildBatchGetBuildBatchesResponse,
    CodeBuildBatchGetBuildsRequest,
    CodeBuildBatchGetBuildsResponse,
    CodeBuildBatchGetCommandExecutionsRequest,
    CodeBuildBatchGetCommandExecutionsResponse,
    CodeBuildBatchGetFleetsRequest,
    CodeBuildBatchGetFleetsResponse,
    CodeBuildBatchGetProjectsRequest,
    CodeBuildBatchGetProjectsResponse,
    CodeBuildBatchGetReportGroupsRequest,
    CodeBuildBatchGetReportGroupsResponse,
    CodeBuildBatchGetReportsRequest,
    CodeBuildBatchGetReportsResponse,
    CodeBuildBatchGetSandboxesRequest,
    CodeBuildBatchGetSandboxesResponse,
    CodeBuildCreateFleetRequest,
    CodeBuildCreateFleetResponse,
    CodeBuildCreateProjectRequest,
    CodeBuildCreateProjectResponse,
    CodeBuildCreateReportGroupRequest,
    CodeBuildCreateReportGroupResponse,
    CodeBuildCreateWebhookRequest,
    CodeBuildCreateWebhookResponse,
    CodeBuildDeleteBuildBatchRequest,
    CodeBuildDeleteBuildBatchResponse,
    CodeBuildDeleteFleetRequest,
    CodeBuildDeleteFleetResponse,
    CodeBuildDeleteProjectRequest,
    CodeBuildDeleteProjectResponse,
    CodeBuildDeleteReportGroupRequest,
    CodeBuildDeleteReportGroupResponse,
    CodeBuildDeleteReportRequest,
    CodeBuildDeleteReportResponse,
    CodeBuildDeleteResourcePolicyRequest,
    CodeBuildDeleteResourcePolicyResponse,
    CodeBuildDeleteSourceCredentialsRequest,
    CodeBuildDeleteSourceCredentialsResponse,
    CodeBuildDeleteWebhookRequest,
    CodeBuildDeleteWebhookResponse,
    CodeBuildDescribeCodeCoveragesRequest,
    CodeBuildDescribeCodeCoveragesResponse,
    CodeBuildDescribeTestCasesRequest,
    CodeBuildDescribeTestCasesResponse,
    CodeBuildGetReportGroupTrendRequest,
    CodeBuildGetReportGroupTrendResponse,
    CodeBuildGetResourcePolicyRequest,
    CodeBuildGetResourcePolicyResponse,
    CodeBuildImportSourceCredentialsRequest,
    CodeBuildImportSourceCredentialsResponse,
    CodeBuildInvalidateProjectCacheRequest,
    CodeBuildInvalidateProjectCacheResponse,
    CodeBuildListBuildBatchesForProjectRequest,
    CodeBuildListBuildBatchesForProjectResponse,
    CodeBuildListBuildBatchesRequest,
    CodeBuildListBuildBatchesResponse,
    CodeBuildListBuildsForProjectRequest,
    CodeBuildListBuildsForProjectResponse,
    CodeBuildListBuildsRequest,
    CodeBuildListBuildsResponse,
    CodeBuildListCommandExecutionsForSandboxRequest,
    CodeBuildListCommandExecutionsForSandboxResponse,
    CodeBuildListCuratedEnvironmentImagesRequest,
    CodeBuildListCuratedEnvironmentImagesResponse,
    CodeBuildListFleetsRequest,
    CodeBuildListFleetsResponse,
    CodeBuildListProjectsRequest,
    CodeBuildListProjectsResponse,
    CodeBuildListReportGroupsRequest,
    CodeBuildListReportGroupsResponse,
    CodeBuildListReportsForReportGroupRequest,
    CodeBuildListReportsForReportGroupResponse,
    CodeBuildListReportsRequest,
    CodeBuildListReportsResponse,
    CodeBuildListSandboxesForProjectRequest,
    CodeBuildListSandboxesForProjectResponse,
    CodeBuildListSandboxesRequest,
    CodeBuildListSandboxesResponse,
    CodeBuildListSharedProjectsRequest,
    CodeBuildListSharedProjectsResponse,
    CodeBuildListSharedReportGroupsRequest,
    CodeBuildListSharedReportGroupsResponse,
    CodeBuildListSourceCredentialsRequest,
    CodeBuildListSourceCredentialsResponse,
    CodeBuildPutResourcePolicyRequest,
    CodeBuildPutResourcePolicyResponse,
    CodeBuildRetryBuildBatchRequest,
    CodeBuildRetryBuildBatchResponse,
    CodeBuildRetryBuildRequest,
    CodeBuildRetryBuildResponse,
    CodeBuildStartBuildBatchRequest,
    CodeBuildStartBuildBatchResponse,
    CodeBuildStartBuildRequest,
    CodeBuildStartBuildResponse,
    CodeBuildStartCommandExecutionRequest,
    CodeBuildStartCommandExecutionResponse,
    CodeBuildStartSandboxConnectionRequest,
    CodeBuildStartSandboxConnectionResponse,
    CodeBuildStartSandboxRequest,
    CodeBuildStartSandboxResponse,
    CodeBuildStopBuildBatchRequest,
    CodeBuildStopBuildBatchResponse,
    CodeBuildStopBuildRequest,
    CodeBuildStopBuildResponse,
    CodeBuildStopSandboxRequest,
    CodeBuildStopSandboxResponse,
    CodeBuildUpdateFleetRequest,
    CodeBuildUpdateFleetResponse,
    CodeBuildUpdateProjectRequest,
    CodeBuildUpdateProjectResponse,
    CodeBuildUpdateProjectVisibilityRequest,
    CodeBuildUpdateProjectVisibilityResponse,
    CodeBuildUpdateReportGroupRequest,
    CodeBuildUpdateReportGroupResponse,
    CodeBuildUpdateWebhookRequest,
    CodeBuildUpdateWebhookResponse,
)
from werkflow_aws.types.codebuild_client import CodeBuildClient
from .base import AWSBaseService


class AWSCodeBuild(AWSBaseService[CodeBuildClient]):
    service_name = 'codebuild'
    boto3_service_name = 'codebuild'

    def __init__(self) -> None:
        super().__init__(service_name='codebuild', boto3_service_name='codebuild')

    async def batch_delete_builds(
        self,
        request: CodeBuildBatchDeleteBuildsRequest,
    ) -> CodeBuildBatchDeleteBuildsResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_builds, request, CodeBuildBatchDeleteBuildsResponse)

    async def batch_get_build_batches(
        self,
        request: CodeBuildBatchGetBuildBatchesRequest,
    ) -> CodeBuildBatchGetBuildBatchesResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_build_batches, request, CodeBuildBatchGetBuildBatchesResponse)

    async def batch_get_builds(
        self,
        request: CodeBuildBatchGetBuildsRequest,
    ) -> CodeBuildBatchGetBuildsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_builds, request, CodeBuildBatchGetBuildsResponse)

    async def batch_get_command_executions(
        self,
        request: CodeBuildBatchGetCommandExecutionsRequest,
    ) -> CodeBuildBatchGetCommandExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_command_executions, request, CodeBuildBatchGetCommandExecutionsResponse)

    async def batch_get_fleets(
        self,
        request: CodeBuildBatchGetFleetsRequest,
    ) -> CodeBuildBatchGetFleetsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_fleets, request, CodeBuildBatchGetFleetsResponse)

    async def batch_get_projects(
        self,
        request: CodeBuildBatchGetProjectsRequest,
    ) -> CodeBuildBatchGetProjectsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_projects, request, CodeBuildBatchGetProjectsResponse)

    async def batch_get_report_groups(
        self,
        request: CodeBuildBatchGetReportGroupsRequest,
    ) -> CodeBuildBatchGetReportGroupsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_report_groups, request, CodeBuildBatchGetReportGroupsResponse)

    async def batch_get_reports(
        self,
        request: CodeBuildBatchGetReportsRequest,
    ) -> CodeBuildBatchGetReportsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_reports, request, CodeBuildBatchGetReportsResponse)

    async def batch_get_sandboxes(
        self,
        request: CodeBuildBatchGetSandboxesRequest,
    ) -> CodeBuildBatchGetSandboxesResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_sandboxes, request, CodeBuildBatchGetSandboxesResponse)

    async def create_fleet(
        self,
        request: CodeBuildCreateFleetRequest,
    ) -> CodeBuildCreateFleetResponse:
        client = self._require_client()
        return await self._execute(client.create_fleet, request, CodeBuildCreateFleetResponse)

    async def create_project(
        self,
        request: CodeBuildCreateProjectRequest,
    ) -> CodeBuildCreateProjectResponse:
        client = self._require_client()
        return await self._execute(client.create_project, request, CodeBuildCreateProjectResponse)

    async def create_report_group(
        self,
        request: CodeBuildCreateReportGroupRequest,
    ) -> CodeBuildCreateReportGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_report_group, request, CodeBuildCreateReportGroupResponse)

    async def create_webhook(
        self,
        request: CodeBuildCreateWebhookRequest,
    ) -> CodeBuildCreateWebhookResponse:
        client = self._require_client()
        return await self._execute(client.create_webhook, request, CodeBuildCreateWebhookResponse)

    async def delete_build_batch(
        self,
        request: CodeBuildDeleteBuildBatchRequest,
    ) -> CodeBuildDeleteBuildBatchResponse:
        client = self._require_client()
        return await self._execute(client.delete_build_batch, request, CodeBuildDeleteBuildBatchResponse)

    async def delete_fleet(
        self,
        request: CodeBuildDeleteFleetRequest,
    ) -> CodeBuildDeleteFleetResponse:
        client = self._require_client()
        return await self._execute(client.delete_fleet, request, CodeBuildDeleteFleetResponse)

    async def delete_project(
        self,
        request: CodeBuildDeleteProjectRequest,
    ) -> CodeBuildDeleteProjectResponse:
        client = self._require_client()
        return await self._execute(client.delete_project, request, CodeBuildDeleteProjectResponse)

    async def delete_report(
        self,
        request: CodeBuildDeleteReportRequest,
    ) -> CodeBuildDeleteReportResponse:
        client = self._require_client()
        return await self._execute(client.delete_report, request, CodeBuildDeleteReportResponse)

    async def delete_report_group(
        self,
        request: CodeBuildDeleteReportGroupRequest,
    ) -> CodeBuildDeleteReportGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_report_group, request, CodeBuildDeleteReportGroupResponse)

    async def delete_resource_policy(
        self,
        request: CodeBuildDeleteResourcePolicyRequest,
    ) -> CodeBuildDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, CodeBuildDeleteResourcePolicyResponse)

    async def delete_source_credentials(
        self,
        request: CodeBuildDeleteSourceCredentialsRequest,
    ) -> CodeBuildDeleteSourceCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.delete_source_credentials, request, CodeBuildDeleteSourceCredentialsResponse)

    async def delete_webhook(
        self,
        request: CodeBuildDeleteWebhookRequest,
    ) -> CodeBuildDeleteWebhookResponse:
        client = self._require_client()
        return await self._execute(client.delete_webhook, request, CodeBuildDeleteWebhookResponse)

    async def describe_code_coverages(
        self,
        request: CodeBuildDescribeCodeCoveragesRequest,
    ) -> CodeBuildDescribeCodeCoveragesResponse:
        client = self._require_client()
        return await self._execute(client.describe_code_coverages, request, CodeBuildDescribeCodeCoveragesResponse)

    async def describe_code_coverages_paginated(
        self,
        request: CodeBuildDescribeCodeCoveragesRequest,
    ) -> list[CodeBuildDescribeCodeCoveragesResponse]:
        return await self._paginate('describe_code_coverages', request, CodeBuildDescribeCodeCoveragesResponse)

    async def describe_test_cases(
        self,
        request: CodeBuildDescribeTestCasesRequest,
    ) -> CodeBuildDescribeTestCasesResponse:
        client = self._require_client()
        return await self._execute(client.describe_test_cases, request, CodeBuildDescribeTestCasesResponse)

    async def describe_test_cases_paginated(
        self,
        request: CodeBuildDescribeTestCasesRequest,
    ) -> list[CodeBuildDescribeTestCasesResponse]:
        return await self._paginate('describe_test_cases', request, CodeBuildDescribeTestCasesResponse)

    async def get_report_group_trend(
        self,
        request: CodeBuildGetReportGroupTrendRequest,
    ) -> CodeBuildGetReportGroupTrendResponse:
        client = self._require_client()
        return await self._execute(client.get_report_group_trend, request, CodeBuildGetReportGroupTrendResponse)

    async def get_resource_policy(
        self,
        request: CodeBuildGetResourcePolicyRequest,
    ) -> CodeBuildGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, CodeBuildGetResourcePolicyResponse)

    async def import_source_credentials(
        self,
        request: CodeBuildImportSourceCredentialsRequest,
    ) -> CodeBuildImportSourceCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.import_source_credentials, request, CodeBuildImportSourceCredentialsResponse)

    async def invalidate_project_cache(
        self,
        request: CodeBuildInvalidateProjectCacheRequest,
    ) -> CodeBuildInvalidateProjectCacheResponse:
        client = self._require_client()
        return await self._execute(client.invalidate_project_cache, request, CodeBuildInvalidateProjectCacheResponse)

    async def list_build_batches(
        self,
        request: CodeBuildListBuildBatchesRequest | None = None,
    ) -> CodeBuildListBuildBatchesResponse:
        client = self._require_client()
        return await self._execute(client.list_build_batches, request, CodeBuildListBuildBatchesResponse)

    async def list_build_batches_paginated(
        self,
        request: CodeBuildListBuildBatchesRequest | None = None,
    ) -> list[CodeBuildListBuildBatchesResponse]:
        return await self._paginate('list_build_batches', request, CodeBuildListBuildBatchesResponse)

    async def list_build_batches_for_project(
        self,
        request: CodeBuildListBuildBatchesForProjectRequest | None = None,
    ) -> CodeBuildListBuildBatchesForProjectResponse:
        client = self._require_client()
        return await self._execute(client.list_build_batches_for_project, request, CodeBuildListBuildBatchesForProjectResponse)

    async def list_build_batches_for_project_paginated(
        self,
        request: CodeBuildListBuildBatchesForProjectRequest | None = None,
    ) -> list[CodeBuildListBuildBatchesForProjectResponse]:
        return await self._paginate('list_build_batches_for_project', request, CodeBuildListBuildBatchesForProjectResponse)

    async def list_builds(
        self,
        request: CodeBuildListBuildsRequest | None = None,
    ) -> CodeBuildListBuildsResponse:
        client = self._require_client()
        return await self._execute(client.list_builds, request, CodeBuildListBuildsResponse)

    async def list_builds_paginated(
        self,
        request: CodeBuildListBuildsRequest | None = None,
    ) -> list[CodeBuildListBuildsResponse]:
        return await self._paginate('list_builds', request, CodeBuildListBuildsResponse)

    async def list_builds_for_project(
        self,
        request: CodeBuildListBuildsForProjectRequest,
    ) -> CodeBuildListBuildsForProjectResponse:
        client = self._require_client()
        return await self._execute(client.list_builds_for_project, request, CodeBuildListBuildsForProjectResponse)

    async def list_builds_for_project_paginated(
        self,
        request: CodeBuildListBuildsForProjectRequest,
    ) -> list[CodeBuildListBuildsForProjectResponse]:
        return await self._paginate('list_builds_for_project', request, CodeBuildListBuildsForProjectResponse)

    async def list_command_executions_for_sandbox(
        self,
        request: CodeBuildListCommandExecutionsForSandboxRequest,
    ) -> CodeBuildListCommandExecutionsForSandboxResponse:
        client = self._require_client()
        return await self._execute(client.list_command_executions_for_sandbox, request, CodeBuildListCommandExecutionsForSandboxResponse)

    async def list_command_executions_for_sandbox_paginated(
        self,
        request: CodeBuildListCommandExecutionsForSandboxRequest,
    ) -> list[CodeBuildListCommandExecutionsForSandboxResponse]:
        return await self._paginate('list_command_executions_for_sandbox', request, CodeBuildListCommandExecutionsForSandboxResponse)

    async def list_curated_environment_images(
        self,
        request: CodeBuildListCuratedEnvironmentImagesRequest | None = None,
    ) -> CodeBuildListCuratedEnvironmentImagesResponse:
        client = self._require_client()
        return await self._execute(client.list_curated_environment_images, request, CodeBuildListCuratedEnvironmentImagesResponse)

    async def list_fleets(
        self,
        request: CodeBuildListFleetsRequest | None = None,
    ) -> CodeBuildListFleetsResponse:
        client = self._require_client()
        return await self._execute(client.list_fleets, request, CodeBuildListFleetsResponse)

    async def list_projects(
        self,
        request: CodeBuildListProjectsRequest | None = None,
    ) -> CodeBuildListProjectsResponse:
        client = self._require_client()
        return await self._execute(client.list_projects, request, CodeBuildListProjectsResponse)

    async def list_projects_paginated(
        self,
        request: CodeBuildListProjectsRequest | None = None,
    ) -> list[CodeBuildListProjectsResponse]:
        return await self._paginate('list_projects', request, CodeBuildListProjectsResponse)

    async def list_report_groups(
        self,
        request: CodeBuildListReportGroupsRequest | None = None,
    ) -> CodeBuildListReportGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_report_groups, request, CodeBuildListReportGroupsResponse)

    async def list_report_groups_paginated(
        self,
        request: CodeBuildListReportGroupsRequest | None = None,
    ) -> list[CodeBuildListReportGroupsResponse]:
        return await self._paginate('list_report_groups', request, CodeBuildListReportGroupsResponse)

    async def list_reports(
        self,
        request: CodeBuildListReportsRequest | None = None,
    ) -> CodeBuildListReportsResponse:
        client = self._require_client()
        return await self._execute(client.list_reports, request, CodeBuildListReportsResponse)

    async def list_reports_paginated(
        self,
        request: CodeBuildListReportsRequest | None = None,
    ) -> list[CodeBuildListReportsResponse]:
        return await self._paginate('list_reports', request, CodeBuildListReportsResponse)

    async def list_reports_for_report_group(
        self,
        request: CodeBuildListReportsForReportGroupRequest,
    ) -> CodeBuildListReportsForReportGroupResponse:
        client = self._require_client()
        return await self._execute(client.list_reports_for_report_group, request, CodeBuildListReportsForReportGroupResponse)

    async def list_reports_for_report_group_paginated(
        self,
        request: CodeBuildListReportsForReportGroupRequest,
    ) -> list[CodeBuildListReportsForReportGroupResponse]:
        return await self._paginate('list_reports_for_report_group', request, CodeBuildListReportsForReportGroupResponse)

    async def list_sandboxes(
        self,
        request: CodeBuildListSandboxesRequest | None = None,
    ) -> CodeBuildListSandboxesResponse:
        client = self._require_client()
        return await self._execute(client.list_sandboxes, request, CodeBuildListSandboxesResponse)

    async def list_sandboxes_paginated(
        self,
        request: CodeBuildListSandboxesRequest | None = None,
    ) -> list[CodeBuildListSandboxesResponse]:
        return await self._paginate('list_sandboxes', request, CodeBuildListSandboxesResponse)

    async def list_sandboxes_for_project(
        self,
        request: CodeBuildListSandboxesForProjectRequest,
    ) -> CodeBuildListSandboxesForProjectResponse:
        client = self._require_client()
        return await self._execute(client.list_sandboxes_for_project, request, CodeBuildListSandboxesForProjectResponse)

    async def list_sandboxes_for_project_paginated(
        self,
        request: CodeBuildListSandboxesForProjectRequest,
    ) -> list[CodeBuildListSandboxesForProjectResponse]:
        return await self._paginate('list_sandboxes_for_project', request, CodeBuildListSandboxesForProjectResponse)

    async def list_shared_projects(
        self,
        request: CodeBuildListSharedProjectsRequest | None = None,
    ) -> CodeBuildListSharedProjectsResponse:
        client = self._require_client()
        return await self._execute(client.list_shared_projects, request, CodeBuildListSharedProjectsResponse)

    async def list_shared_projects_paginated(
        self,
        request: CodeBuildListSharedProjectsRequest | None = None,
    ) -> list[CodeBuildListSharedProjectsResponse]:
        return await self._paginate('list_shared_projects', request, CodeBuildListSharedProjectsResponse)

    async def list_shared_report_groups(
        self,
        request: CodeBuildListSharedReportGroupsRequest | None = None,
    ) -> CodeBuildListSharedReportGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_shared_report_groups, request, CodeBuildListSharedReportGroupsResponse)

    async def list_shared_report_groups_paginated(
        self,
        request: CodeBuildListSharedReportGroupsRequest | None = None,
    ) -> list[CodeBuildListSharedReportGroupsResponse]:
        return await self._paginate('list_shared_report_groups', request, CodeBuildListSharedReportGroupsResponse)

    async def list_source_credentials(
        self,
        request: CodeBuildListSourceCredentialsRequest | None = None,
    ) -> CodeBuildListSourceCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.list_source_credentials, request, CodeBuildListSourceCredentialsResponse)

    async def put_resource_policy(
        self,
        request: CodeBuildPutResourcePolicyRequest,
    ) -> CodeBuildPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, CodeBuildPutResourcePolicyResponse)

    async def retry_build(
        self,
        request: CodeBuildRetryBuildRequest | None = None,
    ) -> CodeBuildRetryBuildResponse:
        client = self._require_client()
        return await self._execute(client.retry_build, request, CodeBuildRetryBuildResponse)

    async def retry_build_batch(
        self,
        request: CodeBuildRetryBuildBatchRequest | None = None,
    ) -> CodeBuildRetryBuildBatchResponse:
        client = self._require_client()
        return await self._execute(client.retry_build_batch, request, CodeBuildRetryBuildBatchResponse)

    async def start_build(
        self,
        request: CodeBuildStartBuildRequest,
    ) -> CodeBuildStartBuildResponse:
        client = self._require_client()
        return await self._execute(client.start_build, request, CodeBuildStartBuildResponse)

    async def start_build_batch(
        self,
        request: CodeBuildStartBuildBatchRequest,
    ) -> CodeBuildStartBuildBatchResponse:
        client = self._require_client()
        return await self._execute(client.start_build_batch, request, CodeBuildStartBuildBatchResponse)

    async def start_command_execution(
        self,
        request: CodeBuildStartCommandExecutionRequest,
    ) -> CodeBuildStartCommandExecutionResponse:
        client = self._require_client()
        return await self._execute(client.start_command_execution, request, CodeBuildStartCommandExecutionResponse)

    async def start_sandbox(
        self,
        request: CodeBuildStartSandboxRequest | None = None,
    ) -> CodeBuildStartSandboxResponse:
        client = self._require_client()
        return await self._execute(client.start_sandbox, request, CodeBuildStartSandboxResponse)

    async def start_sandbox_connection(
        self,
        request: CodeBuildStartSandboxConnectionRequest,
    ) -> CodeBuildStartSandboxConnectionResponse:
        client = self._require_client()
        return await self._execute(client.start_sandbox_connection, request, CodeBuildStartSandboxConnectionResponse)

    async def stop_build(
        self,
        request: CodeBuildStopBuildRequest,
    ) -> CodeBuildStopBuildResponse:
        client = self._require_client()
        return await self._execute(client.stop_build, request, CodeBuildStopBuildResponse)

    async def stop_build_batch(
        self,
        request: CodeBuildStopBuildBatchRequest,
    ) -> CodeBuildStopBuildBatchResponse:
        client = self._require_client()
        return await self._execute(client.stop_build_batch, request, CodeBuildStopBuildBatchResponse)

    async def stop_sandbox(
        self,
        request: CodeBuildStopSandboxRequest,
    ) -> CodeBuildStopSandboxResponse:
        client = self._require_client()
        return await self._execute(client.stop_sandbox, request, CodeBuildStopSandboxResponse)

    async def update_fleet(
        self,
        request: CodeBuildUpdateFleetRequest,
    ) -> CodeBuildUpdateFleetResponse:
        client = self._require_client()
        return await self._execute(client.update_fleet, request, CodeBuildUpdateFleetResponse)

    async def update_project(
        self,
        request: CodeBuildUpdateProjectRequest,
    ) -> CodeBuildUpdateProjectResponse:
        client = self._require_client()
        return await self._execute(client.update_project, request, CodeBuildUpdateProjectResponse)

    async def update_project_visibility(
        self,
        request: CodeBuildUpdateProjectVisibilityRequest,
    ) -> CodeBuildUpdateProjectVisibilityResponse:
        client = self._require_client()
        return await self._execute(client.update_project_visibility, request, CodeBuildUpdateProjectVisibilityResponse)

    async def update_report_group(
        self,
        request: CodeBuildUpdateReportGroupRequest,
    ) -> CodeBuildUpdateReportGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_report_group, request, CodeBuildUpdateReportGroupResponse)

    async def update_webhook(
        self,
        request: CodeBuildUpdateWebhookRequest,
    ) -> CodeBuildUpdateWebhookResponse:
        client = self._require_client()
        return await self._execute(client.update_webhook, request, CodeBuildUpdateWebhookResponse)
