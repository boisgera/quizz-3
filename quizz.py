import marimo

__generated_with = "0.9.16"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md("""# Mines AP 2024-2025 Groupe 6 - Quizz 3""")
    return


@app.cell
def __(mo):
    mo.md("""## Question 1""")
    return


@app.cell(hide_code=True)
def __(mo):
    widget_1 = mo.ui.radio(
        options={"None": None, "0": "0", "7": "7", "15": "15"},
        value=None,
    )

    comments_1 = mo.ui.text_area(debounce=False)
    mo.md(f'''
    Quelle est la valeur de `s` à l'issue de l'exécution de ce code?
    ```python
    d = {{"a": 1, "b": 2, "d": 4}}
    s = 0
    for key in ["a", "b", "c", "d", "e", "f"]:
        s = s + d.get(key, 0)
    ```

    {widget_1}

    Commentaires:

    {comments_1}
    ''')
    return comments_1, widget_1


@app.cell
def __(mo):
    mo.md("""## Question 2""")
    return


app._unparsable_cell(
    r"""
    widget_2 = mo.ui.code_editor(value='''\
    objects = [None, 1, 2.0, 3.0+0j, \"quatre\"]
    hashes = {{hash(obj) % 2**8 for obj in objects}}\
    ''')

    comments_2 = mo.ui.text_area(debounce=False)

    mo.md(f'''
    Réécrire le code suivant sans utiliser de \"set comprehension\" (notation \"set-builder\")

    ```python
    objects = [None, 1, 2.0, 3.0+0j, \"quatre\"]
    hashes = {hash(obj) % 2**8 for obj in objects}
    ```

    Votre réponse:
    {widget_2}

    Commentaires:

    {comments_2}
    ''')
    """,
    name="__",
    column=None, disabled=False, hide_code=True
)


@app.cell
def __(mo):
    mo.md("""## Question 3""")
    return


@app.cell(hide_code=True)
def __(mo):
    widget_3 = mo.ui.array([mo.ui.checkbox()] * 6)
    comments_3 = mo.ui.text_area(debounce=False)

    mo.md(
        f"""
    Sélectionnez les expressions qui correspondent à des dictionnaires valides.

     - {widget_3[0]} `{{}}`

     - {widget_3[1]} `{{"a": 1, "b": 2, "c": 3}}`

     - {widget_3[2]} `{{1: ["one", "un"], 2: ["two", "deux"], 3: ["three", "trois"]}}`

     - {widget_3[3]} `{{n: str(n) for n in range(10)}}`

     - {widget_3[4]} `{{[]: 0, [0]: 1, [0, 1]: 2}}`

     - {widget_3[5]} `{{False: 0, True: 1}}`

    Commentaires :

    {comments_3}

    """
    )
    return comments_3, widget_3


@app.cell
def __(mo):
    widget_4 = mo.ui.array([mo.ui.checkbox()] * 6)
    comments_4 = mo.ui.text_area(debounce=False)


    mo.md(f"""## Question 4

    Un graphique extrait de la spécification JSON:

    ![](https://www.json.org/img/number.png)

    Sélectionnez les chaînes de caractères `number_json` qui sont des représentations valides de nombres en JSON 
    (c'est-à-dire qui ne vont pas générer d'erreur quand on va exécuter `number = json.loads(number_json))`)

     - {widget_4[0]} `number_json = "-0"`

     - {widget_4[1]} `number_json = "1_000"`

     - {widget_4[2]} `number_json = "0e23"`

     - {widget_4[3]} `number_json = "inf"`

     - {widget_4[4]} `number_json = "42"`

     - {widget_4[5]} `number_json = "007"`

    Commentaires :

    {comments_4}

    """)
    return comments_4, widget_4


@app.cell
def __(mo):
    widget_5 = mo.ui.array([mo.ui.checkbox()] * 4)
    comments_5 = mo.ui.text_area(debounce=False)


    mo.md(f"""## Question 5

    Supposons que `s1 = {{"a", "b", "c"}}` et `s2 = {{"c", "b", "a"}}`. Alors

     - {widget_5[0]} on a `s2 == s1`

     - {widget_5[1]} on a `s1 | s2 == s1`

     - {widget_5[2]} on a `s1 - s2 == s1`

     - {widget_5[3]} on a `set(list(s1) + list(s1)) == s1`

    Commentaires :

    {comments_5}


    """)
    return comments_5, widget_5


@app.cell
def __(mo):
    widget_6 = mo.ui.code_editor(value='''NAMES = ["Aaron", "Abel", "Abigaël", "Abraham", ...] # The real list is much longer

    def is_classic_name(name):
        """
        Returns True if name belongs to the list of known names, False otherwise.
        """  
        return name in NAMES''')

    comments_6 = mo.ui.text_area(debounce=False)

    mo.md(f'''## Question 6


    Comment modiferiez-vous le code suivant pour que l'usage de la fonction `is_classic_name` soit plus performant ?

    ```python
    NAMES = ["Aaron", "Abel", "Abigaël", "Abraham", ...] # The real list is much longer

    def is_classic_name(name):
        """
        Returns True if name belongs to the list of known names, False otherwise.
        """  
        return name in NAMES
    ```

    Votre réponse:

    {widget_6}

    Commentaires :

    {comments_6}

    ''')
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
    autosave = mo.ui.checkbox(label="Sauvegarde automatique dans le fichier answer.py", value=True)
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
    subject = "Quizz AP #3"
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
