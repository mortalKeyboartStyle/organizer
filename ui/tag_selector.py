# tag_selector.py
# Keyword: tag_selector_basic

DEFAULT_TAGS = ["a", "img", "div"]

def get_user_tags(user_input):
    """
    Zwraca listę znaczników wprowadzonych przez użytkownika.
    Jeżeli brak, używa domyślnej listy DEFAULT_TAGS.
    """
    if not user_input.strip():
        return DEFAULT_TAGS
    return [tag.strip() for tag in user_input.split(",") if tag.strip()]
