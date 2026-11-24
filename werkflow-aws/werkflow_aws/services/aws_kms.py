from werkflow_aws.models.kms import (
    KMSCancelKeyDeletionRequest,
    KMSCancelKeyDeletionResponse,
    KMSConnectCustomKeyStoreRequest,
    KMSConnectCustomKeyStoreResponse,
    KMSCreateAliasRequest,
    KMSCreateAliasResponse,
    KMSCreateCustomKeyStoreRequest,
    KMSCreateCustomKeyStoreResponse,
    KMSCreateGrantRequest,
    KMSCreateGrantResponse,
    KMSCreateKeyRequest,
    KMSCreateKeyResponse,
    KMSDecapsulateRequest,
    KMSDecapsulateResponse,
    KMSDecryptRequest,
    KMSDecryptResponse,
    KMSDeleteAliasRequest,
    KMSDeleteAliasResponse,
    KMSDeleteCustomKeyStoreRequest,
    KMSDeleteCustomKeyStoreResponse,
    KMSDeleteImportedKeyMaterialRequest,
    KMSDeleteImportedKeyMaterialResponse,
    KMSDeriveSharedSecretRequest,
    KMSDeriveSharedSecretResponse,
    KMSDescribeCustomKeyStoresRequest,
    KMSDescribeCustomKeyStoresResponse,
    KMSDescribeKeyRequest,
    KMSDescribeKeyResponse,
    KMSDisableKeyRequest,
    KMSDisableKeyResponse,
    KMSDisableKeyRotationRequest,
    KMSDisableKeyRotationResponse,
    KMSDisconnectCustomKeyStoreRequest,
    KMSDisconnectCustomKeyStoreResponse,
    KMSEnableKeyRequest,
    KMSEnableKeyResponse,
    KMSEnableKeyRotationRequest,
    KMSEnableKeyRotationResponse,
    KMSEncapsulateRequest,
    KMSEncapsulateResponse,
    KMSEncryptRequest,
    KMSEncryptResponse,
    KMSGenerateDataKeyPairRequest,
    KMSGenerateDataKeyPairResponse,
    KMSGenerateDataKeyPairWithoutPlaintextRequest,
    KMSGenerateDataKeyPairWithoutPlaintextResponse,
    KMSGenerateDataKeyRequest,
    KMSGenerateDataKeyResponse,
    KMSGenerateDataKeyWithoutPlaintextRequest,
    KMSGenerateDataKeyWithoutPlaintextResponse,
    KMSGenerateMacRequest,
    KMSGenerateMacResponse,
    KMSGenerateRandomRequest,
    KMSGenerateRandomResponse,
    KMSGetKeyLastUsageRequest,
    KMSGetKeyLastUsageResponse,
    KMSGetKeyPolicyRequest,
    KMSGetKeyPolicyResponse,
    KMSGetKeyRotationStatusRequest,
    KMSGetKeyRotationStatusResponse,
    KMSGetParametersForImportRequest,
    KMSGetParametersForImportResponse,
    KMSGetPublicKeyRequest,
    KMSGetPublicKeyResponse,
    KMSImportKeyMaterialRequest,
    KMSImportKeyMaterialResponse,
    KMSListAliasesRequest,
    KMSListAliasesResponse,
    KMSListGrantsRequest,
    KMSListGrantsResponse,
    KMSListKeyPoliciesRequest,
    KMSListKeyPoliciesResponse,
    KMSListKeyRotationsRequest,
    KMSListKeyRotationsResponse,
    KMSListKeysRequest,
    KMSListKeysResponse,
    KMSListResourceTagsRequest,
    KMSListResourceTagsResponse,
    KMSListRetirableGrantsRequest,
    KMSListRetirableGrantsResponse,
    KMSPutKeyPolicyRequest,
    KMSPutKeyPolicyResponse,
    KMSReEncryptRequest,
    KMSReEncryptResponse,
    KMSReplicateKeyRequest,
    KMSReplicateKeyResponse,
    KMSRetireGrantRequest,
    KMSRetireGrantResponse,
    KMSRevokeGrantRequest,
    KMSRevokeGrantResponse,
    KMSRotateKeyOnDemandRequest,
    KMSRotateKeyOnDemandResponse,
    KMSScheduleKeyDeletionRequest,
    KMSScheduleKeyDeletionResponse,
    KMSSignRequest,
    KMSSignResponse,
    KMSTagResourceRequest,
    KMSTagResourceResponse,
    KMSUntagResourceRequest,
    KMSUntagResourceResponse,
    KMSUpdateAliasRequest,
    KMSUpdateAliasResponse,
    KMSUpdateCustomKeyStoreRequest,
    KMSUpdateCustomKeyStoreResponse,
    KMSUpdateKeyDescriptionRequest,
    KMSUpdateKeyDescriptionResponse,
    KMSUpdatePrimaryRegionRequest,
    KMSUpdatePrimaryRegionResponse,
    KMSVerifyMacRequest,
    KMSVerifyMacResponse,
    KMSVerifyRequest,
    KMSVerifyResponse,
)
from werkflow_aws.types.kms_client import KMSClient
from .base import AWSBaseService


class AWSKMS(AWSBaseService[KMSClient]):
    service_name = 'kms'
    boto3_service_name = 'kms'

    def __init__(self) -> None:
        super().__init__(service_name='kms', boto3_service_name='kms')

    async def cancel_key_deletion(
        self,
        request: KMSCancelKeyDeletionRequest,
    ) -> KMSCancelKeyDeletionResponse:
        client = self._require_client()
        return await self._execute(client.cancel_key_deletion, request, KMSCancelKeyDeletionResponse)

    async def connect_custom_key_store(
        self,
        request: KMSConnectCustomKeyStoreRequest,
    ) -> KMSConnectCustomKeyStoreResponse:
        client = self._require_client()
        return await self._execute(client.connect_custom_key_store, request, KMSConnectCustomKeyStoreResponse)

    async def create_alias(
        self,
        request: KMSCreateAliasRequest,
    ) -> KMSCreateAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_alias, request, KMSCreateAliasResponse)

    async def create_custom_key_store(
        self,
        request: KMSCreateCustomKeyStoreRequest,
    ) -> KMSCreateCustomKeyStoreResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_key_store, request, KMSCreateCustomKeyStoreResponse)

    async def create_grant(
        self,
        request: KMSCreateGrantRequest,
    ) -> KMSCreateGrantResponse:
        client = self._require_client()
        return await self._execute(client.create_grant, request, KMSCreateGrantResponse)

    async def create_key(
        self,
        request: KMSCreateKeyRequest | None = None,
    ) -> KMSCreateKeyResponse:
        client = self._require_client()
        return await self._execute(client.create_key, request, KMSCreateKeyResponse)

    async def decapsulate(
        self,
        request: KMSDecapsulateRequest,
    ) -> KMSDecapsulateResponse:
        client = self._require_client()
        return await self._execute(client.decapsulate, request, KMSDecapsulateResponse)

    async def decrypt(
        self,
        request: KMSDecryptRequest | None = None,
    ) -> KMSDecryptResponse:
        client = self._require_client()
        return await self._execute(client.decrypt, request, KMSDecryptResponse)

    async def delete_alias(
        self,
        request: KMSDeleteAliasRequest,
    ) -> KMSDeleteAliasResponse:
        client = self._require_client()
        return await self._execute(client.delete_alias, request, KMSDeleteAliasResponse)

    async def delete_custom_key_store(
        self,
        request: KMSDeleteCustomKeyStoreRequest,
    ) -> KMSDeleteCustomKeyStoreResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_key_store, request, KMSDeleteCustomKeyStoreResponse)

    async def delete_imported_key_material(
        self,
        request: KMSDeleteImportedKeyMaterialRequest,
    ) -> KMSDeleteImportedKeyMaterialResponse:
        client = self._require_client()
        return await self._execute(client.delete_imported_key_material, request, KMSDeleteImportedKeyMaterialResponse)

    async def derive_shared_secret(
        self,
        request: KMSDeriveSharedSecretRequest,
    ) -> KMSDeriveSharedSecretResponse:
        client = self._require_client()
        return await self._execute(client.derive_shared_secret, request, KMSDeriveSharedSecretResponse)

    async def describe_custom_key_stores(
        self,
        request: KMSDescribeCustomKeyStoresRequest | None = None,
    ) -> KMSDescribeCustomKeyStoresResponse:
        client = self._require_client()
        return await self._execute(client.describe_custom_key_stores, request, KMSDescribeCustomKeyStoresResponse)

    async def describe_custom_key_stores_paginated(
        self,
        request: KMSDescribeCustomKeyStoresRequest | None = None,
    ) -> list[KMSDescribeCustomKeyStoresResponse]:
        return await self._paginate('describe_custom_key_stores', request, KMSDescribeCustomKeyStoresResponse)

    async def describe_key(
        self,
        request: KMSDescribeKeyRequest,
    ) -> KMSDescribeKeyResponse:
        client = self._require_client()
        return await self._execute(client.describe_key, request, KMSDescribeKeyResponse)

    async def disable_key(
        self,
        request: KMSDisableKeyRequest,
    ) -> KMSDisableKeyResponse:
        client = self._require_client()
        return await self._execute(client.disable_key, request, KMSDisableKeyResponse)

    async def disable_key_rotation(
        self,
        request: KMSDisableKeyRotationRequest,
    ) -> KMSDisableKeyRotationResponse:
        client = self._require_client()
        return await self._execute(client.disable_key_rotation, request, KMSDisableKeyRotationResponse)

    async def disconnect_custom_key_store(
        self,
        request: KMSDisconnectCustomKeyStoreRequest,
    ) -> KMSDisconnectCustomKeyStoreResponse:
        client = self._require_client()
        return await self._execute(client.disconnect_custom_key_store, request, KMSDisconnectCustomKeyStoreResponse)

    async def enable_key(
        self,
        request: KMSEnableKeyRequest,
    ) -> KMSEnableKeyResponse:
        client = self._require_client()
        return await self._execute(client.enable_key, request, KMSEnableKeyResponse)

    async def enable_key_rotation(
        self,
        request: KMSEnableKeyRotationRequest,
    ) -> KMSEnableKeyRotationResponse:
        client = self._require_client()
        return await self._execute(client.enable_key_rotation, request, KMSEnableKeyRotationResponse)

    async def encapsulate(
        self,
        request: KMSEncapsulateRequest,
    ) -> KMSEncapsulateResponse:
        client = self._require_client()
        return await self._execute(client.encapsulate, request, KMSEncapsulateResponse)

    async def encrypt(
        self,
        request: KMSEncryptRequest,
    ) -> KMSEncryptResponse:
        client = self._require_client()
        return await self._execute(client.encrypt, request, KMSEncryptResponse)

    async def generate_data_key(
        self,
        request: KMSGenerateDataKeyRequest,
    ) -> KMSGenerateDataKeyResponse:
        client = self._require_client()
        return await self._execute(client.generate_data_key, request, KMSGenerateDataKeyResponse)

    async def generate_data_key_pair(
        self,
        request: KMSGenerateDataKeyPairRequest,
    ) -> KMSGenerateDataKeyPairResponse:
        client = self._require_client()
        return await self._execute(client.generate_data_key_pair, request, KMSGenerateDataKeyPairResponse)

    async def generate_data_key_pair_without_plaintext(
        self,
        request: KMSGenerateDataKeyPairWithoutPlaintextRequest,
    ) -> KMSGenerateDataKeyPairWithoutPlaintextResponse:
        client = self._require_client()
        return await self._execute(client.generate_data_key_pair_without_plaintext, request, KMSGenerateDataKeyPairWithoutPlaintextResponse)

    async def generate_data_key_without_plaintext(
        self,
        request: KMSGenerateDataKeyWithoutPlaintextRequest,
    ) -> KMSGenerateDataKeyWithoutPlaintextResponse:
        client = self._require_client()
        return await self._execute(client.generate_data_key_without_plaintext, request, KMSGenerateDataKeyWithoutPlaintextResponse)

    async def generate_mac(
        self,
        request: KMSGenerateMacRequest,
    ) -> KMSGenerateMacResponse:
        client = self._require_client()
        return await self._execute(client.generate_mac, request, KMSGenerateMacResponse)

    async def generate_random(
        self,
        request: KMSGenerateRandomRequest | None = None,
    ) -> KMSGenerateRandomResponse:
        client = self._require_client()
        return await self._execute(client.generate_random, request, KMSGenerateRandomResponse)

    async def get_key_last_usage(
        self,
        request: KMSGetKeyLastUsageRequest,
    ) -> KMSGetKeyLastUsageResponse:
        client = self._require_client()
        return await self._execute(client.get_key_last_usage, request, KMSGetKeyLastUsageResponse)

    async def get_key_policy(
        self,
        request: KMSGetKeyPolicyRequest,
    ) -> KMSGetKeyPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_key_policy, request, KMSGetKeyPolicyResponse)

    async def get_key_rotation_status(
        self,
        request: KMSGetKeyRotationStatusRequest,
    ) -> KMSGetKeyRotationStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_key_rotation_status, request, KMSGetKeyRotationStatusResponse)

    async def get_parameters_for_import(
        self,
        request: KMSGetParametersForImportRequest,
    ) -> KMSGetParametersForImportResponse:
        client = self._require_client()
        return await self._execute(client.get_parameters_for_import, request, KMSGetParametersForImportResponse)

    async def get_public_key(
        self,
        request: KMSGetPublicKeyRequest,
    ) -> KMSGetPublicKeyResponse:
        client = self._require_client()
        return await self._execute(client.get_public_key, request, KMSGetPublicKeyResponse)

    async def import_key_material(
        self,
        request: KMSImportKeyMaterialRequest,
    ) -> KMSImportKeyMaterialResponse:
        client = self._require_client()
        return await self._execute(client.import_key_material, request, KMSImportKeyMaterialResponse)

    async def list_aliases(
        self,
        request: KMSListAliasesRequest | None = None,
    ) -> KMSListAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_aliases, request, KMSListAliasesResponse)

    async def list_aliases_paginated(
        self,
        request: KMSListAliasesRequest | None = None,
    ) -> list[KMSListAliasesResponse]:
        return await self._paginate('list_aliases', request, KMSListAliasesResponse)

    async def list_grants(
        self,
        request: KMSListGrantsRequest,
    ) -> KMSListGrantsResponse:
        client = self._require_client()
        return await self._execute(client.list_grants, request, KMSListGrantsResponse)

    async def list_grants_paginated(
        self,
        request: KMSListGrantsRequest,
    ) -> list[KMSListGrantsResponse]:
        return await self._paginate('list_grants', request, KMSListGrantsResponse)

    async def list_key_policies(
        self,
        request: KMSListKeyPoliciesRequest,
    ) -> KMSListKeyPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_key_policies, request, KMSListKeyPoliciesResponse)

    async def list_key_policies_paginated(
        self,
        request: KMSListKeyPoliciesRequest,
    ) -> list[KMSListKeyPoliciesResponse]:
        return await self._paginate('list_key_policies', request, KMSListKeyPoliciesResponse)

    async def list_key_rotations(
        self,
        request: KMSListKeyRotationsRequest,
    ) -> KMSListKeyRotationsResponse:
        client = self._require_client()
        return await self._execute(client.list_key_rotations, request, KMSListKeyRotationsResponse)

    async def list_key_rotations_paginated(
        self,
        request: KMSListKeyRotationsRequest,
    ) -> list[KMSListKeyRotationsResponse]:
        return await self._paginate('list_key_rotations', request, KMSListKeyRotationsResponse)

    async def list_keys(
        self,
        request: KMSListKeysRequest | None = None,
    ) -> KMSListKeysResponse:
        client = self._require_client()
        return await self._execute(client.list_keys, request, KMSListKeysResponse)

    async def list_keys_paginated(
        self,
        request: KMSListKeysRequest | None = None,
    ) -> list[KMSListKeysResponse]:
        return await self._paginate('list_keys', request, KMSListKeysResponse)

    async def list_resource_tags(
        self,
        request: KMSListResourceTagsRequest,
    ) -> KMSListResourceTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_tags, request, KMSListResourceTagsResponse)

    async def list_resource_tags_paginated(
        self,
        request: KMSListResourceTagsRequest,
    ) -> list[KMSListResourceTagsResponse]:
        return await self._paginate('list_resource_tags', request, KMSListResourceTagsResponse)

    async def list_retirable_grants(
        self,
        request: KMSListRetirableGrantsRequest | None = None,
    ) -> KMSListRetirableGrantsResponse:
        client = self._require_client()
        return await self._execute(client.list_retirable_grants, request, KMSListRetirableGrantsResponse)

    async def list_retirable_grants_paginated(
        self,
        request: KMSListRetirableGrantsRequest | None = None,
    ) -> list[KMSListRetirableGrantsResponse]:
        return await self._paginate('list_retirable_grants', request, KMSListRetirableGrantsResponse)

    async def put_key_policy(
        self,
        request: KMSPutKeyPolicyRequest,
    ) -> KMSPutKeyPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_key_policy, request, KMSPutKeyPolicyResponse)

    async def re_encrypt(
        self,
        request: KMSReEncryptRequest,
    ) -> KMSReEncryptResponse:
        client = self._require_client()
        return await self._execute(client.re_encrypt, request, KMSReEncryptResponse)

    async def replicate_key(
        self,
        request: KMSReplicateKeyRequest,
    ) -> KMSReplicateKeyResponse:
        client = self._require_client()
        return await self._execute(client.replicate_key, request, KMSReplicateKeyResponse)

    async def retire_grant(
        self,
        request: KMSRetireGrantRequest | None = None,
    ) -> KMSRetireGrantResponse:
        client = self._require_client()
        return await self._execute(client.retire_grant, request, KMSRetireGrantResponse)

    async def revoke_grant(
        self,
        request: KMSRevokeGrantRequest,
    ) -> KMSRevokeGrantResponse:
        client = self._require_client()
        return await self._execute(client.revoke_grant, request, KMSRevokeGrantResponse)

    async def rotate_key_on_demand(
        self,
        request: KMSRotateKeyOnDemandRequest,
    ) -> KMSRotateKeyOnDemandResponse:
        client = self._require_client()
        return await self._execute(client.rotate_key_on_demand, request, KMSRotateKeyOnDemandResponse)

    async def schedule_key_deletion(
        self,
        request: KMSScheduleKeyDeletionRequest,
    ) -> KMSScheduleKeyDeletionResponse:
        client = self._require_client()
        return await self._execute(client.schedule_key_deletion, request, KMSScheduleKeyDeletionResponse)

    async def sign(
        self,
        request: KMSSignRequest,
    ) -> KMSSignResponse:
        client = self._require_client()
        return await self._execute(client.sign, request, KMSSignResponse)

    async def tag_resource(
        self,
        request: KMSTagResourceRequest,
    ) -> KMSTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, KMSTagResourceResponse)

    async def untag_resource(
        self,
        request: KMSUntagResourceRequest,
    ) -> KMSUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, KMSUntagResourceResponse)

    async def update_alias(
        self,
        request: KMSUpdateAliasRequest,
    ) -> KMSUpdateAliasResponse:
        client = self._require_client()
        return await self._execute(client.update_alias, request, KMSUpdateAliasResponse)

    async def update_custom_key_store(
        self,
        request: KMSUpdateCustomKeyStoreRequest,
    ) -> KMSUpdateCustomKeyStoreResponse:
        client = self._require_client()
        return await self._execute(client.update_custom_key_store, request, KMSUpdateCustomKeyStoreResponse)

    async def update_key_description(
        self,
        request: KMSUpdateKeyDescriptionRequest,
    ) -> KMSUpdateKeyDescriptionResponse:
        client = self._require_client()
        return await self._execute(client.update_key_description, request, KMSUpdateKeyDescriptionResponse)

    async def update_primary_region(
        self,
        request: KMSUpdatePrimaryRegionRequest,
    ) -> KMSUpdatePrimaryRegionResponse:
        client = self._require_client()
        return await self._execute(client.update_primary_region, request, KMSUpdatePrimaryRegionResponse)

    async def verify(
        self,
        request: KMSVerifyRequest,
    ) -> KMSVerifyResponse:
        client = self._require_client()
        return await self._execute(client.verify, request, KMSVerifyResponse)

    async def verify_mac(
        self,
        request: KMSVerifyMacRequest,
    ) -> KMSVerifyMacResponse:
        client = self._require_client()
        return await self._execute(client.verify_mac, request, KMSVerifyMacResponse)
