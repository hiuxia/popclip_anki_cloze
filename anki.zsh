curl -X POST 'http://localhost:8765' -H 'Content-Type: application/json' -d "{
    \"action\": \"guiAddCards\",
    \"version\": 6,
    \"params\": {
        \"note\": {
            \"deckName\": \"Default\",
            \"modelName\": \"Cloze\",
            \"fields\": {
                \"Text\": \"${POPCLIP_TEXT}\"
            },
            \"tags\": [
                \"popclip\"
            ]
        }
    }
}"
