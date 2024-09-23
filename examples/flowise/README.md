# Beispiele für Flowise

[FlowiseAI](https://flowiseai.com/) ist ein

> Open source low-code tool for developers to build customized LLM orchestration flow & AI agents

## Setup

Mit den [Konfigurationsdateien aus dem Flowise-Repo](https://github.com/FlowiseAI/Flowise/tree/main/docker) lässt sich schnell eine lokale Instanz von FlowiseAI starten. Die nötigen Dateien (außer .env) befinden sich bereits in diesem Verzeichnis. 

Ich habe dort an den Standardwerten bis auf die Portnummer (3000 => 3333) nichts verändert. Außerdem habe ich noch eine Environemnt-Variable für den OPENAI_API_KEY hinzugefügt.

```bash
docker-compose up
```

Baut das Image und startet den Container. Nach dem Starten des Containers ist FlowiseAI in meiner Konfiguration unter http://localhost:3333/ erreichbar. 