"""
LLM Behavior Analyzer - Now with personality! 🎮💪🍵

Added personal test cases for gaming, fitness, and tea to make evaluation
more engaging while demonstrating real-world LLM consistency challenges.
"""
import json
import time
from datetime import datetime
from pathlib import Path
from anthropic import Anthropic
import pandas as pd

import config
import prompts
import prompts_personal  # New import!

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
    
    def test_consistency(self, test_case, show_responses=True):
        """Test consistency across prompt variations"""
        category = test_case["category"]
        variations = test_case["variations"]
        
        print(f"\n{'='*60}")
        print(f"Testing: {category}")
        if "evaluation_criteria" in test_case:
            print(f"Criteria: {test_case['evaluation_criteria']}")
        print(f"{'='*60}")
        
        responses = {}
        
        for variation in variations:
            print(f"\n📝 Prompt: {variation}")
            
            # Test multiple times
            variation_responses = []
            for i in range(config.NUM_ITERATIONS):
                response = self.query_model(variation)
                variation_responses.append(response)
                
                if show_responses and i == 0:  # Show first response only
                    print(f"💬 Response: {response[:150]}...")
                
                time.sleep(1)  # Rate limiting
            
            responses[variation] = variation_responses
            
            # Store results
            self.results.append({
                "timestamp": datetime.now().isoformat(),
                "test_type": "consistency",
                "category": category,
                "prompt": variation,
                "responses": variation_responses,
                "num_iterations": len(variation_responses),
                "evaluation_criteria": test_case.get("evaluation_criteria", "")
            })
        
        return responses
    
    def test_refusal_behavior(self):
        """Test how model handles requests it should refuse or clarify"""
        print(f"\n{'='*60}")
        print(f"Testing refusal behavior")
        print(f"{'='*60}")
        
        for prompt in prompts.REFUSAL_TESTS:
            print(f"\n📝 Prompt: {prompt}")
            response = self.query_model(prompt)
            print(f"💬 Response: {response[:200]}...")
            
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
        print(f"✅ Results saved to: {filename}")
        print(f"{'='*60}")
        
        return filename
    
    def run_standard_analysis(self):
        """Run standard test suite"""
        print("\n🔬 STANDARD ANALYSIS")
        print("="*60)
        
        for test_case in prompts.CONSISTENCY_TESTS:
            responses = self.test_consistency(test_case)
            analysis = self.analyze_consistency(responses)
            
            print(f"\n📊 Consistency Analysis for {test_case['category']}:")
            for prompt, metrics in analysis.items():
                print(f"  • {prompt[:50]}...")
                print(f"    Consistency: {metrics['consistency_score']:.2%}")
                print(f"    Unique: {metrics['unique_responses']}/{metrics['total_responses']}")
    
    def run_personal_analysis(self):
        """Run personal interest-based tests"""
        print("\n\n🎮 PERSONAL ANALYSIS - Gaming, Fitness & Tea")
        print("="*60)
        print("Testing LLM consistency on topics I actually care about!")
        print("="*60)
        
        # Gaming tests
        print("\n\n🎮 GAMING TESTS (Valorant & Smash Bros)")
        for test_case in prompts_personal.GAMING_TESTS:
            responses = self.test_consistency(test_case)
            analysis = self.analyze_consistency(responses)
            
            avg_consistency = sum(m['consistency_score'] for m in analysis.values()) / len(analysis)
            print(f"\n📊 Average consistency for {test_case['category']}: {avg_consistency:.2%}")
        
        # Fitness tests
        print("\n\n💪 FITNESS TESTS (Strength Training)")
        for test_case in prompts_personal.FITNESS_TESTS:
            responses = self.test_consistency(test_case, show_responses=True)
            analysis = self.analyze_consistency(responses)
            
            avg_consistency = sum(m['consistency_score'] for m in analysis.values()) / len(analysis)
            print(f"\n📊 Average consistency for {test_case['category']}: {avg_consistency:.2%}")
        
        # Tea tests
        print("\n\n🍵 TEA TESTS (Tea Culture & Brewing)")
        for test_case in prompts_personal.TEA_TESTS:
            responses = self.test_consistency(test_case)
            analysis = self.analyze_consistency(responses)
            
            avg_consistency = sum(m['consistency_score'] for m in analysis.values()) / len(analysis)
            print(f"\n📊 Average consistency for {test_case['category']}: {avg_consistency:.2%}")
        
        # Crossover tests (the fun ones!)
        print("\n\n🔀 CROSSOVER TESTS (Interdisciplinary)")
        for test_case in prompts_personal.CROSSOVER_TESTS:
            responses = self.test_consistency(test_case, show_responses=True)
        
        # Safety tests
        print("\n\n🛡️ SAFETY TESTS (With Gaming/Fitness Context)")
        for test_case in prompts_personal.SAFETY_WITH_PERSONALITY:
            responses = self.test_consistency(test_case, show_responses=True)
    
    def run_full_analysis(self, include_personal=True):
        """Run complete analysis suite"""
        print("\n" + "="*60)
        print("🚀 LLM BEHAVIOR ANALYSIS")
        print("="*60)
        print(f"Model: {self.model}")
        print(f"Iterations per prompt: {config.NUM_ITERATIONS}")
        print(f"Testing both standard and personal categories")
        
        # Standard tests
        self.run_standard_analysis()
        self.test_refusal_behavior()
        
        # Personal tests (the cool part!)
        if include_personal:
            self.run_personal_analysis()
        
        # Save all results
        self.save_results()
        
        # Summary
        print("\n\n" + "="*60)
        print("✨ ANALYSIS COMPLETE!")
        print("="*60)
        
        test_summary = prompts_personal.get_personal_test_summary()
        print("\n📊 Tests Run:")
        for category, count in test_summary.items():
            print(f"  • {category}: {count} test cases")
        
        print(f"\n💾 Total results: {len(self.results)} data points")
        print("\n🎯 Key Insight: Testing LLM consistency on real-world topics")
        print("   (gaming, fitness, tea) reveals how models handle domain-specific advice.")

def main():
    """Main entry point"""
    print("🎮💪🍵 LLM Behavior Analyzer - Personal Edition")
    print("Testing AI consistency on topics that actually matter!\n")
    
    analyzer = LLMAnalyzer(model_name="claude")
    analyzer.run_full_analysis(include_personal=True)
    
    print("\n👋 Want to run specific categories?")
    print("   gaming_only = LLMAnalyzer()")
    print("   gaming_only.run_personal_analysis()")

if __name__ == "__main__":
    main()