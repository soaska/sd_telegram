import unittest
import os
import sys

# Add the parent directory to the sys.path to allow for absolute imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data import BotData

class TestBotData(unittest.TestCase):
    def setUp(self):
        """Set up a new BotData instance for each test."""
        self.bot_data = BotData(
            prompts_file='tests/prompts.json',
            presets_file='tests/presets.json'
        )

    def test_initialization(self):
        """Test that the BotData class initializes correctly."""
        self.assertEqual(self.bot_data.prompts['default'], 'a default prompt')
        self.assertEqual(self.bot_data.presets['default']['steps'], 20)
        self.assertEqual(self.bot_data.current_params['prompt'], 'a default prompt')

    def test_update_params(self):
        """Test that the update_params method works correctly."""
        self.bot_data.update_params({'steps': 25, 'width': 1024})
        self.assertEqual(self.bot_data.current_params['steps'], 25)
        self.assertEqual(self.bot_data.current_params['width'], 1024)

    def test_reset_params(self):
        """Test that the reset_params method works correctly."""
        self.bot_data.update_params({'steps': 100})
        self.bot_data.reset_params()
        self.assertEqual(self.bot_data.current_params['steps'], 20)

    def test_apply_preset(self):
        """Test that the apply_preset method works correctly."""
        self.bot_data.apply_preset('test_preset')
        self.assertEqual(self.bot_data.current_params['steps'], 30)
        self.assertEqual(self.bot_data.current_params['cfg_scale'], 8)

    def test_toggle_sd_status(self):
        """Test that the toggle_sd_status method works correctly."""
        initial_status = self.bot_data.sd_status
        self.bot_data.toggle_sd_status()
        self.assertNotEqual(initial_status, self.bot_data.sd_status)
        self.bot_data.toggle_sd_status()
        self.assertEqual(initial_status, self.bot_data.sd_status)

if __name__ == '__main__':
    unittest.main()