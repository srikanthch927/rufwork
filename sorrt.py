
from config import populate_sub_category

# Helper functions
def append_component(sub_category_data, component_type, name, category, data):
    sub_category_data["components"].append({
        "componentType": component_type,
        "ComponentName": name,
        "ComponentCategory": category,
        "ComponentData": data
    })

def find_or_create_category(categories, category_name):
    for cat in categories:
        if cat["categoryName"] == category_name:
            return cat
    new_category = {"categoryName": category_name, "subCategories": []}
    categories.append(new_category)
    return new_category

# Construct the component_fixed dictionary dynamically
component_fixed = {
    "eci": llm_output.get("eci", ""),
    "package_id": llm_output.get("package_id", ""),
    "agent": llm_output.get("agent", ""),
    "status_code": llm_output.get("status_code", 0),
    "categories": []
}

if llm_output["status_code"] == 200:
    for plan_result in llm_output.get("plan_level_results", []):
        category = find_or_create_category(component_fixed["categories"], plan_result.get("category", ""))
        sub_category_data = {
            "subCategoryName": plan_result.get("sub_category", ""),
            "components": []
        }

        # Add Insights
        for insight in plan_result.get("Insights", []):
            append_component(
                sub_category_data,
                "text",
                "model_insight",
                "Considerations",
                [{"displayText": insight.get("Insight", "")}]
            )

        # Add Summaries
        for summary in plan_result.get("summaries", []):
            append_component(
                sub_category_data,
                "text",
                "model_summary",
                "Summaries",
                [{"displayText": summary.get("summary", "")}]
            )

        # Populate sub-category components using config
        populate_sub_category(sub_category_data, append_component)

        # Append the subcategory to the category
        category["subCategories"].append(sub_category_data)

    print(json.dumps(component_fixed, indent=4))
