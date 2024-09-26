# Ein Ausblick auf _instructor_ für strukturierte Ausgaben von LLM

[Instructor](https://python.useinstructor.com/)

> Instructor makes it easy to get structured data like JSON from LLMs like GPT-3.5, GPT-4, GPT-4-Vision, and open-source models including Mistral/Mixtral, Anyscale, Ollama, and llama-cpp-python. 

> It stands out for its simplicity, transparency, and user-centric design, built on top of Pydantic. Instructor helps you manage validation context, retries with Tenacity, and streaming Lists and Partial responses.

Instructor erlaubt die Definiton von (komplexen) Schemata und Validierungsregeln mit Pydantic. Im Hintergrund kümmert sich Instructor um die Übermittlung des Schemas an die API des gewählten Anbieters und nutzt dabei die jeweilis unterstützen Verfahren, gute strukturierte Outputs zu erzeugen (Function Calling, Structured Ouputs, ...).

## Einfache Beispiele

### basic_example.py

Strukturierte Information über einen Benutzer (Name und Alter) wird aus einer User-Nachricht extrahiert.

## extracting_receipts.py

Extrahiert Liste von Einzelposten und die Gesamtsumme einer Rechnung. Validiert ob die Summe der extrahierten Einzelposten mit der extrahierten Gesamtsumme übereinstimmt.

![Rechnung](img/receipt-ocr-original.jpg)

===>

```python
Receipt(
    items=[
        Item(
            name='PET TOY',
            price=1.97,
            quantity=1,
        ),
        Item(
            name='FLOPPY PUPPY',
            price=1.97,
            quantity=1,
        ),
        Item(
            name='SSSUPREME',
            price=4.97,
            quantity=1,
        ),
        Item(
            name='2.5 SQUEAK',
            price=5.92,
            quantity=1,
        ),
        Item(
            name='MUNCHY DMBEL',
            price=3.77,
            quantity=1,
        ),
        Item(
            name='DOG TREAT',
            price=2.92,
            quantity=1,
        ),
        Item(
            name='PED PCH',
            price=0.5,
            quantity=1,
        ),
        Item(
            name='PED PCH',
            price=0.5,
            quantity=1,
        ),
        Item(
            name='HNYMD SMORES',
            price=3.98,
            quantity=1,
        ),
        Item(
            name='FRENCH DRSNG',
            price=1.98,
            quantity=1,
        ),
        Item(
            name='3 ORANGES',
            price=5.47,
            quantity=1,
        ),
        Item(
            name='BABY CARROTS',
            price=1.48,
            quantity=1,
        ),
        Item(
            name='COLLARDS',
            price=2.5,
            quantity=1,
        ),
        Item(
            name='CALZONE',
            price=2.5,
            quantity=1,
        ),
        Item(
            name='MM RVW MNT',
            price=19.77,
            quantity=1,
        ),
        Item(
            name='STKOBRLPLABL',
            price=1.97,
            quantity=1,
        ),
        Item(
            name='STKOBRLPLABL',
            price=1.97,
            quantity=1,
        ),
        Item(
            name='STKO SUNFLWR',
            price=0.97,
            quantity=1,
        ),
        Item(
            name='STKO SUNFLWR',
            price=0.97,
            quantity=1,
        ),
        Item(
            name='STKO SUNFLWR',
            price=0.97,
            quantity=1,
        ),
        Item(
            name='STKO SUNFLWR',
            price=0.97,
            quantity=1,
        ),
        Item(
            name='BLING BEADS',
            price=0.99,
            quantity=1,
        ),
        Item(
            name='GREAT VALUE',
            price=9.97,
            quantity=1,
        ),
        Item(
            name='LIPTON',
            price=4.48,
            quantity=1,
        ),
        Item(
            name='DRY DOG',
            price=12.44,
            quantity=1,
        ),
    ],
    total=98.21,
)
```

## Ausblick: es darf komplex werden ...

- Siehe Vikram Oberois Arbeiten, Protokolle des New York City Council aufzubereiten:
    - [Talk](https://nycsodata24.sched.com/event/1aiLm/how-i-use-ai-to-make-it-easy-to-navigate-city-council-meetings), NYC School of Data
    - [Prompts und Schemata](https://gist.github.com/voberoi/cfeb935b163c150eee5d7c86e7fb4337)