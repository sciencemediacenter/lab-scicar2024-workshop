# Weitere Quellen

## Webseiten als Markdown mit Jina AI

Webseiten sind natürlich eine wichtige Quelle für Informationen, die man weiterverarbeiten möchte. Mit ```wget``` oder ```curl``` lassen sich auch leicht einzelne Webseiten herunterladen und als Eingabe für eine Pipeline verwenden. 

Bei modernen Webseiten lädt man neben dem "eigentlichen" Inhalt (bspw. die Texte, die Menschen lesen und Sprachmodelle verarbeiten sollen) eine Menge an Rahmenwerk runter, das für die weitere Verarbeitung unnötig ist.

Das gilt z.B. für den Blog von Zach Seward:

```bash
curl -s https://www.zachseward.com/
```
 Auch wenn große Sprachmodelle mit diesen Strukturen umgehen können und ggf. gewisse Strukturelemente auch dabei helfen, zu verstehen, welche Inhalte auf welcher Bedeutungsebene stehen, kann es nützlich sein, eine aufgeräumtere Fassung der Inhalte zu verwenden. Nebenbei spart man noch etwas Geld, da weniger Token verarbeitet werden müssen.

 Jina AI bietet eine [Reader-Modell](https://jina.ai/news/reader-lm-small-language-models-for-cleaning-and-converting-html-to-markdown) an, mit dem HTML-Inhalte in Markdown überführt werden können. Der Zugriff auf das Reader-Modell ist in _Fabric_ integriert. Für höhere Durchsätze kann ein API-Key hinterlegt werden. Für unseren einfachen Test geht's aber auch so:

 ```bash
 fabric -u https://www.zachseward.com/
 ```
```markdown
Title: Zach Seward — ZMS

URL Source: https://www.zachseward.com/

Markdown Content:
Zach Seward — ZMS
===============

[Skip to content](https://www.zachseward.com/#main-content)

[![Image 1: Zach Seward](https://www.zachseward.com/content/images/2023/03/ZMS.png)](https://www.zachseward.com/)

*   [About](https://www.zachseward.com/about/)
*   [Blog](https://www.zachseward.com/blog/)
*   [Email](https://www.zachseward.com/#/portal/)
*   [Log in](https://www.zachseward.com/#/portal/signin)
*   [Membership](https://www.zachseward.com/#/portal/signup)
*   Search

![Image 2: Zach Seward](https://www.zachseward.com/content/images/size/w256/2024/03/Zach-Seward1935-squarecloser-1.png)

Hi, I'm **Zach Seward**, a journalist and media entrepreneur based in New York. I'm the editorial director of AI initiatives at The New York Times. Before that, I co-founded the business news organization Quartz. My professional biography, contact information, etc., [can be found here](https://www.zachseward.com/about).

Sign up below to receive new writing from me every once in a while. Thanks!

Your email address  Subscribe

Please check your inbox and click the link to confirm your subscription.

Please enter a valid email address!

An error occurred, please try again later.

Featured Posts
--------------

Jun 19, 2024

Paid Members Public

[Stephen Clark Seward](https://www.zachseward.com/stephen-clark-seward/)
------------------------------------------------------------------------

My eulogy for Dad

![Image 3: Stephen Clark Seward](https://www.zachseward.com/content/images/size/w1460/2024/06/740437963.308778.jpg)

May 2, 2024

Paid Members Public

[AI is not like you and me](https://www.zachseward.com/ai-is-not-a-person/)
---------------------------------------------------------------------------

My talk at an Aspen Institute event

![Image 4: AI is not like you and me](https://www.zachseward.com/content/images/size/w1460/2024/05/coverslide-1.jpg)

Apr 12, 2024

Paid Members Public

[Creating structure with generative AI](https://www.zachseward.com/creating-structure-with-generative-ai/)
----------------------------------------------------------------------------------------------------------

My talk at ISOJ 2024

![Image 5: Creating structure with generative AI](https://www.zachseward.com/content/images/size/w1460/2024/04/title-slide.001-1.jpeg)

Mar 11, 2024

Paid Members Public

[AI news that's fit to print](https://www.zachseward.com/ai-news-thats-fit-to-print-sxsw-2024/)
-----------------------------------------------------------------------------------------------

My talk at SXSW 2024

![Image 6: AI news that's fit to print](https://www.zachseward.com/content/images/size/w1460/2024/03/AI-news-that-s-fit-to-print---SXSW-2024.001.jpeg)

Aug 7, 2023

Paid Members Public

[Keeping score](https://www.zachseward.com/keeping-score/)
----------------------------------------------------------

With a stubby blue pencil, no eraser.

![Image 7: Keeping score](https://www.zachseward.com/content/images/size/w1460/2023/08/IMG_3477-1.jpeg)

Jul 26, 2023

Paid Members Public

[A few tactics that actually helped diversify our newsroom](https://www.zachseward.com/a-few-tactics-that-actually-helped-diversify-our-newsroom/)
--------------------------------------------------------------------------------------------------------------------------------------------------

This is is not a success story, but we did make some progress.

![Image 8: A few tactics that actually helped diversify our newsroom](https://www.zachseward.com/content/images/size/w1460/2023/07/tempImagey1RErn.gif)

[All Posts →](https://www.zachseward.com/blog/)

Read more from Zach
-------------------

Sign up to receive occasional emails with new posts.

Your email address  Subscribe

Please check your inbox and click the link to confirm your subscription.

Please enter a valid email address!

An error occurred, please try again later.

© 2024, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)  
[Go back up ↑](https://www.zachseward.com/#top) [Go somewhere else ↘](https://randomstreetview.com/)
```

Nun können wir mit dem Pattern _mb-extract-blog-posts_ die Metadaten zu einzeln Blog-Posts aus dem aufgeräumten Markdown extrahieren:

```bash
fabric -u https://www.zachseward.com/ | fabric --pattern mb-extract-blog-posts > data/zachseward_blog.csv
```

Ergebnis:

|Title                                                    |Author     |URL                                                                                  |Date        |Description                                                   |
|---------------------------------------------------------|-----------|-------------------------------------------------------------------------------------|------------|--------------------------------------------------------------|
|My eulogy for Dad                                        |Zach Seward|https://www.zachseward.com/stephen-clark-seward/                                     |Jun 19, 2024|My eulogy for Dad                                             |
|AI is not like you and me                                |Zach Seward|https://www.zachseward.com/ai-is-not-a-person/                                       |May 2, 2024 |My talk at an Aspen Institute event                           |
|Creating structure with generative AI                    |Zach Seward|https://www.zachseward.com/creating-structure-with-generative-ai/                    |Apr 12, 2024|My talk at ISOJ 2024                                          |
|AI news that's fit to print                              |Zach Seward|https://www.zachseward.com/ai-news-thats-fit-to-print-sxsw-2024/                     |Mar 11, 2024|My talk at SXSW 2024                                          |
|Keeping score                                            |Zach Seward|https://www.zachseward.com/keeping-score/                                            |Aug 7, 2023 |With a stubby blue pencil, no eraser.                         |
|A few tactics that actually helped diversify our newsroom|Zach Seward|https://www.zachseward.com/a-few-tactics-that-actually-helped-diversify-our-newsroom/|Jul 26, 2023|This is is not a success story, but we did make some progress.|

## YouTube-Transkripte

_Fabric_ verfügt zudem über eine Integration von Funktionen, die Transkripte und Kommentare zu YouTube-Videos herunterladen.

Für dieses Beispiel muss ein API-Key für YouTube im Setup von _Fabric_ eingetragen werden.

Betrachten wir [dieses Video von Matthew Berman](https://www.youtube.com/watch?v=GwlRyItIopc&ab_channel=MatthewBerman): "Sam Altman Teases Orion (GPT-5), NotebookLM, Pixtral, Meta Training on Facebook Data" (17.09.2024), in dem über verschiedene Neuigkeiten aus dem Bereich der Künstlichen Intelligenz gesprochen wird.

```bash
fabric -y "https://www.youtube.com/watch?v=GwlRyItIopc&ab_channelMatthewBerman" --transcript --dry-run 
```
Lädt das Transkript zu dem Video herunter, verwendet es aber nicht (--dry-run) als Eingabe für ein Sprachmodell.

```bash
fabric -y "https://www.youtube.com/watch?v=GwlRyItIopc&ab_channelMatthewBerman" --comments --dry-run 
```
Lädt die Kommentare zu dem Video herunter, wiederum als _dry run_.

Um bspw. das Transkript weiterzuverarbeiten, kann es direkt im selben Aufruf von _Fabric_ mit einem Pattern verwendet werden.

Hier erzeugen wir mit dem eingebauten Pattern _create\_summary_ eine Zusammenfassung des Transkripts:

```bash
 fabric -y "https://www.youtube.com/watch?v=GwlRyItIopc&ab_channelMatthewBerman" --transcript --pattern create_summary
 ```

```markdown
# ONE SENTENCE SUMMARY:
Sam Altman's cryptic tweet hints at OpenAI's upcoming Orion model, while Microsoft revamps its AI co-pilot features across platforms.

# MAIN POINTS:
1. Sam Altman's tweet suggests a new AI model, possibly named Orion, coming soon.
2. Microsoft's co-pilot product is being revamped for better AI integration in Windows.
3. Co-pilot features include advanced functions in Excel, PowerPoint, and Outlook.
4. Meta allegedly trained its AI on publicly posted Facebook and Instagram data.
5. Mraw AI's new vision model, Pixol 12b, allows users to query images interactively.
6. E11, an open-source tool, simplifies prompt engineering for AI models.
7. Adobe announces a text-to-video model, Firefly, for commercial use.
8. Clara CEO is shutting down major SaaS providers, opting for AI-driven solutions.
9. Google Labs releases Notebook LM, converting documents into audio discussions.
10. The Godmother of AI launches World Labs, focusing on spatial AI development.

# TAKEAWAYS:
1. Expect OpenAI's Orion model release based on Altman's cryptic hints.
2. Enhanced AI features in Microsoft products aim to improve user experience.
3. Publicly available data on social media is being used for AI training.
4. New tools like E11 make prompt engineering more accessible and efficient.
5. The AI landscape is evolving, with companies exploring diverse applications and models.
```
Diese Zusammenfassung ist sicherlich nicht perfekt, aber sie ist hilfreich, um einen schnellen Überblick zu bekommmen und zu entscheiden, in welche Videos ich einen genaueren Blick werfen möchte. 

In diesem Sinne ermöglichet generative KI eine ganz neue Skalierung von Newsgathering- und Monitoring-Werkzeugen. (Siehe dazu auch [AI and News: What's next](https://generative-ai-newsroom.com/ai-and-news-whats-next-154fbeb6a646) von David Caswell)