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
}

# Data configurations for tiles, tables, and other data components
assest_details_tile = [{' Plan Assets': 0, 'Current Assets': 0, 'Future Assets': 0}]
goals = [
    {
        'Name': 'Retirement',
        'Target Amount': 6000.0,
        'Gap Amount': 0,
        'Start Year': 2025,
        'End Year': 2041,
        'Check In': 0,
        'Rank': 1,
        'Total Goals': 2,
    },
    {
        'Name': 'Excess capital',
        'Target Amount': 0,
        'Gap Amount': 0,
        'Start Year': 2024,
        'End Year': 2041,
        'Check In': 0,
        'Rank': 2147483647,
        'Total Goals': 2,
    },
]
account_details = [
    {'Name': 'Bank accounts', 'External': 0, 'JPMC': 60569.97, 'Total': 60569.97, 'flag_type': 'Assets'},
    {'Name': 'Investment accounts', 'External': 31648.15, 'JPMC': 74321.08, 'Total': 105969.23, 'flag_type': 'Assets'},
    {'Name': 'Other Assets', 'External': 74321.08, 'JPMC': 31648.15, 'Total': 105969.23, 'flag_type': 'Assets'},
    {'Name': 'Liabilities', 'External': 0, 'JPMC': 17411.98, 'Total': 17411.98, 'flag_type': 'Liabilities'},
]
expected_inflows_and_contributions = [
    {'Total Future Contributions Expected': 0, 'Total Future Inflows Expected': 0}
]
future_inflow_details = [
    {
        "inflow": "small business income",
        "start_year": 2022,
        "end_year": 2024,
        "expected_income": 120000.0,
    },
    {
        "inflow": "401(k)",
        "start_year": 2026,
        "end_year": 2043,
        "expected_income": 23000.0,
    },
]
entity_affiliation = [{"Entity Name": '', "Relationship": ''}]
