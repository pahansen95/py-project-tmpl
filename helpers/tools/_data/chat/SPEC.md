# LLM Provider Configuration Specification

**Version**: 1.2  
**Last Updated**: 2025-06-11

## Overview

This specification defines a standardized configuration structure for Large Language Model providers. It supports multiple providers through a consistent map-based data model compatible with TOML, YAML, JSON, and similar formats.

## Configuration Schema

### Provider Configuration

```
provider:                          # Root configuration map
  name: string                     # Required: Provider identifier
  api_key: string                  # Required: Authentication key (supports variables)
  default_model: string            # Optional: Default model selection
  
  connection:                      # Required: Network configuration
    base_url: string              # Required: API endpoint (https:// or http://)
    headers: map[string, string]  # Optional: Non-auth headers
    
  opts:                           # Optional: Provider-specific options
    # Examples by provider:
    organization: string          # OpenAI: org-xxx format
    project: string               # OpenAI: proj-xxx format
    anthropic_version: string     # Anthropic: API version
    beta: list[string]           # Anthropic: Beta features
    api_version: string          # Azure: API version
    resource_name: string        # Azure: Resource identifier
    region: string               # AWS: Region code
    profile: string              # AWS: Profile name
    
  endpoints:                      # Required: API paths
    chat: string                  # Required: Chat completion path (starts with /)
    models: string                # Optional: Model listing path
    
  models: list[                   # Required: Available models
    name: string                  # Required: Internal identifier
    id: string                    # Required: Provider model ID
    capabilities: list[string]    # Required: ["oneshot"|"reasoning"], ["text", "image"]
    
    limits:                       # Required: Resource boundaries
      input_tokens: integer       # Range: [1, 10,000,000]
      output_tokens: integer      # Range: [1, 1,000,000]
      context_window: integer     # Range: [1, 10,000,000]
      rate_limit: integer         # Optional: RPM [1, 1,000,000]
      
    cost:                         # Required: Pricing per 1M tokens
      input: float                # Range: [0.0001, 10,000.00]
      output: float               # Range: [0.0001, 10,000.00]
      per_tokens: integer         # Fixed: 1000000
      currency: string            # Optional: ISO 4217 (default: USD)
      
    opts:                         # Optional: Model parameters
      temperature: float          # Range: [0.0, 2.0]
      top_p: float               # Range: [0.0, 1.0]
      max_output_tokens: integer  # Output length limit
      reasoning_effort: string    # For reasoning models
  ]

profiles: list[                   # Optional: Usage presets
  name: string                    # Required: Profile identifier
  description: string             # Optional: Purpose description
  model: string                   # Optional: Model override
  # Additional model opts...
]
```

## Variable Resolution

Variables enable dynamic values through `${source:path}` syntax in any string field.

**Sources:**
- `${env:NAME}` - Environment variables
- `${self:path.to.value}` - Internal references
- `${self:list[index]}` - Array access
- `\${literal}` - Escaped literal

**Resolution Order:**
1. Parse configuration structure
2. Resolve all `${env:...}` variables
3. Resolve all `${self:...}` references (error on cycles)

**Path Grammar:**
```
path     := segment (accessor)*
accessor := '.' segment | '[' index ']'
segment  := [a-zA-Z_][a-zA-Z0-9_]*
index    := [0-9]+
```

## Data Types

**String Types:**
- `api_key`: 1-512 chars, alphanumeric + `-_.`
- `base_url`: Valid URI with scheme, no trailing slash
- `currency`: ISO 4217 three-letter code

**Capabilities:**
- Model types (one required): `oneshot`, `reasoning`
- Functions (one+ required): `text`, `image`

**Standards:**
- Tokens: Provider-specific, costs per 1M
- Rates: Requests per minute, sliding window
- Time: ISO 8601 dates, RFC 3339 timestamps

## Error Types

- **ConfigParseError**: Invalid syntax
- **VariableResolutionError**: Undefined variable
- **CyclicReferenceError**: Circular reference
- **PathNotFoundError**: Invalid path
- **TypeMismatchError**: Wrong value type
- **ValidationError**: Constraint violation

## Configuration Layout

### Organization

1. Provider metadata
2. Connection settings  
3. Provider options
4. API endpoints
5. Models (by tier: flagship → specialized → budget → legacy)
6. Profiles (by use: default → quality → cost → specialized)

### Documentation

```
# Provider Configuration
# Version: X.Y
# Last Updated: YYYY-MM-DD

[section]
field = value  # Required|Optional: Description

# ===========================
# Section Name
# ===========================
```

### Formatting

- Logical grouping with consistent spacing
- Aligned values within sections
- Comments above or inline with fields
- Single blank lines between sections
- Double blank lines between major sections

## Format Syntax

### TOML
- Maps → `[table]` or `{inline = "table"}`
- Lists → `["array"]` or `[[array.of.tables]]`
- Comments → `#`
- Variables → `"${env:VAR}"` (quoted)

### YAML
- Maps → Indented key-value pairs
- Lists → Dash-prefixed items
- Comments → `#`
- Variables → Quoted or unquoted

### JSON
- Maps → `{"objects": {}}`
- Lists → `["arrays"]`
- Comments → Not supported (use JSON5)
- Variables → `"${env:VAR}"` (escape: `\\$`)

## Complete Example

```toml
# OpenAI Provider Configuration
# Version: 1.2
# Last Updated: 2025-06-11

[provider]
name = "OpenAI"
api_key = "${env:OPENAI_API_KEY}"
default_model = "gpt-4.1"

[provider.connection]
base_url = "https://api.openai.com/v1"

[provider.opts]
organization = "${env:OPENAI_ORG_ID}"     # Optional: org-xxx format
project = "${env:OPENAI_PROJECT_ID}"      # Optional: proj-xxx format

[provider.endpoints]
chat = "/chat/completions"
models = "/models"

# ===========================
# Latest Models
# ===========================

[[provider.models]]
name = "gpt-4.1"
id = "gpt-4.1"
capabilities = ["oneshot", "text", "image"]

[provider.models.limits]
input_tokens = 1_000_000
output_tokens = 32_768
context_window = 1_000_000
rate_limit = 5_000

[provider.models.cost]
input = 3.00
output = 12.00
per_tokens = 1_000_000

[provider.models.opts]
temperature = 1.0
max_output_tokens = 32_768


# ===========================
# Reasoning Models  
# ===========================

[[provider.models]]
name = "o3"
id = "o3"
capabilities = ["reasoning", "text"]

[provider.models.limits]
input_tokens = 200_000
output_tokens = 100_000
context_window = 200_000

[provider.models.cost]
input = 2.00
output = 8.00
per_tokens = 1_000_000

[provider.models.opts]
reasoning_effort = "medium"  # low, medium, high


# ===========================
# Usage Profiles
# ===========================

[[profiles]]
name = "budget"
description = "Cost-optimized for high-volume processing"
model = "gpt-4.1-nano"
temperature = 0.7
max_output_tokens = 2048

[[profiles]]
name = "reasoning"
description = "Analytical tasks requiring chain-of-thought"
model = "o3"
reasoning_effort = "high"
```