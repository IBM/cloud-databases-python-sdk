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
Unit Tests for CloudDatabasesV5
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_cloud_databases.cloud_databases_v5 import *


service = CloudDatabasesV5(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://fake'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Deployments
##############################################################################
# region

class TestListDeployables():
    """
    Test Class for list_deployables
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_deployables_all_params(self):
        """
        list_deployables()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployables')
        mock_response = '{"deployables": [{"type": "elasticsearch", "versions": [{"version": "5.6", "status": "stable", "is_preferred": true, "transitions": [{"application": "elasticsearch", "method": "restore", "from_version": "5.6", "to_version": "6.7"}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_deployables()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestListRegions():
    """
    Test Class for list_regions
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_regions_all_params(self):
        """
        list_regions()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/regions')
        mock_response = '{"regions": ["regions"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_regions()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetDeploymentInfo():
    """
    Test Class for get_deployment_info
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_deployment_info_all_params(self):
        """
        get_deployment_info()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString')
        mock_response = '{"deployment": {"id": "crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::", "name": "crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::", "type": "redis", "platform_options": {"anyKey": "anyValue"}, "version": "4", "admin_usernames": {"mapKey": "inner"}, "enable_public_endpoints": true, "enable_private_endpoints": false}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_deployment_info(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_deployment_info_value_error(self):
        """
        test_get_deployment_info_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString')
        mock_response = '{"deployment": {"id": "crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::", "name": "crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::", "type": "redis", "platform_options": {"anyKey": "anyValue"}, "version": "4", "admin_usernames": {"mapKey": "inner"}, "enable_public_endpoints": true, "enable_private_endpoints": false}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_deployment_info(**req_copy)



# endregion
##############################################################################
# End of Service: Deployments
##############################################################################

##############################################################################
# Start of Service: DatabaseUsers
##############################################################################
# region

class TestCreateDatabaseUser():
    """
    Test Class for create_database_user
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_database_user_all_params(self):
        """
        create_database_user()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a CreateDatabaseUserRequestUser model
        create_database_user_request_user_model = {}
        create_database_user_request_user_model['user_type'] = 'database'
        create_database_user_request_user_model['username'] = 'james'
        create_database_user_request_user_model['password'] = 'kickoutthe'

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user = create_database_user_request_user_model

        # Invoke method
        response = service.create_database_user(
            id,
            user_type,
            user=user,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['user'] == create_database_user_request_user_model


    @responses.activate
    def test_create_database_user_value_error(self):
        """
        test_create_database_user_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a CreateDatabaseUserRequestUser model
        create_database_user_request_user_model = {}
        create_database_user_request_user_model['user_type'] = 'database'
        create_database_user_request_user_model['username'] = 'james'
        create_database_user_request_user_model['password'] = 'kickoutthe'

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user = create_database_user_request_user_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "user_type": user_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_database_user(**req_copy)



class TestChangeUserPassword():
    """
    Test Class for change_user_password
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_change_user_password_all_params(self):
        """
        change_user_password()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database/james')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a APasswordSettingUser model
        a_password_setting_user_model = {}
        a_password_setting_user_model['password'] = 'xyzzyyzzyx'

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        username = 'james'
        user = a_password_setting_user_model

        # Invoke method
        response = service.change_user_password(
            id,
            user_type,
            username,
            user=user,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['user'] == a_password_setting_user_model


    @responses.activate
    def test_change_user_password_value_error(self):
        """
        test_change_user_password_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database/james')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a APasswordSettingUser model
        a_password_setting_user_model = {}
        a_password_setting_user_model['password'] = 'xyzzyyzzyx'

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        username = 'james'
        user = a_password_setting_user_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "user_type": user_type,
            "username": username,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.change_user_password(**req_copy)



class TestDeleteDatabaseUser():
    """
    Test Class for delete_database_user
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_database_user_all_params(self):
        """
        delete_database_user()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database/james')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        username = 'james'

        # Invoke method
        response = service.delete_database_user(
            id,
            user_type,
            username,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_delete_database_user_value_error(self):
        """
        test_delete_database_user_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database/james')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        username = 'james'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "user_type": user_type,
            "username": username,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_database_user(**req_copy)



# endregion
##############################################################################
# End of Service: DatabaseUsers
##############################################################################

##############################################################################
# Start of Service: DatabaseConfiguration
##############################################################################
# region

class TestUpdateDatabaseConfiguration():
    """
    Test Class for update_database_configuration
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_database_configuration_all_params(self):
        """
        update_database_configuration()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/configuration')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SetConfigurationConfigurationPGConfiguration model
        set_configuration_configuration_model = {}
        set_configuration_configuration_model['max_connections'] = 200
        set_configuration_configuration_model['max_prepared_transactions'] = 0
        set_configuration_configuration_model['deadlock_timeout'] = 100
        set_configuration_configuration_model['effective_io_concurrency'] = 1
        set_configuration_configuration_model['max_replication_slots'] = 10
        set_configuration_configuration_model['max_wal_senders'] = 12
        set_configuration_configuration_model['shared_buffers'] = 16
        set_configuration_configuration_model['synchronous_commit'] = 'local'
        set_configuration_configuration_model['wal_level'] = 'hot_standby'
        set_configuration_configuration_model['archive_timeout'] = 300
        set_configuration_configuration_model['log_min_duration_statement'] = 100

        # Set up parameter values
        id = 'testString'
        configuration = set_configuration_configuration_model

        # Invoke method
        response = service.update_database_configuration(
            id,
            configuration,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['configuration'] == set_configuration_configuration_model


    @responses.activate
    def test_update_database_configuration_value_error(self):
        """
        test_update_database_configuration_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/configuration')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SetConfigurationConfigurationPGConfiguration model
        set_configuration_configuration_model = {}
        set_configuration_configuration_model['max_connections'] = 200
        set_configuration_configuration_model['max_prepared_transactions'] = 0
        set_configuration_configuration_model['deadlock_timeout'] = 100
        set_configuration_configuration_model['effective_io_concurrency'] = 1
        set_configuration_configuration_model['max_replication_slots'] = 10
        set_configuration_configuration_model['max_wal_senders'] = 12
        set_configuration_configuration_model['shared_buffers'] = 16
        set_configuration_configuration_model['synchronous_commit'] = 'local'
        set_configuration_configuration_model['wal_level'] = 'hot_standby'
        set_configuration_configuration_model['archive_timeout'] = 300
        set_configuration_configuration_model['log_min_duration_statement'] = 100

        # Set up parameter values
        id = 'testString'
        configuration = set_configuration_configuration_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "configuration": configuration,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_database_configuration(**req_copy)



# endregion
##############################################################################
# End of Service: DatabaseConfiguration
##############################################################################

##############################################################################
# Start of Service: Remotes
##############################################################################
# region

class TestListRemotes():
    """
    Test Class for list_remotes
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_remotes_all_params(self):
        """
        list_remotes()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/remotes')
        mock_response = '{"remotes": {"leader": "01f30581-54f8-41a4-8193-4a04cc022e9b-h", "replicas": ["replicas"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.list_remotes(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_remotes_value_error(self):
        """
        test_list_remotes_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/remotes')
        mock_response = '{"remotes": {"leader": "01f30581-54f8-41a4-8193-4a04cc022e9b-h", "replicas": ["replicas"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_remotes(**req_copy)



class TestResyncReplica():
    """
    Test Class for resync_replica
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_resync_replica_all_params(self):
        """
        resync_replica()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/remotes/resync')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.resync_replica(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_resync_replica_value_error(self):
        """
        test_resync_replica_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/remotes/resync')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.resync_replica(**req_copy)



class TestSetPromotion():
    """
    Test Class for set_promotion
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_set_promotion_all_params(self):
        """
        set_promotion()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/remotes/promotion')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SetPromotionPromotionPromote model
        set_promotion_promotion_model = {}
        set_promotion_promotion_model['promotion'] = {}

        # Set up parameter values
        id = 'testString'
        promotion = set_promotion_promotion_model

        # Invoke method
        response = service.set_promotion(
            id,
            promotion,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['Promotion'] == set_promotion_promotion_model


    @responses.activate
    def test_set_promotion_value_error(self):
        """
        test_set_promotion_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/remotes/promotion')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SetPromotionPromotionPromote model
        set_promotion_promotion_model = {}
        set_promotion_promotion_model['promotion'] = {}

        # Set up parameter values
        id = 'testString'
        promotion = set_promotion_promotion_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "promotion": promotion,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.set_promotion(**req_copy)



# endregion
##############################################################################
# End of Service: Remotes
##############################################################################

##############################################################################
# Start of Service: Tasks
##############################################################################
# region

class TestListDeploymentTasks():
    """
    Test Class for list_deployment_tasks
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_deployment_tasks_all_params(self):
        """
        list_deployment_tasks()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/tasks')
        mock_response = '{"tasks": [{"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.list_deployment_tasks(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_deployment_tasks_value_error(self):
        """
        test_list_deployment_tasks_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/tasks')
        mock_response = '{"tasks": [{"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_deployment_tasks(**req_copy)



class TestGetTask():
    """
    Test Class for get_task
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_task_all_params(self):
        """
        get_task()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/tasks/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_task(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_task_value_error(self):
        """
        test_get_task_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/tasks/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_task(**req_copy)



# endregion
##############################################################################
# End of Service: Tasks
##############################################################################

##############################################################################
# Start of Service: Backups
##############################################################################
# region

class TestGetBackupInfo():
    """
    Test Class for get_backup_info
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_backup_info_all_params(self):
        """
        get_backup_info()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/backups/testString')
        mock_response = '{"backup": {"id": "5a970218cb7544000671c094", "deployment_id": "595eada310b7ac00116dd48b", "type": "scheduled", "status": "running", "is_downloadable": true, "is_restorable": true, "created_at": "2018-02-28T19:25:12.000Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        backup_id = 'testString'

        # Invoke method
        response = service.get_backup_info(
            backup_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_backup_info_value_error(self):
        """
        test_get_backup_info_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/backups/testString')
        mock_response = '{"backup": {"id": "5a970218cb7544000671c094", "deployment_id": "595eada310b7ac00116dd48b", "type": "scheduled", "status": "running", "is_downloadable": true, "is_restorable": true, "created_at": "2018-02-28T19:25:12.000Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        backup_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "backup_id": backup_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_backup_info(**req_copy)



class TestListDeploymentBackups():
    """
    Test Class for list_deployment_backups
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_deployment_backups_all_params(self):
        """
        list_deployment_backups()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/backups')
        mock_response = '{"backups": [{"id": "5a970218cb7544000671c094", "deployment_id": "595eada310b7ac00116dd48b", "type": "scheduled", "status": "running", "is_downloadable": true, "is_restorable": true, "created_at": "2018-02-28T19:25:12.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.list_deployment_backups(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_deployment_backups_value_error(self):
        """
        test_list_deployment_backups_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/backups')
        mock_response = '{"backups": [{"id": "5a970218cb7544000671c094", "deployment_id": "595eada310b7ac00116dd48b", "type": "scheduled", "status": "running", "is_downloadable": true, "is_restorable": true, "created_at": "2018-02-28T19:25:12.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_deployment_backups(**req_copy)



class TestStartOndemandBackup():
    """
    Test Class for start_ondemand_backup
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_start_ondemand_backup_all_params(self):
        """
        start_ondemand_backup()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/backups')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.start_ondemand_backup(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_start_ondemand_backup_value_error(self):
        """
        test_start_ondemand_backup_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/backups')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.start_ondemand_backup(**req_copy)



class TestGetPitRdata():
    """
    Test Class for get_pit_rdata
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_pit_rdata_all_params(self):
        """
        get_pit_rdata()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/point_in_time_recovery_data')
        mock_response = '{"earliest_point_in_time_recovery_time": "earliest_point_in_time_recovery_time"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_pit_rdata(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_pit_rdata_value_error(self):
        """
        test_get_pit_rdata_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/point_in_time_recovery_data')
        mock_response = '{"earliest_point_in_time_recovery_time": "earliest_point_in_time_recovery_time"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_pit_rdata(**req_copy)



# endregion
##############################################################################
# End of Service: Backups
##############################################################################

##############################################################################
# Start of Service: Connections
##############################################################################
# region

class TestGetConnection():
    """
    Test Class for get_connection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_connection_all_params(self):
        """
        get_connection()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "/ibmclouddb", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"mapKey": "inner"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'
        certificate_root = 'testString'

        # Invoke method
        response = service.get_connection(
            id,
            user_type,
            user_id,
            endpoint_type,
            certificate_root=certificate_root,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'certificate_root={}'.format(certificate_root) in query_string


    @responses.activate
    def test_get_connection_required_params(self):
        """
        test_get_connection_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "/ibmclouddb", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"mapKey": "inner"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'

        # Invoke method
        response = service.get_connection(
            id,
            user_type,
            user_id,
            endpoint_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_connection_value_error(self):
        """
        test_get_connection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "/ibmclouddb", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"mapKey": "inner"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "user_type": user_type,
            "user_id": user_id,
            "endpoint_type": endpoint_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_connection(**req_copy)



class TestCompleteConnection():
    """
    Test Class for complete_connection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_complete_connection_all_params(self):
        """
        complete_connection()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "/ibmclouddb", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"mapKey": "inner"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'
        password = 'providedpassword'
        certificate_root = 'testString'

        # Invoke method
        response = service.complete_connection(
            id,
            user_type,
            user_id,
            endpoint_type,
            password=password,
            certificate_root=certificate_root,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['password'] == 'providedpassword'
        assert req_body['certificate_root'] == 'testString'


    @responses.activate
    def test_complete_connection_required_params(self):
        """
        test_complete_connection_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "/ibmclouddb", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"mapKey": "inner"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'

        # Invoke method
        response = service.complete_connection(
            id,
            user_type,
            user_id,
            endpoint_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_complete_connection_value_error(self):
        """
        test_complete_connection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "/ibmclouddb", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"mapKey": "inner"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "user_type": user_type,
            "user_id": user_id,
            "endpoint_type": endpoint_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.complete_connection(**req_copy)



# endregion
##############################################################################
# End of Service: Connections
##############################################################################

##############################################################################
# Start of Service: Scaling
##############################################################################
# region

class TestListDeploymentScalingGroups():
    """
    Test Class for list_deployment_scaling_groups
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_deployment_scaling_groups_all_params(self):
        """
        list_deployment_scaling_groups()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/groups')
        mock_response = '{"groups": [{"id": "member", "count": 2, "members": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 20, "step_size_count": 1, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "memory": {"units": "mb", "allocation_mb": 12288, "minimum_mb": 1024, "maximum_mb": 114688, "step_size_mb": 1024, "is_adjustable": true, "is_optional": false, "can_scale_down": true}, "cpu": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 32, "step_size_count": 2, "is_adjustable": false, "is_optional": false, "can_scale_down": true}, "disk": {"units": "mb", "allocation_mb": 10240, "minimum_mb": 2048, "maximum_mb": 4194304, "step_size_mb": 2048, "is_adjustable": true, "is_optional": false, "can_scale_down": false}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.list_deployment_scaling_groups(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_deployment_scaling_groups_value_error(self):
        """
        test_list_deployment_scaling_groups_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/groups')
        mock_response = '{"groups": [{"id": "member", "count": 2, "members": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 20, "step_size_count": 1, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "memory": {"units": "mb", "allocation_mb": 12288, "minimum_mb": 1024, "maximum_mb": 114688, "step_size_mb": 1024, "is_adjustable": true, "is_optional": false, "can_scale_down": true}, "cpu": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 32, "step_size_count": 2, "is_adjustable": false, "is_optional": false, "can_scale_down": true}, "disk": {"units": "mb", "allocation_mb": 10240, "minimum_mb": 2048, "maximum_mb": 4194304, "step_size_mb": 2048, "is_adjustable": true, "is_optional": false, "can_scale_down": false}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_deployment_scaling_groups(**req_copy)



class TestGetDefaultScalingGroups():
    """
    Test Class for get_default_scaling_groups
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_default_scaling_groups_all_params(self):
        """
        get_default_scaling_groups()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployables/postgresql/groups')
        mock_response = '{"groups": [{"id": "member", "count": 2, "members": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 20, "step_size_count": 1, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "memory": {"units": "mb", "allocation_mb": 12288, "minimum_mb": 1024, "maximum_mb": 114688, "step_size_mb": 1024, "is_adjustable": true, "is_optional": false, "can_scale_down": true}, "cpu": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 32, "step_size_count": 2, "is_adjustable": false, "is_optional": false, "can_scale_down": true}, "disk": {"units": "mb", "allocation_mb": 10240, "minimum_mb": 2048, "maximum_mb": 4194304, "step_size_mb": 2048, "is_adjustable": true, "is_optional": false, "can_scale_down": false}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'postgresql'

        # Invoke method
        response = service.get_default_scaling_groups(
            type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_default_scaling_groups_value_error(self):
        """
        test_get_default_scaling_groups_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployables/postgresql/groups')
        mock_response = '{"groups": [{"id": "member", "count": 2, "members": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 20, "step_size_count": 1, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "memory": {"units": "mb", "allocation_mb": 12288, "minimum_mb": 1024, "maximum_mb": 114688, "step_size_mb": 1024, "is_adjustable": true, "is_optional": false, "can_scale_down": true}, "cpu": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 32, "step_size_count": 2, "is_adjustable": false, "is_optional": false, "can_scale_down": true}, "disk": {"units": "mb", "allocation_mb": 10240, "minimum_mb": 2048, "maximum_mb": 4194304, "step_size_mb": 2048, "is_adjustable": true, "is_optional": false, "can_scale_down": false}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'postgresql'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_default_scaling_groups(**req_copy)



class TestSetDeploymentScalingGroup():
    """
    Test Class for set_deployment_scaling_group
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_set_deployment_scaling_group_all_params(self):
        """
        set_deployment_scaling_group()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/groups/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a SetMemoryGroupMemory model
        set_memory_group_memory_model = {}
        set_memory_group_memory_model['allocation_mb'] = 4096

        # Construct a dict representation of a SetDeploymentScalingGroupRequestSetMemoryGroup model
        set_deployment_scaling_group_request_model = {}
        set_deployment_scaling_group_request_model['memory'] = set_memory_group_memory_model

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'
        set_deployment_scaling_group_request = set_deployment_scaling_group_request_model

        # Invoke method
        response = service.set_deployment_scaling_group(
            id,
            group_id,
            set_deployment_scaling_group_request,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == set_deployment_scaling_group_request


    @responses.activate
    def test_set_deployment_scaling_group_value_error(self):
        """
        test_set_deployment_scaling_group_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/groups/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a SetMemoryGroupMemory model
        set_memory_group_memory_model = {}
        set_memory_group_memory_model['allocation_mb'] = 4096

        # Construct a dict representation of a SetDeploymentScalingGroupRequestSetMemoryGroup model
        set_deployment_scaling_group_request_model = {}
        set_deployment_scaling_group_request_model['memory'] = set_memory_group_memory_model

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'
        set_deployment_scaling_group_request = set_deployment_scaling_group_request_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "group_id": group_id,
            "set_deployment_scaling_group_request": set_deployment_scaling_group_request,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.set_deployment_scaling_group(**req_copy)



# endregion
##############################################################################
# End of Service: Scaling
##############################################################################

##############################################################################
# Start of Service: Autoscaling
##############################################################################
# region

class TestGetAutoscalingConditions():
    """
    Test Class for get_autoscaling_conditions
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_autoscaling_conditions_all_params(self):
        """
        get_autoscaling_conditions()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/groups/testString/autoscaling')
        mock_response = '{"autoscaling": {"disk": {"scalers": {"capacity": {"enabled": true, "free_space_less_than_percent": 10}, "io_utilization": {"enabled": true, "over_period": "30m", "above_percent": 45}}, "rate": {"increase_percent": 20, "period_seconds": 900, "limit_mb_per_member": 3670016, "units": "mb"}}, "memory": {"scalers": {"io_utilization": {"enabled": true, "over_period": "30m", "above_percent": 45}}, "rate": {"increase_percent": 10, "period_seconds": 900, "limit_mb_per_member": 3670016, "units": "mb"}}, "cpu": {"scalers": {"anyKey": "anyValue"}, "rate": {"increase_percent": 10, "period_seconds": 900, "limit_count_per_member": 10, "units": "count"}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'

        # Invoke method
        response = service.get_autoscaling_conditions(
            id,
            group_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_autoscaling_conditions_value_error(self):
        """
        test_get_autoscaling_conditions_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/groups/testString/autoscaling')
        mock_response = '{"autoscaling": {"disk": {"scalers": {"capacity": {"enabled": true, "free_space_less_than_percent": 10}, "io_utilization": {"enabled": true, "over_period": "30m", "above_percent": 45}}, "rate": {"increase_percent": 20, "period_seconds": 900, "limit_mb_per_member": 3670016, "units": "mb"}}, "memory": {"scalers": {"io_utilization": {"enabled": true, "over_period": "30m", "above_percent": 45}}, "rate": {"increase_percent": 10, "period_seconds": 900, "limit_mb_per_member": 3670016, "units": "mb"}}, "cpu": {"scalers": {"anyKey": "anyValue"}, "rate": {"increase_percent": 10, "period_seconds": 900, "limit_count_per_member": 10, "units": "count"}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "group_id": group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_autoscaling_conditions(**req_copy)



class TestSetAutoscalingConditions():
    """
    Test Class for set_autoscaling_conditions
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_set_autoscaling_conditions_all_params(self):
        """
        set_autoscaling_conditions()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/groups/testString/autoscaling')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryScalersIoUtilization model
        autoscaling_memory_group_memory_scalers_io_utilization_model = {}
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '5m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 90

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryScalers model
        autoscaling_memory_group_memory_scalers_model = {}
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryRate model
        autoscaling_memory_group_memory_rate_model = {}
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10.0
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 300
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 125952
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        # Construct a dict representation of a AutoscalingMemoryGroupMemory model
        autoscaling_memory_group_memory_model = {}
        autoscaling_memory_group_memory_model['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model['rate'] = autoscaling_memory_group_memory_rate_model

        # Construct a dict representation of a AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup model
        autoscaling_set_group_autoscaling_model = {}
        autoscaling_set_group_autoscaling_model['memory'] = autoscaling_memory_group_memory_model

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'
        autoscaling = autoscaling_set_group_autoscaling_model

        # Invoke method
        response = service.set_autoscaling_conditions(
            id,
            group_id,
            autoscaling,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['autoscaling'] == autoscaling_set_group_autoscaling_model


    @responses.activate
    def test_set_autoscaling_conditions_value_error(self):
        """
        test_set_autoscaling_conditions_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/groups/testString/autoscaling')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryScalersIoUtilization model
        autoscaling_memory_group_memory_scalers_io_utilization_model = {}
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '5m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 90

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryScalers model
        autoscaling_memory_group_memory_scalers_model = {}
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryRate model
        autoscaling_memory_group_memory_rate_model = {}
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10.0
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 300
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 125952
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        # Construct a dict representation of a AutoscalingMemoryGroupMemory model
        autoscaling_memory_group_memory_model = {}
        autoscaling_memory_group_memory_model['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model['rate'] = autoscaling_memory_group_memory_rate_model

        # Construct a dict representation of a AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup model
        autoscaling_set_group_autoscaling_model = {}
        autoscaling_set_group_autoscaling_model['memory'] = autoscaling_memory_group_memory_model

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'
        autoscaling = autoscaling_set_group_autoscaling_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "group_id": group_id,
            "autoscaling": autoscaling,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.set_autoscaling_conditions(**req_copy)



# endregion
##############################################################################
# End of Service: Autoscaling
##############################################################################

##############################################################################
# Start of Service: Management
##############################################################################
# region

class TestKillConnections():
    """
    Test Class for kill_connections
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_kill_connections_all_params(self):
        """
        kill_connections()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/management/database_connections')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.kill_connections(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_kill_connections_value_error(self):
        """
        test_kill_connections_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/management/database_connections')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.kill_connections(**req_copy)



# endregion
##############################################################################
# End of Service: Management
##############################################################################

##############################################################################
# Start of Service: Security
##############################################################################
# region

class TestGetAllowlist():
    """
    Test Class for get_allowlist
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_allowlist_all_params(self):
        """
        get_allowlist()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/whitelists/ip_addresses')
        mock_response = '{"ip_addresses": [{"address": "address", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_allowlist(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_allowlist_value_error(self):
        """
        test_get_allowlist_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/whitelists/ip_addresses')
        mock_response = '{"ip_addresses": [{"address": "address", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_allowlist(**req_copy)



class TestSetAllowlist():
    """
    Test Class for set_allowlist
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_set_allowlist_all_params(self):
        """
        set_allowlist()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/whitelists/ip_addresses')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {}
        allowlist_entry_model['address'] = '195.212.0.0/16'
        allowlist_entry_model['description'] = 'Dev IP space 1'

        # Set up parameter values
        id = 'testString'
        ip_addresses = [allowlist_entry_model]
        if_match = 'testString'

        # Invoke method
        response = service.set_allowlist(
            id,
            ip_addresses=ip_addresses,
            if_match=if_match,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['ip_addresses'] == [allowlist_entry_model]


    @responses.activate
    def test_set_allowlist_required_params(self):
        """
        test_set_allowlist_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/whitelists/ip_addresses')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {}
        allowlist_entry_model['address'] = '195.212.0.0/16'
        allowlist_entry_model['description'] = 'Dev IP space 1'

        # Set up parameter values
        id = 'testString'
        ip_addresses = [allowlist_entry_model]

        # Invoke method
        response = service.set_allowlist(
            id,
            ip_addresses=ip_addresses,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['ip_addresses'] == [allowlist_entry_model]


    @responses.activate
    def test_set_allowlist_value_error(self):
        """
        test_set_allowlist_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/whitelists/ip_addresses')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {}
        allowlist_entry_model['address'] = '195.212.0.0/16'
        allowlist_entry_model['description'] = 'Dev IP space 1'

        # Set up parameter values
        id = 'testString'
        ip_addresses = [allowlist_entry_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.set_allowlist(**req_copy)



class TestAddAllowlistEntry():
    """
    Test Class for add_allowlist_entry
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_add_allowlist_entry_all_params(self):
        """
        add_allowlist_entry()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/whitelists/ip_addresses')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {}
        allowlist_entry_model['address'] = '172.16.0.0/16'
        allowlist_entry_model['description'] = 'Dev IP space 3'

        # Set up parameter values
        id = 'testString'
        ip_address = allowlist_entry_model

        # Invoke method
        response = service.add_allowlist_entry(
            id,
            ip_address=ip_address,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['ip_address'] == allowlist_entry_model


    @responses.activate
    def test_add_allowlist_entry_value_error(self):
        """
        test_add_allowlist_entry_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/whitelists/ip_addresses')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {}
        allowlist_entry_model['address'] = '172.16.0.0/16'
        allowlist_entry_model['description'] = 'Dev IP space 3'

        # Set up parameter values
        id = 'testString'
        ip_address = allowlist_entry_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.add_allowlist_entry(**req_copy)



class TestDeleteAllowlistEntry():
    """
    Test Class for delete_allowlist_entry
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_allowlist_entry_all_params(self):
        """
        delete_allowlist_entry()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/whitelists/ip_addresses/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'
        ipaddress = 'testString'

        # Invoke method
        response = service.delete_allowlist_entry(
            id,
            ipaddress,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_delete_allowlist_entry_value_error(self):
        """
        test_delete_allowlist_entry_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/deployments/testString/whitelists/ip_addresses/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'
        ipaddress = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "ipaddress": ipaddress,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_allowlist_entry(**req_copy)



# endregion
##############################################################################
# End of Service: Security
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestAPasswordSettingUser():
    """
    Test Class for APasswordSettingUser
    """

    def test_a_password_setting_user_serialization(self):
        """
        Test serialization/deserialization for APasswordSettingUser
        """

        # Construct a json representation of a APasswordSettingUser model
        a_password_setting_user_model_json = {}
        a_password_setting_user_model_json['password'] = 'xyzzy'

        # Construct a model instance of APasswordSettingUser by calling from_dict on the json representation
        a_password_setting_user_model = APasswordSettingUser.from_dict(a_password_setting_user_model_json)
        assert a_password_setting_user_model != False

        # Construct a model instance of APasswordSettingUser by calling from_dict on the json representation
        a_password_setting_user_model_dict = APasswordSettingUser.from_dict(a_password_setting_user_model_json).__dict__
        a_password_setting_user_model2 = APasswordSettingUser(**a_password_setting_user_model_dict)

        # Verify the model instances are equivalent
        assert a_password_setting_user_model == a_password_setting_user_model2

        # Convert model instance back to dict and verify no loss of data
        a_password_setting_user_model_json2 = a_password_setting_user_model.to_dict()
        assert a_password_setting_user_model_json2 == a_password_setting_user_model_json

class TestAddAllowlistEntryResponse():
    """
    Test Class for AddAllowlistEntryResponse
    """

    def test_add_allowlist_entry_response_serialization(self):
        """
        Test serialization/deserialization for AddAllowlistEntryResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-d9c96544393b'
        task_model['description'] = 'Adding allowlist entry for database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 10
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:21:30Z"))

        # Construct a json representation of a AddAllowlistEntryResponse model
        add_allowlist_entry_response_model_json = {}
        add_allowlist_entry_response_model_json['task'] = task_model

        # Construct a model instance of AddAllowlistEntryResponse by calling from_dict on the json representation
        add_allowlist_entry_response_model = AddAllowlistEntryResponse.from_dict(add_allowlist_entry_response_model_json)
        assert add_allowlist_entry_response_model != False

        # Construct a model instance of AddAllowlistEntryResponse by calling from_dict on the json representation
        add_allowlist_entry_response_model_dict = AddAllowlistEntryResponse.from_dict(add_allowlist_entry_response_model_json).__dict__
        add_allowlist_entry_response_model2 = AddAllowlistEntryResponse(**add_allowlist_entry_response_model_dict)

        # Verify the model instances are equivalent
        assert add_allowlist_entry_response_model == add_allowlist_entry_response_model2

        # Convert model instance back to dict and verify no loss of data
        add_allowlist_entry_response_model_json2 = add_allowlist_entry_response_model.to_dict()
        assert add_allowlist_entry_response_model_json2 == add_allowlist_entry_response_model_json

class TestAllowlist():
    """
    Test Class for Allowlist
    """

    def test_allowlist_serialization(self):
        """
        Test serialization/deserialization for Allowlist
        """

        # Construct dict forms of any model objects needed in order to build this model.

        allowlist_entry_model = {} # AllowlistEntry
        allowlist_entry_model['address'] = '195.212.0.0/16'
        allowlist_entry_model['description'] = 'Dev IP space 1'

        # Construct a json representation of a Allowlist model
        allowlist_model_json = {}
        allowlist_model_json['ip_addresses'] = [allowlist_entry_model]

        # Construct a model instance of Allowlist by calling from_dict on the json representation
        allowlist_model = Allowlist.from_dict(allowlist_model_json)
        assert allowlist_model != False

        # Construct a model instance of Allowlist by calling from_dict on the json representation
        allowlist_model_dict = Allowlist.from_dict(allowlist_model_json).__dict__
        allowlist_model2 = Allowlist(**allowlist_model_dict)

        # Verify the model instances are equivalent
        assert allowlist_model == allowlist_model2

        # Convert model instance back to dict and verify no loss of data
        allowlist_model_json2 = allowlist_model.to_dict()
        assert allowlist_model_json2 == allowlist_model_json

class TestAllowlistEntry():
    """
    Test Class for AllowlistEntry
    """

    def test_allowlist_entry_serialization(self):
        """
        Test serialization/deserialization for AllowlistEntry
        """

        # Construct a json representation of a AllowlistEntry model
        allowlist_entry_model_json = {}
        allowlist_entry_model_json['address'] = 'testString'
        allowlist_entry_model_json['description'] = 'testString'

        # Construct a model instance of AllowlistEntry by calling from_dict on the json representation
        allowlist_entry_model = AllowlistEntry.from_dict(allowlist_entry_model_json)
        assert allowlist_entry_model != False

        # Construct a model instance of AllowlistEntry by calling from_dict on the json representation
        allowlist_entry_model_dict = AllowlistEntry.from_dict(allowlist_entry_model_json).__dict__
        allowlist_entry_model2 = AllowlistEntry(**allowlist_entry_model_dict)

        # Verify the model instances are equivalent
        assert allowlist_entry_model == allowlist_entry_model2

        # Convert model instance back to dict and verify no loss of data
        allowlist_entry_model_json2 = allowlist_entry_model.to_dict()
        assert allowlist_entry_model_json2 == allowlist_entry_model_json

class TestAutoscalingCPUGroupCPU():
    """
    Test Class for AutoscalingCPUGroupCPU
    """

    def test_autoscaling_cpu_group_cpu_serialization(self):
        """
        Test serialization/deserialization for AutoscalingCPUGroupCPU
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_cpu_group_cpu_rate_model = {} # AutoscalingCPUGroupCPURate
        autoscaling_cpu_group_cpu_rate_model['increase_percent'] = 10
        autoscaling_cpu_group_cpu_rate_model['period_seconds'] = 900
        autoscaling_cpu_group_cpu_rate_model['limit_count_per_member'] = 10
        autoscaling_cpu_group_cpu_rate_model['units'] = 'count'

        # Construct a json representation of a AutoscalingCPUGroupCPU model
        autoscaling_cpu_group_cpu_model_json = {}
        autoscaling_cpu_group_cpu_model_json['scalers'] = { 'foo': 'bar' }
        autoscaling_cpu_group_cpu_model_json['rate'] = autoscaling_cpu_group_cpu_rate_model

        # Construct a model instance of AutoscalingCPUGroupCPU by calling from_dict on the json representation
        autoscaling_cpu_group_cpu_model = AutoscalingCPUGroupCPU.from_dict(autoscaling_cpu_group_cpu_model_json)
        assert autoscaling_cpu_group_cpu_model != False

        # Construct a model instance of AutoscalingCPUGroupCPU by calling from_dict on the json representation
        autoscaling_cpu_group_cpu_model_dict = AutoscalingCPUGroupCPU.from_dict(autoscaling_cpu_group_cpu_model_json).__dict__
        autoscaling_cpu_group_cpu_model2 = AutoscalingCPUGroupCPU(**autoscaling_cpu_group_cpu_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_cpu_group_cpu_model == autoscaling_cpu_group_cpu_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_cpu_group_cpu_model_json2 = autoscaling_cpu_group_cpu_model.to_dict()
        assert autoscaling_cpu_group_cpu_model_json2 == autoscaling_cpu_group_cpu_model_json

class TestAutoscalingCPUGroupCPURate():
    """
    Test Class for AutoscalingCPUGroupCPURate
    """

    def test_autoscaling_cpu_group_cpu_rate_serialization(self):
        """
        Test serialization/deserialization for AutoscalingCPUGroupCPURate
        """

        # Construct a json representation of a AutoscalingCPUGroupCPURate model
        autoscaling_cpu_group_cpu_rate_model_json = {}
        autoscaling_cpu_group_cpu_rate_model_json['increase_percent'] = 10
        autoscaling_cpu_group_cpu_rate_model_json['period_seconds'] = 900
        autoscaling_cpu_group_cpu_rate_model_json['limit_count_per_member'] = 10
        autoscaling_cpu_group_cpu_rate_model_json['units'] = 'count'

        # Construct a model instance of AutoscalingCPUGroupCPURate by calling from_dict on the json representation
        autoscaling_cpu_group_cpu_rate_model = AutoscalingCPUGroupCPURate.from_dict(autoscaling_cpu_group_cpu_rate_model_json)
        assert autoscaling_cpu_group_cpu_rate_model != False

        # Construct a model instance of AutoscalingCPUGroupCPURate by calling from_dict on the json representation
        autoscaling_cpu_group_cpu_rate_model_dict = AutoscalingCPUGroupCPURate.from_dict(autoscaling_cpu_group_cpu_rate_model_json).__dict__
        autoscaling_cpu_group_cpu_rate_model2 = AutoscalingCPUGroupCPURate(**autoscaling_cpu_group_cpu_rate_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_cpu_group_cpu_rate_model == autoscaling_cpu_group_cpu_rate_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_cpu_group_cpu_rate_model_json2 = autoscaling_cpu_group_cpu_rate_model.to_dict()
        assert autoscaling_cpu_group_cpu_rate_model_json2 == autoscaling_cpu_group_cpu_rate_model_json

class TestAutoscalingDiskGroupDisk():
    """
    Test Class for AutoscalingDiskGroupDisk
    """

    def test_autoscaling_disk_group_disk_serialization(self):
        """
        Test serialization/deserialization for AutoscalingDiskGroupDisk
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_disk_group_disk_scalers_capacity_model = {} # AutoscalingDiskGroupDiskScalersCapacity
        autoscaling_disk_group_disk_scalers_capacity_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model['free_space_less_than_percent'] = 10

        autoscaling_disk_group_disk_scalers_io_utilization_model = {} # AutoscalingDiskGroupDiskScalersIoUtilization
        autoscaling_disk_group_disk_scalers_io_utilization_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_disk_group_disk_scalers_model = {} # AutoscalingDiskGroupDiskScalers
        autoscaling_disk_group_disk_scalers_model['capacity'] = autoscaling_disk_group_disk_scalers_capacity_model
        autoscaling_disk_group_disk_scalers_model['io_utilization'] = autoscaling_disk_group_disk_scalers_io_utilization_model

        autoscaling_disk_group_disk_rate_model = {} # AutoscalingDiskGroupDiskRate
        autoscaling_disk_group_disk_rate_model['increase_percent'] = 20
        autoscaling_disk_group_disk_rate_model['period_seconds'] = 900
        autoscaling_disk_group_disk_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_disk_group_disk_rate_model['units'] = 'mb'

        # Construct a json representation of a AutoscalingDiskGroupDisk model
        autoscaling_disk_group_disk_model_json = {}
        autoscaling_disk_group_disk_model_json['scalers'] = autoscaling_disk_group_disk_scalers_model
        autoscaling_disk_group_disk_model_json['rate'] = autoscaling_disk_group_disk_rate_model

        # Construct a model instance of AutoscalingDiskGroupDisk by calling from_dict on the json representation
        autoscaling_disk_group_disk_model = AutoscalingDiskGroupDisk.from_dict(autoscaling_disk_group_disk_model_json)
        assert autoscaling_disk_group_disk_model != False

        # Construct a model instance of AutoscalingDiskGroupDisk by calling from_dict on the json representation
        autoscaling_disk_group_disk_model_dict = AutoscalingDiskGroupDisk.from_dict(autoscaling_disk_group_disk_model_json).__dict__
        autoscaling_disk_group_disk_model2 = AutoscalingDiskGroupDisk(**autoscaling_disk_group_disk_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_disk_group_disk_model == autoscaling_disk_group_disk_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_disk_group_disk_model_json2 = autoscaling_disk_group_disk_model.to_dict()
        assert autoscaling_disk_group_disk_model_json2 == autoscaling_disk_group_disk_model_json

class TestAutoscalingDiskGroupDiskRate():
    """
    Test Class for AutoscalingDiskGroupDiskRate
    """

    def test_autoscaling_disk_group_disk_rate_serialization(self):
        """
        Test serialization/deserialization for AutoscalingDiskGroupDiskRate
        """

        # Construct a json representation of a AutoscalingDiskGroupDiskRate model
        autoscaling_disk_group_disk_rate_model_json = {}
        autoscaling_disk_group_disk_rate_model_json['increase_percent'] = 20
        autoscaling_disk_group_disk_rate_model_json['period_seconds'] = 900
        autoscaling_disk_group_disk_rate_model_json['limit_mb_per_member'] = 3670016
        autoscaling_disk_group_disk_rate_model_json['units'] = 'mb'

        # Construct a model instance of AutoscalingDiskGroupDiskRate by calling from_dict on the json representation
        autoscaling_disk_group_disk_rate_model = AutoscalingDiskGroupDiskRate.from_dict(autoscaling_disk_group_disk_rate_model_json)
        assert autoscaling_disk_group_disk_rate_model != False

        # Construct a model instance of AutoscalingDiskGroupDiskRate by calling from_dict on the json representation
        autoscaling_disk_group_disk_rate_model_dict = AutoscalingDiskGroupDiskRate.from_dict(autoscaling_disk_group_disk_rate_model_json).__dict__
        autoscaling_disk_group_disk_rate_model2 = AutoscalingDiskGroupDiskRate(**autoscaling_disk_group_disk_rate_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_disk_group_disk_rate_model == autoscaling_disk_group_disk_rate_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_disk_group_disk_rate_model_json2 = autoscaling_disk_group_disk_rate_model.to_dict()
        assert autoscaling_disk_group_disk_rate_model_json2 == autoscaling_disk_group_disk_rate_model_json

class TestAutoscalingDiskGroupDiskScalers():
    """
    Test Class for AutoscalingDiskGroupDiskScalers
    """

    def test_autoscaling_disk_group_disk_scalers_serialization(self):
        """
        Test serialization/deserialization for AutoscalingDiskGroupDiskScalers
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_disk_group_disk_scalers_capacity_model = {} # AutoscalingDiskGroupDiskScalersCapacity
        autoscaling_disk_group_disk_scalers_capacity_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model['free_space_less_than_percent'] = 10

        autoscaling_disk_group_disk_scalers_io_utilization_model = {} # AutoscalingDiskGroupDiskScalersIoUtilization
        autoscaling_disk_group_disk_scalers_io_utilization_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model['above_percent'] = 45

        # Construct a json representation of a AutoscalingDiskGroupDiskScalers model
        autoscaling_disk_group_disk_scalers_model_json = {}
        autoscaling_disk_group_disk_scalers_model_json['capacity'] = autoscaling_disk_group_disk_scalers_capacity_model
        autoscaling_disk_group_disk_scalers_model_json['io_utilization'] = autoscaling_disk_group_disk_scalers_io_utilization_model

        # Construct a model instance of AutoscalingDiskGroupDiskScalers by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_model = AutoscalingDiskGroupDiskScalers.from_dict(autoscaling_disk_group_disk_scalers_model_json)
        assert autoscaling_disk_group_disk_scalers_model != False

        # Construct a model instance of AutoscalingDiskGroupDiskScalers by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_model_dict = AutoscalingDiskGroupDiskScalers.from_dict(autoscaling_disk_group_disk_scalers_model_json).__dict__
        autoscaling_disk_group_disk_scalers_model2 = AutoscalingDiskGroupDiskScalers(**autoscaling_disk_group_disk_scalers_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_disk_group_disk_scalers_model == autoscaling_disk_group_disk_scalers_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_disk_group_disk_scalers_model_json2 = autoscaling_disk_group_disk_scalers_model.to_dict()
        assert autoscaling_disk_group_disk_scalers_model_json2 == autoscaling_disk_group_disk_scalers_model_json

class TestAutoscalingDiskGroupDiskScalersCapacity():
    """
    Test Class for AutoscalingDiskGroupDiskScalersCapacity
    """

    def test_autoscaling_disk_group_disk_scalers_capacity_serialization(self):
        """
        Test serialization/deserialization for AutoscalingDiskGroupDiskScalersCapacity
        """

        # Construct a json representation of a AutoscalingDiskGroupDiskScalersCapacity model
        autoscaling_disk_group_disk_scalers_capacity_model_json = {}
        autoscaling_disk_group_disk_scalers_capacity_model_json['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model_json['free_space_less_than_percent'] = 10

        # Construct a model instance of AutoscalingDiskGroupDiskScalersCapacity by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_capacity_model = AutoscalingDiskGroupDiskScalersCapacity.from_dict(autoscaling_disk_group_disk_scalers_capacity_model_json)
        assert autoscaling_disk_group_disk_scalers_capacity_model != False

        # Construct a model instance of AutoscalingDiskGroupDiskScalersCapacity by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_capacity_model_dict = AutoscalingDiskGroupDiskScalersCapacity.from_dict(autoscaling_disk_group_disk_scalers_capacity_model_json).__dict__
        autoscaling_disk_group_disk_scalers_capacity_model2 = AutoscalingDiskGroupDiskScalersCapacity(**autoscaling_disk_group_disk_scalers_capacity_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_disk_group_disk_scalers_capacity_model == autoscaling_disk_group_disk_scalers_capacity_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_disk_group_disk_scalers_capacity_model_json2 = autoscaling_disk_group_disk_scalers_capacity_model.to_dict()
        assert autoscaling_disk_group_disk_scalers_capacity_model_json2 == autoscaling_disk_group_disk_scalers_capacity_model_json

class TestAutoscalingDiskGroupDiskScalersIoUtilization():
    """
    Test Class for AutoscalingDiskGroupDiskScalersIoUtilization
    """

    def test_autoscaling_disk_group_disk_scalers_io_utilization_serialization(self):
        """
        Test serialization/deserialization for AutoscalingDiskGroupDiskScalersIoUtilization
        """

        # Construct a json representation of a AutoscalingDiskGroupDiskScalersIoUtilization model
        autoscaling_disk_group_disk_scalers_io_utilization_model_json = {}
        autoscaling_disk_group_disk_scalers_io_utilization_model_json['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model_json['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model_json['above_percent'] = 45

        # Construct a model instance of AutoscalingDiskGroupDiskScalersIoUtilization by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_io_utilization_model = AutoscalingDiskGroupDiskScalersIoUtilization.from_dict(autoscaling_disk_group_disk_scalers_io_utilization_model_json)
        assert autoscaling_disk_group_disk_scalers_io_utilization_model != False

        # Construct a model instance of AutoscalingDiskGroupDiskScalersIoUtilization by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_io_utilization_model_dict = AutoscalingDiskGroupDiskScalersIoUtilization.from_dict(autoscaling_disk_group_disk_scalers_io_utilization_model_json).__dict__
        autoscaling_disk_group_disk_scalers_io_utilization_model2 = AutoscalingDiskGroupDiskScalersIoUtilization(**autoscaling_disk_group_disk_scalers_io_utilization_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_disk_group_disk_scalers_io_utilization_model == autoscaling_disk_group_disk_scalers_io_utilization_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_disk_group_disk_scalers_io_utilization_model_json2 = autoscaling_disk_group_disk_scalers_io_utilization_model.to_dict()
        assert autoscaling_disk_group_disk_scalers_io_utilization_model_json2 == autoscaling_disk_group_disk_scalers_io_utilization_model_json

class TestAutoscalingGroup():
    """
    Test Class for AutoscalingGroup
    """

    def test_autoscaling_group_serialization(self):
        """
        Test serialization/deserialization for AutoscalingGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_disk_group_disk_scalers_capacity_model = {} # AutoscalingDiskGroupDiskScalersCapacity
        autoscaling_disk_group_disk_scalers_capacity_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model['free_space_less_than_percent'] = 10

        autoscaling_disk_group_disk_scalers_io_utilization_model = {} # AutoscalingDiskGroupDiskScalersIoUtilization
        autoscaling_disk_group_disk_scalers_io_utilization_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_disk_group_disk_scalers_model = {} # AutoscalingDiskGroupDiskScalers
        autoscaling_disk_group_disk_scalers_model['capacity'] = autoscaling_disk_group_disk_scalers_capacity_model
        autoscaling_disk_group_disk_scalers_model['io_utilization'] = autoscaling_disk_group_disk_scalers_io_utilization_model

        autoscaling_disk_group_disk_rate_model = {} # AutoscalingDiskGroupDiskRate
        autoscaling_disk_group_disk_rate_model['increase_percent'] = 20
        autoscaling_disk_group_disk_rate_model['period_seconds'] = 900
        autoscaling_disk_group_disk_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_disk_group_disk_rate_model['units'] = 'mb'

        autoscaling_disk_group_disk_model = {} # AutoscalingDiskGroupDisk
        autoscaling_disk_group_disk_model['scalers'] = autoscaling_disk_group_disk_scalers_model
        autoscaling_disk_group_disk_model['rate'] = autoscaling_disk_group_disk_rate_model

        autoscaling_memory_group_memory_scalers_io_utilization_model = {} # AutoscalingMemoryGroupMemoryScalersIoUtilization
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_memory_group_memory_scalers_model = {} # AutoscalingMemoryGroupMemoryScalers
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        autoscaling_memory_group_memory_rate_model = {} # AutoscalingMemoryGroupMemoryRate
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 900
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        autoscaling_memory_group_memory_model = {} # AutoscalingMemoryGroupMemory
        autoscaling_memory_group_memory_model['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model['rate'] = autoscaling_memory_group_memory_rate_model

        autoscaling_cpu_group_cpu_rate_model = {} # AutoscalingCPUGroupCPURate
        autoscaling_cpu_group_cpu_rate_model['increase_percent'] = 10
        autoscaling_cpu_group_cpu_rate_model['period_seconds'] = 900
        autoscaling_cpu_group_cpu_rate_model['limit_count_per_member'] = 10
        autoscaling_cpu_group_cpu_rate_model['units'] = 'count'

        autoscaling_cpu_group_cpu_model = {} # AutoscalingCPUGroupCPU
        autoscaling_cpu_group_cpu_model['scalers'] = { 'foo': 'bar' }
        autoscaling_cpu_group_cpu_model['rate'] = autoscaling_cpu_group_cpu_rate_model

        autoscaling_group_autoscaling_model = {} # AutoscalingGroupAutoscaling
        autoscaling_group_autoscaling_model['disk'] = autoscaling_disk_group_disk_model
        autoscaling_group_autoscaling_model['memory'] = autoscaling_memory_group_memory_model
        autoscaling_group_autoscaling_model['cpu'] = autoscaling_cpu_group_cpu_model

        # Construct a json representation of a AutoscalingGroup model
        autoscaling_group_model_json = {}
        autoscaling_group_model_json['autoscaling'] = autoscaling_group_autoscaling_model

        # Construct a model instance of AutoscalingGroup by calling from_dict on the json representation
        autoscaling_group_model = AutoscalingGroup.from_dict(autoscaling_group_model_json)
        assert autoscaling_group_model != False

        # Construct a model instance of AutoscalingGroup by calling from_dict on the json representation
        autoscaling_group_model_dict = AutoscalingGroup.from_dict(autoscaling_group_model_json).__dict__
        autoscaling_group_model2 = AutoscalingGroup(**autoscaling_group_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_group_model == autoscaling_group_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_group_model_json2 = autoscaling_group_model.to_dict()
        assert autoscaling_group_model_json2 == autoscaling_group_model_json

class TestAutoscalingGroupAutoscaling():
    """
    Test Class for AutoscalingGroupAutoscaling
    """

    def test_autoscaling_group_autoscaling_serialization(self):
        """
        Test serialization/deserialization for AutoscalingGroupAutoscaling
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_disk_group_disk_scalers_capacity_model = {} # AutoscalingDiskGroupDiskScalersCapacity
        autoscaling_disk_group_disk_scalers_capacity_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model['free_space_less_than_percent'] = 10

        autoscaling_disk_group_disk_scalers_io_utilization_model = {} # AutoscalingDiskGroupDiskScalersIoUtilization
        autoscaling_disk_group_disk_scalers_io_utilization_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_disk_group_disk_scalers_model = {} # AutoscalingDiskGroupDiskScalers
        autoscaling_disk_group_disk_scalers_model['capacity'] = autoscaling_disk_group_disk_scalers_capacity_model
        autoscaling_disk_group_disk_scalers_model['io_utilization'] = autoscaling_disk_group_disk_scalers_io_utilization_model

        autoscaling_disk_group_disk_rate_model = {} # AutoscalingDiskGroupDiskRate
        autoscaling_disk_group_disk_rate_model['increase_percent'] = 20
        autoscaling_disk_group_disk_rate_model['period_seconds'] = 900
        autoscaling_disk_group_disk_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_disk_group_disk_rate_model['units'] = 'mb'

        autoscaling_disk_group_disk_model = {} # AutoscalingDiskGroupDisk
        autoscaling_disk_group_disk_model['scalers'] = autoscaling_disk_group_disk_scalers_model
        autoscaling_disk_group_disk_model['rate'] = autoscaling_disk_group_disk_rate_model

        autoscaling_memory_group_memory_scalers_io_utilization_model = {} # AutoscalingMemoryGroupMemoryScalersIoUtilization
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_memory_group_memory_scalers_model = {} # AutoscalingMemoryGroupMemoryScalers
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        autoscaling_memory_group_memory_rate_model = {} # AutoscalingMemoryGroupMemoryRate
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 900
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        autoscaling_memory_group_memory_model = {} # AutoscalingMemoryGroupMemory
        autoscaling_memory_group_memory_model['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model['rate'] = autoscaling_memory_group_memory_rate_model

        autoscaling_cpu_group_cpu_rate_model = {} # AutoscalingCPUGroupCPURate
        autoscaling_cpu_group_cpu_rate_model['increase_percent'] = 10
        autoscaling_cpu_group_cpu_rate_model['period_seconds'] = 900
        autoscaling_cpu_group_cpu_rate_model['limit_count_per_member'] = 10
        autoscaling_cpu_group_cpu_rate_model['units'] = 'count'

        autoscaling_cpu_group_cpu_model = {} # AutoscalingCPUGroupCPU
        autoscaling_cpu_group_cpu_model['scalers'] = { 'foo': 'bar' }
        autoscaling_cpu_group_cpu_model['rate'] = autoscaling_cpu_group_cpu_rate_model

        # Construct a json representation of a AutoscalingGroupAutoscaling model
        autoscaling_group_autoscaling_model_json = {}
        autoscaling_group_autoscaling_model_json['disk'] = autoscaling_disk_group_disk_model
        autoscaling_group_autoscaling_model_json['memory'] = autoscaling_memory_group_memory_model
        autoscaling_group_autoscaling_model_json['cpu'] = autoscaling_cpu_group_cpu_model

        # Construct a model instance of AutoscalingGroupAutoscaling by calling from_dict on the json representation
        autoscaling_group_autoscaling_model = AutoscalingGroupAutoscaling.from_dict(autoscaling_group_autoscaling_model_json)
        assert autoscaling_group_autoscaling_model != False

        # Construct a model instance of AutoscalingGroupAutoscaling by calling from_dict on the json representation
        autoscaling_group_autoscaling_model_dict = AutoscalingGroupAutoscaling.from_dict(autoscaling_group_autoscaling_model_json).__dict__
        autoscaling_group_autoscaling_model2 = AutoscalingGroupAutoscaling(**autoscaling_group_autoscaling_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_group_autoscaling_model == autoscaling_group_autoscaling_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_group_autoscaling_model_json2 = autoscaling_group_autoscaling_model.to_dict()
        assert autoscaling_group_autoscaling_model_json2 == autoscaling_group_autoscaling_model_json

class TestAutoscalingMemoryGroupMemory():
    """
    Test Class for AutoscalingMemoryGroupMemory
    """

    def test_autoscaling_memory_group_memory_serialization(self):
        """
        Test serialization/deserialization for AutoscalingMemoryGroupMemory
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_memory_group_memory_scalers_io_utilization_model = {} # AutoscalingMemoryGroupMemoryScalersIoUtilization
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_memory_group_memory_scalers_model = {} # AutoscalingMemoryGroupMemoryScalers
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        autoscaling_memory_group_memory_rate_model = {} # AutoscalingMemoryGroupMemoryRate
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 900
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        # Construct a json representation of a AutoscalingMemoryGroupMemory model
        autoscaling_memory_group_memory_model_json = {}
        autoscaling_memory_group_memory_model_json['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model_json['rate'] = autoscaling_memory_group_memory_rate_model

        # Construct a model instance of AutoscalingMemoryGroupMemory by calling from_dict on the json representation
        autoscaling_memory_group_memory_model = AutoscalingMemoryGroupMemory.from_dict(autoscaling_memory_group_memory_model_json)
        assert autoscaling_memory_group_memory_model != False

        # Construct a model instance of AutoscalingMemoryGroupMemory by calling from_dict on the json representation
        autoscaling_memory_group_memory_model_dict = AutoscalingMemoryGroupMemory.from_dict(autoscaling_memory_group_memory_model_json).__dict__
        autoscaling_memory_group_memory_model2 = AutoscalingMemoryGroupMemory(**autoscaling_memory_group_memory_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_memory_group_memory_model == autoscaling_memory_group_memory_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_memory_group_memory_model_json2 = autoscaling_memory_group_memory_model.to_dict()
        assert autoscaling_memory_group_memory_model_json2 == autoscaling_memory_group_memory_model_json

class TestAutoscalingMemoryGroupMemoryRate():
    """
    Test Class for AutoscalingMemoryGroupMemoryRate
    """

    def test_autoscaling_memory_group_memory_rate_serialization(self):
        """
        Test serialization/deserialization for AutoscalingMemoryGroupMemoryRate
        """

        # Construct a json representation of a AutoscalingMemoryGroupMemoryRate model
        autoscaling_memory_group_memory_rate_model_json = {}
        autoscaling_memory_group_memory_rate_model_json['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model_json['period_seconds'] = 900
        autoscaling_memory_group_memory_rate_model_json['limit_mb_per_member'] = 3670016
        autoscaling_memory_group_memory_rate_model_json['units'] = 'mb'

        # Construct a model instance of AutoscalingMemoryGroupMemoryRate by calling from_dict on the json representation
        autoscaling_memory_group_memory_rate_model = AutoscalingMemoryGroupMemoryRate.from_dict(autoscaling_memory_group_memory_rate_model_json)
        assert autoscaling_memory_group_memory_rate_model != False

        # Construct a model instance of AutoscalingMemoryGroupMemoryRate by calling from_dict on the json representation
        autoscaling_memory_group_memory_rate_model_dict = AutoscalingMemoryGroupMemoryRate.from_dict(autoscaling_memory_group_memory_rate_model_json).__dict__
        autoscaling_memory_group_memory_rate_model2 = AutoscalingMemoryGroupMemoryRate(**autoscaling_memory_group_memory_rate_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_memory_group_memory_rate_model == autoscaling_memory_group_memory_rate_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_memory_group_memory_rate_model_json2 = autoscaling_memory_group_memory_rate_model.to_dict()
        assert autoscaling_memory_group_memory_rate_model_json2 == autoscaling_memory_group_memory_rate_model_json

class TestAutoscalingMemoryGroupMemoryScalers():
    """
    Test Class for AutoscalingMemoryGroupMemoryScalers
    """

    def test_autoscaling_memory_group_memory_scalers_serialization(self):
        """
        Test serialization/deserialization for AutoscalingMemoryGroupMemoryScalers
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_memory_group_memory_scalers_io_utilization_model = {} # AutoscalingMemoryGroupMemoryScalersIoUtilization
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 45

        # Construct a json representation of a AutoscalingMemoryGroupMemoryScalers model
        autoscaling_memory_group_memory_scalers_model_json = {}
        autoscaling_memory_group_memory_scalers_model_json['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        # Construct a model instance of AutoscalingMemoryGroupMemoryScalers by calling from_dict on the json representation
        autoscaling_memory_group_memory_scalers_model = AutoscalingMemoryGroupMemoryScalers.from_dict(autoscaling_memory_group_memory_scalers_model_json)
        assert autoscaling_memory_group_memory_scalers_model != False

        # Construct a model instance of AutoscalingMemoryGroupMemoryScalers by calling from_dict on the json representation
        autoscaling_memory_group_memory_scalers_model_dict = AutoscalingMemoryGroupMemoryScalers.from_dict(autoscaling_memory_group_memory_scalers_model_json).__dict__
        autoscaling_memory_group_memory_scalers_model2 = AutoscalingMemoryGroupMemoryScalers(**autoscaling_memory_group_memory_scalers_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_memory_group_memory_scalers_model == autoscaling_memory_group_memory_scalers_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_memory_group_memory_scalers_model_json2 = autoscaling_memory_group_memory_scalers_model.to_dict()
        assert autoscaling_memory_group_memory_scalers_model_json2 == autoscaling_memory_group_memory_scalers_model_json

class TestAutoscalingMemoryGroupMemoryScalersIoUtilization():
    """
    Test Class for AutoscalingMemoryGroupMemoryScalersIoUtilization
    """

    def test_autoscaling_memory_group_memory_scalers_io_utilization_serialization(self):
        """
        Test serialization/deserialization for AutoscalingMemoryGroupMemoryScalersIoUtilization
        """

        # Construct a json representation of a AutoscalingMemoryGroupMemoryScalersIoUtilization model
        autoscaling_memory_group_memory_scalers_io_utilization_model_json = {}
        autoscaling_memory_group_memory_scalers_io_utilization_model_json['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model_json['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model_json['above_percent'] = 45

        # Construct a model instance of AutoscalingMemoryGroupMemoryScalersIoUtilization by calling from_dict on the json representation
        autoscaling_memory_group_memory_scalers_io_utilization_model = AutoscalingMemoryGroupMemoryScalersIoUtilization.from_dict(autoscaling_memory_group_memory_scalers_io_utilization_model_json)
        assert autoscaling_memory_group_memory_scalers_io_utilization_model != False

        # Construct a model instance of AutoscalingMemoryGroupMemoryScalersIoUtilization by calling from_dict on the json representation
        autoscaling_memory_group_memory_scalers_io_utilization_model_dict = AutoscalingMemoryGroupMemoryScalersIoUtilization.from_dict(autoscaling_memory_group_memory_scalers_io_utilization_model_json).__dict__
        autoscaling_memory_group_memory_scalers_io_utilization_model2 = AutoscalingMemoryGroupMemoryScalersIoUtilization(**autoscaling_memory_group_memory_scalers_io_utilization_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_memory_group_memory_scalers_io_utilization_model == autoscaling_memory_group_memory_scalers_io_utilization_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_memory_group_memory_scalers_io_utilization_model_json2 = autoscaling_memory_group_memory_scalers_io_utilization_model.to_dict()
        assert autoscaling_memory_group_memory_scalers_io_utilization_model_json2 == autoscaling_memory_group_memory_scalers_io_utilization_model_json

class TestBackup():
    """
    Test Class for Backup
    """

    def test_backup_serialization(self):
        """
        Test serialization/deserialization for Backup
        """

        # Construct a json representation of a Backup model
        backup_model_json = {}
        backup_model_json['id'] = '5a970218cb7544000671c094'
        backup_model_json['deployment_id'] = '595eada310b7ac00116dd48b'
        backup_model_json['type'] = 'scheduled'
        backup_model_json['status'] = 'running'
        backup_model_json['is_downloadable'] = True
        backup_model_json['is_restorable'] = True
        backup_model_json['created_at'] = datetime_to_string(string_to_datetime("2018-02-28T19:25:12.000Z"))

        # Construct a model instance of Backup by calling from_dict on the json representation
        backup_model = Backup.from_dict(backup_model_json)
        assert backup_model != False

        # Construct a model instance of Backup by calling from_dict on the json representation
        backup_model_dict = Backup.from_dict(backup_model_json).__dict__
        backup_model2 = Backup(**backup_model_dict)

        # Verify the model instances are equivalent
        assert backup_model == backup_model2

        # Convert model instance back to dict and verify no loss of data
        backup_model_json2 = backup_model.to_dict()
        assert backup_model_json2 == backup_model_json

class TestBackups():
    """
    Test Class for Backups
    """

    def test_backups_serialization(self):
        """
        Test serialization/deserialization for Backups
        """

        # Construct dict forms of any model objects needed in order to build this model.

        backup_model = {} # Backup
        backup_model['id'] = 'crn:v1:bluemix:public:databases-for-elasticsearch:us-south:a/2740839ce64e9c423ffc238516c755e1:afa742a3-6f83-4f6e-a06e-b5c501e9e87a:backup:e47213d6-4a13-47f4-a511-9ef459670192'
        backup_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-elasticsearch:us-south:a/2740839ce64e9c423ffc238516c755e1:afa742a3-6f83-4f6e-a06e-b5c501e9e87a::'
        backup_model['type'] = 'scheduled'
        backup_model['status'] = 'completed'
        backup_model['is_downloadable'] = False
        backup_model['is_restorable'] = True
        backup_model['created_at'] = datetime_to_string(string_to_datetime("2019-05-29T14:30:46.000Z"))

        # Construct a json representation of a Backups model
        backups_model_json = {}
        backups_model_json['backups'] = [backup_model]

        # Construct a model instance of Backups by calling from_dict on the json representation
        backups_model = Backups.from_dict(backups_model_json)
        assert backups_model != False

        # Construct a model instance of Backups by calling from_dict on the json representation
        backups_model_dict = Backups.from_dict(backups_model_json).__dict__
        backups_model2 = Backups(**backups_model_dict)

        # Verify the model instances are equivalent
        assert backups_model == backups_model2

        # Convert model instance back to dict and verify no loss of data
        backups_model_json2 = backups_model.to_dict()
        assert backups_model_json2 == backups_model_json

class TestChangeUserPasswordResponse():
    """
    Test Class for ChangeUserPasswordResponse
    """

    def test_change_user_password_response_serialization(self):
        """
        Test serialization/deserialization for ChangeUserPasswordResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-b5c96544393b'
        task_model['description'] = 'Setting user password for database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:22:30Z"))

        # Construct a json representation of a ChangeUserPasswordResponse model
        change_user_password_response_model_json = {}
        change_user_password_response_model_json['task'] = task_model

        # Construct a model instance of ChangeUserPasswordResponse by calling from_dict on the json representation
        change_user_password_response_model = ChangeUserPasswordResponse.from_dict(change_user_password_response_model_json)
        assert change_user_password_response_model != False

        # Construct a model instance of ChangeUserPasswordResponse by calling from_dict on the json representation
        change_user_password_response_model_dict = ChangeUserPasswordResponse.from_dict(change_user_password_response_model_json).__dict__
        change_user_password_response_model2 = ChangeUserPasswordResponse(**change_user_password_response_model_dict)

        # Verify the model instances are equivalent
        assert change_user_password_response_model == change_user_password_response_model2

        # Convert model instance back to dict and verify no loss of data
        change_user_password_response_model_json2 = change_user_password_response_model.to_dict()
        assert change_user_password_response_model_json2 == change_user_password_response_model_json

class TestConnection():
    """
    Test Class for Connection
    """

    def test_connection_serialization(self):
        """
        Test serialization/deserialization for Connection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        postgre_sql_connection_uri_hosts_item_model = {} # PostgreSQLConnectionURIHostsItem
        postgre_sql_connection_uri_hosts_item_model['hostname'] = 'testString'
        postgre_sql_connection_uri_hosts_item_model['port'] = 38

        postgre_sql_connection_uri_authentication_model = {} # PostgreSQLConnectionURIAuthentication
        postgre_sql_connection_uri_authentication_model['method'] = 'testString'
        postgre_sql_connection_uri_authentication_model['username'] = 'testString'
        postgre_sql_connection_uri_authentication_model['password'] = 'testString'

        postgre_sql_connection_uri_certificate_model = {} # PostgreSQLConnectionURICertificate
        postgre_sql_connection_uri_certificate_model['name'] = 'testString'
        postgre_sql_connection_uri_certificate_model['certificate_base64'] = 'testString'

        postgre_sql_connection_uri_model = {} # PostgreSQLConnectionURI
        postgre_sql_connection_uri_model['type'] = 'uri'
        postgre_sql_connection_uri_model['composed'] = ['testString']
        postgre_sql_connection_uri_model['scheme'] = 'testString'
        postgre_sql_connection_uri_model['hosts'] = [postgre_sql_connection_uri_hosts_item_model]
        postgre_sql_connection_uri_model['path'] = '/ibmclouddb'
        postgre_sql_connection_uri_model['query_options'] = { 'foo': 'bar' }
        postgre_sql_connection_uri_model['authentication'] = postgre_sql_connection_uri_authentication_model
        postgre_sql_connection_uri_model['certificate'] = postgre_sql_connection_uri_certificate_model
        postgre_sql_connection_uri_model['database'] = 'testString'

        connection_cli_certificate_model = {} # ConnectionCLICertificate
        connection_cli_certificate_model['name'] = 'testString'
        connection_cli_certificate_model['certificate_base64'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_cli_certificate_model

        connection_connection_model = {} # ConnectionConnectionPostgreSQLConnection
        connection_connection_model['postgres'] = postgre_sql_connection_uri_model
        connection_connection_model['cli'] = connection_cli_model

        # Construct a json representation of a Connection model
        connection_model_json = {}
        connection_model_json['connection'] = connection_connection_model

        # Construct a model instance of Connection by calling from_dict on the json representation
        connection_model = Connection.from_dict(connection_model_json)
        assert connection_model != False

        # Construct a model instance of Connection by calling from_dict on the json representation
        connection_model_dict = Connection.from_dict(connection_model_json).__dict__
        connection_model2 = Connection(**connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_model == connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_model_json2 = connection_model.to_dict()
        assert connection_model_json2 == connection_model_json

class TestConnectionCLI():
    """
    Test Class for ConnectionCLI
    """

    def test_connection_cli_serialization(self):
        """
        Test serialization/deserialization for ConnectionCLI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_cli_certificate_model = {} # ConnectionCLICertificate
        connection_cli_certificate_model['name'] = 'testString'
        connection_cli_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a ConnectionCLI model
        connection_cli_model_json = {}
        connection_cli_model_json['type'] = 'cli'
        connection_cli_model_json['composed'] = ['testString']
        connection_cli_model_json['environment'] = {}
        connection_cli_model_json['bin'] = 'testString'
        connection_cli_model_json['arguments'] = [['testString']]
        connection_cli_model_json['certificate'] = connection_cli_certificate_model

        # Construct a model instance of ConnectionCLI by calling from_dict on the json representation
        connection_cli_model = ConnectionCLI.from_dict(connection_cli_model_json)
        assert connection_cli_model != False

        # Construct a model instance of ConnectionCLI by calling from_dict on the json representation
        connection_cli_model_dict = ConnectionCLI.from_dict(connection_cli_model_json).__dict__
        connection_cli_model2 = ConnectionCLI(**connection_cli_model_dict)

        # Verify the model instances are equivalent
        assert connection_cli_model == connection_cli_model2

        # Convert model instance back to dict and verify no loss of data
        connection_cli_model_json2 = connection_cli_model.to_dict()
        assert connection_cli_model_json2 == connection_cli_model_json

class TestConnectionCLICertificate():
    """
    Test Class for ConnectionCLICertificate
    """

    def test_connection_cli_certificate_serialization(self):
        """
        Test serialization/deserialization for ConnectionCLICertificate
        """

        # Construct a json representation of a ConnectionCLICertificate model
        connection_cli_certificate_model_json = {}
        connection_cli_certificate_model_json['name'] = 'testString'
        connection_cli_certificate_model_json['certificate_base64'] = 'testString'

        # Construct a model instance of ConnectionCLICertificate by calling from_dict on the json representation
        connection_cli_certificate_model = ConnectionCLICertificate.from_dict(connection_cli_certificate_model_json)
        assert connection_cli_certificate_model != False

        # Construct a model instance of ConnectionCLICertificate by calling from_dict on the json representation
        connection_cli_certificate_model_dict = ConnectionCLICertificate.from_dict(connection_cli_certificate_model_json).__dict__
        connection_cli_certificate_model2 = ConnectionCLICertificate(**connection_cli_certificate_model_dict)

        # Verify the model instances are equivalent
        assert connection_cli_certificate_model == connection_cli_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        connection_cli_certificate_model_json2 = connection_cli_certificate_model.to_dict()
        assert connection_cli_certificate_model_json2 == connection_cli_certificate_model_json

class TestCreateDatabaseUserRequestUser():
    """
    Test Class for CreateDatabaseUserRequestUser
    """

    def test_create_database_user_request_user_serialization(self):
        """
        Test serialization/deserialization for CreateDatabaseUserRequestUser
        """

        # Construct a json representation of a CreateDatabaseUserRequestUser model
        create_database_user_request_user_model_json = {}
        create_database_user_request_user_model_json['user_type'] = 'database'
        create_database_user_request_user_model_json['username'] = 'james'
        create_database_user_request_user_model_json['password'] = 'kickoutthe'

        # Construct a model instance of CreateDatabaseUserRequestUser by calling from_dict on the json representation
        create_database_user_request_user_model = CreateDatabaseUserRequestUser.from_dict(create_database_user_request_user_model_json)
        assert create_database_user_request_user_model != False

        # Construct a model instance of CreateDatabaseUserRequestUser by calling from_dict on the json representation
        create_database_user_request_user_model_dict = CreateDatabaseUserRequestUser.from_dict(create_database_user_request_user_model_json).__dict__
        create_database_user_request_user_model2 = CreateDatabaseUserRequestUser(**create_database_user_request_user_model_dict)

        # Verify the model instances are equivalent
        assert create_database_user_request_user_model == create_database_user_request_user_model2

        # Convert model instance back to dict and verify no loss of data
        create_database_user_request_user_model_json2 = create_database_user_request_user_model.to_dict()
        assert create_database_user_request_user_model_json2 == create_database_user_request_user_model_json

class TestCreateDatabaseUserResponse():
    """
    Test Class for CreateDatabaseUserResponse
    """

    def test_create_database_user_response_serialization(self):
        """
        Test serialization/deserialization for CreateDatabaseUserResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-b5c96544393b'
        task_model['description'] = 'Creating user for database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:21:30Z"))

        # Construct a json representation of a CreateDatabaseUserResponse model
        create_database_user_response_model_json = {}
        create_database_user_response_model_json['task'] = task_model

        # Construct a model instance of CreateDatabaseUserResponse by calling from_dict on the json representation
        create_database_user_response_model = CreateDatabaseUserResponse.from_dict(create_database_user_response_model_json)
        assert create_database_user_response_model != False

        # Construct a model instance of CreateDatabaseUserResponse by calling from_dict on the json representation
        create_database_user_response_model_dict = CreateDatabaseUserResponse.from_dict(create_database_user_response_model_json).__dict__
        create_database_user_response_model2 = CreateDatabaseUserResponse(**create_database_user_response_model_dict)

        # Verify the model instances are equivalent
        assert create_database_user_response_model == create_database_user_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_database_user_response_model_json2 = create_database_user_response_model.to_dict()
        assert create_database_user_response_model_json2 == create_database_user_response_model_json

class TestDeleteAllowlistEntryResponse():
    """
    Test Class for DeleteAllowlistEntryResponse
    """

    def test_delete_allowlist_entry_response_serialization(self):
        """
        Test serialization/deserialization for DeleteAllowlistEntryResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4d36-92f3-b5c96544393b'
        task_model['description'] = 'Deleting allowlist entry for database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 15
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:25:30Z"))

        # Construct a json representation of a DeleteAllowlistEntryResponse model
        delete_allowlist_entry_response_model_json = {}
        delete_allowlist_entry_response_model_json['task'] = task_model

        # Construct a model instance of DeleteAllowlistEntryResponse by calling from_dict on the json representation
        delete_allowlist_entry_response_model = DeleteAllowlistEntryResponse.from_dict(delete_allowlist_entry_response_model_json)
        assert delete_allowlist_entry_response_model != False

        # Construct a model instance of DeleteAllowlistEntryResponse by calling from_dict on the json representation
        delete_allowlist_entry_response_model_dict = DeleteAllowlistEntryResponse.from_dict(delete_allowlist_entry_response_model_json).__dict__
        delete_allowlist_entry_response_model2 = DeleteAllowlistEntryResponse(**delete_allowlist_entry_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_allowlist_entry_response_model == delete_allowlist_entry_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_allowlist_entry_response_model_json2 = delete_allowlist_entry_response_model.to_dict()
        assert delete_allowlist_entry_response_model_json2 == delete_allowlist_entry_response_model_json

class TestDeleteDatabaseUserResponse():
    """
    Test Class for DeleteDatabaseUserResponse
    """

    def test_delete_database_user_response_serialization(self):
        """
        Test serialization/deserialization for DeleteDatabaseUserResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-b5c96555393b'
        task_model['description'] = 'Deleting user from database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-99bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 10
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:23:30Z"))

        # Construct a json representation of a DeleteDatabaseUserResponse model
        delete_database_user_response_model_json = {}
        delete_database_user_response_model_json['task'] = task_model

        # Construct a model instance of DeleteDatabaseUserResponse by calling from_dict on the json representation
        delete_database_user_response_model = DeleteDatabaseUserResponse.from_dict(delete_database_user_response_model_json)
        assert delete_database_user_response_model != False

        # Construct a model instance of DeleteDatabaseUserResponse by calling from_dict on the json representation
        delete_database_user_response_model_dict = DeleteDatabaseUserResponse.from_dict(delete_database_user_response_model_json).__dict__
        delete_database_user_response_model2 = DeleteDatabaseUserResponse(**delete_database_user_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_database_user_response_model == delete_database_user_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_database_user_response_model_json2 = delete_database_user_response_model.to_dict()
        assert delete_database_user_response_model_json2 == delete_database_user_response_model_json

class TestDeployables():
    """
    Test Class for Deployables
    """

    def test_deployables_serialization(self):
        """
        Test serialization/deserialization for Deployables
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deployables_versions_item_transitions_item_model = {} # DeployablesVersionsItemTransitionsItem
        deployables_versions_item_transitions_item_model['application'] = 'elasticsearch'
        deployables_versions_item_transitions_item_model['method'] = 'restore'
        deployables_versions_item_transitions_item_model['from_version'] = '5.6'
        deployables_versions_item_transitions_item_model['to_version'] = '6.7'

        deployables_versions_item_model = {} # DeployablesVersionsItem
        deployables_versions_item_model['version'] = '5.6'
        deployables_versions_item_model['status'] = 'stable'
        deployables_versions_item_model['is_preferred'] = True
        deployables_versions_item_model['transitions'] = [deployables_versions_item_transitions_item_model]

        # Construct a json representation of a Deployables model
        deployables_model_json = {}
        deployables_model_json['type'] = 'elasticsearch'
        deployables_model_json['versions'] = [deployables_versions_item_model]

        # Construct a model instance of Deployables by calling from_dict on the json representation
        deployables_model = Deployables.from_dict(deployables_model_json)
        assert deployables_model != False

        # Construct a model instance of Deployables by calling from_dict on the json representation
        deployables_model_dict = Deployables.from_dict(deployables_model_json).__dict__
        deployables_model2 = Deployables(**deployables_model_dict)

        # Verify the model instances are equivalent
        assert deployables_model == deployables_model2

        # Convert model instance back to dict and verify no loss of data
        deployables_model_json2 = deployables_model.to_dict()
        assert deployables_model_json2 == deployables_model_json

class TestDeployablesVersionsItem():
    """
    Test Class for DeployablesVersionsItem
    """

    def test_deployables_versions_item_serialization(self):
        """
        Test serialization/deserialization for DeployablesVersionsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deployables_versions_item_transitions_item_model = {} # DeployablesVersionsItemTransitionsItem
        deployables_versions_item_transitions_item_model['application'] = 'elasticsearch'
        deployables_versions_item_transitions_item_model['method'] = 'restore'
        deployables_versions_item_transitions_item_model['from_version'] = '5.6'
        deployables_versions_item_transitions_item_model['to_version'] = '6.7'

        # Construct a json representation of a DeployablesVersionsItem model
        deployables_versions_item_model_json = {}
        deployables_versions_item_model_json['version'] = '5.6'
        deployables_versions_item_model_json['status'] = 'stable'
        deployables_versions_item_model_json['is_preferred'] = True
        deployables_versions_item_model_json['transitions'] = [deployables_versions_item_transitions_item_model]

        # Construct a model instance of DeployablesVersionsItem by calling from_dict on the json representation
        deployables_versions_item_model = DeployablesVersionsItem.from_dict(deployables_versions_item_model_json)
        assert deployables_versions_item_model != False

        # Construct a model instance of DeployablesVersionsItem by calling from_dict on the json representation
        deployables_versions_item_model_dict = DeployablesVersionsItem.from_dict(deployables_versions_item_model_json).__dict__
        deployables_versions_item_model2 = DeployablesVersionsItem(**deployables_versions_item_model_dict)

        # Verify the model instances are equivalent
        assert deployables_versions_item_model == deployables_versions_item_model2

        # Convert model instance back to dict and verify no loss of data
        deployables_versions_item_model_json2 = deployables_versions_item_model.to_dict()
        assert deployables_versions_item_model_json2 == deployables_versions_item_model_json

class TestDeployablesVersionsItemTransitionsItem():
    """
    Test Class for DeployablesVersionsItemTransitionsItem
    """

    def test_deployables_versions_item_transitions_item_serialization(self):
        """
        Test serialization/deserialization for DeployablesVersionsItemTransitionsItem
        """

        # Construct a json representation of a DeployablesVersionsItemTransitionsItem model
        deployables_versions_item_transitions_item_model_json = {}
        deployables_versions_item_transitions_item_model_json['application'] = 'elasticsearch'
        deployables_versions_item_transitions_item_model_json['method'] = 'restore'
        deployables_versions_item_transitions_item_model_json['from_version'] = '5.6'
        deployables_versions_item_transitions_item_model_json['to_version'] = '6.7'

        # Construct a model instance of DeployablesVersionsItemTransitionsItem by calling from_dict on the json representation
        deployables_versions_item_transitions_item_model = DeployablesVersionsItemTransitionsItem.from_dict(deployables_versions_item_transitions_item_model_json)
        assert deployables_versions_item_transitions_item_model != False

        # Construct a model instance of DeployablesVersionsItemTransitionsItem by calling from_dict on the json representation
        deployables_versions_item_transitions_item_model_dict = DeployablesVersionsItemTransitionsItem.from_dict(deployables_versions_item_transitions_item_model_json).__dict__
        deployables_versions_item_transitions_item_model2 = DeployablesVersionsItemTransitionsItem(**deployables_versions_item_transitions_item_model_dict)

        # Verify the model instances are equivalent
        assert deployables_versions_item_transitions_item_model == deployables_versions_item_transitions_item_model2

        # Convert model instance back to dict and verify no loss of data
        deployables_versions_item_transitions_item_model_json2 = deployables_versions_item_transitions_item_model.to_dict()
        assert deployables_versions_item_transitions_item_model_json2 == deployables_versions_item_transitions_item_model_json

class TestDeployment():
    """
    Test Class for Deployment
    """

    def test_deployment_serialization(self):
        """
        Test serialization/deserialization for Deployment
        """

        # Construct a json representation of a Deployment model
        deployment_model_json = {}
        deployment_model_json['id'] = 'crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::'
        deployment_model_json['name'] = 'crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::'
        deployment_model_json['type'] = 'redis'
        deployment_model_json['platform_options'] = { 'foo': 'bar' }
        deployment_model_json['version'] = '4'
        deployment_model_json['admin_usernames'] = {}
        deployment_model_json['enable_public_endpoints'] = True
        deployment_model_json['enable_private_endpoints'] = False

        # Construct a model instance of Deployment by calling from_dict on the json representation
        deployment_model = Deployment.from_dict(deployment_model_json)
        assert deployment_model != False

        # Construct a model instance of Deployment by calling from_dict on the json representation
        deployment_model_dict = Deployment.from_dict(deployment_model_json).__dict__
        deployment_model2 = Deployment(**deployment_model_dict)

        # Verify the model instances are equivalent
        assert deployment_model == deployment_model2

        # Convert model instance back to dict and verify no loss of data
        deployment_model_json2 = deployment_model.to_dict()
        assert deployment_model_json2 == deployment_model_json

class TestElasticsearchConnectionHTTPS():
    """
    Test Class for ElasticsearchConnectionHTTPS
    """

    def test_elasticsearch_connection_https_serialization(self):
        """
        Test serialization/deserialization for ElasticsearchConnectionHTTPS
        """

        # Construct dict forms of any model objects needed in order to build this model.

        elasticsearch_connection_https_hosts_item_model = {} # ElasticsearchConnectionHTTPSHostsItem
        elasticsearch_connection_https_hosts_item_model['hostname'] = 'testString'
        elasticsearch_connection_https_hosts_item_model['port'] = 38

        elasticsearch_connection_https_authentication_model = {} # ElasticsearchConnectionHTTPSAuthentication
        elasticsearch_connection_https_authentication_model['method'] = 'testString'
        elasticsearch_connection_https_authentication_model['username'] = 'testString'
        elasticsearch_connection_https_authentication_model['password'] = 'testString'

        elasticsearch_connection_https_certificate_model = {} # ElasticsearchConnectionHTTPSCertificate
        elasticsearch_connection_https_certificate_model['name'] = 'testString'
        elasticsearch_connection_https_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a ElasticsearchConnectionHTTPS model
        elasticsearch_connection_https_model_json = {}
        elasticsearch_connection_https_model_json['type'] = 'uri'
        elasticsearch_connection_https_model_json['composed'] = ['testString']
        elasticsearch_connection_https_model_json['scheme'] = 'testString'
        elasticsearch_connection_https_model_json['hosts'] = [elasticsearch_connection_https_hosts_item_model]
        elasticsearch_connection_https_model_json['path'] = 'testString'
        elasticsearch_connection_https_model_json['query_options'] = { 'foo': 'bar' }
        elasticsearch_connection_https_model_json['authentication'] = elasticsearch_connection_https_authentication_model
        elasticsearch_connection_https_model_json['certificate'] = elasticsearch_connection_https_certificate_model

        # Construct a model instance of ElasticsearchConnectionHTTPS by calling from_dict on the json representation
        elasticsearch_connection_https_model = ElasticsearchConnectionHTTPS.from_dict(elasticsearch_connection_https_model_json)
        assert elasticsearch_connection_https_model != False

        # Construct a model instance of ElasticsearchConnectionHTTPS by calling from_dict on the json representation
        elasticsearch_connection_https_model_dict = ElasticsearchConnectionHTTPS.from_dict(elasticsearch_connection_https_model_json).__dict__
        elasticsearch_connection_https_model2 = ElasticsearchConnectionHTTPS(**elasticsearch_connection_https_model_dict)

        # Verify the model instances are equivalent
        assert elasticsearch_connection_https_model == elasticsearch_connection_https_model2

        # Convert model instance back to dict and verify no loss of data
        elasticsearch_connection_https_model_json2 = elasticsearch_connection_https_model.to_dict()
        assert elasticsearch_connection_https_model_json2 == elasticsearch_connection_https_model_json

class TestElasticsearchConnectionHTTPSAuthentication():
    """
    Test Class for ElasticsearchConnectionHTTPSAuthentication
    """

    def test_elasticsearch_connection_https_authentication_serialization(self):
        """
        Test serialization/deserialization for ElasticsearchConnectionHTTPSAuthentication
        """

        # Construct a json representation of a ElasticsearchConnectionHTTPSAuthentication model
        elasticsearch_connection_https_authentication_model_json = {}
        elasticsearch_connection_https_authentication_model_json['method'] = 'testString'
        elasticsearch_connection_https_authentication_model_json['username'] = 'testString'
        elasticsearch_connection_https_authentication_model_json['password'] = 'testString'

        # Construct a model instance of ElasticsearchConnectionHTTPSAuthentication by calling from_dict on the json representation
        elasticsearch_connection_https_authentication_model = ElasticsearchConnectionHTTPSAuthentication.from_dict(elasticsearch_connection_https_authentication_model_json)
        assert elasticsearch_connection_https_authentication_model != False

        # Construct a model instance of ElasticsearchConnectionHTTPSAuthentication by calling from_dict on the json representation
        elasticsearch_connection_https_authentication_model_dict = ElasticsearchConnectionHTTPSAuthentication.from_dict(elasticsearch_connection_https_authentication_model_json).__dict__
        elasticsearch_connection_https_authentication_model2 = ElasticsearchConnectionHTTPSAuthentication(**elasticsearch_connection_https_authentication_model_dict)

        # Verify the model instances are equivalent
        assert elasticsearch_connection_https_authentication_model == elasticsearch_connection_https_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        elasticsearch_connection_https_authentication_model_json2 = elasticsearch_connection_https_authentication_model.to_dict()
        assert elasticsearch_connection_https_authentication_model_json2 == elasticsearch_connection_https_authentication_model_json

class TestElasticsearchConnectionHTTPSCertificate():
    """
    Test Class for ElasticsearchConnectionHTTPSCertificate
    """

    def test_elasticsearch_connection_https_certificate_serialization(self):
        """
        Test serialization/deserialization for ElasticsearchConnectionHTTPSCertificate
        """

        # Construct a json representation of a ElasticsearchConnectionHTTPSCertificate model
        elasticsearch_connection_https_certificate_model_json = {}
        elasticsearch_connection_https_certificate_model_json['name'] = 'testString'
        elasticsearch_connection_https_certificate_model_json['certificate_base64'] = 'testString'

        # Construct a model instance of ElasticsearchConnectionHTTPSCertificate by calling from_dict on the json representation
        elasticsearch_connection_https_certificate_model = ElasticsearchConnectionHTTPSCertificate.from_dict(elasticsearch_connection_https_certificate_model_json)
        assert elasticsearch_connection_https_certificate_model != False

        # Construct a model instance of ElasticsearchConnectionHTTPSCertificate by calling from_dict on the json representation
        elasticsearch_connection_https_certificate_model_dict = ElasticsearchConnectionHTTPSCertificate.from_dict(elasticsearch_connection_https_certificate_model_json).__dict__
        elasticsearch_connection_https_certificate_model2 = ElasticsearchConnectionHTTPSCertificate(**elasticsearch_connection_https_certificate_model_dict)

        # Verify the model instances are equivalent
        assert elasticsearch_connection_https_certificate_model == elasticsearch_connection_https_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        elasticsearch_connection_https_certificate_model_json2 = elasticsearch_connection_https_certificate_model.to_dict()
        assert elasticsearch_connection_https_certificate_model_json2 == elasticsearch_connection_https_certificate_model_json

class TestElasticsearchConnectionHTTPSHostsItem():
    """
    Test Class for ElasticsearchConnectionHTTPSHostsItem
    """

    def test_elasticsearch_connection_https_hosts_item_serialization(self):
        """
        Test serialization/deserialization for ElasticsearchConnectionHTTPSHostsItem
        """

        # Construct a json representation of a ElasticsearchConnectionHTTPSHostsItem model
        elasticsearch_connection_https_hosts_item_model_json = {}
        elasticsearch_connection_https_hosts_item_model_json['hostname'] = 'testString'
        elasticsearch_connection_https_hosts_item_model_json['port'] = 38

        # Construct a model instance of ElasticsearchConnectionHTTPSHostsItem by calling from_dict on the json representation
        elasticsearch_connection_https_hosts_item_model = ElasticsearchConnectionHTTPSHostsItem.from_dict(elasticsearch_connection_https_hosts_item_model_json)
        assert elasticsearch_connection_https_hosts_item_model != False

        # Construct a model instance of ElasticsearchConnectionHTTPSHostsItem by calling from_dict on the json representation
        elasticsearch_connection_https_hosts_item_model_dict = ElasticsearchConnectionHTTPSHostsItem.from_dict(elasticsearch_connection_https_hosts_item_model_json).__dict__
        elasticsearch_connection_https_hosts_item_model2 = ElasticsearchConnectionHTTPSHostsItem(**elasticsearch_connection_https_hosts_item_model_dict)

        # Verify the model instances are equivalent
        assert elasticsearch_connection_https_hosts_item_model == elasticsearch_connection_https_hosts_item_model2

        # Convert model instance back to dict and verify no loss of data
        elasticsearch_connection_https_hosts_item_model_json2 = elasticsearch_connection_https_hosts_item_model.to_dict()
        assert elasticsearch_connection_https_hosts_item_model_json2 == elasticsearch_connection_https_hosts_item_model_json

class TestGRPCConnectionURI():
    """
    Test Class for GRPCConnectionURI
    """

    def test_grpc_connection_uri_serialization(self):
        """
        Test serialization/deserialization for GRPCConnectionURI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        grpc_connection_uri_hosts_item_model = {} # GRPCConnectionURIHostsItem
        grpc_connection_uri_hosts_item_model['hostname'] = 'testString'
        grpc_connection_uri_hosts_item_model['port'] = 38

        grpc_connection_uri_authentication_model = {} # GRPCConnectionURIAuthentication
        grpc_connection_uri_authentication_model['method'] = 'testString'
        grpc_connection_uri_authentication_model['username'] = 'testString'
        grpc_connection_uri_authentication_model['password'] = 'testString'

        grpc_connection_uri_certificate_model = {} # GRPCConnectionURICertificate
        grpc_connection_uri_certificate_model['name'] = 'testString'
        grpc_connection_uri_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a GRPCConnectionURI model
        grpc_connection_uri_model_json = {}
        grpc_connection_uri_model_json['type'] = 'uri'
        grpc_connection_uri_model_json['composed'] = ['testString']
        grpc_connection_uri_model_json['scheme'] = 'testString'
        grpc_connection_uri_model_json['hosts'] = [grpc_connection_uri_hosts_item_model]
        grpc_connection_uri_model_json['path'] = 'testString'
        grpc_connection_uri_model_json['query_options'] = { 'foo': 'bar' }
        grpc_connection_uri_model_json['authentication'] = grpc_connection_uri_authentication_model
        grpc_connection_uri_model_json['certificate'] = grpc_connection_uri_certificate_model

        # Construct a model instance of GRPCConnectionURI by calling from_dict on the json representation
        grpc_connection_uri_model = GRPCConnectionURI.from_dict(grpc_connection_uri_model_json)
        assert grpc_connection_uri_model != False

        # Construct a model instance of GRPCConnectionURI by calling from_dict on the json representation
        grpc_connection_uri_model_dict = GRPCConnectionURI.from_dict(grpc_connection_uri_model_json).__dict__
        grpc_connection_uri_model2 = GRPCConnectionURI(**grpc_connection_uri_model_dict)

        # Verify the model instances are equivalent
        assert grpc_connection_uri_model == grpc_connection_uri_model2

        # Convert model instance back to dict and verify no loss of data
        grpc_connection_uri_model_json2 = grpc_connection_uri_model.to_dict()
        assert grpc_connection_uri_model_json2 == grpc_connection_uri_model_json

class TestGRPCConnectionURIAuthentication():
    """
    Test Class for GRPCConnectionURIAuthentication
    """

    def test_grpc_connection_uri_authentication_serialization(self):
        """
        Test serialization/deserialization for GRPCConnectionURIAuthentication
        """

        # Construct a json representation of a GRPCConnectionURIAuthentication model
        grpc_connection_uri_authentication_model_json = {}
        grpc_connection_uri_authentication_model_json['method'] = 'testString'
        grpc_connection_uri_authentication_model_json['username'] = 'testString'
        grpc_connection_uri_authentication_model_json['password'] = 'testString'

        # Construct a model instance of GRPCConnectionURIAuthentication by calling from_dict on the json representation
        grpc_connection_uri_authentication_model = GRPCConnectionURIAuthentication.from_dict(grpc_connection_uri_authentication_model_json)
        assert grpc_connection_uri_authentication_model != False

        # Construct a model instance of GRPCConnectionURIAuthentication by calling from_dict on the json representation
        grpc_connection_uri_authentication_model_dict = GRPCConnectionURIAuthentication.from_dict(grpc_connection_uri_authentication_model_json).__dict__
        grpc_connection_uri_authentication_model2 = GRPCConnectionURIAuthentication(**grpc_connection_uri_authentication_model_dict)

        # Verify the model instances are equivalent
        assert grpc_connection_uri_authentication_model == grpc_connection_uri_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        grpc_connection_uri_authentication_model_json2 = grpc_connection_uri_authentication_model.to_dict()
        assert grpc_connection_uri_authentication_model_json2 == grpc_connection_uri_authentication_model_json

class TestGRPCConnectionURICertificate():
    """
    Test Class for GRPCConnectionURICertificate
    """

    def test_grpc_connection_uri_certificate_serialization(self):
        """
        Test serialization/deserialization for GRPCConnectionURICertificate
        """

        # Construct a json representation of a GRPCConnectionURICertificate model
        grpc_connection_uri_certificate_model_json = {}
        grpc_connection_uri_certificate_model_json['name'] = 'testString'
        grpc_connection_uri_certificate_model_json['certificate_base64'] = 'testString'

        # Construct a model instance of GRPCConnectionURICertificate by calling from_dict on the json representation
        grpc_connection_uri_certificate_model = GRPCConnectionURICertificate.from_dict(grpc_connection_uri_certificate_model_json)
        assert grpc_connection_uri_certificate_model != False

        # Construct a model instance of GRPCConnectionURICertificate by calling from_dict on the json representation
        grpc_connection_uri_certificate_model_dict = GRPCConnectionURICertificate.from_dict(grpc_connection_uri_certificate_model_json).__dict__
        grpc_connection_uri_certificate_model2 = GRPCConnectionURICertificate(**grpc_connection_uri_certificate_model_dict)

        # Verify the model instances are equivalent
        assert grpc_connection_uri_certificate_model == grpc_connection_uri_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        grpc_connection_uri_certificate_model_json2 = grpc_connection_uri_certificate_model.to_dict()
        assert grpc_connection_uri_certificate_model_json2 == grpc_connection_uri_certificate_model_json

class TestGRPCConnectionURIHostsItem():
    """
    Test Class for GRPCConnectionURIHostsItem
    """

    def test_grpc_connection_uri_hosts_item_serialization(self):
        """
        Test serialization/deserialization for GRPCConnectionURIHostsItem
        """

        # Construct a json representation of a GRPCConnectionURIHostsItem model
        grpc_connection_uri_hosts_item_model_json = {}
        grpc_connection_uri_hosts_item_model_json['hostname'] = 'testString'
        grpc_connection_uri_hosts_item_model_json['port'] = 38

        # Construct a model instance of GRPCConnectionURIHostsItem by calling from_dict on the json representation
        grpc_connection_uri_hosts_item_model = GRPCConnectionURIHostsItem.from_dict(grpc_connection_uri_hosts_item_model_json)
        assert grpc_connection_uri_hosts_item_model != False

        # Construct a model instance of GRPCConnectionURIHostsItem by calling from_dict on the json representation
        grpc_connection_uri_hosts_item_model_dict = GRPCConnectionURIHostsItem.from_dict(grpc_connection_uri_hosts_item_model_json).__dict__
        grpc_connection_uri_hosts_item_model2 = GRPCConnectionURIHostsItem(**grpc_connection_uri_hosts_item_model_dict)

        # Verify the model instances are equivalent
        assert grpc_connection_uri_hosts_item_model == grpc_connection_uri_hosts_item_model2

        # Convert model instance back to dict and verify no loss of data
        grpc_connection_uri_hosts_item_model_json2 = grpc_connection_uri_hosts_item_model.to_dict()
        assert grpc_connection_uri_hosts_item_model_json2 == grpc_connection_uri_hosts_item_model_json

class TestGetBackupInfoResponse():
    """
    Test Class for GetBackupInfoResponse
    """

    def test_get_backup_info_response_serialization(self):
        """
        Test serialization/deserialization for GetBackupInfoResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        backup_model = {} # Backup
        backup_model['id'] = 'crn:v1:bluemix:public:databases-for-elasticsearch:us-south:a/274074dce64e9c423ffc238516c755e1:afa742a3-6f83-4f6e-a06e-b5c501e9e87a:backup:87635880-b11c-4359-9d06-41fd9f90feaf'
        backup_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-elasticsearch:us-south:a/274074dce64e9c423ffc238516c755e1:afa742a3-6f83-4f6e-a06e-b5c501e9e87a::'
        backup_model['type'] = 'scheduled'
        backup_model['status'] = 'completed'
        backup_model['is_downloadable'] = False
        backup_model['is_restorable'] = True
        backup_model['created_at'] = datetime_to_string(string_to_datetime("2019-06-10T14:31:40.000Z"))

        # Construct a json representation of a GetBackupInfoResponse model
        get_backup_info_response_model_json = {}
        get_backup_info_response_model_json['backup'] = backup_model

        # Construct a model instance of GetBackupInfoResponse by calling from_dict on the json representation
        get_backup_info_response_model = GetBackupInfoResponse.from_dict(get_backup_info_response_model_json)
        assert get_backup_info_response_model != False

        # Construct a model instance of GetBackupInfoResponse by calling from_dict on the json representation
        get_backup_info_response_model_dict = GetBackupInfoResponse.from_dict(get_backup_info_response_model_json).__dict__
        get_backup_info_response_model2 = GetBackupInfoResponse(**get_backup_info_response_model_dict)

        # Verify the model instances are equivalent
        assert get_backup_info_response_model == get_backup_info_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_backup_info_response_model_json2 = get_backup_info_response_model.to_dict()
        assert get_backup_info_response_model_json2 == get_backup_info_response_model_json

class TestGetDeploymentInfoResponse():
    """
    Test Class for GetDeploymentInfoResponse
    """

    def test_get_deployment_info_response_serialization(self):
        """
        Test serialization/deserialization for GetDeploymentInfoResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deployment_model = {} # Deployment
        deployment_model['id'] = 'crn:v1:staging:public:databases-for-enterprisedb:us-south:a/b9552134280015ebfde430a819fa4bb3:5589ecbf-de5f-4eac-9917-df0dd7e706c8::'
        deployment_model['name'] = 'crn:v1:staging:public:databases-for-enterprisedb:us-south:a/b9552134280015ebfde430a819fa4bb3:5589ecbf-de5f-4eac-9917-df0dd7e706c8::'
        deployment_model['type'] = 'enterprisedb'
        deployment_model['platform_options'] = { 'foo': 'bar' }
        deployment_model['version'] = '12'
        deployment_model['admin_usernames'] = {}
        deployment_model['enable_public_endpoints'] = True
        deployment_model['enable_private_endpoints'] = False

        # Construct a json representation of a GetDeploymentInfoResponse model
        get_deployment_info_response_model_json = {}
        get_deployment_info_response_model_json['deployment'] = deployment_model

        # Construct a model instance of GetDeploymentInfoResponse by calling from_dict on the json representation
        get_deployment_info_response_model = GetDeploymentInfoResponse.from_dict(get_deployment_info_response_model_json)
        assert get_deployment_info_response_model != False

        # Construct a model instance of GetDeploymentInfoResponse by calling from_dict on the json representation
        get_deployment_info_response_model_dict = GetDeploymentInfoResponse.from_dict(get_deployment_info_response_model_json).__dict__
        get_deployment_info_response_model2 = GetDeploymentInfoResponse(**get_deployment_info_response_model_dict)

        # Verify the model instances are equivalent
        assert get_deployment_info_response_model == get_deployment_info_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_deployment_info_response_model_json2 = get_deployment_info_response_model.to_dict()
        assert get_deployment_info_response_model_json2 == get_deployment_info_response_model_json

class TestGetTaskResponse():
    """
    Test Class for GetTaskResponse
    """

    def test_get_task_response_serialization(self):
        """
        Test serialization/deserialization for GetTaskResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f4-b5c96544393b'
        task_model['description'] = 'Backing up database on-demand'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:31:30Z"))

        # Construct a json representation of a GetTaskResponse model
        get_task_response_model_json = {}
        get_task_response_model_json['task'] = task_model

        # Construct a model instance of GetTaskResponse by calling from_dict on the json representation
        get_task_response_model = GetTaskResponse.from_dict(get_task_response_model_json)
        assert get_task_response_model != False

        # Construct a model instance of GetTaskResponse by calling from_dict on the json representation
        get_task_response_model_dict = GetTaskResponse.from_dict(get_task_response_model_json).__dict__
        get_task_response_model2 = GetTaskResponse(**get_task_response_model_dict)

        # Verify the model instances are equivalent
        assert get_task_response_model == get_task_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_task_response_model_json2 = get_task_response_model.to_dict()
        assert get_task_response_model_json2 == get_task_response_model_json

class TestGroup():
    """
    Test Class for Group
    """

    def test_group_serialization(self):
        """
        Test serialization/deserialization for Group
        """

        # Construct dict forms of any model objects needed in order to build this model.

        group_members_model = {} # GroupMembers
        group_members_model['units'] = 'count'
        group_members_model['allocation_count'] = 2
        group_members_model['minimum_count'] = 2
        group_members_model['maximum_count'] = 20
        group_members_model['step_size_count'] = 1
        group_members_model['is_adjustable'] = True
        group_members_model['is_optional'] = False
        group_members_model['can_scale_down'] = False

        group_memory_model = {} # GroupMemory
        group_memory_model['units'] = 'mb'
        group_memory_model['allocation_mb'] = 12288
        group_memory_model['minimum_mb'] = 1024
        group_memory_model['maximum_mb'] = 114688
        group_memory_model['step_size_mb'] = 1024
        group_memory_model['is_adjustable'] = True
        group_memory_model['is_optional'] = False
        group_memory_model['can_scale_down'] = True

        group_cpu_model = {} # GroupCpu
        group_cpu_model['units'] = 'count'
        group_cpu_model['allocation_count'] = 2
        group_cpu_model['minimum_count'] = 2
        group_cpu_model['maximum_count'] = 32
        group_cpu_model['step_size_count'] = 2
        group_cpu_model['is_adjustable'] = False
        group_cpu_model['is_optional'] = False
        group_cpu_model['can_scale_down'] = True

        group_disk_model = {} # GroupDisk
        group_disk_model['units'] = 'mb'
        group_disk_model['allocation_mb'] = 10240
        group_disk_model['minimum_mb'] = 2048
        group_disk_model['maximum_mb'] = 4194304
        group_disk_model['step_size_mb'] = 2048
        group_disk_model['is_adjustable'] = True
        group_disk_model['is_optional'] = False
        group_disk_model['can_scale_down'] = False

        # Construct a json representation of a Group model
        group_model_json = {}
        group_model_json['id'] = 'member'
        group_model_json['count'] = 2
        group_model_json['members'] = group_members_model
        group_model_json['memory'] = group_memory_model
        group_model_json['cpu'] = group_cpu_model
        group_model_json['disk'] = group_disk_model

        # Construct a model instance of Group by calling from_dict on the json representation
        group_model = Group.from_dict(group_model_json)
        assert group_model != False

        # Construct a model instance of Group by calling from_dict on the json representation
        group_model_dict = Group.from_dict(group_model_json).__dict__
        group_model2 = Group(**group_model_dict)

        # Verify the model instances are equivalent
        assert group_model == group_model2

        # Convert model instance back to dict and verify no loss of data
        group_model_json2 = group_model.to_dict()
        assert group_model_json2 == group_model_json

class TestGroupCpu():
    """
    Test Class for GroupCpu
    """

    def test_group_cpu_serialization(self):
        """
        Test serialization/deserialization for GroupCpu
        """

        # Construct a json representation of a GroupCpu model
        group_cpu_model_json = {}
        group_cpu_model_json['units'] = 'count'
        group_cpu_model_json['allocation_count'] = 2
        group_cpu_model_json['minimum_count'] = 2
        group_cpu_model_json['maximum_count'] = 32
        group_cpu_model_json['step_size_count'] = 2
        group_cpu_model_json['is_adjustable'] = False
        group_cpu_model_json['is_optional'] = False
        group_cpu_model_json['can_scale_down'] = True

        # Construct a model instance of GroupCpu by calling from_dict on the json representation
        group_cpu_model = GroupCpu.from_dict(group_cpu_model_json)
        assert group_cpu_model != False

        # Construct a model instance of GroupCpu by calling from_dict on the json representation
        group_cpu_model_dict = GroupCpu.from_dict(group_cpu_model_json).__dict__
        group_cpu_model2 = GroupCpu(**group_cpu_model_dict)

        # Verify the model instances are equivalent
        assert group_cpu_model == group_cpu_model2

        # Convert model instance back to dict and verify no loss of data
        group_cpu_model_json2 = group_cpu_model.to_dict()
        assert group_cpu_model_json2 == group_cpu_model_json

class TestGroupDisk():
    """
    Test Class for GroupDisk
    """

    def test_group_disk_serialization(self):
        """
        Test serialization/deserialization for GroupDisk
        """

        # Construct a json representation of a GroupDisk model
        group_disk_model_json = {}
        group_disk_model_json['units'] = 'mb'
        group_disk_model_json['allocation_mb'] = 10240
        group_disk_model_json['minimum_mb'] = 2048
        group_disk_model_json['maximum_mb'] = 4194304
        group_disk_model_json['step_size_mb'] = 2048
        group_disk_model_json['is_adjustable'] = True
        group_disk_model_json['is_optional'] = False
        group_disk_model_json['can_scale_down'] = False

        # Construct a model instance of GroupDisk by calling from_dict on the json representation
        group_disk_model = GroupDisk.from_dict(group_disk_model_json)
        assert group_disk_model != False

        # Construct a model instance of GroupDisk by calling from_dict on the json representation
        group_disk_model_dict = GroupDisk.from_dict(group_disk_model_json).__dict__
        group_disk_model2 = GroupDisk(**group_disk_model_dict)

        # Verify the model instances are equivalent
        assert group_disk_model == group_disk_model2

        # Convert model instance back to dict and verify no loss of data
        group_disk_model_json2 = group_disk_model.to_dict()
        assert group_disk_model_json2 == group_disk_model_json

class TestGroupMembers():
    """
    Test Class for GroupMembers
    """

    def test_group_members_serialization(self):
        """
        Test serialization/deserialization for GroupMembers
        """

        # Construct a json representation of a GroupMembers model
        group_members_model_json = {}
        group_members_model_json['units'] = 'count'
        group_members_model_json['allocation_count'] = 2
        group_members_model_json['minimum_count'] = 2
        group_members_model_json['maximum_count'] = 20
        group_members_model_json['step_size_count'] = 1
        group_members_model_json['is_adjustable'] = True
        group_members_model_json['is_optional'] = False
        group_members_model_json['can_scale_down'] = False

        # Construct a model instance of GroupMembers by calling from_dict on the json representation
        group_members_model = GroupMembers.from_dict(group_members_model_json)
        assert group_members_model != False

        # Construct a model instance of GroupMembers by calling from_dict on the json representation
        group_members_model_dict = GroupMembers.from_dict(group_members_model_json).__dict__
        group_members_model2 = GroupMembers(**group_members_model_dict)

        # Verify the model instances are equivalent
        assert group_members_model == group_members_model2

        # Convert model instance back to dict and verify no loss of data
        group_members_model_json2 = group_members_model.to_dict()
        assert group_members_model_json2 == group_members_model_json

class TestGroupMemory():
    """
    Test Class for GroupMemory
    """

    def test_group_memory_serialization(self):
        """
        Test serialization/deserialization for GroupMemory
        """

        # Construct a json representation of a GroupMemory model
        group_memory_model_json = {}
        group_memory_model_json['units'] = 'mb'
        group_memory_model_json['allocation_mb'] = 12288
        group_memory_model_json['minimum_mb'] = 1024
        group_memory_model_json['maximum_mb'] = 114688
        group_memory_model_json['step_size_mb'] = 1024
        group_memory_model_json['is_adjustable'] = True
        group_memory_model_json['is_optional'] = False
        group_memory_model_json['can_scale_down'] = True

        # Construct a model instance of GroupMemory by calling from_dict on the json representation
        group_memory_model = GroupMemory.from_dict(group_memory_model_json)
        assert group_memory_model != False

        # Construct a model instance of GroupMemory by calling from_dict on the json representation
        group_memory_model_dict = GroupMemory.from_dict(group_memory_model_json).__dict__
        group_memory_model2 = GroupMemory(**group_memory_model_dict)

        # Verify the model instances are equivalent
        assert group_memory_model == group_memory_model2

        # Convert model instance back to dict and verify no loss of data
        group_memory_model_json2 = group_memory_model.to_dict()
        assert group_memory_model_json2 == group_memory_model_json

class TestGroups():
    """
    Test Class for Groups
    """

    def test_groups_serialization(self):
        """
        Test serialization/deserialization for Groups
        """

        # Construct dict forms of any model objects needed in order to build this model.

        group_members_model = {} # GroupMembers
        group_members_model['units'] = 'count'
        group_members_model['allocation_count'] = 3
        group_members_model['minimum_count'] = 3
        group_members_model['maximum_count'] = 20
        group_members_model['step_size_count'] = 1
        group_members_model['is_adjustable'] = False
        group_members_model['is_optional'] = False
        group_members_model['can_scale_down'] = False

        group_memory_model = {} # GroupMemory
        group_memory_model['units'] = 'mb'
        group_memory_model['allocation_mb'] = 3072
        group_memory_model['minimum_mb'] = 3072
        group_memory_model['maximum_mb'] = 344064
        group_memory_model['step_size_mb'] = 384
        group_memory_model['is_adjustable'] = True
        group_memory_model['is_optional'] = False
        group_memory_model['can_scale_down'] = True

        group_cpu_model = {} # GroupCpu
        group_cpu_model['units'] = 'count'
        group_cpu_model['allocation_count'] = 0
        group_cpu_model['minimum_count'] = 3
        group_cpu_model['maximum_count'] = 90
        group_cpu_model['step_size_count'] = 3
        group_cpu_model['is_adjustable'] = False
        group_cpu_model['is_optional'] = True
        group_cpu_model['can_scale_down'] = True

        group_disk_model = {} # GroupDisk
        group_disk_model['units'] = 'mb'
        group_disk_model['allocation_mb'] = 15360
        group_disk_model['minimum_mb'] = 15360
        group_disk_model['maximum_mb'] = 11010048
        group_disk_model['step_size_mb'] = 3072
        group_disk_model['is_adjustable'] = True
        group_disk_model['is_optional'] = False
        group_disk_model['can_scale_down'] = False

        group_model = {} # Group
        group_model['id'] = 'member'
        group_model['count'] = 3
        group_model['members'] = group_members_model
        group_model['memory'] = group_memory_model
        group_model['cpu'] = group_cpu_model
        group_model['disk'] = group_disk_model

        # Construct a json representation of a Groups model
        groups_model_json = {}
        groups_model_json['groups'] = [group_model]

        # Construct a model instance of Groups by calling from_dict on the json representation
        groups_model = Groups.from_dict(groups_model_json)
        assert groups_model != False

        # Construct a model instance of Groups by calling from_dict on the json representation
        groups_model_dict = Groups.from_dict(groups_model_json).__dict__
        groups_model2 = Groups(**groups_model_dict)

        # Verify the model instances are equivalent
        assert groups_model == groups_model2

        # Convert model instance back to dict and verify no loss of data
        groups_model_json2 = groups_model.to_dict()
        assert groups_model_json2 == groups_model_json

class TestKillConnectionsResponse():
    """
    Test Class for KillConnectionsResponse
    """

    def test_kill_connections_response_serialization(self):
        """
        Test serialization/deserialization for KillConnectionsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0c59-4db6-92f3-b5c96544393b'
        task_model['description'] = 'Killing all database connections.'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:31:30Z"))

        # Construct a json representation of a KillConnectionsResponse model
        kill_connections_response_model_json = {}
        kill_connections_response_model_json['task'] = task_model

        # Construct a model instance of KillConnectionsResponse by calling from_dict on the json representation
        kill_connections_response_model = KillConnectionsResponse.from_dict(kill_connections_response_model_json)
        assert kill_connections_response_model != False

        # Construct a model instance of KillConnectionsResponse by calling from_dict on the json representation
        kill_connections_response_model_dict = KillConnectionsResponse.from_dict(kill_connections_response_model_json).__dict__
        kill_connections_response_model2 = KillConnectionsResponse(**kill_connections_response_model_dict)

        # Verify the model instances are equivalent
        assert kill_connections_response_model == kill_connections_response_model2

        # Convert model instance back to dict and verify no loss of data
        kill_connections_response_model_json2 = kill_connections_response_model.to_dict()
        assert kill_connections_response_model_json2 == kill_connections_response_model_json

class TestListDeployablesResponse():
    """
    Test Class for ListDeployablesResponse
    """

    def test_list_deployables_response_serialization(self):
        """
        Test serialization/deserialization for ListDeployablesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deployables_versions_item_transitions_item_model = {} # DeployablesVersionsItemTransitionsItem
        deployables_versions_item_transitions_item_model['application'] = 'elasticsearch'
        deployables_versions_item_transitions_item_model['method'] = 'restore'
        deployables_versions_item_transitions_item_model['from_version'] = '5.6'
        deployables_versions_item_transitions_item_model['to_version'] = '6.7'

        deployables_versions_item_model = {} # DeployablesVersionsItem
        deployables_versions_item_model['version'] = '6.7'
        deployables_versions_item_model['status'] = 'stable'
        deployables_versions_item_model['is_preferred'] = True
        deployables_versions_item_model['transitions'] = [deployables_versions_item_transitions_item_model]

        deployables_model = {} # Deployables
        deployables_model['type'] = 'elasticsearch'
        deployables_model['versions'] = [deployables_versions_item_model]

        # Construct a json representation of a ListDeployablesResponse model
        list_deployables_response_model_json = {}
        list_deployables_response_model_json['deployables'] = [deployables_model]

        # Construct a model instance of ListDeployablesResponse by calling from_dict on the json representation
        list_deployables_response_model = ListDeployablesResponse.from_dict(list_deployables_response_model_json)
        assert list_deployables_response_model != False

        # Construct a model instance of ListDeployablesResponse by calling from_dict on the json representation
        list_deployables_response_model_dict = ListDeployablesResponse.from_dict(list_deployables_response_model_json).__dict__
        list_deployables_response_model2 = ListDeployablesResponse(**list_deployables_response_model_dict)

        # Verify the model instances are equivalent
        assert list_deployables_response_model == list_deployables_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_deployables_response_model_json2 = list_deployables_response_model.to_dict()
        assert list_deployables_response_model_json2 == list_deployables_response_model_json

class TestListRegionsResponse():
    """
    Test Class for ListRegionsResponse
    """

    def test_list_regions_response_serialization(self):
        """
        Test serialization/deserialization for ListRegionsResponse
        """

        # Construct a json representation of a ListRegionsResponse model
        list_regions_response_model_json = {}
        list_regions_response_model_json['regions'] = ['testString']

        # Construct a model instance of ListRegionsResponse by calling from_dict on the json representation
        list_regions_response_model = ListRegionsResponse.from_dict(list_regions_response_model_json)
        assert list_regions_response_model != False

        # Construct a model instance of ListRegionsResponse by calling from_dict on the json representation
        list_regions_response_model_dict = ListRegionsResponse.from_dict(list_regions_response_model_json).__dict__
        list_regions_response_model2 = ListRegionsResponse(**list_regions_response_model_dict)

        # Verify the model instances are equivalent
        assert list_regions_response_model == list_regions_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_regions_response_model_json2 = list_regions_response_model.to_dict()
        assert list_regions_response_model_json2 == list_regions_response_model_json

class TestListRemotesResponse():
    """
    Test Class for ListRemotesResponse
    """

    def test_list_remotes_response_serialization(self):
        """
        Test serialization/deserialization for ListRemotesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        remotes_model = {} # Remotes
        remotes_model['leader'] = 'testString'
        remotes_model['replicas'] = ['crn:v1:bluemix:public:databases-for-postgresql:us-south:a/389574dce64e9c423ffc238516c755e1:0e399ae3-4a1a-476d-b85b-755c7af54788::']

        # Construct a json representation of a ListRemotesResponse model
        list_remotes_response_model_json = {}
        list_remotes_response_model_json['remotes'] = remotes_model

        # Construct a model instance of ListRemotesResponse by calling from_dict on the json representation
        list_remotes_response_model = ListRemotesResponse.from_dict(list_remotes_response_model_json)
        assert list_remotes_response_model != False

        # Construct a model instance of ListRemotesResponse by calling from_dict on the json representation
        list_remotes_response_model_dict = ListRemotesResponse.from_dict(list_remotes_response_model_json).__dict__
        list_remotes_response_model2 = ListRemotesResponse(**list_remotes_response_model_dict)

        # Verify the model instances are equivalent
        assert list_remotes_response_model == list_remotes_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_remotes_response_model_json2 = list_remotes_response_model.to_dict()
        assert list_remotes_response_model_json2 == list_remotes_response_model_json

class TestMongoDBConnectionURI():
    """
    Test Class for MongoDBConnectionURI
    """

    def test_mongo_db_connection_uri_serialization(self):
        """
        Test serialization/deserialization for MongoDBConnectionURI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        mongo_db_connection_uri_hosts_item_model = {} # MongoDBConnectionURIHostsItem
        mongo_db_connection_uri_hosts_item_model['hostname'] = 'testString'
        mongo_db_connection_uri_hosts_item_model['port'] = 38

        mongo_db_connection_uri_authentication_model = {} # MongoDBConnectionURIAuthentication
        mongo_db_connection_uri_authentication_model['method'] = 'testString'
        mongo_db_connection_uri_authentication_model['username'] = 'testString'
        mongo_db_connection_uri_authentication_model['password'] = 'testString'

        mongo_db_connection_uri_certificate_model = {} # MongoDBConnectionURICertificate
        mongo_db_connection_uri_certificate_model['name'] = 'testString'
        mongo_db_connection_uri_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a MongoDBConnectionURI model
        mongo_db_connection_uri_model_json = {}
        mongo_db_connection_uri_model_json['type'] = 'uri'
        mongo_db_connection_uri_model_json['composed'] = ['testString']
        mongo_db_connection_uri_model_json['scheme'] = 'testString'
        mongo_db_connection_uri_model_json['hosts'] = [mongo_db_connection_uri_hosts_item_model]
        mongo_db_connection_uri_model_json['path'] = 'testString'
        mongo_db_connection_uri_model_json['query_options'] = { 'foo': 'bar' }
        mongo_db_connection_uri_model_json['authentication'] = mongo_db_connection_uri_authentication_model
        mongo_db_connection_uri_model_json['certificate'] = mongo_db_connection_uri_certificate_model
        mongo_db_connection_uri_model_json['database'] = 'testString'
        mongo_db_connection_uri_model_json['replica_set'] = 'testString'

        # Construct a model instance of MongoDBConnectionURI by calling from_dict on the json representation
        mongo_db_connection_uri_model = MongoDBConnectionURI.from_dict(mongo_db_connection_uri_model_json)
        assert mongo_db_connection_uri_model != False

        # Construct a model instance of MongoDBConnectionURI by calling from_dict on the json representation
        mongo_db_connection_uri_model_dict = MongoDBConnectionURI.from_dict(mongo_db_connection_uri_model_json).__dict__
        mongo_db_connection_uri_model2 = MongoDBConnectionURI(**mongo_db_connection_uri_model_dict)

        # Verify the model instances are equivalent
        assert mongo_db_connection_uri_model == mongo_db_connection_uri_model2

        # Convert model instance back to dict and verify no loss of data
        mongo_db_connection_uri_model_json2 = mongo_db_connection_uri_model.to_dict()
        assert mongo_db_connection_uri_model_json2 == mongo_db_connection_uri_model_json

class TestMongoDBConnectionURIAuthentication():
    """
    Test Class for MongoDBConnectionURIAuthentication
    """

    def test_mongo_db_connection_uri_authentication_serialization(self):
        """
        Test serialization/deserialization for MongoDBConnectionURIAuthentication
        """

        # Construct a json representation of a MongoDBConnectionURIAuthentication model
        mongo_db_connection_uri_authentication_model_json = {}
        mongo_db_connection_uri_authentication_model_json['method'] = 'testString'
        mongo_db_connection_uri_authentication_model_json['username'] = 'testString'
        mongo_db_connection_uri_authentication_model_json['password'] = 'testString'

        # Construct a model instance of MongoDBConnectionURIAuthentication by calling from_dict on the json representation
        mongo_db_connection_uri_authentication_model = MongoDBConnectionURIAuthentication.from_dict(mongo_db_connection_uri_authentication_model_json)
        assert mongo_db_connection_uri_authentication_model != False

        # Construct a model instance of MongoDBConnectionURIAuthentication by calling from_dict on the json representation
        mongo_db_connection_uri_authentication_model_dict = MongoDBConnectionURIAuthentication.from_dict(mongo_db_connection_uri_authentication_model_json).__dict__
        mongo_db_connection_uri_authentication_model2 = MongoDBConnectionURIAuthentication(**mongo_db_connection_uri_authentication_model_dict)

        # Verify the model instances are equivalent
        assert mongo_db_connection_uri_authentication_model == mongo_db_connection_uri_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        mongo_db_connection_uri_authentication_model_json2 = mongo_db_connection_uri_authentication_model.to_dict()
        assert mongo_db_connection_uri_authentication_model_json2 == mongo_db_connection_uri_authentication_model_json

class TestMongoDBConnectionURICertificate():
    """
    Test Class for MongoDBConnectionURICertificate
    """

    def test_mongo_db_connection_uri_certificate_serialization(self):
        """
        Test serialization/deserialization for MongoDBConnectionURICertificate
        """

        # Construct a json representation of a MongoDBConnectionURICertificate model
        mongo_db_connection_uri_certificate_model_json = {}
        mongo_db_connection_uri_certificate_model_json['name'] = 'testString'
        mongo_db_connection_uri_certificate_model_json['certificate_base64'] = 'testString'

        # Construct a model instance of MongoDBConnectionURICertificate by calling from_dict on the json representation
        mongo_db_connection_uri_certificate_model = MongoDBConnectionURICertificate.from_dict(mongo_db_connection_uri_certificate_model_json)
        assert mongo_db_connection_uri_certificate_model != False

        # Construct a model instance of MongoDBConnectionURICertificate by calling from_dict on the json representation
        mongo_db_connection_uri_certificate_model_dict = MongoDBConnectionURICertificate.from_dict(mongo_db_connection_uri_certificate_model_json).__dict__
        mongo_db_connection_uri_certificate_model2 = MongoDBConnectionURICertificate(**mongo_db_connection_uri_certificate_model_dict)

        # Verify the model instances are equivalent
        assert mongo_db_connection_uri_certificate_model == mongo_db_connection_uri_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        mongo_db_connection_uri_certificate_model_json2 = mongo_db_connection_uri_certificate_model.to_dict()
        assert mongo_db_connection_uri_certificate_model_json2 == mongo_db_connection_uri_certificate_model_json

class TestMongoDBConnectionURIHostsItem():
    """
    Test Class for MongoDBConnectionURIHostsItem
    """

    def test_mongo_db_connection_uri_hosts_item_serialization(self):
        """
        Test serialization/deserialization for MongoDBConnectionURIHostsItem
        """

        # Construct a json representation of a MongoDBConnectionURIHostsItem model
        mongo_db_connection_uri_hosts_item_model_json = {}
        mongo_db_connection_uri_hosts_item_model_json['hostname'] = 'testString'
        mongo_db_connection_uri_hosts_item_model_json['port'] = 38

        # Construct a model instance of MongoDBConnectionURIHostsItem by calling from_dict on the json representation
        mongo_db_connection_uri_hosts_item_model = MongoDBConnectionURIHostsItem.from_dict(mongo_db_connection_uri_hosts_item_model_json)
        assert mongo_db_connection_uri_hosts_item_model != False

        # Construct a model instance of MongoDBConnectionURIHostsItem by calling from_dict on the json representation
        mongo_db_connection_uri_hosts_item_model_dict = MongoDBConnectionURIHostsItem.from_dict(mongo_db_connection_uri_hosts_item_model_json).__dict__
        mongo_db_connection_uri_hosts_item_model2 = MongoDBConnectionURIHostsItem(**mongo_db_connection_uri_hosts_item_model_dict)

        # Verify the model instances are equivalent
        assert mongo_db_connection_uri_hosts_item_model == mongo_db_connection_uri_hosts_item_model2

        # Convert model instance back to dict and verify no loss of data
        mongo_db_connection_uri_hosts_item_model_json2 = mongo_db_connection_uri_hosts_item_model.to_dict()
        assert mongo_db_connection_uri_hosts_item_model_json2 == mongo_db_connection_uri_hosts_item_model_json

class TestPointInTimeRecoveryData():
    """
    Test Class for PointInTimeRecoveryData
    """

    def test_point_in_time_recovery_data_serialization(self):
        """
        Test serialization/deserialization for PointInTimeRecoveryData
        """

        # Construct a json representation of a PointInTimeRecoveryData model
        point_in_time_recovery_data_model_json = {}
        point_in_time_recovery_data_model_json['earliest_point_in_time_recovery_time'] = 'testString'

        # Construct a model instance of PointInTimeRecoveryData by calling from_dict on the json representation
        point_in_time_recovery_data_model = PointInTimeRecoveryData.from_dict(point_in_time_recovery_data_model_json)
        assert point_in_time_recovery_data_model != False

        # Construct a model instance of PointInTimeRecoveryData by calling from_dict on the json representation
        point_in_time_recovery_data_model_dict = PointInTimeRecoveryData.from_dict(point_in_time_recovery_data_model_json).__dict__
        point_in_time_recovery_data_model2 = PointInTimeRecoveryData(**point_in_time_recovery_data_model_dict)

        # Verify the model instances are equivalent
        assert point_in_time_recovery_data_model == point_in_time_recovery_data_model2

        # Convert model instance back to dict and verify no loss of data
        point_in_time_recovery_data_model_json2 = point_in_time_recovery_data_model.to_dict()
        assert point_in_time_recovery_data_model_json2 == point_in_time_recovery_data_model_json

class TestPostgreSQLConnectionURI():
    """
    Test Class for PostgreSQLConnectionURI
    """

    def test_postgre_sql_connection_uri_serialization(self):
        """
        Test serialization/deserialization for PostgreSQLConnectionURI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        postgre_sql_connection_uri_hosts_item_model = {} # PostgreSQLConnectionURIHostsItem
        postgre_sql_connection_uri_hosts_item_model['hostname'] = 'testString'
        postgre_sql_connection_uri_hosts_item_model['port'] = 38

        postgre_sql_connection_uri_authentication_model = {} # PostgreSQLConnectionURIAuthentication
        postgre_sql_connection_uri_authentication_model['method'] = 'testString'
        postgre_sql_connection_uri_authentication_model['username'] = 'testString'
        postgre_sql_connection_uri_authentication_model['password'] = 'testString'

        postgre_sql_connection_uri_certificate_model = {} # PostgreSQLConnectionURICertificate
        postgre_sql_connection_uri_certificate_model['name'] = 'testString'
        postgre_sql_connection_uri_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a PostgreSQLConnectionURI model
        postgre_sql_connection_uri_model_json = {}
        postgre_sql_connection_uri_model_json['type'] = 'uri'
        postgre_sql_connection_uri_model_json['composed'] = ['testString']
        postgre_sql_connection_uri_model_json['scheme'] = 'testString'
        postgre_sql_connection_uri_model_json['hosts'] = [postgre_sql_connection_uri_hosts_item_model]
        postgre_sql_connection_uri_model_json['path'] = '/ibmclouddb'
        postgre_sql_connection_uri_model_json['query_options'] = { 'foo': 'bar' }
        postgre_sql_connection_uri_model_json['authentication'] = postgre_sql_connection_uri_authentication_model
        postgre_sql_connection_uri_model_json['certificate'] = postgre_sql_connection_uri_certificate_model
        postgre_sql_connection_uri_model_json['database'] = 'testString'

        # Construct a model instance of PostgreSQLConnectionURI by calling from_dict on the json representation
        postgre_sql_connection_uri_model = PostgreSQLConnectionURI.from_dict(postgre_sql_connection_uri_model_json)
        assert postgre_sql_connection_uri_model != False

        # Construct a model instance of PostgreSQLConnectionURI by calling from_dict on the json representation
        postgre_sql_connection_uri_model_dict = PostgreSQLConnectionURI.from_dict(postgre_sql_connection_uri_model_json).__dict__
        postgre_sql_connection_uri_model2 = PostgreSQLConnectionURI(**postgre_sql_connection_uri_model_dict)

        # Verify the model instances are equivalent
        assert postgre_sql_connection_uri_model == postgre_sql_connection_uri_model2

        # Convert model instance back to dict and verify no loss of data
        postgre_sql_connection_uri_model_json2 = postgre_sql_connection_uri_model.to_dict()
        assert postgre_sql_connection_uri_model_json2 == postgre_sql_connection_uri_model_json

class TestPostgreSQLConnectionURIAuthentication():
    """
    Test Class for PostgreSQLConnectionURIAuthentication
    """

    def test_postgre_sql_connection_uri_authentication_serialization(self):
        """
        Test serialization/deserialization for PostgreSQLConnectionURIAuthentication
        """

        # Construct a json representation of a PostgreSQLConnectionURIAuthentication model
        postgre_sql_connection_uri_authentication_model_json = {}
        postgre_sql_connection_uri_authentication_model_json['method'] = 'testString'
        postgre_sql_connection_uri_authentication_model_json['username'] = 'testString'
        postgre_sql_connection_uri_authentication_model_json['password'] = 'testString'

        # Construct a model instance of PostgreSQLConnectionURIAuthentication by calling from_dict on the json representation
        postgre_sql_connection_uri_authentication_model = PostgreSQLConnectionURIAuthentication.from_dict(postgre_sql_connection_uri_authentication_model_json)
        assert postgre_sql_connection_uri_authentication_model != False

        # Construct a model instance of PostgreSQLConnectionURIAuthentication by calling from_dict on the json representation
        postgre_sql_connection_uri_authentication_model_dict = PostgreSQLConnectionURIAuthentication.from_dict(postgre_sql_connection_uri_authentication_model_json).__dict__
        postgre_sql_connection_uri_authentication_model2 = PostgreSQLConnectionURIAuthentication(**postgre_sql_connection_uri_authentication_model_dict)

        # Verify the model instances are equivalent
        assert postgre_sql_connection_uri_authentication_model == postgre_sql_connection_uri_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        postgre_sql_connection_uri_authentication_model_json2 = postgre_sql_connection_uri_authentication_model.to_dict()
        assert postgre_sql_connection_uri_authentication_model_json2 == postgre_sql_connection_uri_authentication_model_json

class TestPostgreSQLConnectionURICertificate():
    """
    Test Class for PostgreSQLConnectionURICertificate
    """

    def test_postgre_sql_connection_uri_certificate_serialization(self):
        """
        Test serialization/deserialization for PostgreSQLConnectionURICertificate
        """

        # Construct a json representation of a PostgreSQLConnectionURICertificate model
        postgre_sql_connection_uri_certificate_model_json = {}
        postgre_sql_connection_uri_certificate_model_json['name'] = 'testString'
        postgre_sql_connection_uri_certificate_model_json['certificate_base64'] = 'testString'

        # Construct a model instance of PostgreSQLConnectionURICertificate by calling from_dict on the json representation
        postgre_sql_connection_uri_certificate_model = PostgreSQLConnectionURICertificate.from_dict(postgre_sql_connection_uri_certificate_model_json)
        assert postgre_sql_connection_uri_certificate_model != False

        # Construct a model instance of PostgreSQLConnectionURICertificate by calling from_dict on the json representation
        postgre_sql_connection_uri_certificate_model_dict = PostgreSQLConnectionURICertificate.from_dict(postgre_sql_connection_uri_certificate_model_json).__dict__
        postgre_sql_connection_uri_certificate_model2 = PostgreSQLConnectionURICertificate(**postgre_sql_connection_uri_certificate_model_dict)

        # Verify the model instances are equivalent
        assert postgre_sql_connection_uri_certificate_model == postgre_sql_connection_uri_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        postgre_sql_connection_uri_certificate_model_json2 = postgre_sql_connection_uri_certificate_model.to_dict()
        assert postgre_sql_connection_uri_certificate_model_json2 == postgre_sql_connection_uri_certificate_model_json

class TestPostgreSQLConnectionURIHostsItem():
    """
    Test Class for PostgreSQLConnectionURIHostsItem
    """

    def test_postgre_sql_connection_uri_hosts_item_serialization(self):
        """
        Test serialization/deserialization for PostgreSQLConnectionURIHostsItem
        """

        # Construct a json representation of a PostgreSQLConnectionURIHostsItem model
        postgre_sql_connection_uri_hosts_item_model_json = {}
        postgre_sql_connection_uri_hosts_item_model_json['hostname'] = 'testString'
        postgre_sql_connection_uri_hosts_item_model_json['port'] = 38

        # Construct a model instance of PostgreSQLConnectionURIHostsItem by calling from_dict on the json representation
        postgre_sql_connection_uri_hosts_item_model = PostgreSQLConnectionURIHostsItem.from_dict(postgre_sql_connection_uri_hosts_item_model_json)
        assert postgre_sql_connection_uri_hosts_item_model != False

        # Construct a model instance of PostgreSQLConnectionURIHostsItem by calling from_dict on the json representation
        postgre_sql_connection_uri_hosts_item_model_dict = PostgreSQLConnectionURIHostsItem.from_dict(postgre_sql_connection_uri_hosts_item_model_json).__dict__
        postgre_sql_connection_uri_hosts_item_model2 = PostgreSQLConnectionURIHostsItem(**postgre_sql_connection_uri_hosts_item_model_dict)

        # Verify the model instances are equivalent
        assert postgre_sql_connection_uri_hosts_item_model == postgre_sql_connection_uri_hosts_item_model2

        # Convert model instance back to dict and verify no loss of data
        postgre_sql_connection_uri_hosts_item_model_json2 = postgre_sql_connection_uri_hosts_item_model.to_dict()
        assert postgre_sql_connection_uri_hosts_item_model_json2 == postgre_sql_connection_uri_hosts_item_model_json

class TestRabbitMQConnectionAMQPS():
    """
    Test Class for RabbitMQConnectionAMQPS
    """

    def test_rabbit_mq_connection_amqps_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionAMQPS
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rabbit_mq_connection_amqps_hosts_item_model = {} # RabbitMQConnectionAMQPSHostsItem
        rabbit_mq_connection_amqps_hosts_item_model['hostname'] = 'testString'
        rabbit_mq_connection_amqps_hosts_item_model['port'] = 38

        rabbit_mq_connection_amqps_authentication_model = {} # RabbitMQConnectionAMQPSAuthentication
        rabbit_mq_connection_amqps_authentication_model['method'] = 'testString'
        rabbit_mq_connection_amqps_authentication_model['username'] = 'testString'
        rabbit_mq_connection_amqps_authentication_model['password'] = 'testString'

        rabbit_mq_connection_amqps_certificate_model = {} # RabbitMQConnectionAMQPSCertificate
        rabbit_mq_connection_amqps_certificate_model['name'] = 'testString'
        rabbit_mq_connection_amqps_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a RabbitMQConnectionAMQPS model
        rabbit_mq_connection_amqps_model_json = {}
        rabbit_mq_connection_amqps_model_json['type'] = 'uri'
        rabbit_mq_connection_amqps_model_json['composed'] = ['testString']
        rabbit_mq_connection_amqps_model_json['scheme'] = 'testString'
        rabbit_mq_connection_amqps_model_json['hosts'] = [rabbit_mq_connection_amqps_hosts_item_model]
        rabbit_mq_connection_amqps_model_json['path'] = 'testString'
        rabbit_mq_connection_amqps_model_json['query_options'] = { 'foo': 'bar' }
        rabbit_mq_connection_amqps_model_json['authentication'] = rabbit_mq_connection_amqps_authentication_model
        rabbit_mq_connection_amqps_model_json['certificate'] = rabbit_mq_connection_amqps_certificate_model

        # Construct a model instance of RabbitMQConnectionAMQPS by calling from_dict on the json representation
        rabbit_mq_connection_amqps_model = RabbitMQConnectionAMQPS.from_dict(rabbit_mq_connection_amqps_model_json)
        assert rabbit_mq_connection_amqps_model != False

        # Construct a model instance of RabbitMQConnectionAMQPS by calling from_dict on the json representation
        rabbit_mq_connection_amqps_model_dict = RabbitMQConnectionAMQPS.from_dict(rabbit_mq_connection_amqps_model_json).__dict__
        rabbit_mq_connection_amqps_model2 = RabbitMQConnectionAMQPS(**rabbit_mq_connection_amqps_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_amqps_model == rabbit_mq_connection_amqps_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_amqps_model_json2 = rabbit_mq_connection_amqps_model.to_dict()
        assert rabbit_mq_connection_amqps_model_json2 == rabbit_mq_connection_amqps_model_json

class TestRabbitMQConnectionAMQPSAuthentication():
    """
    Test Class for RabbitMQConnectionAMQPSAuthentication
    """

    def test_rabbit_mq_connection_amqps_authentication_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionAMQPSAuthentication
        """

        # Construct a json representation of a RabbitMQConnectionAMQPSAuthentication model
        rabbit_mq_connection_amqps_authentication_model_json = {}
        rabbit_mq_connection_amqps_authentication_model_json['method'] = 'testString'
        rabbit_mq_connection_amqps_authentication_model_json['username'] = 'testString'
        rabbit_mq_connection_amqps_authentication_model_json['password'] = 'testString'

        # Construct a model instance of RabbitMQConnectionAMQPSAuthentication by calling from_dict on the json representation
        rabbit_mq_connection_amqps_authentication_model = RabbitMQConnectionAMQPSAuthentication.from_dict(rabbit_mq_connection_amqps_authentication_model_json)
        assert rabbit_mq_connection_amqps_authentication_model != False

        # Construct a model instance of RabbitMQConnectionAMQPSAuthentication by calling from_dict on the json representation
        rabbit_mq_connection_amqps_authentication_model_dict = RabbitMQConnectionAMQPSAuthentication.from_dict(rabbit_mq_connection_amqps_authentication_model_json).__dict__
        rabbit_mq_connection_amqps_authentication_model2 = RabbitMQConnectionAMQPSAuthentication(**rabbit_mq_connection_amqps_authentication_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_amqps_authentication_model == rabbit_mq_connection_amqps_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_amqps_authentication_model_json2 = rabbit_mq_connection_amqps_authentication_model.to_dict()
        assert rabbit_mq_connection_amqps_authentication_model_json2 == rabbit_mq_connection_amqps_authentication_model_json

class TestRabbitMQConnectionAMQPSCertificate():
    """
    Test Class for RabbitMQConnectionAMQPSCertificate
    """

    def test_rabbit_mq_connection_amqps_certificate_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionAMQPSCertificate
        """

        # Construct a json representation of a RabbitMQConnectionAMQPSCertificate model
        rabbit_mq_connection_amqps_certificate_model_json = {}
        rabbit_mq_connection_amqps_certificate_model_json['name'] = 'testString'
        rabbit_mq_connection_amqps_certificate_model_json['certificate_base64'] = 'testString'

        # Construct a model instance of RabbitMQConnectionAMQPSCertificate by calling from_dict on the json representation
        rabbit_mq_connection_amqps_certificate_model = RabbitMQConnectionAMQPSCertificate.from_dict(rabbit_mq_connection_amqps_certificate_model_json)
        assert rabbit_mq_connection_amqps_certificate_model != False

        # Construct a model instance of RabbitMQConnectionAMQPSCertificate by calling from_dict on the json representation
        rabbit_mq_connection_amqps_certificate_model_dict = RabbitMQConnectionAMQPSCertificate.from_dict(rabbit_mq_connection_amqps_certificate_model_json).__dict__
        rabbit_mq_connection_amqps_certificate_model2 = RabbitMQConnectionAMQPSCertificate(**rabbit_mq_connection_amqps_certificate_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_amqps_certificate_model == rabbit_mq_connection_amqps_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_amqps_certificate_model_json2 = rabbit_mq_connection_amqps_certificate_model.to_dict()
        assert rabbit_mq_connection_amqps_certificate_model_json2 == rabbit_mq_connection_amqps_certificate_model_json

class TestRabbitMQConnectionAMQPSHostsItem():
    """
    Test Class for RabbitMQConnectionAMQPSHostsItem
    """

    def test_rabbit_mq_connection_amqps_hosts_item_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionAMQPSHostsItem
        """

        # Construct a json representation of a RabbitMQConnectionAMQPSHostsItem model
        rabbit_mq_connection_amqps_hosts_item_model_json = {}
        rabbit_mq_connection_amqps_hosts_item_model_json['hostname'] = 'testString'
        rabbit_mq_connection_amqps_hosts_item_model_json['port'] = 38

        # Construct a model instance of RabbitMQConnectionAMQPSHostsItem by calling from_dict on the json representation
        rabbit_mq_connection_amqps_hosts_item_model = RabbitMQConnectionAMQPSHostsItem.from_dict(rabbit_mq_connection_amqps_hosts_item_model_json)
        assert rabbit_mq_connection_amqps_hosts_item_model != False

        # Construct a model instance of RabbitMQConnectionAMQPSHostsItem by calling from_dict on the json representation
        rabbit_mq_connection_amqps_hosts_item_model_dict = RabbitMQConnectionAMQPSHostsItem.from_dict(rabbit_mq_connection_amqps_hosts_item_model_json).__dict__
        rabbit_mq_connection_amqps_hosts_item_model2 = RabbitMQConnectionAMQPSHostsItem(**rabbit_mq_connection_amqps_hosts_item_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_amqps_hosts_item_model == rabbit_mq_connection_amqps_hosts_item_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_amqps_hosts_item_model_json2 = rabbit_mq_connection_amqps_hosts_item_model.to_dict()
        assert rabbit_mq_connection_amqps_hosts_item_model_json2 == rabbit_mq_connection_amqps_hosts_item_model_json

class TestRabbitMQConnectionHTTPS():
    """
    Test Class for RabbitMQConnectionHTTPS
    """

    def test_rabbit_mq_connection_https_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionHTTPS
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rabbit_mq_connection_https_hosts_item_model = {} # RabbitMQConnectionHTTPSHostsItem
        rabbit_mq_connection_https_hosts_item_model['hostname'] = 'testString'
        rabbit_mq_connection_https_hosts_item_model['port'] = 38

        rabbit_mq_connection_https_authentication_model = {} # RabbitMQConnectionHTTPSAuthentication
        rabbit_mq_connection_https_authentication_model['method'] = 'testString'
        rabbit_mq_connection_https_authentication_model['username'] = 'testString'
        rabbit_mq_connection_https_authentication_model['password'] = 'testString'

        rabbit_mq_connection_https_certificate_model = {} # RabbitMQConnectionHTTPSCertificate
        rabbit_mq_connection_https_certificate_model['name'] = 'testString'
        rabbit_mq_connection_https_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a RabbitMQConnectionHTTPS model
        rabbit_mq_connection_https_model_json = {}
        rabbit_mq_connection_https_model_json['type'] = 'uri'
        rabbit_mq_connection_https_model_json['composed'] = ['testString']
        rabbit_mq_connection_https_model_json['scheme'] = 'testString'
        rabbit_mq_connection_https_model_json['hosts'] = [rabbit_mq_connection_https_hosts_item_model]
        rabbit_mq_connection_https_model_json['path'] = 'testString'
        rabbit_mq_connection_https_model_json['query_options'] = { 'foo': 'bar' }
        rabbit_mq_connection_https_model_json['authentication'] = rabbit_mq_connection_https_authentication_model
        rabbit_mq_connection_https_model_json['certificate'] = rabbit_mq_connection_https_certificate_model
        rabbit_mq_connection_https_model_json['browser_accessible'] = True

        # Construct a model instance of RabbitMQConnectionHTTPS by calling from_dict on the json representation
        rabbit_mq_connection_https_model = RabbitMQConnectionHTTPS.from_dict(rabbit_mq_connection_https_model_json)
        assert rabbit_mq_connection_https_model != False

        # Construct a model instance of RabbitMQConnectionHTTPS by calling from_dict on the json representation
        rabbit_mq_connection_https_model_dict = RabbitMQConnectionHTTPS.from_dict(rabbit_mq_connection_https_model_json).__dict__
        rabbit_mq_connection_https_model2 = RabbitMQConnectionHTTPS(**rabbit_mq_connection_https_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_https_model == rabbit_mq_connection_https_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_https_model_json2 = rabbit_mq_connection_https_model.to_dict()
        assert rabbit_mq_connection_https_model_json2 == rabbit_mq_connection_https_model_json

class TestRabbitMQConnectionHTTPSAuthentication():
    """
    Test Class for RabbitMQConnectionHTTPSAuthentication
    """

    def test_rabbit_mq_connection_https_authentication_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionHTTPSAuthentication
        """

        # Construct a json representation of a RabbitMQConnectionHTTPSAuthentication model
        rabbit_mq_connection_https_authentication_model_json = {}
        rabbit_mq_connection_https_authentication_model_json['method'] = 'testString'
        rabbit_mq_connection_https_authentication_model_json['username'] = 'testString'
        rabbit_mq_connection_https_authentication_model_json['password'] = 'testString'

        # Construct a model instance of RabbitMQConnectionHTTPSAuthentication by calling from_dict on the json representation
        rabbit_mq_connection_https_authentication_model = RabbitMQConnectionHTTPSAuthentication.from_dict(rabbit_mq_connection_https_authentication_model_json)
        assert rabbit_mq_connection_https_authentication_model != False

        # Construct a model instance of RabbitMQConnectionHTTPSAuthentication by calling from_dict on the json representation
        rabbit_mq_connection_https_authentication_model_dict = RabbitMQConnectionHTTPSAuthentication.from_dict(rabbit_mq_connection_https_authentication_model_json).__dict__
        rabbit_mq_connection_https_authentication_model2 = RabbitMQConnectionHTTPSAuthentication(**rabbit_mq_connection_https_authentication_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_https_authentication_model == rabbit_mq_connection_https_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_https_authentication_model_json2 = rabbit_mq_connection_https_authentication_model.to_dict()
        assert rabbit_mq_connection_https_authentication_model_json2 == rabbit_mq_connection_https_authentication_model_json

class TestRabbitMQConnectionHTTPSCertificate():
    """
    Test Class for RabbitMQConnectionHTTPSCertificate
    """

    def test_rabbit_mq_connection_https_certificate_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionHTTPSCertificate
        """

        # Construct a json representation of a RabbitMQConnectionHTTPSCertificate model
        rabbit_mq_connection_https_certificate_model_json = {}
        rabbit_mq_connection_https_certificate_model_json['name'] = 'testString'
        rabbit_mq_connection_https_certificate_model_json['certificate_base64'] = 'testString'

        # Construct a model instance of RabbitMQConnectionHTTPSCertificate by calling from_dict on the json representation
        rabbit_mq_connection_https_certificate_model = RabbitMQConnectionHTTPSCertificate.from_dict(rabbit_mq_connection_https_certificate_model_json)
        assert rabbit_mq_connection_https_certificate_model != False

        # Construct a model instance of RabbitMQConnectionHTTPSCertificate by calling from_dict on the json representation
        rabbit_mq_connection_https_certificate_model_dict = RabbitMQConnectionHTTPSCertificate.from_dict(rabbit_mq_connection_https_certificate_model_json).__dict__
        rabbit_mq_connection_https_certificate_model2 = RabbitMQConnectionHTTPSCertificate(**rabbit_mq_connection_https_certificate_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_https_certificate_model == rabbit_mq_connection_https_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_https_certificate_model_json2 = rabbit_mq_connection_https_certificate_model.to_dict()
        assert rabbit_mq_connection_https_certificate_model_json2 == rabbit_mq_connection_https_certificate_model_json

class TestRabbitMQConnectionHTTPSHostsItem():
    """
    Test Class for RabbitMQConnectionHTTPSHostsItem
    """

    def test_rabbit_mq_connection_https_hosts_item_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionHTTPSHostsItem
        """

        # Construct a json representation of a RabbitMQConnectionHTTPSHostsItem model
        rabbit_mq_connection_https_hosts_item_model_json = {}
        rabbit_mq_connection_https_hosts_item_model_json['hostname'] = 'testString'
        rabbit_mq_connection_https_hosts_item_model_json['port'] = 38

        # Construct a model instance of RabbitMQConnectionHTTPSHostsItem by calling from_dict on the json representation
        rabbit_mq_connection_https_hosts_item_model = RabbitMQConnectionHTTPSHostsItem.from_dict(rabbit_mq_connection_https_hosts_item_model_json)
        assert rabbit_mq_connection_https_hosts_item_model != False

        # Construct a model instance of RabbitMQConnectionHTTPSHostsItem by calling from_dict on the json representation
        rabbit_mq_connection_https_hosts_item_model_dict = RabbitMQConnectionHTTPSHostsItem.from_dict(rabbit_mq_connection_https_hosts_item_model_json).__dict__
        rabbit_mq_connection_https_hosts_item_model2 = RabbitMQConnectionHTTPSHostsItem(**rabbit_mq_connection_https_hosts_item_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_https_hosts_item_model == rabbit_mq_connection_https_hosts_item_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_https_hosts_item_model_json2 = rabbit_mq_connection_https_hosts_item_model.to_dict()
        assert rabbit_mq_connection_https_hosts_item_model_json2 == rabbit_mq_connection_https_hosts_item_model_json

class TestRabbitMQConnectionMQTTS():
    """
    Test Class for RabbitMQConnectionMQTTS
    """

    def test_rabbit_mq_connection_mqtts_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionMQTTS
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rabbit_mq_connection_mqtts_hosts_item_model = {} # RabbitMQConnectionMQTTSHostsItem
        rabbit_mq_connection_mqtts_hosts_item_model['hostname'] = 'testString'
        rabbit_mq_connection_mqtts_hosts_item_model['port'] = 38

        rabbit_mq_connection_mqtts_authentication_model = {} # RabbitMQConnectionMQTTSAuthentication
        rabbit_mq_connection_mqtts_authentication_model['method'] = 'testString'
        rabbit_mq_connection_mqtts_authentication_model['username'] = 'testString'
        rabbit_mq_connection_mqtts_authentication_model['password'] = 'testString'

        rabbit_mq_connection_mqtts_certificate_model = {} # RabbitMQConnectionMQTTSCertificate
        rabbit_mq_connection_mqtts_certificate_model['name'] = 'testString'
        rabbit_mq_connection_mqtts_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a RabbitMQConnectionMQTTS model
        rabbit_mq_connection_mqtts_model_json = {}
        rabbit_mq_connection_mqtts_model_json['type'] = 'uri'
        rabbit_mq_connection_mqtts_model_json['composed'] = ['testString']
        rabbit_mq_connection_mqtts_model_json['scheme'] = 'testString'
        rabbit_mq_connection_mqtts_model_json['hosts'] = [rabbit_mq_connection_mqtts_hosts_item_model]
        rabbit_mq_connection_mqtts_model_json['path'] = 'testString'
        rabbit_mq_connection_mqtts_model_json['query_options'] = { 'foo': 'bar' }
        rabbit_mq_connection_mqtts_model_json['authentication'] = rabbit_mq_connection_mqtts_authentication_model
        rabbit_mq_connection_mqtts_model_json['certificate'] = rabbit_mq_connection_mqtts_certificate_model

        # Construct a model instance of RabbitMQConnectionMQTTS by calling from_dict on the json representation
        rabbit_mq_connection_mqtts_model = RabbitMQConnectionMQTTS.from_dict(rabbit_mq_connection_mqtts_model_json)
        assert rabbit_mq_connection_mqtts_model != False

        # Construct a model instance of RabbitMQConnectionMQTTS by calling from_dict on the json representation
        rabbit_mq_connection_mqtts_model_dict = RabbitMQConnectionMQTTS.from_dict(rabbit_mq_connection_mqtts_model_json).__dict__
        rabbit_mq_connection_mqtts_model2 = RabbitMQConnectionMQTTS(**rabbit_mq_connection_mqtts_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_mqtts_model == rabbit_mq_connection_mqtts_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_mqtts_model_json2 = rabbit_mq_connection_mqtts_model.to_dict()
        assert rabbit_mq_connection_mqtts_model_json2 == rabbit_mq_connection_mqtts_model_json

class TestRabbitMQConnectionMQTTSAuthentication():
    """
    Test Class for RabbitMQConnectionMQTTSAuthentication
    """

    def test_rabbit_mq_connection_mqtts_authentication_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionMQTTSAuthentication
        """

        # Construct a json representation of a RabbitMQConnectionMQTTSAuthentication model
        rabbit_mq_connection_mqtts_authentication_model_json = {}
        rabbit_mq_connection_mqtts_authentication_model_json['method'] = 'testString'
        rabbit_mq_connection_mqtts_authentication_model_json['username'] = 'testString'
        rabbit_mq_connection_mqtts_authentication_model_json['password'] = 'testString'

        # Construct a model instance of RabbitMQConnectionMQTTSAuthentication by calling from_dict on the json representation
        rabbit_mq_connection_mqtts_authentication_model = RabbitMQConnectionMQTTSAuthentication.from_dict(rabbit_mq_connection_mqtts_authentication_model_json)
        assert rabbit_mq_connection_mqtts_authentication_model != False

        # Construct a model instance of RabbitMQConnectionMQTTSAuthentication by calling from_dict on the json representation
        rabbit_mq_connection_mqtts_authentication_model_dict = RabbitMQConnectionMQTTSAuthentication.from_dict(rabbit_mq_connection_mqtts_authentication_model_json).__dict__
        rabbit_mq_connection_mqtts_authentication_model2 = RabbitMQConnectionMQTTSAuthentication(**rabbit_mq_connection_mqtts_authentication_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_mqtts_authentication_model == rabbit_mq_connection_mqtts_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_mqtts_authentication_model_json2 = rabbit_mq_connection_mqtts_authentication_model.to_dict()
        assert rabbit_mq_connection_mqtts_authentication_model_json2 == rabbit_mq_connection_mqtts_authentication_model_json

class TestRabbitMQConnectionMQTTSCertificate():
    """
    Test Class for RabbitMQConnectionMQTTSCertificate
    """

    def test_rabbit_mq_connection_mqtts_certificate_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionMQTTSCertificate
        """

        # Construct a json representation of a RabbitMQConnectionMQTTSCertificate model
        rabbit_mq_connection_mqtts_certificate_model_json = {}
        rabbit_mq_connection_mqtts_certificate_model_json['name'] = 'testString'
        rabbit_mq_connection_mqtts_certificate_model_json['certificate_base64'] = 'testString'

        # Construct a model instance of RabbitMQConnectionMQTTSCertificate by calling from_dict on the json representation
        rabbit_mq_connection_mqtts_certificate_model = RabbitMQConnectionMQTTSCertificate.from_dict(rabbit_mq_connection_mqtts_certificate_model_json)
        assert rabbit_mq_connection_mqtts_certificate_model != False

        # Construct a model instance of RabbitMQConnectionMQTTSCertificate by calling from_dict on the json representation
        rabbit_mq_connection_mqtts_certificate_model_dict = RabbitMQConnectionMQTTSCertificate.from_dict(rabbit_mq_connection_mqtts_certificate_model_json).__dict__
        rabbit_mq_connection_mqtts_certificate_model2 = RabbitMQConnectionMQTTSCertificate(**rabbit_mq_connection_mqtts_certificate_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_mqtts_certificate_model == rabbit_mq_connection_mqtts_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_mqtts_certificate_model_json2 = rabbit_mq_connection_mqtts_certificate_model.to_dict()
        assert rabbit_mq_connection_mqtts_certificate_model_json2 == rabbit_mq_connection_mqtts_certificate_model_json

class TestRabbitMQConnectionMQTTSHostsItem():
    """
    Test Class for RabbitMQConnectionMQTTSHostsItem
    """

    def test_rabbit_mq_connection_mqtts_hosts_item_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionMQTTSHostsItem
        """

        # Construct a json representation of a RabbitMQConnectionMQTTSHostsItem model
        rabbit_mq_connection_mqtts_hosts_item_model_json = {}
        rabbit_mq_connection_mqtts_hosts_item_model_json['hostname'] = 'testString'
        rabbit_mq_connection_mqtts_hosts_item_model_json['port'] = 38

        # Construct a model instance of RabbitMQConnectionMQTTSHostsItem by calling from_dict on the json representation
        rabbit_mq_connection_mqtts_hosts_item_model = RabbitMQConnectionMQTTSHostsItem.from_dict(rabbit_mq_connection_mqtts_hosts_item_model_json)
        assert rabbit_mq_connection_mqtts_hosts_item_model != False

        # Construct a model instance of RabbitMQConnectionMQTTSHostsItem by calling from_dict on the json representation
        rabbit_mq_connection_mqtts_hosts_item_model_dict = RabbitMQConnectionMQTTSHostsItem.from_dict(rabbit_mq_connection_mqtts_hosts_item_model_json).__dict__
        rabbit_mq_connection_mqtts_hosts_item_model2 = RabbitMQConnectionMQTTSHostsItem(**rabbit_mq_connection_mqtts_hosts_item_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_mqtts_hosts_item_model == rabbit_mq_connection_mqtts_hosts_item_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_mqtts_hosts_item_model_json2 = rabbit_mq_connection_mqtts_hosts_item_model.to_dict()
        assert rabbit_mq_connection_mqtts_hosts_item_model_json2 == rabbit_mq_connection_mqtts_hosts_item_model_json

class TestRabbitMQConnectionStompSSL():
    """
    Test Class for RabbitMQConnectionStompSSL
    """

    def test_rabbit_mq_connection_stomp_ssl_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionStompSSL
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rabbit_mq_connection_stomp_ssl_hosts_item_model = {} # RabbitMQConnectionStompSSLHostsItem
        rabbit_mq_connection_stomp_ssl_hosts_item_model['hostname'] = 'testString'
        rabbit_mq_connection_stomp_ssl_hosts_item_model['port'] = 38

        rabbit_mq_connection_stomp_ssl_authentication_model = {} # RabbitMQConnectionStompSSLAuthentication
        rabbit_mq_connection_stomp_ssl_authentication_model['method'] = 'testString'
        rabbit_mq_connection_stomp_ssl_authentication_model['username'] = 'testString'
        rabbit_mq_connection_stomp_ssl_authentication_model['password'] = 'testString'

        rabbit_mq_connection_stomp_ssl_certificate_model = {} # RabbitMQConnectionStompSSLCertificate
        rabbit_mq_connection_stomp_ssl_certificate_model['name'] = 'testString'
        rabbit_mq_connection_stomp_ssl_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a RabbitMQConnectionStompSSL model
        rabbit_mq_connection_stomp_ssl_model_json = {}
        rabbit_mq_connection_stomp_ssl_model_json['type'] = 'testString'
        rabbit_mq_connection_stomp_ssl_model_json['composed'] = ['testString']
        rabbit_mq_connection_stomp_ssl_model_json['hosts'] = [rabbit_mq_connection_stomp_ssl_hosts_item_model]
        rabbit_mq_connection_stomp_ssl_model_json['authentication'] = rabbit_mq_connection_stomp_ssl_authentication_model
        rabbit_mq_connection_stomp_ssl_model_json['certificate'] = rabbit_mq_connection_stomp_ssl_certificate_model
        rabbit_mq_connection_stomp_ssl_model_json['ssl'] = True

        # Construct a model instance of RabbitMQConnectionStompSSL by calling from_dict on the json representation
        rabbit_mq_connection_stomp_ssl_model = RabbitMQConnectionStompSSL.from_dict(rabbit_mq_connection_stomp_ssl_model_json)
        assert rabbit_mq_connection_stomp_ssl_model != False

        # Construct a model instance of RabbitMQConnectionStompSSL by calling from_dict on the json representation
        rabbit_mq_connection_stomp_ssl_model_dict = RabbitMQConnectionStompSSL.from_dict(rabbit_mq_connection_stomp_ssl_model_json).__dict__
        rabbit_mq_connection_stomp_ssl_model2 = RabbitMQConnectionStompSSL(**rabbit_mq_connection_stomp_ssl_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_stomp_ssl_model == rabbit_mq_connection_stomp_ssl_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_stomp_ssl_model_json2 = rabbit_mq_connection_stomp_ssl_model.to_dict()
        assert rabbit_mq_connection_stomp_ssl_model_json2 == rabbit_mq_connection_stomp_ssl_model_json

class TestRabbitMQConnectionStompSSLAuthentication():
    """
    Test Class for RabbitMQConnectionStompSSLAuthentication
    """

    def test_rabbit_mq_connection_stomp_ssl_authentication_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionStompSSLAuthentication
        """

        # Construct a json representation of a RabbitMQConnectionStompSSLAuthentication model
        rabbit_mq_connection_stomp_ssl_authentication_model_json = {}
        rabbit_mq_connection_stomp_ssl_authentication_model_json['method'] = 'testString'
        rabbit_mq_connection_stomp_ssl_authentication_model_json['username'] = 'testString'
        rabbit_mq_connection_stomp_ssl_authentication_model_json['password'] = 'testString'

        # Construct a model instance of RabbitMQConnectionStompSSLAuthentication by calling from_dict on the json representation
        rabbit_mq_connection_stomp_ssl_authentication_model = RabbitMQConnectionStompSSLAuthentication.from_dict(rabbit_mq_connection_stomp_ssl_authentication_model_json)
        assert rabbit_mq_connection_stomp_ssl_authentication_model != False

        # Construct a model instance of RabbitMQConnectionStompSSLAuthentication by calling from_dict on the json representation
        rabbit_mq_connection_stomp_ssl_authentication_model_dict = RabbitMQConnectionStompSSLAuthentication.from_dict(rabbit_mq_connection_stomp_ssl_authentication_model_json).__dict__
        rabbit_mq_connection_stomp_ssl_authentication_model2 = RabbitMQConnectionStompSSLAuthentication(**rabbit_mq_connection_stomp_ssl_authentication_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_stomp_ssl_authentication_model == rabbit_mq_connection_stomp_ssl_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_stomp_ssl_authentication_model_json2 = rabbit_mq_connection_stomp_ssl_authentication_model.to_dict()
        assert rabbit_mq_connection_stomp_ssl_authentication_model_json2 == rabbit_mq_connection_stomp_ssl_authentication_model_json

class TestRabbitMQConnectionStompSSLCertificate():
    """
    Test Class for RabbitMQConnectionStompSSLCertificate
    """

    def test_rabbit_mq_connection_stomp_ssl_certificate_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionStompSSLCertificate
        """

        # Construct a json representation of a RabbitMQConnectionStompSSLCertificate model
        rabbit_mq_connection_stomp_ssl_certificate_model_json = {}
        rabbit_mq_connection_stomp_ssl_certificate_model_json['name'] = 'testString'
        rabbit_mq_connection_stomp_ssl_certificate_model_json['certificate_base64'] = 'testString'

        # Construct a model instance of RabbitMQConnectionStompSSLCertificate by calling from_dict on the json representation
        rabbit_mq_connection_stomp_ssl_certificate_model = RabbitMQConnectionStompSSLCertificate.from_dict(rabbit_mq_connection_stomp_ssl_certificate_model_json)
        assert rabbit_mq_connection_stomp_ssl_certificate_model != False

        # Construct a model instance of RabbitMQConnectionStompSSLCertificate by calling from_dict on the json representation
        rabbit_mq_connection_stomp_ssl_certificate_model_dict = RabbitMQConnectionStompSSLCertificate.from_dict(rabbit_mq_connection_stomp_ssl_certificate_model_json).__dict__
        rabbit_mq_connection_stomp_ssl_certificate_model2 = RabbitMQConnectionStompSSLCertificate(**rabbit_mq_connection_stomp_ssl_certificate_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_stomp_ssl_certificate_model == rabbit_mq_connection_stomp_ssl_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_stomp_ssl_certificate_model_json2 = rabbit_mq_connection_stomp_ssl_certificate_model.to_dict()
        assert rabbit_mq_connection_stomp_ssl_certificate_model_json2 == rabbit_mq_connection_stomp_ssl_certificate_model_json

class TestRabbitMQConnectionStompSSLHostsItem():
    """
    Test Class for RabbitMQConnectionStompSSLHostsItem
    """

    def test_rabbit_mq_connection_stomp_ssl_hosts_item_serialization(self):
        """
        Test serialization/deserialization for RabbitMQConnectionStompSSLHostsItem
        """

        # Construct a json representation of a RabbitMQConnectionStompSSLHostsItem model
        rabbit_mq_connection_stomp_ssl_hosts_item_model_json = {}
        rabbit_mq_connection_stomp_ssl_hosts_item_model_json['hostname'] = 'testString'
        rabbit_mq_connection_stomp_ssl_hosts_item_model_json['port'] = 38

        # Construct a model instance of RabbitMQConnectionStompSSLHostsItem by calling from_dict on the json representation
        rabbit_mq_connection_stomp_ssl_hosts_item_model = RabbitMQConnectionStompSSLHostsItem.from_dict(rabbit_mq_connection_stomp_ssl_hosts_item_model_json)
        assert rabbit_mq_connection_stomp_ssl_hosts_item_model != False

        # Construct a model instance of RabbitMQConnectionStompSSLHostsItem by calling from_dict on the json representation
        rabbit_mq_connection_stomp_ssl_hosts_item_model_dict = RabbitMQConnectionStompSSLHostsItem.from_dict(rabbit_mq_connection_stomp_ssl_hosts_item_model_json).__dict__
        rabbit_mq_connection_stomp_ssl_hosts_item_model2 = RabbitMQConnectionStompSSLHostsItem(**rabbit_mq_connection_stomp_ssl_hosts_item_model_dict)

        # Verify the model instances are equivalent
        assert rabbit_mq_connection_stomp_ssl_hosts_item_model == rabbit_mq_connection_stomp_ssl_hosts_item_model2

        # Convert model instance back to dict and verify no loss of data
        rabbit_mq_connection_stomp_ssl_hosts_item_model_json2 = rabbit_mq_connection_stomp_ssl_hosts_item_model.to_dict()
        assert rabbit_mq_connection_stomp_ssl_hosts_item_model_json2 == rabbit_mq_connection_stomp_ssl_hosts_item_model_json

class TestRedisConnectionURI():
    """
    Test Class for RedisConnectionURI
    """

    def test_redis_connection_uri_serialization(self):
        """
        Test serialization/deserialization for RedisConnectionURI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        redis_connection_uri_hosts_item_model = {} # RedisConnectionURIHostsItem
        redis_connection_uri_hosts_item_model['hostname'] = 'testString'
        redis_connection_uri_hosts_item_model['port'] = 38

        redis_connection_uri_authentication_model = {} # RedisConnectionURIAuthentication
        redis_connection_uri_authentication_model['method'] = 'testString'
        redis_connection_uri_authentication_model['username'] = 'testString'
        redis_connection_uri_authentication_model['password'] = 'testString'

        redis_connection_uri_certificate_model = {} # RedisConnectionURICertificate
        redis_connection_uri_certificate_model['name'] = 'testString'
        redis_connection_uri_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a RedisConnectionURI model
        redis_connection_uri_model_json = {}
        redis_connection_uri_model_json['type'] = 'uri'
        redis_connection_uri_model_json['composed'] = ['testString']
        redis_connection_uri_model_json['scheme'] = 'testString'
        redis_connection_uri_model_json['hosts'] = [redis_connection_uri_hosts_item_model]
        redis_connection_uri_model_json['path'] = '/0'
        redis_connection_uri_model_json['query_options'] = { 'foo': 'bar' }
        redis_connection_uri_model_json['authentication'] = redis_connection_uri_authentication_model
        redis_connection_uri_model_json['certificate'] = redis_connection_uri_certificate_model
        redis_connection_uri_model_json['database'] = 38

        # Construct a model instance of RedisConnectionURI by calling from_dict on the json representation
        redis_connection_uri_model = RedisConnectionURI.from_dict(redis_connection_uri_model_json)
        assert redis_connection_uri_model != False

        # Construct a model instance of RedisConnectionURI by calling from_dict on the json representation
        redis_connection_uri_model_dict = RedisConnectionURI.from_dict(redis_connection_uri_model_json).__dict__
        redis_connection_uri_model2 = RedisConnectionURI(**redis_connection_uri_model_dict)

        # Verify the model instances are equivalent
        assert redis_connection_uri_model == redis_connection_uri_model2

        # Convert model instance back to dict and verify no loss of data
        redis_connection_uri_model_json2 = redis_connection_uri_model.to_dict()
        assert redis_connection_uri_model_json2 == redis_connection_uri_model_json

class TestRedisConnectionURIAuthentication():
    """
    Test Class for RedisConnectionURIAuthentication
    """

    def test_redis_connection_uri_authentication_serialization(self):
        """
        Test serialization/deserialization for RedisConnectionURIAuthentication
        """

        # Construct a json representation of a RedisConnectionURIAuthentication model
        redis_connection_uri_authentication_model_json = {}
        redis_connection_uri_authentication_model_json['method'] = 'testString'
        redis_connection_uri_authentication_model_json['username'] = 'testString'
        redis_connection_uri_authentication_model_json['password'] = 'testString'

        # Construct a model instance of RedisConnectionURIAuthentication by calling from_dict on the json representation
        redis_connection_uri_authentication_model = RedisConnectionURIAuthentication.from_dict(redis_connection_uri_authentication_model_json)
        assert redis_connection_uri_authentication_model != False

        # Construct a model instance of RedisConnectionURIAuthentication by calling from_dict on the json representation
        redis_connection_uri_authentication_model_dict = RedisConnectionURIAuthentication.from_dict(redis_connection_uri_authentication_model_json).__dict__
        redis_connection_uri_authentication_model2 = RedisConnectionURIAuthentication(**redis_connection_uri_authentication_model_dict)

        # Verify the model instances are equivalent
        assert redis_connection_uri_authentication_model == redis_connection_uri_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        redis_connection_uri_authentication_model_json2 = redis_connection_uri_authentication_model.to_dict()
        assert redis_connection_uri_authentication_model_json2 == redis_connection_uri_authentication_model_json

class TestRedisConnectionURICertificate():
    """
    Test Class for RedisConnectionURICertificate
    """

    def test_redis_connection_uri_certificate_serialization(self):
        """
        Test serialization/deserialization for RedisConnectionURICertificate
        """

        # Construct a json representation of a RedisConnectionURICertificate model
        redis_connection_uri_certificate_model_json = {}
        redis_connection_uri_certificate_model_json['name'] = 'testString'
        redis_connection_uri_certificate_model_json['certificate_base64'] = 'testString'

        # Construct a model instance of RedisConnectionURICertificate by calling from_dict on the json representation
        redis_connection_uri_certificate_model = RedisConnectionURICertificate.from_dict(redis_connection_uri_certificate_model_json)
        assert redis_connection_uri_certificate_model != False

        # Construct a model instance of RedisConnectionURICertificate by calling from_dict on the json representation
        redis_connection_uri_certificate_model_dict = RedisConnectionURICertificate.from_dict(redis_connection_uri_certificate_model_json).__dict__
        redis_connection_uri_certificate_model2 = RedisConnectionURICertificate(**redis_connection_uri_certificate_model_dict)

        # Verify the model instances are equivalent
        assert redis_connection_uri_certificate_model == redis_connection_uri_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        redis_connection_uri_certificate_model_json2 = redis_connection_uri_certificate_model.to_dict()
        assert redis_connection_uri_certificate_model_json2 == redis_connection_uri_certificate_model_json

class TestRedisConnectionURIHostsItem():
    """
    Test Class for RedisConnectionURIHostsItem
    """

    def test_redis_connection_uri_hosts_item_serialization(self):
        """
        Test serialization/deserialization for RedisConnectionURIHostsItem
        """

        # Construct a json representation of a RedisConnectionURIHostsItem model
        redis_connection_uri_hosts_item_model_json = {}
        redis_connection_uri_hosts_item_model_json['hostname'] = 'testString'
        redis_connection_uri_hosts_item_model_json['port'] = 38

        # Construct a model instance of RedisConnectionURIHostsItem by calling from_dict on the json representation
        redis_connection_uri_hosts_item_model = RedisConnectionURIHostsItem.from_dict(redis_connection_uri_hosts_item_model_json)
        assert redis_connection_uri_hosts_item_model != False

        # Construct a model instance of RedisConnectionURIHostsItem by calling from_dict on the json representation
        redis_connection_uri_hosts_item_model_dict = RedisConnectionURIHostsItem.from_dict(redis_connection_uri_hosts_item_model_json).__dict__
        redis_connection_uri_hosts_item_model2 = RedisConnectionURIHostsItem(**redis_connection_uri_hosts_item_model_dict)

        # Verify the model instances are equivalent
        assert redis_connection_uri_hosts_item_model == redis_connection_uri_hosts_item_model2

        # Convert model instance back to dict and verify no loss of data
        redis_connection_uri_hosts_item_model_json2 = redis_connection_uri_hosts_item_model.to_dict()
        assert redis_connection_uri_hosts_item_model_json2 == redis_connection_uri_hosts_item_model_json

class TestRemotes():
    """
    Test Class for Remotes
    """

    def test_remotes_serialization(self):
        """
        Test serialization/deserialization for Remotes
        """

        # Construct a json representation of a Remotes model
        remotes_model_json = {}
        remotes_model_json['leader'] = '01f30581-54f8-41a4-8193-4a04cc022e9b-h'
        remotes_model_json['replicas'] = ['23h40521-57g6-31b5-9256-6b15df456f7j-g', 'g1d8g764-hngm-595j-7349450f3058-y']

        # Construct a model instance of Remotes by calling from_dict on the json representation
        remotes_model = Remotes.from_dict(remotes_model_json)
        assert remotes_model != False

        # Construct a model instance of Remotes by calling from_dict on the json representation
        remotes_model_dict = Remotes.from_dict(remotes_model_json).__dict__
        remotes_model2 = Remotes(**remotes_model_dict)

        # Verify the model instances are equivalent
        assert remotes_model == remotes_model2

        # Convert model instance back to dict and verify no loss of data
        remotes_model_json2 = remotes_model.to_dict()
        assert remotes_model_json2 == remotes_model_json

class TestResyncReplicaResponse():
    """
    Test Class for ResyncReplicaResponse
    """

    def test_resync_replica_response_serialization(self):
        """
        Test serialization/deserialization for ResyncReplicaResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc257516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:5abb6a7d11a1a5001479a0b0'
        task_model['description'] = 'Reinitializing read-only replica.'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc257516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:31:30Z"))

        # Construct a json representation of a ResyncReplicaResponse model
        resync_replica_response_model_json = {}
        resync_replica_response_model_json['task'] = task_model

        # Construct a model instance of ResyncReplicaResponse by calling from_dict on the json representation
        resync_replica_response_model = ResyncReplicaResponse.from_dict(resync_replica_response_model_json)
        assert resync_replica_response_model != False

        # Construct a model instance of ResyncReplicaResponse by calling from_dict on the json representation
        resync_replica_response_model_dict = ResyncReplicaResponse.from_dict(resync_replica_response_model_json).__dict__
        resync_replica_response_model2 = ResyncReplicaResponse(**resync_replica_response_model_dict)

        # Verify the model instances are equivalent
        assert resync_replica_response_model == resync_replica_response_model2

        # Convert model instance back to dict and verify no loss of data
        resync_replica_response_model_json2 = resync_replica_response_model.to_dict()
        assert resync_replica_response_model_json2 == resync_replica_response_model_json

class TestSetAllowlistResponse():
    """
    Test Class for SetAllowlistResponse
    """

    def test_set_allowlist_response_serialization(self):
        """
        Test serialization/deserialization for SetAllowlistResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-b5c96544573b'
        task_model['description'] = 'Updating allowlist for database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 10
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:21:30Z"))

        # Construct a json representation of a SetAllowlistResponse model
        set_allowlist_response_model_json = {}
        set_allowlist_response_model_json['task'] = task_model

        # Construct a model instance of SetAllowlistResponse by calling from_dict on the json representation
        set_allowlist_response_model = SetAllowlistResponse.from_dict(set_allowlist_response_model_json)
        assert set_allowlist_response_model != False

        # Construct a model instance of SetAllowlistResponse by calling from_dict on the json representation
        set_allowlist_response_model_dict = SetAllowlistResponse.from_dict(set_allowlist_response_model_json).__dict__
        set_allowlist_response_model2 = SetAllowlistResponse(**set_allowlist_response_model_dict)

        # Verify the model instances are equivalent
        assert set_allowlist_response_model == set_allowlist_response_model2

        # Convert model instance back to dict and verify no loss of data
        set_allowlist_response_model_json2 = set_allowlist_response_model.to_dict()
        assert set_allowlist_response_model_json2 == set_allowlist_response_model_json

class TestSetAutoscalingConditionsResponse():
    """
    Test Class for SetAutoscalingConditionsResponse
    """

    def test_set_autoscaling_conditions_response_serialization(self):
        """
        Test serialization/deserialization for SetAutoscalingConditionsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423a4ef238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4d36-92f3-b5c96544393b'
        task_model['description'] = 'Synthesized autoscaling'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 38
        task_model['created_at'] = datetime_to_string(string_to_datetime("2019-10-17T14:15:52.393Z"))

        # Construct a json representation of a SetAutoscalingConditionsResponse model
        set_autoscaling_conditions_response_model_json = {}
        set_autoscaling_conditions_response_model_json['task'] = task_model

        # Construct a model instance of SetAutoscalingConditionsResponse by calling from_dict on the json representation
        set_autoscaling_conditions_response_model = SetAutoscalingConditionsResponse.from_dict(set_autoscaling_conditions_response_model_json)
        assert set_autoscaling_conditions_response_model != False

        # Construct a model instance of SetAutoscalingConditionsResponse by calling from_dict on the json representation
        set_autoscaling_conditions_response_model_dict = SetAutoscalingConditionsResponse.from_dict(set_autoscaling_conditions_response_model_json).__dict__
        set_autoscaling_conditions_response_model2 = SetAutoscalingConditionsResponse(**set_autoscaling_conditions_response_model_dict)

        # Verify the model instances are equivalent
        assert set_autoscaling_conditions_response_model == set_autoscaling_conditions_response_model2

        # Convert model instance back to dict and verify no loss of data
        set_autoscaling_conditions_response_model_json2 = set_autoscaling_conditions_response_model.to_dict()
        assert set_autoscaling_conditions_response_model_json2 == set_autoscaling_conditions_response_model_json

class TestSetCPUGroupCPU():
    """
    Test Class for SetCPUGroupCPU
    """

    def test_set_cpu_group_cpu_serialization(self):
        """
        Test serialization/deserialization for SetCPUGroupCPU
        """

        # Construct a json representation of a SetCPUGroupCPU model
        set_cpu_group_cpu_model_json = {}
        set_cpu_group_cpu_model_json['allocation_count'] = 2

        # Construct a model instance of SetCPUGroupCPU by calling from_dict on the json representation
        set_cpu_group_cpu_model = SetCPUGroupCPU.from_dict(set_cpu_group_cpu_model_json)
        assert set_cpu_group_cpu_model != False

        # Construct a model instance of SetCPUGroupCPU by calling from_dict on the json representation
        set_cpu_group_cpu_model_dict = SetCPUGroupCPU.from_dict(set_cpu_group_cpu_model_json).__dict__
        set_cpu_group_cpu_model2 = SetCPUGroupCPU(**set_cpu_group_cpu_model_dict)

        # Verify the model instances are equivalent
        assert set_cpu_group_cpu_model == set_cpu_group_cpu_model2

        # Convert model instance back to dict and verify no loss of data
        set_cpu_group_cpu_model_json2 = set_cpu_group_cpu_model.to_dict()
        assert set_cpu_group_cpu_model_json2 == set_cpu_group_cpu_model_json

class TestSetDeploymentScalingGroupResponse():
    """
    Test Class for SetDeploymentScalingGroupResponse
    """

    def test_set_deployment_scaling_group_response_serialization(self):
        """
        Test serialization/deserialization for SetDeploymentScalingGroupResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f4-b5c96544393b'
        task_model['description'] = 'Scaling database deployment'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:20:30Z"))

        # Construct a json representation of a SetDeploymentScalingGroupResponse model
        set_deployment_scaling_group_response_model_json = {}
        set_deployment_scaling_group_response_model_json['task'] = task_model

        # Construct a model instance of SetDeploymentScalingGroupResponse by calling from_dict on the json representation
        set_deployment_scaling_group_response_model = SetDeploymentScalingGroupResponse.from_dict(set_deployment_scaling_group_response_model_json)
        assert set_deployment_scaling_group_response_model != False

        # Construct a model instance of SetDeploymentScalingGroupResponse by calling from_dict on the json representation
        set_deployment_scaling_group_response_model_dict = SetDeploymentScalingGroupResponse.from_dict(set_deployment_scaling_group_response_model_json).__dict__
        set_deployment_scaling_group_response_model2 = SetDeploymentScalingGroupResponse(**set_deployment_scaling_group_response_model_dict)

        # Verify the model instances are equivalent
        assert set_deployment_scaling_group_response_model == set_deployment_scaling_group_response_model2

        # Convert model instance back to dict and verify no loss of data
        set_deployment_scaling_group_response_model_json2 = set_deployment_scaling_group_response_model.to_dict()
        assert set_deployment_scaling_group_response_model_json2 == set_deployment_scaling_group_response_model_json

class TestSetDiskGroupDisk():
    """
    Test Class for SetDiskGroupDisk
    """

    def test_set_disk_group_disk_serialization(self):
        """
        Test serialization/deserialization for SetDiskGroupDisk
        """

        # Construct a json representation of a SetDiskGroupDisk model
        set_disk_group_disk_model_json = {}
        set_disk_group_disk_model_json['allocation_mb'] = 20480

        # Construct a model instance of SetDiskGroupDisk by calling from_dict on the json representation
        set_disk_group_disk_model = SetDiskGroupDisk.from_dict(set_disk_group_disk_model_json)
        assert set_disk_group_disk_model != False

        # Construct a model instance of SetDiskGroupDisk by calling from_dict on the json representation
        set_disk_group_disk_model_dict = SetDiskGroupDisk.from_dict(set_disk_group_disk_model_json).__dict__
        set_disk_group_disk_model2 = SetDiskGroupDisk(**set_disk_group_disk_model_dict)

        # Verify the model instances are equivalent
        assert set_disk_group_disk_model == set_disk_group_disk_model2

        # Convert model instance back to dict and verify no loss of data
        set_disk_group_disk_model_json2 = set_disk_group_disk_model.to_dict()
        assert set_disk_group_disk_model_json2 == set_disk_group_disk_model_json

class TestSetMembersGroupMembers():
    """
    Test Class for SetMembersGroupMembers
    """

    def test_set_members_group_members_serialization(self):
        """
        Test serialization/deserialization for SetMembersGroupMembers
        """

        # Construct a json representation of a SetMembersGroupMembers model
        set_members_group_members_model_json = {}
        set_members_group_members_model_json['allocation_count'] = 4

        # Construct a model instance of SetMembersGroupMembers by calling from_dict on the json representation
        set_members_group_members_model = SetMembersGroupMembers.from_dict(set_members_group_members_model_json)
        assert set_members_group_members_model != False

        # Construct a model instance of SetMembersGroupMembers by calling from_dict on the json representation
        set_members_group_members_model_dict = SetMembersGroupMembers.from_dict(set_members_group_members_model_json).__dict__
        set_members_group_members_model2 = SetMembersGroupMembers(**set_members_group_members_model_dict)

        # Verify the model instances are equivalent
        assert set_members_group_members_model == set_members_group_members_model2

        # Convert model instance back to dict and verify no loss of data
        set_members_group_members_model_json2 = set_members_group_members_model.to_dict()
        assert set_members_group_members_model_json2 == set_members_group_members_model_json

class TestSetMemoryGroupMemory():
    """
    Test Class for SetMemoryGroupMemory
    """

    def test_set_memory_group_memory_serialization(self):
        """
        Test serialization/deserialization for SetMemoryGroupMemory
        """

        # Construct a json representation of a SetMemoryGroupMemory model
        set_memory_group_memory_model_json = {}
        set_memory_group_memory_model_json['allocation_mb'] = 12288

        # Construct a model instance of SetMemoryGroupMemory by calling from_dict on the json representation
        set_memory_group_memory_model = SetMemoryGroupMemory.from_dict(set_memory_group_memory_model_json)
        assert set_memory_group_memory_model != False

        # Construct a model instance of SetMemoryGroupMemory by calling from_dict on the json representation
        set_memory_group_memory_model_dict = SetMemoryGroupMemory.from_dict(set_memory_group_memory_model_json).__dict__
        set_memory_group_memory_model2 = SetMemoryGroupMemory(**set_memory_group_memory_model_dict)

        # Verify the model instances are equivalent
        assert set_memory_group_memory_model == set_memory_group_memory_model2

        # Convert model instance back to dict and verify no loss of data
        set_memory_group_memory_model_json2 = set_memory_group_memory_model.to_dict()
        assert set_memory_group_memory_model_json2 == set_memory_group_memory_model_json

class TestSetPromotionResponse():
    """
    Test Class for SetPromotionResponse
    """

    def test_set_promotion_response_serialization(self):
        """
        Test serialization/deserialization for SetPromotionResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc257516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:5abb6a7d11a1a5001479a0b0'
        task_model['description'] = 'Promoting read-only replica to standalone instance.'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc257516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:31:30Z"))

        # Construct a json representation of a SetPromotionResponse model
        set_promotion_response_model_json = {}
        set_promotion_response_model_json['task'] = task_model

        # Construct a model instance of SetPromotionResponse by calling from_dict on the json representation
        set_promotion_response_model = SetPromotionResponse.from_dict(set_promotion_response_model_json)
        assert set_promotion_response_model != False

        # Construct a model instance of SetPromotionResponse by calling from_dict on the json representation
        set_promotion_response_model_dict = SetPromotionResponse.from_dict(set_promotion_response_model_json).__dict__
        set_promotion_response_model2 = SetPromotionResponse(**set_promotion_response_model_dict)

        # Verify the model instances are equivalent
        assert set_promotion_response_model == set_promotion_response_model2

        # Convert model instance back to dict and verify no loss of data
        set_promotion_response_model_json2 = set_promotion_response_model.to_dict()
        assert set_promotion_response_model_json2 == set_promotion_response_model_json

class TestStartOndemandBackupResponse():
    """
    Test Class for StartOndemandBackupResponse
    """

    def test_start_ondemand_backup_response_serialization(self):
        """
        Test serialization/deserialization for StartOndemandBackupResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f4-b5c96544393b'
        task_model['description'] = 'Backing up database on-demand'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:30:30Z"))

        # Construct a json representation of a StartOndemandBackupResponse model
        start_ondemand_backup_response_model_json = {}
        start_ondemand_backup_response_model_json['task'] = task_model

        # Construct a model instance of StartOndemandBackupResponse by calling from_dict on the json representation
        start_ondemand_backup_response_model = StartOndemandBackupResponse.from_dict(start_ondemand_backup_response_model_json)
        assert start_ondemand_backup_response_model != False

        # Construct a model instance of StartOndemandBackupResponse by calling from_dict on the json representation
        start_ondemand_backup_response_model_dict = StartOndemandBackupResponse.from_dict(start_ondemand_backup_response_model_json).__dict__
        start_ondemand_backup_response_model2 = StartOndemandBackupResponse(**start_ondemand_backup_response_model_dict)

        # Verify the model instances are equivalent
        assert start_ondemand_backup_response_model == start_ondemand_backup_response_model2

        # Convert model instance back to dict and verify no loss of data
        start_ondemand_backup_response_model_json2 = start_ondemand_backup_response_model.to_dict()
        assert start_ondemand_backup_response_model_json2 == start_ondemand_backup_response_model_json

class TestTask():
    """
    Test Class for Task
    """

    def test_task_serialization(self):
        """
        Test serialization/deserialization for Task
        """

        # Construct a json representation of a Task model
        task_model_json = {}
        task_model_json['id'] = 'testString'
        task_model_json['description'] = 'testString'
        task_model_json['status'] = 'running'
        task_model_json['deployment_id'] = 'testString'
        task_model_json['progress_percent'] = 38
        task_model_json['created_at'] = datetime_to_string(string_to_datetime("2019-01-01T12:00:00.000Z"))

        # Construct a model instance of Task by calling from_dict on the json representation
        task_model = Task.from_dict(task_model_json)
        assert task_model != False

        # Construct a model instance of Task by calling from_dict on the json representation
        task_model_dict = Task.from_dict(task_model_json).__dict__
        task_model2 = Task(**task_model_dict)

        # Verify the model instances are equivalent
        assert task_model == task_model2

        # Convert model instance back to dict and verify no loss of data
        task_model_json2 = task_model.to_dict()
        assert task_model_json2 == task_model_json

class TestTasks():
    """
    Test Class for Tasks
    """

    def test_tasks_serialization(self):
        """
        Test serialization/deserialization for Tasks
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f4-b5c96544393b'
        task_model['description'] = 'Backing up database on-demand'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:31:30Z"))

        # Construct a json representation of a Tasks model
        tasks_model_json = {}
        tasks_model_json['tasks'] = [task_model]

        # Construct a model instance of Tasks by calling from_dict on the json representation
        tasks_model = Tasks.from_dict(tasks_model_json)
        assert tasks_model != False

        # Construct a model instance of Tasks by calling from_dict on the json representation
        tasks_model_dict = Tasks.from_dict(tasks_model_json).__dict__
        tasks_model2 = Tasks(**tasks_model_dict)

        # Verify the model instances are equivalent
        assert tasks_model == tasks_model2

        # Convert model instance back to dict and verify no loss of data
        tasks_model_json2 = tasks_model.to_dict()
        assert tasks_model_json2 == tasks_model_json

class TestUpdateDatabaseConfigurationResponse():
    """
    Test Class for UpdateDatabaseConfigurationResponse
    """

    def test_update_database_configuration_response_serialization(self):
        """
        Test serialization/deserialization for UpdateDatabaseConfigurationResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-b5c96544393a'
        task_model['description'] = 'Applying new configuration'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = datetime_to_string(string_to_datetime("2018-03-28T10:31:30Z"))

        # Construct a json representation of a UpdateDatabaseConfigurationResponse model
        update_database_configuration_response_model_json = {}
        update_database_configuration_response_model_json['task'] = task_model

        # Construct a model instance of UpdateDatabaseConfigurationResponse by calling from_dict on the json representation
        update_database_configuration_response_model = UpdateDatabaseConfigurationResponse.from_dict(update_database_configuration_response_model_json)
        assert update_database_configuration_response_model != False

        # Construct a model instance of UpdateDatabaseConfigurationResponse by calling from_dict on the json representation
        update_database_configuration_response_model_dict = UpdateDatabaseConfigurationResponse.from_dict(update_database_configuration_response_model_json).__dict__
        update_database_configuration_response_model2 = UpdateDatabaseConfigurationResponse(**update_database_configuration_response_model_dict)

        # Verify the model instances are equivalent
        assert update_database_configuration_response_model == update_database_configuration_response_model2

        # Convert model instance back to dict and verify no loss of data
        update_database_configuration_response_model_json2 = update_database_configuration_response_model.to_dict()
        assert update_database_configuration_response_model_json2 == update_database_configuration_response_model_json

class TestAutoscalingSetGroupAutoscalingAutoscalingCPUGroup():
    """
    Test Class for AutoscalingSetGroupAutoscalingAutoscalingCPUGroup
    """

    def test_autoscaling_set_group_autoscaling_autoscaling_cpu_group_serialization(self):
        """
        Test serialization/deserialization for AutoscalingSetGroupAutoscalingAutoscalingCPUGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_cpu_group_cpu_rate_model = {} # AutoscalingCPUGroupCPURate
        autoscaling_cpu_group_cpu_rate_model['increase_percent'] = 10
        autoscaling_cpu_group_cpu_rate_model['period_seconds'] = 900
        autoscaling_cpu_group_cpu_rate_model['limit_count_per_member'] = 10
        autoscaling_cpu_group_cpu_rate_model['units'] = 'count'

        autoscaling_cpu_group_cpu_model = {} # AutoscalingCPUGroupCPU
        autoscaling_cpu_group_cpu_model['scalers'] = { 'foo': 'bar' }
        autoscaling_cpu_group_cpu_model['rate'] = autoscaling_cpu_group_cpu_rate_model

        # Construct a json representation of a AutoscalingSetGroupAutoscalingAutoscalingCPUGroup model
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json = {}
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json['cpu'] = autoscaling_cpu_group_cpu_model

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingCPUGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model = AutoscalingSetGroupAutoscalingAutoscalingCPUGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json)
        assert autoscaling_set_group_autoscaling_autoscaling_cpu_group_model != False

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingCPUGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_dict = AutoscalingSetGroupAutoscalingAutoscalingCPUGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json).__dict__
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model2 = AutoscalingSetGroupAutoscalingAutoscalingCPUGroup(**autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_set_group_autoscaling_autoscaling_cpu_group_model == autoscaling_set_group_autoscaling_autoscaling_cpu_group_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json2 = autoscaling_set_group_autoscaling_autoscaling_cpu_group_model.to_dict()
        assert autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json2 == autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json

class TestAutoscalingSetGroupAutoscalingAutoscalingDiskGroup():
    """
    Test Class for AutoscalingSetGroupAutoscalingAutoscalingDiskGroup
    """

    def test_autoscaling_set_group_autoscaling_autoscaling_disk_group_serialization(self):
        """
        Test serialization/deserialization for AutoscalingSetGroupAutoscalingAutoscalingDiskGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_disk_group_disk_scalers_capacity_model = {} # AutoscalingDiskGroupDiskScalersCapacity
        autoscaling_disk_group_disk_scalers_capacity_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model['free_space_less_than_percent'] = 10

        autoscaling_disk_group_disk_scalers_io_utilization_model = {} # AutoscalingDiskGroupDiskScalersIoUtilization
        autoscaling_disk_group_disk_scalers_io_utilization_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_disk_group_disk_scalers_model = {} # AutoscalingDiskGroupDiskScalers
        autoscaling_disk_group_disk_scalers_model['capacity'] = autoscaling_disk_group_disk_scalers_capacity_model
        autoscaling_disk_group_disk_scalers_model['io_utilization'] = autoscaling_disk_group_disk_scalers_io_utilization_model

        autoscaling_disk_group_disk_rate_model = {} # AutoscalingDiskGroupDiskRate
        autoscaling_disk_group_disk_rate_model['increase_percent'] = 20
        autoscaling_disk_group_disk_rate_model['period_seconds'] = 900
        autoscaling_disk_group_disk_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_disk_group_disk_rate_model['units'] = 'mb'

        autoscaling_disk_group_disk_model = {} # AutoscalingDiskGroupDisk
        autoscaling_disk_group_disk_model['scalers'] = autoscaling_disk_group_disk_scalers_model
        autoscaling_disk_group_disk_model['rate'] = autoscaling_disk_group_disk_rate_model

        # Construct a json representation of a AutoscalingSetGroupAutoscalingAutoscalingDiskGroup model
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json = {}
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json['disk'] = autoscaling_disk_group_disk_model

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingDiskGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model = AutoscalingSetGroupAutoscalingAutoscalingDiskGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json)
        assert autoscaling_set_group_autoscaling_autoscaling_disk_group_model != False

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingDiskGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model_dict = AutoscalingSetGroupAutoscalingAutoscalingDiskGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json).__dict__
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model2 = AutoscalingSetGroupAutoscalingAutoscalingDiskGroup(**autoscaling_set_group_autoscaling_autoscaling_disk_group_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_set_group_autoscaling_autoscaling_disk_group_model == autoscaling_set_group_autoscaling_autoscaling_disk_group_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json2 = autoscaling_set_group_autoscaling_autoscaling_disk_group_model.to_dict()
        assert autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json2 == autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json

class TestAutoscalingSetGroupAutoscalingAutoscalingMemoryGroup():
    """
    Test Class for AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup
    """

    def test_autoscaling_set_group_autoscaling_autoscaling_memory_group_serialization(self):
        """
        Test serialization/deserialization for AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_memory_group_memory_scalers_io_utilization_model = {} # AutoscalingMemoryGroupMemoryScalersIoUtilization
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_memory_group_memory_scalers_model = {} # AutoscalingMemoryGroupMemoryScalers
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        autoscaling_memory_group_memory_rate_model = {} # AutoscalingMemoryGroupMemoryRate
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 900
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        autoscaling_memory_group_memory_model = {} # AutoscalingMemoryGroupMemory
        autoscaling_memory_group_memory_model['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model['rate'] = autoscaling_memory_group_memory_rate_model

        # Construct a json representation of a AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup model
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json = {}
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json['memory'] = autoscaling_memory_group_memory_model

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model = AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json)
        assert autoscaling_set_group_autoscaling_autoscaling_memory_group_model != False

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model_dict = AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json).__dict__
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model2 = AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup(**autoscaling_set_group_autoscaling_autoscaling_memory_group_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_set_group_autoscaling_autoscaling_memory_group_model == autoscaling_set_group_autoscaling_autoscaling_memory_group_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json2 = autoscaling_set_group_autoscaling_autoscaling_memory_group_model.to_dict()
        assert autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json2 == autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json

class TestConnectionConnectionElasticsearchConnection():
    """
    Test Class for ConnectionConnectionElasticsearchConnection
    """

    def test_connection_connection_elasticsearch_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionConnectionElasticsearchConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        elasticsearch_connection_https_hosts_item_model = {} # ElasticsearchConnectionHTTPSHostsItem
        elasticsearch_connection_https_hosts_item_model['hostname'] = 'testString'
        elasticsearch_connection_https_hosts_item_model['port'] = 38

        elasticsearch_connection_https_authentication_model = {} # ElasticsearchConnectionHTTPSAuthentication
        elasticsearch_connection_https_authentication_model['method'] = 'testString'
        elasticsearch_connection_https_authentication_model['username'] = 'testString'
        elasticsearch_connection_https_authentication_model['password'] = 'testString'

        elasticsearch_connection_https_certificate_model = {} # ElasticsearchConnectionHTTPSCertificate
        elasticsearch_connection_https_certificate_model['name'] = 'testString'
        elasticsearch_connection_https_certificate_model['certificate_base64'] = 'testString'

        elasticsearch_connection_https_model = {} # ElasticsearchConnectionHTTPS
        elasticsearch_connection_https_model['type'] = 'uri'
        elasticsearch_connection_https_model['composed'] = ['testString']
        elasticsearch_connection_https_model['scheme'] = 'testString'
        elasticsearch_connection_https_model['hosts'] = [elasticsearch_connection_https_hosts_item_model]
        elasticsearch_connection_https_model['path'] = 'testString'
        elasticsearch_connection_https_model['query_options'] = { 'foo': 'bar' }
        elasticsearch_connection_https_model['authentication'] = elasticsearch_connection_https_authentication_model
        elasticsearch_connection_https_model['certificate'] = elasticsearch_connection_https_certificate_model

        connection_cli_certificate_model = {} # ConnectionCLICertificate
        connection_cli_certificate_model['name'] = 'testString'
        connection_cli_certificate_model['certificate_base64'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_cli_certificate_model

        # Construct a json representation of a ConnectionConnectionElasticsearchConnection model
        connection_connection_elasticsearch_connection_model_json = {}
        connection_connection_elasticsearch_connection_model_json['https'] = elasticsearch_connection_https_model
        connection_connection_elasticsearch_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionConnectionElasticsearchConnection by calling from_dict on the json representation
        connection_connection_elasticsearch_connection_model = ConnectionConnectionElasticsearchConnection.from_dict(connection_connection_elasticsearch_connection_model_json)
        assert connection_connection_elasticsearch_connection_model != False

        # Construct a model instance of ConnectionConnectionElasticsearchConnection by calling from_dict on the json representation
        connection_connection_elasticsearch_connection_model_dict = ConnectionConnectionElasticsearchConnection.from_dict(connection_connection_elasticsearch_connection_model_json).__dict__
        connection_connection_elasticsearch_connection_model2 = ConnectionConnectionElasticsearchConnection(**connection_connection_elasticsearch_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_connection_elasticsearch_connection_model == connection_connection_elasticsearch_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_connection_elasticsearch_connection_model_json2 = connection_connection_elasticsearch_connection_model.to_dict()
        assert connection_connection_elasticsearch_connection_model_json2 == connection_connection_elasticsearch_connection_model_json

class TestConnectionConnectionEtcdConnection():
    """
    Test Class for ConnectionConnectionEtcdConnection
    """

    def test_connection_connection_etcd_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionConnectionEtcdConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        grpc_connection_uri_hosts_item_model = {} # GRPCConnectionURIHostsItem
        grpc_connection_uri_hosts_item_model['hostname'] = 'testString'
        grpc_connection_uri_hosts_item_model['port'] = 38

        grpc_connection_uri_authentication_model = {} # GRPCConnectionURIAuthentication
        grpc_connection_uri_authentication_model['method'] = 'testString'
        grpc_connection_uri_authentication_model['username'] = 'testString'
        grpc_connection_uri_authentication_model['password'] = 'testString'

        grpc_connection_uri_certificate_model = {} # GRPCConnectionURICertificate
        grpc_connection_uri_certificate_model['name'] = 'testString'
        grpc_connection_uri_certificate_model['certificate_base64'] = 'testString'

        grpc_connection_uri_model = {} # GRPCConnectionURI
        grpc_connection_uri_model['type'] = 'uri'
        grpc_connection_uri_model['composed'] = ['testString']
        grpc_connection_uri_model['scheme'] = 'testString'
        grpc_connection_uri_model['hosts'] = [grpc_connection_uri_hosts_item_model]
        grpc_connection_uri_model['path'] = 'testString'
        grpc_connection_uri_model['query_options'] = { 'foo': 'bar' }
        grpc_connection_uri_model['authentication'] = grpc_connection_uri_authentication_model
        grpc_connection_uri_model['certificate'] = grpc_connection_uri_certificate_model

        connection_cli_certificate_model = {} # ConnectionCLICertificate
        connection_cli_certificate_model['name'] = 'testString'
        connection_cli_certificate_model['certificate_base64'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_cli_certificate_model

        # Construct a json representation of a ConnectionConnectionEtcdConnection model
        connection_connection_etcd_connection_model_json = {}
        connection_connection_etcd_connection_model_json['grpc'] = grpc_connection_uri_model
        connection_connection_etcd_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionConnectionEtcdConnection by calling from_dict on the json representation
        connection_connection_etcd_connection_model = ConnectionConnectionEtcdConnection.from_dict(connection_connection_etcd_connection_model_json)
        assert connection_connection_etcd_connection_model != False

        # Construct a model instance of ConnectionConnectionEtcdConnection by calling from_dict on the json representation
        connection_connection_etcd_connection_model_dict = ConnectionConnectionEtcdConnection.from_dict(connection_connection_etcd_connection_model_json).__dict__
        connection_connection_etcd_connection_model2 = ConnectionConnectionEtcdConnection(**connection_connection_etcd_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_connection_etcd_connection_model == connection_connection_etcd_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_connection_etcd_connection_model_json2 = connection_connection_etcd_connection_model.to_dict()
        assert connection_connection_etcd_connection_model_json2 == connection_connection_etcd_connection_model_json

class TestConnectionConnectionMongoDBConnection():
    """
    Test Class for ConnectionConnectionMongoDBConnection
    """

    def test_connection_connection_mongo_db_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionConnectionMongoDBConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        mongo_db_connection_uri_hosts_item_model = {} # MongoDBConnectionURIHostsItem
        mongo_db_connection_uri_hosts_item_model['hostname'] = 'testString'
        mongo_db_connection_uri_hosts_item_model['port'] = 38

        mongo_db_connection_uri_authentication_model = {} # MongoDBConnectionURIAuthentication
        mongo_db_connection_uri_authentication_model['method'] = 'testString'
        mongo_db_connection_uri_authentication_model['username'] = 'testString'
        mongo_db_connection_uri_authentication_model['password'] = 'testString'

        mongo_db_connection_uri_certificate_model = {} # MongoDBConnectionURICertificate
        mongo_db_connection_uri_certificate_model['name'] = 'testString'
        mongo_db_connection_uri_certificate_model['certificate_base64'] = 'testString'

        mongo_db_connection_uri_model = {} # MongoDBConnectionURI
        mongo_db_connection_uri_model['type'] = 'uri'
        mongo_db_connection_uri_model['composed'] = ['testString']
        mongo_db_connection_uri_model['scheme'] = 'testString'
        mongo_db_connection_uri_model['hosts'] = [mongo_db_connection_uri_hosts_item_model]
        mongo_db_connection_uri_model['path'] = 'testString'
        mongo_db_connection_uri_model['query_options'] = { 'foo': 'bar' }
        mongo_db_connection_uri_model['authentication'] = mongo_db_connection_uri_authentication_model
        mongo_db_connection_uri_model['certificate'] = mongo_db_connection_uri_certificate_model
        mongo_db_connection_uri_model['database'] = 'testString'
        mongo_db_connection_uri_model['replica_set'] = 'testString'

        connection_cli_certificate_model = {} # ConnectionCLICertificate
        connection_cli_certificate_model['name'] = 'testString'
        connection_cli_certificate_model['certificate_base64'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_cli_certificate_model

        # Construct a json representation of a ConnectionConnectionMongoDBConnection model
        connection_connection_mongo_db_connection_model_json = {}
        connection_connection_mongo_db_connection_model_json['mongodb'] = mongo_db_connection_uri_model
        connection_connection_mongo_db_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionConnectionMongoDBConnection by calling from_dict on the json representation
        connection_connection_mongo_db_connection_model = ConnectionConnectionMongoDBConnection.from_dict(connection_connection_mongo_db_connection_model_json)
        assert connection_connection_mongo_db_connection_model != False

        # Construct a model instance of ConnectionConnectionMongoDBConnection by calling from_dict on the json representation
        connection_connection_mongo_db_connection_model_dict = ConnectionConnectionMongoDBConnection.from_dict(connection_connection_mongo_db_connection_model_json).__dict__
        connection_connection_mongo_db_connection_model2 = ConnectionConnectionMongoDBConnection(**connection_connection_mongo_db_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_connection_mongo_db_connection_model == connection_connection_mongo_db_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_connection_mongo_db_connection_model_json2 = connection_connection_mongo_db_connection_model.to_dict()
        assert connection_connection_mongo_db_connection_model_json2 == connection_connection_mongo_db_connection_model_json

class TestConnectionConnectionPostgreSQLConnection():
    """
    Test Class for ConnectionConnectionPostgreSQLConnection
    """

    def test_connection_connection_postgre_sql_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionConnectionPostgreSQLConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        postgre_sql_connection_uri_hosts_item_model = {} # PostgreSQLConnectionURIHostsItem
        postgre_sql_connection_uri_hosts_item_model['hostname'] = 'testString'
        postgre_sql_connection_uri_hosts_item_model['port'] = 38

        postgre_sql_connection_uri_authentication_model = {} # PostgreSQLConnectionURIAuthentication
        postgre_sql_connection_uri_authentication_model['method'] = 'testString'
        postgre_sql_connection_uri_authentication_model['username'] = 'testString'
        postgre_sql_connection_uri_authentication_model['password'] = 'testString'

        postgre_sql_connection_uri_certificate_model = {} # PostgreSQLConnectionURICertificate
        postgre_sql_connection_uri_certificate_model['name'] = 'testString'
        postgre_sql_connection_uri_certificate_model['certificate_base64'] = 'testString'

        postgre_sql_connection_uri_model = {} # PostgreSQLConnectionURI
        postgre_sql_connection_uri_model['type'] = 'uri'
        postgre_sql_connection_uri_model['composed'] = ['testString']
        postgre_sql_connection_uri_model['scheme'] = 'testString'
        postgre_sql_connection_uri_model['hosts'] = [postgre_sql_connection_uri_hosts_item_model]
        postgre_sql_connection_uri_model['path'] = '/ibmclouddb'
        postgre_sql_connection_uri_model['query_options'] = { 'foo': 'bar' }
        postgre_sql_connection_uri_model['authentication'] = postgre_sql_connection_uri_authentication_model
        postgre_sql_connection_uri_model['certificate'] = postgre_sql_connection_uri_certificate_model
        postgre_sql_connection_uri_model['database'] = 'testString'

        connection_cli_certificate_model = {} # ConnectionCLICertificate
        connection_cli_certificate_model['name'] = 'testString'
        connection_cli_certificate_model['certificate_base64'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_cli_certificate_model

        # Construct a json representation of a ConnectionConnectionPostgreSQLConnection model
        connection_connection_postgre_sql_connection_model_json = {}
        connection_connection_postgre_sql_connection_model_json['postgres'] = postgre_sql_connection_uri_model
        connection_connection_postgre_sql_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionConnectionPostgreSQLConnection by calling from_dict on the json representation
        connection_connection_postgre_sql_connection_model = ConnectionConnectionPostgreSQLConnection.from_dict(connection_connection_postgre_sql_connection_model_json)
        assert connection_connection_postgre_sql_connection_model != False

        # Construct a model instance of ConnectionConnectionPostgreSQLConnection by calling from_dict on the json representation
        connection_connection_postgre_sql_connection_model_dict = ConnectionConnectionPostgreSQLConnection.from_dict(connection_connection_postgre_sql_connection_model_json).__dict__
        connection_connection_postgre_sql_connection_model2 = ConnectionConnectionPostgreSQLConnection(**connection_connection_postgre_sql_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_connection_postgre_sql_connection_model == connection_connection_postgre_sql_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_connection_postgre_sql_connection_model_json2 = connection_connection_postgre_sql_connection_model.to_dict()
        assert connection_connection_postgre_sql_connection_model_json2 == connection_connection_postgre_sql_connection_model_json

class TestConnectionConnectionRabbitMQConnection():
    """
    Test Class for ConnectionConnectionRabbitMQConnection
    """

    def test_connection_connection_rabbit_mq_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionConnectionRabbitMQConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rabbit_mq_connection_amqps_hosts_item_model = {} # RabbitMQConnectionAMQPSHostsItem
        rabbit_mq_connection_amqps_hosts_item_model['hostname'] = 'testString'
        rabbit_mq_connection_amqps_hosts_item_model['port'] = 38

        rabbit_mq_connection_amqps_authentication_model = {} # RabbitMQConnectionAMQPSAuthentication
        rabbit_mq_connection_amqps_authentication_model['method'] = 'testString'
        rabbit_mq_connection_amqps_authentication_model['username'] = 'testString'
        rabbit_mq_connection_amqps_authentication_model['password'] = 'testString'

        rabbit_mq_connection_amqps_certificate_model = {} # RabbitMQConnectionAMQPSCertificate
        rabbit_mq_connection_amqps_certificate_model['name'] = 'testString'
        rabbit_mq_connection_amqps_certificate_model['certificate_base64'] = 'testString'

        rabbit_mq_connection_amqps_model = {} # RabbitMQConnectionAMQPS
        rabbit_mq_connection_amqps_model['type'] = 'uri'
        rabbit_mq_connection_amqps_model['composed'] = ['testString']
        rabbit_mq_connection_amqps_model['scheme'] = 'testString'
        rabbit_mq_connection_amqps_model['hosts'] = [rabbit_mq_connection_amqps_hosts_item_model]
        rabbit_mq_connection_amqps_model['path'] = 'testString'
        rabbit_mq_connection_amqps_model['query_options'] = { 'foo': 'bar' }
        rabbit_mq_connection_amqps_model['authentication'] = rabbit_mq_connection_amqps_authentication_model
        rabbit_mq_connection_amqps_model['certificate'] = rabbit_mq_connection_amqps_certificate_model

        rabbit_mq_connection_mqtts_hosts_item_model = {} # RabbitMQConnectionMQTTSHostsItem
        rabbit_mq_connection_mqtts_hosts_item_model['hostname'] = 'testString'
        rabbit_mq_connection_mqtts_hosts_item_model['port'] = 38

        rabbit_mq_connection_mqtts_authentication_model = {} # RabbitMQConnectionMQTTSAuthentication
        rabbit_mq_connection_mqtts_authentication_model['method'] = 'testString'
        rabbit_mq_connection_mqtts_authentication_model['username'] = 'testString'
        rabbit_mq_connection_mqtts_authentication_model['password'] = 'testString'

        rabbit_mq_connection_mqtts_certificate_model = {} # RabbitMQConnectionMQTTSCertificate
        rabbit_mq_connection_mqtts_certificate_model['name'] = 'testString'
        rabbit_mq_connection_mqtts_certificate_model['certificate_base64'] = 'testString'

        rabbit_mq_connection_mqtts_model = {} # RabbitMQConnectionMQTTS
        rabbit_mq_connection_mqtts_model['type'] = 'uri'
        rabbit_mq_connection_mqtts_model['composed'] = ['testString']
        rabbit_mq_connection_mqtts_model['scheme'] = 'testString'
        rabbit_mq_connection_mqtts_model['hosts'] = [rabbit_mq_connection_mqtts_hosts_item_model]
        rabbit_mq_connection_mqtts_model['path'] = 'testString'
        rabbit_mq_connection_mqtts_model['query_options'] = { 'foo': 'bar' }
        rabbit_mq_connection_mqtts_model['authentication'] = rabbit_mq_connection_mqtts_authentication_model
        rabbit_mq_connection_mqtts_model['certificate'] = rabbit_mq_connection_mqtts_certificate_model

        rabbit_mq_connection_stomp_ssl_hosts_item_model = {} # RabbitMQConnectionStompSSLHostsItem
        rabbit_mq_connection_stomp_ssl_hosts_item_model['hostname'] = 'testString'
        rabbit_mq_connection_stomp_ssl_hosts_item_model['port'] = 38

        rabbit_mq_connection_stomp_ssl_authentication_model = {} # RabbitMQConnectionStompSSLAuthentication
        rabbit_mq_connection_stomp_ssl_authentication_model['method'] = 'testString'
        rabbit_mq_connection_stomp_ssl_authentication_model['username'] = 'testString'
        rabbit_mq_connection_stomp_ssl_authentication_model['password'] = 'testString'

        rabbit_mq_connection_stomp_ssl_certificate_model = {} # RabbitMQConnectionStompSSLCertificate
        rabbit_mq_connection_stomp_ssl_certificate_model['name'] = 'testString'
        rabbit_mq_connection_stomp_ssl_certificate_model['certificate_base64'] = 'testString'

        rabbit_mq_connection_stomp_ssl_model = {} # RabbitMQConnectionStompSSL
        rabbit_mq_connection_stomp_ssl_model['type'] = 'testString'
        rabbit_mq_connection_stomp_ssl_model['composed'] = ['testString']
        rabbit_mq_connection_stomp_ssl_model['hosts'] = [rabbit_mq_connection_stomp_ssl_hosts_item_model]
        rabbit_mq_connection_stomp_ssl_model['authentication'] = rabbit_mq_connection_stomp_ssl_authentication_model
        rabbit_mq_connection_stomp_ssl_model['certificate'] = rabbit_mq_connection_stomp_ssl_certificate_model
        rabbit_mq_connection_stomp_ssl_model['ssl'] = True

        rabbit_mq_connection_https_hosts_item_model = {} # RabbitMQConnectionHTTPSHostsItem
        rabbit_mq_connection_https_hosts_item_model['hostname'] = 'testString'
        rabbit_mq_connection_https_hosts_item_model['port'] = 38

        rabbit_mq_connection_https_authentication_model = {} # RabbitMQConnectionHTTPSAuthentication
        rabbit_mq_connection_https_authentication_model['method'] = 'testString'
        rabbit_mq_connection_https_authentication_model['username'] = 'testString'
        rabbit_mq_connection_https_authentication_model['password'] = 'testString'

        rabbit_mq_connection_https_certificate_model = {} # RabbitMQConnectionHTTPSCertificate
        rabbit_mq_connection_https_certificate_model['name'] = 'testString'
        rabbit_mq_connection_https_certificate_model['certificate_base64'] = 'testString'

        rabbit_mq_connection_https_model = {} # RabbitMQConnectionHTTPS
        rabbit_mq_connection_https_model['type'] = 'uri'
        rabbit_mq_connection_https_model['composed'] = ['testString']
        rabbit_mq_connection_https_model['scheme'] = 'testString'
        rabbit_mq_connection_https_model['hosts'] = [rabbit_mq_connection_https_hosts_item_model]
        rabbit_mq_connection_https_model['path'] = 'testString'
        rabbit_mq_connection_https_model['query_options'] = { 'foo': 'bar' }
        rabbit_mq_connection_https_model['authentication'] = rabbit_mq_connection_https_authentication_model
        rabbit_mq_connection_https_model['certificate'] = rabbit_mq_connection_https_certificate_model
        rabbit_mq_connection_https_model['browser_accessible'] = True

        connection_cli_certificate_model = {} # ConnectionCLICertificate
        connection_cli_certificate_model['name'] = 'testString'
        connection_cli_certificate_model['certificate_base64'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_cli_certificate_model

        # Construct a json representation of a ConnectionConnectionRabbitMQConnection model
        connection_connection_rabbit_mq_connection_model_json = {}
        connection_connection_rabbit_mq_connection_model_json['amqps'] = rabbit_mq_connection_amqps_model
        connection_connection_rabbit_mq_connection_model_json['mqtts'] = rabbit_mq_connection_mqtts_model
        connection_connection_rabbit_mq_connection_model_json['stomp_ssl'] = rabbit_mq_connection_stomp_ssl_model
        connection_connection_rabbit_mq_connection_model_json['https'] = rabbit_mq_connection_https_model
        connection_connection_rabbit_mq_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionConnectionRabbitMQConnection by calling from_dict on the json representation
        connection_connection_rabbit_mq_connection_model = ConnectionConnectionRabbitMQConnection.from_dict(connection_connection_rabbit_mq_connection_model_json)
        assert connection_connection_rabbit_mq_connection_model != False

        # Construct a model instance of ConnectionConnectionRabbitMQConnection by calling from_dict on the json representation
        connection_connection_rabbit_mq_connection_model_dict = ConnectionConnectionRabbitMQConnection.from_dict(connection_connection_rabbit_mq_connection_model_json).__dict__
        connection_connection_rabbit_mq_connection_model2 = ConnectionConnectionRabbitMQConnection(**connection_connection_rabbit_mq_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_connection_rabbit_mq_connection_model == connection_connection_rabbit_mq_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_connection_rabbit_mq_connection_model_json2 = connection_connection_rabbit_mq_connection_model.to_dict()
        assert connection_connection_rabbit_mq_connection_model_json2 == connection_connection_rabbit_mq_connection_model_json

class TestConnectionConnectionRedisConnection():
    """
    Test Class for ConnectionConnectionRedisConnection
    """

    def test_connection_connection_redis_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionConnectionRedisConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        redis_connection_uri_hosts_item_model = {} # RedisConnectionURIHostsItem
        redis_connection_uri_hosts_item_model['hostname'] = 'testString'
        redis_connection_uri_hosts_item_model['port'] = 38

        redis_connection_uri_authentication_model = {} # RedisConnectionURIAuthentication
        redis_connection_uri_authentication_model['method'] = 'testString'
        redis_connection_uri_authentication_model['username'] = 'testString'
        redis_connection_uri_authentication_model['password'] = 'testString'

        redis_connection_uri_certificate_model = {} # RedisConnectionURICertificate
        redis_connection_uri_certificate_model['name'] = 'testString'
        redis_connection_uri_certificate_model['certificate_base64'] = 'testString'

        redis_connection_uri_model = {} # RedisConnectionURI
        redis_connection_uri_model['type'] = 'uri'
        redis_connection_uri_model['composed'] = ['testString']
        redis_connection_uri_model['scheme'] = 'testString'
        redis_connection_uri_model['hosts'] = [redis_connection_uri_hosts_item_model]
        redis_connection_uri_model['path'] = '/0'
        redis_connection_uri_model['query_options'] = { 'foo': 'bar' }
        redis_connection_uri_model['authentication'] = redis_connection_uri_authentication_model
        redis_connection_uri_model['certificate'] = redis_connection_uri_certificate_model
        redis_connection_uri_model['database'] = 38

        connection_cli_certificate_model = {} # ConnectionCLICertificate
        connection_cli_certificate_model['name'] = 'testString'
        connection_cli_certificate_model['certificate_base64'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_cli_certificate_model

        # Construct a json representation of a ConnectionConnectionRedisConnection model
        connection_connection_redis_connection_model_json = {}
        connection_connection_redis_connection_model_json['rediss'] = redis_connection_uri_model
        connection_connection_redis_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionConnectionRedisConnection by calling from_dict on the json representation
        connection_connection_redis_connection_model = ConnectionConnectionRedisConnection.from_dict(connection_connection_redis_connection_model_json)
        assert connection_connection_redis_connection_model != False

        # Construct a model instance of ConnectionConnectionRedisConnection by calling from_dict on the json representation
        connection_connection_redis_connection_model_dict = ConnectionConnectionRedisConnection.from_dict(connection_connection_redis_connection_model_json).__dict__
        connection_connection_redis_connection_model2 = ConnectionConnectionRedisConnection(**connection_connection_redis_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_connection_redis_connection_model == connection_connection_redis_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_connection_redis_connection_model_json2 = connection_connection_redis_connection_model.to_dict()
        assert connection_connection_redis_connection_model_json2 == connection_connection_redis_connection_model_json

class TestSetConfigurationConfigurationPGConfiguration():
    """
    Test Class for SetConfigurationConfigurationPGConfiguration
    """

    def test_set_configuration_configuration_pg_configuration_serialization(self):
        """
        Test serialization/deserialization for SetConfigurationConfigurationPGConfiguration
        """

        # Construct a json representation of a SetConfigurationConfigurationPGConfiguration model
        set_configuration_configuration_pg_configuration_model_json = {}
        set_configuration_configuration_pg_configuration_model_json['max_connections'] = 115
        set_configuration_configuration_pg_configuration_model_json['max_prepared_transactions'] = 0
        set_configuration_configuration_pg_configuration_model_json['deadlock_timeout'] = 100
        set_configuration_configuration_pg_configuration_model_json['effective_io_concurrency'] = 1
        set_configuration_configuration_pg_configuration_model_json['max_replication_slots'] = 10
        set_configuration_configuration_pg_configuration_model_json['max_wal_senders'] = 12
        set_configuration_configuration_pg_configuration_model_json['shared_buffers'] = 16
        set_configuration_configuration_pg_configuration_model_json['synchronous_commit'] = 'local'
        set_configuration_configuration_pg_configuration_model_json['wal_level'] = 'hot_standby'
        set_configuration_configuration_pg_configuration_model_json['archive_timeout'] = 300
        set_configuration_configuration_pg_configuration_model_json['log_min_duration_statement'] = 100

        # Construct a model instance of SetConfigurationConfigurationPGConfiguration by calling from_dict on the json representation
        set_configuration_configuration_pg_configuration_model = SetConfigurationConfigurationPGConfiguration.from_dict(set_configuration_configuration_pg_configuration_model_json)
        assert set_configuration_configuration_pg_configuration_model != False

        # Construct a model instance of SetConfigurationConfigurationPGConfiguration by calling from_dict on the json representation
        set_configuration_configuration_pg_configuration_model_dict = SetConfigurationConfigurationPGConfiguration.from_dict(set_configuration_configuration_pg_configuration_model_json).__dict__
        set_configuration_configuration_pg_configuration_model2 = SetConfigurationConfigurationPGConfiguration(**set_configuration_configuration_pg_configuration_model_dict)

        # Verify the model instances are equivalent
        assert set_configuration_configuration_pg_configuration_model == set_configuration_configuration_pg_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        set_configuration_configuration_pg_configuration_model_json2 = set_configuration_configuration_pg_configuration_model.to_dict()
        assert set_configuration_configuration_pg_configuration_model_json2 == set_configuration_configuration_pg_configuration_model_json

class TestSetConfigurationConfigurationRedisConfiguration():
    """
    Test Class for SetConfigurationConfigurationRedisConfiguration
    """

    def test_set_configuration_configuration_redis_configuration_serialization(self):
        """
        Test serialization/deserialization for SetConfigurationConfigurationRedisConfiguration
        """

        # Construct a json representation of a SetConfigurationConfigurationRedisConfiguration model
        set_configuration_configuration_redis_configuration_model_json = {}
        set_configuration_configuration_redis_configuration_model_json['maxmemory-redis'] = 0
        set_configuration_configuration_redis_configuration_model_json['maxmemory-policy'] = 'volatile-lru'
        set_configuration_configuration_redis_configuration_model_json['appendonly'] = 'yes'
        set_configuration_configuration_redis_configuration_model_json['maxmemory-samples'] = 0
        set_configuration_configuration_redis_configuration_model_json['stop-writes-on-bgsave-error'] = 'yes'

        # Construct a model instance of SetConfigurationConfigurationRedisConfiguration by calling from_dict on the json representation
        set_configuration_configuration_redis_configuration_model = SetConfigurationConfigurationRedisConfiguration.from_dict(set_configuration_configuration_redis_configuration_model_json)
        assert set_configuration_configuration_redis_configuration_model != False

        # Construct a model instance of SetConfigurationConfigurationRedisConfiguration by calling from_dict on the json representation
        set_configuration_configuration_redis_configuration_model_dict = SetConfigurationConfigurationRedisConfiguration.from_dict(set_configuration_configuration_redis_configuration_model_json).__dict__
        set_configuration_configuration_redis_configuration_model2 = SetConfigurationConfigurationRedisConfiguration(**set_configuration_configuration_redis_configuration_model_dict)

        # Verify the model instances are equivalent
        assert set_configuration_configuration_redis_configuration_model == set_configuration_configuration_redis_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        set_configuration_configuration_redis_configuration_model_json2 = set_configuration_configuration_redis_configuration_model.to_dict()
        assert set_configuration_configuration_redis_configuration_model_json2 == set_configuration_configuration_redis_configuration_model_json

class TestSetDeploymentScalingGroupRequestSetCPUGroup():
    """
    Test Class for SetDeploymentScalingGroupRequestSetCPUGroup
    """

    def test_set_deployment_scaling_group_request_set_cpu_group_serialization(self):
        """
        Test serialization/deserialization for SetDeploymentScalingGroupRequestSetCPUGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        set_cpu_group_cpu_model = {} # SetCPUGroupCPU
        set_cpu_group_cpu_model['allocation_count'] = 2

        # Construct a json representation of a SetDeploymentScalingGroupRequestSetCPUGroup model
        set_deployment_scaling_group_request_set_cpu_group_model_json = {}
        set_deployment_scaling_group_request_set_cpu_group_model_json['cpu'] = set_cpu_group_cpu_model

        # Construct a model instance of SetDeploymentScalingGroupRequestSetCPUGroup by calling from_dict on the json representation
        set_deployment_scaling_group_request_set_cpu_group_model = SetDeploymentScalingGroupRequestSetCPUGroup.from_dict(set_deployment_scaling_group_request_set_cpu_group_model_json)
        assert set_deployment_scaling_group_request_set_cpu_group_model != False

        # Construct a model instance of SetDeploymentScalingGroupRequestSetCPUGroup by calling from_dict on the json representation
        set_deployment_scaling_group_request_set_cpu_group_model_dict = SetDeploymentScalingGroupRequestSetCPUGroup.from_dict(set_deployment_scaling_group_request_set_cpu_group_model_json).__dict__
        set_deployment_scaling_group_request_set_cpu_group_model2 = SetDeploymentScalingGroupRequestSetCPUGroup(**set_deployment_scaling_group_request_set_cpu_group_model_dict)

        # Verify the model instances are equivalent
        assert set_deployment_scaling_group_request_set_cpu_group_model == set_deployment_scaling_group_request_set_cpu_group_model2

        # Convert model instance back to dict and verify no loss of data
        set_deployment_scaling_group_request_set_cpu_group_model_json2 = set_deployment_scaling_group_request_set_cpu_group_model.to_dict()
        assert set_deployment_scaling_group_request_set_cpu_group_model_json2 == set_deployment_scaling_group_request_set_cpu_group_model_json

class TestSetDeploymentScalingGroupRequestSetDiskGroup():
    """
    Test Class for SetDeploymentScalingGroupRequestSetDiskGroup
    """

    def test_set_deployment_scaling_group_request_set_disk_group_serialization(self):
        """
        Test serialization/deserialization for SetDeploymentScalingGroupRequestSetDiskGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        set_disk_group_disk_model = {} # SetDiskGroupDisk
        set_disk_group_disk_model['allocation_mb'] = 20480

        # Construct a json representation of a SetDeploymentScalingGroupRequestSetDiskGroup model
        set_deployment_scaling_group_request_set_disk_group_model_json = {}
        set_deployment_scaling_group_request_set_disk_group_model_json['disk'] = set_disk_group_disk_model

        # Construct a model instance of SetDeploymentScalingGroupRequestSetDiskGroup by calling from_dict on the json representation
        set_deployment_scaling_group_request_set_disk_group_model = SetDeploymentScalingGroupRequestSetDiskGroup.from_dict(set_deployment_scaling_group_request_set_disk_group_model_json)
        assert set_deployment_scaling_group_request_set_disk_group_model != False

        # Construct a model instance of SetDeploymentScalingGroupRequestSetDiskGroup by calling from_dict on the json representation
        set_deployment_scaling_group_request_set_disk_group_model_dict = SetDeploymentScalingGroupRequestSetDiskGroup.from_dict(set_deployment_scaling_group_request_set_disk_group_model_json).__dict__
        set_deployment_scaling_group_request_set_disk_group_model2 = SetDeploymentScalingGroupRequestSetDiskGroup(**set_deployment_scaling_group_request_set_disk_group_model_dict)

        # Verify the model instances are equivalent
        assert set_deployment_scaling_group_request_set_disk_group_model == set_deployment_scaling_group_request_set_disk_group_model2

        # Convert model instance back to dict and verify no loss of data
        set_deployment_scaling_group_request_set_disk_group_model_json2 = set_deployment_scaling_group_request_set_disk_group_model.to_dict()
        assert set_deployment_scaling_group_request_set_disk_group_model_json2 == set_deployment_scaling_group_request_set_disk_group_model_json

class TestSetDeploymentScalingGroupRequestSetMembersGroup():
    """
    Test Class for SetDeploymentScalingGroupRequestSetMembersGroup
    """

    def test_set_deployment_scaling_group_request_set_members_group_serialization(self):
        """
        Test serialization/deserialization for SetDeploymentScalingGroupRequestSetMembersGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        set_members_group_members_model = {} # SetMembersGroupMembers
        set_members_group_members_model['allocation_count'] = 4

        # Construct a json representation of a SetDeploymentScalingGroupRequestSetMembersGroup model
        set_deployment_scaling_group_request_set_members_group_model_json = {}
        set_deployment_scaling_group_request_set_members_group_model_json['members'] = set_members_group_members_model

        # Construct a model instance of SetDeploymentScalingGroupRequestSetMembersGroup by calling from_dict on the json representation
        set_deployment_scaling_group_request_set_members_group_model = SetDeploymentScalingGroupRequestSetMembersGroup.from_dict(set_deployment_scaling_group_request_set_members_group_model_json)
        assert set_deployment_scaling_group_request_set_members_group_model != False

        # Construct a model instance of SetDeploymentScalingGroupRequestSetMembersGroup by calling from_dict on the json representation
        set_deployment_scaling_group_request_set_members_group_model_dict = SetDeploymentScalingGroupRequestSetMembersGroup.from_dict(set_deployment_scaling_group_request_set_members_group_model_json).__dict__
        set_deployment_scaling_group_request_set_members_group_model2 = SetDeploymentScalingGroupRequestSetMembersGroup(**set_deployment_scaling_group_request_set_members_group_model_dict)

        # Verify the model instances are equivalent
        assert set_deployment_scaling_group_request_set_members_group_model == set_deployment_scaling_group_request_set_members_group_model2

        # Convert model instance back to dict and verify no loss of data
        set_deployment_scaling_group_request_set_members_group_model_json2 = set_deployment_scaling_group_request_set_members_group_model.to_dict()
        assert set_deployment_scaling_group_request_set_members_group_model_json2 == set_deployment_scaling_group_request_set_members_group_model_json

class TestSetDeploymentScalingGroupRequestSetMemoryGroup():
    """
    Test Class for SetDeploymentScalingGroupRequestSetMemoryGroup
    """

    def test_set_deployment_scaling_group_request_set_memory_group_serialization(self):
        """
        Test serialization/deserialization for SetDeploymentScalingGroupRequestSetMemoryGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        set_memory_group_memory_model = {} # SetMemoryGroupMemory
        set_memory_group_memory_model['allocation_mb'] = 12288

        # Construct a json representation of a SetDeploymentScalingGroupRequestSetMemoryGroup model
        set_deployment_scaling_group_request_set_memory_group_model_json = {}
        set_deployment_scaling_group_request_set_memory_group_model_json['memory'] = set_memory_group_memory_model

        # Construct a model instance of SetDeploymentScalingGroupRequestSetMemoryGroup by calling from_dict on the json representation
        set_deployment_scaling_group_request_set_memory_group_model = SetDeploymentScalingGroupRequestSetMemoryGroup.from_dict(set_deployment_scaling_group_request_set_memory_group_model_json)
        assert set_deployment_scaling_group_request_set_memory_group_model != False

        # Construct a model instance of SetDeploymentScalingGroupRequestSetMemoryGroup by calling from_dict on the json representation
        set_deployment_scaling_group_request_set_memory_group_model_dict = SetDeploymentScalingGroupRequestSetMemoryGroup.from_dict(set_deployment_scaling_group_request_set_memory_group_model_json).__dict__
        set_deployment_scaling_group_request_set_memory_group_model2 = SetDeploymentScalingGroupRequestSetMemoryGroup(**set_deployment_scaling_group_request_set_memory_group_model_dict)

        # Verify the model instances are equivalent
        assert set_deployment_scaling_group_request_set_memory_group_model == set_deployment_scaling_group_request_set_memory_group_model2

        # Convert model instance back to dict and verify no loss of data
        set_deployment_scaling_group_request_set_memory_group_model_json2 = set_deployment_scaling_group_request_set_memory_group_model.to_dict()
        assert set_deployment_scaling_group_request_set_memory_group_model_json2 == set_deployment_scaling_group_request_set_memory_group_model_json

class TestSetPromotionPromotionPromote():
    """
    Test Class for SetPromotionPromotionPromote
    """

    def test_set_promotion_promotion_promote_serialization(self):
        """
        Test serialization/deserialization for SetPromotionPromotionPromote
        """

        # Construct a json representation of a SetPromotionPromotionPromote model
        set_promotion_promotion_promote_model_json = {}
        set_promotion_promotion_promote_model_json['promotion'] = {}

        # Construct a model instance of SetPromotionPromotionPromote by calling from_dict on the json representation
        set_promotion_promotion_promote_model = SetPromotionPromotionPromote.from_dict(set_promotion_promotion_promote_model_json)
        assert set_promotion_promotion_promote_model != False

        # Construct a model instance of SetPromotionPromotionPromote by calling from_dict on the json representation
        set_promotion_promotion_promote_model_dict = SetPromotionPromotionPromote.from_dict(set_promotion_promotion_promote_model_json).__dict__
        set_promotion_promotion_promote_model2 = SetPromotionPromotionPromote(**set_promotion_promotion_promote_model_dict)

        # Verify the model instances are equivalent
        assert set_promotion_promotion_promote_model == set_promotion_promotion_promote_model2

        # Convert model instance back to dict and verify no loss of data
        set_promotion_promotion_promote_model_json2 = set_promotion_promotion_promote_model.to_dict()
        assert set_promotion_promotion_promote_model_json2 == set_promotion_promotion_promote_model_json

class TestSetPromotionPromotionUpgradePromote():
    """
    Test Class for SetPromotionPromotionUpgradePromote
    """

    def test_set_promotion_promotion_upgrade_promote_serialization(self):
        """
        Test serialization/deserialization for SetPromotionPromotionUpgradePromote
        """

        # Construct a json representation of a SetPromotionPromotionUpgradePromote model
        set_promotion_promotion_upgrade_promote_model_json = {}
        set_promotion_promotion_upgrade_promote_model_json['promotion'] = {}

        # Construct a model instance of SetPromotionPromotionUpgradePromote by calling from_dict on the json representation
        set_promotion_promotion_upgrade_promote_model = SetPromotionPromotionUpgradePromote.from_dict(set_promotion_promotion_upgrade_promote_model_json)
        assert set_promotion_promotion_upgrade_promote_model != False

        # Construct a model instance of SetPromotionPromotionUpgradePromote by calling from_dict on the json representation
        set_promotion_promotion_upgrade_promote_model_dict = SetPromotionPromotionUpgradePromote.from_dict(set_promotion_promotion_upgrade_promote_model_json).__dict__
        set_promotion_promotion_upgrade_promote_model2 = SetPromotionPromotionUpgradePromote(**set_promotion_promotion_upgrade_promote_model_dict)

        # Verify the model instances are equivalent
        assert set_promotion_promotion_upgrade_promote_model == set_promotion_promotion_upgrade_promote_model2

        # Convert model instance back to dict and verify no loss of data
        set_promotion_promotion_upgrade_promote_model_json2 = set_promotion_promotion_upgrade_promote_model.to_dict()
        assert set_promotion_promotion_upgrade_promote_model_json2 == set_promotion_promotion_upgrade_promote_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
