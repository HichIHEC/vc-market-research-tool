import gradio as gr
from analysis.startup_analyzer import StartupAnalyzer
from analysis.customer_analyzer import CustomerAnalyzer
from analysis.competitive_analyzer import CompetitiveAnalyzer
from analysis.market_sizer import MarketSizer

class GradioApp:
    def __init__(self):
        self.startup_analyzer = StartupAnalyzer()
        self.customer_analyzer = CustomerAnalyzer()
        self.competitive_analyzer = CompetitiveAnalyzer()
        self.market_sizer = MarketSizer()

    def analyze_startup(self, startup_description):
        return self.startup_analyzer.analyze(startup_description)

    def analyze_customer(self, customer_data):
        return self.customer_analyzer.profile(customer_data)

    def analyze_competition(self, competition_data):
        return self.competitive_analyzer.map_competition(competition_data)

    def size_market(self, market_data):
        return self.market_sizer.size_market(market_data)

    def launch_interface(self):
        with gr.Blocks() as demo:
            gr.Markdown("## AI-Powered Venture Capital Market Research Tool")
            with gr.Tab("Startup Analysis"):
                startup_input = gr.Textbox(label="Startup Description")
                startup_output = gr.JSON(label="Startup Profile")
                startup_button = gr.Button("Analyze")
                startup_button.click(self.analyze_startup, inputs=startup_input, outputs=startup_output)

            with gr.Tab("Customer Analysis"):
                customer_input = gr.Textbox(label="Customer Data")
                customer_output = gr.JSON(label="Customer Profile")
                customer_button = gr.Button("Analyze")
                customer_button.click(self.analyze_customer, inputs=customer_input, outputs=customer_output)

            with gr.Tab("Competitive Analysis"):
                competition_input = gr.Textbox(label="Competition Data")
                competition_output = gr.JSON(label="Competitive Landscape")
                competition_button = gr.Button("Analyze")
                competition_button.click(self.analyze_competition, inputs=competition_input, outputs=competition_output)

            with gr.Tab("Market Sizing"):
                market_input = gr.Textbox(label="Market Data")
                market_output = gr.JSON(label="Market Size Estimates")
                market_button = gr.Button("Size Market")
                market_button.click(self.size_market, inputs=market_input, outputs=market_output)

        demo.launch()

if __name__ == "__main__":
    app = GradioApp()
    app.launch_interface()