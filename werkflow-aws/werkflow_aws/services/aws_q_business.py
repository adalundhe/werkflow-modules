from werkflow_aws.models.q_business import (
    QBusinessAssociatePermissionRequest,
    QBusinessAssociatePermissionResponse,
    QBusinessBatchDeleteDocumentRequest,
    QBusinessBatchDeleteDocumentResponse,
    QBusinessBatchPutDocumentRequest,
    QBusinessBatchPutDocumentResponse,
    QBusinessCancelSubscriptionRequest,
    QBusinessCancelSubscriptionResponse,
    QBusinessChatRequest,
    QBusinessChatResponse,
    QBusinessChatSyncRequest,
    QBusinessChatSyncResponse,
    QBusinessCheckDocumentAccessRequest,
    QBusinessCheckDocumentAccessResponse,
    QBusinessCreateAnonymousWebExperienceUrlRequest,
    QBusinessCreateAnonymousWebExperienceUrlResponse,
    QBusinessCreateApplicationRequest,
    QBusinessCreateApplicationResponse,
    QBusinessCreateChatResponseConfigurationRequest,
    QBusinessCreateChatResponseConfigurationResponse,
    QBusinessCreateDataAccessorRequest,
    QBusinessCreateDataAccessorResponse,
    QBusinessCreateDataSourceRequest,
    QBusinessCreateDataSourceResponse,
    QBusinessCreateIndexRequest,
    QBusinessCreateIndexResponse,
    QBusinessCreatePluginRequest,
    QBusinessCreatePluginResponse,
    QBusinessCreateRetrieverRequest,
    QBusinessCreateRetrieverResponse,
    QBusinessCreateSubscriptionRequest,
    QBusinessCreateSubscriptionResponse,
    QBusinessCreateUserRequest,
    QBusinessCreateUserResponse,
    QBusinessCreateWebExperienceRequest,
    QBusinessCreateWebExperienceResponse,
    QBusinessDeleteApplicationRequest,
    QBusinessDeleteApplicationResponse,
    QBusinessDeleteAttachmentRequest,
    QBusinessDeleteAttachmentResponse,
    QBusinessDeleteChatControlsConfigurationRequest,
    QBusinessDeleteChatControlsConfigurationResponse,
    QBusinessDeleteChatResponseConfigurationRequest,
    QBusinessDeleteChatResponseConfigurationResponse,
    QBusinessDeleteConversationRequest,
    QBusinessDeleteConversationResponse,
    QBusinessDeleteDataAccessorRequest,
    QBusinessDeleteDataAccessorResponse,
    QBusinessDeleteDataSourceRequest,
    QBusinessDeleteDataSourceResponse,
    QBusinessDeleteGroupRequest,
    QBusinessDeleteGroupResponse,
    QBusinessDeleteIndexRequest,
    QBusinessDeleteIndexResponse,
    QBusinessDeletePluginRequest,
    QBusinessDeletePluginResponse,
    QBusinessDeleteRetrieverRequest,
    QBusinessDeleteRetrieverResponse,
    QBusinessDeleteUserRequest,
    QBusinessDeleteUserResponse,
    QBusinessDeleteWebExperienceRequest,
    QBusinessDeleteWebExperienceResponse,
    QBusinessDisassociatePermissionRequest,
    QBusinessDisassociatePermissionResponse,
    QBusinessGetApplicationRequest,
    QBusinessGetApplicationResponse,
    QBusinessGetChatControlsConfigurationRequest,
    QBusinessGetChatControlsConfigurationResponse,
    QBusinessGetChatResponseConfigurationRequest,
    QBusinessGetChatResponseConfigurationResponse,
    QBusinessGetDataAccessorRequest,
    QBusinessGetDataAccessorResponse,
    QBusinessGetDataSourceRequest,
    QBusinessGetDataSourceResponse,
    QBusinessGetDocumentContentRequest,
    QBusinessGetDocumentContentResponse,
    QBusinessGetGroupRequest,
    QBusinessGetGroupResponse,
    QBusinessGetIndexRequest,
    QBusinessGetIndexResponse,
    QBusinessGetMediaRequest,
    QBusinessGetMediaResponse,
    QBusinessGetPluginRequest,
    QBusinessGetPluginResponse,
    QBusinessGetPolicyRequest,
    QBusinessGetPolicyResponse,
    QBusinessGetRetrieverRequest,
    QBusinessGetRetrieverResponse,
    QBusinessGetUserRequest,
    QBusinessGetUserResponse,
    QBusinessGetWebExperienceRequest,
    QBusinessGetWebExperienceResponse,
    QBusinessListApplicationsRequest,
    QBusinessListApplicationsResponse,
    QBusinessListAttachmentsRequest,
    QBusinessListAttachmentsResponse,
    QBusinessListChatResponseConfigurationsRequest,
    QBusinessListChatResponseConfigurationsResponse,
    QBusinessListConversationsRequest,
    QBusinessListConversationsResponse,
    QBusinessListDataAccessorsRequest,
    QBusinessListDataAccessorsResponse,
    QBusinessListDataSourceSyncJobsRequest,
    QBusinessListDataSourceSyncJobsResponse,
    QBusinessListDataSourcesRequest,
    QBusinessListDataSourcesResponse,
    QBusinessListDocumentsRequest,
    QBusinessListDocumentsResponse,
    QBusinessListGroupsRequest,
    QBusinessListGroupsResponse,
    QBusinessListIndicesRequest,
    QBusinessListIndicesResponse,
    QBusinessListMessagesRequest,
    QBusinessListMessagesResponse,
    QBusinessListPluginActionsRequest,
    QBusinessListPluginActionsResponse,
    QBusinessListPluginTypeActionsRequest,
    QBusinessListPluginTypeActionsResponse,
    QBusinessListPluginTypeMetadataRequest,
    QBusinessListPluginTypeMetadataResponse,
    QBusinessListPluginsRequest,
    QBusinessListPluginsResponse,
    QBusinessListRetrieversRequest,
    QBusinessListRetrieversResponse,
    QBusinessListSubscriptionsRequest,
    QBusinessListSubscriptionsResponse,
    QBusinessListTagsForResourceRequest,
    QBusinessListTagsForResourceResponse,
    QBusinessListWebExperiencesRequest,
    QBusinessListWebExperiencesResponse,
    QBusinessPutFeedbackRequest,
    QBusinessPutFeedbackResponse,
    QBusinessPutGroupRequest,
    QBusinessPutGroupResponse,
    QBusinessSearchRelevantContentRequest,
    QBusinessSearchRelevantContentResponse,
    QBusinessStartDataSourceSyncJobRequest,
    QBusinessStartDataSourceSyncJobResponse,
    QBusinessStopDataSourceSyncJobRequest,
    QBusinessStopDataSourceSyncJobResponse,
    QBusinessTagResourceRequest,
    QBusinessTagResourceResponse,
    QBusinessUntagResourceRequest,
    QBusinessUntagResourceResponse,
    QBusinessUpdateApplicationRequest,
    QBusinessUpdateApplicationResponse,
    QBusinessUpdateChatControlsConfigurationRequest,
    QBusinessUpdateChatControlsConfigurationResponse,
    QBusinessUpdateChatResponseConfigurationRequest,
    QBusinessUpdateChatResponseConfigurationResponse,
    QBusinessUpdateDataAccessorRequest,
    QBusinessUpdateDataAccessorResponse,
    QBusinessUpdateDataSourceRequest,
    QBusinessUpdateDataSourceResponse,
    QBusinessUpdateIndexRequest,
    QBusinessUpdateIndexResponse,
    QBusinessUpdatePluginRequest,
    QBusinessUpdatePluginResponse,
    QBusinessUpdateRetrieverRequest,
    QBusinessUpdateRetrieverResponse,
    QBusinessUpdateSubscriptionRequest,
    QBusinessUpdateSubscriptionResponse,
    QBusinessUpdateUserRequest,
    QBusinessUpdateUserResponse,
    QBusinessUpdateWebExperienceRequest,
    QBusinessUpdateWebExperienceResponse,
)
from werkflow_aws.types.q_business_client import QBusinessClient
from .base import AWSBaseService


class AWSQBusiness(AWSBaseService[QBusinessClient]):
    service_name = 'q'
    boto3_service_name = 'qbusiness'

    def __init__(self) -> None:
        super().__init__(service_name='q', boto3_service_name='qbusiness')

    async def associate_permission(
        self,
        request: QBusinessAssociatePermissionRequest,
    ) -> QBusinessAssociatePermissionResponse:
        client = self._require_client()
        return await self._execute(client.associate_permission, request, QBusinessAssociatePermissionResponse)

    async def batch_delete_document(
        self,
        request: QBusinessBatchDeleteDocumentRequest,
    ) -> QBusinessBatchDeleteDocumentResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_document, request, QBusinessBatchDeleteDocumentResponse)

    async def batch_put_document(
        self,
        request: QBusinessBatchPutDocumentRequest,
    ) -> QBusinessBatchPutDocumentResponse:
        client = self._require_client()
        return await self._execute(client.batch_put_document, request, QBusinessBatchPutDocumentResponse)

    async def cancel_subscription(
        self,
        request: QBusinessCancelSubscriptionRequest,
    ) -> QBusinessCancelSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.cancel_subscription, request, QBusinessCancelSubscriptionResponse)

    async def chat(
        self,
        request: QBusinessChatRequest,
    ) -> QBusinessChatResponse:
        client = self._require_client()
        return await self._execute(client.chat, request, QBusinessChatResponse)

    async def chat_sync(
        self,
        request: QBusinessChatSyncRequest,
    ) -> QBusinessChatSyncResponse:
        client = self._require_client()
        return await self._execute(client.chat_sync, request, QBusinessChatSyncResponse)

    async def check_document_access(
        self,
        request: QBusinessCheckDocumentAccessRequest,
    ) -> QBusinessCheckDocumentAccessResponse:
        client = self._require_client()
        return await self._execute(client.check_document_access, request, QBusinessCheckDocumentAccessResponse)

    async def create_anonymous_web_experience_url(
        self,
        request: QBusinessCreateAnonymousWebExperienceUrlRequest,
    ) -> QBusinessCreateAnonymousWebExperienceUrlResponse:
        client = self._require_client()
        return await self._execute(client.create_anonymous_web_experience_url, request, QBusinessCreateAnonymousWebExperienceUrlResponse)

    async def create_application(
        self,
        request: QBusinessCreateApplicationRequest,
    ) -> QBusinessCreateApplicationResponse:
        client = self._require_client()
        return await self._execute(client.create_application, request, QBusinessCreateApplicationResponse)

    async def create_chat_response_configuration(
        self,
        request: QBusinessCreateChatResponseConfigurationRequest,
    ) -> QBusinessCreateChatResponseConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_chat_response_configuration, request, QBusinessCreateChatResponseConfigurationResponse)

    async def create_data_accessor(
        self,
        request: QBusinessCreateDataAccessorRequest,
    ) -> QBusinessCreateDataAccessorResponse:
        client = self._require_client()
        return await self._execute(client.create_data_accessor, request, QBusinessCreateDataAccessorResponse)

    async def create_data_source(
        self,
        request: QBusinessCreateDataSourceRequest,
    ) -> QBusinessCreateDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.create_data_source, request, QBusinessCreateDataSourceResponse)

    async def create_index(
        self,
        request: QBusinessCreateIndexRequest,
    ) -> QBusinessCreateIndexResponse:
        client = self._require_client()
        return await self._execute(client.create_index, request, QBusinessCreateIndexResponse)

    async def create_plugin(
        self,
        request: QBusinessCreatePluginRequest,
    ) -> QBusinessCreatePluginResponse:
        client = self._require_client()
        return await self._execute(client.create_plugin, request, QBusinessCreatePluginResponse)

    async def create_retriever(
        self,
        request: QBusinessCreateRetrieverRequest,
    ) -> QBusinessCreateRetrieverResponse:
        client = self._require_client()
        return await self._execute(client.create_retriever, request, QBusinessCreateRetrieverResponse)

    async def create_subscription(
        self,
        request: QBusinessCreateSubscriptionRequest,
    ) -> QBusinessCreateSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_subscription, request, QBusinessCreateSubscriptionResponse)

    async def create_user(
        self,
        request: QBusinessCreateUserRequest,
    ) -> QBusinessCreateUserResponse:
        client = self._require_client()
        return await self._execute(client.create_user, request, QBusinessCreateUserResponse)

    async def create_web_experience(
        self,
        request: QBusinessCreateWebExperienceRequest,
    ) -> QBusinessCreateWebExperienceResponse:
        client = self._require_client()
        return await self._execute(client.create_web_experience, request, QBusinessCreateWebExperienceResponse)

    async def delete_application(
        self,
        request: QBusinessDeleteApplicationRequest,
    ) -> QBusinessDeleteApplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_application, request, QBusinessDeleteApplicationResponse)

    async def delete_attachment(
        self,
        request: QBusinessDeleteAttachmentRequest,
    ) -> QBusinessDeleteAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_attachment, request, QBusinessDeleteAttachmentResponse)

    async def delete_chat_controls_configuration(
        self,
        request: QBusinessDeleteChatControlsConfigurationRequest,
    ) -> QBusinessDeleteChatControlsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_chat_controls_configuration, request, QBusinessDeleteChatControlsConfigurationResponse)

    async def delete_chat_response_configuration(
        self,
        request: QBusinessDeleteChatResponseConfigurationRequest,
    ) -> QBusinessDeleteChatResponseConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_chat_response_configuration, request, QBusinessDeleteChatResponseConfigurationResponse)

    async def delete_conversation(
        self,
        request: QBusinessDeleteConversationRequest,
    ) -> QBusinessDeleteConversationResponse:
        client = self._require_client()
        return await self._execute(client.delete_conversation, request, QBusinessDeleteConversationResponse)

    async def delete_data_accessor(
        self,
        request: QBusinessDeleteDataAccessorRequest,
    ) -> QBusinessDeleteDataAccessorResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_accessor, request, QBusinessDeleteDataAccessorResponse)

    async def delete_data_source(
        self,
        request: QBusinessDeleteDataSourceRequest,
    ) -> QBusinessDeleteDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_source, request, QBusinessDeleteDataSourceResponse)

    async def delete_group(
        self,
        request: QBusinessDeleteGroupRequest,
    ) -> QBusinessDeleteGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_group, request, QBusinessDeleteGroupResponse)

    async def delete_index(
        self,
        request: QBusinessDeleteIndexRequest,
    ) -> QBusinessDeleteIndexResponse:
        client = self._require_client()
        return await self._execute(client.delete_index, request, QBusinessDeleteIndexResponse)

    async def delete_plugin(
        self,
        request: QBusinessDeletePluginRequest,
    ) -> QBusinessDeletePluginResponse:
        client = self._require_client()
        return await self._execute(client.delete_plugin, request, QBusinessDeletePluginResponse)

    async def delete_retriever(
        self,
        request: QBusinessDeleteRetrieverRequest,
    ) -> QBusinessDeleteRetrieverResponse:
        client = self._require_client()
        return await self._execute(client.delete_retriever, request, QBusinessDeleteRetrieverResponse)

    async def delete_user(
        self,
        request: QBusinessDeleteUserRequest,
    ) -> QBusinessDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.delete_user, request, QBusinessDeleteUserResponse)

    async def delete_web_experience(
        self,
        request: QBusinessDeleteWebExperienceRequest,
    ) -> QBusinessDeleteWebExperienceResponse:
        client = self._require_client()
        return await self._execute(client.delete_web_experience, request, QBusinessDeleteWebExperienceResponse)

    async def disassociate_permission(
        self,
        request: QBusinessDisassociatePermissionRequest,
    ) -> QBusinessDisassociatePermissionResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_permission, request, QBusinessDisassociatePermissionResponse)

    async def get_application(
        self,
        request: QBusinessGetApplicationRequest,
    ) -> QBusinessGetApplicationResponse:
        client = self._require_client()
        return await self._execute(client.get_application, request, QBusinessGetApplicationResponse)

    async def get_chat_controls_configuration(
        self,
        request: QBusinessGetChatControlsConfigurationRequest,
    ) -> QBusinessGetChatControlsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_chat_controls_configuration, request, QBusinessGetChatControlsConfigurationResponse)

    async def get_chat_controls_configuration_paginated(
        self,
        request: QBusinessGetChatControlsConfigurationRequest,
    ) -> list[QBusinessGetChatControlsConfigurationResponse]:
        return await self._paginate('get_chat_controls_configuration', request, QBusinessGetChatControlsConfigurationResponse)

    async def get_chat_response_configuration(
        self,
        request: QBusinessGetChatResponseConfigurationRequest,
    ) -> QBusinessGetChatResponseConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_chat_response_configuration, request, QBusinessGetChatResponseConfigurationResponse)

    async def get_data_accessor(
        self,
        request: QBusinessGetDataAccessorRequest,
    ) -> QBusinessGetDataAccessorResponse:
        client = self._require_client()
        return await self._execute(client.get_data_accessor, request, QBusinessGetDataAccessorResponse)

    async def get_data_source(
        self,
        request: QBusinessGetDataSourceRequest,
    ) -> QBusinessGetDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.get_data_source, request, QBusinessGetDataSourceResponse)

    async def get_document_content(
        self,
        request: QBusinessGetDocumentContentRequest,
    ) -> QBusinessGetDocumentContentResponse:
        client = self._require_client()
        return await self._execute(client.get_document_content, request, QBusinessGetDocumentContentResponse)

    async def get_group(
        self,
        request: QBusinessGetGroupRequest,
    ) -> QBusinessGetGroupResponse:
        client = self._require_client()
        return await self._execute(client.get_group, request, QBusinessGetGroupResponse)

    async def get_index(
        self,
        request: QBusinessGetIndexRequest,
    ) -> QBusinessGetIndexResponse:
        client = self._require_client()
        return await self._execute(client.get_index, request, QBusinessGetIndexResponse)

    async def get_media(
        self,
        request: QBusinessGetMediaRequest,
    ) -> QBusinessGetMediaResponse:
        client = self._require_client()
        return await self._execute(client.get_media, request, QBusinessGetMediaResponse)

    async def get_plugin(
        self,
        request: QBusinessGetPluginRequest,
    ) -> QBusinessGetPluginResponse:
        client = self._require_client()
        return await self._execute(client.get_plugin, request, QBusinessGetPluginResponse)

    async def get_policy(
        self,
        request: QBusinessGetPolicyRequest,
    ) -> QBusinessGetPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_policy, request, QBusinessGetPolicyResponse)

    async def get_retriever(
        self,
        request: QBusinessGetRetrieverRequest,
    ) -> QBusinessGetRetrieverResponse:
        client = self._require_client()
        return await self._execute(client.get_retriever, request, QBusinessGetRetrieverResponse)

    async def get_user(
        self,
        request: QBusinessGetUserRequest,
    ) -> QBusinessGetUserResponse:
        client = self._require_client()
        return await self._execute(client.get_user, request, QBusinessGetUserResponse)

    async def get_web_experience(
        self,
        request: QBusinessGetWebExperienceRequest,
    ) -> QBusinessGetWebExperienceResponse:
        client = self._require_client()
        return await self._execute(client.get_web_experience, request, QBusinessGetWebExperienceResponse)

    async def list_applications(
        self,
        request: QBusinessListApplicationsRequest | None = None,
    ) -> QBusinessListApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.list_applications, request, QBusinessListApplicationsResponse)

    async def list_applications_paginated(
        self,
        request: QBusinessListApplicationsRequest | None = None,
    ) -> list[QBusinessListApplicationsResponse]:
        return await self._paginate('list_applications', request, QBusinessListApplicationsResponse)

    async def list_attachments(
        self,
        request: QBusinessListAttachmentsRequest,
    ) -> QBusinessListAttachmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_attachments, request, QBusinessListAttachmentsResponse)

    async def list_attachments_paginated(
        self,
        request: QBusinessListAttachmentsRequest,
    ) -> list[QBusinessListAttachmentsResponse]:
        return await self._paginate('list_attachments', request, QBusinessListAttachmentsResponse)

    async def list_chat_response_configurations(
        self,
        request: QBusinessListChatResponseConfigurationsRequest,
    ) -> QBusinessListChatResponseConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_chat_response_configurations, request, QBusinessListChatResponseConfigurationsResponse)

    async def list_chat_response_configurations_paginated(
        self,
        request: QBusinessListChatResponseConfigurationsRequest,
    ) -> list[QBusinessListChatResponseConfigurationsResponse]:
        return await self._paginate('list_chat_response_configurations', request, QBusinessListChatResponseConfigurationsResponse)

    async def list_conversations(
        self,
        request: QBusinessListConversationsRequest,
    ) -> QBusinessListConversationsResponse:
        client = self._require_client()
        return await self._execute(client.list_conversations, request, QBusinessListConversationsResponse)

    async def list_conversations_paginated(
        self,
        request: QBusinessListConversationsRequest,
    ) -> list[QBusinessListConversationsResponse]:
        return await self._paginate('list_conversations', request, QBusinessListConversationsResponse)

    async def list_data_accessors(
        self,
        request: QBusinessListDataAccessorsRequest,
    ) -> QBusinessListDataAccessorsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_accessors, request, QBusinessListDataAccessorsResponse)

    async def list_data_accessors_paginated(
        self,
        request: QBusinessListDataAccessorsRequest,
    ) -> list[QBusinessListDataAccessorsResponse]:
        return await self._paginate('list_data_accessors', request, QBusinessListDataAccessorsResponse)

    async def list_data_source_sync_jobs(
        self,
        request: QBusinessListDataSourceSyncJobsRequest,
    ) -> QBusinessListDataSourceSyncJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_source_sync_jobs, request, QBusinessListDataSourceSyncJobsResponse)

    async def list_data_source_sync_jobs_paginated(
        self,
        request: QBusinessListDataSourceSyncJobsRequest,
    ) -> list[QBusinessListDataSourceSyncJobsResponse]:
        return await self._paginate('list_data_source_sync_jobs', request, QBusinessListDataSourceSyncJobsResponse)

    async def list_data_sources(
        self,
        request: QBusinessListDataSourcesRequest,
    ) -> QBusinessListDataSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_sources, request, QBusinessListDataSourcesResponse)

    async def list_data_sources_paginated(
        self,
        request: QBusinessListDataSourcesRequest,
    ) -> list[QBusinessListDataSourcesResponse]:
        return await self._paginate('list_data_sources', request, QBusinessListDataSourcesResponse)

    async def list_documents(
        self,
        request: QBusinessListDocumentsRequest,
    ) -> QBusinessListDocumentsResponse:
        client = self._require_client()
        return await self._execute(client.list_documents, request, QBusinessListDocumentsResponse)

    async def list_documents_paginated(
        self,
        request: QBusinessListDocumentsRequest,
    ) -> list[QBusinessListDocumentsResponse]:
        return await self._paginate('list_documents', request, QBusinessListDocumentsResponse)

    async def list_groups(
        self,
        request: QBusinessListGroupsRequest,
    ) -> QBusinessListGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_groups, request, QBusinessListGroupsResponse)

    async def list_groups_paginated(
        self,
        request: QBusinessListGroupsRequest,
    ) -> list[QBusinessListGroupsResponse]:
        return await self._paginate('list_groups', request, QBusinessListGroupsResponse)

    async def list_indices(
        self,
        request: QBusinessListIndicesRequest,
    ) -> QBusinessListIndicesResponse:
        client = self._require_client()
        return await self._execute(client.list_indices, request, QBusinessListIndicesResponse)

    async def list_indices_paginated(
        self,
        request: QBusinessListIndicesRequest,
    ) -> list[QBusinessListIndicesResponse]:
        return await self._paginate('list_indices', request, QBusinessListIndicesResponse)

    async def list_messages(
        self,
        request: QBusinessListMessagesRequest,
    ) -> QBusinessListMessagesResponse:
        client = self._require_client()
        return await self._execute(client.list_messages, request, QBusinessListMessagesResponse)

    async def list_messages_paginated(
        self,
        request: QBusinessListMessagesRequest,
    ) -> list[QBusinessListMessagesResponse]:
        return await self._paginate('list_messages', request, QBusinessListMessagesResponse)

    async def list_plugin_actions(
        self,
        request: QBusinessListPluginActionsRequest,
    ) -> QBusinessListPluginActionsResponse:
        client = self._require_client()
        return await self._execute(client.list_plugin_actions, request, QBusinessListPluginActionsResponse)

    async def list_plugin_actions_paginated(
        self,
        request: QBusinessListPluginActionsRequest,
    ) -> list[QBusinessListPluginActionsResponse]:
        return await self._paginate('list_plugin_actions', request, QBusinessListPluginActionsResponse)

    async def list_plugin_type_actions(
        self,
        request: QBusinessListPluginTypeActionsRequest,
    ) -> QBusinessListPluginTypeActionsResponse:
        client = self._require_client()
        return await self._execute(client.list_plugin_type_actions, request, QBusinessListPluginTypeActionsResponse)

    async def list_plugin_type_actions_paginated(
        self,
        request: QBusinessListPluginTypeActionsRequest,
    ) -> list[QBusinessListPluginTypeActionsResponse]:
        return await self._paginate('list_plugin_type_actions', request, QBusinessListPluginTypeActionsResponse)

    async def list_plugin_type_metadata(
        self,
        request: QBusinessListPluginTypeMetadataRequest | None = None,
    ) -> QBusinessListPluginTypeMetadataResponse:
        client = self._require_client()
        return await self._execute(client.list_plugin_type_metadata, request, QBusinessListPluginTypeMetadataResponse)

    async def list_plugin_type_metadata_paginated(
        self,
        request: QBusinessListPluginTypeMetadataRequest | None = None,
    ) -> list[QBusinessListPluginTypeMetadataResponse]:
        return await self._paginate('list_plugin_type_metadata', request, QBusinessListPluginTypeMetadataResponse)

    async def list_plugins(
        self,
        request: QBusinessListPluginsRequest,
    ) -> QBusinessListPluginsResponse:
        client = self._require_client()
        return await self._execute(client.list_plugins, request, QBusinessListPluginsResponse)

    async def list_plugins_paginated(
        self,
        request: QBusinessListPluginsRequest,
    ) -> list[QBusinessListPluginsResponse]:
        return await self._paginate('list_plugins', request, QBusinessListPluginsResponse)

    async def list_retrievers(
        self,
        request: QBusinessListRetrieversRequest,
    ) -> QBusinessListRetrieversResponse:
        client = self._require_client()
        return await self._execute(client.list_retrievers, request, QBusinessListRetrieversResponse)

    async def list_retrievers_paginated(
        self,
        request: QBusinessListRetrieversRequest,
    ) -> list[QBusinessListRetrieversResponse]:
        return await self._paginate('list_retrievers', request, QBusinessListRetrieversResponse)

    async def list_subscriptions(
        self,
        request: QBusinessListSubscriptionsRequest,
    ) -> QBusinessListSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.list_subscriptions, request, QBusinessListSubscriptionsResponse)

    async def list_subscriptions_paginated(
        self,
        request: QBusinessListSubscriptionsRequest,
    ) -> list[QBusinessListSubscriptionsResponse]:
        return await self._paginate('list_subscriptions', request, QBusinessListSubscriptionsResponse)

    async def list_tags_for_resource(
        self,
        request: QBusinessListTagsForResourceRequest,
    ) -> QBusinessListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, QBusinessListTagsForResourceResponse)

    async def list_web_experiences(
        self,
        request: QBusinessListWebExperiencesRequest,
    ) -> QBusinessListWebExperiencesResponse:
        client = self._require_client()
        return await self._execute(client.list_web_experiences, request, QBusinessListWebExperiencesResponse)

    async def list_web_experiences_paginated(
        self,
        request: QBusinessListWebExperiencesRequest,
    ) -> list[QBusinessListWebExperiencesResponse]:
        return await self._paginate('list_web_experiences', request, QBusinessListWebExperiencesResponse)

    async def put_feedback(
        self,
        request: QBusinessPutFeedbackRequest,
    ) -> QBusinessPutFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.put_feedback, request, QBusinessPutFeedbackResponse)

    async def put_group(
        self,
        request: QBusinessPutGroupRequest,
    ) -> QBusinessPutGroupResponse:
        client = self._require_client()
        return await self._execute(client.put_group, request, QBusinessPutGroupResponse)

    async def search_relevant_content(
        self,
        request: QBusinessSearchRelevantContentRequest,
    ) -> QBusinessSearchRelevantContentResponse:
        client = self._require_client()
        return await self._execute(client.search_relevant_content, request, QBusinessSearchRelevantContentResponse)

    async def search_relevant_content_paginated(
        self,
        request: QBusinessSearchRelevantContentRequest,
    ) -> list[QBusinessSearchRelevantContentResponse]:
        return await self._paginate('search_relevant_content', request, QBusinessSearchRelevantContentResponse)

    async def start_data_source_sync_job(
        self,
        request: QBusinessStartDataSourceSyncJobRequest,
    ) -> QBusinessStartDataSourceSyncJobResponse:
        client = self._require_client()
        return await self._execute(client.start_data_source_sync_job, request, QBusinessStartDataSourceSyncJobResponse)

    async def stop_data_source_sync_job(
        self,
        request: QBusinessStopDataSourceSyncJobRequest,
    ) -> QBusinessStopDataSourceSyncJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_data_source_sync_job, request, QBusinessStopDataSourceSyncJobResponse)

    async def tag_resource(
        self,
        request: QBusinessTagResourceRequest,
    ) -> QBusinessTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, QBusinessTagResourceResponse)

    async def untag_resource(
        self,
        request: QBusinessUntagResourceRequest,
    ) -> QBusinessUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, QBusinessUntagResourceResponse)

    async def update_application(
        self,
        request: QBusinessUpdateApplicationRequest,
    ) -> QBusinessUpdateApplicationResponse:
        client = self._require_client()
        return await self._execute(client.update_application, request, QBusinessUpdateApplicationResponse)

    async def update_chat_controls_configuration(
        self,
        request: QBusinessUpdateChatControlsConfigurationRequest,
    ) -> QBusinessUpdateChatControlsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_chat_controls_configuration, request, QBusinessUpdateChatControlsConfigurationResponse)

    async def update_chat_response_configuration(
        self,
        request: QBusinessUpdateChatResponseConfigurationRequest,
    ) -> QBusinessUpdateChatResponseConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_chat_response_configuration, request, QBusinessUpdateChatResponseConfigurationResponse)

    async def update_data_accessor(
        self,
        request: QBusinessUpdateDataAccessorRequest,
    ) -> QBusinessUpdateDataAccessorResponse:
        client = self._require_client()
        return await self._execute(client.update_data_accessor, request, QBusinessUpdateDataAccessorResponse)

    async def update_data_source(
        self,
        request: QBusinessUpdateDataSourceRequest,
    ) -> QBusinessUpdateDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.update_data_source, request, QBusinessUpdateDataSourceResponse)

    async def update_index(
        self,
        request: QBusinessUpdateIndexRequest,
    ) -> QBusinessUpdateIndexResponse:
        client = self._require_client()
        return await self._execute(client.update_index, request, QBusinessUpdateIndexResponse)

    async def update_plugin(
        self,
        request: QBusinessUpdatePluginRequest,
    ) -> QBusinessUpdatePluginResponse:
        client = self._require_client()
        return await self._execute(client.update_plugin, request, QBusinessUpdatePluginResponse)

    async def update_retriever(
        self,
        request: QBusinessUpdateRetrieverRequest,
    ) -> QBusinessUpdateRetrieverResponse:
        client = self._require_client()
        return await self._execute(client.update_retriever, request, QBusinessUpdateRetrieverResponse)

    async def update_subscription(
        self,
        request: QBusinessUpdateSubscriptionRequest,
    ) -> QBusinessUpdateSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.update_subscription, request, QBusinessUpdateSubscriptionResponse)

    async def update_user(
        self,
        request: QBusinessUpdateUserRequest,
    ) -> QBusinessUpdateUserResponse:
        client = self._require_client()
        return await self._execute(client.update_user, request, QBusinessUpdateUserResponse)

    async def update_web_experience(
        self,
        request: QBusinessUpdateWebExperienceRequest,
    ) -> QBusinessUpdateWebExperienceResponse:
        client = self._require_client()
        return await self._execute(client.update_web_experience, request, QBusinessUpdateWebExperienceResponse)
