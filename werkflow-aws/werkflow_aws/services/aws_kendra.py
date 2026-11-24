from werkflow_aws.models.kendra import (
    KendraAssociateEntitiesToExperienceRequest,
    KendraAssociateEntitiesToExperienceResponse,
    KendraAssociatePersonasToEntitiesRequest,
    KendraAssociatePersonasToEntitiesResponse,
    KendraBatchDeleteDocumentRequest,
    KendraBatchDeleteDocumentResponse,
    KendraBatchDeleteFeaturedResultsSetRequest,
    KendraBatchDeleteFeaturedResultsSetResponse,
    KendraBatchGetDocumentStatusRequest,
    KendraBatchGetDocumentStatusResponse,
    KendraBatchPutDocumentRequest,
    KendraBatchPutDocumentResponse,
    KendraClearQuerySuggestionsRequest,
    KendraClearQuerySuggestionsResponse,
    KendraCreateAccessControlConfigurationRequest,
    KendraCreateAccessControlConfigurationResponse,
    KendraCreateDataSourceRequest,
    KendraCreateDataSourceResponse,
    KendraCreateExperienceRequest,
    KendraCreateExperienceResponse,
    KendraCreateFaqRequest,
    KendraCreateFaqResponse,
    KendraCreateFeaturedResultsSetRequest,
    KendraCreateFeaturedResultsSetResponse,
    KendraCreateIndexRequest,
    KendraCreateIndexResponse,
    KendraCreateQuerySuggestionsBlockListRequest,
    KendraCreateQuerySuggestionsBlockListResponse,
    KendraCreateThesaurusRequest,
    KendraCreateThesaurusResponse,
    KendraDeleteAccessControlConfigurationRequest,
    KendraDeleteAccessControlConfigurationResponse,
    KendraDeleteDataSourceRequest,
    KendraDeleteDataSourceResponse,
    KendraDeleteExperienceRequest,
    KendraDeleteExperienceResponse,
    KendraDeleteFaqRequest,
    KendraDeleteFaqResponse,
    KendraDeleteIndexRequest,
    KendraDeleteIndexResponse,
    KendraDeletePrincipalMappingRequest,
    KendraDeletePrincipalMappingResponse,
    KendraDeleteQuerySuggestionsBlockListRequest,
    KendraDeleteQuerySuggestionsBlockListResponse,
    KendraDeleteThesaurusRequest,
    KendraDeleteThesaurusResponse,
    KendraDescribeAccessControlConfigurationRequest,
    KendraDescribeAccessControlConfigurationResponse,
    KendraDescribeDataSourceRequest,
    KendraDescribeDataSourceResponse,
    KendraDescribeExperienceRequest,
    KendraDescribeExperienceResponse,
    KendraDescribeFaqRequest,
    KendraDescribeFaqResponse,
    KendraDescribeFeaturedResultsSetRequest,
    KendraDescribeFeaturedResultsSetResponse,
    KendraDescribeIndexRequest,
    KendraDescribeIndexResponse,
    KendraDescribePrincipalMappingRequest,
    KendraDescribePrincipalMappingResponse,
    KendraDescribeQuerySuggestionsBlockListRequest,
    KendraDescribeQuerySuggestionsBlockListResponse,
    KendraDescribeQuerySuggestionsConfigRequest,
    KendraDescribeQuerySuggestionsConfigResponse,
    KendraDescribeThesaurusRequest,
    KendraDescribeThesaurusResponse,
    KendraDisassociateEntitiesFromExperienceRequest,
    KendraDisassociateEntitiesFromExperienceResponse,
    KendraDisassociatePersonasFromEntitiesRequest,
    KendraDisassociatePersonasFromEntitiesResponse,
    KendraGetQuerySuggestionsRequest,
    KendraGetQuerySuggestionsResponse,
    KendraGetSnapshotsRequest,
    KendraGetSnapshotsResponse,
    KendraListAccessControlConfigurationsRequest,
    KendraListAccessControlConfigurationsResponse,
    KendraListDataSourceSyncJobsRequest,
    KendraListDataSourceSyncJobsResponse,
    KendraListDataSourcesRequest,
    KendraListDataSourcesResponse,
    KendraListEntityPersonasRequest,
    KendraListEntityPersonasResponse,
    KendraListExperienceEntitiesRequest,
    KendraListExperienceEntitiesResponse,
    KendraListExperiencesRequest,
    KendraListExperiencesResponse,
    KendraListFaqsRequest,
    KendraListFaqsResponse,
    KendraListFeaturedResultsSetsRequest,
    KendraListFeaturedResultsSetsResponse,
    KendraListGroupsOlderThanOrderingIdRequest,
    KendraListGroupsOlderThanOrderingIdResponse,
    KendraListIndicesRequest,
    KendraListIndicesResponse,
    KendraListQuerySuggestionsBlockListsRequest,
    KendraListQuerySuggestionsBlockListsResponse,
    KendraListTagsForResourceRequest,
    KendraListTagsForResourceResponse,
    KendraListThesauriRequest,
    KendraListThesauriResponse,
    KendraPutPrincipalMappingRequest,
    KendraPutPrincipalMappingResponse,
    KendraQueryRequest,
    KendraQueryResponse,
    KendraRetrieveRequest,
    KendraRetrieveResponse,
    KendraStartDataSourceSyncJobRequest,
    KendraStartDataSourceSyncJobResponse,
    KendraStopDataSourceSyncJobRequest,
    KendraStopDataSourceSyncJobResponse,
    KendraSubmitFeedbackRequest,
    KendraSubmitFeedbackResponse,
    KendraTagResourceRequest,
    KendraTagResourceResponse,
    KendraUntagResourceRequest,
    KendraUntagResourceResponse,
    KendraUpdateAccessControlConfigurationRequest,
    KendraUpdateAccessControlConfigurationResponse,
    KendraUpdateDataSourceRequest,
    KendraUpdateDataSourceResponse,
    KendraUpdateExperienceRequest,
    KendraUpdateExperienceResponse,
    KendraUpdateFeaturedResultsSetRequest,
    KendraUpdateFeaturedResultsSetResponse,
    KendraUpdateIndexRequest,
    KendraUpdateIndexResponse,
    KendraUpdateQuerySuggestionsBlockListRequest,
    KendraUpdateQuerySuggestionsBlockListResponse,
    KendraUpdateQuerySuggestionsConfigRequest,
    KendraUpdateQuerySuggestionsConfigResponse,
    KendraUpdateThesaurusRequest,
    KendraUpdateThesaurusResponse,
)
from werkflow_aws.types.kendra_client import KendraClient
from .base import AWSBaseService


class AWSKendra(AWSBaseService[KendraClient]):
    service_name = 'kendra'
    boto3_service_name = 'kendra'

    def __init__(self) -> None:
        super().__init__(service_name='kendra', boto3_service_name='kendra')

    async def associate_entities_to_experience(
        self,
        request: KendraAssociateEntitiesToExperienceRequest,
    ) -> KendraAssociateEntitiesToExperienceResponse:
        client = self._require_client()
        return await self._execute(client.associate_entities_to_experience, request, KendraAssociateEntitiesToExperienceResponse)

    async def associate_personas_to_entities(
        self,
        request: KendraAssociatePersonasToEntitiesRequest,
    ) -> KendraAssociatePersonasToEntitiesResponse:
        client = self._require_client()
        return await self._execute(client.associate_personas_to_entities, request, KendraAssociatePersonasToEntitiesResponse)

    async def batch_delete_document(
        self,
        request: KendraBatchDeleteDocumentRequest,
    ) -> KendraBatchDeleteDocumentResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_document, request, KendraBatchDeleteDocumentResponse)

    async def batch_delete_featured_results_set(
        self,
        request: KendraBatchDeleteFeaturedResultsSetRequest,
    ) -> KendraBatchDeleteFeaturedResultsSetResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_featured_results_set, request, KendraBatchDeleteFeaturedResultsSetResponse)

    async def batch_get_document_status(
        self,
        request: KendraBatchGetDocumentStatusRequest,
    ) -> KendraBatchGetDocumentStatusResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_document_status, request, KendraBatchGetDocumentStatusResponse)

    async def batch_put_document(
        self,
        request: KendraBatchPutDocumentRequest,
    ) -> KendraBatchPutDocumentResponse:
        client = self._require_client()
        return await self._execute(client.batch_put_document, request, KendraBatchPutDocumentResponse)

    async def clear_query_suggestions(
        self,
        request: KendraClearQuerySuggestionsRequest,
    ) -> KendraClearQuerySuggestionsResponse:
        client = self._require_client()
        return await self._execute(client.clear_query_suggestions, request, KendraClearQuerySuggestionsResponse)

    async def create_access_control_configuration(
        self,
        request: KendraCreateAccessControlConfigurationRequest,
    ) -> KendraCreateAccessControlConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_access_control_configuration, request, KendraCreateAccessControlConfigurationResponse)

    async def create_data_source(
        self,
        request: KendraCreateDataSourceRequest,
    ) -> KendraCreateDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.create_data_source, request, KendraCreateDataSourceResponse)

    async def create_experience(
        self,
        request: KendraCreateExperienceRequest,
    ) -> KendraCreateExperienceResponse:
        client = self._require_client()
        return await self._execute(client.create_experience, request, KendraCreateExperienceResponse)

    async def create_faq(
        self,
        request: KendraCreateFaqRequest,
    ) -> KendraCreateFaqResponse:
        client = self._require_client()
        return await self._execute(client.create_faq, request, KendraCreateFaqResponse)

    async def create_featured_results_set(
        self,
        request: KendraCreateFeaturedResultsSetRequest,
    ) -> KendraCreateFeaturedResultsSetResponse:
        client = self._require_client()
        return await self._execute(client.create_featured_results_set, request, KendraCreateFeaturedResultsSetResponse)

    async def create_index(
        self,
        request: KendraCreateIndexRequest,
    ) -> KendraCreateIndexResponse:
        client = self._require_client()
        return await self._execute(client.create_index, request, KendraCreateIndexResponse)

    async def create_query_suggestions_block_list(
        self,
        request: KendraCreateQuerySuggestionsBlockListRequest,
    ) -> KendraCreateQuerySuggestionsBlockListResponse:
        client = self._require_client()
        return await self._execute(client.create_query_suggestions_block_list, request, KendraCreateQuerySuggestionsBlockListResponse)

    async def create_thesaurus(
        self,
        request: KendraCreateThesaurusRequest,
    ) -> KendraCreateThesaurusResponse:
        client = self._require_client()
        return await self._execute(client.create_thesaurus, request, KendraCreateThesaurusResponse)

    async def delete_access_control_configuration(
        self,
        request: KendraDeleteAccessControlConfigurationRequest,
    ) -> KendraDeleteAccessControlConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_access_control_configuration, request, KendraDeleteAccessControlConfigurationResponse)

    async def delete_data_source(
        self,
        request: KendraDeleteDataSourceRequest,
    ) -> KendraDeleteDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_source, request, KendraDeleteDataSourceResponse)

    async def delete_experience(
        self,
        request: KendraDeleteExperienceRequest,
    ) -> KendraDeleteExperienceResponse:
        client = self._require_client()
        return await self._execute(client.delete_experience, request, KendraDeleteExperienceResponse)

    async def delete_faq(
        self,
        request: KendraDeleteFaqRequest,
    ) -> KendraDeleteFaqResponse:
        client = self._require_client()
        return await self._execute(client.delete_faq, request, KendraDeleteFaqResponse)

    async def delete_index(
        self,
        request: KendraDeleteIndexRequest,
    ) -> KendraDeleteIndexResponse:
        client = self._require_client()
        return await self._execute(client.delete_index, request, KendraDeleteIndexResponse)

    async def delete_principal_mapping(
        self,
        request: KendraDeletePrincipalMappingRequest,
    ) -> KendraDeletePrincipalMappingResponse:
        client = self._require_client()
        return await self._execute(client.delete_principal_mapping, request, KendraDeletePrincipalMappingResponse)

    async def delete_query_suggestions_block_list(
        self,
        request: KendraDeleteQuerySuggestionsBlockListRequest,
    ) -> KendraDeleteQuerySuggestionsBlockListResponse:
        client = self._require_client()
        return await self._execute(client.delete_query_suggestions_block_list, request, KendraDeleteQuerySuggestionsBlockListResponse)

    async def delete_thesaurus(
        self,
        request: KendraDeleteThesaurusRequest,
    ) -> KendraDeleteThesaurusResponse:
        client = self._require_client()
        return await self._execute(client.delete_thesaurus, request, KendraDeleteThesaurusResponse)

    async def describe_access_control_configuration(
        self,
        request: KendraDescribeAccessControlConfigurationRequest,
    ) -> KendraDescribeAccessControlConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_access_control_configuration, request, KendraDescribeAccessControlConfigurationResponse)

    async def describe_data_source(
        self,
        request: KendraDescribeDataSourceRequest,
    ) -> KendraDescribeDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_source, request, KendraDescribeDataSourceResponse)

    async def describe_experience(
        self,
        request: KendraDescribeExperienceRequest,
    ) -> KendraDescribeExperienceResponse:
        client = self._require_client()
        return await self._execute(client.describe_experience, request, KendraDescribeExperienceResponse)

    async def describe_faq(
        self,
        request: KendraDescribeFaqRequest,
    ) -> KendraDescribeFaqResponse:
        client = self._require_client()
        return await self._execute(client.describe_faq, request, KendraDescribeFaqResponse)

    async def describe_featured_results_set(
        self,
        request: KendraDescribeFeaturedResultsSetRequest,
    ) -> KendraDescribeFeaturedResultsSetResponse:
        client = self._require_client()
        return await self._execute(client.describe_featured_results_set, request, KendraDescribeFeaturedResultsSetResponse)

    async def describe_index(
        self,
        request: KendraDescribeIndexRequest,
    ) -> KendraDescribeIndexResponse:
        client = self._require_client()
        return await self._execute(client.describe_index, request, KendraDescribeIndexResponse)

    async def describe_principal_mapping(
        self,
        request: KendraDescribePrincipalMappingRequest,
    ) -> KendraDescribePrincipalMappingResponse:
        client = self._require_client()
        return await self._execute(client.describe_principal_mapping, request, KendraDescribePrincipalMappingResponse)

    async def describe_query_suggestions_block_list(
        self,
        request: KendraDescribeQuerySuggestionsBlockListRequest,
    ) -> KendraDescribeQuerySuggestionsBlockListResponse:
        client = self._require_client()
        return await self._execute(client.describe_query_suggestions_block_list, request, KendraDescribeQuerySuggestionsBlockListResponse)

    async def describe_query_suggestions_config(
        self,
        request: KendraDescribeQuerySuggestionsConfigRequest,
    ) -> KendraDescribeQuerySuggestionsConfigResponse:
        client = self._require_client()
        return await self._execute(client.describe_query_suggestions_config, request, KendraDescribeQuerySuggestionsConfigResponse)

    async def describe_thesaurus(
        self,
        request: KendraDescribeThesaurusRequest,
    ) -> KendraDescribeThesaurusResponse:
        client = self._require_client()
        return await self._execute(client.describe_thesaurus, request, KendraDescribeThesaurusResponse)

    async def disassociate_entities_from_experience(
        self,
        request: KendraDisassociateEntitiesFromExperienceRequest,
    ) -> KendraDisassociateEntitiesFromExperienceResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_entities_from_experience, request, KendraDisassociateEntitiesFromExperienceResponse)

    async def disassociate_personas_from_entities(
        self,
        request: KendraDisassociatePersonasFromEntitiesRequest,
    ) -> KendraDisassociatePersonasFromEntitiesResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_personas_from_entities, request, KendraDisassociatePersonasFromEntitiesResponse)

    async def get_query_suggestions(
        self,
        request: KendraGetQuerySuggestionsRequest,
    ) -> KendraGetQuerySuggestionsResponse:
        client = self._require_client()
        return await self._execute(client.get_query_suggestions, request, KendraGetQuerySuggestionsResponse)

    async def get_snapshots(
        self,
        request: KendraGetSnapshotsRequest,
    ) -> KendraGetSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.get_snapshots, request, KendraGetSnapshotsResponse)

    async def list_access_control_configurations(
        self,
        request: KendraListAccessControlConfigurationsRequest,
    ) -> KendraListAccessControlConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_access_control_configurations, request, KendraListAccessControlConfigurationsResponse)

    async def list_data_source_sync_jobs(
        self,
        request: KendraListDataSourceSyncJobsRequest,
    ) -> KendraListDataSourceSyncJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_source_sync_jobs, request, KendraListDataSourceSyncJobsResponse)

    async def list_data_sources(
        self,
        request: KendraListDataSourcesRequest,
    ) -> KendraListDataSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_sources, request, KendraListDataSourcesResponse)

    async def list_entity_personas(
        self,
        request: KendraListEntityPersonasRequest,
    ) -> KendraListEntityPersonasResponse:
        client = self._require_client()
        return await self._execute(client.list_entity_personas, request, KendraListEntityPersonasResponse)

    async def list_experience_entities(
        self,
        request: KendraListExperienceEntitiesRequest,
    ) -> KendraListExperienceEntitiesResponse:
        client = self._require_client()
        return await self._execute(client.list_experience_entities, request, KendraListExperienceEntitiesResponse)

    async def list_experiences(
        self,
        request: KendraListExperiencesRequest,
    ) -> KendraListExperiencesResponse:
        client = self._require_client()
        return await self._execute(client.list_experiences, request, KendraListExperiencesResponse)

    async def list_faqs(
        self,
        request: KendraListFaqsRequest,
    ) -> KendraListFaqsResponse:
        client = self._require_client()
        return await self._execute(client.list_faqs, request, KendraListFaqsResponse)

    async def list_featured_results_sets(
        self,
        request: KendraListFeaturedResultsSetsRequest,
    ) -> KendraListFeaturedResultsSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_featured_results_sets, request, KendraListFeaturedResultsSetsResponse)

    async def list_groups_older_than_ordering_id(
        self,
        request: KendraListGroupsOlderThanOrderingIdRequest,
    ) -> KendraListGroupsOlderThanOrderingIdResponse:
        client = self._require_client()
        return await self._execute(client.list_groups_older_than_ordering_id, request, KendraListGroupsOlderThanOrderingIdResponse)

    async def list_indices(
        self,
        request: KendraListIndicesRequest | None = None,
    ) -> KendraListIndicesResponse:
        client = self._require_client()
        return await self._execute(client.list_indices, request, KendraListIndicesResponse)

    async def list_query_suggestions_block_lists(
        self,
        request: KendraListQuerySuggestionsBlockListsRequest,
    ) -> KendraListQuerySuggestionsBlockListsResponse:
        client = self._require_client()
        return await self._execute(client.list_query_suggestions_block_lists, request, KendraListQuerySuggestionsBlockListsResponse)

    async def list_tags_for_resource(
        self,
        request: KendraListTagsForResourceRequest,
    ) -> KendraListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, KendraListTagsForResourceResponse)

    async def list_thesauri(
        self,
        request: KendraListThesauriRequest,
    ) -> KendraListThesauriResponse:
        client = self._require_client()
        return await self._execute(client.list_thesauri, request, KendraListThesauriResponse)

    async def put_principal_mapping(
        self,
        request: KendraPutPrincipalMappingRequest,
    ) -> KendraPutPrincipalMappingResponse:
        client = self._require_client()
        return await self._execute(client.put_principal_mapping, request, KendraPutPrincipalMappingResponse)

    async def query(
        self,
        request: KendraQueryRequest,
    ) -> KendraQueryResponse:
        client = self._require_client()
        return await self._execute(client.query, request, KendraQueryResponse)

    async def retrieve(
        self,
        request: KendraRetrieveRequest,
    ) -> KendraRetrieveResponse:
        client = self._require_client()
        return await self._execute(client.retrieve, request, KendraRetrieveResponse)

    async def start_data_source_sync_job(
        self,
        request: KendraStartDataSourceSyncJobRequest,
    ) -> KendraStartDataSourceSyncJobResponse:
        client = self._require_client()
        return await self._execute(client.start_data_source_sync_job, request, KendraStartDataSourceSyncJobResponse)

    async def stop_data_source_sync_job(
        self,
        request: KendraStopDataSourceSyncJobRequest,
    ) -> KendraStopDataSourceSyncJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_data_source_sync_job, request, KendraStopDataSourceSyncJobResponse)

    async def submit_feedback(
        self,
        request: KendraSubmitFeedbackRequest,
    ) -> KendraSubmitFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.submit_feedback, request, KendraSubmitFeedbackResponse)

    async def tag_resource(
        self,
        request: KendraTagResourceRequest,
    ) -> KendraTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, KendraTagResourceResponse)

    async def untag_resource(
        self,
        request: KendraUntagResourceRequest,
    ) -> KendraUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, KendraUntagResourceResponse)

    async def update_access_control_configuration(
        self,
        request: KendraUpdateAccessControlConfigurationRequest,
    ) -> KendraUpdateAccessControlConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_access_control_configuration, request, KendraUpdateAccessControlConfigurationResponse)

    async def update_data_source(
        self,
        request: KendraUpdateDataSourceRequest,
    ) -> KendraUpdateDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.update_data_source, request, KendraUpdateDataSourceResponse)

    async def update_experience(
        self,
        request: KendraUpdateExperienceRequest,
    ) -> KendraUpdateExperienceResponse:
        client = self._require_client()
        return await self._execute(client.update_experience, request, KendraUpdateExperienceResponse)

    async def update_featured_results_set(
        self,
        request: KendraUpdateFeaturedResultsSetRequest,
    ) -> KendraUpdateFeaturedResultsSetResponse:
        client = self._require_client()
        return await self._execute(client.update_featured_results_set, request, KendraUpdateFeaturedResultsSetResponse)

    async def update_index(
        self,
        request: KendraUpdateIndexRequest,
    ) -> KendraUpdateIndexResponse:
        client = self._require_client()
        return await self._execute(client.update_index, request, KendraUpdateIndexResponse)

    async def update_query_suggestions_block_list(
        self,
        request: KendraUpdateQuerySuggestionsBlockListRequest,
    ) -> KendraUpdateQuerySuggestionsBlockListResponse:
        client = self._require_client()
        return await self._execute(client.update_query_suggestions_block_list, request, KendraUpdateQuerySuggestionsBlockListResponse)

    async def update_query_suggestions_config(
        self,
        request: KendraUpdateQuerySuggestionsConfigRequest,
    ) -> KendraUpdateQuerySuggestionsConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_query_suggestions_config, request, KendraUpdateQuerySuggestionsConfigResponse)

    async def update_thesaurus(
        self,
        request: KendraUpdateThesaurusRequest,
    ) -> KendraUpdateThesaurusResponse:
        client = self._require_client()
        return await self._execute(client.update_thesaurus, request, KendraUpdateThesaurusResponse)
