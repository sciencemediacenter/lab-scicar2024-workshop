# Custom Patterns

Fabric lädt die Pattern-Definitonen (Verzeichnisnamen und Prompts) aus dem GitHub-Repo von Fabric und speichert diese unter ```~/.config/fabric/patterns```

Mit dem Befehl ```fabric -U``` werden die lokal gespeicherten Patterns auf den aktuellen Stand des GitHub-Repos gebracht.

Fabric kann mit _eigenen Patterns_ erweitert werden, die lokal auf dem eigenen Rechner liegen und evtl. in einem eigenen GitHub-Repo verwaltet werden.

Für diesen Workshop nutze ich das GitHub-Repo für den Workshop (dieses!) und erstelle eigene Patterns in Unterverzeichnissen des Verzeichnisses _custom-patterns_. 

## "Hello world" – egal, was du sagst ...

Das erste eigene Pattern, _mb-hello-world_, ist denkbar einfach:

```markdown
Ignore user input and say "hello world!"
```

Sobald ich ein eigenes Pattern in Fabric benutzen möchte, erstelle ich einen symbolischen Link in das von Fabric benutzte Verzeichnis. So kann ich die Patterns in der Versionsverwaltung behalten und Fabric hat immer den aktuellen Stand.

```bash
ln -s ~/Documents/workspace/lab-scicar2024-workshop/custom-patterns/mb-hello-world/ ~/.config/fabric/patterns/mb-hello-world
```
Die _custom patterns_ werden auf die gleiche Weise wie die Patterns aufgerufen, die Fabric mitbringt:

```bash
 echo "scicar24" | fabric --pattern mb-hello-world
 ```

```markdown
hello world!
```
## Erzeugen wir **Daten**

Wir können Prompts so schreiben, dass sie die angefragten Sprachmodelle Daten in einem spezifizierten JSON-Format zurückgeben. (Ja, das geht auch besser und "formatsicherer", dazu später mehr.)

Wenn wir aus dem gezeigten Angebot des SMC alle Quellen extrahieren wollen, sodass wir eine Liste von JSON-Objekten im Format:

```json
{
    "author": ...,
    "title": ...,
    "year": ...,
    "venue": ...,
    "doi": ...
}
```

erhalten, können wir dieses Format im Prompt definieren und das Model anweisen, sich bei der Ausgabe an dieses Format zu halten.

Das Prompt zu _mb-extract-publications_ habe ich mit der Vorgabe des gewünschten Formats mithilfe des _Prompt Generators_ von Anthropic erzeugt. Aus meiner vagen und kurzen Anweisung wurde so ein präziser und langer Prompt.

Wenn ich das Pattern auf den Text des SMC-Angebots anwende, bekomme ich sofort sehr gute Ergebnisse, **ABER** _bisweilen_ wird die letzte Publikation nicht extrahiert. 

```
[6] Schekman R (2013): How journals like Nature, Cell and Science are damaging science. Guardian. Zeitungsartikel.
```

Mag es daran liegen, dass die Referenz am Ende eines längeren Kontextfensters steht? Oder weil diese Referenz nicht genau dem Muster der anderen Referenzen entspricht – es gibt keine DOI, dafür den Hinweis "Zeitungsartikel"?

Hier hilft das Denken in Pipelines weiter, denn in diesem Fall kann ich die Eingabe (das SMC-Angeobt) leicht vorfiltern und nur die relevanten Teile des Angebots über _Fabric_ an das Sprachmodell übergeben:

```bash
cat data/smc_angebot.txt | grep -E "\([0-9]+\)" | fabric --pattern mb-extract-publications -T 0
```

So werden nur die Zeilen an _Fabric_ übergeben, die eine Jahreszahl in runden Klammern enthalten. (Ein Pattern, das natürlich schnell bricht). Das Ergebnis ist eine perfekte Extraktion der referenzierten Publikation in das von mir spezifizierte Datenformat.

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