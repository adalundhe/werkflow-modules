from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class DataZoneClient(ABC):

    @abstractmethod
    def accept_predictions(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        revision: str | None = None,
        acceptRule: dict[str, Any] | None = None,
        acceptChoices: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_subscription_request(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        decisionComment: str | None = None,
        assetScopes: list[dict[str, Any]] | None = None,
        assetPermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_entity_owner(
        self,
        *,
        domainIdentifier: str,
        entityType: str,
        entityIdentifier: str,
        owner: dict[str, Any],
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_policy_grant(
        self,
        *,
        domainIdentifier: str,
        entityType: str,
        entityIdentifier: str,
        policyType: str,
        principal: dict[str, Any],
        detail: dict[str, Any],
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_environment_role(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        environmentRoleArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_governed_terms(
        self,
        *,
        domainIdentifier: str,
        entityIdentifier: str,
        entityType: str,
        governedGlossaryTerms: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_attributes_metadata(
        self,
        *,
        domainIdentifier: str,
        entityType: str,
        entityIdentifier: str,
        attributeIdentifiers: list[str],
        entityRevision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_put_attributes_metadata(
        self,
        *,
        domainIdentifier: str,
        entityType: str,
        entityIdentifier: str,
        attributes: list[dict[str, Any]],
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_metadata_generation_run(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_subscription(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_account_pool(
        self,
        *,
        domainIdentifier: str,
        name: str,
        resolutionStrategy: str,
        accountSource: dict[str, Any],
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_asset(
        self,
        *,
        name: str,
        domainIdentifier: str,
        typeIdentifier: str,
        owningProjectIdentifier: str,
        externalIdentifier: str | None = None,
        typeRevision: str | None = None,
        description: str | None = None,
        glossaryTerms: list[str] | None = None,
        formsInput: list[dict[str, Any]] | None = None,
        predictionConfiguration: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_asset_filter(
        self,
        *,
        domainIdentifier: str,
        assetIdentifier: str,
        name: str,
        configuration: dict[str, Any],
        description: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_asset_revision(
        self,
        *,
        name: str,
        domainIdentifier: str,
        identifier: str,
        typeRevision: str | None = None,
        description: str | None = None,
        glossaryTerms: list[str] | None = None,
        formsInput: list[dict[str, Any]] | None = None,
        predictionConfiguration: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_asset_type(
        self,
        *,
        domainIdentifier: str,
        name: str,
        formsInput: dict[str, dict[str, Any]],
        owningProjectIdentifier: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_connection(
        self,
        *,
        domainIdentifier: str,
        name: str,
        awsLocation: dict[str, Any] | None = None,
        clientToken: str | None = None,
        configurations: list[dict[str, Any]] | None = None,
        description: str | None = None,
        environmentIdentifier: str | None = None,
        props: dict[str, Any] | None = None,
        enableTrustedIdentityPropagation: bool | None = None,
        scope: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_product(
        self,
        *,
        domainIdentifier: str,
        name: str,
        owningProjectIdentifier: str,
        description: str | None = None,
        glossaryTerms: list[str] | None = None,
        formsInput: list[dict[str, Any]] | None = None,
        items: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_product_revision(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str,
        description: str | None = None,
        glossaryTerms: list[str] | None = None,
        items: list[dict[str, Any]] | None = None,
        formsInput: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_source(
        self,
        *,
        name: str,
        domainIdentifier: str,
        projectIdentifier: str,
        type: str,
        description: str | None = None,
        environmentIdentifier: str | None = None,
        connectionIdentifier: str | None = None,
        configuration: dict[str, Any] | None = None,
        recommendation: dict[str, Any] | None = None,
        enableSetting: str | None = None,
        schedule: dict[str, Any] | None = None,
        publishOnImport: bool | None = None,
        assetFormsInput: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_designation(
        self,
        *,
        domainIdentifier: str,
        name: str,
        policy: str,
        description: str | None = None,
        deletionProtection: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain(
        self,
        *,
        name: str,
        description: str | None = None,
        singleSignOn: dict[str, Any] | None = None,
        domainExecutionRole: str | None = None,
        kmsKeyIdentifier: str | None = None,
        tags: dict[str, str] | None = None,
        domainVersion: str | None = None,
        serviceRole: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain_unit(
        self,
        *,
        domainIdentifier: str,
        name: str,
        parentDomainUnitIdentifier: str,
        description: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_environment(
        self,
        *,
        projectIdentifier: str,
        domainIdentifier: str,
        name: str,
        description: str | None = None,
        environmentProfileIdentifier: str | None = None,
        userParameters: list[dict[str, Any]] | None = None,
        glossaryTerms: list[str] | None = None,
        environmentAccountIdentifier: str | None = None,
        environmentAccountRegion: str | None = None,
        environmentBlueprintIdentifier: str | None = None,
        deploymentOrder: int | None = None,
        environmentConfigurationId: str | None = None,
        environmentConfigurationName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_environment_action(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        name: str,
        parameters: dict[str, Any],
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_environment_blueprint(
        self,
        *,
        domainIdentifier: str,
        name: str,
        provisioningProperties: dict[str, Any],
        description: str | None = None,
        userParameters: list[dict[str, Any]] | None = None,
        blueprintCategory: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_environment_profile(
        self,
        *,
        domainIdentifier: str,
        name: str,
        environmentBlueprintIdentifier: str,
        projectIdentifier: str,
        description: str | None = None,
        userParameters: list[dict[str, Any]] | None = None,
        awsAccountId: str | None = None,
        awsAccountRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_form_type(
        self,
        *,
        domainIdentifier: str,
        name: str,
        model: dict[str, Any],
        owningProjectIdentifier: str,
        status: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_glossary(
        self,
        *,
        domainIdentifier: str,
        name: str,
        owningProjectIdentifier: str,
        description: str | None = None,
        status: str | None = None,
        usageRestrictions: list[str] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_glossary_term(
        self,
        *,
        domainIdentifier: str,
        glossaryIdentifier: str,
        name: str,
        status: str | None = None,
        shortDescription: str | None = None,
        longDescription: str | None = None,
        termRelations: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_group_profile(
        self,
        *,
        domainIdentifier: str,
        groupIdentifier: str | None = None,
        rolePrincipalArn: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_listing_change_set(
        self,
        *,
        domainIdentifier: str,
        entityIdentifier: str,
        entityType: str,
        action: str,
        entityRevision: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_notebook(
        self,
        *,
        domainIdentifier: str,
        owningProjectIdentifier: str,
        name: str,
        description: str | None = None,
        type: str | None = None,
        metadata: dict[str, str] | None = None,
        parameters: dict[str, str] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_project(
        self,
        *,
        domainIdentifier: str,
        name: str,
        description: str | None = None,
        resourceTags: dict[str, str] | None = None,
        glossaryTerms: list[str] | None = None,
        domainUnitId: str | None = None,
        projectProfileId: str | None = None,
        userParameters: list[dict[str, Any]] | None = None,
        projectCategory: str | None = None,
        projectExecutionRole: str | None = None,
        membershipAssignments: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_project_membership(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        member: dict[str, Any],
        designation: str,
        userCreatedDesignationId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_project_profile(
        self,
        *,
        domainIdentifier: str,
        name: str,
        description: str | None = None,
        status: str | None = None,
        projectResourceTags: list[dict[str, Any]] | None = None,
        allowCustomProjectResourceTags: bool | None = None,
        projectResourceTagsDescription: str | None = None,
        environmentConfigurations: list[dict[str, Any]] | None = None,
        domainUnitIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_rule(
        self,
        *,
        domainIdentifier: str,
        name: str,
        target: dict[str, Any],
        action: str,
        scope: dict[str, Any],
        detail: dict[str, Any],
        description: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_subscription_grant(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        grantedEntity: dict[str, Any],
        subscriptionTargetIdentifier: str | None = None,
        assetTargetNames: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_subscription_request(
        self,
        *,
        domainIdentifier: str,
        subscribedPrincipals: list[dict[str, Any]],
        subscribedListings: list[dict[str, Any]],
        requestReason: str,
        clientToken: str | None = None,
        metadataForms: list[dict[str, Any]] | None = None,
        assetPermissions: list[dict[str, Any]] | None = None,
        assetScopes: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_subscription_target(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        name: str,
        type: str,
        subscriptionTargetConfig: list[dict[str, Any]],
        authorizedPrincipals: list[str],
        manageAccessRole: str,
        applicableAssetTypes: list[str],
        provider: str | None = None,
        clientToken: str | None = None,
        subscriptionGrantCreationMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user_profile(
        self,
        *,
        domainIdentifier: str,
        userIdentifier: str,
        userType: str | None = None,
        sessionName: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_pool(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_asset(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_asset_filter(
        self,
        *,
        domainIdentifier: str,
        assetIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_asset_type(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_connection(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_export_configuration(
        self,
        *,
        domainIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_product(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_source(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        clientToken: str | None = None,
        retainPermissionsOnRevokeFailure: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_designation(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain(
        self,
        *,
        identifier: str,
        clientToken: str | None = None,
        skipDeletionCheck: bool | None = None,
        cascadeDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain_unit(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_environment(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_environment_action(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_environment_blueprint(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_environment_blueprint_configuration(
        self,
        *,
        domainIdentifier: str,
        environmentBlueprintIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_environment_profile(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_form_type(
        self,
        *,
        domainIdentifier: str,
        formTypeIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_glossary(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_glossary_term(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_lineage_event(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_listing(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_notebook(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_project(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        skipDeletionCheck: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_project_membership(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        member: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_project_profile(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_rule(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_subscription_grant(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_subscription_request(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_subscription_target(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_time_series_data_points(
        self,
        *,
        domainIdentifier: str,
        entityIdentifier: str,
        entityType: str,
        formName: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_environment_role(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        environmentRoleArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_governed_terms(
        self,
        *,
        domainIdentifier: str,
        entityIdentifier: str,
        entityType: str,
        governedGlossaryTerms: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_pool(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_asset(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        revision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_asset_filter(
        self,
        *,
        domainIdentifier: str,
        assetIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_asset_type(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        revision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connection(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        withSecret: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_export_configuration(
        self,
        *,
        domainIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_product(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        revision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_source(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_source_run(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_designation(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain(
        self,
        *,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_unit(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_environment(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_environment_action(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_environment_blueprint(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_environment_blueprint_configuration(
        self,
        *,
        domainIdentifier: str,
        environmentBlueprintIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_environment_credentials(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_environment_profile(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_form_type(
        self,
        *,
        domainIdentifier: str,
        formTypeIdentifier: str,
        revision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_glossary(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_glossary_term(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_group_profile(
        self,
        *,
        domainIdentifier: str,
        groupIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_iam_portal_login_url(
        self,
        *,
        domainIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_job_run(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lineage_event(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lineage_node(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        eventTimestamp: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_listing(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        listingRevision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_metadata_generation_run(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        type: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_notebook(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_notebook_export(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_notebook_run(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_project(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_project_profile(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_rule(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        revision: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_subscription(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_subscription_grant(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_subscription_request_details(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_subscription_target(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_time_series_data_point(
        self,
        *,
        domainIdentifier: str,
        entityIdentifier: str,
        entityType: str,
        identifier: str,
        formName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_profile(
        self,
        *,
        domainIdentifier: str,
        userIdentifier: str,
        type: str | None = None,
        sessionName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_account_pools(
        self,
        *,
        domainIdentifier: str,
        name: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_accounts_in_account_pool(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_asset_filters(
        self,
        *,
        domainIdentifier: str,
        assetIdentifier: str,
        status: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_asset_revisions(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_connections(
        self,
        *,
        domainIdentifier: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        name: str | None = None,
        environmentIdentifier: str | None = None,
        projectIdentifier: str | None = None,
        type: str | None = None,
        scope: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_product_revisions(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_source_run_activities(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        status: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_source_runs(
        self,
        *,
        domainIdentifier: str,
        dataSourceIdentifier: str,
        status: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_sources(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        environmentIdentifier: str | None = None,
        connectionIdentifier: str | None = None,
        type: str | None = None,
        status: str | None = None,
        name: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_designations(
        self,
        *,
        domainIdentifier: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domain_units_for_parent(
        self,
        *,
        domainIdentifier: str,
        parentDomainUnitIdentifier: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domains(
        self,
        *,
        status: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_entity_owners(
        self,
        *,
        domainIdentifier: str,
        entityType: str,
        entityIdentifier: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_environment_actions(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_environment_blueprint_configurations(
        self,
        *,
        domainIdentifier: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_environment_blueprints(
        self,
        *,
        domainIdentifier: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
        name: str | None = None,
        managed: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_environment_profiles(
        self,
        *,
        domainIdentifier: str,
        awsAccountId: str | None = None,
        awsAccountRegion: str | None = None,
        environmentBlueprintIdentifier: str | None = None,
        projectIdentifier: str | None = None,
        name: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_environments(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        awsAccountId: str | None = None,
        status: str | None = None,
        awsAccountRegion: str | None = None,
        environmentProfileIdentifier: str | None = None,
        environmentBlueprintIdentifier: str | None = None,
        provider: str | None = None,
        name: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_job_runs(
        self,
        *,
        domainIdentifier: str,
        jobIdentifier: str,
        status: str | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_lineage_events(
        self,
        *,
        domainIdentifier: str,
        maxResults: int | None = None,
        timestampAfter: datetime.datetime | str | None = None,
        timestampBefore: datetime.datetime | str | None = None,
        processingStatus: str | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_lineage_node_history(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
        direction: str | None = None,
        eventTimestampGTE: datetime.datetime | str | None = None,
        eventTimestampLTE: datetime.datetime | str | None = None,
        sortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_metadata_generation_runs(
        self,
        *,
        domainIdentifier: str,
        status: str | None = None,
        type: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        targetIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notebook_runs(
        self,
        *,
        domainIdentifier: str,
        owningProjectIdentifier: str,
        notebookIdentifier: str | None = None,
        status: str | None = None,
        scheduleIdentifier: str | None = None,
        maxResults: int | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notebooks(
        self,
        *,
        domainIdentifier: str,
        owningProjectIdentifier: str,
        maxResults: int | None = None,
        sortOrder: str | None = None,
        sortBy: str | None = None,
        status: str | None = None,
        type: str | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notifications(
        self,
        *,
        domainIdentifier: str,
        type: str,
        afterTimestamp: datetime.datetime | str | None = None,
        beforeTimestamp: datetime.datetime | str | None = None,
        subjects: list[str] | None = None,
        taskStatus: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policy_grants(
        self,
        *,
        domainIdentifier: str,
        entityType: str,
        entityIdentifier: str,
        policyType: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_project_memberships(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_project_profiles(
        self,
        *,
        domainIdentifier: str,
        name: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_projects(
        self,
        *,
        domainIdentifier: str,
        userIdentifier: str | None = None,
        groupIdentifier: str | None = None,
        name: str | None = None,
        projectCategory: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_rules(
        self,
        *,
        domainIdentifier: str,
        targetType: str,
        targetIdentifier: str,
        ruleType: str | None = None,
        action: str | None = None,
        projectIds: list[str] | None = None,
        assetTypes: list[str] | None = None,
        dataProduct: bool | None = None,
        includeCascaded: bool | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_subscription_grants(
        self,
        *,
        domainIdentifier: str,
        environmentId: str | None = None,
        subscriptionTargetId: str | None = None,
        subscribedListingId: str | None = None,
        subscriptionId: str | None = None,
        owningProjectId: str | None = None,
        owningIamPrincipalArn: str | None = None,
        owningUserId: str | None = None,
        owningGroupId: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_subscription_requests(
        self,
        *,
        domainIdentifier: str,
        status: str | None = None,
        subscribedListingId: str | None = None,
        owningProjectId: str | None = None,
        owningIamPrincipalArn: str | None = None,
        approverProjectId: str | None = None,
        owningUserId: str | None = None,
        owningGroupId: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_subscription_targets(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_subscriptions(
        self,
        *,
        domainIdentifier: str,
        subscriptionRequestIdentifier: str | None = None,
        status: str | None = None,
        subscribedListingId: str | None = None,
        owningProjectId: str | None = None,
        owningIamPrincipalArn: str | None = None,
        owningUserId: str | None = None,
        owningGroupId: str | None = None,
        approverProjectId: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
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
    def list_time_series_data_points(
        self,
        *,
        domainIdentifier: str,
        entityIdentifier: str,
        entityType: str,
        formName: str,
        startedAt: datetime.datetime | str | None = None,
        endedAt: datetime.datetime | str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def post_lineage_event(
        self,
        *,
        domainIdentifier: str,
        event: bytes | BinaryIO | str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def post_time_series_data_points(
        self,
        *,
        domainIdentifier: str,
        entityIdentifier: str,
        entityType: str,
        forms: list[dict[str, Any]],
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_data_export_configuration(
        self,
        *,
        domainIdentifier: str,
        enableExport: bool,
        encryptionConfiguration: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_environment_blueprint_configuration(
        self,
        *,
        domainIdentifier: str,
        environmentBlueprintIdentifier: str,
        enabledRegions: list[str],
        provisioningRoleArn: str | None = None,
        manageAccessRoleArn: str | None = None,
        environmentRolePermissionBoundary: str | None = None,
        regionalParameters: dict[str, dict[str, str]] | None = None,
        resourceConfigurations: list[dict[str, Any]] | None = None,
        allowUserProvidedConfigurations: bool | None = None,
        globalParameters: dict[str, str] | None = None,
        provisioningConfigurations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def query_graph(
        self,
        *,
        domainIdentifier: str,
        match: list[dict[str, Any]],
        maxResults: int | None = None,
        nextToken: str | None = None,
        additionalAttributes: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_predictions(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        revision: str | None = None,
        rejectRule: dict[str, Any] | None = None,
        rejectChoices: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_subscription_request(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        decisionComment: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_entity_owner(
        self,
        *,
        domainIdentifier: str,
        entityType: str,
        entityIdentifier: str,
        owner: dict[str, Any],
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_policy_grant(
        self,
        *,
        domainIdentifier: str,
        entityType: str,
        entityIdentifier: str,
        policyType: str,
        principal: dict[str, Any],
        grantIdentifier: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_subscription(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        retainPermissions: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search(
        self,
        *,
        domainIdentifier: str,
        searchScope: str,
        owningProjectIdentifier: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        searchText: str | None = None,
        searchIn: list[dict[str, Any]] | None = None,
        filters: dict[str, Any] | None = None,
        sort: dict[str, Any] | None = None,
        additionalAttributes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_group_profiles(
        self,
        *,
        domainIdentifier: str,
        groupType: str,
        searchText: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_listings(
        self,
        *,
        domainIdentifier: str,
        searchText: str | None = None,
        searchIn: list[dict[str, Any]] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        filters: dict[str, Any] | None = None,
        aggregations: list[dict[str, Any]] | None = None,
        sort: dict[str, Any] | None = None,
        additionalAttributes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_types(
        self,
        *,
        domainIdentifier: str,
        searchScope: str,
        managed: bool,
        maxResults: int | None = None,
        nextToken: str | None = None,
        searchText: str | None = None,
        searchIn: list[dict[str, Any]] | None = None,
        filters: dict[str, Any] | None = None,
        sort: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_user_profiles(
        self,
        *,
        domainIdentifier: str,
        userType: str,
        searchText: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_data_source_run(
        self,
        *,
        domainIdentifier: str,
        dataSourceIdentifier: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_metadata_generation_run(
        self,
        *,
        domainIdentifier: str,
        target: dict[str, Any],
        owningProjectIdentifier: str,
        type: str | None = None,
        types: list[str] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_notebook_export(
        self,
        *,
        domainIdentifier: str,
        notebookIdentifier: str,
        owningProjectIdentifier: str,
        fileFormat: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_notebook_import(
        self,
        *,
        domainIdentifier: str,
        owningProjectIdentifier: str,
        sourceLocation: dict[str, Any],
        name: str,
        description: str | None = None,
        type: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_notebook_run(
        self,
        *,
        domainIdentifier: str,
        owningProjectIdentifier: str,
        notebookIdentifier: str,
        scheduleIdentifier: str | None = None,
        computeConfiguration: dict[str, Any] | None = None,
        networkConfiguration: dict[str, Any] | None = None,
        timeoutConfiguration: dict[str, Any] | None = None,
        notificationConfiguration: dict[str, Any] | None = None,
        triggerSource: dict[str, Any] | None = None,
        metadata: dict[str, str] | None = None,
        parameters: dict[str, str] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_notebook_sync(
        self,
        *,
        domainIdentifier: str,
        owningProjectIdentifier: str,
        sourceLocation: dict[str, Any],
        gitMetadata: dict[str, Any] | None = None,
        notebookId: str | None = None,
        name: str | None = None,
        description: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_notebook_run(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        clientToken: str | None = None,
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
    def update_account_pool(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str | None = None,
        description: str | None = None,
        resolutionStrategy: str | None = None,
        accountSource: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_asset_filter(
        self,
        *,
        domainIdentifier: str,
        assetIdentifier: str,
        identifier: str,
        name: str | None = None,
        description: str | None = None,
        configuration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_asset_owner(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        targetProjectIdentifier: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_connection(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        configurations: list[dict[str, Any]] | None = None,
        description: str | None = None,
        awsLocation: dict[str, Any] | None = None,
        props: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_source(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str | None = None,
        description: str | None = None,
        enableSetting: str | None = None,
        publishOnImport: bool | None = None,
        assetFormsInput: list[dict[str, Any]] | None = None,
        schedule: dict[str, Any] | None = None,
        configuration: dict[str, Any] | None = None,
        recommendation: dict[str, Any] | None = None,
        retainPermissionsOnRevokeFailure: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_designation(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str | None = None,
        description: str | None = None,
        policy: str | None = None,
        deletionProtection: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain(
        self,
        *,
        identifier: str,
        description: str | None = None,
        singleSignOn: dict[str, Any] | None = None,
        domainExecutionRole: str | None = None,
        serviceRole: str | None = None,
        name: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_unit(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        description: str | None = None,
        name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_environment(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str | None = None,
        description: str | None = None,
        glossaryTerms: list[str] | None = None,
        blueprintVersion: str | None = None,
        userParameters: list[dict[str, Any]] | None = None,
        environmentConfigurationName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_environment_action(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        identifier: str,
        parameters: dict[str, Any] | None = None,
        name: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_environment_blueprint(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        description: str | None = None,
        provisioningProperties: dict[str, Any] | None = None,
        userParameters: list[dict[str, Any]] | None = None,
        blueprintCategory: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_environment_profile(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str | None = None,
        description: str | None = None,
        userParameters: list[dict[str, Any]] | None = None,
        awsAccountId: str | None = None,
        awsAccountRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_glossary(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str | None = None,
        description: str | None = None,
        status: str | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_glossary_term(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        glossaryIdentifier: str | None = None,
        name: str | None = None,
        shortDescription: str | None = None,
        longDescription: str | None = None,
        termRelations: dict[str, Any] | None = None,
        status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_group_profile(
        self,
        *,
        domainIdentifier: str,
        groupIdentifier: str,
        status: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_notebook(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        description: str | None = None,
        status: str | None = None,
        name: str | None = None,
        cellOrder: list[dict[str, Any]] | None = None,
        type: str | None = None,
        metadata: dict[str, str] | None = None,
        parameters: dict[str, str] | None = None,
        environmentConfiguration: dict[str, Any] | None = None,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_project(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str | None = None,
        description: str | None = None,
        resourceTags: dict[str, str] | None = None,
        glossaryTerms: list[str] | None = None,
        domainUnitId: str | None = None,
        environmentDeploymentDetails: dict[str, Any] | None = None,
        userParameters: list[dict[str, Any]] | None = None,
        projectProfileVersion: str | None = None,
        projectProfileAction: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_project_profile(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str | None = None,
        description: str | None = None,
        status: str | None = None,
        projectResourceTags: list[dict[str, Any]] | None = None,
        allowCustomProjectResourceTags: bool | None = None,
        projectResourceTagsDescription: str | None = None,
        environmentConfigurations: list[dict[str, Any]] | None = None,
        domainUnitIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_root_domain_unit_owner(
        self,
        *,
        domainIdentifier: str,
        currentOwner: str,
        newOwner: str,
        clientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_rule(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str | None = None,
        description: str | None = None,
        scope: dict[str, Any] | None = None,
        detail: dict[str, Any] | None = None,
        includeChildDomainUnits: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_subscription_grant_status(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        assetIdentifier: str,
        status: str,
        failureCause: dict[str, Any] | None = None,
        targetName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_subscription_request(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        requestReason: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_subscription_target(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        identifier: str,
        name: str | None = None,
        authorizedPrincipals: list[str] | None = None,
        applicableAssetTypes: list[str] | None = None,
        subscriptionTargetConfig: list[dict[str, Any]] | None = None,
        manageAccessRole: str | None = None,
        provider: str | None = None,
        subscriptionGrantCreationMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_profile(
        self,
        *,
        domainIdentifier: str,
        userIdentifier: str,
        status: str,
        type: str | None = None,
        sessionName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
