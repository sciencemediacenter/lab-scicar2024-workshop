# Custom Patterns

Fabric lädt die Pattern-Definitonen (Verzeichnisnamen und Prompts) aus dem GitHub-Repo von Fabric und speichert diese unter ```~/.config/fabric/patterns```

Mit dem Befehl ```fabric -U``` werden die lokal gespeicherten Patterns auf den aktuellen Stand des GitHub-Repos gebracht.

Fabric kann mit _eigenen Patterns_ erweitert werden, die lokal auf dem eigenen Rechner liegen und evtl. in einem eigenen GitHub-Repo verwaltet werden.

Für diesen Workshop nutze ich das GitHub-Repo für den Workshop (dieses!) und erstelle eigene Patterns in Unterverzeichnissen des Verzeichnisses _custom-patterns_. Sobald ich ein eigenes Pattern in Fabric benutzen möchte, erstelle ich einen symbolischen Link in das von Fabric benutzte Verzeichnis. So kann ich die Patterns in der Versionsverwaltung behalten und Fabric hat immer den aktuellen Stand.

```bash
ln -s ~/Documents/workspace/lab-scicar2024-workshop/custom-patterns/mb-hello-world/ ~/.config/fabric/patterns/mb-hello-world
```
Das Pattern _mb-hello-world_ ist denkbar einfach:

```markdown
Ignore user input and say "hello world!"
```

Die _custom patterns_ werden auf die gleiche Weise wie die Patterns aufgerufen, die Fabric mitbringt:

```bash
 echo "scicar24" | fabric --pattern mb-hello-world
 ```

```markdown
hello world!
```


