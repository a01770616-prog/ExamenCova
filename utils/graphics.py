import plotly.express as px

def scatter_avance_presupuesto(df):
    
    fig = px.scatter(
        df,
        x="BudgetThousands",
        y="PercentComplete",
        color="State",
        hover_data=["ProjectName", "Manager"],
        title="Avance vs Presupuesto (k$)",
        labels=["BudgetThousands","PercentComplete"]
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        legend_title_text="State",
    )

    return fig
