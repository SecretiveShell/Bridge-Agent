# Bridge-Agent

Bridge agent is an agentic framework based on [MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge).

## Usage

You must point the framework at MCP-Bridge. Here is an example `config.json`:

```json
{
    "openai_api_key": "none",
    "openai_base_url": "http://localhost:9090/v1",
    "openai_model": "gpt-4o-mini"
}
```

## workflow example

submit a json workflow to the `/execute` endpoint

```json
{
  "nodes": [
    {
      "id": "start_1",
      "type": "StartNode",
      "output": "node_fetch"
    },
    {
      "id": "node_fetch",
      "type": "GenericNode",
      "input": "start_1",
      "output": "node_check_response",
      "action": "fetch example.com"
    },
    {
      "id": "node_check_response",
      "type": "ConditionalNode",
      "input": "node_fetch",
      "condition": "Did the call complete successfully",
      "outputs": [
        {
          "value": "true",
          "output": "node_summarize"
        },
        {
          "value": "false",
          "output": "node_error"
        }
      ]
    },
    {
      "id": "node_summarize",
      "type": "GenericNode",
      "input": "node_check_response",
      "output": "end_success",
      "action": "summarize_content",
      "parameters": {
        "content": "response.body"
      }
    },
    {
      "id": "node_error",
      "type": "GenericNode",
      "input": "node_check_response",
      "output": "end_failure",
      "action": "explain_error",
      "parameters": {
        "error_code": "response.error_code",
        "error_message": "response.error_message"
      }
    },
    {
      "id": "end_success",
      "type": "EndNode",
      "input": "node_summarize"
    },
    {
      "id": "end_failure",
      "type": "EndNode",
      "input": "node_error"
    }
  ]
}
```

the result is
```json
{
  "output": "The content from example.com is about an \"Example Domain\" that is used for illustrative purposes in documents. It states that this domain can be used in literature without prior coordination or permission.",
  "chat_history": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Please execute the following action: fetch example.com\n\nUse tools if available, and if not use your best judgement/common sense."
    },
    {
      "role": "assistant",
      "content": "I successfully fetched the content from [example.com](http://example.com). Here it is:\n\n# Example Domain\n\nThis domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.\n\nMore information..."
    },
    {
      "role": "user",
      "content": "Please evaluate the following condition: Did the call complete successfully. The output should be one of the following options:\n- true\n- false\nDo not include any other text."
    },
    {
      "role": "assistant",
      "content": "true"
    },
    {
      "role": "user",
      "content": "Please execute the following action: summarize_content\n\nUse tools if available, and if not use your best judgement/common sense."
    },
    {
      "role": "assistant",
      "content": "The content from example.com is about an \"Example Domain\" that is used for illustrative purposes in documents. It states that this domain can be used in literature without prior coordination or permission."
    }
  ]
}
```