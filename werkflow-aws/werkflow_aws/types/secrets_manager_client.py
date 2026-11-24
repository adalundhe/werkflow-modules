from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class SecretsManagerClient(ABC):

    @abstractmethod
    def get_secret_value(
        self,
        *,
        SecretId: str,
        VersionId: str | None = None,
        VersionStage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_secret(
        self,
        *,
        Name: str,
        ClientRequestToken: str | None = None,
        Description: str | None = None,
        KmsKeyId: str | None = None,
        SecretBinary: bytes | BinaryIO | str | None = None,
        SecretString: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        AddReplicaRegions: list[dict[str, Any]] | None = None,
        ForceOverwriteReplicaSecret: bool | None = None,
        Type: str | None = None,
        CrossAccountPrimaryARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_secret_value(
        self,
        *,
        SecretId: str,
        ClientRequestToken: str | None = None,
        SecretBinary: bytes | BinaryIO | str | None = None,
        SecretString: str | None = None,
        VersionStages: list[str] | None = None,
        RotationToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_secret(
        self,
        *,
        SecretId: str,
        ClientRequestToken: str | None = None,
        Description: str | None = None,
        KmsKeyId: str | None = None,
        SecretBinary: bytes | BinaryIO | str | None = None,
        SecretString: str | None = None,
        Type: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_secret(
        self,
        *,
        SecretId: str,
        RecoveryWindowInDays: int | None = None,
        ForceDeleteWithoutRecovery: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_secret(
        self,
        *,
        SecretId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_secret(
        self,
        *,
        SecretId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_secrets(
        self,
        *,
        IncludePlannedDeletion: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        SortOrder: str | None = None,
        SortBy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def rotate_secret(
        self,
        *,
        SecretId: str,
        ClientRequestToken: str | None = None,
        RotationLambdaARN: str | None = None,
        RotationRules: dict[str, Any] | None = None,
        ExternalSecretRotationMetadata: list[dict[str, Any]] | None = None,
        ExternalSecretRotationRoleArn: str | None = None,
        RotateImmediately: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        SecretId: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        SecretId: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_cross_account_replica(
        self,
        *,
        SecretId: str,
        CrossAccountReplicaARN: str,
        ReplicaRestriction: str | None = None,
        ReplicationRoleARN: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_secret_value(
        self,
        *,
        SecretIdList: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_rotate_secret(
        self,
        *,
        SecretId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        SecretId: str,
        PolicyName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_cross_account_replica(
        self,
        *,
        SecretId: str,
        CrossAccountReplicaARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_random_password(
        self,
        *,
        PasswordLength: int | None = None,
        ExcludeCharacters: str | None = None,
        ExcludeNumbers: bool | None = None,
        ExcludePunctuation: bool | None = None,
        ExcludeUppercase: bool | None = None,
        ExcludeLowercase: bool | None = None,
        IncludeSpace: bool | None = None,
        RequireEachIncludedType: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        SecretId: str,
        PolicyName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_policies(
        self,
        *,
        SecretId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_secret_version_ids(
        self,
        *,
        SecretId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IncludeDeprecated: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        SecretId: str,
        ResourcePolicy: str,
        PolicyName: str | None = None,
        BlockPublicPolicy: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_regions_from_replication(
        self,
        *,
        SecretId: str,
        RemoveReplicaRegions: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replicate_secret_to_regions(
        self,
        *,
        SecretId: str,
        AddReplicaRegions: list[dict[str, Any]],
        ForceOverwriteReplicaSecret: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_replication_to_replica(
        self,
        *,
        SecretId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_secret_version_stage(
        self,
        *,
        SecretId: str,
        VersionStage: str,
        RemoveFromVersionId: str | None = None,
        MoveToVersionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def validate_resource_policy(
        self,
        *,
        ResourcePolicy: str,
        SecretId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
