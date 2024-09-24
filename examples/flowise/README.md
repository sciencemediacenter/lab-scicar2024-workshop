# Beispiele für Flowise

[FlowiseAI](https://flowiseai.com/) ist ein

> Open source low-code tool for developers to build customized LLM orchestration flow & AI agents

## Setup

Mit den [Konfigurationsdateien aus dem Flowise-Repo](https://github.com/FlowiseAI/Flowise/tree/main/docker) lässt sich schnell eine lokale Instanz von FlowiseAI starten. Die nötigen Dateien (außer .env) befinden sich bereits in diesem Verzeichnis. 

Ich habe dort an den Standardwerten bis auf die Portnummer (3000 => 3333) nichts verändert. 

```bash
docker-compose up
```

Baut das Image und startet den Container. Nach dem Starten des Containers ist FlowiseAI in meiner Konfiguration unter http://localhost:3333/ erreichbar. 

In der Oberfläche von FlowiseAI können dann Credentials für die verwendeten externen Services hinterlegt werden. Dies Beispiele in diesem Workshop nutzen eine API-Key für OpenAI mit der Bezeichnung _OPEN_AI_KEY_.

Die Flow-Definitionen in _flows/_ können importiert werden, nachdem man einen neuen Chatflow angelegt hat.