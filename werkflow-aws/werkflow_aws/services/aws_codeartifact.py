import functools
from werkflow_aws.exceptions import EmptyResponseException
from werkflow_aws.models.codeartifact import (
    CodeArtifactCreateDomainRequest,
    CodeArtifactCreateRepositoryRequest,
    CodeArtifactDeleteDomainRequest,
    CodeArtifactDeletePackageVersionsRequest,
    CodeArtifactDeletePackageVersionsResponse,
    CodeArtifactDeleteRepositoryRequest,
    CodeArtifactDescribeDomainRequest,
    CodeArtifactDescribeRepositoryRequest,
    CodeArtifactDomainResponse,
    CodeArtifactListDomainsRequest,
    CodeArtifactListDomainsResponse,
    CodeArtifactListPackagesRequest,
    CodeArtifactListPackagesResponse,
    CodeArtifactListPackageVersionsRequest,
    CodeArtifactListPackageVersionsResponse,
    CodeArtifactListRepositoriesRequest,
    CodeArtifactListRepositoriesResponse,
    CodeArtifactRepositoryResponse,
)
from werkflow_aws.types import (
    CodeArtifactClient,
    CodeArtifactFormat,
)
from .base import AWSBaseService
from werkflow_aws.models.codeartifact import (
    CodeArtifactAssociateExternalConnectionRequest,
    CodeArtifactAssociateExternalConnectionResponse,
    CodeArtifactCopyPackageVersionsRequest,
    CodeArtifactCopyPackageVersionsResponse,
    CodeArtifactCreatePackageGroupRequest,
    CodeArtifactCreatePackageGroupResponse,
    CodeArtifactDeleteDomainPermissionsPolicyRequest,
    CodeArtifactDeleteDomainPermissionsPolicyResponse,
    CodeArtifactDeletePackageGroupRequest,
    CodeArtifactDeletePackageGroupResponse,
    CodeArtifactDeletePackageRequest,
    CodeArtifactDeletePackageResponse,
    CodeArtifactDeleteRepositoryPermissionsPolicyRequest,
    CodeArtifactDeleteRepositoryPermissionsPolicyResponse,
    CodeArtifactDescribePackageGroupRequest,
    CodeArtifactDescribePackageGroupResponse,
    CodeArtifactDescribePackageRequest,
    CodeArtifactDescribePackageResponse,
    CodeArtifactDescribePackageVersionRequest,
    CodeArtifactDescribePackageVersionResponse,
    CodeArtifactDisassociateExternalConnectionRequest,
    CodeArtifactDisassociateExternalConnectionResponse,
    CodeArtifactDisposePackageVersionsRequest,
    CodeArtifactDisposePackageVersionsResponse,
    CodeArtifactGetAssociatedPackageGroupRequest,
    CodeArtifactGetAssociatedPackageGroupResponse,
    CodeArtifactGetDomainPermissionsPolicyRequest,
    CodeArtifactGetDomainPermissionsPolicyResponse,
    CodeArtifactGetPackageVersionAssetRequest,
    CodeArtifactGetPackageVersionAssetResponse,
    CodeArtifactGetPackageVersionReadmeRequest,
    CodeArtifactGetPackageVersionReadmeResponse,
    CodeArtifactGetRepositoryPermissionsPolicyRequest,
    CodeArtifactGetRepositoryPermissionsPolicyResponse,
    CodeArtifactListAllowedRepositoriesForGroupRequest,
    CodeArtifactListAllowedRepositoriesForGroupResponse,
    CodeArtifactListAssociatedPackagesRequest,
    CodeArtifactListAssociatedPackagesResponse,
    CodeArtifactListPackageGroupsRequest,
    CodeArtifactListPackageGroupsResponse,
    CodeArtifactListPackageVersionAssetsRequest,
    CodeArtifactListPackageVersionAssetsResponse,
    CodeArtifactListPackageVersionDependenciesRequest,
    CodeArtifactListPackageVersionDependenciesResponse,
    CodeArtifactListRepositoriesInDomainRequest,
    CodeArtifactListRepositoriesInDomainResponse,
    CodeArtifactListSubPackageGroupsRequest,
    CodeArtifactListSubPackageGroupsResponse,
    CodeArtifactListTagsForResourceRequest,
    CodeArtifactListTagsForResourceResponse,
    CodeArtifactPublishPackageVersionRequest,
    CodeArtifactPublishPackageVersionResponse,
    CodeArtifactPutDomainPermissionsPolicyRequest,
    CodeArtifactPutDomainPermissionsPolicyResponse,
    CodeArtifactPutPackageOriginConfigurationRequest,
    CodeArtifactPutPackageOriginConfigurationResponse,
    CodeArtifactPutRepositoryPermissionsPolicyRequest,
    CodeArtifactPutRepositoryPermissionsPolicyResponse,
    CodeArtifactTagResourceRequest,
    CodeArtifactTagResourceResponse,
    CodeArtifactUntagResourceRequest,
    CodeArtifactUntagResourceResponse,
    CodeArtifactUpdatePackageGroupOriginConfigurationRequest,
    CodeArtifactUpdatePackageGroupOriginConfigurationResponse,
    CodeArtifactUpdatePackageGroupRequest,
    CodeArtifactUpdatePackageGroupResponse,
    CodeArtifactUpdatePackageVersionsStatusRequest,
    CodeArtifactUpdatePackageVersionsStatusResponse,
    CodeArtifactUpdateRepositoryRequest,
    CodeArtifactUpdateRepositoryResponse,
)


class AWSCodeArtifact(AWSBaseService[CodeArtifactClient]):
    service_name = 'CodeArtifact'
    boto3_service_name = 'codeartifact'

    def __init__(self) -> None:
        super().__init__(
            service_name='CodeArtifact',
            boto3_service_name='codeartifact',
        )

    async def get_authorization_token(
        self,
        domain: str,
        domain_owner: str | None = None,
        duration_seconds: int = 1000,
    ) -> str:
        client = self._require_client()
        loop = self._get_loop()

        if domain_owner is not None:
            result = await loop.run_in_executor(
                self._executor,
                functools.partial(
                    client.get_authorization_token,
                    domain=domain,
                    domainOwner=domain_owner,
                    durationSeconds=duration_seconds,
                ),
            )
        else:
            result = await loop.run_in_executor(
                self._executor,
                functools.partial(
                    client.get_authorization_token,
                    domain=domain,
                    durationSeconds=duration_seconds,
                ),
            )

        authorization_token = result.get('authorizationToken')
        if authorization_token is None:
            raise EmptyResponseException(
                self.service_name,
                'get_authorization_token',
                'authorizationToken',
            )
        return str(authorization_token)

    async def get_repository_endpoint(
        self,
        domain: str,
        domain_owner: str | None,
        repository: str,
        repository_format: CodeArtifactFormat,
    ) -> str:
        client = self._require_client()
        loop = self._get_loop()

        if domain_owner is not None:
            result = await loop.run_in_executor(
                self._executor,
                functools.partial(
                    client.get_repository_endpoint,
                    domain=domain,
                    domainOwner=domain_owner,
                    repository=repository,
                    format=repository_format,
                ),
            )
        else:
            result = await loop.run_in_executor(
                self._executor,
                functools.partial(
                    client.get_repository_endpoint,
                    domain=domain,
                    repository=repository,
                    format=repository_format,
                ),
            )

        endpoint = result.get('repositoryEndpoint')
        if endpoint is None:
            raise EmptyResponseException(
                self.service_name,
                'get_repository_endpoint',
                'repositoryEndpoint',
            )
        return str(endpoint)

    async def list_domains(
        self,
        request: CodeArtifactListDomainsRequest | None = None,
    ) -> CodeArtifactListDomainsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_domains,
            request or CodeArtifactListDomainsRequest(),
            CodeArtifactListDomainsResponse,
        )

    async def list_domains_paginated(
        self,
        request: CodeArtifactListDomainsRequest | None = None,
    ) -> list[CodeArtifactListDomainsResponse]:
        return await self._paginate(
            'list_domains',
            request or CodeArtifactListDomainsRequest(),
            CodeArtifactListDomainsResponse,
        )

    async def describe_domain(
        self,
        request: CodeArtifactDescribeDomainRequest,
    ) -> CodeArtifactDomainResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_domain,
            request,
            CodeArtifactDomainResponse,
        )

    async def create_domain(
        self,
        request: CodeArtifactCreateDomainRequest,
    ) -> CodeArtifactDomainResponse:
        client = self._require_client()
        return await self._execute(
            client.create_domain,
            request,
            CodeArtifactDomainResponse,
        )

    async def delete_domain(
        self,
        request: CodeArtifactDeleteDomainRequest,
    ) -> CodeArtifactDomainResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_domain,
            request,
            CodeArtifactDomainResponse,
        )

    async def list_repositories(
        self,
        request: CodeArtifactListRepositoriesRequest | None = None,
    ) -> CodeArtifactListRepositoriesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_repositories,
            request or CodeArtifactListRepositoriesRequest(),
            CodeArtifactListRepositoriesResponse,
        )

    async def list_repositories_paginated(
        self,
        request: CodeArtifactListRepositoriesRequest | None = None,
    ) -> list[CodeArtifactListRepositoriesResponse]:
        return await self._paginate(
            'list_repositories',
            request or CodeArtifactListRepositoriesRequest(),
            CodeArtifactListRepositoriesResponse,
        )

    async def describe_repository(
        self,
        request: CodeArtifactDescribeRepositoryRequest,
    ) -> CodeArtifactRepositoryResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_repository,
            request,
            CodeArtifactRepositoryResponse,
        )

    async def create_repository(
        self,
        request: CodeArtifactCreateRepositoryRequest,
    ) -> CodeArtifactRepositoryResponse:
        client = self._require_client()
        return await self._execute(
            client.create_repository,
            request,
            CodeArtifactRepositoryResponse,
        )

    async def delete_repository(
        self,
        request: CodeArtifactDeleteRepositoryRequest,
    ) -> CodeArtifactRepositoryResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_repository,
            request,
            CodeArtifactRepositoryResponse,
        )

    async def list_packages(
        self,
        request: CodeArtifactListPackagesRequest,
    ) -> CodeArtifactListPackagesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_packages,
            request,
            CodeArtifactListPackagesResponse,
        )

    async def list_packages_paginated(
        self,
        request: CodeArtifactListPackagesRequest,
    ) -> list[CodeArtifactListPackagesResponse]:
        return await self._paginate(
            'list_packages',
            request,
            CodeArtifactListPackagesResponse,
        )

    async def list_package_versions(
        self,
        request: CodeArtifactListPackageVersionsRequest,
    ) -> CodeArtifactListPackageVersionsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_package_versions,
            request,
            CodeArtifactListPackageVersionsResponse,
        )

    async def list_package_versions_paginated(
        self,
        request: CodeArtifactListPackageVersionsRequest,
    ) -> list[CodeArtifactListPackageVersionsResponse]:
        return await self._paginate(
            'list_package_versions',
            request,
            CodeArtifactListPackageVersionsResponse,
        )

    async def delete_package_versions(
        self,
        request: CodeArtifactDeletePackageVersionsRequest,
    ) -> CodeArtifactDeletePackageVersionsResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_package_versions,
            request,
            CodeArtifactDeletePackageVersionsResponse,
        )

    async def associate_external_connection(
        self,
        request: CodeArtifactAssociateExternalConnectionRequest,
    ) -> CodeArtifactAssociateExternalConnectionResponse:
        client = self._require_client()
        return await self._execute(client.associate_external_connection, request, CodeArtifactAssociateExternalConnectionResponse)

    async def copy_package_versions(
        self,
        request: CodeArtifactCopyPackageVersionsRequest,
    ) -> CodeArtifactCopyPackageVersionsResponse:
        client = self._require_client()
        return await self._execute(client.copy_package_versions, request, CodeArtifactCopyPackageVersionsResponse)

    async def create_package_group(
        self,
        request: CodeArtifactCreatePackageGroupRequest,
    ) -> CodeArtifactCreatePackageGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_package_group, request, CodeArtifactCreatePackageGroupResponse)

    async def delete_domain_permissions_policy(
        self,
        request: CodeArtifactDeleteDomainPermissionsPolicyRequest,
    ) -> CodeArtifactDeleteDomainPermissionsPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain_permissions_policy, request, CodeArtifactDeleteDomainPermissionsPolicyResponse)

    async def delete_package(
        self,
        request: CodeArtifactDeletePackageRequest,
    ) -> CodeArtifactDeletePackageResponse:
        client = self._require_client()
        return await self._execute(client.delete_package, request, CodeArtifactDeletePackageResponse)

    async def delete_package_group(
        self,
        request: CodeArtifactDeletePackageGroupRequest,
    ) -> CodeArtifactDeletePackageGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_package_group, request, CodeArtifactDeletePackageGroupResponse)

    async def delete_repository_permissions_policy(
        self,
        request: CodeArtifactDeleteRepositoryPermissionsPolicyRequest,
    ) -> CodeArtifactDeleteRepositoryPermissionsPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_repository_permissions_policy, request, CodeArtifactDeleteRepositoryPermissionsPolicyResponse)

    async def describe_package(
        self,
        request: CodeArtifactDescribePackageRequest,
    ) -> CodeArtifactDescribePackageResponse:
        client = self._require_client()
        return await self._execute(client.describe_package, request, CodeArtifactDescribePackageResponse)

    async def describe_package_group(
        self,
        request: CodeArtifactDescribePackageGroupRequest,
    ) -> CodeArtifactDescribePackageGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_package_group, request, CodeArtifactDescribePackageGroupResponse)

    async def describe_package_version(
        self,
        request: CodeArtifactDescribePackageVersionRequest,
    ) -> CodeArtifactDescribePackageVersionResponse:
        client = self._require_client()
        return await self._execute(client.describe_package_version, request, CodeArtifactDescribePackageVersionResponse)

    async def disassociate_external_connection(
        self,
        request: CodeArtifactDisassociateExternalConnectionRequest,
    ) -> CodeArtifactDisassociateExternalConnectionResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_external_connection, request, CodeArtifactDisassociateExternalConnectionResponse)

    async def dispose_package_versions(
        self,
        request: CodeArtifactDisposePackageVersionsRequest,
    ) -> CodeArtifactDisposePackageVersionsResponse:
        client = self._require_client()
        return await self._execute(client.dispose_package_versions, request, CodeArtifactDisposePackageVersionsResponse)

    async def get_associated_package_group(
        self,
        request: CodeArtifactGetAssociatedPackageGroupRequest,
    ) -> CodeArtifactGetAssociatedPackageGroupResponse:
        client = self._require_client()
        return await self._execute(client.get_associated_package_group, request, CodeArtifactGetAssociatedPackageGroupResponse)

    async def get_domain_permissions_policy(
        self,
        request: CodeArtifactGetDomainPermissionsPolicyRequest,
    ) -> CodeArtifactGetDomainPermissionsPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_permissions_policy, request, CodeArtifactGetDomainPermissionsPolicyResponse)

    async def get_package_version_asset(
        self,
        request: CodeArtifactGetPackageVersionAssetRequest,
    ) -> CodeArtifactGetPackageVersionAssetResponse:
        client = self._require_client()
        return await self._execute(client.get_package_version_asset, request, CodeArtifactGetPackageVersionAssetResponse)

    async def get_package_version_readme(
        self,
        request: CodeArtifactGetPackageVersionReadmeRequest,
    ) -> CodeArtifactGetPackageVersionReadmeResponse:
        client = self._require_client()
        return await self._execute(client.get_package_version_readme, request, CodeArtifactGetPackageVersionReadmeResponse)

    async def get_repository_permissions_policy(
        self,
        request: CodeArtifactGetRepositoryPermissionsPolicyRequest,
    ) -> CodeArtifactGetRepositoryPermissionsPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_repository_permissions_policy, request, CodeArtifactGetRepositoryPermissionsPolicyResponse)

    async def list_allowed_repositories_for_group(
        self,
        request: CodeArtifactListAllowedRepositoriesForGroupRequest,
    ) -> CodeArtifactListAllowedRepositoriesForGroupResponse:
        client = self._require_client()
        return await self._execute(client.list_allowed_repositories_for_group, request, CodeArtifactListAllowedRepositoriesForGroupResponse)

    async def list_allowed_repositories_for_group_paginated(
        self,
        request: CodeArtifactListAllowedRepositoriesForGroupRequest,
    ) -> list[CodeArtifactListAllowedRepositoriesForGroupResponse]:
        return await self._paginate('list_allowed_repositories_for_group', request, CodeArtifactListAllowedRepositoriesForGroupResponse)

    async def list_associated_packages(
        self,
        request: CodeArtifactListAssociatedPackagesRequest,
    ) -> CodeArtifactListAssociatedPackagesResponse:
        client = self._require_client()
        return await self._execute(client.list_associated_packages, request, CodeArtifactListAssociatedPackagesResponse)

    async def list_associated_packages_paginated(
        self,
        request: CodeArtifactListAssociatedPackagesRequest,
    ) -> list[CodeArtifactListAssociatedPackagesResponse]:
        return await self._paginate('list_associated_packages', request, CodeArtifactListAssociatedPackagesResponse)

    async def list_package_groups(
        self,
        request: CodeArtifactListPackageGroupsRequest,
    ) -> CodeArtifactListPackageGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_package_groups, request, CodeArtifactListPackageGroupsResponse)

    async def list_package_groups_paginated(
        self,
        request: CodeArtifactListPackageGroupsRequest,
    ) -> list[CodeArtifactListPackageGroupsResponse]:
        return await self._paginate('list_package_groups', request, CodeArtifactListPackageGroupsResponse)

    async def list_package_version_assets(
        self,
        request: CodeArtifactListPackageVersionAssetsRequest,
    ) -> CodeArtifactListPackageVersionAssetsResponse:
        client = self._require_client()
        return await self._execute(client.list_package_version_assets, request, CodeArtifactListPackageVersionAssetsResponse)

    async def list_package_version_assets_paginated(
        self,
        request: CodeArtifactListPackageVersionAssetsRequest,
    ) -> list[CodeArtifactListPackageVersionAssetsResponse]:
        return await self._paginate('list_package_version_assets', request, CodeArtifactListPackageVersionAssetsResponse)

    async def list_package_version_dependencies(
        self,
        request: CodeArtifactListPackageVersionDependenciesRequest,
    ) -> CodeArtifactListPackageVersionDependenciesResponse:
        client = self._require_client()
        return await self._execute(client.list_package_version_dependencies, request, CodeArtifactListPackageVersionDependenciesResponse)

    async def list_repositories_in_domain(
        self,
        request: CodeArtifactListRepositoriesInDomainRequest,
    ) -> CodeArtifactListRepositoriesInDomainResponse:
        client = self._require_client()
        return await self._execute(client.list_repositories_in_domain, request, CodeArtifactListRepositoriesInDomainResponse)

    async def list_repositories_in_domain_paginated(
        self,
        request: CodeArtifactListRepositoriesInDomainRequest,
    ) -> list[CodeArtifactListRepositoriesInDomainResponse]:
        return await self._paginate('list_repositories_in_domain', request, CodeArtifactListRepositoriesInDomainResponse)

    async def list_sub_package_groups(
        self,
        request: CodeArtifactListSubPackageGroupsRequest,
    ) -> CodeArtifactListSubPackageGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_sub_package_groups, request, CodeArtifactListSubPackageGroupsResponse)

    async def list_sub_package_groups_paginated(
        self,
        request: CodeArtifactListSubPackageGroupsRequest,
    ) -> list[CodeArtifactListSubPackageGroupsResponse]:
        return await self._paginate('list_sub_package_groups', request, CodeArtifactListSubPackageGroupsResponse)

    async def list_tags_for_resource(
        self,
        request: CodeArtifactListTagsForResourceRequest,
    ) -> CodeArtifactListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, CodeArtifactListTagsForResourceResponse)

    async def publish_package_version(
        self,
        request: CodeArtifactPublishPackageVersionRequest,
    ) -> CodeArtifactPublishPackageVersionResponse:
        client = self._require_client()
        return await self._execute(client.publish_package_version, request, CodeArtifactPublishPackageVersionResponse)

    async def put_domain_permissions_policy(
        self,
        request: CodeArtifactPutDomainPermissionsPolicyRequest,
    ) -> CodeArtifactPutDomainPermissionsPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_domain_permissions_policy, request, CodeArtifactPutDomainPermissionsPolicyResponse)

    async def put_package_origin_configuration(
        self,
        request: CodeArtifactPutPackageOriginConfigurationRequest,
    ) -> CodeArtifactPutPackageOriginConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_package_origin_configuration, request, CodeArtifactPutPackageOriginConfigurationResponse)

    async def put_repository_permissions_policy(
        self,
        request: CodeArtifactPutRepositoryPermissionsPolicyRequest,
    ) -> CodeArtifactPutRepositoryPermissionsPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_repository_permissions_policy, request, CodeArtifactPutRepositoryPermissionsPolicyResponse)

    async def tag_resource(
        self,
        request: CodeArtifactTagResourceRequest,
    ) -> CodeArtifactTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, CodeArtifactTagResourceResponse)

    async def untag_resource(
        self,
        request: CodeArtifactUntagResourceRequest,
    ) -> CodeArtifactUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, CodeArtifactUntagResourceResponse)

    async def update_package_group(
        self,
        request: CodeArtifactUpdatePackageGroupRequest,
    ) -> CodeArtifactUpdatePackageGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_package_group, request, CodeArtifactUpdatePackageGroupResponse)

    async def update_package_group_origin_configuration(
        self,
        request: CodeArtifactUpdatePackageGroupOriginConfigurationRequest,
    ) -> CodeArtifactUpdatePackageGroupOriginConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_package_group_origin_configuration, request, CodeArtifactUpdatePackageGroupOriginConfigurationResponse)

    async def update_package_versions_status(
        self,
        request: CodeArtifactUpdatePackageVersionsStatusRequest,
    ) -> CodeArtifactUpdatePackageVersionsStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_package_versions_status, request, CodeArtifactUpdatePackageVersionsStatusResponse)

    async def update_repository(
        self,
        request: CodeArtifactUpdateRepositoryRequest,
    ) -> CodeArtifactUpdateRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.update_repository, request, CodeArtifactUpdateRepositoryResponse)

