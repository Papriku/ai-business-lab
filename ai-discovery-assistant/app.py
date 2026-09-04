from src.discovery import analyze_request


business_request = input("Enter your business request: ")

analysis = analyze_request(business_request)

print("\nCLEAR:")
print(analysis.clear)

print("\nMISSING INFORMATION:")
print(analysis.missing_information)

print("\nDISCOVERY QUESTIONS:")
print(analysis.discovery_questions)

print("\nSUMMARY:")
print(analysis.summary)