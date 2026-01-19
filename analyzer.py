"""
LLM Behavior Analyzer - Main analysis logic
"""
import json
import time
from datetime import datetime
from pathlib import Path
from anthropic import Anthropic
import pandas as pd

import config
import prompts

class LLMAnalyzer:
    def __init__(self, model_name="claude"):
        """Initialize the analyzer with specified model"""
        self.model_name = model_name
        
        if model_name == "claude":
            if not config.ANTHROPIC_API_KEY:
                raise ValueError("ANTHROPIC_API_KEY not found in environment")
            self.client = Anthropic(api_key=config.ANTHROPIC_API_KEY)
            self.model = config.DEFAULT_MODELS["claude"]
        else:
            raise ValueError(f"Model {model_name} not yet supported")
        
        self.results = []
        
    def query_model(self, prompt, temperature=None):
        """Send a prompt to the model and return response"""
        temp = temperature or config.DEFAULT_TEMPERATURE
        
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=config.MAX_TOKENS,
                temperature=temp,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
        except Exception as e:
            return f"Error: {str(e)}"
    
    def test_consistency(self, test_case):
        """Test consistency across prompt variations"""
        category = test_case["category"]
        variations = test_case["variations"]
        
        print(f"\n{'='*60}")
        print(f"Testing consistency for: {category}")
        print(f"{'='*60}")
        
        responses = {}
        
        for variation in variations:
            print(f"\nPrompt: {variation}")
            
            # Test multiple times
            variation_responses = []
            for i in range(config.NUM_ITERATIONS):
                response = self.query_model(variation)
                variation_responses.append(response)
                print(f"  Iteration {i+1}: {response[:100]}...")
                time.sleep(1)  # Rate limiting
            
            responses[variation] = variation_responses
            
            # Store results
            self.results.append({
                "timestamp": datetime.now().isoformat(),
                "test_type": "consistency",
                "category": category,
                "prompt": variation,
                "responses": variation_responses,
                "num_iterations": len(variation_responses)
            })
        
        return responses
    
    def test_refusal_behavior(self):
        """Test how model handles requests it should refuse or clarify"""
        print(f"\n{'='*60}")
        print(f"Testing refusal behavior")
        print(f"{'='*60}")
        
        for prompt in prompts.REFUSAL_TESTS:
            print(f"\nPrompt: {prompt}")
            response = self.query_model(prompt)
            print(f"Response: {response[:200]}...")
            
            self.results.append({
                "timestamp": datetime.now().isoformat(),
                "test_type": "refusal",
                "prompt": prompt,
                "response": response
            })
            
            time.sleep(1)
    
    def analyze_consistency(self, responses):
        """Analyze how consistent responses are"""
        analysis = {}
        
        for prompt, response_list in responses.items():
            # Simple consistency metric: how similar are the responses?
            # For now, just count unique responses
            unique_responses = len(set(response_list))
            consistency_score = 1 - (unique_responses - 1) / len(response_list)
            
            analysis[prompt] = {
                "total_responses": len(response_list),
                "unique_responses": unique_responses,
                "consistency_score": consistency_score
            }
        
        return analysis
    
    def save_results(self):
        """Save results to JSON file"""
        timestamp = datetime.now().strftime(config.TIMESTAMP_FORMAT)
        filename = f"{config.RESULTS_DIR}/analysis_{timestamp}.json"
        
        Path(config.RESULTS_DIR).mkdir(exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n{'='*60}")
        print(f"Results saved to: {filename}")
        print(f"{'='*60}")
        
        return filename
    
    def run_full_analysis(self):
        """Run complete analysis suite"""
        print("Starting LLM Behavior Analysis")
        print(f"Model: {self.model}")
        print(f"Iterations per prompt: {config.NUM_ITERATIONS}")
        
        # Test 1: Consistency
        for test_case in prompts.CONSISTENCY_TESTS:
            responses = self.test_consistency(test_case)
            analysis = self.analyze_consistency(responses)
            
            print(f"\nConsistency Analysis for {test_case['category']}:")
            for prompt, metrics in analysis.items():
                print(f"  {prompt[:50]}...")
                print(f"    Consistency Score: {metrics['consistency_score']:.2f}")
                print(f"    Unique Responses: {metrics['unique_responses']}/{metrics['total_responses']}")
        
        # Test 2: Refusal behavior
        self.test_refusal_behavior()
        
        # Save all results
        self.save_results()
        
        print("\nAnalysis complete!")

def main():
    """Main entry point"""
    analyzer = LLMAnalyzer(model_name="claude")
    analyzer.run_full_analysis()

if __name__ == "__main__":
    main()