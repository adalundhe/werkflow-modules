from werkflow_aws.models.rekognition import (
    RekognitionAssociateFacesRequest,
    RekognitionAssociateFacesResponse,
    RekognitionCompareFacesRequest,
    RekognitionCompareFacesResponse,
    RekognitionCopyProjectVersionRequest,
    RekognitionCopyProjectVersionResponse,
    RekognitionCreateCollectionRequest,
    RekognitionCreateCollectionResponse,
    RekognitionCreateDatasetRequest,
    RekognitionCreateDatasetResponse,
    RekognitionCreateFaceLivenessSessionRequest,
    RekognitionCreateFaceLivenessSessionResponse,
    RekognitionCreateProjectRequest,
    RekognitionCreateProjectResponse,
    RekognitionCreateProjectVersionRequest,
    RekognitionCreateProjectVersionResponse,
    RekognitionCreateStreamProcessorRequest,
    RekognitionCreateStreamProcessorResponse,
    RekognitionCreateUserRequest,
    RekognitionCreateUserResponse,
    RekognitionDeleteCollectionRequest,
    RekognitionDeleteCollectionResponse,
    RekognitionDeleteDatasetRequest,
    RekognitionDeleteDatasetResponse,
    RekognitionDeleteFacesRequest,
    RekognitionDeleteFacesResponse,
    RekognitionDeleteProjectPolicyRequest,
    RekognitionDeleteProjectPolicyResponse,
    RekognitionDeleteProjectRequest,
    RekognitionDeleteProjectResponse,
    RekognitionDeleteProjectVersionRequest,
    RekognitionDeleteProjectVersionResponse,
    RekognitionDeleteStreamProcessorRequest,
    RekognitionDeleteStreamProcessorResponse,
    RekognitionDeleteUserRequest,
    RekognitionDeleteUserResponse,
    RekognitionDescribeCollectionRequest,
    RekognitionDescribeCollectionResponse,
    RekognitionDescribeDatasetRequest,
    RekognitionDescribeDatasetResponse,
    RekognitionDescribeProjectVersionsRequest,
    RekognitionDescribeProjectVersionsResponse,
    RekognitionDescribeProjectsRequest,
    RekognitionDescribeProjectsResponse,
    RekognitionDescribeStreamProcessorRequest,
    RekognitionDescribeStreamProcessorResponse,
    RekognitionDetectCustomLabelsRequest,
    RekognitionDetectCustomLabelsResponse,
    RekognitionDetectFacesRequest,
    RekognitionDetectFacesResponse,
    RekognitionDetectLabelsRequest,
    RekognitionDetectLabelsResponse,
    RekognitionDetectModerationLabelsRequest,
    RekognitionDetectModerationLabelsResponse,
    RekognitionDetectProtectiveEquipmentRequest,
    RekognitionDetectProtectiveEquipmentResponse,
    RekognitionDetectTextRequest,
    RekognitionDetectTextResponse,
    RekognitionDisassociateFacesRequest,
    RekognitionDisassociateFacesResponse,
    RekognitionDistributeDatasetEntriesRequest,
    RekognitionDistributeDatasetEntriesResponse,
    RekognitionGetCelebrityInfoRequest,
    RekognitionGetCelebrityInfoResponse,
    RekognitionGetCelebrityRecognitionRequest,
    RekognitionGetCelebrityRecognitionResponse,
    RekognitionGetContentModerationRequest,
    RekognitionGetContentModerationResponse,
    RekognitionGetFaceDetectionRequest,
    RekognitionGetFaceDetectionResponse,
    RekognitionGetFaceLivenessSessionResultsRequest,
    RekognitionGetFaceLivenessSessionResultsResponse,
    RekognitionGetFaceSearchRequest,
    RekognitionGetFaceSearchResponse,
    RekognitionGetLabelDetectionRequest,
    RekognitionGetLabelDetectionResponse,
    RekognitionGetMediaAnalysisJobRequest,
    RekognitionGetMediaAnalysisJobResponse,
    RekognitionGetPersonTrackingRequest,
    RekognitionGetPersonTrackingResponse,
    RekognitionGetSegmentDetectionRequest,
    RekognitionGetSegmentDetectionResponse,
    RekognitionGetTextDetectionRequest,
    RekognitionGetTextDetectionResponse,
    RekognitionIndexFacesRequest,
    RekognitionIndexFacesResponse,
    RekognitionListCollectionsRequest,
    RekognitionListCollectionsResponse,
    RekognitionListDatasetEntriesRequest,
    RekognitionListDatasetEntriesResponse,
    RekognitionListDatasetLabelsRequest,
    RekognitionListDatasetLabelsResponse,
    RekognitionListFacesRequest,
    RekognitionListFacesResponse,
    RekognitionListMediaAnalysisJobsRequest,
    RekognitionListMediaAnalysisJobsResponse,
    RekognitionListProjectPoliciesRequest,
    RekognitionListProjectPoliciesResponse,
    RekognitionListStreamProcessorsRequest,
    RekognitionListStreamProcessorsResponse,
    RekognitionListTagsForResourceRequest,
    RekognitionListTagsForResourceResponse,
    RekognitionListUsersRequest,
    RekognitionListUsersResponse,
    RekognitionPutProjectPolicyRequest,
    RekognitionPutProjectPolicyResponse,
    RekognitionRecognizeCelebritiesRequest,
    RekognitionRecognizeCelebritiesResponse,
    RekognitionSearchFacesByImageRequest,
    RekognitionSearchFacesByImageResponse,
    RekognitionSearchFacesRequest,
    RekognitionSearchFacesResponse,
    RekognitionSearchUsersByImageRequest,
    RekognitionSearchUsersByImageResponse,
    RekognitionSearchUsersRequest,
    RekognitionSearchUsersResponse,
    RekognitionStartCelebrityRecognitionRequest,
    RekognitionStartCelebrityRecognitionResponse,
    RekognitionStartContentModerationRequest,
    RekognitionStartContentModerationResponse,
    RekognitionStartFaceDetectionRequest,
    RekognitionStartFaceDetectionResponse,
    RekognitionStartFaceSearchRequest,
    RekognitionStartFaceSearchResponse,
    RekognitionStartLabelDetectionRequest,
    RekognitionStartLabelDetectionResponse,
    RekognitionStartMediaAnalysisJobRequest,
    RekognitionStartMediaAnalysisJobResponse,
    RekognitionStartPersonTrackingRequest,
    RekognitionStartPersonTrackingResponse,
    RekognitionStartProjectVersionRequest,
    RekognitionStartProjectVersionResponse,
    RekognitionStartSegmentDetectionRequest,
    RekognitionStartSegmentDetectionResponse,
    RekognitionStartStreamProcessorRequest,
    RekognitionStartStreamProcessorResponse,
    RekognitionStartTextDetectionRequest,
    RekognitionStartTextDetectionResponse,
    RekognitionStopProjectVersionRequest,
    RekognitionStopProjectVersionResponse,
    RekognitionStopStreamProcessorRequest,
    RekognitionStopStreamProcessorResponse,
    RekognitionTagResourceRequest,
    RekognitionTagResourceResponse,
    RekognitionUntagResourceRequest,
    RekognitionUntagResourceResponse,
    RekognitionUpdateDatasetEntriesRequest,
    RekognitionUpdateDatasetEntriesResponse,
    RekognitionUpdateStreamProcessorRequest,
    RekognitionUpdateStreamProcessorResponse,
)
from werkflow_aws.types.rekognition_client import RekognitionClient
from .base import AWSBaseService


class AWSRekognition(AWSBaseService[RekognitionClient]):
    service_name = 'rekognition'
    boto3_service_name = 'rekognition'

    def __init__(self) -> None:
        super().__init__(service_name='rekognition', boto3_service_name='rekognition')

    async def associate_faces(
        self,
        request: RekognitionAssociateFacesRequest,
    ) -> RekognitionAssociateFacesResponse:
        client = self._require_client()
        return await self._execute(client.associate_faces, request, RekognitionAssociateFacesResponse)

    async def compare_faces(
        self,
        request: RekognitionCompareFacesRequest,
    ) -> RekognitionCompareFacesResponse:
        client = self._require_client()
        return await self._execute(client.compare_faces, request, RekognitionCompareFacesResponse)

    async def copy_project_version(
        self,
        request: RekognitionCopyProjectVersionRequest,
    ) -> RekognitionCopyProjectVersionResponse:
        client = self._require_client()
        return await self._execute(client.copy_project_version, request, RekognitionCopyProjectVersionResponse)

    async def create_collection(
        self,
        request: RekognitionCreateCollectionRequest,
    ) -> RekognitionCreateCollectionResponse:
        client = self._require_client()
        return await self._execute(client.create_collection, request, RekognitionCreateCollectionResponse)

    async def create_dataset(
        self,
        request: RekognitionCreateDatasetRequest,
    ) -> RekognitionCreateDatasetResponse:
        client = self._require_client()
        return await self._execute(client.create_dataset, request, RekognitionCreateDatasetResponse)

    async def create_face_liveness_session(
        self,
        request: RekognitionCreateFaceLivenessSessionRequest | None = None,
    ) -> RekognitionCreateFaceLivenessSessionResponse:
        client = self._require_client()
        return await self._execute(client.create_face_liveness_session, request, RekognitionCreateFaceLivenessSessionResponse)

    async def create_project(
        self,
        request: RekognitionCreateProjectRequest,
    ) -> RekognitionCreateProjectResponse:
        client = self._require_client()
        return await self._execute(client.create_project, request, RekognitionCreateProjectResponse)

    async def create_project_version(
        self,
        request: RekognitionCreateProjectVersionRequest,
    ) -> RekognitionCreateProjectVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_project_version, request, RekognitionCreateProjectVersionResponse)

    async def create_stream_processor(
        self,
        request: RekognitionCreateStreamProcessorRequest,
    ) -> RekognitionCreateStreamProcessorResponse:
        client = self._require_client()
        return await self._execute(client.create_stream_processor, request, RekognitionCreateStreamProcessorResponse)

    async def create_user(
        self,
        request: RekognitionCreateUserRequest,
    ) -> RekognitionCreateUserResponse:
        client = self._require_client()
        return await self._execute(client.create_user, request, RekognitionCreateUserResponse)

    async def delete_collection(
        self,
        request: RekognitionDeleteCollectionRequest,
    ) -> RekognitionDeleteCollectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_collection, request, RekognitionDeleteCollectionResponse)

    async def delete_dataset(
        self,
        request: RekognitionDeleteDatasetRequest,
    ) -> RekognitionDeleteDatasetResponse:
        client = self._require_client()
        return await self._execute(client.delete_dataset, request, RekognitionDeleteDatasetResponse)

    async def delete_faces(
        self,
        request: RekognitionDeleteFacesRequest,
    ) -> RekognitionDeleteFacesResponse:
        client = self._require_client()
        return await self._execute(client.delete_faces, request, RekognitionDeleteFacesResponse)

    async def delete_project(
        self,
        request: RekognitionDeleteProjectRequest,
    ) -> RekognitionDeleteProjectResponse:
        client = self._require_client()
        return await self._execute(client.delete_project, request, RekognitionDeleteProjectResponse)

    async def delete_project_policy(
        self,
        request: RekognitionDeleteProjectPolicyRequest,
    ) -> RekognitionDeleteProjectPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_project_policy, request, RekognitionDeleteProjectPolicyResponse)

    async def delete_project_version(
        self,
        request: RekognitionDeleteProjectVersionRequest,
    ) -> RekognitionDeleteProjectVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_project_version, request, RekognitionDeleteProjectVersionResponse)

    async def delete_stream_processor(
        self,
        request: RekognitionDeleteStreamProcessorRequest,
    ) -> RekognitionDeleteStreamProcessorResponse:
        client = self._require_client()
        return await self._execute(client.delete_stream_processor, request, RekognitionDeleteStreamProcessorResponse)

    async def delete_user(
        self,
        request: RekognitionDeleteUserRequest,
    ) -> RekognitionDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.delete_user, request, RekognitionDeleteUserResponse)

    async def describe_collection(
        self,
        request: RekognitionDescribeCollectionRequest,
    ) -> RekognitionDescribeCollectionResponse:
        client = self._require_client()
        return await self._execute(client.describe_collection, request, RekognitionDescribeCollectionResponse)

    async def describe_dataset(
        self,
        request: RekognitionDescribeDatasetRequest,
    ) -> RekognitionDescribeDatasetResponse:
        client = self._require_client()
        return await self._execute(client.describe_dataset, request, RekognitionDescribeDatasetResponse)

    async def describe_project_versions(
        self,
        request: RekognitionDescribeProjectVersionsRequest,
    ) -> RekognitionDescribeProjectVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_project_versions, request, RekognitionDescribeProjectVersionsResponse)

    async def describe_project_versions_paginated(
        self,
        request: RekognitionDescribeProjectVersionsRequest,
    ) -> list[RekognitionDescribeProjectVersionsResponse]:
        return await self._paginate('describe_project_versions', request, RekognitionDescribeProjectVersionsResponse)

    async def describe_projects(
        self,
        request: RekognitionDescribeProjectsRequest | None = None,
    ) -> RekognitionDescribeProjectsResponse:
        client = self._require_client()
        return await self._execute(client.describe_projects, request, RekognitionDescribeProjectsResponse)

    async def describe_projects_paginated(
        self,
        request: RekognitionDescribeProjectsRequest | None = None,
    ) -> list[RekognitionDescribeProjectsResponse]:
        return await self._paginate('describe_projects', request, RekognitionDescribeProjectsResponse)

    async def describe_stream_processor(
        self,
        request: RekognitionDescribeStreamProcessorRequest,
    ) -> RekognitionDescribeStreamProcessorResponse:
        client = self._require_client()
        return await self._execute(client.describe_stream_processor, request, RekognitionDescribeStreamProcessorResponse)

    async def detect_custom_labels(
        self,
        request: RekognitionDetectCustomLabelsRequest,
    ) -> RekognitionDetectCustomLabelsResponse:
        client = self._require_client()
        return await self._execute(client.detect_custom_labels, request, RekognitionDetectCustomLabelsResponse)

    async def detect_faces(
        self,
        request: RekognitionDetectFacesRequest,
    ) -> RekognitionDetectFacesResponse:
        client = self._require_client()
        return await self._execute(client.detect_faces, request, RekognitionDetectFacesResponse)

    async def detect_labels(
        self,
        request: RekognitionDetectLabelsRequest,
    ) -> RekognitionDetectLabelsResponse:
        client = self._require_client()
        return await self._execute(client.detect_labels, request, RekognitionDetectLabelsResponse)

    async def detect_moderation_labels(
        self,
        request: RekognitionDetectModerationLabelsRequest,
    ) -> RekognitionDetectModerationLabelsResponse:
        client = self._require_client()
        return await self._execute(client.detect_moderation_labels, request, RekognitionDetectModerationLabelsResponse)

    async def detect_protective_equipment(
        self,
        request: RekognitionDetectProtectiveEquipmentRequest,
    ) -> RekognitionDetectProtectiveEquipmentResponse:
        client = self._require_client()
        return await self._execute(client.detect_protective_equipment, request, RekognitionDetectProtectiveEquipmentResponse)

    async def detect_text(
        self,
        request: RekognitionDetectTextRequest,
    ) -> RekognitionDetectTextResponse:
        client = self._require_client()
        return await self._execute(client.detect_text, request, RekognitionDetectTextResponse)

    async def disassociate_faces(
        self,
        request: RekognitionDisassociateFacesRequest,
    ) -> RekognitionDisassociateFacesResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_faces, request, RekognitionDisassociateFacesResponse)

    async def distribute_dataset_entries(
        self,
        request: RekognitionDistributeDatasetEntriesRequest,
    ) -> RekognitionDistributeDatasetEntriesResponse:
        client = self._require_client()
        return await self._execute(client.distribute_dataset_entries, request, RekognitionDistributeDatasetEntriesResponse)

    async def get_celebrity_info(
        self,
        request: RekognitionGetCelebrityInfoRequest,
    ) -> RekognitionGetCelebrityInfoResponse:
        client = self._require_client()
        return await self._execute(client.get_celebrity_info, request, RekognitionGetCelebrityInfoResponse)

    async def get_celebrity_recognition(
        self,
        request: RekognitionGetCelebrityRecognitionRequest,
    ) -> RekognitionGetCelebrityRecognitionResponse:
        client = self._require_client()
        return await self._execute(client.get_celebrity_recognition, request, RekognitionGetCelebrityRecognitionResponse)

    async def get_content_moderation(
        self,
        request: RekognitionGetContentModerationRequest,
    ) -> RekognitionGetContentModerationResponse:
        client = self._require_client()
        return await self._execute(client.get_content_moderation, request, RekognitionGetContentModerationResponse)

    async def get_face_detection(
        self,
        request: RekognitionGetFaceDetectionRequest,
    ) -> RekognitionGetFaceDetectionResponse:
        client = self._require_client()
        return await self._execute(client.get_face_detection, request, RekognitionGetFaceDetectionResponse)

    async def get_face_liveness_session_results(
        self,
        request: RekognitionGetFaceLivenessSessionResultsRequest,
    ) -> RekognitionGetFaceLivenessSessionResultsResponse:
        client = self._require_client()
        return await self._execute(client.get_face_liveness_session_results, request, RekognitionGetFaceLivenessSessionResultsResponse)

    async def get_face_search(
        self,
        request: RekognitionGetFaceSearchRequest,
    ) -> RekognitionGetFaceSearchResponse:
        client = self._require_client()
        return await self._execute(client.get_face_search, request, RekognitionGetFaceSearchResponse)

    async def get_label_detection(
        self,
        request: RekognitionGetLabelDetectionRequest,
    ) -> RekognitionGetLabelDetectionResponse:
        client = self._require_client()
        return await self._execute(client.get_label_detection, request, RekognitionGetLabelDetectionResponse)

    async def get_media_analysis_job(
        self,
        request: RekognitionGetMediaAnalysisJobRequest,
    ) -> RekognitionGetMediaAnalysisJobResponse:
        client = self._require_client()
        return await self._execute(client.get_media_analysis_job, request, RekognitionGetMediaAnalysisJobResponse)

    async def get_person_tracking(
        self,
        request: RekognitionGetPersonTrackingRequest,
    ) -> RekognitionGetPersonTrackingResponse:
        client = self._require_client()
        return await self._execute(client.get_person_tracking, request, RekognitionGetPersonTrackingResponse)

    async def get_segment_detection(
        self,
        request: RekognitionGetSegmentDetectionRequest,
    ) -> RekognitionGetSegmentDetectionResponse:
        client = self._require_client()
        return await self._execute(client.get_segment_detection, request, RekognitionGetSegmentDetectionResponse)

    async def get_text_detection(
        self,
        request: RekognitionGetTextDetectionRequest,
    ) -> RekognitionGetTextDetectionResponse:
        client = self._require_client()
        return await self._execute(client.get_text_detection, request, RekognitionGetTextDetectionResponse)

    async def index_faces(
        self,
        request: RekognitionIndexFacesRequest,
    ) -> RekognitionIndexFacesResponse:
        client = self._require_client()
        return await self._execute(client.index_faces, request, RekognitionIndexFacesResponse)

    async def list_collections(
        self,
        request: RekognitionListCollectionsRequest | None = None,
    ) -> RekognitionListCollectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_collections, request, RekognitionListCollectionsResponse)

    async def list_collections_paginated(
        self,
        request: RekognitionListCollectionsRequest | None = None,
    ) -> list[RekognitionListCollectionsResponse]:
        return await self._paginate('list_collections', request, RekognitionListCollectionsResponse)

    async def list_dataset_entries(
        self,
        request: RekognitionListDatasetEntriesRequest,
    ) -> RekognitionListDatasetEntriesResponse:
        client = self._require_client()
        return await self._execute(client.list_dataset_entries, request, RekognitionListDatasetEntriesResponse)

    async def list_dataset_entries_paginated(
        self,
        request: RekognitionListDatasetEntriesRequest,
    ) -> list[RekognitionListDatasetEntriesResponse]:
        return await self._paginate('list_dataset_entries', request, RekognitionListDatasetEntriesResponse)

    async def list_dataset_labels(
        self,
        request: RekognitionListDatasetLabelsRequest,
    ) -> RekognitionListDatasetLabelsResponse:
        client = self._require_client()
        return await self._execute(client.list_dataset_labels, request, RekognitionListDatasetLabelsResponse)

    async def list_dataset_labels_paginated(
        self,
        request: RekognitionListDatasetLabelsRequest,
    ) -> list[RekognitionListDatasetLabelsResponse]:
        return await self._paginate('list_dataset_labels', request, RekognitionListDatasetLabelsResponse)

    async def list_faces(
        self,
        request: RekognitionListFacesRequest,
    ) -> RekognitionListFacesResponse:
        client = self._require_client()
        return await self._execute(client.list_faces, request, RekognitionListFacesResponse)

    async def list_faces_paginated(
        self,
        request: RekognitionListFacesRequest,
    ) -> list[RekognitionListFacesResponse]:
        return await self._paginate('list_faces', request, RekognitionListFacesResponse)

    async def list_media_analysis_jobs(
        self,
        request: RekognitionListMediaAnalysisJobsRequest | None = None,
    ) -> RekognitionListMediaAnalysisJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_media_analysis_jobs, request, RekognitionListMediaAnalysisJobsResponse)

    async def list_project_policies(
        self,
        request: RekognitionListProjectPoliciesRequest,
    ) -> RekognitionListProjectPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_project_policies, request, RekognitionListProjectPoliciesResponse)

    async def list_project_policies_paginated(
        self,
        request: RekognitionListProjectPoliciesRequest,
    ) -> list[RekognitionListProjectPoliciesResponse]:
        return await self._paginate('list_project_policies', request, RekognitionListProjectPoliciesResponse)

    async def list_stream_processors(
        self,
        request: RekognitionListStreamProcessorsRequest | None = None,
    ) -> RekognitionListStreamProcessorsResponse:
        client = self._require_client()
        return await self._execute(client.list_stream_processors, request, RekognitionListStreamProcessorsResponse)

    async def list_stream_processors_paginated(
        self,
        request: RekognitionListStreamProcessorsRequest | None = None,
    ) -> list[RekognitionListStreamProcessorsResponse]:
        return await self._paginate('list_stream_processors', request, RekognitionListStreamProcessorsResponse)

    async def list_tags_for_resource(
        self,
        request: RekognitionListTagsForResourceRequest,
    ) -> RekognitionListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, RekognitionListTagsForResourceResponse)

    async def list_users(
        self,
        request: RekognitionListUsersRequest,
    ) -> RekognitionListUsersResponse:
        client = self._require_client()
        return await self._execute(client.list_users, request, RekognitionListUsersResponse)

    async def list_users_paginated(
        self,
        request: RekognitionListUsersRequest,
    ) -> list[RekognitionListUsersResponse]:
        return await self._paginate('list_users', request, RekognitionListUsersResponse)

    async def put_project_policy(
        self,
        request: RekognitionPutProjectPolicyRequest,
    ) -> RekognitionPutProjectPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_project_policy, request, RekognitionPutProjectPolicyResponse)

    async def recognize_celebrities(
        self,
        request: RekognitionRecognizeCelebritiesRequest,
    ) -> RekognitionRecognizeCelebritiesResponse:
        client = self._require_client()
        return await self._execute(client.recognize_celebrities, request, RekognitionRecognizeCelebritiesResponse)

    async def search_faces(
        self,
        request: RekognitionSearchFacesRequest,
    ) -> RekognitionSearchFacesResponse:
        client = self._require_client()
        return await self._execute(client.search_faces, request, RekognitionSearchFacesResponse)

    async def search_faces_by_image(
        self,
        request: RekognitionSearchFacesByImageRequest,
    ) -> RekognitionSearchFacesByImageResponse:
        client = self._require_client()
        return await self._execute(client.search_faces_by_image, request, RekognitionSearchFacesByImageResponse)

    async def search_users(
        self,
        request: RekognitionSearchUsersRequest,
    ) -> RekognitionSearchUsersResponse:
        client = self._require_client()
        return await self._execute(client.search_users, request, RekognitionSearchUsersResponse)

    async def search_users_by_image(
        self,
        request: RekognitionSearchUsersByImageRequest,
    ) -> RekognitionSearchUsersByImageResponse:
        client = self._require_client()
        return await self._execute(client.search_users_by_image, request, RekognitionSearchUsersByImageResponse)

    async def start_celebrity_recognition(
        self,
        request: RekognitionStartCelebrityRecognitionRequest,
    ) -> RekognitionStartCelebrityRecognitionResponse:
        client = self._require_client()
        return await self._execute(client.start_celebrity_recognition, request, RekognitionStartCelebrityRecognitionResponse)

    async def start_content_moderation(
        self,
        request: RekognitionStartContentModerationRequest,
    ) -> RekognitionStartContentModerationResponse:
        client = self._require_client()
        return await self._execute(client.start_content_moderation, request, RekognitionStartContentModerationResponse)

    async def start_face_detection(
        self,
        request: RekognitionStartFaceDetectionRequest,
    ) -> RekognitionStartFaceDetectionResponse:
        client = self._require_client()
        return await self._execute(client.start_face_detection, request, RekognitionStartFaceDetectionResponse)

    async def start_face_search(
        self,
        request: RekognitionStartFaceSearchRequest,
    ) -> RekognitionStartFaceSearchResponse:
        client = self._require_client()
        return await self._execute(client.start_face_search, request, RekognitionStartFaceSearchResponse)

    async def start_label_detection(
        self,
        request: RekognitionStartLabelDetectionRequest,
    ) -> RekognitionStartLabelDetectionResponse:
        client = self._require_client()
        return await self._execute(client.start_label_detection, request, RekognitionStartLabelDetectionResponse)

    async def start_media_analysis_job(
        self,
        request: RekognitionStartMediaAnalysisJobRequest,
    ) -> RekognitionStartMediaAnalysisJobResponse:
        client = self._require_client()
        return await self._execute(client.start_media_analysis_job, request, RekognitionStartMediaAnalysisJobResponse)

    async def start_person_tracking(
        self,
        request: RekognitionStartPersonTrackingRequest,
    ) -> RekognitionStartPersonTrackingResponse:
        client = self._require_client()
        return await self._execute(client.start_person_tracking, request, RekognitionStartPersonTrackingResponse)

    async def start_project_version(
        self,
        request: RekognitionStartProjectVersionRequest,
    ) -> RekognitionStartProjectVersionResponse:
        client = self._require_client()
        return await self._execute(client.start_project_version, request, RekognitionStartProjectVersionResponse)

    async def start_segment_detection(
        self,
        request: RekognitionStartSegmentDetectionRequest,
    ) -> RekognitionStartSegmentDetectionResponse:
        client = self._require_client()
        return await self._execute(client.start_segment_detection, request, RekognitionStartSegmentDetectionResponse)

    async def start_stream_processor(
        self,
        request: RekognitionStartStreamProcessorRequest,
    ) -> RekognitionStartStreamProcessorResponse:
        client = self._require_client()
        return await self._execute(client.start_stream_processor, request, RekognitionStartStreamProcessorResponse)

    async def start_text_detection(
        self,
        request: RekognitionStartTextDetectionRequest,
    ) -> RekognitionStartTextDetectionResponse:
        client = self._require_client()
        return await self._execute(client.start_text_detection, request, RekognitionStartTextDetectionResponse)

    async def stop_project_version(
        self,
        request: RekognitionStopProjectVersionRequest,
    ) -> RekognitionStopProjectVersionResponse:
        client = self._require_client()
        return await self._execute(client.stop_project_version, request, RekognitionStopProjectVersionResponse)

    async def stop_stream_processor(
        self,
        request: RekognitionStopStreamProcessorRequest,
    ) -> RekognitionStopStreamProcessorResponse:
        client = self._require_client()
        return await self._execute(client.stop_stream_processor, request, RekognitionStopStreamProcessorResponse)

    async def tag_resource(
        self,
        request: RekognitionTagResourceRequest,
    ) -> RekognitionTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, RekognitionTagResourceResponse)

    async def untag_resource(
        self,
        request: RekognitionUntagResourceRequest,
    ) -> RekognitionUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, RekognitionUntagResourceResponse)

    async def update_dataset_entries(
        self,
        request: RekognitionUpdateDatasetEntriesRequest,
    ) -> RekognitionUpdateDatasetEntriesResponse:
        client = self._require_client()
        return await self._execute(client.update_dataset_entries, request, RekognitionUpdateDatasetEntriesResponse)

    async def update_stream_processor(
        self,
        request: RekognitionUpdateStreamProcessorRequest,
    ) -> RekognitionUpdateStreamProcessorResponse:
        client = self._require_client()
        return await self._execute(client.update_stream_processor, request, RekognitionUpdateStreamProcessorResponse)
