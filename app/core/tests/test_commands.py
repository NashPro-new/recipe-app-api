"""
Test custom Django management commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')                        # mocking a database for tests Command is class from wait for db and .check is BaseCommand's function (django feature)

class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""
        patched_check.return_value = True                                           # will check if db is connected and will show true if it is

        call_command('wait_for_db')                                                 # will execute command in wait for db

        patched_check.assert_called_once_with(databases=['default'])                # Ensures the mocked object that is checked method is called once only with default parameters

    @patch('time.sleep')                                                            # mocking again

    def test_wait_for_db_delay(self, patched_sleep, patched_check):                 # (when the database is not ready) patch sleep for time sleep mock and patch check for check 
        """Test waiting for database when getting OperationalError."""
        patched_check.side_effect = [Psycopg2OpError] * 2 + \
            [OperationalError] * 3 + [True]                                         # raising an exception if database is not ready (therefore .side_effect) in patched check, first two times psycop error and then second is 3 operational errors

        call_command('wait_for_db')                                                 # will execute command in wait for db

        self.assertEqual(patched_check.call_count, 6)                               # will check wait for 6 times
        patched_check.assert_called_with(databases=['default'])                     # Ensures the mocked object that is checked method is called once only with default parameters
