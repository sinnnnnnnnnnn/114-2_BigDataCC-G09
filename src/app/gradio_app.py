from __future__ import annotations

import os

import gradio as gr

from src.analysis.analyze_data import (
    build_insights,
    filter_records,
    kpi_summary,
    plot_metric,
    port_performance,
    route_performance,
)
from src.analysis.clean_data import clean_shipping_data
from src.utils.data_loader import load_uploaded_csv


DEFAULT_FILTERS = {
    "port": "All",
    "route": "All",
    "vessel_type": "All",
    "min_cargo_teu": 0,
    "metric": "turnaround_hours",
    "chart_type": "Trend Line Chart",
}


def _choices(df, column: str) -> list[str]:
    return ["All"] + sorted(df[column].dropna().astype(str).unique().tolist())


def load_dataset(file_obj):
    file_path = getattr(file_obj, "name", None) if file_obj is not None else None
    raw_df = load_uploaded_csv(file_path)
    result = clean_shipping_data(raw_df)
    cleaned = result.cleaned
    max_cargo = int(cleaned["cargo_teu"].max()) if not cleaned.empty else 0
    status = "\n".join([f"- {issue}" for issue in result.issues])
    if result.output_path:
        status += f"\n- 已輸出清洗檔案：{result.output_path}"

    return (
        cleaned,
        raw_df.head(12),
        cleaned.head(12),
        status,
        gr.update(choices=_choices(cleaned, "port_name"), value="All"),
        gr.update(choices=_choices(cleaned, "route"), value="All"),
        gr.update(choices=_choices(cleaned, "vessel_type"), value="All"),
        gr.update(maximum=max(max_cargo, 1), value=0),
    )


def run_analysis(cleaned_df, port, route, vessel_type, min_cargo_teu, metric, chart_type):
    if cleaned_df is None or len(cleaned_df) == 0:
        _, raw_preview, cleaned_preview, status, *_ = load_dataset(None)
        cleaned_df = cleaned_preview

    filtered = filter_records(cleaned_df, port, route, vessel_type, int(min_cargo_teu))
    fig = plot_metric(filtered, metric, chart_type)
    return (
        kpi_summary(filtered),
        port_performance(filtered),
        route_performance(filtered),
        filtered.head(30),
        fig,
        build_insights(filtered),
    )


def build_app() -> gr.Blocks:
    with gr.Blocks(title="Shipping & Port Logistics Dashboard") as demo:
        cleaned_state = gr.State()

        gr.Markdown(
            """
            # 航運資料儀表板
            以 Gradio 整合航運 CSV 清洗、港口 KPI 分析與 Matplotlib 視覺化，支援內建資料與自訂 CSV 上傳。
            """
        )

        with gr.Row():
            with gr.Column(scale=1, min_width=280):
                csv_file = gr.File(label="上傳航運 CSV", file_types=[".csv"])
                load_button = gr.Button("Load / Clean Dataset", variant="primary")
                port = gr.Dropdown(label="港口", choices=["All"], value="All")
                route = gr.Dropdown(label="航線", choices=["All"], value="All")
                vessel_type = gr.Dropdown(label="船舶類型", choices=["All"], value="All")
                min_cargo_teu = gr.Slider(
                    label="最低貨櫃量 TEU",
                    minimum=0,
                    maximum=1,
                    value=0,
                    step=100,
                )
                metric = gr.Dropdown(
                    label="分析指標",
                    choices=["turnaround_hours", "cargo_teu", "avg_speed_knots", "delay_rate"],
                    value=DEFAULT_FILTERS["metric"],
                )
                chart_type = gr.Radio(
                    label="圖表類型",
                    choices=["Trend Line Chart", "Port Average Bar Chart", "Route Average Bar Chart"],
                    value=DEFAULT_FILTERS["chart_type"],
                )
                analyze_button = gr.Button("Execute Logistics Analysis", variant="primary")
                cleaning_log = gr.Markdown(label="清洗紀錄")

            with gr.Column(scale=2):
                insight = gr.Markdown()
                kpis = gr.Dataframe(label="KPI Summary", interactive=False)
                chart = gr.Plot(label="Visualization")

        with gr.Tab("Raw Data View"):
            raw_preview = gr.Dataframe(label="Raw Preview", interactive=False)
        with gr.Tab("Cleaned Data View"):
            cleaned_preview = gr.Dataframe(label="Cleaned Preview", interactive=False)
        with gr.Tab("Port Performance"):
            port_table = gr.Dataframe(label="Port Performance", interactive=False)
        with gr.Tab("Route Performance"):
            route_table = gr.Dataframe(label="Route Performance", interactive=False)
        with gr.Tab("Filtered Records"):
            filtered_preview = gr.Dataframe(label="Filtered Records", interactive=False)

        load_outputs = [
            cleaned_state,
            raw_preview,
            cleaned_preview,
            cleaning_log,
            port,
            route,
            vessel_type,
            min_cargo_teu,
        ]
        load_button.click(load_dataset, inputs=[csv_file], outputs=load_outputs)
        demo.load(load_dataset, inputs=[csv_file], outputs=load_outputs).then(
            run_analysis,
            inputs=[cleaned_state, port, route, vessel_type, min_cargo_teu, metric, chart_type],
            outputs=[kpis, port_table, route_table, filtered_preview, chart, insight],
        )
        analyze_button.click(
            run_analysis,
            inputs=[cleaned_state, port, route, vessel_type, min_cargo_teu, metric, chart_type],
            outputs=[kpis, port_table, route_table, filtered_preview, chart, insight],
        )

    return demo


if __name__ == "__main__":
    port = int(os.getenv("GRADIO_SERVER_PORT", "8080"))
    build_app().launch(server_name="0.0.0.0", server_port=port)
