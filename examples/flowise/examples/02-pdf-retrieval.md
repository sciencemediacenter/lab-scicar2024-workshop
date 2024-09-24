# Daten aus PDF auslesen

## Flow

## Programmatischer Aufruf

```bash
curl http://localhost:3333/api/v1/prediction/9c527c0e-d6eb-4cf8-a7aa-a5a7a34a0b44 \
     -X POST \
     -F'question="Lese die Rechnung aufmerksam und vollständig!
Extrahiere die Daten für den Abfahrtsort, den Zielort und den bezahlten Betrag inklusive Mehrwertsteuer.
Gebe ein JSON-Objekt mit folgender Struktur zurück: {
\"abfahrtsort\": Abfahrtsort,
\"zielort\": Zielort,
\"preis\": Bezahlter Betrag inklusive Mehrwertsteuer
}"' \
     -F "files=@/Users/mbittkowski/Downloads/DB_Rechnung_121649591420.pdf" \
     -H "Content-Type: multipart/form-data"
```

Kapselung als Shell-Skript mit Parameter für die PDF-Datei und Formatierung des Ergebnisses mit _jq_.

```bash
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
```

Beispiel: ```sh examples/flowise/scrape_db_rechnung.sh ~/Downloads/DB_Rechnung_121649591420.pdf ```

```json
{
  "abfahrtsort": "Tübingen Hbf",
  "zielort": "Köln Hbf",
  "preis": 77.95
}
```