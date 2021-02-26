# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import requests
import responses
from mysdk.example_service_v1 import *


service = ExampleServiceV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'http://cloud.ibm.com/mysdk/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Resources
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_resources
#-----------------------------------------------------------------------------
class TestListResources():

    #--------------------------------------------------------
    # list_resources()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resources_all_params(self):
        # Set up mock
        url = base_url + '/resources'
        mock_response = '{"offset": 6, "limit": 5, "resources": [{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        limit = 38

        # Invoke method
        response = service.list_resources(
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'limit={}'.format(limit) in query_string


    #--------------------------------------------------------
    # test_list_resources_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resources_required_params(self):
        # Set up mock
        url = base_url + '/resources'
        mock_response = '{"offset": 6, "limit": 5, "resources": [{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_resources()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_resource
#-----------------------------------------------------------------------------
class TestCreateResource():

    #--------------------------------------------------------
    # create_resource()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_all_params(self):
        # Set up mock
        url = base_url + '/resources'
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        resource_id = 'testString'
        name = 'testString'
        tag = 'testString'

        # Invoke method
        response = service.create_resource(
            resource_id,
            name,
            tag=tag,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['resource_id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['tag'] == 'testString'


    #--------------------------------------------------------
    # test_create_resource_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_resource_value_error(self):
        # Set up mock
        url = base_url + '/resources'
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        resource_id = 'testString'
        name = 'testString'
        tag = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "resource_id": resource_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_resource(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_resource
#-----------------------------------------------------------------------------
class TestGetResource():

    #--------------------------------------------------------
    # get_resource()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_all_params(self):
        # Set up mock
        url = base_url + '/resources/testString'
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_id = 'testString'

        # Invoke method
        response = service.get_resource(
            resource_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resource_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_value_error(self):
        # Set up mock
        url = base_url + '/resources/testString'
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "resource_id": resource_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_resource(**req_copy)



# endregion
##############################################################################
# End of Service: Resources
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for Resource
#-----------------------------------------------------------------------------
class TestResource():

    #--------------------------------------------------------
    # Test serialization/deserialization for Resource
    #--------------------------------------------------------
    def test_resource_serialization(self):

        # Construct a json representation of a Resource model
        resource_model_json = {}
        resource_model_json['resource_id'] = 'testString'
        resource_model_json['name'] = 'testString'
        resource_model_json['tag'] = 'testString'
        resource_model_json['read_only'] = 'testString'

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model = Resource.from_dict(resource_model_json)
        assert resource_model != False

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model_dict = Resource.from_dict(resource_model_json).__dict__
        resource_model2 = Resource(**resource_model_dict)

        # Verify the model instances are equivalent
        assert resource_model == resource_model2

        # Convert model instance back to dict and verify no loss of data
        resource_model_json2 = resource_model.to_dict()
        assert resource_model_json2 == resource_model_json

#-----------------------------------------------------------------------------
# Test Class for Resources
#-----------------------------------------------------------------------------
class TestResources():

    #--------------------------------------------------------
    # Test serialization/deserialization for Resources
    #--------------------------------------------------------
    def test_resources_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        resource_model = {} # Resource
        resource_model['resource_id'] = 'testString'
        resource_model['name'] = 'testString'
        resource_model['tag'] = 'testString'
        resource_model['read_only'] = 'testString'

        # Construct a json representation of a Resources model
        resources_model_json = {}
        resources_model_json['offset'] = 38
        resources_model_json['limit'] = 38
        resources_model_json['resources'] = [resource_model]

        # Construct a model instance of Resources by calling from_dict on the json representation
        resources_model = Resources.from_dict(resources_model_json)
        assert resources_model != False

        # Construct a model instance of Resources by calling from_dict on the json representation
        resources_model_dict = Resources.from_dict(resources_model_json).__dict__
        resources_model2 = Resources(**resources_model_dict)

        # Verify the model instances are equivalent
        assert resources_model == resources_model2

        # Convert model instance back to dict and verify no loss of data
        resources_model_json2 = resources_model.to_dict()
        assert resources_model_json2 == resources_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
