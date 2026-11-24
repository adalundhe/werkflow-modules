from werkflow_aws.models.comprehend import (
    ComprehendBatchDetectDominantLanguageRequest,
    ComprehendBatchDetectDominantLanguageResponse,
    ComprehendBatchDetectEntitiesRequest,
    ComprehendBatchDetectEntitiesResponse,
    ComprehendBatchDetectKeyPhrasesRequest,
    ComprehendBatchDetectKeyPhrasesResponse,
    ComprehendBatchDetectSentimentRequest,
    ComprehendBatchDetectSentimentResponse,
    ComprehendBatchDetectSyntaxRequest,
    ComprehendBatchDetectSyntaxResponse,
    ComprehendBatchDetectTargetedSentimentRequest,
    ComprehendBatchDetectTargetedSentimentResponse,
    ComprehendClassifyDocumentRequest,
    ComprehendClassifyDocumentResponse,
    ComprehendContainsPiiEntitiesRequest,
    ComprehendContainsPiiEntitiesResponse,
    ComprehendCreateDatasetRequest,
    ComprehendCreateDatasetResponse,
    ComprehendCreateDocumentClassifierRequest,
    ComprehendCreateDocumentClassifierResponse,
    ComprehendCreateEndpointRequest,
    ComprehendCreateEndpointResponse,
    ComprehendCreateEntityRecognizerRequest,
    ComprehendCreateEntityRecognizerResponse,
    ComprehendCreateFlywheelRequest,
    ComprehendCreateFlywheelResponse,
    ComprehendDeleteDocumentClassifierRequest,
    ComprehendDeleteDocumentClassifierResponse,
    ComprehendDeleteEndpointRequest,
    ComprehendDeleteEndpointResponse,
    ComprehendDeleteEntityRecognizerRequest,
    ComprehendDeleteEntityRecognizerResponse,
    ComprehendDeleteFlywheelRequest,
    ComprehendDeleteFlywheelResponse,
    ComprehendDeleteResourcePolicyRequest,
    ComprehendDeleteResourcePolicyResponse,
    ComprehendDescribeDatasetRequest,
    ComprehendDescribeDatasetResponse,
    ComprehendDescribeDocumentClassificationJobRequest,
    ComprehendDescribeDocumentClassificationJobResponse,
    ComprehendDescribeDocumentClassifierRequest,
    ComprehendDescribeDocumentClassifierResponse,
    ComprehendDescribeDominantLanguageDetectionJobRequest,
    ComprehendDescribeDominantLanguageDetectionJobResponse,
    ComprehendDescribeEndpointRequest,
    ComprehendDescribeEndpointResponse,
    ComprehendDescribeEntitiesDetectionJobRequest,
    ComprehendDescribeEntitiesDetectionJobResponse,
    ComprehendDescribeEntityRecognizerRequest,
    ComprehendDescribeEntityRecognizerResponse,
    ComprehendDescribeEventsDetectionJobRequest,
    ComprehendDescribeEventsDetectionJobResponse,
    ComprehendDescribeFlywheelIterationRequest,
    ComprehendDescribeFlywheelIterationResponse,
    ComprehendDescribeFlywheelRequest,
    ComprehendDescribeFlywheelResponse,
    ComprehendDescribeKeyPhrasesDetectionJobRequest,
    ComprehendDescribeKeyPhrasesDetectionJobResponse,
    ComprehendDescribePiiEntitiesDetectionJobRequest,
    ComprehendDescribePiiEntitiesDetectionJobResponse,
    ComprehendDescribeResourcePolicyRequest,
    ComprehendDescribeResourcePolicyResponse,
    ComprehendDescribeSentimentDetectionJobRequest,
    ComprehendDescribeSentimentDetectionJobResponse,
    ComprehendDescribeTargetedSentimentDetectionJobRequest,
    ComprehendDescribeTargetedSentimentDetectionJobResponse,
    ComprehendDescribeTopicsDetectionJobRequest,
    ComprehendDescribeTopicsDetectionJobResponse,
    ComprehendDetectDominantLanguageRequest,
    ComprehendDetectDominantLanguageResponse,
    ComprehendDetectEntitiesRequest,
    ComprehendDetectEntitiesResponse,
    ComprehendDetectKeyPhrasesRequest,
    ComprehendDetectKeyPhrasesResponse,
    ComprehendDetectPiiEntitiesRequest,
    ComprehendDetectPiiEntitiesResponse,
    ComprehendDetectSentimentRequest,
    ComprehendDetectSentimentResponse,
    ComprehendDetectSyntaxRequest,
    ComprehendDetectSyntaxResponse,
    ComprehendDetectTargetedSentimentRequest,
    ComprehendDetectTargetedSentimentResponse,
    ComprehendDetectToxicContentRequest,
    ComprehendDetectToxicContentResponse,
    ComprehendImportModelRequest,
    ComprehendImportModelResponse,
    ComprehendListDatasetsRequest,
    ComprehendListDatasetsResponse,
    ComprehendListDocumentClassificationJobsRequest,
    ComprehendListDocumentClassificationJobsResponse,
    ComprehendListDocumentClassifierSummariesRequest,
    ComprehendListDocumentClassifierSummariesResponse,
    ComprehendListDocumentClassifiersRequest,
    ComprehendListDocumentClassifiersResponse,
    ComprehendListDominantLanguageDetectionJobsRequest,
    ComprehendListDominantLanguageDetectionJobsResponse,
    ComprehendListEndpointsRequest,
    ComprehendListEndpointsResponse,
    ComprehendListEntitiesDetectionJobsRequest,
    ComprehendListEntitiesDetectionJobsResponse,
    ComprehendListEntityRecognizerSummariesRequest,
    ComprehendListEntityRecognizerSummariesResponse,
    ComprehendListEntityRecognizersRequest,
    ComprehendListEntityRecognizersResponse,
    ComprehendListEventsDetectionJobsRequest,
    ComprehendListEventsDetectionJobsResponse,
    ComprehendListFlywheelIterationHistoryRequest,
    ComprehendListFlywheelIterationHistoryResponse,
    ComprehendListFlywheelsRequest,
    ComprehendListFlywheelsResponse,
    ComprehendListKeyPhrasesDetectionJobsRequest,
    ComprehendListKeyPhrasesDetectionJobsResponse,
    ComprehendListPiiEntitiesDetectionJobsRequest,
    ComprehendListPiiEntitiesDetectionJobsResponse,
    ComprehendListSentimentDetectionJobsRequest,
    ComprehendListSentimentDetectionJobsResponse,
    ComprehendListTagsForResourceRequest,
    ComprehendListTagsForResourceResponse,
    ComprehendListTargetedSentimentDetectionJobsRequest,
    ComprehendListTargetedSentimentDetectionJobsResponse,
    ComprehendListTopicsDetectionJobsRequest,
    ComprehendListTopicsDetectionJobsResponse,
    ComprehendPutResourcePolicyRequest,
    ComprehendPutResourcePolicyResponse,
    ComprehendStartDocumentClassificationJobRequest,
    ComprehendStartDocumentClassificationJobResponse,
    ComprehendStartDominantLanguageDetectionJobRequest,
    ComprehendStartDominantLanguageDetectionJobResponse,
    ComprehendStartEntitiesDetectionJobRequest,
    ComprehendStartEntitiesDetectionJobResponse,
    ComprehendStartEventsDetectionJobRequest,
    ComprehendStartEventsDetectionJobResponse,
    ComprehendStartFlywheelIterationRequest,
    ComprehendStartFlywheelIterationResponse,
    ComprehendStartKeyPhrasesDetectionJobRequest,
    ComprehendStartKeyPhrasesDetectionJobResponse,
    ComprehendStartPiiEntitiesDetectionJobRequest,
    ComprehendStartPiiEntitiesDetectionJobResponse,
    ComprehendStartSentimentDetectionJobRequest,
    ComprehendStartSentimentDetectionJobResponse,
    ComprehendStartTargetedSentimentDetectionJobRequest,
    ComprehendStartTargetedSentimentDetectionJobResponse,
    ComprehendStartTopicsDetectionJobRequest,
    ComprehendStartTopicsDetectionJobResponse,
    ComprehendStopDominantLanguageDetectionJobRequest,
    ComprehendStopDominantLanguageDetectionJobResponse,
    ComprehendStopEntitiesDetectionJobRequest,
    ComprehendStopEntitiesDetectionJobResponse,
    ComprehendStopEventsDetectionJobRequest,
    ComprehendStopEventsDetectionJobResponse,
    ComprehendStopKeyPhrasesDetectionJobRequest,
    ComprehendStopKeyPhrasesDetectionJobResponse,
    ComprehendStopPiiEntitiesDetectionJobRequest,
    ComprehendStopPiiEntitiesDetectionJobResponse,
    ComprehendStopSentimentDetectionJobRequest,
    ComprehendStopSentimentDetectionJobResponse,
    ComprehendStopTargetedSentimentDetectionJobRequest,
    ComprehendStopTargetedSentimentDetectionJobResponse,
    ComprehendStopTrainingDocumentClassifierRequest,
    ComprehendStopTrainingDocumentClassifierResponse,
    ComprehendStopTrainingEntityRecognizerRequest,
    ComprehendStopTrainingEntityRecognizerResponse,
    ComprehendTagResourceRequest,
    ComprehendTagResourceResponse,
    ComprehendUntagResourceRequest,
    ComprehendUntagResourceResponse,
    ComprehendUpdateEndpointRequest,
    ComprehendUpdateEndpointResponse,
    ComprehendUpdateFlywheelRequest,
    ComprehendUpdateFlywheelResponse,
)
from werkflow_aws.types.comprehend_client import ComprehendClient
from .base import AWSBaseService


class AWSComprehend(AWSBaseService[ComprehendClient]):
    service_name = 'comprehend'
    boto3_service_name = 'comprehend'

    def __init__(self) -> None:
        super().__init__(service_name='comprehend', boto3_service_name='comprehend')

    async def batch_detect_dominant_language(
        self,
        request: ComprehendBatchDetectDominantLanguageRequest,
    ) -> ComprehendBatchDetectDominantLanguageResponse:
        client = self._require_client()
        return await self._execute(client.batch_detect_dominant_language, request, ComprehendBatchDetectDominantLanguageResponse)

    async def batch_detect_entities(
        self,
        request: ComprehendBatchDetectEntitiesRequest,
    ) -> ComprehendBatchDetectEntitiesResponse:
        client = self._require_client()
        return await self._execute(client.batch_detect_entities, request, ComprehendBatchDetectEntitiesResponse)

    async def batch_detect_key_phrases(
        self,
        request: ComprehendBatchDetectKeyPhrasesRequest,
    ) -> ComprehendBatchDetectKeyPhrasesResponse:
        client = self._require_client()
        return await self._execute(client.batch_detect_key_phrases, request, ComprehendBatchDetectKeyPhrasesResponse)

    async def batch_detect_sentiment(
        self,
        request: ComprehendBatchDetectSentimentRequest,
    ) -> ComprehendBatchDetectSentimentResponse:
        client = self._require_client()
        return await self._execute(client.batch_detect_sentiment, request, ComprehendBatchDetectSentimentResponse)

    async def batch_detect_syntax(
        self,
        request: ComprehendBatchDetectSyntaxRequest,
    ) -> ComprehendBatchDetectSyntaxResponse:
        client = self._require_client()
        return await self._execute(client.batch_detect_syntax, request, ComprehendBatchDetectSyntaxResponse)

    async def batch_detect_targeted_sentiment(
        self,
        request: ComprehendBatchDetectTargetedSentimentRequest,
    ) -> ComprehendBatchDetectTargetedSentimentResponse:
        client = self._require_client()
        return await self._execute(client.batch_detect_targeted_sentiment, request, ComprehendBatchDetectTargetedSentimentResponse)

    async def classify_document(
        self,
        request: ComprehendClassifyDocumentRequest,
    ) -> ComprehendClassifyDocumentResponse:
        client = self._require_client()
        return await self._execute(client.classify_document, request, ComprehendClassifyDocumentResponse)

    async def contains_pii_entities(
        self,
        request: ComprehendContainsPiiEntitiesRequest,
    ) -> ComprehendContainsPiiEntitiesResponse:
        client = self._require_client()
        return await self._execute(client.contains_pii_entities, request, ComprehendContainsPiiEntitiesResponse)

    async def create_dataset(
        self,
        request: ComprehendCreateDatasetRequest,
    ) -> ComprehendCreateDatasetResponse:
        client = self._require_client()
        return await self._execute(client.create_dataset, request, ComprehendCreateDatasetResponse)

    async def create_document_classifier(
        self,
        request: ComprehendCreateDocumentClassifierRequest,
    ) -> ComprehendCreateDocumentClassifierResponse:
        client = self._require_client()
        return await self._execute(client.create_document_classifier, request, ComprehendCreateDocumentClassifierResponse)

    async def create_endpoint(
        self,
        request: ComprehendCreateEndpointRequest,
    ) -> ComprehendCreateEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_endpoint, request, ComprehendCreateEndpointResponse)

    async def create_entity_recognizer(
        self,
        request: ComprehendCreateEntityRecognizerRequest,
    ) -> ComprehendCreateEntityRecognizerResponse:
        client = self._require_client()
        return await self._execute(client.create_entity_recognizer, request, ComprehendCreateEntityRecognizerResponse)

    async def create_flywheel(
        self,
        request: ComprehendCreateFlywheelRequest,
    ) -> ComprehendCreateFlywheelResponse:
        client = self._require_client()
        return await self._execute(client.create_flywheel, request, ComprehendCreateFlywheelResponse)

    async def delete_document_classifier(
        self,
        request: ComprehendDeleteDocumentClassifierRequest,
    ) -> ComprehendDeleteDocumentClassifierResponse:
        client = self._require_client()
        return await self._execute(client.delete_document_classifier, request, ComprehendDeleteDocumentClassifierResponse)

    async def delete_endpoint(
        self,
        request: ComprehendDeleteEndpointRequest,
    ) -> ComprehendDeleteEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_endpoint, request, ComprehendDeleteEndpointResponse)

    async def delete_entity_recognizer(
        self,
        request: ComprehendDeleteEntityRecognizerRequest,
    ) -> ComprehendDeleteEntityRecognizerResponse:
        client = self._require_client()
        return await self._execute(client.delete_entity_recognizer, request, ComprehendDeleteEntityRecognizerResponse)

    async def delete_flywheel(
        self,
        request: ComprehendDeleteFlywheelRequest,
    ) -> ComprehendDeleteFlywheelResponse:
        client = self._require_client()
        return await self._execute(client.delete_flywheel, request, ComprehendDeleteFlywheelResponse)

    async def delete_resource_policy(
        self,
        request: ComprehendDeleteResourcePolicyRequest,
    ) -> ComprehendDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, ComprehendDeleteResourcePolicyResponse)

    async def describe_dataset(
        self,
        request: ComprehendDescribeDatasetRequest,
    ) -> ComprehendDescribeDatasetResponse:
        client = self._require_client()
        return await self._execute(client.describe_dataset, request, ComprehendDescribeDatasetResponse)

    async def describe_document_classification_job(
        self,
        request: ComprehendDescribeDocumentClassificationJobRequest,
    ) -> ComprehendDescribeDocumentClassificationJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_document_classification_job, request, ComprehendDescribeDocumentClassificationJobResponse)

    async def describe_document_classifier(
        self,
        request: ComprehendDescribeDocumentClassifierRequest,
    ) -> ComprehendDescribeDocumentClassifierResponse:
        client = self._require_client()
        return await self._execute(client.describe_document_classifier, request, ComprehendDescribeDocumentClassifierResponse)

    async def describe_dominant_language_detection_job(
        self,
        request: ComprehendDescribeDominantLanguageDetectionJobRequest,
    ) -> ComprehendDescribeDominantLanguageDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_dominant_language_detection_job, request, ComprehendDescribeDominantLanguageDetectionJobResponse)

    async def describe_endpoint(
        self,
        request: ComprehendDescribeEndpointRequest,
    ) -> ComprehendDescribeEndpointResponse:
        client = self._require_client()
        return await self._execute(client.describe_endpoint, request, ComprehendDescribeEndpointResponse)

    async def describe_entities_detection_job(
        self,
        request: ComprehendDescribeEntitiesDetectionJobRequest,
    ) -> ComprehendDescribeEntitiesDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_entities_detection_job, request, ComprehendDescribeEntitiesDetectionJobResponse)

    async def describe_entity_recognizer(
        self,
        request: ComprehendDescribeEntityRecognizerRequest,
    ) -> ComprehendDescribeEntityRecognizerResponse:
        client = self._require_client()
        return await self._execute(client.describe_entity_recognizer, request, ComprehendDescribeEntityRecognizerResponse)

    async def describe_events_detection_job(
        self,
        request: ComprehendDescribeEventsDetectionJobRequest,
    ) -> ComprehendDescribeEventsDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_events_detection_job, request, ComprehendDescribeEventsDetectionJobResponse)

    async def describe_flywheel(
        self,
        request: ComprehendDescribeFlywheelRequest,
    ) -> ComprehendDescribeFlywheelResponse:
        client = self._require_client()
        return await self._execute(client.describe_flywheel, request, ComprehendDescribeFlywheelResponse)

    async def describe_flywheel_iteration(
        self,
        request: ComprehendDescribeFlywheelIterationRequest,
    ) -> ComprehendDescribeFlywheelIterationResponse:
        client = self._require_client()
        return await self._execute(client.describe_flywheel_iteration, request, ComprehendDescribeFlywheelIterationResponse)

    async def describe_key_phrases_detection_job(
        self,
        request: ComprehendDescribeKeyPhrasesDetectionJobRequest,
    ) -> ComprehendDescribeKeyPhrasesDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_key_phrases_detection_job, request, ComprehendDescribeKeyPhrasesDetectionJobResponse)

    async def describe_pii_entities_detection_job(
        self,
        request: ComprehendDescribePiiEntitiesDetectionJobRequest,
    ) -> ComprehendDescribePiiEntitiesDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_pii_entities_detection_job, request, ComprehendDescribePiiEntitiesDetectionJobResponse)

    async def describe_resource_policy(
        self,
        request: ComprehendDescribeResourcePolicyRequest,
    ) -> ComprehendDescribeResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.describe_resource_policy, request, ComprehendDescribeResourcePolicyResponse)

    async def describe_sentiment_detection_job(
        self,
        request: ComprehendDescribeSentimentDetectionJobRequest,
    ) -> ComprehendDescribeSentimentDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_sentiment_detection_job, request, ComprehendDescribeSentimentDetectionJobResponse)

    async def describe_targeted_sentiment_detection_job(
        self,
        request: ComprehendDescribeTargetedSentimentDetectionJobRequest,
    ) -> ComprehendDescribeTargetedSentimentDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_targeted_sentiment_detection_job, request, ComprehendDescribeTargetedSentimentDetectionJobResponse)

    async def describe_topics_detection_job(
        self,
        request: ComprehendDescribeTopicsDetectionJobRequest,
    ) -> ComprehendDescribeTopicsDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_topics_detection_job, request, ComprehendDescribeTopicsDetectionJobResponse)

    async def detect_dominant_language(
        self,
        request: ComprehendDetectDominantLanguageRequest,
    ) -> ComprehendDetectDominantLanguageResponse:
        client = self._require_client()
        return await self._execute(client.detect_dominant_language, request, ComprehendDetectDominantLanguageResponse)

    async def detect_entities(
        self,
        request: ComprehendDetectEntitiesRequest | None = None,
    ) -> ComprehendDetectEntitiesResponse:
        client = self._require_client()
        return await self._execute(client.detect_entities, request, ComprehendDetectEntitiesResponse)

    async def detect_key_phrases(
        self,
        request: ComprehendDetectKeyPhrasesRequest,
    ) -> ComprehendDetectKeyPhrasesResponse:
        client = self._require_client()
        return await self._execute(client.detect_key_phrases, request, ComprehendDetectKeyPhrasesResponse)

    async def detect_pii_entities(
        self,
        request: ComprehendDetectPiiEntitiesRequest,
    ) -> ComprehendDetectPiiEntitiesResponse:
        client = self._require_client()
        return await self._execute(client.detect_pii_entities, request, ComprehendDetectPiiEntitiesResponse)

    async def detect_sentiment(
        self,
        request: ComprehendDetectSentimentRequest,
    ) -> ComprehendDetectSentimentResponse:
        client = self._require_client()
        return await self._execute(client.detect_sentiment, request, ComprehendDetectSentimentResponse)

    async def detect_syntax(
        self,
        request: ComprehendDetectSyntaxRequest,
    ) -> ComprehendDetectSyntaxResponse:
        client = self._require_client()
        return await self._execute(client.detect_syntax, request, ComprehendDetectSyntaxResponse)

    async def detect_targeted_sentiment(
        self,
        request: ComprehendDetectTargetedSentimentRequest,
    ) -> ComprehendDetectTargetedSentimentResponse:
        client = self._require_client()
        return await self._execute(client.detect_targeted_sentiment, request, ComprehendDetectTargetedSentimentResponse)

    async def detect_toxic_content(
        self,
        request: ComprehendDetectToxicContentRequest,
    ) -> ComprehendDetectToxicContentResponse:
        client = self._require_client()
        return await self._execute(client.detect_toxic_content, request, ComprehendDetectToxicContentResponse)

    async def import_model(
        self,
        request: ComprehendImportModelRequest,
    ) -> ComprehendImportModelResponse:
        client = self._require_client()
        return await self._execute(client.import_model, request, ComprehendImportModelResponse)

    async def list_datasets(
        self,
        request: ComprehendListDatasetsRequest | None = None,
    ) -> ComprehendListDatasetsResponse:
        client = self._require_client()
        return await self._execute(client.list_datasets, request, ComprehendListDatasetsResponse)

    async def list_document_classification_jobs(
        self,
        request: ComprehendListDocumentClassificationJobsRequest | None = None,
    ) -> ComprehendListDocumentClassificationJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_document_classification_jobs, request, ComprehendListDocumentClassificationJobsResponse)

    async def list_document_classification_jobs_paginated(
        self,
        request: ComprehendListDocumentClassificationJobsRequest | None = None,
    ) -> list[ComprehendListDocumentClassificationJobsResponse]:
        return await self._paginate('list_document_classification_jobs', request, ComprehendListDocumentClassificationJobsResponse)

    async def list_document_classifier_summaries(
        self,
        request: ComprehendListDocumentClassifierSummariesRequest | None = None,
    ) -> ComprehendListDocumentClassifierSummariesResponse:
        client = self._require_client()
        return await self._execute(client.list_document_classifier_summaries, request, ComprehendListDocumentClassifierSummariesResponse)

    async def list_document_classifiers(
        self,
        request: ComprehendListDocumentClassifiersRequest | None = None,
    ) -> ComprehendListDocumentClassifiersResponse:
        client = self._require_client()
        return await self._execute(client.list_document_classifiers, request, ComprehendListDocumentClassifiersResponse)

    async def list_document_classifiers_paginated(
        self,
        request: ComprehendListDocumentClassifiersRequest | None = None,
    ) -> list[ComprehendListDocumentClassifiersResponse]:
        return await self._paginate('list_document_classifiers', request, ComprehendListDocumentClassifiersResponse)

    async def list_dominant_language_detection_jobs(
        self,
        request: ComprehendListDominantLanguageDetectionJobsRequest | None = None,
    ) -> ComprehendListDominantLanguageDetectionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_dominant_language_detection_jobs, request, ComprehendListDominantLanguageDetectionJobsResponse)

    async def list_dominant_language_detection_jobs_paginated(
        self,
        request: ComprehendListDominantLanguageDetectionJobsRequest | None = None,
    ) -> list[ComprehendListDominantLanguageDetectionJobsResponse]:
        return await self._paginate('list_dominant_language_detection_jobs', request, ComprehendListDominantLanguageDetectionJobsResponse)

    async def list_endpoints(
        self,
        request: ComprehendListEndpointsRequest | None = None,
    ) -> ComprehendListEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.list_endpoints, request, ComprehendListEndpointsResponse)

    async def list_endpoints_paginated(
        self,
        request: ComprehendListEndpointsRequest | None = None,
    ) -> list[ComprehendListEndpointsResponse]:
        return await self._paginate('list_endpoints', request, ComprehendListEndpointsResponse)

    async def list_entities_detection_jobs(
        self,
        request: ComprehendListEntitiesDetectionJobsRequest | None = None,
    ) -> ComprehendListEntitiesDetectionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_entities_detection_jobs, request, ComprehendListEntitiesDetectionJobsResponse)

    async def list_entities_detection_jobs_paginated(
        self,
        request: ComprehendListEntitiesDetectionJobsRequest | None = None,
    ) -> list[ComprehendListEntitiesDetectionJobsResponse]:
        return await self._paginate('list_entities_detection_jobs', request, ComprehendListEntitiesDetectionJobsResponse)

    async def list_entity_recognizer_summaries(
        self,
        request: ComprehendListEntityRecognizerSummariesRequest | None = None,
    ) -> ComprehendListEntityRecognizerSummariesResponse:
        client = self._require_client()
        return await self._execute(client.list_entity_recognizer_summaries, request, ComprehendListEntityRecognizerSummariesResponse)

    async def list_entity_recognizers(
        self,
        request: ComprehendListEntityRecognizersRequest | None = None,
    ) -> ComprehendListEntityRecognizersResponse:
        client = self._require_client()
        return await self._execute(client.list_entity_recognizers, request, ComprehendListEntityRecognizersResponse)

    async def list_entity_recognizers_paginated(
        self,
        request: ComprehendListEntityRecognizersRequest | None = None,
    ) -> list[ComprehendListEntityRecognizersResponse]:
        return await self._paginate('list_entity_recognizers', request, ComprehendListEntityRecognizersResponse)

    async def list_events_detection_jobs(
        self,
        request: ComprehendListEventsDetectionJobsRequest | None = None,
    ) -> ComprehendListEventsDetectionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_events_detection_jobs, request, ComprehendListEventsDetectionJobsResponse)

    async def list_flywheel_iteration_history(
        self,
        request: ComprehendListFlywheelIterationHistoryRequest,
    ) -> ComprehendListFlywheelIterationHistoryResponse:
        client = self._require_client()
        return await self._execute(client.list_flywheel_iteration_history, request, ComprehendListFlywheelIterationHistoryResponse)

    async def list_flywheels(
        self,
        request: ComprehendListFlywheelsRequest | None = None,
    ) -> ComprehendListFlywheelsResponse:
        client = self._require_client()
        return await self._execute(client.list_flywheels, request, ComprehendListFlywheelsResponse)

    async def list_key_phrases_detection_jobs(
        self,
        request: ComprehendListKeyPhrasesDetectionJobsRequest | None = None,
    ) -> ComprehendListKeyPhrasesDetectionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_key_phrases_detection_jobs, request, ComprehendListKeyPhrasesDetectionJobsResponse)

    async def list_key_phrases_detection_jobs_paginated(
        self,
        request: ComprehendListKeyPhrasesDetectionJobsRequest | None = None,
    ) -> list[ComprehendListKeyPhrasesDetectionJobsResponse]:
        return await self._paginate('list_key_phrases_detection_jobs', request, ComprehendListKeyPhrasesDetectionJobsResponse)

    async def list_pii_entities_detection_jobs(
        self,
        request: ComprehendListPiiEntitiesDetectionJobsRequest | None = None,
    ) -> ComprehendListPiiEntitiesDetectionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_pii_entities_detection_jobs, request, ComprehendListPiiEntitiesDetectionJobsResponse)

    async def list_pii_entities_detection_jobs_paginated(
        self,
        request: ComprehendListPiiEntitiesDetectionJobsRequest | None = None,
    ) -> list[ComprehendListPiiEntitiesDetectionJobsResponse]:
        return await self._paginate('list_pii_entities_detection_jobs', request, ComprehendListPiiEntitiesDetectionJobsResponse)

    async def list_sentiment_detection_jobs(
        self,
        request: ComprehendListSentimentDetectionJobsRequest | None = None,
    ) -> ComprehendListSentimentDetectionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_sentiment_detection_jobs, request, ComprehendListSentimentDetectionJobsResponse)

    async def list_sentiment_detection_jobs_paginated(
        self,
        request: ComprehendListSentimentDetectionJobsRequest | None = None,
    ) -> list[ComprehendListSentimentDetectionJobsResponse]:
        return await self._paginate('list_sentiment_detection_jobs', request, ComprehendListSentimentDetectionJobsResponse)

    async def list_tags_for_resource(
        self,
        request: ComprehendListTagsForResourceRequest,
    ) -> ComprehendListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, ComprehendListTagsForResourceResponse)

    async def list_targeted_sentiment_detection_jobs(
        self,
        request: ComprehendListTargetedSentimentDetectionJobsRequest | None = None,
    ) -> ComprehendListTargetedSentimentDetectionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_targeted_sentiment_detection_jobs, request, ComprehendListTargetedSentimentDetectionJobsResponse)

    async def list_topics_detection_jobs(
        self,
        request: ComprehendListTopicsDetectionJobsRequest | None = None,
    ) -> ComprehendListTopicsDetectionJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_topics_detection_jobs, request, ComprehendListTopicsDetectionJobsResponse)

    async def list_topics_detection_jobs_paginated(
        self,
        request: ComprehendListTopicsDetectionJobsRequest | None = None,
    ) -> list[ComprehendListTopicsDetectionJobsResponse]:
        return await self._paginate('list_topics_detection_jobs', request, ComprehendListTopicsDetectionJobsResponse)

    async def put_resource_policy(
        self,
        request: ComprehendPutResourcePolicyRequest,
    ) -> ComprehendPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, ComprehendPutResourcePolicyResponse)

    async def start_document_classification_job(
        self,
        request: ComprehendStartDocumentClassificationJobRequest,
    ) -> ComprehendStartDocumentClassificationJobResponse:
        client = self._require_client()
        return await self._execute(client.start_document_classification_job, request, ComprehendStartDocumentClassificationJobResponse)

    async def start_dominant_language_detection_job(
        self,
        request: ComprehendStartDominantLanguageDetectionJobRequest,
    ) -> ComprehendStartDominantLanguageDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.start_dominant_language_detection_job, request, ComprehendStartDominantLanguageDetectionJobResponse)

    async def start_entities_detection_job(
        self,
        request: ComprehendStartEntitiesDetectionJobRequest,
    ) -> ComprehendStartEntitiesDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.start_entities_detection_job, request, ComprehendStartEntitiesDetectionJobResponse)

    async def start_events_detection_job(
        self,
        request: ComprehendStartEventsDetectionJobRequest,
    ) -> ComprehendStartEventsDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.start_events_detection_job, request, ComprehendStartEventsDetectionJobResponse)

    async def start_flywheel_iteration(
        self,
        request: ComprehendStartFlywheelIterationRequest,
    ) -> ComprehendStartFlywheelIterationResponse:
        client = self._require_client()
        return await self._execute(client.start_flywheel_iteration, request, ComprehendStartFlywheelIterationResponse)

    async def start_key_phrases_detection_job(
        self,
        request: ComprehendStartKeyPhrasesDetectionJobRequest,
    ) -> ComprehendStartKeyPhrasesDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.start_key_phrases_detection_job, request, ComprehendStartKeyPhrasesDetectionJobResponse)

    async def start_pii_entities_detection_job(
        self,
        request: ComprehendStartPiiEntitiesDetectionJobRequest,
    ) -> ComprehendStartPiiEntitiesDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.start_pii_entities_detection_job, request, ComprehendStartPiiEntitiesDetectionJobResponse)

    async def start_sentiment_detection_job(
        self,
        request: ComprehendStartSentimentDetectionJobRequest,
    ) -> ComprehendStartSentimentDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.start_sentiment_detection_job, request, ComprehendStartSentimentDetectionJobResponse)

    async def start_targeted_sentiment_detection_job(
        self,
        request: ComprehendStartTargetedSentimentDetectionJobRequest,
    ) -> ComprehendStartTargetedSentimentDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.start_targeted_sentiment_detection_job, request, ComprehendStartTargetedSentimentDetectionJobResponse)

    async def start_topics_detection_job(
        self,
        request: ComprehendStartTopicsDetectionJobRequest,
    ) -> ComprehendStartTopicsDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.start_topics_detection_job, request, ComprehendStartTopicsDetectionJobResponse)

    async def stop_dominant_language_detection_job(
        self,
        request: ComprehendStopDominantLanguageDetectionJobRequest,
    ) -> ComprehendStopDominantLanguageDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_dominant_language_detection_job, request, ComprehendStopDominantLanguageDetectionJobResponse)

    async def stop_entities_detection_job(
        self,
        request: ComprehendStopEntitiesDetectionJobRequest,
    ) -> ComprehendStopEntitiesDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_entities_detection_job, request, ComprehendStopEntitiesDetectionJobResponse)

    async def stop_events_detection_job(
        self,
        request: ComprehendStopEventsDetectionJobRequest,
    ) -> ComprehendStopEventsDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_events_detection_job, request, ComprehendStopEventsDetectionJobResponse)

    async def stop_key_phrases_detection_job(
        self,
        request: ComprehendStopKeyPhrasesDetectionJobRequest,
    ) -> ComprehendStopKeyPhrasesDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_key_phrases_detection_job, request, ComprehendStopKeyPhrasesDetectionJobResponse)

    async def stop_pii_entities_detection_job(
        self,
        request: ComprehendStopPiiEntitiesDetectionJobRequest,
    ) -> ComprehendStopPiiEntitiesDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_pii_entities_detection_job, request, ComprehendStopPiiEntitiesDetectionJobResponse)

    async def stop_sentiment_detection_job(
        self,
        request: ComprehendStopSentimentDetectionJobRequest,
    ) -> ComprehendStopSentimentDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_sentiment_detection_job, request, ComprehendStopSentimentDetectionJobResponse)

    async def stop_targeted_sentiment_detection_job(
        self,
        request: ComprehendStopTargetedSentimentDetectionJobRequest,
    ) -> ComprehendStopTargetedSentimentDetectionJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_targeted_sentiment_detection_job, request, ComprehendStopTargetedSentimentDetectionJobResponse)

    async def stop_training_document_classifier(
        self,
        request: ComprehendStopTrainingDocumentClassifierRequest,
    ) -> ComprehendStopTrainingDocumentClassifierResponse:
        client = self._require_client()
        return await self._execute(client.stop_training_document_classifier, request, ComprehendStopTrainingDocumentClassifierResponse)

    async def stop_training_entity_recognizer(
        self,
        request: ComprehendStopTrainingEntityRecognizerRequest,
    ) -> ComprehendStopTrainingEntityRecognizerResponse:
        client = self._require_client()
        return await self._execute(client.stop_training_entity_recognizer, request, ComprehendStopTrainingEntityRecognizerResponse)

    async def tag_resource(
        self,
        request: ComprehendTagResourceRequest,
    ) -> ComprehendTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, ComprehendTagResourceResponse)

    async def untag_resource(
        self,
        request: ComprehendUntagResourceRequest,
    ) -> ComprehendUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, ComprehendUntagResourceResponse)

    async def update_endpoint(
        self,
        request: ComprehendUpdateEndpointRequest,
    ) -> ComprehendUpdateEndpointResponse:
        client = self._require_client()
        return await self._execute(client.update_endpoint, request, ComprehendUpdateEndpointResponse)

    async def update_flywheel(
        self,
        request: ComprehendUpdateFlywheelRequest,
    ) -> ComprehendUpdateFlywheelResponse:
        client = self._require_client()
        return await self._execute(client.update_flywheel, request, ComprehendUpdateFlywheelResponse)
