# API Documentation

## Endpoint: /api/total_items

- Method: GET
- Parameters:
    - start_date: [DATE] (required)
    - end_date: [DATE] (required)
    - department: [string] (required)
- Returns:
    - Integer: Total items sold in the marketing department during the specified period.

## Endpoint: /api/nth_most_total_item

- Method: GET
- Parameters:
    - item_by: [string] (required, options: "quantity" or "price")
    - start_date: [DATE] (required)
    - end_date: [DATE] (required)
    - n: [integer] (required)
- Returns:
    - String: The nth most sold item based on the quantity or price sold during the specified period.
