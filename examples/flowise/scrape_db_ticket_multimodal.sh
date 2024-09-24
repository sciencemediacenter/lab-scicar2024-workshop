#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_image_file>"
    exit 1
fi

image_path="$1"
image_name=$(basename "$image_path")
mime_type=$(file -b --mime-type "$image_path")

# Convert image to base64
image=$(base64 -i "$image_path")

(curl -s http://localhost:3333/api/v1/prediction/16b1492d-08e8-4484-8590-551a786e1045 \
     -X POST \
     -H "Content-Type: application/json" \
     -d @- << EOF
{
    "question": "Do",
    "uploads": [
        {
            "data": "data:${mime_type};base64,${image}",
            "type": "file",
            "name": "${image_name}",
            "mime": "${mime_type}"
        }
    ]
}
EOF
) | jq '.json'