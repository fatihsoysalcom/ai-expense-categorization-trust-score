import re

def categorize_expense(description: str) -> dict:
    """
    Simulates an AI agent categorizing an expense and providing a confidence score.
    This simplified version uses keyword matching to demonstrate the concept of
    categorization and transparency (confidence/justification), crucial for trust.
    """
    description_lower = description.lower()
    
    # Define categories and associated keywords
    categories = {
        "Food & Beverage": ["coffee", "restaurant", "lunch", "dinner", "cafe", "food", "snack", "meal"],
        "Travel": ["taxi", "flight", "hotel", "uber", "airport", "travel", "bus", "train", "mileage"],
        "Software & Cloud": ["software", "license", "cloud", "aws", "azure", "google cloud", "subscription", "saas", "platform"],
        "Office Supplies": ["stapler", "pen", "paper", "office supply", "printer", "ink", "stationery"],
        "Utilities": ["electricity", "water", "internet", "gas", "utility bill"],
        "Marketing": ["advertisement", "campaign", "marketing", "promo", "social media"],
        "Consulting Services": ["consulting", "advisor", "service fee", "professional fee"]
    }

    best_category = "Miscellaneous"
    highest_confidence = 0.0
    justification = "No specific keywords matched any predefined category."

    # Iterate through categories to find the best match
    for category, keywords in categories.items():
        matches = []
        for keyword in keywords:
            # Use regex for whole word matching to avoid partial matches (e.g., 'car' in 'card')
            if re.search(r'\b' + re.escape(keyword) + r'\b', description_lower):
                matches.append(keyword)
        
        # Simple confidence calculation: more keyword matches = higher confidence
        # This simulates how an AI might derive certainty from data points.
        current_confidence = len(matches) * 0.25 # Each match adds 25% confidence
        if current_confidence > 1.0:
            current_confidence = 1.0 # Cap at 100%

        if current_confidence > highest_confidence:
            highest_confidence = current_confidence
            best_category = category
            if matches:
                # Providing a justification helps build trust in the AI's decision.
                justification = f"Matched keywords: {', '.join(matches)}"
            else:
                # Fallback justification, though with current logic, matches should exist if confidence > 0
                justification = f"Strongest match based on general context for {category}."
        # In a real AI, tie-breaking or multi-category assignments would be more complex.

    # If no keywords matched any specific category, it remains Miscellaneous with low confidence
    if highest_confidence == 0.0:
        best_category = "Miscellaneous"
        justification = "No specific keywords found for any predefined category."
        highest_confidence = 0.1 # Assign a base low confidence for miscellaneous items

    return {
        "description": description,
        "predicted_category": best_category,
        "confidence": round(highest_confidence, 2), # Round for cleaner output
        "justification": justification # Provides transparency for the decision, fostering trust
    }

# --- Sample Expense Data ---
sample_expenses = [
    "Starbucks Coffee for client meeting",
    "Amazon Web Services monthly bill",
    "Taxi ride to airport for business trip",
    "New pens and notebooks for office",
    "Lunch at 'The Bistro'",
    "Monthly internet bill",
    "Flight ticket to Istanbul",
    "Subscription for design software",
    "Parking fee",
    "Dinner with team at Italian restaurant",
    "Electricity bill for office",
    "Consulting services fee for Q3 report",
    "Google Ads campaign budget",
    "Car mileage reimbursement"
]

print("--- AI Expense Categorization Simulation ---")
print("This script demonstrates how an AI might categorize expenses and provide")
print("a 'confidence score' and 'justification' to build trust in its decisions,")
print("a key aspect of AI-powered financial management.
")

for expense_desc in sample_expenses:
    result = categorize_expense(expense_desc)
    print(f"Expense: '{result['description']}'")
    print(f"  Category: {result['predicted_category']}")
    print(f"  Confidence: {result['confidence']:.0%}") # Format as percentage
    print(f"  Justification: {result['justification']}
")

print("------------------------------------------")
print("Note: This is a simplified rule-based system. Real AI models use")
print("machine learning for more sophisticated and adaptive categorization.")
