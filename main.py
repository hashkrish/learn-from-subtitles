import MeCab
from pykakasi import kakasi


def tokenize_japanese_text(text):
    tagger = MeCab.Tagger()
    result = tagger.parse(text)
    lines = result.split("\n")
    tokens = []
    for line in lines[:-2]:
        surface, feature = line.split("\t")
        feature = feature
        tokens.append(surface)
    return tokens


def get_japanese_pronunciation(text):
    return kakasi().convert(text).pop()["hira"]


from jinja2 import Template

# Load the template from a file or as a string
template_string = """
<!DOCTYPE html>
<html>
<head>
    <title>Japanese Pronunciation</title>
    <style>
        body {
            /* dark mode */
            background-color: #1a1a1a;
            color: #fff;

        }
        .element {
            font-size: 16px;
            margin-bottom: 5px;
            display: inline-block;
            margin: 5px;
            padding: 5px;
            mouse: pointer;
        }
        .pronunciation {
            font-size: 12px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    {% for token, pronunciation in tokens_pronunciations %}
        <span class="element">
            <span class="pronunciation">
                {% if token.strip() != pronunciation.strip() %}
                    {{ pronunciation }}
                {% endif %}
            </span><br>
            {{ token }}
        </span>
    {% endfor %}
</body>
</html>
"""


def main():
    # Example usage
    text = "私は日本語を勉強しています。"

    tokens = tokenize_japanese_text(text)
    pronunciations = [get_japanese_pronunciation(token) for token in tokens]

    # for token, pronunciation in zip(tokens, pronunciations):
    #     print(f"Word: {token}\tPronunciation: {pronunciation}")

    template = Template(template_string)

    # Render the template with the provided data
    rendered_output = template.render(tokens_pronunciations=zip(tokens, pronunciations))

    # Save or display the rendered output as desired
    print(rendered_output)


if __name__ == "__main__":
    main()
