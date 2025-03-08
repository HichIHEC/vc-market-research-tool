Sure, here's the contents for the file: /vc-market-research-tool/vc-market-research-tool/setup.py

from setuptools import setup, find_packages

setup(
    name='vc-market-research-tool',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='AI-powered market research tool for analyzing startup investment opportunities.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'gradio',
        'numpy',
        'pandas',
        'matplotlib',
        'scikit-learn',
        'torch',  # Include if using PyTorch for models
        'transformers',  # Include if using Hugging Face Transformers
        'pdfkit',  # For PDF report generation
        'beautifulsoup4',  # For web scraping if needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)