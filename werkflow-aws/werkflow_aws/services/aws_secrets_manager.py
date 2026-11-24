from werkflow_aws.models.secrets_manager import (
    AWSSecretsManagerCreateSecretRequest,
    AWSSecretsManagerCreateSecretResponse,
    AWSSecretsManagerDeleteSecretRequest,
    AWSSecretsManagerDeleteSecretResponse,
    AWSSecretsManagerDescribeSecretRequest,
    AWSSecretsManagerDescribeSecretResponse,
    AWSSecretsManagerEmptyResponse,
    AWSSecretsManagerGetSecretValueRequest,
    AWSSecretsManagerGetSecretValueResponse,
    AWSSecretsManagerListSecretsRequest,
    AWSSecretsManagerListSecretsResponse,
    AWSSecretsManagerPutSecretValueRequest,
    AWSSecretsManagerPutSecretValueResponse,
    AWSSecretsManagerRestoreSecretRequest,
    AWSSecretsManagerRestoreSecretResponse,
    AWSSecretsManagerRotateSecretRequest,
    AWSSecretsManagerRotateSecretResponse,
    AWSSecretsManagerTagResourceRequest,
    AWSSecretsManagerUntagResourceRequest,
    AWSSecretsManagerUpdateSecretRequest,
    AWSSecretsManagerUpdateSecretResponse,
)
from werkflow_aws.types import SecretsManagerClient
from .base import AWSBaseService
from werkflow_aws.models.secrets_manager import (
    AWSSecretsManagerAssociateCrossAccountReplicaRequest,
    AWSSecretsManagerAssociateCrossAccountReplicaResponse,
    AWSSecretsManagerBatchGetSecretValueRequest,
    AWSSecretsManagerBatchGetSecretValueResponse,
    AWSSecretsManagerCancelRotateSecretRequest,
    AWSSecretsManagerCancelRotateSecretResponse,
    AWSSecretsManagerDeleteResourcePolicyRequest,
    AWSSecretsManagerDeleteResourcePolicyResponse,
    AWSSecretsManagerDisassociateCrossAccountReplicaRequest,
    AWSSecretsManagerDisassociateCrossAccountReplicaResponse,
    AWSSecretsManagerGetRandomPasswordRequest,
    AWSSecretsManagerGetRandomPasswordResponse,
    AWSSecretsManagerGetResourcePolicyRequest,
    AWSSecretsManagerGetResourcePolicyResponse,
    AWSSecretsManagerListResourcePoliciesRequest,
    AWSSecretsManagerListResourcePoliciesResponse,
    AWSSecretsManagerListSecretVersionIdsRequest,
    AWSSecretsManagerListSecretVersionIdsResponse,
    AWSSecretsManagerPutResourcePolicyRequest,
    AWSSecretsManagerPutResourcePolicyResponse,
    AWSSecretsManagerRemoveRegionsFromReplicationRequest,
    AWSSecretsManagerRemoveRegionsFromReplicationResponse,
    AWSSecretsManagerReplicateSecretToRegionsRequest,
    AWSSecretsManagerReplicateSecretToRegionsResponse,
    AWSSecretsManagerStopReplicationToReplicaRequest,
    AWSSecretsManagerStopReplicationToReplicaResponse,
    AWSSecretsManagerUpdateSecretVersionStageRequest,
    AWSSecretsManagerUpdateSecretVersionStageResponse,
    AWSSecretsManagerValidateResourcePolicyRequest,
    AWSSecretsManagerValidateResourcePolicyResponse,
)


class AWSSecretsManager(AWSBaseService[SecretsManagerClient]):
    service_name = 'SecretsManager'
    boto3_service_name = 'secretsmanager'

    def __init__(self) -> None:
        super().__init__(
            service_name='SecretsManager',
            boto3_service_name='secretsmanager',
        )

    async def get_secret_value(
        self,
        request: AWSSecretsManagerGetSecretValueRequest,
    ) -> AWSSecretsManagerGetSecretValueResponse:
        client = self._require_client()
        return await self._execute(
            client.get_secret_value,
            request,
            AWSSecretsManagerGetSecretValueResponse,
        )

    async def create_secret(
        self,
        request: AWSSecretsManagerCreateSecretRequest,
    ) -> AWSSecretsManagerCreateSecretResponse:
        client = self._require_client()
        return await self._execute(
            client.create_secret,
            request,
            AWSSecretsManagerCreateSecretResponse,
        )

    async def put_secret_value(
        self,
        request: AWSSecretsManagerPutSecretValueRequest,
    ) -> AWSSecretsManagerPutSecretValueResponse:
        client = self._require_client()
        return await self._execute(
            client.put_secret_value,
            request,
            AWSSecretsManagerPutSecretValueResponse,
        )

    async def update_secret(
        self,
        request: AWSSecretsManagerUpdateSecretRequest,
    ) -> AWSSecretsManagerUpdateSecretResponse:
        client = self._require_client()
        return await self._execute(
            client.update_secret,
            request,
            AWSSecretsManagerUpdateSecretResponse,
        )

    async def delete_secret(
        self,
        request: AWSSecretsManagerDeleteSecretRequest,
    ) -> AWSSecretsManagerDeleteSecretResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_secret,
            request,
            AWSSecretsManagerDeleteSecretResponse,
        )

    async def restore_secret(
        self,
        request: AWSSecretsManagerRestoreSecretRequest,
    ) -> AWSSecretsManagerRestoreSecretResponse:
        client = self._require_client()
        return await self._execute(
            client.restore_secret,
            request,
            AWSSecretsManagerRestoreSecretResponse,
        )

    async def describe_secret(
        self,
        request: AWSSecretsManagerDescribeSecretRequest,
    ) -> AWSSecretsManagerDescribeSecretResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_secret,
            request,
            AWSSecretsManagerDescribeSecretResponse,
        )

    async def list_secrets(
        self,
        request: AWSSecretsManagerListSecretsRequest | None = None,
    ) -> AWSSecretsManagerListSecretsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_secrets,
            request or AWSSecretsManagerListSecretsRequest(),
            AWSSecretsManagerListSecretsResponse,
        )

    async def list_secrets_paginated(
        self,
        request: AWSSecretsManagerListSecretsRequest | None = None,
    ) -> list[AWSSecretsManagerListSecretsResponse]:
        return await self._paginate(
            'list_secrets',
            request or AWSSecretsManagerListSecretsRequest(),
            AWSSecretsManagerListSecretsResponse,
        )

    async def rotate_secret(
        self,
        request: AWSSecretsManagerRotateSecretRequest,
    ) -> AWSSecretsManagerRotateSecretResponse:
        client = self._require_client()
        return await self._execute(
            client.rotate_secret,
            request,
            AWSSecretsManagerRotateSecretResponse,
        )

    async def tag_resource(
        self,
        request: AWSSecretsManagerTagResourceRequest,
    ) -> AWSSecretsManagerEmptyResponse:
        client = self._require_client()
        return await self._execute(
            client.tag_resource,
            request,
            AWSSecretsManagerEmptyResponse,
        )

    async def untag_resource(
        self,
        request: AWSSecretsManagerUntagResourceRequest,
    ) -> AWSSecretsManagerEmptyResponse:
        client = self._require_client()
        return await self._execute(
            client.untag_resource,
            request,
            AWSSecretsManagerEmptyResponse,
        )

    async def associate_cross_account_replica(
        self,
        request: AWSSecretsManagerAssociateCrossAccountReplicaRequest,
    ) -> AWSSecretsManagerAssociateCrossAccountReplicaResponse:
        client = self._require_client()
        return await self._execute(client.associate_cross_account_replica, request, AWSSecretsManagerAssociateCrossAccountReplicaResponse)

    async def batch_get_secret_value(
        self,
        request: AWSSecretsManagerBatchGetSecretValueRequest | None = None,
    ) -> AWSSecretsManagerBatchGetSecretValueResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_secret_value, request, AWSSecretsManagerBatchGetSecretValueResponse)

    async def cancel_rotate_secret(
        self,
        request: AWSSecretsManagerCancelRotateSecretRequest,
    ) -> AWSSecretsManagerCancelRotateSecretResponse:
        client = self._require_client()
        return await self._execute(client.cancel_rotate_secret, request, AWSSecretsManagerCancelRotateSecretResponse)

    async def delete_resource_policy(
        self,
        request: AWSSecretsManagerDeleteResourcePolicyRequest,
    ) -> AWSSecretsManagerDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, AWSSecretsManagerDeleteResourcePolicyResponse)

    async def disassociate_cross_account_replica(
        self,
        request: AWSSecretsManagerDisassociateCrossAccountReplicaRequest,
    ) -> AWSSecretsManagerDisassociateCrossAccountReplicaResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_cross_account_replica, request, AWSSecretsManagerDisassociateCrossAccountReplicaResponse)

    async def get_random_password(
        self,
        request: AWSSecretsManagerGetRandomPasswordRequest | None = None,
    ) -> AWSSecretsManagerGetRandomPasswordResponse:
        client = self._require_client()
        return await self._execute(client.get_random_password, request, AWSSecretsManagerGetRandomPasswordResponse)

    async def get_resource_policy(
        self,
        request: AWSSecretsManagerGetResourcePolicyRequest,
    ) -> AWSSecretsManagerGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, AWSSecretsManagerGetResourcePolicyResponse)

    async def list_resource_policies(
        self,
        request: AWSSecretsManagerListResourcePoliciesRequest,
    ) -> AWSSecretsManagerListResourcePoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_policies, request, AWSSecretsManagerListResourcePoliciesResponse)

    async def list_resource_policies_paginated(
        self,
        request: AWSSecretsManagerListResourcePoliciesRequest,
    ) -> list[AWSSecretsManagerListResourcePoliciesResponse]:
        return await self._paginate('list_resource_policies', request, AWSSecretsManagerListResourcePoliciesResponse)

    async def list_secret_version_ids(
        self,
        request: AWSSecretsManagerListSecretVersionIdsRequest,
    ) -> AWSSecretsManagerListSecretVersionIdsResponse:
        client = self._require_client()
        return await self._execute(client.list_secret_version_ids, request, AWSSecretsManagerListSecretVersionIdsResponse)

    async def put_resource_policy(
        self,
        request: AWSSecretsManagerPutResourcePolicyRequest,
    ) -> AWSSecretsManagerPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, AWSSecretsManagerPutResourcePolicyResponse)

    async def remove_regions_from_replication(
        self,
        request: AWSSecretsManagerRemoveRegionsFromReplicationRequest,
    ) -> AWSSecretsManagerRemoveRegionsFromReplicationResponse:
        client = self._require_client()
        return await self._execute(client.remove_regions_from_replication, request, AWSSecretsManagerRemoveRegionsFromReplicationResponse)

    async def replicate_secret_to_regions(
        self,
        request: AWSSecretsManagerReplicateSecretToRegionsRequest,
    ) -> AWSSecretsManagerReplicateSecretToRegionsResponse:
        client = self._require_client()
        return await self._execute(client.replicate_secret_to_regions, request, AWSSecretsManagerReplicateSecretToRegionsResponse)

    async def stop_replication_to_replica(
        self,
        request: AWSSecretsManagerStopReplicationToReplicaRequest,
    ) -> AWSSecretsManagerStopReplicationToReplicaResponse:
        client = self._require_client()
        return await self._execute(client.stop_replication_to_replica, request, AWSSecretsManagerStopReplicationToReplicaResponse)

    async def update_secret_version_stage(
        self,
        request: AWSSecretsManagerUpdateSecretVersionStageRequest,
    ) -> AWSSecretsManagerUpdateSecretVersionStageResponse:
        client = self._require_client()
        return await self._execute(client.update_secret_version_stage, request, AWSSecretsManagerUpdateSecretVersionStageResponse)

    async def validate_resource_policy(
        self,
        request: AWSSecretsManagerValidateResourcePolicyRequest,
    ) -> AWSSecretsManagerValidateResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.validate_resource_policy, request, AWSSecretsManagerValidateResourcePolicyResponse)

