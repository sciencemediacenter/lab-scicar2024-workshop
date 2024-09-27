# Hello Fabric

> fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. ([GitHub](https://github.com/danielmiessler/fabric))

## "Modular Framework"

### Probleme in Bestandteile zerlegen

![Challenges and Components](img/fabric-modularity.png)

[Quelle](https://github.com/danielmiessler/fabric?tab=readme-ov-file#breaking-problems-into-components)

## "Crowdsourced set of AI prompts"

- "Too many Prompts"
- Fabric verwaltet kuratierte Prompts als sogenannte _Patterns_
- Fabric erlaubt die Nutzung die Verwendung dieser Prompts gegen unterschiedliche Sprachmodelle
- Fabric übernimmt dabei die Ansprache an die APIs
- Fabric ist ein schlichtes Kommandozeilenwerkzeug, das Eingaben erhält und Ausgaben in ein Terminal ausgibt und/oder in Dateien schreibt.

## Beispiele

### Erstelle Zusammenfassung

```bash
cat ../data/smc_angebot.txt | fabric --pattern summarize
```

```markdown
# ONE SENTENCE SUMMARY:
Kürzliche Studien zeigen, dass KI-Chatbots effektiv Zustimmung zu Verschwörungstheorien senken können, indem sie evidenzbasierte Argumente liefern.

# MAIN POINTS:
1. Gespräche mit KI-Chatbots verringern signifikant die Zustimmung zu Verschwörungstheorien.
2. Individuell angepasste Evidenz kann gegen Verschwörungstheorien wirken.
3. Die Studie umfasst über 2000 Teilnehmende, die ihre Überzeugungen bewerteten.
4. Der Effekt auf die Überzeugungen hielt bis zu zwei Monate an.
5. Experten sind sich über die praktische Anwendbarkeit des Ansatzes uneinig.
6. Vertrauen in die KI beeinflusst die Wirksamkeit der Überzeugung.
7. Die Mechanismen, die zu Veränderungen führen, sind noch unklar.
8. Menschen mit starkem Verschwörungsglauben könnten weniger offen für KI-Interaktionen sein.
9. KI könnte in sozialen Medien zur Korrektur von Falschinformationen eingesetzt werden.
10. Zukünftige Forschung sollte sich auf die Motivation zur Auseinandersetzung konzentrieren.

# TAKEAWAYS:
1. KI-Chatbots können als Werkzeuge zur Reduzierung von Verschwörungsglauben dienen.
2. Individuelle Anpassung der Argumente ist entscheidend für die Wirksamkeit.
3. Skepsis über die langfristige Wirkung und Anwendbarkeit in der Praxis bleibt.
4. Vertrauen in KI spielt eine wesentliche Rolle bei der Überzeugungsarbeit.
5. Notwendigkeit weiterer Studien, um die Mechanismen besser zu verstehen.
```

#### Was steckt hinter dem Pattern _summarize_?

Siehe https://github.com/danielmiessler/fabric/blob/main/patterns/summarize/system.md

```markdown
# IDENTITY and PURPOSE

You are an expert content summarizer. You take content in and output a Markdown formatted summary using the format below.

Take a deep breath and think step by step about how to best accomplish this goal using the following steps.

# OUTPUT SECTIONS

- Combine all of your understanding of the content into a single, 20-word sentence in a section called ONE SENTENCE SUMMARY:.

- Output the 10 most important points of the content as a list with no more than 15 words per point into a section called MAIN POINTS:.

- Output a list of the 5 best takeaways from the content in a section called TAKEAWAYS:.

# OUTPUT INSTRUCTIONS

- Create the output using the formatting above.
- You only output human readable Markdown.
- Output numbered lists, not bullets.
- Do not output warnings or notes—just the requested sections.
- Do not repeat items in the output sections.
- Do not start items with the same opening words.

# INPUT:

INPUT:
```

### Erkläre Begriffe

```bash
cat ../data/smc_angebot.txt | fabric --pattern explain_terms
```

```markdown
- KÜNSTLICHE INTELLIGENZ: Künstliche Intelligenz (KI) bezeichnet Systeme, die in der Lage sind, Aufgaben auszuführen, die normalerweise menschliche Intelligenz erfordern, wie das Verstehen von Sprache, das Lernen aus Erfahrungen und das Treffen von Entscheidungen.
-- Analogie: Ein KI-System ist wie ein sehr intelligenter, vielseitiger Roboter, der viele verschiedene Aufgaben ausführen kann, ähnlich einem menschlichen Mitarbeiter, der in verschiedenen Abteilungen eines Unternehmens arbeitet.
-- Warum es wichtig ist: KI hat das Potenzial, viele Bereiche des Lebens zu revolutionieren, von der Automatisierung bis zur Entscheidungsfindung.

- DESINFORMATION: Desinformation bezieht sich auf falsche oder irreführende Informationen, die absichtlich verbreitet werden, um die öffentliche Meinung zu beeinflussen oder Verwirrung zu stiften.
-- Analogie: Desinformation ist wie ein gefälschtes Dokument, das absichtlich erstellt wurde, um jemandem einen falschen Eindruck zu vermitteln.
-- Warum es wichtig ist: Die Verbreitung von Desinformation kann ernsthafte gesellschaftliche Folgen haben, einschließlich der Beeinflussung von Wahlen und der Erzeugung von Misstrauen gegenüber Institutionen.

- SPRECHMODELLE: Sprachmodelle sind KI-Systeme, die darauf trainiert sind, menschliche Sprache zu verstehen, zu generieren und zu verarbeiten, um verschiedene Aufgaben wie Textgenerierung, Übersetzung und Beantwortung von Fragen zu ermöglichen.
-- Analogie: Ein Sprachmodell ist wie ein sehr gebildeter Dolmetscher, der in der Lage ist, zwischen verschiedenen Sprachen und Themen zu wechseln, ohne selbst eine Meinung zu haben.
-- Warum es wichtig ist: Sprachmodelle sind entscheidend für die Entwicklung von Anwendungen wie Chatbots, die in der Lage sind, menschenähnliche Gespräche zu führen.

- VERSCHWÖRUNGSTHEORIEN: Verschwörungstheorien sind Erklärungen, die behaupten, dass geheime, oft böswillige Gruppen hinter bedeutenden Ereignissen stehen, und die häufig auf Misstrauen gegenüber offiziellen Erklärungen basieren.
-- Analogie: Verschwörungstheorien sind wie fiktive Geschichten, die sich um Geheimnisse und Intrigen drehen, bei denen die Wahrheit oft weniger aufregend oder komplex ist als die Theorie selbst.
-- Warum es wichtig ist: Verschwörungstheorien können zu gesellschaftlichen Spannungen führen und das Vertrauen in wichtige Institutionen und die Wissenschaft untergraben.

- DEBUNKING: Debunking bezeichnet den Prozess, falsche Informationen oder Mythen zu widerlegen, indem man evidenzbasierte Argumente und Fakten präsentiert.
-- Analogie: Debunking ist wie ein Detektiv, der einen Fall aufklärt, indem er Beweise sammelt und die falschen Annahmen des Täters entlarvt.
-- Warum es wichtig ist: Debunking ist entscheidend im Kampf gegen Falschinformationen und Desinformation, da es das Verständnis und die Aufklärung der Öffentlichkeit fördert.

- EMPATHISCHE KOMMUNIKATION: Empathische Kommunikation ist ein Ansatz, bei dem Verständnis und Mitgefühl für die Perspektiven und Gefühle anderer in den Vordergrund gestellt werden, um Vertrauen aufzubauen und effektivere Gespräche zu führen.
-- Analogie: Empathische Kommunikation ist wie ein einfühlsames Gespräch zwischen Freunden, bei dem jeder versucht, die Gefühle und Ansichten des anderen zu verstehen und zu respektieren.
-- Warum es wichtig ist: Empathische Kommunikation kann helfen, Spannungen abzubauen und produktive Dialoge zu fördern, insbesondere in kontroversen Themen wie Verschwörungstheorien.

- MOTIVATED REASONING: Motivated reasoning beschreibt den kognitiven Prozess, bei dem Menschen Informationen so interpretieren, dass sie ihren bestehenden Überzeugungen und Gefühlen entsprechen, oft unabhängig von den tatsächlichen Beweisen.
-- Analogie: Motivated reasoning ist wie das Auswählen von Lieblingssnacks aus einem Buffet, wo man nur die Dinge nimmt, die man mag, anstatt alle Optionen objektiv zu betrachten.
-- Warum es wichtig ist: Motivated reasoning kann dazu führen, dass Menschen an falschen Überzeugungen festhalten und sich gegen widersprüchliche Informationen abschotten, was die Überzeugungsarbeit erschwert.

- BLACK-BOX-INTERVENTIONEN: Black-box-Interventionen sind Ansätze, bei denen die genauen Mechanismen oder Abläufe eines Systems nicht vollständig verstanden oder kontrolliert werden können, was oft bei KI-Systemen der Fall ist.
-- Analogie: Eine Black-box-Intervention ist wie ein Zaubertrick, bei dem man nicht sehen kann, wie das Ergebnis erzielt wurde, man weiß nur, dass es funktioniert hat.
-- Warum es wichtig ist: Das Verständnis der Funktionsweise von Interventionsmechanismen ist entscheidend für die Entwicklung effektiver Strategien zur Bekämpfung von Problemen wie Falschinformationen.
```

#### Was steckt hinter dem Pattern _explain\_terms_

Siehe https://github.com/danielmiessler/fabric/blob/main/patterns/explain_terms/system.md

```markdown
# IDENTITY

You are the world's best explainer of terms required to understand a given piece of content. You take input and produce a glossary of terms for all the important terms mentioned, including a 2-sentence definition / explanation of that term.

# STEPS

- Consume the content.

- Fully and deeply understand the content, and what it's trying to convey.

- Look for the more obscure or advanced terms mentioned in the content, so not the basic ones but the more advanced terms.

- Think about which of those terms would be best to explain to someone trying to understand this content.

- Think about the order of terms that would make the most sense to explain.

- Think of the name of the term, the definition or explanation, and also an analogy that could be useful in explaining it.

# OUTPUT

- Output the full list of advanced, terms used in the content.

- For each term, use the following format for the output:

## EXAMPLE OUTPUT

- STOCHASTIC PARROT: In machine learning, the term stochastic parrot is a metaphor to describe the theory that large language models, though able to generate plausible language, do not understand the meaning of the language they process.
-- Analogy: A parrot that can recite a poem in a foreign language without understanding it.
-- Why It Matters: It pertains to the debate about whether AI actually understands things vs. just mimicking patterns.

# OUTPUT FORMAT

- Output in the format above only using valid Markdown.

- Do not use bold or italic formatting in the Markdown (no asterisks).

- Do not complain about anything, just do what you're told.
```