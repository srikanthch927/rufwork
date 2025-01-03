import json
from config import *
# Define llm_output
llm_output = {
    "eci": "0449828929",
    "package_id": "c8c2e71d",
    "agent": "WealthPlan v3.5 GPT",
    "status_code": 200,
    "plan_level_results": [
        # {
        #     "category": "Financial Review",
        #     "sub_category": "Net Worth",
        #     "summaries": [{
        #             "scenario": "advisor or client led plan",
        #             "summary": "summer'S plan was last updated on 2024-12-26 by the advisor V693181. a PDF was last generated on none.",
        #             "lrcc_valid": True
        #         }],
        #     "Insights": [
        #         {
        #             "scenario": "advisor or client led plan",
        #             "Insight": "REBECA'S plan was last updated on 2024-12-26 by the advisor V693181. a PDF was last generated on none.",
        #             "lrcc_valid": True
        #         }
        #     ]
        # },
        # {
        #     "category": "About the Client",
        #     "sub_category": "Personal Profile",
        #     "summaries": [
        #         {
        #             "scenario": "advisor or client led plan",
        #             "summary": "Nisha'S plan was last updated on 2024-12-26 by the advisor V693181. a PDF was last generated on none.",
        #             "lrcc_valid": True
        #         }
        #     ],
        #     "Insights": [
                
        #     ]
        # },
        {
           "category": "Financial Review",
            "sub_category": "Wealth plan future inflows",
            "summaries": [{
                    "scenario": "advisor or client led plan",
                    "summary": "in plan level",
                    "lrcc_valid": True
                }],
            "Insights": [
                
            ]
        }
    ],
    "goal_level_results": [
        {
           "category": "Financial Review",
            "sub_category": "Wealth plan future inflows",
            "summaries": [{
                    "scenario": "advisor or client led plan",
                    "summary": "in goal level",
                    "lrcc_valid": True
                }],
            "Insights": [
                
            ]
        }
    ]
}


entity_affiliation = [{"Entity Name": '', "Relationship": ''}] #table
                       
expected_inflows_and_contributions = [{'Total Future Contributions Expected' : 0, 'Total Future Inflows Expected': 0}] #tile
future_inflow_details =[ {
    "inflow":"small bussiness income",
    "start_year":2022,
    "end_year":2024,
    "expected_income":120000.0
},
{
    "inflow":"401(k)",
    "start_year":2026,
    "end_year":2043,
    "expected_income":23000.0
},
] #table
assest_details_tile = [{' Plan Assets': 0, 'Current Assets':0, 'Future Assets': 0}] #tile

goals =[{'Name': 'Retirement', 'Target Amount': 6000.0, 'Gap Amount':0, 'Star Year': 2025, 'End Year': 2041, 'Check In':0, 'Rank':1, 'Total Goals': 2},
         {'Name': 'Excess capital','Target Amount': 0, 'Gap Amount': 0, 'Start Year' : 2024, 'End Year': 2041, 'Check In' : 0,'Rank': 2147483647, 'Total Goals': 2}] #tile
         
         
account_details = [{'Name': 'Bank accounts', 'External':0, 'JPMC': 60569.97, 'Total':60569.97, 'flag_type': 'Assets'}, {'Name': 'Investment accounts', 'External': 31648.153899999998, 'JPMC': 74321.08,
          'Total': 105969.23389999999, 'flag type': 'Assets'}, {'Name': 'Other Assets', 'External': 74321.08, 'JPMC': 31648.153899999998,
            'Total': 105969.23389999999, 'flag type': 'Assets'}, {'Name': 'Liabilities', 'External': 0, 'JPMC': 17411.98, 'Total': 17411.98, 'flag_type': 'Liabilities'}]   #table                    


financial_and_retirement_info = [
    {
        "name" : "rebeca",
        "relationship" : "client"
    }
]


import json

# Helper Functions
def append_component(sub_category_data, component_type, name, category, data):
    """Appends a component to the sub-category data."""
    sub_category_data["components"].append({
        "componentType": component_type,
        "ComponentName": name,
        "ComponentCategory": category,
        "ComponentData": data,
    })

def find_or_create_category(categories, category_name):
    """Finds or creates a category in the categories list."""
    for cat in categories:
        if cat["categoryName"] == category_name:
            return cat
    new_category = {"categoryName": category_name, "subCategories": []}
    categories.append(new_category)
    return new_category

def find_or_create_sub_category(category, sub_category_name):
    """Finds or creates a sub-category within a category."""
    for sub_category in category["subCategories"]:
        if sub_category["subCategoryName"] == sub_category_name:
            return sub_category
    new_sub_category = {"subCategoryName": sub_category_name, "components": []}
    category["subCategories"].append(new_sub_category)
    return new_sub_category

def populate_directly_mapped_data(categories, sub_category_config, data_mapping, category_mapping):
    """Populates directly mapped data based on the sub-category configuration."""
    for sub_category_name, components in sub_category_config.items():
        for component in components:
            data_key = component["ComponentDataKey"]
            if data_key in data_mapping and data_mapping[data_key]:  # Only process non-empty lists
                try:
                    # Get the category name from the mapping
                    category_name = category_mapping.get(data_key, "Default Category")

                    # Find or create the category
                    category = find_or_create_category(categories, category_name)

                    # Find or create the sub-category
                    sub_category_data = find_or_create_sub_category(category, sub_category_name)

                    # Check if the component is already present in the sub-category to avoid duplication
                    existing_components = [comp["ComponentName"] for comp in sub_category_data["components"]]
                    if component["ComponentName"] not in existing_components:
                        append_component(
                            sub_category_data,
                            component["componentType"],
                            component["ComponentName"],
                            component["ComponentCategory"],
                            data_mapping[data_key]
                        )

                except Exception as e:
                    print(f"Error processing sub-category '{sub_category_name}' for data key '{data_key}': {e}")

def populate_sub_category(data_item, sub_category_config, data_mapping):
    """Populates sub-category data based on a data item and configuration."""
    try:
        sub_category_name = data_item.get("sub_category", "")
        sub_category_data = {
            "subCategoryName": sub_category_name,
            "components": []
        }

        # Add Insights
        for insight in data_item.get("Insights", []):
            append_component(
                sub_category_data,
                "text",
                "model_insight",
                "Considerations",
                [{"displayText": insight.get("Insight", "")}]
            )

        # Add Summaries
        for summary in data_item.get("summaries", []):
            append_component(
                sub_category_data,
                "text",
                "model_summary",
                "Summaries",
                [{"displayText": summary.get("summary", "")}]
            )

        # Populate sub-category components based on configuration
        if sub_category_name in sub_category_config:
            for config_entry in sub_category_config[sub_category_name]:
                component_data = data_mapping.get(config_entry["ComponentDataKey"], [])
                if component_data:
                    append_component(
                        sub_category_data,
                        config_entry["componentType"],
                        config_entry["ComponentName"],
                        config_entry["ComponentCategory"],
                        component_data
                    )
        return sub_category_data
    except Exception as e:
        print(f"Error populating sub-category '{data_item.get('sub_category', '')}': {e}")
        return None

def construct_component_fixed(llm_output):
    """Constructs the component_fixed dictionary based on llm_output."""
    try:
        component_fixed = {
            "eci": llm_output.get("eci", ""),
            "package_id": llm_output.get("package_id", ""),
            "agent": llm_output.get("agent", ""),
            "status_code": llm_output.get("status_code", 0),
            "categories": []
        }

        if llm_output["status_code"] == 200:
            # Handle plan_level_results
            for plan_result in llm_output.get("plan_level_results", []):
                category = find_or_create_category(
                    component_fixed["categories"], 
                    plan_result.get("category", "")
                )
                sub_category_data = populate_sub_category(plan_result, sub_category_config, data_mapping)
                if sub_category_data:
                    existing_sub_category = find_or_create_sub_category(category, sub_category_data["subCategoryName"])
                    existing_sub_category["components"].extend(sub_category_data["components"])

            # Handle goal_level_results
            for goal_result in llm_output.get("goal_level_results", []):
                category = find_or_create_category(
                    component_fixed["categories"], 
                    goal_result.get("category", "Goals")
                )
                sub_category_data = populate_sub_category(goal_result, sub_category_config, data_mapping)
                if sub_category_data:
                    existing_sub_category = find_or_create_sub_category(category, sub_category_data["subCategoryName"])
                    existing_sub_category["components"].extend(sub_category_data["components"])

            # Handle directly mapped data
            populate_directly_mapped_data(component_fixed["categories"], sub_category_config, data_mapping, category_mapping)

        return component_fixed
    except Exception as e:
        print(f"Error constructing component_fixed: {e}")
        return {"eci": "", "package_id": "", "agent": "", "status_code": 500, "categories": []}


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
