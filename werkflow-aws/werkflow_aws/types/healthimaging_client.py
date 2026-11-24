from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class HealthImagingClient(ABC):

    @abstractmethod
    def copy_image_set(
        self,
        *,
        datastoreId: str,
        sourceImageSetId: str,
        copyImageSetInformation: dict[str, Any],
        force: bool | None = None,
        promoteToPrimary: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_datastore(
        self,
        *,
        clientToken: str,
        datastoreName: str | None = None,
        tags: dict[str, str] | None = None,
        kmsKeyArn: str | None = None,
        lambdaAuthorizerArn: str | None = None,
        losslessStorageFormat: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_datastore(
        self,
        *,
        datastoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_image_set(
        self,
        *,
        datastoreId: str,
        imageSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dicom_import_job(
        self,
        *,
        datastoreId: str,
        jobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_datastore(
        self,
        *,
        datastoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_image_frame(
        self,
        *,
        datastoreId: str,
        imageSetId: str,
        imageFrameInformation: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_image_set(
        self,
        *,
        datastoreId: str,
        imageSetId: str,
        versionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_image_set_metadata(
        self,
        *,
        datastoreId: str,
        imageSetId: str,
        versionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dicom_import_jobs(
        self,
        *,
        datastoreId: str,
        jobStatus: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_datastores(
        self,
        *,
        datastoreStatus: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_image_set_versions(
        self,
        *,
        datastoreId: str,
        imageSetId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_image_sets(
        self,
        *,
        datastoreId: str,
        searchCriteria: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_dicom_import_job(
        self,
        *,
        dataAccessRoleArn: str,
        clientToken: str,
        datastoreId: str,
        inputS3Uri: str,
        outputS3Uri: str,
        jobName: str | None = None,
        inputOwnerAccountId: str | None = None,
        importConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_image_set_metadata(
        self,
        *,
        datastoreId: str,
        imageSetId: str,
        latestVersionId: str,
        updateImageSetMetadataUpdates: dict[str, Any],
        force: bool | None = None,
        includeStudyImageSets: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
