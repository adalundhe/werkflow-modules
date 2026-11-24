from werkflow_aws.models.healthimaging import (
    HealthImagingCopyImageSetRequest,
    HealthImagingCopyImageSetResponse,
    HealthImagingCreateDatastoreRequest,
    HealthImagingCreateDatastoreResponse,
    HealthImagingDeleteDatastoreRequest,
    HealthImagingDeleteDatastoreResponse,
    HealthImagingDeleteImageSetRequest,
    HealthImagingDeleteImageSetResponse,
    HealthImagingGetDICOMImportJobRequest,
    HealthImagingGetDICOMImportJobResponse,
    HealthImagingGetDatastoreRequest,
    HealthImagingGetDatastoreResponse,
    HealthImagingGetImageFrameRequest,
    HealthImagingGetImageFrameResponse,
    HealthImagingGetImageSetMetadataRequest,
    HealthImagingGetImageSetMetadataResponse,
    HealthImagingGetImageSetRequest,
    HealthImagingGetImageSetResponse,
    HealthImagingListDICOMImportJobsRequest,
    HealthImagingListDICOMImportJobsResponse,
    HealthImagingListDatastoresRequest,
    HealthImagingListDatastoresResponse,
    HealthImagingListImageSetVersionsRequest,
    HealthImagingListImageSetVersionsResponse,
    HealthImagingListTagsForResourceRequest,
    HealthImagingListTagsForResourceResponse,
    HealthImagingSearchImageSetsRequest,
    HealthImagingSearchImageSetsResponse,
    HealthImagingStartDICOMImportJobRequest,
    HealthImagingStartDICOMImportJobResponse,
    HealthImagingTagResourceRequest,
    HealthImagingTagResourceResponse,
    HealthImagingUntagResourceRequest,
    HealthImagingUntagResourceResponse,
    HealthImagingUpdateImageSetMetadataRequest,
    HealthImagingUpdateImageSetMetadataResponse,
)
from werkflow_aws.types.healthimaging_client import HealthImagingClient
from .base import AWSBaseService


class AWSHealthImaging(AWSBaseService[HealthImagingClient]):
    service_name = 'healthimaging'
    boto3_service_name = 'medical-imaging'

    def __init__(self) -> None:
        super().__init__(service_name='healthimaging', boto3_service_name='medical-imaging')

    async def copy_image_set(
        self,
        request: HealthImagingCopyImageSetRequest,
    ) -> HealthImagingCopyImageSetResponse:
        client = self._require_client()
        return await self._execute(client.copy_image_set, request, HealthImagingCopyImageSetResponse)

    async def create_datastore(
        self,
        request: HealthImagingCreateDatastoreRequest,
    ) -> HealthImagingCreateDatastoreResponse:
        client = self._require_client()
        return await self._execute(client.create_datastore, request, HealthImagingCreateDatastoreResponse)

    async def delete_datastore(
        self,
        request: HealthImagingDeleteDatastoreRequest,
    ) -> HealthImagingDeleteDatastoreResponse:
        client = self._require_client()
        return await self._execute(client.delete_datastore, request, HealthImagingDeleteDatastoreResponse)

    async def delete_image_set(
        self,
        request: HealthImagingDeleteImageSetRequest,
    ) -> HealthImagingDeleteImageSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_image_set, request, HealthImagingDeleteImageSetResponse)

    async def get_dicom_import_job(
        self,
        request: HealthImagingGetDICOMImportJobRequest,
    ) -> HealthImagingGetDICOMImportJobResponse:
        client = self._require_client()
        return await self._execute(client.get_dicom_import_job, request, HealthImagingGetDICOMImportJobResponse)

    async def get_datastore(
        self,
        request: HealthImagingGetDatastoreRequest,
    ) -> HealthImagingGetDatastoreResponse:
        client = self._require_client()
        return await self._execute(client.get_datastore, request, HealthImagingGetDatastoreResponse)

    async def get_image_frame(
        self,
        request: HealthImagingGetImageFrameRequest,
    ) -> HealthImagingGetImageFrameResponse:
        client = self._require_client()
        return await self._execute(client.get_image_frame, request, HealthImagingGetImageFrameResponse)

    async def get_image_set(
        self,
        request: HealthImagingGetImageSetRequest,
    ) -> HealthImagingGetImageSetResponse:
        client = self._require_client()
        return await self._execute(client.get_image_set, request, HealthImagingGetImageSetResponse)

    async def get_image_set_metadata(
        self,
        request: HealthImagingGetImageSetMetadataRequest,
    ) -> HealthImagingGetImageSetMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_image_set_metadata, request, HealthImagingGetImageSetMetadataResponse)

    async def list_dicom_import_jobs(
        self,
        request: HealthImagingListDICOMImportJobsRequest,
    ) -> HealthImagingListDICOMImportJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_dicom_import_jobs, request, HealthImagingListDICOMImportJobsResponse)

    async def list_dicom_import_jobs_paginated(
        self,
        request: HealthImagingListDICOMImportJobsRequest,
    ) -> list[HealthImagingListDICOMImportJobsResponse]:
        return await self._paginate('list_dicom_import_jobs', request, HealthImagingListDICOMImportJobsResponse)

    async def list_datastores(
        self,
        request: HealthImagingListDatastoresRequest | None = None,
    ) -> HealthImagingListDatastoresResponse:
        client = self._require_client()
        return await self._execute(client.list_datastores, request, HealthImagingListDatastoresResponse)

    async def list_datastores_paginated(
        self,
        request: HealthImagingListDatastoresRequest | None = None,
    ) -> list[HealthImagingListDatastoresResponse]:
        return await self._paginate('list_datastores', request, HealthImagingListDatastoresResponse)

    async def list_image_set_versions(
        self,
        request: HealthImagingListImageSetVersionsRequest,
    ) -> HealthImagingListImageSetVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_image_set_versions, request, HealthImagingListImageSetVersionsResponse)

    async def list_image_set_versions_paginated(
        self,
        request: HealthImagingListImageSetVersionsRequest,
    ) -> list[HealthImagingListImageSetVersionsResponse]:
        return await self._paginate('list_image_set_versions', request, HealthImagingListImageSetVersionsResponse)

    async def list_tags_for_resource(
        self,
        request: HealthImagingListTagsForResourceRequest,
    ) -> HealthImagingListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, HealthImagingListTagsForResourceResponse)

    async def search_image_sets(
        self,
        request: HealthImagingSearchImageSetsRequest,
    ) -> HealthImagingSearchImageSetsResponse:
        client = self._require_client()
        return await self._execute(client.search_image_sets, request, HealthImagingSearchImageSetsResponse)

    async def search_image_sets_paginated(
        self,
        request: HealthImagingSearchImageSetsRequest,
    ) -> list[HealthImagingSearchImageSetsResponse]:
        return await self._paginate('search_image_sets', request, HealthImagingSearchImageSetsResponse)

    async def start_dicom_import_job(
        self,
        request: HealthImagingStartDICOMImportJobRequest,
    ) -> HealthImagingStartDICOMImportJobResponse:
        client = self._require_client()
        return await self._execute(client.start_dicom_import_job, request, HealthImagingStartDICOMImportJobResponse)

    async def tag_resource(
        self,
        request: HealthImagingTagResourceRequest,
    ) -> HealthImagingTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, HealthImagingTagResourceResponse)

    async def untag_resource(
        self,
        request: HealthImagingUntagResourceRequest,
    ) -> HealthImagingUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, HealthImagingUntagResourceResponse)

    async def update_image_set_metadata(
        self,
        request: HealthImagingUpdateImageSetMetadataRequest,
    ) -> HealthImagingUpdateImageSetMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_image_set_metadata, request, HealthImagingUpdateImageSetMetadataResponse)
