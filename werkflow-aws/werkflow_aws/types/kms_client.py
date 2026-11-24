from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class KMSClient(ABC):

    @abstractmethod
    def cancel_key_deletion(
        self,
        *,
        KeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def connect_custom_key_store(
        self,
        *,
        CustomKeyStoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_alias(
        self,
        *,
        AliasName: str,
        TargetKeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_key_store(
        self,
        *,
        CustomKeyStoreName: str,
        CloudHsmClusterId: str | None = None,
        TrustAnchorCertificate: str | None = None,
        KeyStorePassword: str | None = None,
        CustomKeyStoreType: str | None = None,
        XksProxyUriEndpoint: str | None = None,
        XksProxyUriPath: str | None = None,
        XksProxyVpcEndpointServiceName: str | None = None,
        XksProxyVpcEndpointServiceOwner: str | None = None,
        XksProxyAuthenticationCredential: dict[str, Any] | None = None,
        XksProxyConnectivity: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_grant(
        self,
        *,
        KeyId: str,
        Operations: list[str],
        GranteePrincipal: str | None = None,
        RetiringPrincipal: str | None = None,
        Constraints: dict[str, Any] | None = None,
        GrantTokens: list[str] | None = None,
        Name: str | None = None,
        DryRun: bool | None = None,
        GranteeServicePrincipal: str | None = None,
        RetiringServicePrincipal: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_key(
        self,
        *,
        Policy: str | None = None,
        Description: str | None = None,
        KeyUsage: str | None = None,
        CustomerMasterKeySpec: str | None = None,
        KeySpec: str | None = None,
        Origin: str | None = None,
        CustomKeyStoreId: str | None = None,
        BypassPolicyLockoutSafetyCheck: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        MultiRegion: bool | None = None,
        XksKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def decapsulate(
        self,
        *,
        KeyId: str,
        SharedSecretCiphertextBlob: bytes | BinaryIO | str,
        EncapsulationAlgorithm: str,
        GrantTokens: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def decrypt(
        self,
        *,
        CiphertextBlob: bytes | BinaryIO | str | None = None,
        EncryptionContext: dict[str, str] | None = None,
        GrantTokens: list[str] | None = None,
        KeyId: str | None = None,
        EncryptionAlgorithm: str | None = None,
        Recipient: dict[str, Any] | None = None,
        DryRun: bool | None = None,
        DryRunModifiers: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_alias(
        self,
        *,
        AliasName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_key_store(
        self,
        *,
        CustomKeyStoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_imported_key_material(
        self,
        *,
        KeyId: str,
        KeyMaterialId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def derive_shared_secret(
        self,
        *,
        KeyId: str,
        KeyAgreementAlgorithm: str,
        PublicKey: bytes | BinaryIO | str,
        GrantTokens: list[str] | None = None,
        DryRun: bool | None = None,
        Recipient: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_custom_key_stores(
        self,
        *,
        CustomKeyStoreId: str | None = None,
        CustomKeyStoreName: str | None = None,
        Limit: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_key(
        self,
        *,
        KeyId: str,
        GrantTokens: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_key(
        self,
        *,
        KeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_key_rotation(
        self,
        *,
        KeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disconnect_custom_key_store(
        self,
        *,
        CustomKeyStoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_key(
        self,
        *,
        KeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_key_rotation(
        self,
        *,
        KeyId: str,
        RotationPeriodInDays: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def encapsulate(
        self,
        *,
        KeyId: str,
        EncapsulationAlgorithm: str,
        GrantTokens: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def encrypt(
        self,
        *,
        KeyId: str,
        Plaintext: bytes | BinaryIO | str,
        EncryptionContext: dict[str, str] | None = None,
        GrantTokens: list[str] | None = None,
        EncryptionAlgorithm: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_data_key(
        self,
        *,
        KeyId: str,
        EncryptionContext: dict[str, str] | None = None,
        NumberOfBytes: int | None = None,
        KeySpec: str | None = None,
        GrantTokens: list[str] | None = None,
        Recipient: dict[str, Any] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_data_key_pair(
        self,
        *,
        KeyId: str,
        KeyPairSpec: str,
        EncryptionContext: dict[str, str] | None = None,
        GrantTokens: list[str] | None = None,
        Recipient: dict[str, Any] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_data_key_pair_without_plaintext(
        self,
        *,
        KeyId: str,
        KeyPairSpec: str,
        EncryptionContext: dict[str, str] | None = None,
        GrantTokens: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_data_key_without_plaintext(
        self,
        *,
        KeyId: str,
        EncryptionContext: dict[str, str] | None = None,
        KeySpec: str | None = None,
        NumberOfBytes: int | None = None,
        GrantTokens: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_mac(
        self,
        *,
        Message: bytes | BinaryIO | str,
        KeyId: str,
        MacAlgorithm: str,
        GrantTokens: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_random(
        self,
        *,
        NumberOfBytes: int | None = None,
        CustomKeyStoreId: str | None = None,
        Recipient: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_key_last_usage(
        self,
        *,
        KeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_key_policy(
        self,
        *,
        KeyId: str,
        PolicyName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_key_rotation_status(
        self,
        *,
        KeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_parameters_for_import(
        self,
        *,
        KeyId: str,
        WrappingAlgorithm: str,
        WrappingKeySpec: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_public_key(
        self,
        *,
        KeyId: str,
        GrantTokens: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_key_material(
        self,
        *,
        KeyId: str,
        ImportToken: bytes | BinaryIO | str,
        EncryptedKeyMaterial: bytes | BinaryIO | str,
        ValidTo: datetime.datetime | str | None = None,
        ExpirationModel: str | None = None,
        ImportType: str | None = None,
        KeyMaterialDescription: str | None = None,
        KeyMaterialId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_aliases(
        self,
        *,
        KeyId: str | None = None,
        Limit: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_grants(
        self,
        *,
        KeyId: str,
        Limit: int | None = None,
        Marker: str | None = None,
        GrantId: str | None = None,
        GranteePrincipal: str | None = None,
        GranteeServicePrincipal: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_key_policies(
        self,
        *,
        KeyId: str,
        Limit: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_key_rotations(
        self,
        *,
        KeyId: str,
        IncludeKeyMaterial: str | None = None,
        Limit: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_keys(
        self,
        *,
        Limit: int | None = None,
        Marker: str | None = None,
        ResourceOwners: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_tags(
        self,
        *,
        KeyId: str,
        Limit: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_retirable_grants(
        self,
        *,
        Limit: int | None = None,
        Marker: str | None = None,
        RetiringPrincipal: str | None = None,
        RetiringServicePrincipal: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_key_policy(
        self,
        *,
        KeyId: str,
        Policy: str,
        PolicyName: str | None = None,
        BypassPolicyLockoutSafetyCheck: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def re_encrypt(
        self,
        *,
        DestinationKeyId: str,
        CiphertextBlob: bytes | BinaryIO | str | None = None,
        SourceEncryptionContext: dict[str, str] | None = None,
        SourceKeyId: str | None = None,
        DestinationEncryptionContext: dict[str, str] | None = None,
        SourceEncryptionAlgorithm: str | None = None,
        DestinationEncryptionAlgorithm: str | None = None,
        GrantTokens: list[str] | None = None,
        DryRun: bool | None = None,
        DryRunModifiers: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replicate_key(
        self,
        *,
        KeyId: str,
        ReplicaRegion: str,
        Policy: str | None = None,
        BypassPolicyLockoutSafetyCheck: bool | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def retire_grant(
        self,
        *,
        GrantToken: str | None = None,
        KeyId: str | None = None,
        GrantId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_grant(
        self,
        *,
        KeyId: str,
        GrantId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def rotate_key_on_demand(
        self,
        *,
        KeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def schedule_key_deletion(
        self,
        *,
        KeyId: str,
        PendingWindowInDays: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def sign(
        self,
        *,
        KeyId: str,
        Message: bytes | BinaryIO | str,
        SigningAlgorithm: str,
        MessageType: str | None = None,
        GrantTokens: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        KeyId: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        KeyId: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_alias(
        self,
        *,
        AliasName: str,
        TargetKeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_custom_key_store(
        self,
        *,
        CustomKeyStoreId: str,
        NewCustomKeyStoreName: str | None = None,
        KeyStorePassword: str | None = None,
        CloudHsmClusterId: str | None = None,
        XksProxyUriEndpoint: str | None = None,
        XksProxyUriPath: str | None = None,
        XksProxyVpcEndpointServiceName: str | None = None,
        XksProxyVpcEndpointServiceOwner: str | None = None,
        XksProxyAuthenticationCredential: dict[str, Any] | None = None,
        XksProxyConnectivity: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_key_description(
        self,
        *,
        KeyId: str,
        Description: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_primary_region(
        self,
        *,
        KeyId: str,
        PrimaryRegion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def verify(
        self,
        *,
        KeyId: str,
        Message: bytes | BinaryIO | str,
        Signature: bytes | BinaryIO | str,
        SigningAlgorithm: str,
        MessageType: str | None = None,
        GrantTokens: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def verify_mac(
        self,
        *,
        Message: bytes | BinaryIO | str,
        KeyId: str,
        MacAlgorithm: str,
        Mac: bytes | BinaryIO | str,
        GrantTokens: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
