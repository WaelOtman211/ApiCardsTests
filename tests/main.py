import unittest

from infra.api_wrapper import APIWrapper
from infra.config_handler import ConfigHandler
from logic.deck_endpoints import DeckEndPoints


class MainTest(unittest.TestCase):

    def setUp(self):
        self.my_api = APIWrapper()
        config_file_path = 'C:\AutomationWithTsahi\APITesting\config.json'
        self.config_handler = ConfigHandler(config_file_path)
        self.base_url = self.config_handler.get_base_url()
        self.cards = self.config_handler.get_cards()
        self.api_logic = DeckEndPoints(self.my_api,self.base_url)


    def test_new_deck(self):
        result = self.api_logic.new_deck_api()
        self.assertTrue(result.json()['success'])

    def test_shuffle_deck(self):
        deck_id = "new"
        result = self.api_logic.shuffle_deck_api(deck_id)
        self.assertTrue(result.ok)

    def test_draw_cards(self):
        deck_id = "new"
        count = 2
        result = self.api_logic.draw_cards_api(deck_id, count)
        self.assertEqual(len(result['cards']), count)

    def test_draw_multiple_cards(self):
        # Arrange
        new_deck_result = self.api_logic.new_deck_api()
        self.assertTrue(new_deck_result.ok)
        self.deck_id = new_deck_result.json()['deck_id']

        # Act
        count = 5
        draw_card_result = self.api_logic.draw_cards_api(self.deck_id, count)

        # Assert
        self.assertTrue(draw_card_result['success'])
        drawn_cards = draw_card_result['cards']
        self.assertEqual(len(drawn_cards), count)

    def test_partial_deck_information(self):
        partial_deck_result = self.api_logic.partial_deck_api(self.cards)
        deck_id = partial_deck_result['deck_id']
        partial_deck_info_result = self.api_logic.partial_deck_info_api(deck_id)
        expected_remaining = 12
        self.assertEqual(expected_remaining, partial_deck_info_result['remaining'], "not the same")



if __name__ == '__main__':
    unittest.main()
