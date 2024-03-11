
class DeckEndPoints:

    def __init__(self, api_object,Baseurl):
        self.my_api = api_object
        self.base_url=Baseurl

    def new_deck_api(self):
        url = self.base_url + 'deck/new/'
        result = self.my_api.api_get_request(url)
        return result

    def shuffle_deck_api(self, deck_id):
        url = f'{self.base_url}deck/{deck_id}/shuffle/'
        result = self.my_api.api_get_request(url)
        return result

    def draw_cards_api(self, deck_id, count):
        url = f'{self.base_url}deck/{deck_id}/draw/?count={count}'
        result = self.my_api.api_get_request(url)
        return result.json()

    def draw_specific_card_api(self, deck_id, card_to_draw):
        url = f'{self.base_url}deck/{deck_id}/draw/?cards={card_to_draw}'
        result = self.my_api.api_get_request(url)
        return result

    def partial_deck_api(self, cards):
        url = f'{self.base_url}deck/new/shuffle/?cards={cards}'
        result = self.my_api.api_get_request(url)
        return result.json()

    def partial_deck_info_api(self, deck_id):
        url = f'{self.base_url}deck/{deck_id}'
        result = self.my_api.api_get_request(url)
        return result.json()

    def add_to_pile_api(self, deck_id, pile_name, cards_to_add):
        url = f'{self.base_url}deck/{deck_id}/pile/{pile_name}/add/'
        data = {"cards": cards_to_add}
        result = self.my_api.api_post_request(url, data=data)
        return result.json()
