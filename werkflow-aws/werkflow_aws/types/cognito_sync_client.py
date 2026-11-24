from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class CognitoSyncClient(ABC):

    @abstractmethod
    def bulk_publish(
        self,
        *,
        IdentityPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dataset(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dataset(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_identity_pool_usage(
        self,
        *,
        IdentityPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_identity_usage(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_bulk_publish_details(
        self,
        *,
        IdentityPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cognito_events(
        self,
        *,
        IdentityPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_identity_pool_configuration(
        self,
        *,
        IdentityPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_datasets(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_identity_pool_usage(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_records(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        LastSyncCount: int | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SyncSessionToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_device(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str,
        Platform: str,
        Token: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_cognito_events(
        self,
        *,
        IdentityPoolId: str,
        Events: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_identity_pool_configuration(
        self,
        *,
        IdentityPoolId: str,
        PushSync: dict[str, Any] | None = None,
        CognitoStreams: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def subscribe_to_dataset(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        DeviceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def unsubscribe_from_dataset(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        DeviceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_records(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        SyncSessionToken: str,
        DeviceId: str | None = None,
        RecordPatches: list[dict[str, Any]] | None = None,
        ClientContext: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
