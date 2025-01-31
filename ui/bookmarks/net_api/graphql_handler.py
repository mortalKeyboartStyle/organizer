"""
graphql_handler.py
Keyword: net_api_graphql

Umożliwienie zapytań GraphQL na wynikach scrapingu.
Przykład z Graphene (Python).
"""

import graphene

class Link(graphene.ObjectType):
    url = graphene.String()
    content = graphene.String()

class Query(graphene.ObjectType):
    all_links = graphene.List(Link)

    def resolve_all_links(root, info):
        # Tu pobierz dane z main_window.results_data albo bazy
        return [
            Link(url="http://example.com", content="Example content"),
            Link(url="http://test.com", content="Test content")
        ]

schema = graphene.Schema(query=Query)

def execute_graphql(query_string):
    """
    Wykonuje zapytanie GraphQL i zwraca wynik (dane lub błędy).
    """
    result = schema.execute_sync(query_string)
    return result.data if not result.errors else result.errors
