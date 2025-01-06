import json
from config import *





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

def append_unique_component(sub_category_data, component_type, name, category, data):
    """Appends a component to the sub-category data only if it doesn't already exist."""
    existing_components = [
        (comp["ComponentName"], comp["ComponentCategory"]) for comp in sub_category_data["components"]
    ]
    if (name, category) not in existing_components:
        sub_category_data["components"].append({
            "componentType": component_type,
            "ComponentName": name,
            "ComponentCategory": category,
            "ComponentData": data,
        })

def populate_sub_category_unique(data_item, sub_category_config, data_mapping, existing_sub_category):
    """Populates unique sub-category data without duplication."""
    try:
        sub_category_name = data_item.get("sub_category", "")
        if not sub_category_name:
            return None

        # Add Insights
        for insight in data_item.get("Insights", []):
            append_unique_component(
                existing_sub_category,
                "text",
                "model_insight",
                "Considerations",
                [{"displayText": insight.get("Insight", "")}] 
            )

        # Add Summaries
        for summary in data_item.get("summaries", []):
            append_unique_component(
                existing_sub_category,
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
                    append_unique_component(
                        existing_sub_category,
                        config_entry["componentType"],
                        config_entry["ComponentName"],
                        config_entry["ComponentCategory"],
                        component_data
                    )
        return existing_sub_category
    except Exception as e:
        print(f"Error populating sub-category '{data_item.get('sub_category', '')}': {e}")
        return None

def construct_component_fixed_unique(llm_output, sub_category_config, data_mapping, category_mapping):
    """Constructs the component_fixed dictionary without repeating subcategories or components."""
    try:
        component_fixed = {
            "eci": llm_output.get("eci", ""),
            "package_id": llm_output.get("package_id", ""),
            "agent": llm_output.get("agent", ""),
            "status_code": llm_output.get("status_code", 0),
            "categories": []
        }

        if llm_output["status_code"] == 200:
            # Handle plan_level_results and goal_level_results together
            for result in llm_output.get("plan_level_results", []) + llm_output.get("goal_level_results", []):
                category = find_or_create_category(
                    component_fixed["categories"],
                    result.get("category", "")
                )
                sub_category_name = result.get("sub_category", "")
                existing_sub_category = find_or_create_sub_category(category, sub_category_name)
                populate_sub_category_unique(result, sub_category_config, data_mapping, existing_sub_category)

            # Handle directly mapped data
            populate_directly_mapped_data(component_fixed["categories"], sub_category_config, data_mapping, category_mapping)

        return component_fixed
    except Exception as e:
        print(f"Error constructing component_fixed: {e}")
        return {"eci": "", "package_id": "", "agent": "", "status_code": 500, "categories": []}

# Main Function

def process_data(llm_output, input_list):
    if len(input_list) < 8:
        raise ValueError("input_list must contain at least 8 elements.")
    if not isinstance(input_list, list):
        raise TypeError("input_list must be a list.")
    if not llm_output:
        return {"eci": "", "package_id": "", "agent": "", "status_code": 500, "categories": []}
    # Rest of the logic
    if not llm_output.get("plan_level_results") and not llm_output.get("goal_level_results"):
        return {"status_code": 200, "categories": []}

    data_mapping = {
        "assest_details_tile": input_list[1],
        "goals": input_list[2],
        "account_details": input_list[3],
        "expected_inflows_and_contributions": input_list[4],
        "future_inflow_details": input_list[5],
        "entity_affiliation": input_list[6],
        "financial_and_retirement_info": input_list[7]
    }

    # sub_category_config = sub_category_config  # Example configuration
    # category_mapping = category_mapping      # Example category mapping

    return construct_component_fixed_unique(llm_output, sub_category_config, data_mapping, category_mapping)
