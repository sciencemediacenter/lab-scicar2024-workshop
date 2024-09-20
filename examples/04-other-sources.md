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
## YouTube-Transkripte