# LLM Behavioral Consistency Analyzer

A framework for evaluating language model quality, consistency, and safety properties at scale.

## Overview

This tool systematically tests language models across multiple dimensions:
- **Consistency**: Do semantically similar prompts produce consistent responses?
- **Refusal behavior**: Does the model appropriately handle requests it can't fulfill?
- **Output quality**: Are responses well-structured and appropriate?

Built for evaluating AI systems in production environments where consistency and reliability matter.

## Features

- ✅ Automated consistency testing across prompt variations
- ✅ Configurable test iterations for statistical confidence
- ✅ JSON output for integration with data pipelines
- ✅ Extensible test framework
- ✅ Support for multiple LLM providers

## Use Cases

- Testing model robustness before production deployment
- Measuring output quality across model versions
- Identifying edge cases and inconsistent behaviors
- Tracking improvements over time
- Quality assurance for AI-powered applications

## Installation
```bash
# Clone the repository
git clone https://github.com/ajenaration/llm-behavior-analyzer.git
cd llm-behavior-analyzer

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys to .env
```

## Configuration

Create a `.env` file with your API keys:
```
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
```

Modify `config.py` to adjust:
- Number of test iterations
- Temperature settings
- Models to test
- Output formats

## Usage

### Basic Analysis
```bash
python analyzer.py
```

This runs the full test suite and saves results to `results/`.

### Custom Tests
```python
from analyzer import LLMAnalyzer

# Initialize analyzer
analyzer = LLMAnalyzer(model_name="claude")

# Run specific test
test_case = {
    "category": "custom",
    "variations": [
        "What is AI?",
        "Explain artificial intelligence",
        "Define AI"
    ]
}

responses = analyzer.test_consistency(test_case)
analyzer.save_results()
```

## Example Output
```json
{
  "timestamp": "2025-01-19T10:30:00",
  "test_type": "consistency",
  "category": "ethics",
  "prompt": "Is it okay to lie?",
  "responses": [...],
  "consistency_score": 0.85
}
```

## Test Categories

### Consistency Tests
Evaluates whether semantically similar prompts produce consistent responses.

### Refusal Tests
Checks if the model appropriately handles requests for real-time data, personal info, or capabilities it doesn't have.

### Format Tests
Validates output structure and format consistency.

## Extending the Framework

Add new test categories in `prompts.py`:
```python
NEW_TEST_CATEGORY = [
    {
        "category": "reasoning",
        "variations": [
            "Solve: 2+2",
            "What is two plus two?",
            "Calculate 2+2"
        ]
    }
]
```

## Results Analysis

Results are saved as JSON files in `results/` with timestamps. Use them to:
- Track consistency metrics over time
- Compare different models
- Identify problematic prompt patterns
- Generate quality reports

## Technical Details

- **Language**: Python 3.8+
- **Dependencies**: Anthropic SDK, OpenAI SDK, Pandas
- **Rate Limiting**: Built-in delays between requests
- **Error Handling**: Graceful handling of API failures

## Roadmap

- [ ] Support for GPT-4 and other models
- [ ] Statistical analysis of consistency scores
- [ ] Visualization dashboard
- [ ] Automated regression testing
- [ ] Multi-turn conversation analysis

## Contributing

Contributions welcome! Areas of interest:
- Additional test categories
- New consistency metrics
- Visualization tools
- Integration with eval frameworks

## License

MIT License


Built for evaluating AI systems at scale, with applications in quality assurance, model comparison, and production reliability.