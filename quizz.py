import marimo

__generated_with = "0.9.16"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md("""# Mines AP 2024-2025 Groupe 6 - Quizz 2""")
    return


@app.cell
def __(mo):
    mo.md("""## Question 1""")
    return


@app.cell
def __(mo):
    widget_1 = mo.ui.radio(
        options={"?": None, "0.12": "0.12", "0.91": "0.91", "1.0": "1.0", "Une erreur": "Une erreur"},
        value="?",
    )

    comments_1 = mo.ui.text_area(debounce=False)
    mo.md(f"""
    Qu'affiche le code Python suivant quand on l'exécute ?
    ```python
    scores = [0.12, 0.66, 0.45, 0.91, 0.77, 1.0]
    threshold = 0.90
    for score in scores:
        if score >= threshold:
            break
    print(score)
    ```

    {widget_1}

    Commentaires:

    {comments_1}
    """)
    return comments_1, widget_1


@app.cell
def __(mo):
    mo.md("""## Question 2""")
    return


@app.cell
def __(mo):
    widget_2 = mo.ui.text()

    comments_2 = mo.ui.text_area(debounce=False)

    mo.md(f"""
    Qu'affiche le code Python suivant quand on l'exécute ?

    ```python
    answer = None

    def set_answer():
        global answer
        answer = 42

    def print_answer():
        print(answer)

    set_answer()
    print_answer()
    ```


    Votre réponse :

    {widget_2}

    Commentaires:

    {comments_2}
    """)
    return comments_2, widget_2


@app.cell
def __(mo):
    mo.md("""## Question 3""")
    return


@app.cell
def __(mo):
    widget_3 = mo.ui.array([mo.ui.checkbox()] * 6)
    comments_3 = mo.ui.text_area(debounce=False)

    mo.md(
        f"""
    Le code Python

    ``` python
    c = 2.0 + 3.0j
    print(c.real, c.conjugate())
    ```

    s'exécute sans erreur et affiche `2.0 (2-3j)`. Parmi les assertions suivantes, lesquelles sont vraies ?

     - {widget_3[0]} `c in dir()`

     - {widget_3[1]} `"c" in dir()`

     - {widget_3[2]} `"c" in dir(c)`

     - {widget_3[3]} `"real" in dir(c)`

     - {widget_3[4]} `"conjugate" in dir(c)`

     - {widget_3[5]} `"conjugate()" in dir(c)`

    Commentaires :

    {comments_3}

    """
    )
    return comments_3, widget_3


@app.cell
def __(mo):
    widget_4 = mo.ui.text_area(debounce=False)
    comments_4 = mo.ui.text_area(debounce=False)


    mo.md(f"""## Question 4

    Dans le code Python

    ```python
    import pyxel

    def update():
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw():
        pyxel.cls(0)
        color = pyxel.frame_count % 16
        pyxel.text(56, 54, "Hello, Snake!", color)

    pyxel.init(160, 120)
    pyxel.run(update, draw)
    ```

    quels sont les types des variables globales `pyxel` et `update` et de la variable locale `color` ?

    Votre réponse :

    {widget_4}

    Commentaires :

    {comments_4}

    """)
    return comments_4, widget_4


@app.cell
def __(mo):
    widget_5 = mo.ui.array([mo.ui.checkbox()] * 4)
    comments_5 = mo.ui.text_area(debounce=False)


    mo.md(f"""## Question 5

    Si `l1 == [1, 2, 3]` et `l2 is l1` sont initialement vrais


     - {widget_5[0]} on a `l2 == l1`

     - {widget_5[1]} on a `id(l2) == id(l1)`

     - {widget_5[2]} on a `l1 is l2`

     - {widget_5[3]} si l'on exécute `l1 = [1, 2, 3, 4]`, on a alors `l2 == [1, 2, 3, 4]`

    Commentaires :

    {comments_5}


    """)
    return comments_5, widget_5


@app.cell
def __(mo):
    widget_6 = mo.ui.text()

    comments_6 = mo.ui.text_area(debounce=False)

    mo.md(f"""## Question 6

    Qu'affiche le code

    ```python
    for item in {{"a": 1, "b": 2, "c": 3}}:
        print(item)
    ```

    ?

    Votre réponse:

    {widget_6}

    Commentaires :

    {comments_6}

    """)
    return comments_6, widget_6


@app.cell
def __(mo):
    mo.md("""## Validation""")
    return


@app.cell
def __():
    import pprint
    import urllib
    return pprint, urllib


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def __(
    comments_1,
    comments_2,
    comments_3,
    comments_4,
    comments_5,
    comments_6,
    pprint,
    widget_1,
    widget_2,
    widget_3,
    widget_4,
    widget_5,
    widget_6,
):
    widgets = [widget_1, widget_2, widget_3, widget_4, widget_5, widget_6]
    comments = [comments_1, comments_2, comments_3, comments_4, comments_5, comments_6]
    answer = pprint.pformat([
        {f"Question {i+1}": widget.value, f"Comment {i+1}": comment.value} for i, (widget, comment) in enumerate(zip(widgets, comments))
    ], indent=4)
    return answer, comments, widgets


@app.cell
def __(mo):
    autosave = mo.ui.checkbox(label="autosave to answer.py", value=True)
    autosave
    return (autosave,)


@app.cell
def __(answer, autosave):
    if autosave.value:
        with open("answer.py", mode="tw", encoding="utf-8") as file:
            file.write(answer)
    return (file,)


@app.cell
def __(answer, mo, urllib):
    to = "Sebastien.Boisgerault@minesparis.psl.eu"
    subject = "Quizz AP #2"
    body = answer

    q = urllib.parse.quote


    mailto = f"mailto:{to}?subject={q(subject)}&body={q(body)}"


    mo.vstack(
        [
            mo.md(f"""
    Envoyez le texte suivant à {mo.icon('lucide:mail')} `Sebastien.Boisgerault@minesparis.psl.eu`
    ```python
    {answer}
    ```
    """),
            mo.Html(f"""
    <div>
      <style>
        #send {{
          text-decoration: none;
          background-color: #EEEEEE;
          color: #333333;
          padding: 2px 6px 2px 6px;
          border-top: 1px solid #CCCCCC;
          border-right: 1px solid #333333;
          border-bottom: 1px solid #333333;
          border-left: 1px solid #CCCCCC;
        }}
        </style>
        <a id="send" href="{mailto}">Envoyez votre réponse</a>
    <div>
    """),
        ]
    )
    return body, mailto, q, subject, to


if __name__ == "__main__":
    app.run()
