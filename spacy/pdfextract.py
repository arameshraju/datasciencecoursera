import spacy
from spacy_layout import spaCyLayout

nlp = spacy.blank("en")
layout = spaCyLayout(nlp)

# Process a document and create a spaCy Doc object
doc = layout("./AI.pdf")

# The text-based contents of the document
print(doc.text)
# Document layout including pages and page sizes
print(doc._.layout)
# Tables in the document and their extracted data
print(doc._.tables)
# Markdown representation of the document
print(doc._.markdown)

# Layout spans for different sections
for span in doc.spans["layout"]:
    # Document section and token and character offsets into the text
    print(span.text, span.start, span.end, span.start_char, span.end_char)
    # Section type, e.g. "text", "title", "section_header" etc.
    print(span.label_)
    # Layout features of the section, including bounding box
    print(span._.layout)
    # Closest heading to the span (accuracy depends on document structure)
    print(span._.heading)
