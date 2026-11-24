from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class EKSClient(ABC):

    @abstractmethod
    def list_clusters(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        include: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster(
        self,
        *,
        name: str,
        roleArn: str,
        resourcesVpcConfig: dict[str, Any],
        version: str | None = None,
        kubernetesNetworkConfig: dict[str, Any] | None = None,
        logging: dict[str, Any] | None = None,
        clientRequestToken: str | None = None,
        tags: dict[str, str] | None = None,
        encryptionConfig: list[dict[str, Any]] | None = None,
        outpostConfig: dict[str, Any] | None = None,
        accessConfig: dict[str, Any] | None = None,
        bootstrapSelfManagedAddons: bool | None = None,
        upgradePolicy: dict[str, Any] | None = None,
        zonalShiftConfig: dict[str, Any] | None = None,
        remoteNetworkConfig: dict[str, Any] | None = None,
        computeConfig: dict[str, Any] | None = None,
        storageConfig: dict[str, Any] | None = None,
        deletionProtection: bool | None = None,
        controlPlaneScalingConfig: dict[str, Any] | None = None,
        kubeApiServerConfig: dict[str, Any] | None = None,
        kubeSchedulerConfig: dict[str, Any] | None = None,
        kubeControllerManagerConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster_config(
        self,
        *,
        name: str,
        resourcesVpcConfig: dict[str, Any] | None = None,
        logging: dict[str, Any] | None = None,
        clientRequestToken: str | None = None,
        accessConfig: dict[str, Any] | None = None,
        upgradePolicy: dict[str, Any] | None = None,
        zonalShiftConfig: dict[str, Any] | None = None,
        computeConfig: dict[str, Any] | None = None,
        kubernetesNetworkConfig: dict[str, Any] | None = None,
        storageConfig: dict[str, Any] | None = None,
        remoteNetworkConfig: dict[str, Any] | None = None,
        deletionProtection: bool | None = None,
        controlPlaneScalingConfig: dict[str, Any] | None = None,
        kubeApiServerConfig: dict[str, Any] | None = None,
        kubeSchedulerConfig: dict[str, Any] | None = None,
        kubeControllerManagerConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster_version(
        self,
        *,
        name: str,
        version: str,
        clientRequestToken: str | None = None,
        force: bool | None = None,
        rollbackConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_nodegroups(
        self,
        *,
        clusterName: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_nodegroup(
        self,
        *,
        clusterName: str,
        nodegroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_nodegroup(
        self,
        *,
        clusterName: str,
        nodegroupName: str,
        subnets: list[str],
        nodeRole: str,
        scalingConfig: dict[str, Any] | None = None,
        diskSize: int | None = None,
        instanceTypes: list[str] | None = None,
        amiType: str | None = None,
        remoteAccess: dict[str, Any] | None = None,
        labels: dict[str, str] | None = None,
        taints: list[dict[str, Any]] | None = None,
        tags: dict[str, str] | None = None,
        clientRequestToken: str | None = None,
        launchTemplate: dict[str, Any] | None = None,
        updateConfig: dict[str, Any] | None = None,
        nodeRepairConfig: dict[str, Any] | None = None,
        capacityType: str | None = None,
        version: str | None = None,
        releaseVersion: str | None = None,
        warmPoolConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_nodegroup_config(
        self,
        *,
        clusterName: str,
        nodegroupName: str,
        labels: dict[str, Any] | None = None,
        taints: dict[str, Any] | None = None,
        scalingConfig: dict[str, Any] | None = None,
        updateConfig: dict[str, Any] | None = None,
        nodeRepairConfig: dict[str, Any] | None = None,
        warmPoolConfig: dict[str, Any] | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_nodegroup_version(
        self,
        *,
        clusterName: str,
        nodegroupName: str,
        version: str | None = None,
        releaseVersion: str | None = None,
        launchTemplate: dict[str, Any] | None = None,
        force: bool | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_nodegroup(
        self,
        *,
        clusterName: str,
        nodegroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_fargate_profiles(
        self,
        *,
        clusterName: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fargate_profile(
        self,
        *,
        clusterName: str,
        fargateProfileName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_fargate_profile(
        self,
        *,
        fargateProfileName: str,
        clusterName: str,
        podExecutionRoleArn: str,
        subnets: list[str] | None = None,
        selectors: list[dict[str, Any]] | None = None,
        clientRequestToken: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_fargate_profile(
        self,
        *,
        clusterName: str,
        fargateProfileName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_addons(
        self,
        *,
        clusterName: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_addon(
        self,
        *,
        clusterName: str,
        addonName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_addon(
        self,
        *,
        clusterName: str,
        addonName: str,
        addonVersion: str | None = None,
        serviceAccountRoleArn: str | None = None,
        resolveConflicts: str | None = None,
        clientRequestToken: str | None = None,
        tags: dict[str, str] | None = None,
        configurationValues: str | None = None,
        podIdentityAssociations: list[dict[str, Any]] | None = None,
        namespaceConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_addon(
        self,
        *,
        clusterName: str,
        addonName: str,
        addonVersion: str | None = None,
        serviceAccountRoleArn: str | None = None,
        resolveConflicts: str | None = None,
        clientRequestToken: str | None = None,
        configurationValues: str | None = None,
        podIdentityAssociations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_addon(
        self,
        *,
        clusterName: str,
        addonName: str,
        preserve: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_updates(
        self,
        *,
        name: str,
        nodegroupName: str | None = None,
        addonName: str | None = None,
        capabilityName: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_update(
        self,
        *,
        name: str,
        updateId: str,
        nodegroupName: str | None = None,
        addonName: str | None = None,
        capabilityName: str | None = None,
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
    def activate_certificate_authority(
        self,
        *,
        clusterName: str,
        certificateAuthorityId: str,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_access_policy(
        self,
        *,
        clusterName: str,
        principalArn: str,
        policyArn: str,
        accessScope: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_encryption_config(
        self,
        *,
        clusterName: str,
        encryptionConfig: list[dict[str, Any]],
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_identity_provider_config(
        self,
        *,
        clusterName: str,
        oidc: dict[str, Any],
        tags: dict[str, str] | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_update(
        self,
        *,
        name: str,
        updateId: str,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_access_entry(
        self,
        *,
        clusterName: str,
        principalArn: str,
        kubernetesGroups: list[str] | None = None,
        tags: dict[str, str] | None = None,
        clientRequestToken: str | None = None,
        username: str | None = None,
        type: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_capability(
        self,
        *,
        capabilityName: str,
        clusterName: str,
        type: str,
        roleArn: str,
        deletePropagationPolicy: str,
        clientRequestToken: str | None = None,
        configuration: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_certificate_authority(
        self,
        *,
        clusterName: str,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_eks_anywhere_subscription(
        self,
        *,
        name: str,
        term: dict[str, Any],
        licenseQuantity: int | None = None,
        licenseType: str | None = None,
        autoRenew: bool | None = None,
        clientRequestToken: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_pod_identity_association(
        self,
        *,
        clusterName: str,
        namespace: str,
        serviceAccount: str,
        roleArn: str,
        clientRequestToken: str | None = None,
        tags: dict[str, str] | None = None,
        disableSessionTags: bool | None = None,
        targetRoleArn: str | None = None,
        policy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_access_entry(
        self,
        *,
        clusterName: str,
        principalArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_capability(
        self,
        *,
        clusterName: str,
        capabilityName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_certificate_authority(
        self,
        *,
        clusterName: str,
        certificateAuthorityId: str,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_eks_anywhere_subscription(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_pod_identity_association(
        self,
        *,
        clusterName: str,
        associationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_cluster(
        self,
        *,
        name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_access_entry(
        self,
        *,
        clusterName: str,
        principalArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_addon_configuration(
        self,
        *,
        addonName: str,
        addonVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_addon_versions(
        self,
        *,
        kubernetesVersion: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        addonName: str | None = None,
        types: list[str] | None = None,
        publishers: list[str] | None = None,
        owners: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capability(
        self,
        *,
        clusterName: str,
        capabilityName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_certificate_authority(
        self,
        *,
        clusterName: str,
        certificateAuthorityId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_versions(
        self,
        *,
        clusterType: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        defaultOnly: bool | None = None,
        includeAll: bool | None = None,
        clusterVersions: list[str] | None = None,
        status: str | None = None,
        versionStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_eks_anywhere_subscription(
        self,
        *,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_identity_provider_config(
        self,
        *,
        clusterName: str,
        identityProviderConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_insight(
        self,
        *,
        clusterName: str,
        id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_insights_refresh(
        self,
        *,
        clusterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pod_identity_association(
        self,
        *,
        clusterName: str,
        associationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_access_policy(
        self,
        *,
        clusterName: str,
        principalArn: str,
        policyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_identity_provider_config(
        self,
        *,
        clusterName: str,
        identityProviderConfig: dict[str, Any],
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_access_entries(
        self,
        *,
        clusterName: str,
        associatedPolicyArn: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_access_policies(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_associated_access_policies(
        self,
        *,
        clusterName: str,
        principalArn: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_capabilities(
        self,
        *,
        clusterName: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_certificate_authorities(
        self,
        *,
        clusterName: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_eks_anywhere_subscriptions(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        includeStatus: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_identity_provider_configs(
        self,
        *,
        clusterName: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_insights(
        self,
        *,
        clusterName: str,
        filter: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pod_identity_associations(
        self,
        *,
        clusterName: str,
        namespace: str | None = None,
        serviceAccount: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_cluster(
        self,
        *,
        name: str,
        connectorConfig: dict[str, Any],
        clientRequestToken: str | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_insights_refresh(
        self,
        *,
        clusterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_access_entry(
        self,
        *,
        clusterName: str,
        principalArn: str,
        kubernetesGroups: list[str] | None = None,
        clientRequestToken: str | None = None,
        username: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_capability(
        self,
        *,
        clusterName: str,
        capabilityName: str,
        roleArn: str | None = None,
        configuration: dict[str, Any] | None = None,
        clientRequestToken: str | None = None,
        deletePropagationPolicy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_eks_anywhere_subscription(
        self,
        *,
        id: str,
        autoRenew: bool,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pod_identity_association(
        self,
        *,
        clusterName: str,
        associationId: str,
        roleArn: str | None = None,
        clientRequestToken: str | None = None,
        disableSessionTags: bool | None = None,
        targetRoleArn: str | None = None,
        policy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
