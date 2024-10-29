import plotly.graph_objects as go
import plotly.express as px


def my_plot_bar(df, x, y, text, color, labels: dict, titulo: str):

    fig = px.bar(df,
                 x=x,
                 y=y,
                 text=text,
                 color=color,
                 labels=labels,
                 title=titulo,

                 barmode='group',
                 height=800)
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    return fig
