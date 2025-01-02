
# Category mapping for variables
category_mapping = {
    "assest_details_tile": "Financial Review",
    "goals": "Financial Review",
    "account_details": "Financial Review",
    "expected_inflows_and_contributions": "Financial Review",
    "future_inflow_details": "Financial Review",
    "entity_affiliation": "About the Client",
    "financial_and_retirement_info": "About the Client"
}


# Data mapping
data_mapping = {
    "assest_details_tile": assest_details_tile,
    "goals": goals,
    "account_details": account_details,
    "expected_inflows_and_contributions": expected_inflows_and_contributions,
    "future_inflow_details": future_inflow_details,
    "entity_affiliation": entity_affiliation,
    "financial_and_retirement_info" : financial_and_retirement_info
}


# Construct the response and print
component_fixed = construct_component_fixed(llm_output)
print(json.dumps(component_fixed, indent=4))
