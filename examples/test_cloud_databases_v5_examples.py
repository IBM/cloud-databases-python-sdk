# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Examples for CloudDatabasesV5
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_cloud_databases.cloud_databases_v5 import *

#
# This file provides an example of how to use the Cloud Databases service.
#
# The following configuration properties are assumed to be defined:
# CLOUD_DATABASES_URL=<service base url>
# CLOUD_DATABASES_AUTH_TYPE=iam
# CLOUD_DATABASES_APIKEY=<IAM apikey>
# CLOUD_DATABASES_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'cloud_databases_v5.env'

cloud_databases_service = None

config = None

# Variables to hold link values
task_id_link = None


##############################################################################
# Start of Examples for Service: CloudDatabasesV5
##############################################################################
# region
class TestCloudDatabasesV5Examples():
    """
    Example Test Class for CloudDatabasesV5
    """

    @classmethod
    def setup_class(cls):
        global cloud_databases_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            cloud_databases_service = CloudDatabasesV5.new_instance(
            )

            # end-common
            assert cloud_databases_service is not None

            # Load the configuration
            global config
            config = read_external_sources(CloudDatabasesV5.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_add_allowlist_entry_example(self):
        """
        add_allowlist_entry request example
        """
        try:
            # begin-addAllowlistEntry

            allowlist_entry_model = {
                'address': '172.16.0.0/16',
                'description': 'Dev IP space 3'
            }

            add_allowlist_entry_response = cloud_databases_service.add_allowlist_entry(
                id='testString',
                ip_address={'address':'172.16.0.0/16','description':'Dev IP space 3'}
            ).get_result()

            print(json.dumps(add_allowlist_entry_response, indent=2))

            # end-addAllowlistEntry

            global task_id_link
            task_id_link = add_allowlist_entry_response['task']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_change_user_password_example(self):
        """
        change_user_password request example
        """
        try:
            # begin-changeUserPassword

            a_password_setting_user_model = {
                'password': 'xyzzyyzzyx'
            }

            change_user_password_response = cloud_databases_service.change_user_password(
                id='testString',
                user_type='database',
                username='james',
                user={'password':'xyzzyyzzyx'}
            ).get_result()

            print(json.dumps(change_user_password_response, indent=2))

            # end-changeUserPassword

            global task_id_link
            task_id_link = change_user_password_response['task']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_database_user_example(self):
        """
        create_database_user request example
        """
        try:
            # begin-createDatabaseUser

            create_database_user_request_user_model = {
                'username': 'james',
                'password': 'kickoutthe'
            }

            create_database_user_response = cloud_databases_service.create_database_user(
                id='testString',
                user_type='database',
                user={'username':'james','password':'kickoutthe'}
            ).get_result()

            print(json.dumps(create_database_user_response, indent=2))

            # end-createDatabaseUser

            global task_id_link
            task_id_link = create_database_user_response['task']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_allowlist_entry_example(self):
        """
        delete_allowlist_entry request example
        """
        try:
            # begin-deleteAllowlistEntry

            delete_allowlist_entry_response = cloud_databases_service.delete_allowlist_entry(
                id='testString',
                ipaddress='testString'
            ).get_result()

            print(json.dumps(delete_allowlist_entry_response, indent=2))

            # end-deleteAllowlistEntry

            global task_id_link
            task_id_link = delete_allowlist_entry_response['task']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_database_user_example(self):
        """
        delete_database_user request example
        """
        try:
            # begin-deleteDatabaseUser

            delete_database_user_response = cloud_databases_service.delete_database_user(
                id='testString',
                user_type='database',
                username='james'
            ).get_result()

            print(json.dumps(delete_database_user_response, indent=2))

            # end-deleteDatabaseUser

            global task_id_link
            task_id_link = delete_database_user_response['task']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_kill_connections_example(self):
        """
        kill_connections request example
        """
        try:
            # begin-killConnections

            kill_connections_response = cloud_databases_service.kill_connections(
                id='testString'
            ).get_result()

            print(json.dumps(kill_connections_response, indent=2))

            # end-killConnections

            global task_id_link
            task_id_link = kill_connections_response['task']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_set_allowlist_example(self):
        """
        set_allowlist request example
        """
        try:
            # begin-setAllowlist

            allowlist_entry_model = {
                'address': '195.212.0.0/16',
                'description': 'Dev IP space 1'
            }

            set_allowlist_response = cloud_databases_service.set_allowlist(
                id='testString',
                ip_addresses=[allowlist_entry_model]
            ).get_result()

            print(json.dumps(set_allowlist_response, indent=2))

            # end-setAllowlist

            global task_id_link
            task_id_link = set_allowlist_response['task']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_set_autoscaling_conditions_example(self):
        """
        set_autoscaling_conditions request example
        """
        try:
            # begin-setAutoscalingConditions

            autoscaling_memory_group_memory_scalers_io_utilization_model = {
                'enabled': True,
                'over_period': '5m',
                'above_percent': 90
            }

            autoscaling_memory_group_memory_scalers_model = {
                'io_utilization': {'enabled':true,'over_period':'5m','above_percent':90}
            }

            autoscaling_memory_group_memory_rate_model = {
                'increase_percent': 10.0,
                'period_seconds': 300,
                'limit_mb_per_member': 125952,
                'units': 'mb'
            }

            autoscaling_memory_group_memory_model = {
                'scalers': {'io_utilization':{'enabled':true,'over_period':'5m','above_percent':90}},
                'rate': {'increase_percent':10.0,'period_seconds':300,'limit_mb_per_member':125952,'units':'mb'}
            }

            autoscaling_set_group_autoscaling_model = {
                'memory': {'scalers':{'io_utilization':{'enabled':true,'over_period':'5m','above_percent':90}},'rate':{'increase_percent':10.0,'period_seconds':300,'limit_mb_per_member':125952,'units':'mb'}}
            }

            set_autoscaling_conditions_response = cloud_databases_service.set_autoscaling_conditions(
                id='testString',
                group_id='testString',
                autoscaling={'memory':{'scalers':{'io_utilization':{'enabled':true,'over_period':'5m','above_percent':90}},'rate':{'increase_percent':10.0,'period_seconds':300,'limit_mb_per_member':125952,'units':'mb'}}}
            ).get_result()

            print(json.dumps(set_autoscaling_conditions_response, indent=2))

            # end-setAutoscalingConditions

            global task_id_link
            task_id_link = set_autoscaling_conditions_response['task']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_set_deployment_scaling_group_example(self):
        """
        set_deployment_scaling_group request example
        """
        try:
            # begin-setDeploymentScalingGroup

            set_memory_group_memory_model = {
                'allocation_mb': 4096
            }

            set_deployment_scaling_group_request_model = {
                'memory': {'allocation_mb':4096}
            }

            set_deployment_scaling_group_response = cloud_databases_service.set_deployment_scaling_group(
                id='testString',
                group_id='testString',
                set_deployment_scaling_group_request=set_deployment_scaling_group_request_model
            ).get_result()

            print(json.dumps(set_deployment_scaling_group_response, indent=2))

            # end-setDeploymentScalingGroup

            global task_id_link
            task_id_link = set_deployment_scaling_group_response['task']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_database_configuration_example(self):
        """
        update_database_configuration request example
        """
        try:
            # begin-updateDatabaseConfiguration

            set_configuration_configuration_model = {
                'max_connections': 200
            }

            update_database_configuration_response = cloud_databases_service.update_database_configuration(
                id='testString',
                configuration={'max_connections':200}
            ).get_result()

            print(json.dumps(update_database_configuration_response, indent=2))

            # end-updateDatabaseConfiguration

            global task_id_link
            task_id_link = update_database_configuration_response['task']['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_deployables_example(self):
        """
        list_deployables request example
        """
        try:
            # begin-listDeployables

            list_deployables_response = cloud_databases_service.list_deployables().get_result()

            print(json.dumps(list_deployables_response, indent=2))

            # end-listDeployables

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_regions_example(self):
        """
        list_regions request example
        """
        try:
            # begin-listRegions

            list_regions_response = cloud_databases_service.list_regions().get_result()

            print(json.dumps(list_regions_response, indent=2))

            # end-listRegions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_deployment_info_example(self):
        """
        get_deployment_info request example
        """
        try:
            # begin-getDeploymentInfo

            get_deployment_info_response = cloud_databases_service.get_deployment_info(
                id='testString'
            ).get_result()

            print(json.dumps(get_deployment_info_response, indent=2))

            # end-getDeploymentInfo

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_remotes_example(self):
        """
        list_remotes request example
        """
        try:
            # begin-listRemotes

            list_remotes_response = cloud_databases_service.list_remotes(
                id='testString'
            ).get_result()

            print(json.dumps(list_remotes_response, indent=2))

            # end-listRemotes

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_resync_replica_example(self):
        """
        resync_replica request example
        """
        try:
            # begin-resyncReplica

            resync_replica_response = cloud_databases_service.resync_replica(
                id='testString'
            ).get_result()

            print(json.dumps(resync_replica_response, indent=2))

            # end-resyncReplica

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_set_promotion_example(self):
        """
        set_promotion request example
        """
        try:
            # begin-setPromotion

            set_promotion_response = cloud_databases_service.set_promotion(
                id='testString',
            ).get_result()

            print(json.dumps(set_promotion_response, indent=2))

            # end-setPromotion

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_deployment_tasks_example(self):
        """
        list_deployment_tasks request example
        """
        try:
            # begin-listDeploymentTasks

            tasks = cloud_databases_service.list_deployment_tasks(
                id='testString'
            ).get_result()

            print(json.dumps(tasks, indent=2))

            # end-listDeploymentTasks

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_task_example(self):
        """
        get_task request example
        """
        try:
            # begin-getTask

            get_task_response = cloud_databases_service.get_task(
                id=task_id_link
            ).get_result()

            print(json.dumps(get_task_response, indent=2))

            # end-getTask

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_backup_info_example(self):
        """
        get_backup_info request example
        """
        try:
            # begin-getBackupInfo

            get_backup_info_response = cloud_databases_service.get_backup_info(
                backup_id='testString'
            ).get_result()

            print(json.dumps(get_backup_info_response, indent=2))

            # end-getBackupInfo

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_deployment_backups_example(self):
        """
        list_deployment_backups request example
        """
        try:
            # begin-listDeploymentBackups

            backups = cloud_databases_service.list_deployment_backups(
                id='testString'
            ).get_result()

            print(json.dumps(backups, indent=2))

            # end-listDeploymentBackups

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_start_ondemand_backup_example(self):
        """
        start_ondemand_backup request example
        """
        try:
            # begin-startOndemandBackup

            start_ondemand_backup_response = cloud_databases_service.start_ondemand_backup(
                id='testString'
            ).get_result()

            print(json.dumps(start_ondemand_backup_response, indent=2))

            # end-startOndemandBackup

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_pit_rdata_example(self):
        """
        get_pit_rdata request example
        """
        try:
            # begin-getPITRdata

            point_in_time_recovery_data = cloud_databases_service.get_pit_rdata(
                id='testString'
            ).get_result()

            print(json.dumps(point_in_time_recovery_data, indent=2))

            # end-getPITRdata

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_connection_example(self):
        """
        get_connection request example
        """
        try:
            # begin-getConnection

            connection = cloud_databases_service.get_connection(
                id='testString',
                user_type='database',
                user_id='testString',
                endpoint_type='public'
            ).get_result()

            print(json.dumps(connection, indent=2))

            # end-getConnection

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_complete_connection_example(self):
        """
        complete_connection request example
        """
        try:
            # begin-completeConnection

            connection = cloud_databases_service.complete_connection(
                id='testString',
                user_type='database',
                user_id='testString',
                endpoint_type='public',
                password='providedpassword'
            ).get_result()

            print(json.dumps(connection, indent=2))

            # end-completeConnection

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_deployment_scaling_groups_example(self):
        """
        list_deployment_scaling_groups request example
        """
        try:
            # begin-listDeploymentScalingGroups

            groups = cloud_databases_service.list_deployment_scaling_groups(
                id='testString'
            ).get_result()

            print(json.dumps(groups, indent=2))

            # end-listDeploymentScalingGroups

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_default_scaling_groups_example(self):
        """
        get_default_scaling_groups request example
        """
        try:
            # begin-getDefaultScalingGroups

            groups = cloud_databases_service.get_default_scaling_groups(
                type='postgresql'
            ).get_result()

            print(json.dumps(groups, indent=2))

            # end-getDefaultScalingGroups

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_autoscaling_conditions_example(self):
        """
        get_autoscaling_conditions request example
        """
        try:
            # begin-getAutoscalingConditions

            autoscaling_group = cloud_databases_service.get_autoscaling_conditions(
                id='testString',
                group_id='testString'
            ).get_result()

            print(json.dumps(autoscaling_group, indent=2))

            # end-getAutoscalingConditions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_allowlist_example(self):
        """
        get_allowlist request example
        """
        try:
            # begin-getAllowlist

            allowlist = cloud_databases_service.get_allowlist(
                id='testString'
            ).get_result()

            print(json.dumps(allowlist, indent=2))

            # end-getAllowlist

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: CloudDatabasesV5
##############################################################################
