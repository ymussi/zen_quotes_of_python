from flask import Flask
from flask_graphql import GraphQLView
from zen.api.quotes.schemas import schema

app = Flask('__name__')

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    "graphql",
    schema=schema,
    graphiql=True
))

if __name__ == "__main__":
    host = '0.0.0.0'
    port = '8888'
    debug = True
    app.run(host, int(port), debug)