# Fabric, Unix Style

>This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface. ([Basics of the Unix Philosophy](https://cscie2x.dce.harvard.edu/hw/ch01s06.html))

## Einleitende Beispiele

Siehe [Data Science at the Command Line](https://jeroenjanssens.com/dsatcl/)

### Welche Kapitel gibt es in  _Alice's Adventures in Wonderland_?

```bash
curl -s "https://www.gutenberg.org/files/11/11-0.txt" | grep " CHAPTER"
```

```
CHAPTER I.     Down the Rabbit-Hole
CHAPTER II.    The Pool of Tears
CHAPTER III.   A Caucus-Race and a Long Tale
CHAPTER IV.    The Rabbit Sends in a Little Bill
CHAPTER V.     Advice from a Caterpillar
CHAPTER VI.    Pig and Pepper
CHAPTER VII.   A Mad Tea-Party
CHAPTER VIII.  The Queen’s Croquet-Ground
CHAPTER IX.    The Mock Turtle’s Story
CHAPTER X.     The Lobster Quadrille
CHAPTER XI.    Who Stole the Tarts?
CHAPTER XII.   Alice’s Evidence
```

### Wie viele Kapitel gibt es?

```bash
curl -s "https://www.gutenberg.org/files/11/11-0.txt" | grep " CHAPTER" | wc -l
```

```
12
```

## Welche Weisheiten stecken in _Alice's Adventures in Wonderland_?

Siehe [_extract\_wisdom_-Pattern](https://github.com/danielmiessler/fabric/blob/main/patterns/extract_wisdom/system.md)

```bash
curl -s "https://www.gutenberg.org/files/11/11-0.txt" | fabric --pattern extract_wisdom > ../data/alice_wisdom.md
```
(Die Anfrage ist vergleichsweise "teuer" – wir wollen sie daher zwischenspeichern.)

```markdown
# SUMMARY
Lewis Carroll's "Alice's Adventures in Wonderland" follows Alice's whimsical journey through a fantastical world filled with peculiar characters and absurdity.

# IDEAS:
- Alice questions the value of a book without pictures or conversations.
- The White Rabbit symbolizes curiosity and the pursuit of knowledge.
- Falling down the rabbit hole represents entering a new realm of understanding.
- Alice’s musings highlight the absurdity of adult logic versus childlike wonder.
- The bottle labelled “Drink Me” reflects the theme of transformation.
- Alice's size changes illustrate the fluidity of identity and self-perception.
- The pool of tears demonstrates the consequences of emotional overwhelm.
- The Caucus Race satirizes the arbitrary nature of competition and social norms.
- The Hatter's riddle underscores the nature of language and meaning.
- The Queen's absurd orders reflect authoritarianism and the randomness of power.
- The Lobster Quadrille symbolizes the chaos of life’s experiences.
- The Mock Turtle's education critiques formal schooling and its absurdities.
- Alice's interactions with characters reveal her growth and resilience.
- The Cheshire Cat represents the importance of perspective and understanding.
- The trial scene critiques justice systems and their inherent absurdities.
- Alice’s assertion against the Queen highlights personal agency and defiance.
- The ending blurs the line between dream and reality, emphasizing subjective experience.
- The theme of identity permeates through Alice’s transformations.
- The narrative structure mirrors the nonsensical nature of dreams.
- Alice’s journey reflects the quest for self-discovery and meaning in chaos.

# INSIGHTS:
- Curiosity drives exploration and personal growth, essential for understanding oneself.
- Identity is fluid, shaped by experiences and perceptions rather than fixed traits.
- Absurdity in authority highlights the irrationality often found in societal structures.
- The blend of dream and reality emphasizes subjective interpretation of experiences.
- Personal agency empowers individuals to challenge societal norms and expectations.
- Transformation is a central theme, reflecting the complexities of growing up.
- Nonsense can reveal deeper truths about human nature and societal behavior.
- Language shapes our understanding of the world, yet can also obfuscate meaning.
- Emotional experiences can lead to significant personal change and reflection.
- The interplay of chaos and order mirrors the unpredictability of life itself.

# QUOTES:
- “What is the use of a book without pictures or conversations?”
- “Oh dear! Oh dear! I shall be late!”
- “How brave they’ll all think me at home!”
- “I wonder if I shall fall right through the earth!”
- “I wish I could shut up like a telescope!”
- “I’ll eat it, and if it makes me grow larger, I can reach the key.”
- “What a curious feeling!”
- “I can’t explain myself, I’m afraid, sir.”
- “I wish you wouldn’t squeeze so.”
- “You’re nothing but a pack of cards!”
- “You must be mad, or you wouldn’t have come here.”
- “I can’t help it; I’m growing.”
- “The best way to explain it is to do it.”
- “You are old, Father William.”
- “Why is a raven like a writing-desk?”
- “You might just as well say that ‘I see what I eat’ is the same thing as ‘I eat what I see’.”
- “What matters it how far we go?”
- “The more there is of mine, the less there is of yours.”
- “You are all pardoned.”
- “Will you, won’t you, will you join the dance?”

# HABITS:
- Alice engages in self-reflection, questioning her identity and surroundings.
- She practices curiosity by following the White Rabbit into the unknown.
- Alice maintains resilience despite the absurdity of her experiences.
- Observing characters, she learns about social dynamics and absurdity.
- She uses imagination to navigate challenges in Wonderland.
- Alice expresses her emotions openly, showcasing vulnerability.
- She practices adaptability by changing sizes and perspectives.
- Engaging with diverse characters fosters her understanding of identity.
- Alice's assertiveness in challenging authority reflects personal growth.
- She recalls childhood lessons, emphasizing the importance of knowledge.

# FACTS:
- The story critiques Victorian societal norms and their absurdities.
- Lewis Carroll originally wrote the story for children.
- The book was first published in 1865, gaining immense popularity.
- The character of the Cheshire Cat has become iconic in popular culture.
- Alice's Adventures serves as a precursor to modern fantasy literature.
- The narrative structure mirrors the illogical nature of dreams.
- Themes of identity and transformation resonate with psychological theories.
- The book has been adapted into numerous films, plays, and artworks.
- The concept of a “Caucus Race” satirizes political processes.
- The Mock Turtle’s education reflects critiques of formal schooling.

# REFERENCES:
- "Alice's Adventures in Wonderland" by Lewis Carroll.
- Various adaptations and illustrations of the book.
- Analysis of the themes and characters in literary critiques.
- Historical context of Victorian society and its influence on the narrative.
- Psychological interpretations of the characters and their journeys.

# RECOMMENDATIONS:
- Embrace curiosity as a pathway to self-discovery and learning.
- Reflect on personal identity and how it evolves through experiences.
- Find humor in absurdity to navigate life's challenges more easily.
- Engage with literature that challenges societal norms and expectations.
- Foster creativity through imaginative play and storytelling.
- Practice resilience in the face of uncertainty and change.
- Cultivate open-mindedness to appreciate diverse perspectives.
- Use language thoughtfully, understanding its power and limitations.
- Explore themes of childhood and growth in personal narratives.
- Encourage playful interactions with the world to enhance learning.
```