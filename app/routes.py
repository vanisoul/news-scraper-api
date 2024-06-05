from flask import Blueprint, jsonify
from .scraper import scrape_news
from flasgger import swag_from

main = Blueprint('main', __name__)

@main.route('/scrape', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Scraping completed successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'news': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'title': {
                                    'type': 'string'
                                },
                                'link': {
                                    'type': 'string'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
})
def scrape():
    news = scrape_news()
    return jsonify({"news": news})
