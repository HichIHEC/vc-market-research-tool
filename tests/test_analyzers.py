import unittest
from src.analysis.startup_analyzer import StartupAnalyzer
from src.analysis.customer_analyzer import CustomerAnalyzer
from src.analysis.competitive_analyzer import CompetitiveAnalyzer
from src.analysis.market_sizer import MarketSizer

class TestStartupAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = StartupAnalyzer()

    def test_analyze_startup(self):
        description = "A tech startup focused on AI solutions for healthcare."
        result = self.analyzer.analyze(description)
        self.assertIn('primary_sector', result)
        self.assertIn('technology_stack', result)

class TestCustomerAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = CustomerAnalyzer()

    def test_profile_customers(self):
        startup_profile = {'primary_sector': 'Healthcare'}
        result = self.analyzer.profile_customers(startup_profile)
        self.assertIn('demographics', result)
        self.assertIn('psychographics', result)

class TestCompetitiveAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = CompetitiveAnalyzer()

    def test_map_competitors(self):
        startup_profile = {'primary_sector': 'Healthcare'}
        result = self.analyzer.map_competitors(startup_profile)
        self.assertIn('competitors', result)
        self.assertIn('SWOT_analysis', result)

class TestMarketSizer(unittest.TestCase):
    def setUp(self):
        self.sizer = MarketSizer()

    def test_calculate_market_size(self):
        data = {'industry': 'Healthcare', 'growth_rate': 0.05}
        result = self.sizer.calculate_market_size(data)
        self.assertIn('TAM', result)
        self.assertIn('SAM', result)
        self.assertIn('SOM', result)

if __name__ == '__main__':
    unittest.main()