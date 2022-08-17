curl \
    -XPUT "http://${ELASTIC_HOST}:${ELASTIC_PORT}/persons?pretty" \
    -H 'Content-Type: application/json' \
    -u ${ELASTIC_USERNAME}:${ELASTIC_PASSWORD} \
    --silent \
    -d'
{
  "settings": {
    "refresh_interval": "1s",
    "analysis": {
      "filter": {
        "english_stop": {
          "type":       "stop",
          "stopwords":  "_english_"
        },
        "english_stemmer": {
          "type": "stemmer",
          "language": "english"
        },
        "english_possessive_stemmer": {
          "type": "stemmer",
          "language": "possessive_english"
        },
        "russian_stop": {
          "type":       "stop",
          "stopwords":  "_russian_"
        },
        "russian_stemmer": {
          "type": "stemmer",
          "language": "russian"
        }
      },
      "analyzer": {
        "ru_en": {
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "english_stop",
            "english_stemmer",
            "english_possessive_stemmer",
            "russian_stop",
            "russian_stemmer"
          ]
        }
      }
    }
  },
  "mappings": {
    "dynamic": "strict",
    "properties": {
      "id": {
        "type": "keyword"
      },
      "full_name": {
        "type": "text",
        "analyzer": "ru_en"
      },
      "roles": {
        "type": "nested",
        "dynamic": "strict",
        "properties": {
          "role": {
            "type": "text",
            "analyzer": "ru_en"
          },
          "film_ids": {
            "type": "keyword"
          }
        }
      }
    }
  }
}'