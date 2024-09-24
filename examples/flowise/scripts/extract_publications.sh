curl http://localhost:3333/api/v1/prediction/7b76d958-ccdc-472d-aa51-b4f0f8c7f651 \
     -s \
     -X POST \
     -H "Content-Type: application/json" \
     -d @- << EOF
{
  "question": "Do!",
  "overrideConfig": {
    "text": "$(cat /dev/stdin)"
  }
}
EOF