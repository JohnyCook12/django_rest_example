
from urllib import parse
import json, requests
from rest_framework import status
from rest_framework.test import APITestCase


class PersonTests(APITestCase):
    """ Test class for Grouping API app on http://127.0.0.1:8000/grouping/ """

    base_url = 'http://127.0.0.1:8000/grouping/'

    def create_person(self, name, age):
        """
        Creates person by POST to /people/ and returns it´s ID.
        Raises AssertionError if server does not respond with HTTP 201 or names doesn´t match.
        :param name:
        :param age:
        :return: id:
        """

        headers = {'accept': 'application/json',
                   'content-type': 'application/json'}
        person_response = requests.post(
            parse.urljoin(self.base_url, 'people'),
            data=json.dumps({'name': name, 'age': age}),
            headers=headers)
        self.assertEqual(person_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(person_response.json()['name'], name)
        self.assertEqual(person_response.json()['age'], age)
        return person_response.json()['id']


    def create_group(self, name):
        """
        Creates group by POST to /groups.
        Raises AssertionError if server does not respond with HTTP 201 or names doesn´t match.
        :param name:
        :return id of group:
        """
        headers = {'accept': 'application/json',
                   'content-type': 'application/json'}
        group_response = requests.post(
            parse.urljoin(self.base_url, 'groups'),
            data=json.dumps({'name': name}),
            headers=headers)

        print('created group ID: ', group_response.json()['id'])

        self.assertEqual(group_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(group_response.json()['name'], name)
        return group_response.json()['id']


    def retrieve_existing_person(self, person_id):
        """
        Tries to retrieve person from /people/{id}.
        Raises AssertionError if server does not respond with HTTP 200.
        :param person_id:
        :return:
        """
        person_response = requests.get(
            parse.urljoin(self.base_url, f'people/{person_id}'),
            headers={'accept': 'application/json'})

        assert person_response.status_code == 200, \
            f"Get person didn't return expected status code, " \
            f"it returned: {person_response.status_code}"


    def retrieve_existing_group(self, group_id):
        """
        Tries to retrieve group from /people/{id}.
        Raises AssertionError if server does not respond with HTTP 200.
        :param group_id:
        :return:
        """
        group_response = requests.get(
            parse.urljoin(self.base_url, f'groups/{group_id}'),
            headers={'accept': 'application/json'})

        assert group_response.status_code == 200, \
            f"Get person didn't return expected status code, " \
            f"it returned: {group_response.status_code}"


    def assign_person_to_group(self, person_id, group_id):
        """
        Tries to assign person from /people/{id} to group. Raises AssertionError
        if server does not respond with HTTP 200 or names doesn´t match.
        :param person_id:
        :param group_id:
        :return:
        """
        headers = {'accept': 'application/json',
                   'content-type': 'application/json'}
        person_response = requests.patch(
            parse.urljoin(self.base_url, f'people/{person_id}'),
            data=json.dumps({'groups': [group_id]}),
            headers=headers)

        self.assertEqual(person_response.status_code, status.HTTP_200_OK)
        self.assertEqual(person_response.json()['groups'], [group_id])


    def count_all_persons(self):
        """
        Tries to retrieve persons from /people and count results.
        Raises AssertionError if server does not respond with HTTP 200.
        :return results count:
        """
        person_response = requests.get(
            parse.urljoin(self.base_url, 'people'),
            headers={'accept': 'application/json'})

        assert person_response.status_code == 200, \
            f"Get person didn't return expected status code, " \
            f"it returned: {person_response.status_code}"
        return len(person_response.json())


    def delete_group(self, group_id):
        """
        Delete group by ID.
        Raises AssertionError if server does not respond with HTTP 204.
        :param group_id:
        :return:
        """
        headers = {'accept': 'application/json',
                   'content-type': 'application/json'}
        group_response = requests.delete(
            parse.urljoin(self.base_url, f'groups/{group_id}'),
            data=json.dumps({'id': group_id}),
            headers=headers)

        print('Deleted group ID: ', group_id)
        self.assertEqual(group_response.status_code, status.HTTP_204_NO_CONTENT)


    def delete_person(self, person_id):
        """
        Delete group by ID.
        Raises AssertionError if server does not respond with HTTP 204.
        :param person_id:
        :return:
        """
        headers = {'accept': 'application/json',
                   'content-type': 'application/json'}
        group_response = requests.delete(
            parse.urljoin(self.base_url, f'people/{person_id}'),
            data=json.dumps({'id': person_id}),
            headers=headers)

        print('Deleted person ID: ', person_id)
        self.assertEqual(group_response.status_code, status.HTTP_204_NO_CONTENT)


    def test_all(self):
        """
        Testing:
        Get person info and count.
        Create person and group.
        Retrieve created person.
        Check if person count raised by 1.
        Delete created person and group
        Check if person count decreased by 1.
        :return:
        """

        person_count_before_creating = self.count_all_persons()

        test_person_id = self.create_person('John Doe', 40)
        test_group_id = self.create_group('hockey_team')

        self.retrieve_existing_person(test_person_id)
        self.retrieve_existing_group(test_group_id)
        self.assign_person_to_group(test_person_id, test_group_id)

        person_count_after_creating = self.count_all_persons()

        assert person_count_after_creating == person_count_before_creating + 1, \
            "person count didn´t increase by 1 after creating new person"
        self.delete_group(test_group_id)
        self.delete_person(test_person_id)
        person_count_after_deleting = self.count_all_persons()

        assert person_count_after_creating == person_count_after_deleting + 1, \
            "person count didn´t decrease by 1 after deleting person"