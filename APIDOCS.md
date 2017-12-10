# gene_suggest/{query}

Return a list of suggested gene names for the given query.

`{query}` is a partial query as input by the user, e.g. `brc`

## Endpoint definition

`gene_suggest/{query}`

## HTTP method

`GET`

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| species | *Optional*. The name of the target species, e.g. `homo_sapiens`. Defaults to all species. | string |
| limit | *Optional*. The maximum number of suggestions to return, e.g. 10. Defaults to all results. | integer |

## Sample request

```
curl --get --include 'http://localhost:5000/gene_suggest/query?species=homo_sapiens'
```

## Sample response

```json
{
    "gene_suggest": ["BRCA1", "BRCA2", "BRCC3", "BRCC3P1"]
}
```

The following table describes each item in the response.

|Response item | Description |
|----------|------------|
| **gene_suggest** | List of suggested gene names |

## Error and status codes

The following table lists the status and error codes related to this request.

| Status code | Meaning |
|--------|----------|
| 200 | Successful response |

