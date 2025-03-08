import matplotlib.pyplot as plt
import seaborn as sns

def plot_market_share(data):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Company', y='Market Share', data=data)
    plt.title('Market Share Distribution')
    plt.xlabel('Company')
    plt.ylabel('Market Share (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_growth_trends(data):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Year', y='Growth Rate', hue='Segment', data=data)
    plt.title('Growth Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate (%)')
    plt.legend(title='Customer Segment')
    plt.tight_layout()
    plt.show()

def plot_swot_analysis(swot_data):
    categories = ['Strengths', 'Weaknesses', 'Opportunities', 'Threats']
    plt.figure(figsize=(10, 6))
    for category in categories:
        plt.bar(category, len(swot_data[category]), label=category)
    plt.title('SWOT Analysis Overview')
    plt.xlabel('Categories')
    plt.ylabel('Number of Points')
    plt.legend()
    plt.tight_layout()
    plt.show()