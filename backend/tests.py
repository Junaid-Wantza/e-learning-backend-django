from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from backend.models import User, Profile
import json
import apiclient



"""
User API TestCase
"""


class UserAPITestCase(APITestCase):
    
    def setUp(self):
        # Create test data
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        self.url = reverse('user-list')
    
    def test_create_user(self):
        # Test creating a new user
        response = self.client.post(self.url, data=self.user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['email'], 'testuser@example.com')

    
    def test_get_all_users(self):
        """
        Ensure we can retrieve all users
        """
        # Create some test users
        User.objects.create_user(username='testuser1', password='testpass')
        User.objects.create_user(username='testuser2', password='testpass')
        
        # Make GET request to the users endpoint
        response = self.client.get(reverse('user-list'))
        
        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check that the response data is not empty
        self.assertIsNotNone(response.data)
        
        # Check that the first item in the response data list has the expected username
        self.assertEqual(response.data[0]['username'], 'testuser1')

        
    def test_get_user_detail(self):
        # Test retrieving details of a specific user
        response = self.client.post(self.url, data=self.user_data)
        user_id = response.data['id']
        detail_url = reverse('user-detail', kwargs={'pk': user_id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['email'], 'testuser@example.com')
    
    def test_update_user(self):
        # Test updating a user's details
        response = self.client.post(self.url, data=self.user_data)
        user_id = response.data['id']
        detail_url = reverse('user-detail', kwargs={'pk': user_id})
        update_data = {
            'username': 'newusername',
            'email': 'newemail@example.com',
            'password': 'newpassword'
        }
        response = self.client.put(detail_url, data=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'newusername')
        self.assertEqual(response.data['email'], 'newemail@example.com')
        
    def test_delete_user(self):
        # Test deleting a user
        response = self.client.post(self.url, data=self.user_data)
        user_id = response.data['id']
        detail_url = reverse('user-detail', kwargs={'pk': user_id})
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(User.objects.filter(id=user_id).exists())



