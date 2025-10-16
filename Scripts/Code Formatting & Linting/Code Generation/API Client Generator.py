#!/usr/bin/python3
# -*- coding: utf-8 -*-
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

"""
API Client Generator - Python Script for CotEditor

Generate Python API client code from API documentation or JSON.
"""

import sys
import json
import re


def generate_api_client(api_data, language="python"):
    """Generate API client code."""
    if language == "python":
        return generate_python_client(api_data)
    elif language == "javascript":
        return generate_javascript_client(api_data)
    else:
        return "Unsupported language"


def generate_python_client(api_data):
    """Generate Python API client."""
    client_code = []
    
    # Imports
    client_code.append("import requests")
    client_code.append("from typing import Dict, Any, Optional")
    client_code.append("")
    
    # Class definition
    client_code.append("class APIClient:")
    client_code.append("    def __init__(self, base_url: str, api_key: Optional[str] = None):")
    client_code.append("        self.base_url = base_url.rstrip('/')")
    client_code.append("        self.api_key = api_key")
    client_code.append("        self.session = requests.Session()")
    client_code.append("        ")
    client_code.append("        if api_key:")
    client_code.append("            self.session.headers.update({'Authorization': f'Bearer {api_key}'})")
    client_code.append("")
    
    # Generate methods
    if isinstance(api_data, dict):
        for endpoint, details in api_data.items():
            if isinstance(details, dict):
                method = details.get('method', 'GET').upper()
                path = details.get('path', endpoint)
                
                method_name = endpoint.replace('-', '_').replace('/', '_')
                
                client_code.append(f"    def {method_name}(self, **kwargs) -> Dict[str, Any]:")
                client_code.append(f"        \"\"\"{details.get('description', f'{method} {path}')}\"\"\"")
                client_code.append(f"        url = f'{{self.base_url}}{path}'")
                
                if method == 'GET':
                    client_code.append("        response = self.session.get(url, params=kwargs)")
                elif method == 'POST':
                    client_code.append("        response = self.session.post(url, json=kwargs)")
                elif method == 'PUT':
                    client_code.append("        response = self.session.put(url, json=kwargs)")
                elif method == 'DELETE':
                    client_code.append("        response = self.session.delete(url)")
                
                client_code.append("        response.raise_for_status()")
                client_code.append("        return response.json()")
                client_code.append("")
    
    return '\n'.join(client_code)


def generate_javascript_client(api_data):
    """Generate JavaScript API client."""
    client_code = []
    
    # Class definition
    client_code.append("class APIClient {")
    client_code.append("    constructor(baseURL, apiKey = null) {")
    client_code.append("        this.baseURL = baseURL.replace(/\\/$/, '');")
    client_code.append("        this.apiKey = apiKey;")
    client_code.append("        this.headers = {")
    client_code.append("            'Content-Type': 'application/json'")
    client_code.append("        };")
    client_code.append("        ")
    client_code.append("        if (apiKey) {")
    client_code.append("            this.headers['Authorization'] = `Bearer ${apiKey}`;")
    client_code.append("        }")
    client_code.append("    }")
    client_code.append("")
    
    # Generate methods
    if isinstance(api_data, dict):
        for endpoint, details in api_data.items():
            if isinstance(details, dict):
                method = details.get('method', 'GET').upper()
                path = details.get('path', endpoint)
                
                method_name = endpoint.replace('-', '_').replace('/', '_');
                
                client_code.append(f"    async {method_name}(params = {{}}) {{")
                client_code.append(f"        // {details.get('description', f'{method} {path}')}")
                client_code.append(f"        const url = `${{this.baseURL}}{path}`;")
                
                if method == 'GET':
                    client_code.append("        const response = await fetch(url + '?' + new URLSearchParams(params), {")
                    client_code.append("            method: 'GET',")
                    client_code.append("            headers: this.headers")
                    client_code.append("        });")
                elif method in ['POST', 'PUT']:
                    client_code.append(f"        const response = await fetch(url, {{")
                    client_code.append(f"            method: '{method}',")
                    client_code.append("            headers: this.headers,")
                    client_code.append("            body: JSON.stringify(params)")
                    client_code.append("        });")
                elif method == 'DELETE':
                    client_code.append("        const response = await fetch(url, {")
                    client_code.append("            method: 'DELETE',")
                    client_code.append("            headers: this.headers")
                    client_code.append("        });")
                
                client_code.append("        if (!response.ok) {")
                client_code.append("            throw new Error(`HTTP error! status: ${response.status}`);")
                client_code.append("        }")
                client_code.append("        return await response.json();")
                client_code.append("    }")
                client_code.append("")
    
    client_code.append("}")
    client_code.append("")
    client_code.append("export default APIClient;")
    
    return '\n'.join(client_code)


def parse_api_endpoints(text):
    """Parse API endpoints from text."""
    # This is a simplified parser - in reality, you'd want more sophisticated parsing
    endpoints = {}
    
    # Look for common API patterns
    url_pattern = r'(GET|POST|PUT|DELETE|PATCH)\s+([^\s]+)'
    matches = re.findall(url_pattern, text, re.IGNORECASE)
    
    for method, path in matches:
        endpoint_name = path.strip('/').replace('/', '_').replace('-', '_')
        endpoints[endpoint_name] = {
            'method': method.upper(),
            'path': path,
            'description': f'{method.upper()} {path}'
        }
    
    return endpoints


def main():
    in_text = sys.stdin.read()
    if in_text:
        try:
            # Try to parse as JSON first
            try:
                api_data = json.loads(in_text)
            except json.JSONDecodeError:
                # If not JSON, try to parse as API documentation
                api_data = parse_api_endpoints(in_text)
            
            # Generate Python client
            client_code = generate_api_client(api_data, "python")
            sys.stdout.write(client_code)
            
        except Exception as e:
            sys.stdout.write(f"Error: {e}")
    else:
        sys.stdout.write("No API data selected.")


if __name__ == "__main__":
    main()
