from werkflow_aws.models.amplify import (
    AmplifyCreateAppRequest,
    AmplifyCreateAppResponse,
    AmplifyCreateBackendEnvironmentRequest,
    AmplifyCreateBackendEnvironmentResponse,
    AmplifyCreateBranchRequest,
    AmplifyCreateBranchResponse,
    AmplifyCreateDeploymentRequest,
    AmplifyCreateDeploymentResponse,
    AmplifyCreateDomainAssociationRequest,
    AmplifyCreateDomainAssociationResponse,
    AmplifyCreateWebhookRequest,
    AmplifyCreateWebhookResponse,
    AmplifyDeleteAppRequest,
    AmplifyDeleteAppResponse,
    AmplifyDeleteBackendEnvironmentRequest,
    AmplifyDeleteBackendEnvironmentResponse,
    AmplifyDeleteBranchRequest,
    AmplifyDeleteBranchResponse,
    AmplifyDeleteDomainAssociationRequest,
    AmplifyDeleteDomainAssociationResponse,
    AmplifyDeleteJobRequest,
    AmplifyDeleteJobResponse,
    AmplifyDeleteWebhookRequest,
    AmplifyDeleteWebhookResponse,
    AmplifyGenerateAccessLogsRequest,
    AmplifyGenerateAccessLogsResponse,
    AmplifyGetAppRequest,
    AmplifyGetAppResponse,
    AmplifyGetArtifactUrlRequest,
    AmplifyGetArtifactUrlResponse,
    AmplifyGetBackendEnvironmentRequest,
    AmplifyGetBackendEnvironmentResponse,
    AmplifyGetBranchRequest,
    AmplifyGetBranchResponse,
    AmplifyGetDomainAssociationRequest,
    AmplifyGetDomainAssociationResponse,
    AmplifyGetJobRequest,
    AmplifyGetJobResponse,
    AmplifyGetWebhookRequest,
    AmplifyGetWebhookResponse,
    AmplifyListAppsRequest,
    AmplifyListAppsResponse,
    AmplifyListArtifactsRequest,
    AmplifyListArtifactsResponse,
    AmplifyListBackendEnvironmentsRequest,
    AmplifyListBackendEnvironmentsResponse,
    AmplifyListBranchesRequest,
    AmplifyListBranchesResponse,
    AmplifyListDomainAssociationsRequest,
    AmplifyListDomainAssociationsResponse,
    AmplifyListJobsRequest,
    AmplifyListJobsResponse,
    AmplifyListTagsForResourceRequest,
    AmplifyListTagsForResourceResponse,
    AmplifyListWebhooksRequest,
    AmplifyListWebhooksResponse,
    AmplifyStartDeploymentRequest,
    AmplifyStartDeploymentResponse,
    AmplifyStartJobRequest,
    AmplifyStartJobResponse,
    AmplifyStopJobRequest,
    AmplifyStopJobResponse,
    AmplifyTagResourceRequest,
    AmplifyTagResourceResponse,
    AmplifyUntagResourceRequest,
    AmplifyUntagResourceResponse,
    AmplifyUpdateAppRequest,
    AmplifyUpdateAppResponse,
    AmplifyUpdateBranchRequest,
    AmplifyUpdateBranchResponse,
    AmplifyUpdateDomainAssociationRequest,
    AmplifyUpdateDomainAssociationResponse,
    AmplifyUpdateWebhookRequest,
    AmplifyUpdateWebhookResponse,
)
from werkflow_aws.types.amplify_client import AmplifyClient
from .base import AWSBaseService


class AWSAmplify(AWSBaseService[AmplifyClient]):
    service_name = 'amplify'
    boto3_service_name = 'amplify'

    def __init__(self) -> None:
        super().__init__(service_name='amplify', boto3_service_name='amplify')

    async def create_app(
        self,
        request: AmplifyCreateAppRequest,
    ) -> AmplifyCreateAppResponse:
        client = self._require_client()
        return await self._execute(client.create_app, request, AmplifyCreateAppResponse)

    async def create_backend_environment(
        self,
        request: AmplifyCreateBackendEnvironmentRequest,
    ) -> AmplifyCreateBackendEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.create_backend_environment, request, AmplifyCreateBackendEnvironmentResponse)

    async def create_branch(
        self,
        request: AmplifyCreateBranchRequest,
    ) -> AmplifyCreateBranchResponse:
        client = self._require_client()
        return await self._execute(client.create_branch, request, AmplifyCreateBranchResponse)

    async def create_deployment(
        self,
        request: AmplifyCreateDeploymentRequest,
    ) -> AmplifyCreateDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.create_deployment, request, AmplifyCreateDeploymentResponse)

    async def create_domain_association(
        self,
        request: AmplifyCreateDomainAssociationRequest,
    ) -> AmplifyCreateDomainAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_domain_association, request, AmplifyCreateDomainAssociationResponse)

    async def create_webhook(
        self,
        request: AmplifyCreateWebhookRequest,
    ) -> AmplifyCreateWebhookResponse:
        client = self._require_client()
        return await self._execute(client.create_webhook, request, AmplifyCreateWebhookResponse)

    async def delete_app(
        self,
        request: AmplifyDeleteAppRequest,
    ) -> AmplifyDeleteAppResponse:
        client = self._require_client()
        return await self._execute(client.delete_app, request, AmplifyDeleteAppResponse)

    async def delete_backend_environment(
        self,
        request: AmplifyDeleteBackendEnvironmentRequest,
    ) -> AmplifyDeleteBackendEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_backend_environment, request, AmplifyDeleteBackendEnvironmentResponse)

    async def delete_branch(
        self,
        request: AmplifyDeleteBranchRequest,
    ) -> AmplifyDeleteBranchResponse:
        client = self._require_client()
        return await self._execute(client.delete_branch, request, AmplifyDeleteBranchResponse)

    async def delete_domain_association(
        self,
        request: AmplifyDeleteDomainAssociationRequest,
    ) -> AmplifyDeleteDomainAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain_association, request, AmplifyDeleteDomainAssociationResponse)

    async def delete_job(
        self,
        request: AmplifyDeleteJobRequest,
    ) -> AmplifyDeleteJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_job, request, AmplifyDeleteJobResponse)

    async def delete_webhook(
        self,
        request: AmplifyDeleteWebhookRequest,
    ) -> AmplifyDeleteWebhookResponse:
        client = self._require_client()
        return await self._execute(client.delete_webhook, request, AmplifyDeleteWebhookResponse)

    async def generate_access_logs(
        self,
        request: AmplifyGenerateAccessLogsRequest,
    ) -> AmplifyGenerateAccessLogsResponse:
        client = self._require_client()
        return await self._execute(client.generate_access_logs, request, AmplifyGenerateAccessLogsResponse)

    async def get_app(
        self,
        request: AmplifyGetAppRequest,
    ) -> AmplifyGetAppResponse:
        client = self._require_client()
        return await self._execute(client.get_app, request, AmplifyGetAppResponse)

    async def get_artifact_url(
        self,
        request: AmplifyGetArtifactUrlRequest,
    ) -> AmplifyGetArtifactUrlResponse:
        client = self._require_client()
        return await self._execute(client.get_artifact_url, request, AmplifyGetArtifactUrlResponse)

    async def get_backend_environment(
        self,
        request: AmplifyGetBackendEnvironmentRequest,
    ) -> AmplifyGetBackendEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.get_backend_environment, request, AmplifyGetBackendEnvironmentResponse)

    async def get_branch(
        self,
        request: AmplifyGetBranchRequest,
    ) -> AmplifyGetBranchResponse:
        client = self._require_client()
        return await self._execute(client.get_branch, request, AmplifyGetBranchResponse)

    async def get_domain_association(
        self,
        request: AmplifyGetDomainAssociationRequest,
    ) -> AmplifyGetDomainAssociationResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_association, request, AmplifyGetDomainAssociationResponse)

    async def get_job(
        self,
        request: AmplifyGetJobRequest,
    ) -> AmplifyGetJobResponse:
        client = self._require_client()
        return await self._execute(client.get_job, request, AmplifyGetJobResponse)

    async def get_webhook(
        self,
        request: AmplifyGetWebhookRequest,
    ) -> AmplifyGetWebhookResponse:
        client = self._require_client()
        return await self._execute(client.get_webhook, request, AmplifyGetWebhookResponse)

    async def list_apps(
        self,
        request: AmplifyListAppsRequest | None = None,
    ) -> AmplifyListAppsResponse:
        client = self._require_client()
        return await self._execute(client.list_apps, request, AmplifyListAppsResponse)

    async def list_apps_paginated(
        self,
        request: AmplifyListAppsRequest | None = None,
    ) -> list[AmplifyListAppsResponse]:
        return await self._paginate('list_apps', request, AmplifyListAppsResponse)

    async def list_artifacts(
        self,
        request: AmplifyListArtifactsRequest,
    ) -> AmplifyListArtifactsResponse:
        client = self._require_client()
        return await self._execute(client.list_artifacts, request, AmplifyListArtifactsResponse)

    async def list_backend_environments(
        self,
        request: AmplifyListBackendEnvironmentsRequest,
    ) -> AmplifyListBackendEnvironmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_backend_environments, request, AmplifyListBackendEnvironmentsResponse)

    async def list_branches(
        self,
        request: AmplifyListBranchesRequest,
    ) -> AmplifyListBranchesResponse:
        client = self._require_client()
        return await self._execute(client.list_branches, request, AmplifyListBranchesResponse)

    async def list_branches_paginated(
        self,
        request: AmplifyListBranchesRequest,
    ) -> list[AmplifyListBranchesResponse]:
        return await self._paginate('list_branches', request, AmplifyListBranchesResponse)

    async def list_domain_associations(
        self,
        request: AmplifyListDomainAssociationsRequest,
    ) -> AmplifyListDomainAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_domain_associations, request, AmplifyListDomainAssociationsResponse)

    async def list_domain_associations_paginated(
        self,
        request: AmplifyListDomainAssociationsRequest,
    ) -> list[AmplifyListDomainAssociationsResponse]:
        return await self._paginate('list_domain_associations', request, AmplifyListDomainAssociationsResponse)

    async def list_jobs(
        self,
        request: AmplifyListJobsRequest,
    ) -> AmplifyListJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_jobs, request, AmplifyListJobsResponse)

    async def list_jobs_paginated(
        self,
        request: AmplifyListJobsRequest,
    ) -> list[AmplifyListJobsResponse]:
        return await self._paginate('list_jobs', request, AmplifyListJobsResponse)

    async def list_tags_for_resource(
        self,
        request: AmplifyListTagsForResourceRequest,
    ) -> AmplifyListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, AmplifyListTagsForResourceResponse)

    async def list_webhooks(
        self,
        request: AmplifyListWebhooksRequest,
    ) -> AmplifyListWebhooksResponse:
        client = self._require_client()
        return await self._execute(client.list_webhooks, request, AmplifyListWebhooksResponse)

    async def start_deployment(
        self,
        request: AmplifyStartDeploymentRequest,
    ) -> AmplifyStartDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.start_deployment, request, AmplifyStartDeploymentResponse)

    async def start_job(
        self,
        request: AmplifyStartJobRequest,
    ) -> AmplifyStartJobResponse:
        client = self._require_client()
        return await self._execute(client.start_job, request, AmplifyStartJobResponse)

    async def stop_job(
        self,
        request: AmplifyStopJobRequest,
    ) -> AmplifyStopJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_job, request, AmplifyStopJobResponse)

    async def tag_resource(
        self,
        request: AmplifyTagResourceRequest,
    ) -> AmplifyTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, AmplifyTagResourceResponse)

    async def untag_resource(
        self,
        request: AmplifyUntagResourceRequest,
    ) -> AmplifyUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, AmplifyUntagResourceResponse)

    async def update_app(
        self,
        request: AmplifyUpdateAppRequest,
    ) -> AmplifyUpdateAppResponse:
        client = self._require_client()
        return await self._execute(client.update_app, request, AmplifyUpdateAppResponse)

    async def update_branch(
        self,
        request: AmplifyUpdateBranchRequest,
    ) -> AmplifyUpdateBranchResponse:
        client = self._require_client()
        return await self._execute(client.update_branch, request, AmplifyUpdateBranchResponse)

    async def update_domain_association(
        self,
        request: AmplifyUpdateDomainAssociationRequest,
    ) -> AmplifyUpdateDomainAssociationResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_association, request, AmplifyUpdateDomainAssociationResponse)

    async def update_webhook(
        self,
        request: AmplifyUpdateWebhookRequest,
    ) -> AmplifyUpdateWebhookResponse:
        client = self._require_client()
        return await self._execute(client.update_webhook, request, AmplifyUpdateWebhookResponse)
