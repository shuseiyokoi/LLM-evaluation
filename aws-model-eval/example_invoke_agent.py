#!/usr/bin/env python3
import sys
import boto3
import json
import uuid

def main():
    if len(sys.argv) < 2:
        print("Usage: python invoke_bedrock_agent.py '<prompt>'")
        sys.exit(1)
    
    prompt = sys.argv[1]
    
    # Your agent configuration
    AGENT_ID = "your-agent-id"  # Replace with your actual agent ID
    AGENT_ALIAS_ID = "your-agent-alias-id"  # Replace with your actual agent alias ID
    
    # Use bedrock-agent-runtime client (not bedrock-runtime)
    bedrock_agent_runtime = boto3.client('bedrock-agent-runtime')
    session_id = str(uuid.uuid4())
    
    try:
        response = bedrock_agent_runtime.invoke_agent(
            agentId=AGENT_ID,
            agentAliasId=AGENT_ALIAS_ID,
            sessionId=session_id,
            inputText=prompt
        )
        
        result = ""
        for event in response['completion']:
            if 'chunk' in event:
                chunk = event['chunk']
                if 'bytes' in chunk:
                    result += chunk['bytes'].decode('utf-8')
        
        print(result)
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()