# Ein Ausblick auf _instructor_ für strukturierte Ausgaben von LLM

[Instructor](https://python.useinstructor.com/)

> Instructor makes it easy to get structured data like JSON from LLMs like GPT-3.5, GPT-4, GPT-4-Vision, and open-source models including Mistral/Mixtral, Anyscale, Ollama, and llama-cpp-python. 

> It stands out for its simplicity, transparency, and user-centric design, built on top of Pydantic. Instructor helps you manage validation context, retries with Tenacity, and streaming Lists and Partial responses.

Instructor erlaubt die Definiton von (komplexen) Schemata und Validierungsregeln mit Pydantic. Im Hintergrund kümmert sich Instructor um die Übermittlung des Schemas an die API des gewählten Anbieters und nutzt dabei die jeweilis unterstützen Verfahren, gute strukturierte Outputs zu erzeugen (Function Calling, Structured Ouputs, ...).