def populate_sub_category(sub_category_data, append_component):
    from data_config import (
        assest_details_tile,
        goals,
        account_details,
        expected_inflows_and_contributions,
        future_inflow_details,
        entity_affiliation,
    )

    sub_category_name = sub_category_data["subCategoryName"]

    if sub_category_name == "Wealth Plan current scenario":
        if assest_details_tile:
            append_component(
                sub_category_data,
                "tile",
                "asset_details",
                "Summaries",
                assest_details_tile,
            )
        if goals:
            append_component(
                sub_category_data,
                "tile_list",
                "goals",
                "Goals",
                goals,
            )

    elif sub_category_name == "Net Worth" and account_details:
        append_component(
            sub_category_data,
            "table",
            "account_details",
            "Summaries",
            account_details,
        )

    elif sub_category_name == "Wealth plan future inflows":
        if expected_inflows_and_contributions:
            append_component(
                sub_category_data,
                "tile",
                "expected inflows and contributions",
                "Summaries",
                expected_inflows_and_contributions,
            )
        if future_inflow_details:
            append_component(
                sub_category_data,
                "table",
                "future inflow details",
                "Tables",
                future_inflow_details,
            )

    elif sub_category_name == "Entity Affiliation" and entity_affiliation:
        append_component(
            sub_category_data,
            "table",
            "entity_affiliation",
            "Tables",
            entity_affiliation,
        )
