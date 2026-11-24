from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class GlacierClient(ABC):

    @abstractmethod
    def abort_multipart_upload(
        self,
        *,
        accountId: str,
        vaultName: str,
        uploadId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def abort_vault_lock(
        self,
        *,
        accountId: str,
        vaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_tags_to_vault(
        self,
        *,
        accountId: str,
        vaultName: str,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def complete_multipart_upload(
        self,
        *,
        accountId: str,
        vaultName: str,
        uploadId: str,
        archiveSize: str | None = None,
        checksum: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def complete_vault_lock(
        self,
        *,
        accountId: str,
        vaultName: str,
        lockId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vault(
        self,
        *,
        accountId: str,
        vaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_archive(
        self,
        *,
        accountId: str,
        vaultName: str,
        archiveId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vault(
        self,
        *,
        accountId: str,
        vaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vault_access_policy(
        self,
        *,
        accountId: str,
        vaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vault_notifications(
        self,
        *,
        accountId: str,
        vaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_job(
        self,
        *,
        accountId: str,
        vaultName: str,
        jobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vault(
        self,
        *,
        accountId: str,
        vaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_retrieval_policy(
        self,
        *,
        accountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job_output(
        self,
        *,
        accountId: str,
        vaultName: str,
        jobId: str,
        range: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vault_access_policy(
        self,
        *,
        accountId: str,
        vaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vault_lock(
        self,
        *,
        accountId: str,
        vaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vault_notifications(
        self,
        *,
        accountId: str,
        vaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def initiate_job(
        self,
        *,
        accountId: str,
        vaultName: str,
        jobParameters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def initiate_multipart_upload(
        self,
        *,
        accountId: str,
        vaultName: str,
        archiveDescription: str | None = None,
        partSize: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def initiate_vault_lock(
        self,
        *,
        accountId: str,
        vaultName: str,
        policy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_jobs(
        self,
        *,
        accountId: str,
        vaultName: str,
        limit: str | None = None,
        marker: str | None = None,
        statuscode: str | None = None,
        completed: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_multipart_uploads(
        self,
        *,
        accountId: str,
        vaultName: str,
        marker: str | None = None,
        limit: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_parts(
        self,
        *,
        accountId: str,
        vaultName: str,
        uploadId: str,
        marker: str | None = None,
        limit: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_provisioned_capacity(
        self,
        *,
        accountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_vault(
        self,
        *,
        accountId: str,
        vaultName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vaults(
        self,
        *,
        accountId: str,
        marker: str | None = None,
        limit: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purchase_provisioned_capacity(
        self,
        *,
        accountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags_from_vault(
        self,
        *,
        accountId: str,
        vaultName: str,
        TagKeys: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_data_retrieval_policy(
        self,
        *,
        accountId: str,
        Policy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_vault_access_policy(
        self,
        *,
        accountId: str,
        vaultName: str,
        policy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_vault_notifications(
        self,
        *,
        accountId: str,
        vaultName: str,
        vaultNotificationConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def upload_archive(
        self,
        *,
        vaultName: str,
        accountId: str,
        archiveDescription: str | None = None,
        checksum: str | None = None,
        body: bytes | BinaryIO | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def upload_multipart_part(
        self,
        *,
        accountId: str,
        vaultName: str,
        uploadId: str,
        checksum: str | None = None,
        range: str | None = None,
        body: bytes | BinaryIO | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
