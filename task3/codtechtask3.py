import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load dataset
df = pd.read_csv("Maths.csv")

# Create Dash app
app = dash.Dash(__name__)
app.title = "Student Performance Dashboard"

# Layout
app.layout = html.Div([
    html.H1("Student Performance Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.Label("Select Gender:"),
        dcc.Dropdown(
            id="gender-filter",
            options=[
                {"label": "All", "value": "All"},
                {"label": "Male", "value": "M"},
                {"label": "Female", "value": "F"}
            ],
            value="All",
            clearable=False
        )
    ], style={"width": "30%", "margin": "auto"}),

    html.Br(),

    dcc.Graph(id="grade-distribution"),
    dcc.Graph(id="studytime-vs-grade"),
    dcc.Graph(id="absences-vs-grade")
])

# Callback
@app.callback(
    Output("grade-distribution", "figure"),
    Output("studytime-vs-grade", "figure"),
    Output("absences-vs-grade", "figure"),
    Input("gender-filter", "value")
)
def update_charts(gender):
    if gender == "All":
        filtered_df = df
    else:
        filtered_df = df[df["sex"] == gender]

    fig1 = px.histogram(
        filtered_df, x="G3", nbins=20,
        title="Final Grade Distribution"
    )

    fig2 = px.scatter(
        filtered_df, x="studytime", y="G3",
        title="Study Time vs Final Grade"
    )

    fig3 = px.scatter(
        filtered_df, x="absences", y="G3",
        title="Absences vs Final Grade"
    )

    return fig1, fig2, fig3


# Run server (VS Code / Local)
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8050, debug=True)