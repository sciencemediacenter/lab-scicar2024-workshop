# Publikationen mit FlowiseAI extrahieren

## Der Flow

## Programmatischer Aufruf

Aufruf der Prediction-API für den von uns definierten Flow

```bash
curl http://localhost:3333/api/v1/prediction/7b76d958-ccdc-472d-aa51-b4f0f8c7f651 \
     -X POST \
     -d '{"question": "Hey, how are you?"}' \
     -H "Content-Type: application/json"
```

```json
{"json":[{"author":"Costello T H et al.","title":"Durably reducing conspiracy beliefs through dialogues with AI","year":"2024","venue":"Science","doi":"10.1126/science.adq1814"},{"author":"Holford D et al.","title":"The empathetic refutational interview to tackle vaccine misconceptions and improve vaccine acceptance","year":"2024","venue":"Health Psychology","doi":"10.1037/hea0001354"}],"question":"Hey, how are you?","chatId":"7e2b5ab8-6b95-438e-a3da-ed4c465b69af","chatMessageId":"f0fe176d-0517-4aee-94df-38c20fd611b0","isStreamValid":false,"sessionId":"7e2b5ab8-6b95-438e-a3da-ed4c465b69af"
```

### Wie überschreiben wir die Daten für das Textfeld _plainText\_0_?

```bash
curl http://localhost:3333/api/v1/prediction/7b76d958-ccdc-472d-aa51-b4f0f8c7f651 \
     -X POST \
     -d '{"question": "Do!", "overrideConfig": {"text": "[5] Johnson A et al. (2024): Inoculation hesitancy: an exploration of challenges in scaling inoculation theory. Royal Society Open Science. DOI: 10.1098/rsos.231711. \n [6] Schekman R (2013): How journals like Nature, Cell and Science are damaging science. Guardian. Zeitungsartikel."}}' \
     -H "Content-Type: application/json"
```

```json
{"json":[{"author":"Johnson A et al.","title":"Inoculation hesitancy: an exploration of challenges in scaling inoculation theory","year":"2024","venue":"Royal Society Open Science","doi":"10.1098/rsos.231711"},{"author":"Schekman R","title":"How journals like Nature, Cell and Science are damaging science","year":"2013","venue":"Guardian","doi":"N/A"}],"question":"Do!","chatId":"d9f3dd21-5452-4e61-bde4-2332bfb1e226","chatMessageId":"b3867dd4-38de-4a61-b7bc-cbd0d0c2f2d0","isStreamValid":false,"sessionId":"d9f3dd21-5452-4e61-bde4-2332bfb1e226"}
```

### Wie bekommt man Daten dynamisch an die API?

```bash
cat data/smc_angebot.txt | curl http://localhost:3333/api/v1/prediction/7b76d958-ccdc-472d-aa51-b4f0f8c7f651 \
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
```

Etwas wild, aber man kann das gut in ein kleines Shell-Skript verpacken:

```bash
cat data/smc_angebot.txt | sh examples/flowise/extract_publications.sh 
```

(und natürlich wäre hier ein kleines Python-Skript für Integration der FlowiseAI-API möglich …)

FlowiseAI liefert das Ergebnis, das uns interessiert unter dem Schlüssel "json" zurück. Mit _jq_ können wir dieses Feld direkt extrahieren und von den Status-Meldungen der FlowiseAI-API trennen:

```bash
cat data/smc_angebot.txt | sh examples/flowise/extract_publications.sh  | jq '.json'
```
Et voilà: wir rufen mit unseren Textdaten einen _entkoppelten_ Flow auf und können die Ergebnisse beliebig weiterverarbeiten.

```json
[
  {
    "author": "Costello T H et al.",
    "title": "Durably reducing conspiracy beliefs through dialogues with AI",
    "year": "2024",
    "venue": "Science",
    "doi": "10.1126/science.adq1814"
  },
  {
    "author": "Holford D et al.",
    "title": "The empathetic refutational interview to tackle vaccine misconceptions and improve vaccine acceptance",
    "year": "2024",
    "venue": "Health Psychology",
    "doi": "10.1037/hea0001354"
  },
  {
    "author": "Ayers J W et al.",
    "title": "Comparing physician and artificial intelligence chatbot responses to patient questions posted to a public social media forum",
    "year": "2023",
    "venue": "JAMA Internal Medicine",
    "doi": "10.1001/jamainternmed.2023.1838"
  },
  {
    "author": "Altay S et al.",
    "title": "Scaling up interactive argumentation by providing counterarguments with a chatbot",
    "year": "2022",
    "venue": "Nature Human Behavior",
    "doi": "10.1038/s41562-021-01271-w"
  },
  {
    "author": "Kozyreva A et al.",
    "title": "Toolbox of individual-level interventions against online misinformation",
    "year": "2024",
    "venue": "Nature Human Behaviour",
    "doi": "10.1038/s41562-024-01881-0"
  },
  {
    "author": "Johnson A et al.",
    "title": "Inoculation hesitancy: an exploration of challenges in scaling inoculation theory",
    "year": "2024",
    "venue": "Royal Society Open Science",
    "doi": "10.1098/rsos.231711"
  },
  {
    "author": "Schekman R",
    "title": "How journals like Nature, Cell and Science are damaging science",
    "year": "2013",
    "venue": "Guardian",
    "doi": "N/A"
  }
]
```