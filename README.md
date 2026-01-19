# LLM Behavioral Consistency Analyzer

A framework for evaluating language model quality, consistency, and safety properties at scale—tested on both standard benchmarks and real-world topics I actually care about.

## Overview

This tool systematically tests language models to answer: **"Does the AI give consistent, quality advice across different phrasings?"** This project serves as practice for the Anthropic Fellowship

Built for practical evaluation scenarios like:
- Does Claude give consistent Valorant agent recommendations?
- Will GPT recommend safe strength training progressions?
- Can AI maintain consistency when explaining tea brew methods?

## Why This Matters

LLMs are only useful if they're **consistent** and **reliable**. This framework measures both:
- **Standard tests**: Ethics, safety, technical knowledge
- **Domain-specific tests**: Gaming (Valorant/Super Smash Bros Ultimate), fitness, and tea culture
- **Safety tests**: Refusal behavior, harmful advice detection
- **Crossover tests**: Interdisciplinary connections

## Real-World Test Categories

### Gaming
- **Valorant strategy**: Agent recommendations for beginners
- **Smash Bros fundamentals**: Core skills and improvement
- **Competitive mindset**: Handling ranked scenarios

### Strength Training
- **Beginner programs**: Safe, effective starting points
- **Progressive overload**: Building strength over time
- **Recovery**: Rest periods and muscle recovery

### Tea Culture
- **Brewing techniques**: Optimal temps and steep times
- **Tea recommendations**: Productivity, focus, relaxation
- **Tea processing**: Green, black, oolong differences

### Crossover Tests
- Gaming skills vs. strength training parallels
- Best tea for gaming sessions or workouts
- Mental models that apply across domains

## Installation

```bash
# Clone the repository
git clone https://github.com/ajenaration/llm-behavior-analyzer.git
cd llm-behavior-analyzer

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
```

### Getting Your Free API Key

**Anthropic Claude (Recommended):**
1. Go to https://console.anthropic.com
2. Sign up (free) and get $5 in free credits (~2,500 API calls)
3. Create an API key
4. Add to `.env` file


## Quick Start

### Run Full Analysis

```bash
python analyzer.py
```

This runs both standard and personal test suites (~15 minutes).

### Run Specific Categories

```python
from analyzer import LLMAnalyzer
import prompts_personal

analyzer = LLMAnalyzer()

# Gaming tests only
for test in prompts_personal.GAMING_TESTS:
    responses = analyzer.test_consistency(test)

# Fitness tests only
for test in prompts_personal.FITNESS_TESTS:
    responses = analyzer.test_consistency(test)

analyzer.save_results()
```

## Example Output

```
GAMING TESTS (Valorant & Smash Bros)
============================================================
Testing: valorant_strategy
Criteria: Should consistently recommend similar beginner agents

Prompt: What are the best Valorant agents for beginners?
Response: For beginners, I'd recommend starting with agents like
    Sage (healing and crowd control), Brimstone (straightforward
    smokes), or Reyna (self-sufficient duelist)...

Average consistency for valorant_strategy: 85.00%
```

## Configuration

Adjust test parameters in `config.py`:

```python
NUM_ITERATIONS = 5  # Tests per prompt variation
DEFAULT_TEMPERATURE = 0.7  # Response randomness
MAX_TOKENS = 1000  # Response length
```


## Use Cases

**For Developers:**
- Quality assurance before production deployment
- Regression testing across model versions
- Identifying inconsistent behaviors

**For Researchers:**
- Measuring LLM consistency across domains
- Comparing different models
- Studying prompt sensitivity

**For Fun:**
- See how well AI understands your hobbies
- Test if LLMs give good gaming/fitness/tea advice
- Experiment with creative crossover questions

## Technical Details

- **Language**: Python 3.8+
- **Primary Model**: Claude (Anthropic)
- **Rate Limiting**: 1-second delays between requests
- **Output Format**: JSON with timestamps and metadata

## Key Findings

Some interesting patterns discovered:

1. **Gaming advice** tends to be highly consistent across phrasings
2. **Fitness recommendations** show more variation (context-dependent)
3. **Tea knowledge** is surprisingly consistent (well-documented domain)
4. **Crossover questions** reveal creative reasoning abilities
5. **Safety refusals** are consistent

## Roadmap

- [ ] Multi-model comparison (Claude vs GPT vs Gemini)
- [ ] Statistical significance testing
- [ ] Visualization dashboard
- [ ] More personal test categories (music, cooking, etc.)
- [ ] Automated quality scoring
- [ ] Integration with evaluation frameworks

## Why I Built This

I wanted to test if LLMs could give consistent advice on topics I care about. Turns out, measuring "consistency" is harder than it looks and is super important for real-world AI applications. This puts things in perspective as a stepping stone for the Anthropic AI Fellowship.

This project combines:
- My interest in AI safety and evaluation
- Practical testing of real-world use cases
- Making technical work more engaging and fun


**Areas of interest:**
- Domain-specific test cases (sports, hobbies, skills)
- Better consistency metrics
- Visualization tools
- Multi-turn conversation testing


*Built for evaluating AI systems at scale, with applications in quality assurance, model comparison, and production reliability. Also for settling debates about whether Claude or GPT gives better Valorant advice.* 


# Future Updates if Admitted to Fellowship 
Add interactive CLI
Comparison mode to different models
Add visualization with matlab or Python's `matplotlib`