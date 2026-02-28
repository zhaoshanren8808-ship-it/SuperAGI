# Salesforce Toolkit

A toolkit for interacting with Salesforce's APIs for CRM operations.

## Features

- **Query Records**: Query records using SOQL-like syntax
- **Create Record**: Create new records in Salesforce
- **Update Record**: Update existing records
- **Search Records**: Search across multiple objects using SOSL

## Configuration

Required environment variables:
- `SALESFORCE_USERNAME`: Salesforce username
- `SALESFORCE_PASSWORD`: Salesforce password
- `SALESFORCE_SECURITY_TOKEN`: Security token
- `SALESFORCE_CONSUMER_KEY`: Connected app consumer key
- `SALESFORCE_CONSUMER_SECRET`: Connected app consumer secret

## Tools

### QueryRecordsTool
Query records from Salesforce.

**Parameters**:
- `object_name`: Object name (Account, Contact, Lead, etc.)
- `fields`: Comma-separated field names
- `where_clause`: Optional WHERE clause

### CreateRecordTool
Create a new record.

**Parameters**:
- `object_name`: Object name
- `record_data`: JSON string with field values

### UpdateRecordTool
Update an existing record.

**Parameters**:
- `object_name`: Object name
- `record_id`: Record ID
- `update_data`: JSON string with fields to update

### SearchRecordsTool
Search across multiple objects.

**Parameters**:
- `search_term`: Search term
- `object_names`: Comma-separated object names

## Dependencies

This toolkit requires the `simple-salesforce` library:
```bash
pip install simple-salesforce
```