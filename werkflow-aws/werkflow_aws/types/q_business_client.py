from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class QBusinessClient(ABC):

    @abstractmethod
    def associate_permission(
        self,
        *,
        applicationId: str,
        statementId: str,
        actions: list[str],
        principal: str,
        conditions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_document(
        self,
        *,
        applicationId: str,
        indexId: str,
        documents: list[dict[str, Any]],
        dataSourceSyncId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_put_document(
        self,
        *,
        applicationId: str,
        indexId: str,
        documents: list[dict[str, Any]],
        roleArn: str | None = None,
        dataSourceSyncId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_subscription(
        self,
        *,
        applicationId: str,
        subscriptionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def chat(
        self,
        *,
        applicationId: str,
        userId: str | None = None,
        userGroups: list[str] | None = None,
        conversationId: str | None = None,
        parentMessageId: str | None = None,
        clientToken: str | None = None,
        inputStream: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def chat_sync(
        self,
        *,
        applicationId: str,
        userId: str | None = None,
        userGroups: list[str] | None = None,
        userMessage: str | None = None,
        attachments: list[dict[str, Any]] | None = None,
        actionExecution: dict[str, Any] | None = None,
        authChallengeResponse: dict[str, Any] | None = None,
        conversationId: str | None = None,
        parentMessageId: str | None = None,
        attributeFilter: dict[str, Any] | None = None,
        chatMode: str | None = None,
        chatModeConfiguration: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def check_document_access(
        self,
        *,
        applicationId: str,
        indexId: str,
        userId: str,
        documentId: str,
        dataSourceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_anonymous_web_experience_url(
        self,
        *,
        applicationId: str,
        webExperienceId: str,
        sessionDurationInMinutes: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_application(
        self,
        *,
        displayName: str,
        roleArn: str | None = None,
        identityType: str | None = None,
        iamIdentityProviderArn: str | None = None,
        identityCenterInstanceArn: str | None = None,
        clientIdsForOIDC: list[str] | None = None,
        description: str | None = None,
        encryptionConfiguration: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
        attachmentsConfiguration: dict[str, Any] | None = None,
        qAppsConfiguration: dict[str, Any] | None = None,
        personalizationConfiguration: dict[str, Any] | None = None,
        quickSightConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_chat_response_configuration(
        self,
        *,
        applicationId: str,
        displayName: str,
        responseConfigurations: dict[str, dict[str, Any]],
        clientToken: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_accessor(
        self,
        *,
        applicationId: str,
        principal: str,
        actionConfigurations: list[dict[str, Any]],
        displayName: str,
        clientToken: str | None = None,
        authenticationDetail: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_source(
        self,
        *,
        applicationId: str,
        indexId: str,
        displayName: str,
        configuration: dict[str, Any],
        vpcConfiguration: dict[str, Any] | None = None,
        description: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        syncSchedule: str | None = None,
        roleArn: str | None = None,
        clientToken: str | None = None,
        documentEnrichmentConfiguration: dict[str, Any] | None = None,
        mediaExtractionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_index(
        self,
        *,
        applicationId: str,
        displayName: str,
        description: str | None = None,
        type: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        capacityConfiguration: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_plugin(
        self,
        *,
        applicationId: str,
        displayName: str,
        type: str,
        authConfiguration: dict[str, Any],
        serverUrl: str | None = None,
        customPluginConfiguration: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_retriever(
        self,
        *,
        applicationId: str,
        type: str,
        displayName: str,
        configuration: dict[str, Any],
        roleArn: str | None = None,
        clientToken: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_subscription(
        self,
        *,
        applicationId: str,
        principal: dict[str, Any],
        type: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user(
        self,
        *,
        applicationId: str,
        userId: str,
        userAliases: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_web_experience(
        self,
        *,
        applicationId: str,
        title: str | None = None,
        subtitle: str | None = None,
        welcomeMessage: str | None = None,
        samplePromptsControlMode: str | None = None,
        origins: list[str] | None = None,
        roleArn: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
        identityProviderConfiguration: dict[str, Any] | None = None,
        browserExtensionConfiguration: dict[str, Any] | None = None,
        customizationConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application(
        self,
        *,
        applicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_attachment(
        self,
        *,
        applicationId: str,
        conversationId: str,
        attachmentId: str,
        userId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_chat_controls_configuration(
        self,
        *,
        applicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_chat_response_configuration(
        self,
        *,
        applicationId: str,
        chatResponseConfigurationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_conversation(
        self,
        *,
        conversationId: str,
        applicationId: str,
        userId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_accessor(
        self,
        *,
        applicationId: str,
        dataAccessorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_source(
        self,
        *,
        applicationId: str,
        indexId: str,
        dataSourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_group(
        self,
        *,
        applicationId: str,
        indexId: str,
        groupName: str,
        dataSourceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_index(
        self,
        *,
        applicationId: str,
        indexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_plugin(
        self,
        *,
        applicationId: str,
        pluginId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_retriever(
        self,
        *,
        applicationId: str,
        retrieverId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        applicationId: str,
        userId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_web_experience(
        self,
        *,
        applicationId: str,
        webExperienceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_permission(
        self,
        *,
        applicationId: str,
        statementId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_application(
        self,
        *,
        applicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_chat_controls_configuration(
        self,
        *,
        applicationId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_chat_response_configuration(
        self,
        *,
        applicationId: str,
        chatResponseConfigurationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_accessor(
        self,
        *,
        applicationId: str,
        dataAccessorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_source(
        self,
        *,
        applicationId: str,
        indexId: str,
        dataSourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_document_content(
        self,
        *,
        applicationId: str,
        indexId: str,
        documentId: str,
        dataSourceId: str | None = None,
        outputFormat: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_group(
        self,
        *,
        applicationId: str,
        indexId: str,
        groupName: str,
        dataSourceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_index(
        self,
        *,
        applicationId: str,
        indexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_media(
        self,
        *,
        applicationId: str,
        conversationId: str,
        messageId: str,
        mediaId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_plugin(
        self,
        *,
        applicationId: str,
        pluginId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy(
        self,
        *,
        applicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_retriever(
        self,
        *,
        applicationId: str,
        retrieverId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user(
        self,
        *,
        applicationId: str,
        userId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_web_experience(
        self,
        *,
        applicationId: str,
        webExperienceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_applications(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_attachments(
        self,
        *,
        applicationId: str,
        conversationId: str | None = None,
        userId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_chat_response_configurations(
        self,
        *,
        applicationId: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_conversations(
        self,
        *,
        applicationId: str,
        userId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_accessors(
        self,
        *,
        applicationId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_source_sync_jobs(
        self,
        *,
        dataSourceId: str,
        applicationId: str,
        indexId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
        startTime: datetime.datetime | str | None = None,
        endTime: datetime.datetime | str | None = None,
        statusFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_sources(
        self,
        *,
        applicationId: str,
        indexId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_documents(
        self,
        *,
        applicationId: str,
        indexId: str,
        dataSourceIds: list[str] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_groups(
        self,
        *,
        applicationId: str,
        indexId: str,
        updatedEarlierThan: datetime.datetime | str,
        dataSourceId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_indices(
        self,
        *,
        applicationId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_messages(
        self,
        *,
        conversationId: str,
        applicationId: str,
        userId: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_plugin_actions(
        self,
        *,
        applicationId: str,
        pluginId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_plugin_type_actions(
        self,
        *,
        pluginType: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_plugin_type_metadata(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_plugins(
        self,
        *,
        applicationId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_retrievers(
        self,
        *,
        applicationId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_subscriptions(
        self,
        *,
        applicationId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_web_experiences(
        self,
        *,
        applicationId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_feedback(
        self,
        *,
        applicationId: str,
        conversationId: str,
        messageId: str,
        userId: str | None = None,
        messageCopiedAt: datetime.datetime | str | None = None,
        messageUsefulness: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_group(
        self,
        *,
        applicationId: str,
        indexId: str,
        groupName: str,
        type: str,
        groupMembers: dict[str, Any],
        dataSourceId: str | None = None,
        roleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_relevant_content(
        self,
        *,
        applicationId: str,
        queryText: str,
        contentSource: dict[str, Any],
        attributeFilter: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_data_source_sync_job(
        self,
        *,
        dataSourceId: str,
        applicationId: str,
        indexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_data_source_sync_job(
        self,
        *,
        dataSourceId: str,
        applicationId: str,
        indexId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceARN: str,
        tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceARN: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_application(
        self,
        *,
        applicationId: str,
        identityCenterInstanceArn: str | None = None,
        displayName: str | None = None,
        description: str | None = None,
        roleArn: str | None = None,
        attachmentsConfiguration: dict[str, Any] | None = None,
        qAppsConfiguration: dict[str, Any] | None = None,
        personalizationConfiguration: dict[str, Any] | None = None,
        autoSubscriptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_chat_controls_configuration(
        self,
        *,
        applicationId: str,
        clientToken: str | None = None,
        responseScope: str | None = None,
        orchestrationConfiguration: dict[str, Any] | None = None,
        blockedPhrasesConfigurationUpdate: dict[str, Any] | None = None,
        topicConfigurationsToCreateOrUpdate: list[dict[str, Any]] | None = None,
        topicConfigurationsToDelete: list[dict[str, Any]] | None = None,
        creatorModeConfiguration: dict[str, Any] | None = None,
        hallucinationReductionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_chat_response_configuration(
        self,
        *,
        applicationId: str,
        chatResponseConfigurationId: str,
        responseConfigurations: dict[str, dict[str, Any]],
        displayName: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_accessor(
        self,
        *,
        applicationId: str,
        dataAccessorId: str,
        actionConfigurations: list[dict[str, Any]],
        authenticationDetail: dict[str, Any] | None = None,
        displayName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_source(
        self,
        *,
        applicationId: str,
        indexId: str,
        dataSourceId: str,
        displayName: str | None = None,
        configuration: dict[str, Any] | None = None,
        vpcConfiguration: dict[str, Any] | None = None,
        description: str | None = None,
        syncSchedule: str | None = None,
        roleArn: str | None = None,
        documentEnrichmentConfiguration: dict[str, Any] | None = None,
        mediaExtractionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_index(
        self,
        *,
        applicationId: str,
        indexId: str,
        displayName: str | None = None,
        description: str | None = None,
        capacityConfiguration: dict[str, Any] | None = None,
        documentAttributeConfigurations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_plugin(
        self,
        *,
        applicationId: str,
        pluginId: str,
        displayName: str | None = None,
        state: str | None = None,
        serverUrl: str | None = None,
        customPluginConfiguration: dict[str, Any] | None = None,
        authConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_retriever(
        self,
        *,
        applicationId: str,
        retrieverId: str,
        configuration: dict[str, Any] | None = None,
        displayName: str | None = None,
        roleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_subscription(
        self,
        *,
        applicationId: str,
        subscriptionId: str,
        type: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user(
        self,
        *,
        applicationId: str,
        userId: str,
        userAliasesToUpdate: list[dict[str, Any]] | None = None,
        userAliasesToDelete: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_web_experience(
        self,
        *,
        applicationId: str,
        webExperienceId: str,
        roleArn: str | None = None,
        authenticationConfiguration: dict[str, Any] | None = None,
        title: str | None = None,
        subtitle: str | None = None,
        welcomeMessage: str | None = None,
        samplePromptsControlMode: str | None = None,
        identityProviderConfiguration: dict[str, Any] | None = None,
        origins: list[str] | None = None,
        browserExtensionConfiguration: dict[str, Any] | None = None,
        customizationConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
