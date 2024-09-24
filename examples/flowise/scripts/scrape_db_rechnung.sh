#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_pdf_file>"
    exit 1
fi

pdf_file="$1"

curl -s http://localhost:3333/api/v1/prediction/9c527c0e-d6eb-4cf8-a7aa-a5a7a34a0b44 \
     -X POST \
     -F 'question=Lese die Rechnung aufmerksam und vollständig!
Extrahiere die Daten für den Abfahrtsort, den Zielort und den bezahlten Betrag inklusive Mehrwertsteuer.
Gebe ein JSON-Objekt mit folgender Struktur zurück: {
"abfahrtsort": Abfahrtsort,
"zielort": Zielort,
"preis": Bezahlter Betrag inklusive Mehrwertsteuer
}' \
     -F "files=@$pdf_file" \
     -H "Content-Type: multipart/form-data" | jq ".text" | jq -r