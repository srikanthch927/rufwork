# Sub-category configuration mapping
sub_category_config = {
    "Wealth Plan current scenario": [
        {
            "componentType": "tile",
            "ComponentName": "asset_details",
            "ComponentCategory": "Summaries",
            "ComponentDataKey": "assest_details_tile",
        },
        {
            "componentType": "tile_list",
            "ComponentName": "goals",
            "ComponentCategory": "Goals",
            "ComponentDataKey": "goals",
        },
    ],
    "Net Worth": [
        {
            "componentType": "table",
            "ComponentName": "account_details",
            "ComponentCategory": "Summaries",
            "ComponentDataKey": "account_details",
        },
    ],
    "Wealth plan future inflows": [
        {
            "componentType": "tile",
            "ComponentName": "expected inflows and contributions",
            "ComponentCategory": "Summaries",
            "ComponentDataKey": "expected_inflows_and_contributions",
        },
        {
            "componentType": "table",
            "ComponentName": "future inflow details",
            "ComponentCategory": "Tables",
            "ComponentDataKey": "future_inflow_details",
        },
    ],
    "Entity Affiliation": [
        {
            "componentType": "table",
            "ComponentName": "entity_affiliation",
            "ComponentCategory": "Tables",
            "ComponentDataKey": "entity_affiliation",
        },
    ],
    "Wealth Plan Family Information" : [
        {
            "componentType": "table",
            "ComponentName": "financial and retirement information",
            "ComponentCategory": "Summaries",
            "ComponentDataKey": "financial_and_retirement_info",
        },
    ],
}



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
