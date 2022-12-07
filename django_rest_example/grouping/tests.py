from urllib import parse

from django.test import TestCase, Client

import json, requests
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse

from .serializers import PersonSerializer, PersonCreateSerializer, GroupSerializer
from .models import Group, Person


class PersonTests(APITestCase):
    base_url = 'http://127.0.0.1:8000/grouping/'

    def test_create_person(self, name="John Doe", age=40):
        """
        Creates person by POST to /people/
        :param name:
        :param age:
        :return:
        """

        headers = {'accept': 'application/json',
                   'content-type': 'application/json'}
        person_response = requests.post(
            parse.urljoin(self.base_url, 'people'),
            data=json.dumps({'name': name, 'age': age}),
            headers=headers)

        print('vytvoreno ID: ', person_response.json()['id'])

        self.assertEqual(person_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(person_response.json()['name'], "John Doe")

    def test_create_group(self, name="football"):
        """
        Creates group by POST to /groups/
        :param name:
        :return:
        """
        headers = {'accept': 'application/json',
                   'content-type': 'application/json'}
        group_response = requests.post(
            parse.urljoin(self.base_url, 'groups'),
            data=json.dumps({'name': name}),
            headers=headers)

        print('created group ID: ', group_response.json()['id'])

        self.assertEqual(group_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(group_response.json()['name'], "football")

    def test_assert_person_exists(self, person_id=26):
        """
        Tries to retrieve person from /people/{id}. Raises AssertionError
        if server does not respond with HTTP 200.
        :param person_id:
        :return:
        """
        person_response = requests.get(
            parse.urljoin(self.base_url, f'people/{person_id}'),
            headers={'accept': 'application/json'})

        print('zaznam ID=26: ',person_response.json())
        assert person_response.status_code == 200, \
            f"Get person didn't return expected status code, " \
            f"it returned: {person_response.status_code}"

    def test_assert_all_existing_persons(self):
        """
        Tries to retrieve person from /people/{id}. Raises AssertionError
        if server does not respond with HTTP 200.
        :param person_id:
        :return:
        """
        person_response = requests.get(
            parse.urljoin(self.base_url, 'people'),
            headers={'accept': 'application/json'})

        print('vsecky ID: ',len(person_response.json()))
        assert person_response.status_code == 200, \
            f"Get person didn't return expected status code, " \
            f"it returned: {person_response.status_code}"


# =============================================================================================================================
# =============================================================================================================================
# =============================================================================================================================


# class RegistrationTestCase(APITestCase):
#     def test_registration(self):
#         data = {"username": "Peter", "email": "john.yyy@seznam.cz", "password1": "Weakpass123", "password2": "Weakpass123"}
#         response = self.client.post("admin/registration", data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class TestClient:
#     def __init__(self, base_url):
#         self.base_url = base_url
#
#     def assert_person_exists(self, person_id):
#         """
#         Tries to retrieve person from /people/{id}. Raises AssertionError
#         if server does not respond with HTTP 200.
#         :param person_id:
#         :return:
#         """
#         person_response = requests.get(
#             parse.urljoin(self.base_url, f'people/{person_id}'),
#             headers={'accept': 'application/json'})
#         assert person_response.status_code == 200, \
#             f"Get person didn't return expected status code, " \
#             f"it returned: {person_response.status_code}"
#
#     def create_person(self, name="John Doe", age=40):
#         """
#         Creates person by POST to /people/
#         :param name:
#         :param age:
#         :return:
#         """
#         headers = {'accept': 'application/json',
#                    'content-type': 'application/json'}
#         person_response = requests.post(
#             parse.urljoin(self.base_url, 'people/'),
#             data=json.dumps({'name': name, 'age': age}),
#             headers=headers)
#
#         assert person_response.status_code == 201, \
#             f"Create person didn't return expected status code, it returned: " \
#             f"{person_response.status_code}"
#
#         return person_response.json()
#
#
# class GroupingAPITestCase(APITestCase):
#
#     def test_created_person_can_be_retrieved(self):
#         # client = TestClient(f'http://localhost:8000')
#         client = TestClient(f'http://127.0.0.1:8000/grouping')
#         person = client.create_person(name="John Doe", age=40)
#         client.assert_person_exists(person['id'])



# =====================   post fungovalo, ale get nikdy nic nenašlo. DB se vždy smazala.   ======================
#
# class GroupingAPITestCase(APITestCase):
#
#     base_url = 'http://127.0.0.1:8000/grouping/'
#
#     def test_create_person(self):
#         previous_person_count = Person.objects.all().count()
#         sample_person = {"name": "Peter", "age": 20}
#         response = self.client.post(reverse('person_list'), sample_person)
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Person.objects.all().count(), previous_person_count+1)
#         self.assertEqual(response.data["name"], "Peter")
#         print("created id: ",response.data)
#
#     def test_create_group(self):
#         previous_group_count = Group.objects.all().count()
#         sample_group = {"name": "football"}
#         response = self.client.post(reverse('group_list'), sample_group)
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Group.objects.all().count(), previous_group_count+1)
#         self.assertEqual(response.data["name"], "football")
#         self.assertEqual(response.data["id"], 1)
#
#
#
#     def test_person_exists2(self, person_id=1):
#         """
#         Tries to retrieve person from /people/{id}. Raises AssertionError
#         if server does not respond with HTTP 200.
#         :param person_id:
#         :return:
#         """
#
#         response = Client().get(reverse('person_list'))
#         # response = self.client.get(reverse('person_list'))
#         # response = self.client.get(reverse('person'), sample_person)
#         print("RESPO: ", response.status_code)
#         print("RESPO: ", response.content)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # self.assertEqual(response.data['name'], 'Peter')


# ===========================================

    #
    # def test_create_person(self, name="John Doe", age=40):
    #     """
    #     Creates person by POST to /people/
    #     :param name:
    #     :param age:
    #     :return:
    #     """
    #     headers = {'accept': 'application/json',
    #                'content-type': 'application/json'}
    #     person_response = requests.post(
    #         parse.urljoin(self.base_url, 'people'),
    #         data=json.dumps({'name': name, 'age': age}),
    #         headers=headers)
    #
    #     self.assertEqual(person_response.status_code, status.HTTP_201_CREATED)

    # def test_assert_person_exists(self, person_id=1):
    #     """
    #     Tries to retrieve person from /people/{id}. Raises AssertionError
    #     if server does not respond with HTTP 200.
    #     :param person_id:
    #     :return:
    #     """
    #     person_response = requests.get(
    #         parse.urljoin(self.base_url, f'people/{person_id}'),
    #         headers={'accept': 'application/json'})
    #     assert person_response.status_code == 200, \
    #         f"Get person didn't return expected status code, " \
    #         f"it returned: {person_response.status_code}"

    # def test_asign_to_group(self):
    #
    #     sample_person = {"id":1, "age": 22, "group": 1}
    #     response = self.client.patch(reverse('person'), sample_person)
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     # self.assertEqual(Group.objects.all().count(), previous_group_count + 1)
    #     self.assertEqual(response.data["group"], 1)
    #     self.assertEqual(response.data["age"], 22)

    # def test_person_exists(self):
    #
    #     response = self.client.get(reverse('person_list'))
    #
    #     # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     # self.assertEqual(Person.objects.all().count(), previous_person_count+1)
    #     # self.assertEqual(response.data["name"], "Peter")
    #     print("response: ",response)
    #     print("response: ",response.json())



