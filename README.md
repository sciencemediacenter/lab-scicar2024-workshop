<div id="header" align="center">
  <img src="https://media.sciencemediacenter.de/static/img/logos/smc/smc-logo-typo-bw-big.png" width="300"/>

  <div id="badges" style="padding-top: 20px">
    <a href="https://www.sciencemediacenter.de">
      <img src="https://img.shields.io/badge/Website-orange?style=plastic" alt="Website Science Media Center"/>
    </a>
    <a href="https://twitter.com/smc_germany_lab">
      <img src="https://img.shields.io/badge/Twitter-blue?style=plastic&logo=twitter&logoColor=white" alt="Twitter SMC Lab"/>
    </a>
  </div>
</div>

# Vom Text zur Analyse: Large Language Models als Werkzeug für datenjournalistische Anwendungen 

Zach Seward, der neue Director of AI Initiatives der NYT, hat jüngst darauf hingewiesen, dass die verbreitete Annahme, Tools wie ChatGPT seien hauptsächlich für das Verfassen von Texten gedacht, das wahre Potenzial von Large Language Models (LLM) unterschätzt. Die eigentliche Stärke von LLM liege nicht im Verfassen von Texten, sondern darin, aus unstrukturierten Texten strukturierte Daten zu gewinnen. Im komplexen Alltag von Journalist:innen erwiesen sich LLMs als nützliche Werkzeuge, um Texte zusammenzufassen, Daten zu verstehen und Informationen strukturiert zu erfassen.

Wie jedoch gelingt der Brückenschlag von dieser wichtigen und richtigen Einschätzung des Potenzials von LLM in die konkrete datenjournalistische Praxis?

Es gibt verschiedene Wege die Nutzung von LLM in ein Tooling für explorative und produktive Anwendungen zu überführen. LLM können über APIs programmatisch genutzt werden, Frameworks wie LangChain helfen bei der Abstraktion häufiger Use Cases und neue No-Code-Ansätze wie FlowiseAI bieten einfache Möglichkeiten, auch komplexe Verkettungen von Anfragen an LLM visuell zu modellieren.

Wir werden in diesem Workshop am Beispiel der Frameworks [Fabric](https://github.com/danielmiessler/fabric) einen weiteren Ansatz für die Nutzung von LLM in der datenjournalistischen Praxis vorstellen: die Verwendung von LLM-Anfragen im Unix-Stil. Kuratierte Prompts aus einer erweiterbaren Bibliothek werden für spezifischen Aufgaben ausgeführt und können mit anderen Werkzeugen auf der Ebene der Kommandozeile kombiniert werden.

Dieser Ansatz erlaubt die einfache Verwendung von LLM-Anfragen in Pipelines, in denen Inhalte mit bestehenden Werkzeugen abgerufen werden, um durch LLM-Anfragen verarbeitet und an weiterverarbeitende Werkzeuge oder weitere LLM-Anfragen weitergereicht zu werden. Nach diesem Muster sollen im Workshop u.a. Webseiten, PDF-Dateien und Transkripte von YouTube-Videos mithilfe von LLM ausgewertet werden.

Grundkenntnisse in der Verwendung einer Unix-Shell sind hilfreich. Für die aktive Teilnahme am Workshop wäre es zudem ratsam, Fabric vorab auf dem eigenen Laptop zu installieren.